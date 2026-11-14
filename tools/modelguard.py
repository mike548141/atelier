#!/usr/bin/env python3
"""modelguard -- a Claude Code PreToolUse hook: every Claude session or subagent
a session starts must name its model.

Why: ECONOMICS.md's standing rule is that the cheapest model that does a job
well is the one used for it, and the session picks that tier itself rather than
asking the principal. A start that names no model does not fail; it silently
inherits a tier (the parent session's, or the default), which is exactly the
choice the rule says must be made on purpose. Notes and memory did not stop
sessions leaving `model` out, so a machine check does.

Two routes start a model, so both are guarded (a guard on the Agent tool alone
guards one tool, not the intent):
  - Agent tool: `model` must be set. A fork always inherits its parent's
    model and is exempt.
  - Bash: any `claude` invocation that starts or resumes a session
    (`claude -p ...`, `claude "prompt"`, `claude -r id`, `--bg`) must carry
    `--model` (or `ANTHROPIC_MODEL=` in the same command). Management
    subcommands (`claude mcp`, `claude --version`, ...) start no model and
    pass. Heredoc bodies are data (a commit message, a file) and are skipped.

Known limit: a script that launches `claude` itself (a Python subprocess, or
`instruments/ccfleet`) is invisible here; only the command text the session
hands to Bash is read. ccfleet always passes `--model` for that reason.

Never blocks on a malformed payload (exit 0, no output). A block is a
`permissionDecision: deny` with the reason, which the session reads and fixes.

Wiring (user-level `~/.claude/settings.json`, or a repo's `.claude/settings.json`):

    "hooks": {"PreToolUse": [{"matcher": "Agent|Bash", "hooks": [
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
# Prefixes that run the next word as the command.
WRAPPERS = {"env", "nohup", "exec", "command", "time", "nice", "caffeinate",
            "sudo", "xargs", "builtin"}
SHELLS = {"bash", "sh", "zsh"}
SEPARATORS = set(";&|()\n")
ASSIGN = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*=")
HEREDOC = re.compile(r"(?<!<)<<(?!<)-?\s*(['\"]?)([A-Za-z_][A-Za-z0-9_]*)\1")


def deny(reason):
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "deny",
        "permissionDecisionReason": reason}}))
    sys.exit(0)


RULE = (
    "The standing rule (atelier ECONOMICS.md): pick the cheapest model that "
    "does THIS job well, set it explicitly, state the tier in your reply, and "
    "never ask the principal which tier to use. A review runs on the tier the "
    "principal names, and only with the approval that tier needs."
)


def strip_heredocs(cmd):
    """Drop heredoc bodies: their text is data (a commit message, a file),
    not commands, and may mention `claude -p` harmlessly."""
    lines, out, i = cmd.split("\n"), [], 0
    while i < len(lines):
        line = lines[i]
        out.append(line)
        i += 1
        for _q, tag in HEREDOC.findall(line):
            while i < len(lines) and lines[i].strip() != tag:
                i += 1
            i += 1  # the terminator line
    return "\n".join(out)


def tokens(cmd):
    lex = shlex.shlex(cmd, posix=True, punctuation_chars=";&|()<>\n")
    lex.whitespace = " \t\r"
    lex.whitespace_split = True
    return list(lex)


def segments(toks):
    seg = []
    for t in toks:
        if t and set(t) <= SEPARATORS:
            if seg:
                yield seg
            seg = []
        else:
            seg.append(t)
    if seg:
        yield seg


def offending(cmd, depth=0):
    """Return the first `claude` session launch with no model, else None."""
    cmd = strip_heredocs(cmd)
    if "ANTHROPIC_MODEL=" in cmd:
        return None
    try:
        toks = tokens(cmd)
    except ValueError:
        # Unbalanced quoting: fall back to a coarse text check.
        for m in re.finditer(r"(?:^|[\s;&|(`])claude(\s[^\n;&|]*)?", cmd):
            args = m.group(1) or ""
            if re.search(r"(^|\s)(-p|--print|-c|--continue|-r|--resume|--bg)\b", args) \
                    and "--model" not in args:
                return m.group(0).strip()
        return None
    for seg in segments(toks):
        words = list(seg)
        while words:
            w = words[0].lstrip("`$")
            if not w or ASSIGN.match(w):
                words.pop(0)
            elif w in WRAPPERS:
                words.pop(0)
                while words and (words[0].startswith("-") or ASSIGN.match(words[0])
                                 or words[0].isdigit()):
                    words.pop(0)
            else:
                break
        if not words:
            continue
        head = os.path.basename(words[0].lstrip("`$"))
        args = words[1:]
        if head in SHELLS and "-c" in args and depth < 3:
            i = args.index("-c")
            if i + 1 < len(args):
                hit = offending(args[i + 1], depth + 1)
                if hit:
                    return hit
            continue
        if head != "claude":
            continue
        if any(a in NO_SESSION_FLAGS for a in args):
            continue
        first = next((a for a in args if not a.startswith("-")), None)
        if first in SUBCOMMANDS:
            continue
        if any(a == "--model" or a.startswith("--model=") for a in args):
            continue
        return " ".join(words)[:120]
    return None



def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        sys.exit(0)  # never block on a malformed payload
    tool = data.get("tool_name")
    ti = data.get("tool_input") or {}

    if tool == "Agent":
        if ti.get("subagent_type") == "fork" or ti.get("model"):
            sys.exit(0)
        deny("Agent call blocked: no `model` set, so it would silently inherit "
             "this session's tier. " + RULE)

    if tool == "Bash":
        hit = offending(ti.get("command") or "")
        if hit:
            deny("Bash call blocked: it starts a Claude session with no "
                 "`--model`, so that session would silently run on the default "
                 f"tier. Offending launch: `{hit}`. Add `--model <id>`. " + RULE)
    sys.exit(0)


if __name__ == "__main__":
    main()
