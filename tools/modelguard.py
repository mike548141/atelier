#!/usr/bin/env python3
"""modelguard -- a Claude Code PreToolUse hook: a net that catches a Claude
session or subagent started with no model named.

Why: ECONOMICS.md's standing rule is that the cheapest model that does a job
well is the one used for it, and the session picks that tier itself rather than
asking the principal. A start that names no model does not fail; it silently
inherits a tier (the parent session's, or the default), which is exactly the
choice the rule says must be made on purpose. Notes and memory did not stop
sessions leaving `model` out, so a machine check does.

Three routes start a model; two are guarded (a guard on the Agent tool alone
guards one tool, not the intent), and the third is named below as unseen:
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
`echo|printf ... | sh` (a wrapped shell too: `| sudo sh`, `| env bash`), text fed
to `at`/`batch`, a `function` body, `set -- claude ...; "$@"`, the code in
`git -c alias.x='!...'` and `git -c core.editor=...`, and the string literals of
`python3 -c`, `node -e`, `perl -e`, `ruby -e` and `osascript -e` (an argv list
`["claude", "-p", ...]`, or a command string; literals that are the arguments of
the language's own `print(` or `console.log(` are printed, not run, and are
skipped, but not those of a method of another object, `os.warn(`, or of a name
the script rebinds or aliases, `say = ...execSync`). A
variable set in the same command text is expanded in a command word
(`c=cl; ${c}aude -p x`), and a word whose literal part can only spell `claude`
(`${c}aude`) is read as `claude` when a session flag or a prompt follows it.
Also read, as running what follows: `screen` and `systemd-run` (their own
options skipped; `screen -S`, `-r`, `-x` take a session's name, alone or ending
a cluster, `-dmS claude`), `tmux new`, `new-window`, `split-window`,
`run-shell`, `if-shell` and `send-keys` (a value option such as `-s claude`,
or `-ds claude`, is a name, not a command; tmux's options end at the first
word that is not one, and every word after it is the command's), what
`echo` or `printf` prints into a shell through any pipeline (`echo ... | tee
log | sh`), into `bash <(...)`, `source <(...)`, or `sh -c "$(echo ...)"`, and
the literal command in an `awk` `system()` call or `| getline` pipe. What a
substitution's `echo` prints is read only where that substitution is the
script a shell runs, not wherever a later `-c` appears. A command nested past
the depth limit of four is denied unread when a word in it is the binary
(`claude`, a path ending `/claude`, `C=claude`); the letters inside another
word (`~/.claude/settings.json`) are not the binary.

After a head this file does not know (`psql`, `journalctl`, `docker logs`
...), a later `claude` word counts as a launch only when it looks like one: a
session flag follows it (`-p`, `-c`, `-r`, or a long flag only `claude` takes,
such as `--print`, `--resume`, `--permission-mode`), or a prompt does (an
argument holding a space). Where `claude` comes straight after a short option
(`-u claude`, `-it claude`, `su - claude`), it names a user, a unit or a
container, and only a long flag only `claude` takes makes it a launch. Not
after `screen` or `tmux`: there only a name option's value is a name, and a
`claude` anywhere else in the command they run is that command. The cost of
that, stated: an unknown wrapper given a short option just before the binary
(`somewrapper -q claude -p x`) passes, as does a bare `claude` last after an
unknown runner (`script -q /dev/null claude`, in tmux or not), and the
long-flag table is a snapshot of one CLI version, so a launch that carries
only a flag newer than it passes there too. What is still refused, and the
refusal says how to
rephrase: an unknown head with `claude` as a positional followed by a word like
`-c` or `-p` (`kubectl logs claude -c main`); putting `claude` last, after a
short option, or joined to a long option with `=` (`--name=claude`) passes.
Accepted false positives, because the guard denies where it cannot tell a name
from a binary: a long option's value as a separate word (`docker run --name
claude -p 8080:80 nginx`; `somewrapper --flag claude -p x` is the same shape,
and is a launch), a path ending in `claude` joined to a long option
(`--dir=/opt/claude 'some text'`), a quoted argument that reads as a command
(`somewrapper 'claude -p is a flag'`, though `say` and `logger` are data),
a literal argv in interpreter code outside a print call, a session named
`claude` given to `screen -d` or `-D`, whose name is optional (`screen -d
claude`; `screen -d -r claude` passes), and, past the depth limit, a path to
the binary that is only read (`ls ~/.local/bin/claude`).

What passes: a lookup of the binary (`command -v claude`, `which`, `type`,
`whence`, `hash`, `ls`/`stat`/`readlink` of its path) and every other command
whose arguments are data (`grep`, `echo`, `git`, `cat`, `pgrep` ...); a
`claude` naming a user, a unit, a container or a search term after an unknown
head, as above; the management subcommands (`claude mcp`, `claude --version`,
...); heredoc bodies that are data (a commit message, a file); comments.

What this hook does not see -- it is a net, not a proof:
  - a launch from inside a script or program (`python3 x.py`, a Makefile,
    `instruments/ccfleet`, a heredoc fed to `python3`): only the command text
    handed to Bash is read, so ccfleet always passes `--model` itself;
  - the harness's `Workflow` tool, the third route: it starts agents, but its
    input's schema is not read here, so a workflow script whose agents name no
    model passes;
  - a binary reached through a name it cannot resolve: an alias, a shell
    function defined outside this command text, a variable set outside it
    whose word has no literal part (`$X -p x`; a variable named like `CLAUDE`
    or `CLAUDE_BIN`, or set in the same command, is resolved, and `${c}aude`
    is read by its literal part);
  - whether the model named is the right one (it checks that one is named);
  - `ANTHROPIC_MODEL` already exported by the parent environment;
  - a session where the hook is not wired (it is the adopter's to switch on);
  - passes accepted because they cannot be judged from the command text (PK13):
    a long option joined to the binary (`nodemon --exec=claude -p x`, the same
    word as the `--name=claude` the advice gives); a command made by a program
    other than `echo` or `printf` and run by a shell (`sh -c "$(cat f)"`); a
    command awk builds in its own variables (`system(c " -p x")`); `sed 'e'`, as
    in `sed '1e claude -p x'`; a tmux key binding or hook that runs the binary
    (`tmux bind C-a run-shell claude`); a runner not named above whose own
    options this file does not know (`dtach` and `abduco` happen to be read as
    unknown heads and are denied).
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
import itertools, json, os, re, shlex, sys

# `claude --help`, v2.1.302: subcommands that start no model session.
SUBCOMMANDS = {
    "agents", "attach", "auth", "auto-mode", "doctor", "gateway", "import",
    "install", "logs", "mcp", "plugin", "plugins", "purge", "respawn", "rm",
    "setup-token", "stop", "kill", "ultrareview", "update", "upgrade",
}
NO_SESSION_FLAGS = {"-h", "--help", "-v", "--version"}
SESSION_FLAGS = {"-p", "--print", "-c", "--continue", "-r", "--resume", "--bg"}
SHORT_SESSION_FLAGS = {"-p", "-c", "-r"}
# `claude --help`, v2.1.302, saved whole as tools/fixtures/claude-help-2.1.302.txt:
# its long flags no common tool shares. After a head this file does not know,
# one of these after a `claude` word marks a launch even where `claude` is a
# short option's value (RK9). Every long flag in that help is here or in
# SHARED_LONG_FLAGS, and a test reads the saved help to hold it so (DP10).
CLAUDE_LONG_FLAGS = {
    "--print", "--continue", "--resume", "--bg", "--add-dir", "--agent",
    "--agents", "--allow-dangerously-skip-permissions", "--allowed-tools",
    "--allowedTools", "--append-system-prompt", "--dangerously-skip-permissions",
    "--disallowed-tools", "--disallowedTools", "--fallback-model",
    "--fork-session", "--from-pr", "--include-partial-messages",
    "--input-format", "--json-schema", "--max-budget-usd", "--mcp-config",
    "--no-session-persistence", "--output-format", "--permission-mode",
    "--permission-prompt-tool", "--plugin-dir", "--replay-user-messages",
    "--session-id", "--setting-sources", "--strict-mcp-config",
    "--system-prompt", "--teleport", "--remote-control",
    # PK13: in the v2.1.302 help, missing from the first cut of this table.
    "--settings", "--effort", "--background", "--worktree", "--tmux", "--bare",
    # DP10: the rest of the v2.1.302 help, `[-file]` forms written out.
    "--append-system-prompt-file", "--autocompact", "--ax-screen-reader",
    "--betas", "--cloud", "--disable-slash-commands",
    "--exclude-dynamic-system-prompt-sections", "--forward-subagent-text",
    "--include-hook-events", "--permission-prompts", "--plugin-url",
    "--prompt-suggestions", "--remote-control-session-name-prefix",
    "--restricted", "--safe-mode", "--system-prompt-file",
    "--system-prompt-snapshot", "--tools",
}
# Long flags in that help that other tools take too, so one after a `claude`
# that is a short option's value does not make it a launch (`--model` is read
# on its own; `--all` is a subcommand's).
SHARED_LONG_FLAGS = {
    "--help", "--version", "--verbose", "--debug", "--debug-file", "--name",
    "--file", "--model", "--environment", "--brief", "--desktop", "--ide",
    "--chrome", "--no-chrome", "--all",
}
# A short option cluster, or su's bare `-`: the word after it is its value.
SHORT_OPT = re.compile(r"-[A-Za-z]*")
# Interpreters whose code flag's text is read for a `claude` argv or command.
INTERPRETER = re.compile(r"(?:python[\d.]*|node|nodejs|deno|bun|perl|ruby|osascript)")
CODE_FLAGS = {"-c", "-e", "-E", "--eval", "-p", "--print"}
STRING_LIT = re.compile(r"""'((?:[^'\\]|\\.)*)'|"((?:[^"\\]|\\.)*)"|`([^`]*)`""")
# git configuration keys whose value git runs as a command.
GIT_CMD_KEYS = {"core.editor", "core.pager", "core.sshcommand", "sequence.editor",
                "diff.external", "gpg.program", "core.fsmonitor"}
