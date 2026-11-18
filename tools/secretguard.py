#!/usr/bin/env python3
"""secretguard -- a Claude Code PreToolUse hook: a Bash command that would
PRINT a secret file is refused, with a pointer to the safe way to get the value.

Why (board 450/010 row 6; first built in an estate child repo, homed here):
the exposures this answers came from an agent reading a whole config file to
get one value, which put every credential in it into the session transcript.
A masked reader existed, but it was optional, and a rule that relies on memory
had already failed twice. A hook does not rely on memory.

What it blocks: a printing verb (cat, head, tail, less, more, strings, xxd, od,
hexdump, awk, sed, grep, egrep, rg, tac, nl, bat, base64, jq, yq) whose stage
names a secret path, anywhere in that stage's text (so `ssh h 'sudo cat x'` and
`bash -c "cat x"` are judged too).

What it lets through, deliberately:
  - a read inside command substitution, `$(cat /run/secrets/x)`, which feeds a
    value to a program and does not print it;
  - output piped into a digest or a count (sha256sum, sha512sum, shasum, wc),
    which is how a secret is compared without being shown;
  - `grep`/`rg` with -c, -l or -q, and `sed -i`, which print no contents;
  - `ls`, `stat` and the like, which show names and modes, never contents;
  - heredoc bodies, which are data (a commit message, a file), not commands;
  - a stage that RUNS a configured masked reader (`reader:` below), judged on
    the stage's own program after `sudo`, `env`, `nice`, `VAR=x` and a Python
    interpreter, never on the reader's name appearing somewhere in the text.

What it blocks on a masked reader itself: a configured raw-value flag
(`reveal:` below) whose next stage displays or stores the value (`| cat`,
`| tee`, `| less`, ... REVEAL_SINKS) or whose stdout is redirected (`>`, `>&2`,
`>(...)`). The reader can see only that its stdout is a pipe; this hook can see
what the pipe feeds.

It is a pattern match on command text: a seatbelt, not a wall. A determined
`python -c "print(open(...).read())"` is not caught. The point is to stop the
reflex `cat`, which is what caused the exposures.

CONFIG. Secret paths come from config, never from paths typed into this file.
Three sources, merged: a small built-in set of universally secret shapes
(DEFAULTS), a user-level file, and a repo-level file.

  user   $SECRETGUARD_PATHS if set, else $CLAUDE_CONFIG_DIR/secretguard-paths
         (default ~/.claude/secretguard-paths), beside leakscan's term list.
  repo   .atelier/secret-paths in the hook's cwd or the nearest parent holding
         one (the payload's `cwd`, else the process's). Safe to commit: it names
         where secrets live, never what they are.

One entry per line; `#` starts a comment:

  /run/secrets/              ends in `/`: everything under that directory
  */stacks/*.env             has a `/`: matched against the whole path, or any
                             tail of it; `*` crosses `/` (fnmatch)
  forwarding.secret          no `/`: matched against the base name
  !.env.example              a leading `!` exempts what any include matched
  pointer: <text>            what the refusal tells the session to use instead
                             (the repo's beats the user's beats the default)
  reader: config-read.py     a masked reader: a stage running it is exempt
  reader: tool.py config show  ... exempt only with these words, in order
  reveal: --reveal           a reader flag that emits the raw value
  defaults: off              drop the built-in set (in either file)

Exit 0 with no output allows. A deny is the documented PreToolUse JSON
(`permissionDecision: deny`), which Claude Code honours in every permission
mode, bypass included. Never blocks on a malformed payload or a config it cannot
read. `--show [DIR]` prints the effective config for a directory; `--try CMD`
prints the verdict for one command (both for an adopter tuning a config).

Wiring (user-level `~/.claude/settings.json`, or a repo's `.claude/settings.json`):

    "hooks": {"PreToolUse": [{"matcher": "Bash", "hooks": [
        {"type": "command", "command": "/usr/bin/python3 -I <atelier>/tools/secretguard.py"}]}]}

Tests: tools/test_secretguard.py.
"""
from __future__ import annotations

import fnmatch
import json
import os
import re
import shlex
import sys

