#!/usr/bin/env python3
"""modelguard -- a Claude Code PreToolUse hook: a net that catches a Claude
session or subagent started with no model named.

Why: ECONOMICS.md's standing rule is that the cheapest model that does a job
well is the one used for it, and the session picks that tier itself rather than
asking the principal. A start that names no model does not fail; it silently
inherits a tier (the parent session's, or the default), which is exactly the
choice the rule says must be made on purpose. Notes and memory did not stop
sessions leaving `model` out, so a machine check does.

Two routes start a model, so both are guarded (a guard on the Agent tool alone
guards one tool, not the intent):
  - Agent tool (named `Task` on older harnesses): `model` must be set. A fork
    always inherits its parent's model and is exempt; no other subagent type is.
  - Bash: a `claude` word in command position that starts or resumes a session
    must carry `--model <id>` (or a non-empty `ANTHROPIC_MODEL=` set on that
    command, or exported earlier in the same command text).

Command position is found by skipping what runs the next word: assignments,
redirections, shell keywords (`if`, `do`, `!`, `{` ...), and wrappers (`env`,
`sudo -u x`, `timeout 60`, `nice -n 5`, `xargs -I{}`, `npx`, `find -exec` ...).
The text a shell will run as code is read too: `bash -c`/`-lc` strings,
`eval`, `$( )` and backticks, a heredoc or here-string fed to a shell, and
`echo|printf ... | sh`. After a head this file does not know, any later
`claude` word with arguments counts as a launch (the parse fails closed).

What passes: a lookup of the binary (`command -v claude`, `which`, `type`,
`whence`, `hash`, `ls`/`stat`/`readlink` of its path) and every other command
whose arguments are data (`grep`, `echo`, `git`, `cat`, `pgrep` ...); the
management subcommands (`claude mcp`, `claude --version`, ...); heredoc bodies
that are data (a commit message, a file); comments.

What this hook does not see -- it is a net, not a proof:
  - a launch from inside a script or program (`python3 x.py`, a Makefile,
    `instruments/ccfleet`): only the command text handed to Bash is read, so
    ccfleet always passes `--model` itself;
  - a binary reached through a name it cannot resolve: an alias, a shell
    function, a variable set outside this command text (a variable named like
    `CLAUDE` or `CLAUDE_BIN`, or set to `claude` in the same command, is
    resolved);
  - whether the model named is the right one (it checks that one is named);
  - `ANTHROPIC_MODEL` already exported by the parent environment;
  - a session where the hook is not wired (it is the adopter's to switch on).
Each bypass found is added to the deny table in tools/test_modelguard.py, so
the table grows with every shape this misses.

A malformed payload (not a JSON object, a tool_input that is not an object, a
command that is not text) is not a real tool call and never blocks: exit 0, no
output. A command that names `claude` and cannot be parsed at all is denied.
A block is a `permissionDecision: deny` with the reason, which the session
reads and fixes.

Wiring (user-level `~/.claude/settings.json`, or a repo's `.claude/settings.json`):

    "hooks": {"PreToolUse": [{"matcher": "Agent|Task|Bash", "hooks": [
        {"type": "command", "command": "<atelier>/tools/modelguard.py"}]}]}

Tests: tools/test_modelguard.py.
"""
import json, os, re, shlex, sys

# `claude --help`, v2.1.302: subcommands that start no model session.
SUBCOMMANDS = {
    "agents", "attach", "auth", "auto-mode", "doctor", "gateway", "import",
    "install", "logs", "mcp", "plugin", "plugins", "purge", "respawn", "rm",
    "setup-token", "stop", "kill", "ultrareview", "update", "upgrade",
}
NO_SESSION_FLAGS = {"-h", "--help", "-v", "--version"}
SESSION_FLAGS = {"-p", "--print", "-c", "--continue", "-r", "--resume", "--bg"}
CLAUDE_NAMES = {"claude", "claude-code"}
SHELLS = {"bash", "sh", "zsh", "dash", "ksh", "fish"}
# Words that precede a command and are skipped to reach it.
SKIP_KEYWORDS = {"if", "then", "else", "elif", "do", "while", "until", "!",
                 "{", "}", "coproc"}
# Segments headed by these hold no command of their own (`for x in a b`).
DATA_KEYWORDS = {"for", "case", "select", "function", "done", "fi", "esac",
                 "in", "[[", "]]"}