AT_HEADS = {"at", "batch"}
CLAUDE_NAMES = {"claude", "claude-code"}
SHELLS = {"bash", "sh", "zsh", "dash", "ksh", "fish"}
# Words that precede a command and are skipped to reach it.
SKIP_KEYWORDS = {"if", "then", "else", "elif", "do", "while", "until", "!",
                 "{", "}", "coproc"}
# Segments headed by these hold no command of their own (`for x in a b`).
DATA_KEYWORDS = {"for", "case", "select", "done", "fi", "esac",
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
    # PK13: they print or speak their arguments and run none of them.
    "say", "logger", "wall", "notify-send", "terminal-notifier",
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
    # PK13: a multiplexer's or a service runner's own options, so the word
    # after them is the command it runs (`screen -dm claude -p x`).
    # `-r`, `-x` and `-ls` take a session's name and run nothing (DP9);
    # `-L` turns logging on and takes no value, `-Logfile` does.
    "screen": {"-S", "-t", "-c", "-e", "-p", "-h", "-T", "-s", "-Logfile",
               "-r", "-R", "-x", "-ls", "-list", "-wipe"},
    "systemd-run": {"-u", "--unit", "-p", "--property", "-E", "--setenv",
                    "--description", "--slice", "--uid", "--gid", "-M",
                    "--machine", "-H", "--host", "--working-directory",
                    "--service-type", "--on-active", "--on-calendar",
                    "--on-boot", "--on-startup", "--on-unit-active",
                    "--on-unit-inactive", "--timer-property"},
}
# Wrappers whose short options cluster as getopt reads them, so the value of
# `-dmS name` or `-ds name` is the word after the cluster (DP9).
CLUSTERED = {"screen"}
# tmux subcommands whose remaining words are a command to run, or keys typed
# into a pane (PK13). Options that take a value, so `-s claude` is a name.
TMUX_RUNS = {"new", "new-session", "neww", "new-window", "splitw",
             "split-window", "respawnw", "respawn-window", "respawnp",
             "respawn-pane", "run", "run-shell", "if", "if-shell", "popup",
             "display-popup", "pipep", "pipe-pane"}