# Universally secret shapes. Kept small on purpose: a guard that blocks normal
# work gets switched off. Left out, and why:
#   *.pem             as often a public certificate as a private key
#   credentials.json  as often an index of where credentials live as the
#                     credentials themselves
#   *.p12, *.pfx      binary; printing them shows nothing usable
DEFAULTS = [
    ".env", ".env.*", "*.env",
    "!.env.example", "!.env.sample", "!.env.template", "!.env.dist", "!.env.defaults",
    "id_rsa", "id_dsa", "id_ecdsa", "id_ed25519",
    "*.key", "privkey*.pem", "*-key.pem", "*_key.pem",
    ".netrc", ".pgpass", ".git-credentials", ".aws/credentials",
    "/run/secrets/",
]
DEFAULT_POINTER = ("Read only the value you need, through a tool that masks "
                   "credentials, or pipe the value into sha256sum to compare it.")
REPO_FILE = os.path.join(".atelier", "secret-paths")

PRINT_VERB = re.compile(
    r"(?:^|[\s;&|('\"`])(cat|head|tail|less|more|strings|xxd|od|hexdump|awk|sed|"
    r"grep|egrep|rg|tac|nl|bat|base64|jq|yq)\b([^;&|]*)")
SAFE_SINKS = re.compile(r"\|\s*(sha256sum|sha512sum|shasum|wc)\b")
SUBST = re.compile(r"\$\([^()]*\)")
# Splits a command into pipeline stages and command-list members. `|&` and a
# newline count; `||` is one separator, not two pipes.
SEGMENT = re.compile(r"\|\||\|&?|&&|;|\n")
# Characters that end a path inside a stage's text.
PATH_SPLIT = re.compile(r"[\s'\"`;|&()<>=,:]+")
HEREDOC = re.compile(r"(?<!<)<<(?!<)-?\s*(['\"]?)([A-Za-z_][A-Za-z0-9_]*)\1")

# Programs that, as the stage after a reveal flag, show or store the raw value.
# A seatbelt list, not a proof: anything not here is a consumer the reader trusts.
REVEAL_SINKS = {"cat", "tee", "less", "more", "most", "head", "tail", "xxd", "od", "hexdump", "strings",
                "awk", "gawk", "sed", "grep", "egrep", "tr", "cut", "rev", "fold", "nl", "base64", "base32",
                "xargs", "echo", "printf", "sh", "bash", "zsh", "dash", "column", "paste", "sort", "uniq",
                "jq", "yq", "diff", "cmp", "dd", "pbcopy", "xclip", "xsel", "logger", "script", "vim", "vi",
                "nano", "view", "bat", "nc", "curl", "wget"}
# A stdout redirect inside the reveal stage: `>`, `>>`, `1>`, `&>`, `>&2`, `>(...)`.
# (`2>` and `2>&1` move stderr only.)
STDOUT_REDIRECT = re.compile(r"(?:^|[^0-9])>|1>")
# Wrappers before the real program: `sudo -n`, `env A=b`, `nice -n 19`, `time`, ...
_WRAPPERS = {"sudo", "env", "nice", "time", "command", "exec", "nohup", "timeout", "ionice", "stdbuf"}
# The wrapper flags that take a separate argument (`sudo -n` does not; `sudo -u x` does).
_TAKES_ARG = {"sudo": {"-u", "-g", "-C", "-p", "-r", "-t", "-U", "-D", "-h"}, "nice": {"-n"},
              "ionice": {"-c", "-n", "-p"}, "timeout": {"-s", "-k"}, "env": {"-u", "-C"}}


class Config:
    def __init__(self):
        self.include: list[tuple[str, str]] = []   # (pattern, source)
        self.exclude: list[tuple[str, str]] = []
        self.readers: list[tuple[str, list[str]]] = []
        self.reveal: set[str] = set()
        self.pointer = DEFAULT_POINTER
        self.sources: list[str] = []