# Heads whose arguments are data: a `claude` among them is looked up, read,
# printed or searched for, never run. `command` is handled on its own.
DATA_HEADS = {
    "which", "type", "whence", "where", "hash", "ls", "ll", "stat", "file",
    "readlink", "realpath", "cat", "less", "more", "head", "tail", "bat",
    "grep", "egrep", "fgrep", "rg", "ag", "ack", "echo", "printf", "print",
    "git", "gh", "pgrep", "pkill", "killall", "kill", "ps", "lsof", "wc", "du",
    "df", "test", "[", "mkdir", "rmdir", "cp", "mv", "rm", "ln", "chmod",
    "chown", "touch", "tee", "sed", "awk", "jq", "yq", "cut", "sort", "uniq",
    "tr", "diff", "cmp", "brew", "pip", "pip3", "cd", "pushd", "popd", "unset",
    "alias", "unalias", "read", "local", "declare", "typeset", "readonly",
    "export", "set", "man", "basename", "dirname", "open", "code", "history",
    "shasum", "md5", "tar", "zip", "unzip", "curl", "wget", "mdfind", "true",
    "scp", "sftp", "rsync",
    "false", ":",
}
# Wrappers: run the rest of the words as the command. Value-taking options
# per wrapper, so `sudo -u name claude` reaches `claude`, not `name`.
WRAPPER_OPTS = {
    "env": {"-u", "-C", "-P", "--unset", "--chdir"},
    "nohup": set(), "exec": {"-a"}, "builtin": set(), "time": set(),
    "nice": {"-n"}, "caffeinate": {"-t", "-w"},
    "sudo": {"-u", "-g", "-C", "-D", "-h", "-p", "-r", "-t", "-U", "-T"},
    "doas": {"-u", "-C"},
    "xargs": {"-I", "-L", "-n", "-P", "-s", "-d", "-E", "-a", "-J", "-R", "-S"},
    "timeout": {"-s", "-k", "--signal", "--kill-after"},
    "gtimeout": {"-s", "-k", "--signal", "--kill-after"},
    "stdbuf": {"-i", "-o", "-e"}, "ionice": {"-c", "-n", "-p"},
    "taskset": {"-c"}, "chrt": set(), "setsid": set(), "unbuffer": set(),
    "watch": {"-n", "-d"}, "flock": {"-w", "-E"},
    "npx": {"-p", "--package"}, "bunx": {"-p", "--package"},
}
# Positional words a wrapper takes before the command (`timeout 60 cmd`).
WRAPPER_POSITIONALS = {"timeout": 1, "gtimeout": 1, "taskset": 1, "chrt": 1,
                       "flock": 1}
PACKAGE_RUNNERS = {"npm": {"exec", "x"}, "pnpm": {"exec", "dlx"},
                   "yarn": {"exec", "dlx"}}
SEPARATORS = set(";&|()\n")
ASSIGN = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*=")
REDIRECT = re.compile(r"[<>&]+")
VAR_WORD = re.compile(r"\$\{?([A-Za-z_][A-Za-z0-9_]*)\}?")
CLAUDE_VAR = re.compile(r"(?i)claude(_?(bin|cli|cmd|exe|path))?")
SHELL_C = re.compile(r"-[A-Za-z]*c[A-Za-z]*")
HEREDOC = re.compile(r"(?<!<)<<(?!<)-?\s*(['\"]?)([A-Za-z_][A-Za-z0-9_]*)\1")
ARITH = re.compile(r"\$?\(\((?:[^()]|\([^()]*\))*\)\)")
# `$(command -v claude)`, `$(which claude)`, `` `which claude` ``: the
# substitution yields the binary's path, so it stands for the binary.
LOOKUP_SUBST = re.compile(
    r"\$\(\s*(?:command\s+-v|which|type\s+-p|whence\s+-p)\s+claude\s*\)"
    r"|`\s*(?:command\s+-v|which|type\s+-p|whence\s+-p)\s+claude\s*`")
SHELL_FED = re.compile(
    r"(?:^|[;&|(])\s*(?:[A-Za-z_][A-Za-z0-9_]*=\S*\s+)*"
    r"(?:(?:sudo|env|nohup|exec|command|time|nice)\s+(?:-\S+\s+)*)*"
    r"(?:\S*/)?(?:bash|sh|zsh|dash|ksh)\b")