TMUX_KEYS = {"send", "send-keys"}
# Their words are each a shell command (DP1); an `if-shell`'s second and third
# are tmux commands.
TMUX_SHELL = {"run", "run-shell", "if", "if-shell"}
TMUX_VALUED = {"-L", "-S", "-f", "-c", "-t", "-s", "-n", "-x", "-y", "-e",
               "-F", "-l", "-p", "-T", "-w"}
AWK_HEADS = {"awk", "gawk", "mawk", "nawk"}
# A string literal in awk program text that is a command: `system("x")`,
# `print | "x"`, `"x" | getline` (PK13).
_AWK_STR = r"""(?:"((?:[^"\\]|\\.)*)"|'((?:[^'\\]|\\.)*)')"""
AWK_CMD = re.compile(r"system\s*\(\s*" + _AWK_STR + r"|\|&?\s*" + _AWK_STR
                     + r"|" + _AWK_STR + r"\s*\|&?\s*getline")
# The calls whose string arguments are printed, not run (PK13b): a bare name,
# not an attribute of another object (`os.warn(`), or `console.log(` (DP21).
CONSOLE = r"console\.(?:log|info|warn|error|debug)"
PRINT_CALL = re.compile(
    r"(?<![\w.$])(" + CONSOLE + r"|print|printf|puts|say|warn|alert)\s*\(\s*$")