def _parse(path: str) -> dict | None:
    try:
        with open(path, encoding="utf-8") as f:
            text = f.read()
    except (OSError, UnicodeDecodeError):
        return None
    out = {"include": [], "exclude": [], "readers": [], "reveal": [], "pointer": None,
           "defaults": True}
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        key, sep, val = line.partition(":")
        key, val = key.strip().lower(), val.strip()
        if sep and key in ("pointer", "reader", "reveal", "defaults"):
            if key == "pointer" and val:
                out["pointer"] = val
            elif key == "reader" and val:
                words = val.split()
                out["readers"].append((words[0], words[1:]))
            elif key == "reveal" and val:
                out["reveal"].extend(val.split())
            elif key == "defaults":
                out["defaults"] = val.lower() not in ("off", "no", "false", "0")
            continue
        line = line.split(" #", 1)[0].strip()
        if line.startswith("!"):
            out["exclude"].append(line[1:].strip())
        else:
            out["include"].append(line)
    return out


def user_file() -> str:
    explicit = os.environ.get("SECRETGUARD_PATHS")
    if explicit:
        return os.path.expanduser(explicit)
    base = os.environ.get("CLAUDE_CONFIG_DIR") or os.path.expanduser("~/.claude")
    return os.path.join(base, "secretguard-paths")


def repo_file(start: str) -> str | None:
    d = os.path.abspath(start)
    while True:
        p = os.path.join(d, REPO_FILE)
        if os.path.isfile(p):
            return p
        parent = os.path.dirname(d)
        if parent == d:
            return None
        d = parent


def load(cwd: str) -> Config:
    cfg = Config()
    parsed = []
    for label, path in (("user", user_file()), ("repo", repo_file(cwd))):
        got = _parse(path) if path else None
        if got is not None:
            parsed.append((f"{label} {path}", got))
    if all(p["defaults"] for _, p in parsed):
        for pat in DEFAULTS:
            (cfg.exclude if pat.startswith("!") else cfg.include).append(
                (pat.lstrip("!"), "built-in default"))
        cfg.sources.append("built-in defaults")
    for src, p in parsed:          # user first, then repo: the repo's pointer wins
        cfg.include += [(x, src) for x in p["include"]]
        cfg.exclude += [(x, src) for x in p["exclude"]]
        cfg.readers += p["readers"]
        cfg.reveal.update(p["reveal"])
        if p["pointer"]:
            cfg.pointer = p["pointer"]
        cfg.sources.append(src)
    return cfg


def _matches(token: str, pattern: str) -> bool:
    if pattern.endswith("/"):
        pattern += "*"
    if "/" not in pattern:
        base = token.rstrip("/").rsplit("/", 1)[-1]
        return fnmatch.fnmatchcase(base, pattern)
    return (fnmatch.fnmatchcase(token, pattern)
            or fnmatch.fnmatchcase(token, "*/" + pattern.lstrip("/")))


def secret_in(text: str, cfg: Config) -> tuple[str, str, str] | None:
    """(path, pattern, source) for the first secret path named in text, else None."""
    for token in PATH_SPLIT.split(text):
        if not token or token[0] in "-!":   # a flag, or a negated glob (`--glob '!*.env'`)
            continue
        hit = next(((p, s) for p, s in cfg.include if _matches(token, p)), None)
        if hit and not any(_matches(token, p) for p, _ in cfg.exclude):
            return token, hit[0], hit[1]
    return None


def strip_heredocs(cmd: str) -> str:
    """Drop heredoc bodies: their text is data, not commands."""
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