MAX_DEPTH = 4
PACKAGE_TAG = re.compile(r"(?:latest|next|beta|alpha|canary|stable|v?\d[\w.+-]*)")
# ssh's options that take a value: the word after them is data, not the
# destination (210/570). The first other word is the destination; the rest
# is the remote command, read as code.
SSH_OPTS = set("BbcDEeFIiJLlmOoPpQRSWw")


def deny(reason):
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "deny",
        "permissionDecisionReason": reason}}))
    sys.exit(0)


RULE = (
    "The standing rule (atelier ECONOMICS.md): pick the cheapest model that "
    "does THIS job well (a review runs on the tier the principal names), set "
    "it explicitly, state the tier in your reply, and never ask the principal "
    "which tier to use."
)


def strip_heredocs(cmd):
    """Drop heredoc bodies: their text is data (a commit message, a file),
    not commands, and may mention `claude -p` harmlessly. A body fed to a
    shell (`bash <<EOF`, `cat <<EOF | sh`) is code: it is returned to be read."""
    lines, out, code, i = cmd.split("\n"), [], [], 0
    while i < len(lines):
        line = lines[i]
        out.append(line)
        i += 1
        fed = bool(SHELL_FED.search(line))
        for _q, tag in HEREDOC.findall(line):
            body = []
            while i < len(lines) and lines[i].strip() != tag:
                body.append(lines[i])
                i += 1
            i += 1  # the terminator line
            if fed:
                code.append("\n".join(body))
    return "\n".join(out), code


def scan(cmd):
    """One quote-aware pass: drop comments (an unquoted `#` that starts a
    word, as the shell does, not shlex's `#` anywhere), and lift out command
    substitutions (`$( )`, backticks) to be read as commands of their own.
    Single-quoted text is literal and left alone."""
    out, spans, i, n, sq, dq = [], [], 0, len(cmd), False, False
    while i < n:
        c = cmd[i]
        if sq:
            out.append(c)
            sq = c != "'"
            i += 1
            continue
        if c == "\\" and i + 1 < n:
            out.append(cmd[i:i + 2])
            i += 2
            continue
        if c == "'" and not dq:
            sq = True
        elif c == '"':
            dq = not dq
        elif c == "#" and not dq and (i == 0 or cmd[i - 1] in " \t\n;&|()"):
            j = cmd.find("\n", i)
            i = n if j < 0 else j
            continue
        elif c == "`":
            j = cmd.find("`", i + 1)
            j = n if j < 0 else j
            spans.append(cmd[i + 1:j])
            out.append(" " if dq else " ; ")
            i = j + 1
            continue
        elif c == "$" and cmd.startswith("$(", i):
            depth, j = 0, i + 1
            while j < n:
                if cmd[j] == "(":
                    depth += 1
                elif cmd[j] == ")":
                    depth -= 1
                    if depth == 0:
                        break
                j += 1
            spans.append(cmd[i + 2:j])
            out.append(" " if dq else " ; ")
            i = j + 1
            continue
        out.append(c)
        i += 1
    return "".join(out), spans


def tokens(cmd):
    lex = shlex.shlex(cmd, posix=True, punctuation_chars=";&|()<>\n")
    lex.whitespace = " \t\r"
    lex.whitespace_split = True
    lex.commenters = ""
    return list(lex)


def segments(toks):
    """Yield (words, the separator before them)."""
    seg, sep = [], None
    for t in toks:
        if t and set(t) <= SEPARATORS:
            if seg:
                yield seg, sep
            seg, sep = [], t
        else:
            seg.append(t)
    if seg:
        yield seg, sep


class Ctx:
    def __init__(self, claude_vars):
        self.claude_vars = claude_vars
        self.exported_model = False


def command_name(word, ctx):
    m = VAR_WORD.fullmatch(word)
    if m:
        name = m.group(1)
        return "claude" if name in ctx.claude_vars or CLAUDE_VAR.fullmatch(name) else word
    base = os.path.basename(word)
    if not base.startswith("@") and "@" in base:
        name, _, tag = base.partition("@")
        # A package version or tag (claude@1.2, claude-code@latest) names the
        # binary; anything else after `@` is a login (claude@host: 210/570).
        if PACKAGE_TAG.fullmatch(tag):
            base = name
    return base