# What a process substitution leaves in its place: a path the shell reads.
PSUB = "/dev/fd/psub"
# What every substitution leaves beside it: a mark naming it, so the text its
# `echo` printed is read only where that substitution is what a shell runs,
# not wherever a later `-c` or `eval` appears (DP9).
SUB_MARK = re.compile(r"\x00(\d+)\x00")
_SUB_IDS = itertools.count()
# Positional words a wrapper takes before the command (`timeout 60 cmd`).
WRAPPER_POSITIONALS = {"timeout": 1, "gtimeout": 1, "taskset": 1, "chrt": 1,
                       "flock": 1}
PACKAGE_RUNNERS = {"npm": {"exec", "x"}, "pnpm": {"exec", "dlx"},
                   "yarn": {"exec", "dlx"}}
SEPARATORS = set(";&|()\n")
ASSIGN = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*=")
REDIRECT = re.compile(r"[<>&]+")
VAR_WORD = re.compile(r"\$\{?([A-Za-z_][A-Za-z0-9_]*)\}?")
VAR_IN = re.compile(r"\$\{([A-Za-z_][A-Za-z0-9_]*)\}|\$([A-Za-z_][A-Za-z0-9_]*)")
POSITIONAL_ALL = {"$@", "$*", "${@}", "${*}"}
POSITIONAL_ONE = re.compile(r"\$\{?([1-9])\}?")
# A word whose literal part could spell the binary, the rest unresolved.
FUZZY = "claude?"
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
    r"(?:\S*/)?(?:bash|sh|zsh|dash|ksh|at|batch)\b")
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
    Single-quoted text is literal and left alone. Each substitution leaves a
    mark in its place; `spans` pairs each mark's number with its text."""
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
            k = next(_SUB_IDS)
            spans.append((k, cmd[i + 1:j]))
            mark = "\x00%d\x00" % k
            out.append(" " + mark + " " if dq else " " + mark + " ; ")
            i = j + 1
            continue
        elif (c == "$" or (c in "<>" and not dq)) and cmd.startswith("(", i + 1):
            # `$( )`, and a process substitution `<( )` / `>( )` (PK13d).
            psub = c != "$"
            depth, j = 0, i + 1
            while j < n:
                if cmd[j] == "(":
                    depth += 1
                elif cmd[j] == ")":
                    depth -= 1
                    if depth == 0:
                        break
                j += 1
            k = next(_SUB_IDS)
            spans.append((k, cmd[i + 2:j]))
            mark = "\x00%d\x00" % k
            out.append(" " + PSUB + mark + " " if psub
                       else " " + mark + " " if dq else " " + mark + " ; ")
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
    def __init__(self, claude_vars, values=None):
        self.claude_vars = claude_vars
        self.values = values or {}  # NAME=value set in this command text
        self.exported_model = False
        self.positional = None  # `set -- ...`
        self.sub_texts = {}  # a substitution's mark: what its echo prints (PK13d)