def program(segment: str) -> str:
    """The base name of the program a stage runs: past `VAR=x`, wrappers and
    their flags, and a Python interpreter (`python3 -I tools/x.py` -> `x.py`)."""
    try:
        words = shlex.split(segment, comments=False)
    except ValueError:
        words = segment.split()
    i, n = 0, len(words)
    while i < n:
        w = words[i]
        base = os.path.basename(w)
        if re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*=.*", w):
            i += 1
        elif base in _WRAPPERS:
            i += 1
            while i < n and (words[i].startswith("-") or re.fullmatch(r"\d+(?:\.\d+)?[smhd]?", words[i])
                             or re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*=.*", words[i])):
                i += 2 if words[i] in _TAKES_ARG.get(base, ()) else 1
        elif re.fullmatch(r"python[0-9.]*", base):
            i += 1
            while i < n and words[i].startswith("-"):
                if words[i] in ("-c", "-m"):
                    return "python " + words[i]     # inline code or a module: not a file we know
                i += 2 if words[i] in ("-X", "-W") else 1
        else:
            return base
    return ""


def masked_reader(segment: str, cfg: Config) -> bool:
    p = program(segment)
    for name, words in cfg.readers:
        if p != name:
            continue
        if not words or re.search(r"\b" + r"\s+".join(map(re.escape, words)) + r"\b", segment):
            return True
    return False


def reveal_refusal(segments: list[str], cfg: Config) -> str | None:
    """A raw-value flag into a display or a file is printing it, pipe or no pipe."""
    if not cfg.reveal:
        return None
    for i, seg in enumerate(segments):
        flags = cfg.reveal.intersection(seg.split())
        if not flags or not masked_reader(seg, cfg):
            continue
        flag = sorted(flags)[0]
        if STDOUT_REDIRECT.search(seg):
            return (f"Refused: `{flag}` with stdout redirected writes or shows the raw value. "
                    "Pipe it into its consumer, or into sha256sum to compare it.")
        nxt = program(segments[i + 1].lstrip("&")) if i + 1 < len(segments) else ""
        if nxt in REVEAL_SINKS:
            return (f"Refused: `{flag} | {nxt}` prints or stores the raw value; the reader "
                    "cannot see where its pipe goes, so this hook does. Pipe it into its "
                    "consumer, or into sha256sum to compare it.")
    return None


def verdict(cmd: str, cfg: Config) -> str | None:
    """Return a refusal reason, or None to allow."""
    cmd = strip_heredocs(cmd)
    # A read fed to a program inside $( ) does not print; remove those spans
    # before judging what remains.
    rest = SUBST.sub(" ", cmd)
    segments = SEGMENT.split(rest)
    why = reveal_refusal(segments, cfg)
    if why or not secret_in(rest, cfg):
        return why
    for segment in segments:
        if masked_reader(segment, cfg):
            continue        # the stage RUNS the masked reader; its arguments are paths, not output
        m = PRINT_VERB.search(segment)
        hit = secret_in(segment, cfg) if m else None
        if not hit:
            continue
        verb, args = m.group(1), m.group(2)
        if verb in ("grep", "egrep", "rg") and re.search(r"\s-[a-zA-Z]*[clq]", " " + args):
            continue
        if verb == "sed" and re.search(r"(?:^|\s)(?:-[a-zA-Z]*i|--in-place)", args):
            continue
        # Piped onward into a digest or a count: judged on the whole command,
        # since the sink sits in a later segment.
        if SAFE_SINKS.search(rest):
            continue
        path, pattern, source = hit
        return (f"Refused: `{verb}` would print a secret file ({path} matches `{pattern}`, "
                f"{source}). {cfg.pointer} A path that is not secret is exempted with a "
                f"`!` line in {REPO_FILE}.")
    return None


def _cwd(data: dict) -> str:
    c = data.get("cwd")
    return c if isinstance(c, str) and os.path.isdir(c) else os.getcwd()


def main(argv: list[str]) -> int:
    if argv[:1] == ["--show"]:
        cfg = load(argv[1] if len(argv) > 1 else os.getcwd())
        print("sources: " + ("; ".join(cfg.sources) or "(none)"))
        for p, s in cfg.include:
            print(f"  secret  {p}    ({s})")
        for p, s in cfg.exclude:
            print(f"  exempt  {p}    ({s})")
        for name, words in cfg.readers:
            print(f"  reader  {' '.join([name, *words])}")
        if cfg.reveal:
            print(f"  reveal  {' '.join(sorted(cfg.reveal))}")
        print(f"pointer: {cfg.pointer}")
        return 0
    if argv[:1] == ["--try"]:
        why = verdict(" ".join(argv[1:]), load(os.getcwd()))
        print(why or "allowed")
        return 1 if why else 0
    try:
        data = json.load(sys.stdin)
        if not isinstance(data, dict):
            return 0
        if data.get("tool_name") not in (None, "Bash"):
            return 0
        cmd = (data.get("tool_input") or {}).get("command") or ""
        if not isinstance(cmd, str):
            return 0
        reason = verdict(cmd, load(_cwd(data)))
    except Exception:
        return 0  # never block on a payload or config we cannot read
    if reason:
        print(json.dumps({"hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": reason}}))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