def has_model(args):
    for i, a in enumerate(args):
        if a.startswith("--model=") and len(a) > len("--model="):
            return True
        if a == "--model" and i + 1 < len(args) and args[i + 1] \
                and not args[i + 1].startswith("-"):
            return True
    return False


def launch_hit(head, args):
    """The launch text if `head args` starts a session with no model."""
    if any(a in NO_SESSION_FLAGS for a in args):
        return None
    session = any(a in SESSION_FLAGS or a.startswith("--resume=") for a in args)
    positionals = [a for a in args if not a.startswith("-")]
    if not session and any(p in SUBCOMMANDS for p in positionals[:2]):
        return None
    if has_model(args):
        return None
    return " ".join([head] + list(args))[:120]


def skip_wrapper(head, args):
    vals = WRAPPER_OPTS.get(head, set())
    npos = WRAPPER_POSITIONALS.get(head, 0)
    i = 0
    while i < len(args):
        a = args[i]
        if a == "--":
            i += 1
            break
        if a.startswith("-") and len(a) > 1:
            i += 2 if a in vals else 1
            continue
        if npos and command_name(a, Ctx(set())) not in CLAUDE_NAMES:
            npos -= 1
            i += 1
            continue
        break
    return args[i:]


def classify(words, ctx, depth, model_set=False):
    """The offending launch in one simple command, else None."""
    words = list(words)
    while words:
        w = words[0]
        if w in SKIP_KEYWORDS:
            words.pop(0)
        elif ASSIGN.match(w):
            if w.startswith("ANTHROPIC_MODEL=") and len(w) > len("ANTHROPIC_MODEL="):
                model_set = True
            words.pop(0)
        elif REDIRECT.fullmatch(w) or (w.isdigit() and len(words) > 1
                                       and REDIRECT.fullmatch(words[1])):
            words.pop(0)
            if words and REDIRECT.fullmatch(words[0]):
                words.pop(0)
            if words:
                words.pop(0)  # the redirection's target
        else:
            break
    if not words:
        return None
    raw, args = words[0], words[1:]
    head = command_name(raw, ctx)
    if head in DATA_KEYWORDS:
        return None
    if head in CLAUDE_NAMES:
        if model_set or ctx.exported_model:
            return None
        return launch_hit(raw, args)
    if head in SHELLS:
        for i, a in enumerate(args[:-1]):
            if a == "<<<":
                hit = offending(args[i + 1], depth + 1, ctx)
                if hit:
                    return hit
        ci = next((i for i, a in enumerate(args) if SHELL_C.fullmatch(a)), None)
        if ci is not None and ci + 1 < len(args):
            return offending(args[ci + 1], depth + 1, ctx)
        return None
    if head == "eval":
        return offending(" ".join(args), depth + 1, ctx)
    if head == "command":
        if any(a in ("-v", "-V") for a in args[:2]):
            return None  # a lookup
        return classify([a for a in args if a != "-p"], ctx, depth, model_set)
    if head == "find":
        for i, a in enumerate(args):
            if a in ("-exec", "-execdir", "-ok", "-okdir"):
                hit = classify(args[i + 1:], ctx, depth, model_set)
                if hit:
                    return hit
        return None
    if head in PACKAGE_RUNNERS:
        if args and args[0] in PACKAGE_RUNNERS[head]:
            return classify(skip_wrapper("npx", args[1:]), ctx, depth, model_set)
        return None
    if head in ("env",) and any(a in ("-S", "--split-string") for a in args):
        i = next(i for i, a in enumerate(args) if a in ("-S", "--split-string"))
        if i + 1 < len(args):
            return offending(" ".join(args[i + 1:]), depth + 1, ctx)
    if head in ("npx", "bunx") and any(a in ("-c", "--call") for a in args):
        i = next(i for i, a in enumerate(args) if a in ("-c", "--call"))
        if i + 1 < len(args):
            return offending(args[i + 1], depth + 1, ctx)
    if head in ("ssh", "autossh"):
        # The login and host are data (`claude@host`, `-l claude`); only the
        # remote command is code, so `ssh host claude -p` is still read.
        i = 0
        while i < len(args) and args[i].startswith("-") and args[i] != "--":
            flag = args[i]
            i += 1
            if len(flag) == 2 and flag[1] in SSH_OPTS:
                i += 1  # its value
        if i < len(args) and args[i] == "--":
            i += 1
        rest = args[i + 1:]  # past the destination
        if rest and depth < MAX_DEPTH:
            return offending(" ".join(rest), depth + 1, ctx)
        return None
    if head in WRAPPER_OPTS:
        return classify(skip_wrapper(head, args), ctx, depth, model_set)
    if head in DATA_HEADS:
        return None
    # A head this file does not know: fail closed on any later `claude`
    # word with arguments, and read any argument that looks like a command.
    for i, a in enumerate(args):
        if command_name(a, ctx) in CLAUDE_NAMES and args[i + 1:]:
            if model_set or ctx.exported_model:
                return None
            hit = launch_hit(a, args[i + 1:])
            if hit:
                return hit
        if (" " in a or "\t" in a) and depth < MAX_DEPTH:
            hit = offending(a, depth + 1, ctx)
            if hit:
                return hit
    return None