def expand(word, ctx):
    """Expand the variables this command text sets; leave the rest."""
    return VAR_IN.sub(lambda m: ctx.values.get(m.group(1) or m.group(2), m.group(0)), word)


def fuzzy_claude(word):
    """True when an unresolved expansion plus the word's literal part can only
    be read as the binary (`${c}aude`, `cl${x}de`): the literal part is
    non-empty and fits `claude` with the expansions standing for any text."""
    parts = VAR_IN.split(word)
    lit = [parts[i] for i in range(0, len(parts), 3)]
    if len(lit) < 2 or not "".join(lit) or any("$" in p or "/" in p for p in lit):
        return False
    pat = ".*".join(re.escape(p) for p in lit)
    return any(re.fullmatch(pat, n) for n in CLAUDE_NAMES)


def command_name(word, ctx):
    m = VAR_WORD.fullmatch(word)
    if m:
        name = m.group(1)
        if name in ctx.claude_vars or CLAUDE_VAR.fullmatch(name):
            return "claude"
    if "$" in word:
        word = expand(word, ctx)
        if "$" in os.path.basename(word):
            return FUZZY if fuzzy_claude(os.path.basename(word)) else word
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


def launch_like(args, named=False):
    """Whether the words after a `claude` word read as a session start: a
    session flag, or a prompt (an argument holding a space). Where `claude` is
    a short option's value (`named`), only a long flag only `claude` takes
    counts (RK9)."""
    for a in args:
        if a in CLAUDE_LONG_FLAGS or a.split("=", 1)[0] in CLAUDE_LONG_FLAGS:
            return True
        if named:
            continue
        if a in SHORT_SESSION_FLAGS or (not a.startswith("-") and (" " in a or "\t" in a)):
            return True
    return False


def unwrap(words, ctx):
    """The command words past assignments and wrappers (`sudo sh` -> `sh`)."""
    words = list(words)
    for _ in range(8):
        while words and ASSIGN.match(words[0]):
            words.pop(0)
        if not words:
            break
        head = command_name(words[0], ctx)
        if head in WRAPPER_OPTS:
            words = skip_wrapper(head, words[1:])
        elif head == "command":
            words = strip_command_opts(words[1:]) or []
        else:
            break
    return words


def strip_command_opts(args):
    """`command`'s own leading options; None for a lookup (`-v`, `-V`)."""
    rest = list(args)
    while rest and rest[0].startswith("-") and rest[0] != "-":
        a = rest.pop(0)
        if a == "--":
            break
        if "v" in a[1:] or "V" in a[1:]:
            return None
    return rest


def string_literals(code):
    """Runs of comma-joined string literals in program text, each a (list,
    the program text before the run's first literal)."""
    runs, cur, end, first = [], [], None, 0
    for m in STRING_LIT.finditer(code):
        text = next(g for g in m.groups() if g is not None)
        if cur and re.fullmatch(r"\s*,\s*", code[end:m.start()]):
            cur.append(text)
        else:
            if cur:
                runs.append((cur, code[:first]))
            cur, first = [text], m.start()
        end = m.end()
    if cur:
        runs.append((cur, code[:first]))
    return runs


def print_call(code, before):
    """Whether a literal whose preceding program text is `before` is the
    argument of the language's own print call: `before` ends in one, and
    `code` never rebinds or aliases its name, every use of the name outside
    string literals being a call of it (`print = os.system`, `def say(c):`,
    `{ execSync: say }`, `import system as say` are not; DP21)."""
    m = PRINT_CALL.search(before)
    if not m:
        return False
    name = m.group(1)
    base = name.split(".")[0]
    bare = STRING_LIT.sub('""', code)
    for o in re.finditer(r"(?<![\w.$])" + re.escape(base) + r"(?![\w$])", bare):
        after, pre = bare[o.end():], bare[:o.start()]
        if base == "console":
            used = re.match(r"\s*\.\s*(?:log|info|warn|error|debug)\s*\(", after)
        else:
            used = re.match(r"\s*\(", after) and not re.search(
                r"\b(?:def|function|sub)\s+$", pre)
        if not used:
            return False
    return True


