#!/usr/bin/env python3
"""prefixhook -- say when a Claude Code skill or command sits outside `/atelier:`.

Why (board 450/010 row 3): the principal asked, 2026-11-18, for every one of
his customisations under one slash prefix "so that they are easy to find as a
group"; sessions had named skills "whatever name made sense to you at the
time". A plugin skill is always `/atelier:<name>`, so the rule is simply that a
skill or command is born in the atelier plugin (MECHANISMS.md § Where it lives
and what it is called). This hook is that rule's tripwire: it does not stop a
session from making one elsewhere, it makes the stray impossible to miss.

What counts as a stray:
  - an entry in the user-level skills dir (`~/.claude/skills/`) other than
    `atelier` (the bare menu, instruments/atelier-menu) and `synced` (skills
    the claude.ai account syncs down, which are not the principal's own);
  - any file in the user-level commands dir (`~/.claude/commands/`);
  - any entry in the repo's own `.claude/skills/` or `.claude/commands/`.

  prefixhook.py            SessionStart hook: reads the hook JSON on stdin,
                           prints one JSON object when there is a stray, else
                           nothing. Never blocks; always exits 0.
  prefixhook.py --check [DIR]   CLI: list strays for DIR (default cwd) and
                           exit 1 if any, 0 if none. For a health sweep.
  CLAUDE_CONFIG_DIR        the user-level dir (default ~/.claude).

Warn-only by design (MECHANISMS.md axis 1): a misplaced skill is a findability
cost, not a harm, so the weakest trigger that still catches it is a message at
session open.
"""
import json
import os
import subprocess
import sys

TAG = "prefixhook"
USER_ALLOWED = {"atelier", "synced"}


def user_dir():
    return os.environ.get("CLAUDE_CONFIG_DIR") or os.path.join(os.path.expanduser("~"), ".claude")


def listing(d):
    try:
        return sorted(n for n in os.listdir(d) if not n.startswith("."))
    except OSError:
        return []


def repo_root(cwd):
    try:
        r = subprocess.run(["git", "-C", cwd, "rev-parse", "--show-toplevel"],
                           capture_output=True, text=True, timeout=5)
        if r.returncode == 0 and r.stdout.strip():
            return r.stdout.strip()
    except (OSError, subprocess.SubprocessError):
        pass
    return None


def strays(cwd):
    """[(where, name)] for every skill or command outside the plugin."""
    out = []
    ud = user_dir()
    for n in listing(os.path.join(ud, "skills")):
        if n not in USER_ALLOWED:
            out.append(("~/.claude/skills", n))
    for n in listing(os.path.join(ud, "commands")):
        out.append(("~/.claude/commands", n))
    root = repo_root(cwd)
    if root:
        for sub in ("skills", "commands"):
            for n in listing(os.path.join(root, ".claude", sub)):
                out.append((os.path.basename(root) + "/.claude/" + sub, n))
    return out


def names(found):
    return ", ".join("/%s (%s)" % (n[:-3] if n.endswith(".md") else n, w) for w, n in found)


def render(found):
    if not found:
        return None
    head = "%d command(s) outside /atelier: %s" % (len(found), names(found))
    ctx = ("%s: %s. The principal wants every skill and command under the /atelier: prefix "
           "(atelier docs/method/MECHANISMS.md § Where it lives and what it is called; board 450/010). "
           "Do not create another one outside the plugin; mention this only if the session touches skills "
           "or commands." % (TAG, head))
    return {"hookSpecificOutput": {"hookEventName": "SessionStart", "additionalContext": ctx},
            "systemMessage": "%s: %s" % (TAG, head[:300])}


def main(argv):
    if argv[:1] == ["--check"]:
        found = strays(argv[1] if len(argv) > 1 else os.getcwd())
        for w, n in found:
            print("%s/%s" % (w, n))
        if not found:
            print("✓ prefixhook: every skill and command is under /atelier:")
        return 1 if found else 0
    try:
        try:
            data = json.load(sys.stdin)
        except Exception:
            data = {}
        cwd = (data.get("cwd") if isinstance(data, dict) else None) or os.getcwd()
        out = render(strays(cwd))
        if out is not None:
            print(json.dumps(out, ensure_ascii=False))
    except BaseException:       # a hook error helps no one; say nothing
        pass
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