def coarse(cmd):
    """Unbalanced quoting: a coarse text check."""
    for m in re.finditer(r"(?:^|[\s;&|(`])claude(\s[^\n;&|]*)?", cmd):
        before = cmd[:m.start() + 1]
        if re.search(r"(?:which|type|whence|hash|command\s+-[vV]|ls)\s*$", before):
            continue
        args = m.group(1) or ""
        if re.search(r"(^|\s)(-p|--print|-c|--continue|-r|--resume|--bg)\b", args) \
                and not re.search(r"--model(=|\s+)[^\s-]", args):
            return m.group(0).strip()
    return None


def offending(cmd, depth=0, ctx=None):
    """Return the first `claude` session launch with no model, else None."""
    if depth > MAX_DEPTH or not cmd:
        return None
    cmd = cmd.replace("\\\n", " ")
    cmd = ARITH.sub(" 0 ", cmd)
    cmd, fed = strip_heredocs(cmd)
    cmd = LOOKUP_SUBST.sub("claude", cmd)
    cmd, spans = scan(cmd)
    try:
        toks = tokens(cmd)
    except ValueError:
        return coarse(cmd)
    if ctx is None:
        ctx = Ctx({t.split("=", 1)[0] for t in toks
                   if ASSIGN.match(t) and command_name(t.split("=", 1)[1], Ctx(set()))
                   in CLAUDE_NAMES})
    for body in fed + spans:
        hit = offending(body, depth + 1, ctx)
        if hit:
            return hit
    prev = None
    for seg, sep in segments(toks):
        hit = classify(seg, ctx, depth)
        if hit:
            return hit
        head = command_name(seg[0], ctx)
        if sep == "|" and prev and head in SHELLS \
                and not any(not a.startswith("-") for a in seg[1:]) \
                and command_name(prev[0], ctx) in ("echo", "printf"):
            text = " ".join(a for a in prev[1:] if not a.startswith("-"))
            hit = offending(text.replace("\\n", "\n"), depth + 1, ctx)
            if hit:
                return hit
        if head in ("export", "declare", "typeset") and any(
                a.startswith("ANTHROPIC_MODEL=") and len(a) > len("ANTHROPIC_MODEL=")
                for a in seg[1:]):
            ctx.exported_model = True
        prev = seg
    return None


def checked(cmd):
    """offending(), failing closed: a parse that breaks on a command naming
    `claude` is a deny, never a silent allow."""
    try:
        return offending(cmd)
    except Exception:
        return "an unparsable command naming claude" if re.search(r"\bclaude\b", cmd) else None


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        sys.exit(0)  # never block on a malformed payload
    if not isinstance(data, dict):
        sys.exit(0)
    tool = data.get("tool_name")
    ti = data.get("tool_input")
    if not isinstance(ti, dict):
        sys.exit(0)

    if tool in ("Agent", "Task"):
        if ti.get("subagent_type") == "fork" or ti.get("model"):
            sys.exit(0)
        deny(f"{tool} call blocked: no `model` set, so it would silently inherit "
             "this session's tier. " + RULE)

    if tool == "Bash":
        cmd = ti.get("command")
        if not isinstance(cmd, str):
            sys.exit(0)
        hit = checked(cmd)
        if hit:
            deny("Bash call blocked: it starts a Claude session with no "
                 "`--model`, so that session would silently run on the default "
                 f"tier. Offending launch: `{hit}`. Add `--model <id>`. " + RULE)
    sys.exit(0)


if __name__ == "__main__":
    main()