def interpreter_hit(args, ctx, depth):
    """A `claude` launch in `python3 -c`/`node -e` text: an argv list whose
    first item is the binary, or a string literal that is a command."""
    for i, a in enumerate(args[:-1]):
        if a not in CODE_FLAGS:
            continue
        for run, before in string_literals(args[i + 1]):
            if print_call(args[i + 1], before):
                continue  # `print('claude', 'x y')`: printed, not run (PK13b)
            if command_name(run[0], ctx) in CLAUDE_NAMES and len(run) > 1:
                hit = launch_hit(run[0], run[1:])
                if hit and launch_like(run[1:]):
                    return hit
            for lit in run:
                if " " in lit or "\t" in lit:
                    hit = offending(lit, depth + 1, ctx, loose=True)
                    if hit:
                        return hit
    return None


def git_hit(args, ctx, depth):
    """git's global `-c key=value` whose value git runs: `alias.x=!cmd`, or
    a key such as `core.editor`. Options after the subcommand are its own."""
    i = 0
    while i < len(args):
        a = args[i]
        if a in ("-c", "-C", "--git-dir", "--work-tree", "--namespace", "--config-env"):
            if a == "-c" and i + 1 < len(args):
                key, _, val = args[i + 1].partition("=")
                code = val[1:] if val.startswith("!") else (
                    val if key.lower() in GIT_CMD_KEYS or key.lower().startswith("pager.") else "")
                if code:
                    hit = offending(code, depth + 1, ctx)
                    if hit:
                        return hit
            i += 2
        elif a.startswith("-"):
            i += 1
        else:
            break
    return None


def takes_value(opt, vals, clustered=True):
    """Whether short option word `opt` leaves its value to the next word: it is
    a value-taking option, or (getopt) a cluster such as `-ds` whose first
    value-taking letter is its last, so `-dsw` carries its value itself."""
    if opt in vals:
        return True
    if not clustered or not re.fullmatch(r"-[A-Za-z]{2,}", opt):
        return False
    for k, ch in enumerate(opt[1:], 1):
        if "-" + ch in vals:
            return k == len(opt) - 1
    return False


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
            i += 2 if takes_value(a, vals, head in CLUSTERED) else 1
            continue
        if npos and command_name(a, Ctx(set())) not in CLAUDE_NAMES:
            npos -= 1
            i += 1
            continue
        break
    return args[i:]


def printed(args):
    """What `echo`/`printf` prints: its words past its own leading options
    (`-n`, `-e`), a dashed word after them kept (`claude --version`, DP9)."""
    i = 0
    while i < len(args) and args[i].startswith("-") and len(args[i]) > 1:
        i += 1
        if args[i - 1] == "--":
            break
    return " ".join(args[i:]).replace("\\n", "\n")


def echo_texts(body):
    """The text each `echo`/`printf` in `body` prints, as a list."""
    try:
        toks = tokens(body)
    except ValueError:
        return []
    out = []
    for seg, _sep in segments(toks):
        words = unwrap(seg, Ctx(set()))
        if words and command_name(words[0], Ctx(set())) in ("echo", "printf"):
            out.append(printed(words[1:]))
    return out


def read_texts(ctx, depth, words):
    """A launch in what a substitution printed, when a shell runs it (PK13d):
    only the substitutions whose marks stand in `words`, the script the shell
    is given, are read (DP9)."""
    for w in words:
        for k in SUB_MARK.findall(w):
            for text in ctx.sub_texts.get(int(k), []):
                hit = offending(text, depth + 1, ctx)
                if hit:
                    return hit
    return None


def unmark(text, ctx):
    """`text` with each substitution's mark replaced by what its echo printed."""
    return SUB_MARK.sub(lambda m: " ".join(ctx.sub_texts.get(int(m.group(1)), [])), text)


def tmux_hit(args, ctx, depth, model_set):
    """tmux: the words after `new`, `new-window`, `split-window`, `run-shell`
    and the like are a command; `send-keys` types text. A value-taking option
    (`-s claude`, or a cluster ending in one, `-ds claude`) names a session and
    is skipped. tmux's options end at the first word that is not one, or at
    `--`: every word after that is the command's, its own `-c` or `-p` too
    (DP1). False when the subcommand is not one of these, so the generic
    reading applies (PK13d)."""
    i = 0
    while i < len(args) and args[i].startswith("-") and args[i] != "--":
        i += 2 if takes_value(args[i], TMUX_VALUED) else 1
    if i >= len(args) or (args[i] not in TMUX_RUNS and args[i] not in TMUX_KEYS):
        return False
    sub, rest, j = args[i], args[i + 1:], 0
    while j < len(rest) and rest[j].startswith("-") and len(rest[j]) > 1:
        if rest[j] == "--":
            j += 1
            break
        j += 2 if takes_value(rest[j], TMUX_VALUED) else 1
    words = rest[j:]
    if not words:
        return None
    if sub in TMUX_KEYS:
        return offending(" ".join(words), depth + 1, ctx)
    if sub in TMUX_SHELL:
        # `run-shell 'cmd'`, `if-shell 'test' 'tmux-cmd' ['tmux-cmd']`
        for k, w in enumerate(words):
            hit = offending(w, depth + 1, ctx) or (
                k > 0 and sub in ("if", "if-shell") and offending("tmux " + w, depth + 1, ctx))
            if hit:
                return hit
        return None
    if len(words) == 1:
        return offending(words[0], depth + 1, ctx)
    return classify(words, ctx, depth, model_set)


def classify(words, ctx, depth, model_set=False, loose=False):
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
    if ctx.positional and (raw in POSITIONAL_ALL or POSITIONAL_ONE.fullmatch(raw)):
        # `set -- claude -p x; "$@"`: the positional parameters are the words.
        m = POSITIONAL_ONE.fullmatch(raw)
        sub = ctx.positional if not m else ctx.positional[int(m.group(1)) - 1:][:1]
        if sub:
            return classify(sub + args, ctx, depth, model_set)
    head = command_name(raw, ctx)
    if head == "function":
        # `function f { claude -p x; }`: the body is code.
        return classify([a for a in args[1:] if a not in ("(", ")")], ctx, depth, model_set)
    if head in DATA_KEYWORDS:
        return None
    if head == FUZZY:
        if model_set or ctx.exported_model or not launch_like(args):
            return None
        return launch_hit(raw, args)
    if head in CLAUDE_NAMES:
        if model_set or ctx.exported_model:
            return None
        if loose and not launch_like(args):
            return None
        return launch_hit(raw, args)
    if head in SHELLS or head in AT_HEADS or head in ("source", "."):
        for i, a in enumerate(args[:-1]):
            if a == "<<<":
                hit = offending(args[i + 1], depth + 1, ctx)
                if hit:
                    return hit
        psubs = [a for a in args if a.startswith(PSUB)]
        if psubs:
            # `bash <(echo 'claude -p x')`: what the substitution prints is
            # the script the shell runs (PK13d).
            hit = read_texts(ctx, depth, psubs)
            if hit:
                return hit
        if head in AT_HEADS or head in ("source", "."):
            return None
        ci = next((i for i, a in enumerate(args) if SHELL_C.fullmatch(a)), None)
        if ci is not None and ci + 1 < len(args):
            # `sh -c "$(echo claude -p x)"`: the script may be a substitution's
            # output, which is read here by what echo or printf prints.
            return (offending(args[ci + 1], depth + 1, ctx)
                    or read_texts(ctx, depth, args[ci + 1:ci + 2]))
        return None
    if head == "eval":
        return offending(" ".join(args), depth + 1, ctx) or read_texts(ctx, depth, args)
    if head in AWK_HEADS:
        for a in args:
            for m in AWK_CMD.finditer(a):
                lit = next((g for g in m.groups() if g is not None), "")
                if re.search(r"claude", lit):
                    hit = offending(lit, depth + 1, ctx)
                    if hit:
                        return hit
        return None
    if head == "tmux":
        hit = tmux_hit(args, ctx, depth, model_set)
        if hit is not False:
            return hit
    if head == "command":
        # Only `command`'s leading options are its own: `command claude -p x`
        # keeps the `-p` (RK15).
        rest = strip_command_opts(args)
        if rest is None:
            return None  # a lookup
        return classify(rest, ctx, depth, model_set)
    if head == "git":
        return git_hit(args, ctx, depth)
    if INTERPRETER.fullmatch(head):
        hit = interpreter_hit(args, ctx, depth)
        if hit:
            return hit
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
        if rest:
            return offending(" ".join(rest), depth + 1, ctx)
        return None
    if head in WRAPPER_OPTS:
        return classify(skip_wrapper(head, args), ctx, depth, model_set)
    if head in DATA_HEADS:
        return None
    # A head this file does not know: a later `claude` word counts when it
    # looks like a launch (a session flag or a prompt follows it), and an
    # argument holding a space is read as a command on the same terms (RK9).
    for i, a in enumerate(args):
        if command_name(a, ctx) in CLAUDE_NAMES and args[i + 1:]:
            if model_set or ctx.exported_model:
                return None
            named = i > 0 and SHORT_OPT.fullmatch(args[i - 1]) is not None
            if launch_like(args[i + 1:], named):
                hit = launch_hit(a, args[i + 1:])
                if hit:
                    return hit
        if " " in a or "\t" in a:
            hit = offending(a, depth + 1, ctx, loose=True)
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


def offending(cmd, depth=0, ctx=None, loose=False):
    """Return the first `claude` session launch with no model, else None."""
    if not cmd:
        return None
    if depth > MAX_DEPTH:
        # Past the depth this reads, a command that names the binary is denied
        # rather than passed unread (PK13d).
        if any(command_name(w, Ctx(set())) in (CLAUDE_NAMES | {FUZZY})
               for w in re.split(r"[\s;&|()<>`'\"=]+", cmd)):
            return "a command naming claude, nested past the depth limit"
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
        values = {t.split("=", 1)[0]: t.split("=", 1)[1] for t in toks
                  if ASSIGN.match(t) and "$" not in t.split("=", 1)[1]}
        ctx = Ctx({k for k, v in values.items()
                   if command_name(v, Ctx(set())) in CLAUDE_NAMES}, values)
    for k, body in spans:
        ctx.sub_texts[k] = echo_texts(body)
    for body in fed + [body for _k, body in spans]:
        hit = offending(body, depth + 1, ctx)
        if hit:
            return hit
    pipe_texts = []  # echo/printf text earlier in the same pipeline (PK13d)
    for seg, sep in segments(toks):
        hit = classify(seg, ctx, depth, loose=loose)
        if hit:
            return hit
        head = command_name(seg[0], ctx)
        piped = unwrap(seg, ctx)  # `| sudo sh`, `| env bash` (RK15)
        fhead = command_name(piped[0], ctx) if piped else None
        if sep not in ("|", "|&"):
            pipe_texts = []
        elif pipe_texts and (fhead in AT_HEADS or (
                fhead in SHELLS and not any(not a.startswith("-") for a in piped[1:]))):
            # `echo 'claude -p x' | tee log | sh`: any stage between is read as
            # passing the text on.
            for text in pipe_texts:
                hit = offending(text, depth + 1, ctx)
                if hit:
                    return hit
        if head in ("echo", "printf"):
            pipe_texts.append(unmark(printed(seg[1:]), ctx))
        if head in ("export", "declare", "typeset") and any(
                a.startswith("ANTHROPIC_MODEL=") and len(a) > len("ANTHROPIC_MODEL=")
                for a in seg[1:]):
            ctx.exported_model = True
        if head == "set":
            a = seg[1:]
            if "--" in a:
                ctx.positional = a[a.index("--") + 1:]
            elif a and not a[0].startswith(("-", "+")):
                ctx.positional = a
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
                 f"tier. Offending launch: `{hit}`. Add `--model <id>`. If no "
                 "session was meant (`claude` here names a user, a unit, a "
                 "container or a search term), rephrase so no session flag or "
                 "prompt follows that word: give it straight after a short "
                 "option (`-u claude`), joined to a long option with `=` "
                 "(`--name=claude`), or put it last. After `screen` or `tmux` "
                 "only a name option's value is a name (`screen -S claude`, "
                 "`tmux new -s claude`); anywhere else in the command they "
                 "run, `claude` is that command. " + RULE)
    sys.exit(0)


if __name__ == "__main__":
    main()
