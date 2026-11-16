#!/usr/bin/env python3
"""floorhook -- a Claude Code SessionStart hook: say, at session open, whether
this child repo's atelier pin and inlined floor copy are current. Warn-only.

Why: a child inlines atelier's safety floor into its CLAUDE.md so the rules bind
where atelier is never read (PROPAGATION.md). The drift check was a line the
model ran by hand at session start, and a floor copy once drifted for weeks
until a fleet run of `pins.py` caught it. The principal's words (board 020/470):
"a hook to confirm the safety rules are up to date and fail noisy if not."
`instruments/ccclose` check 14 is the close-time half; this is the open-time
half, so a session does not work a whole day on a stale floor first.

Same verdicts by the same means as ccclose check 14, and `tools/pins.py` stays
the only judge: this runs `pins.py --json --log --atelier <checkout> --child
<repo>` and only reads its answer. Nothing here re-derives a status.

  LOUD   the floor copy differs from atelier's; or the pin is behind AND the
         floor text changed since the pin; or the pin is ahead, diverged,
         unknown, or missing while the floor is stamped.
  quiet  the pin is behind but the floor is unchanged since it (atelier moves
         daily; a bump is a deliberate read of the delta, not a reflex), or the
         copy is in a report-only state. One line.
  current  one short line to the user only (never to the model's context).
  silent   not a child: atelier itself, not a git repo, or CLAUDE.md carries no
           `atelier@<sha>` pin and no floor stamp.
  "no result: <reason>"  any failure to measure: no atelier checkout, a failed
         fetch, a 10 s timeout, output that does not parse. Never "current".

Output contract (Claude Code hooks docs, SessionStart): one JSON object on
stdout. `hookSpecificOutput.additionalContext` reaches the model before the first
prompt; `systemMessage` is shown to the user. A loud verdict and a no-result
carry both, a quiet verdict only the model's, "current" only the user's.

It NEVER blocks and always exits 0: SessionStart cannot block, and any other exit
code would surface as a hook error. Every failure inside the hook is itself a
"no result", printed and exited 0.

Known limits (020/460): a hook fails open (if it never ran, nothing says so),
it can be switched off (`disableAllHooks`, an untrusted workspace), and it does
not exist in a cloud session. `ccclose` check 14 is the backstop. It costs about
a second a session (pins.py fetches atelier's origin).

Atelier checkout, first that holds `tools/pins.py`: `$ATELIER_TOOLS`, then
`git config hooks.atelierTools` (read in the repo; its parent is atelier), then
the checkout this script lives in. TRUST: the first two name code this hook runs,
the same trust the pre-commit hook gives them.

Wiring (user-level `~/.claude/settings.json`; SessionStart fires on startup,
resume, clear and compact, so `matcher` keeps it to the ones that matter):

    "hooks": {"SessionStart": [{"matcher": "startup|resume", "hooks": [
        {"type": "command", "command": "python3 <atelier>/tools/floorhook.py",
         "timeout": 20}]}]}

Tests: tools/test_floorhook.py.
"""
import json
import os
import re
import signal
import subprocess
import sys

TIMEOUT_S = 10
CLAUDE_MD_MAX = 2 * 1024 * 1024        # pins.py's own cap: a bigger file is not read
PIN_IN_CLAUDE = re.compile(r"atelier@[0-9a-f]{7,40}\b", re.I)
FLOOR_STAMP = re.compile(
    r"^<!--\s*stamp:begin\s+source=docs/method/PROPAGATION\.md\s+region=floor\b", re.M)
TAG = "floorhook"


def clip(s, n):
    s = re.sub(r"[\x00-\x1f\x7f]+", " ", str(s or "")).strip()
    return s if len(s) <= n else s[: n - 1] + "…"


def sh(argv, cwd, secs):
    """Run a command with a hard time limit, killing its whole process group on
    a timeout (pins.py's fetch is a grandchild). Returns (code, out, err); code
    is None when it did not finish or could not run."""
    try:
        p = subprocess.Popen(
            argv, cwd=cwd, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE,
            stderr=subprocess.PIPE, text=True, errors="replace",
            start_new_session=True,
            env={**os.environ, "GIT_TERMINAL_PROMPT": "0"})
    except OSError as e:
        return None, "", str(e)
    try:
        out, err = p.communicate(timeout=secs)
    except subprocess.TimeoutExpired:
        try:
            os.killpg(p.pid, signal.SIGKILL)
        except OSError:
            pass
        try:
            p.communicate(timeout=2)
        except Exception:
            pass
        return None, "", f"no answer within {secs} s"
    return p.returncode, out, err


def git(root, args, secs=5):
    return sh(["git", "--no-optional-locks", "-C", root] + args, root, secs)


def has_pins(d):
    return bool(d) and os.path.isfile(os.path.join(d, "tools", "pins.py"))


def locate_atelier(root):
    """The atelier checkout to measure against: (dir, None) or (None, why)."""
    tried = []
    tools = os.environ.get("ATELIER_TOOLS")
    if not tools:
        code, out, _ = git(root, ["config", "--get", "hooks.atelierTools"])
        tools = out.strip() if code == 0 else ""
    if tools:
        d = os.path.dirname(os.path.abspath(os.path.expanduser(tools.rstrip("/"))))
        if has_pins(d):
            return d, None
        tried.append(d)
    here = os.path.dirname(os.path.abspath(__file__))
    code, out, _ = sh(["git", "--no-optional-locks", "-C", here, "rev-parse",
                       "--path-format=absolute", "--git-common-dir"], here, 5)
    if code == 0 and out.strip():
        d = os.path.dirname(out.strip())        # main checkout, from a worktree too
        if has_pins(d):
            return d, None
        tried.append(d)
    d = os.path.dirname(here)
    if has_pins(d):
        return d, None
    tried.append(d)
    return None, "no atelier checkout found (looked in %s; set $ATELIER_TOOLS)" % ", ".join(tried)


def child_root(cwd):
    """The repo root holding `cwd`, or None if it is no git repo."""
    if not cwd or not os.path.isdir(cwd):
        return None
    code, out, _ = git(cwd, ["rev-parse", "--show-toplevel"])
    return out.strip() if code == 0 and out.strip() else None


def claude_md(root):
    p = os.path.join(root, "CLAUDE.md")
    try:
        if os.path.getsize(p) > CLAUDE_MD_MAX:
            return None
        with open(p, encoding="utf-8", errors="replace") as f:
            return f.read()
    except OSError:
        return None


def verdict(root, timeout):
    """(level, lines, commits): level in silent | current | quiet | loud |
    noresult; `commits` are the atelier commits pins.py lists for a stale pin."""
    if has_pins(root) and os.path.isfile(os.path.join(root, "docs", "method", "PROPAGATION.md")):
        return "silent", [], []                 # atelier itself: nothing pins it
    text = claude_md(root)
    if text is None or not (PIN_IN_CLAUDE.search(text) or FLOOR_STAMP.search(text)):
        return "silent", [], []                 # not a child
    at, why = locate_atelier(root)
    if not at:
        return "noresult", [why], []
    code, out, err = sh([sys.executable, "-I", os.path.join(at, "tools", "pins.py"),
                         "--json", "--log", "--atelier", at, "--child", root], at, timeout)
    # pins exits 1 for "not current" and still prints its JSON; 2 means it could
    # not measure at all (a failed fetch, no origin/main); None, it did not finish.
    if code is None:
        return "noresult", ["pins.py did not finish within %s s or could not run (%s)"
                            % (timeout, clip(err, 120) or "no detail")], []
    if code not in (0, 1):
        return "noresult", ["pins.py exited %s: %s" % (code, clip(err or out, 200) or "no output")], []
    try:
        j = json.loads(out)
        c = j["children"][0]
        status = c["status"]
        if not isinstance(status, str):
            raise ValueError("status")
    except Exception:
        return "noresult", ["pins.py printed nothing readable (%s)" % (clip(err or out, 160) or "no output")], []

    ref = j.get("ref") or "origin/main"
    pin = str(c["pin"])[:7] if c.get("pin") else None
    problems, notes = [], []
    if status == "behind":
        lag = "pin %s is %s commit(s) behind %s" % (pin, c.get("behind"), ref)
        if c.get("floor_moved") is True:
            problems.append(lag + ", and the safety floor has changed since the pin")
        elif c.get("floor_moved") is False:
            notes.append(lag + "; floor unchanged since the pin")
        else:
            notes.append(lag + "; whether the floor changed since the pin could not be read")
    elif status == "ahead":
        problems.append("pin %s is ahead of %s by %s commit(s), not a commit atelier published"
                        % (pin, ref, c.get("ahead")))
    elif status == "diverged":
        problems.append("pin %s has diverged from %s (%s behind, %s ahead)"
                        % (pin, ref, c.get("behind"), c.get("ahead")))
    elif status == "unknown":
        problems.append("pin %s is not a commit in the atelier checkout %s" % (pin, at))
    elif status == "no-pin":
        problems.append("the floor is stamped but CLAUDE.md names no atelier pin")
    elif status != "current":
        return "noresult", ["pins.py reported a status floorhook does not know: %s" % clip(status, 40)], []

    detail = clip(c.get("copy_detail"), 200)
    copy = c.get("copy")
    failing = set((j.get("floor_copy") or {}).get("failing") or [])
    if copy in ("drift", "malformed"):
        problems.append("the floor copy differs from atelier's floor at the pin"
                        + (" (%s)" % detail if detail else ""))
    elif c.get("name") in failing and status != "unknown":
        problems.append("the floor copy fails pins.py's check (%s%s)"
                        % (copy, ": " + detail if detail else ""))
    if problems:
        return "loud", problems + notes, [clip(l, 110) for l in (c.get("log") or [])[:3]]
    if copy == "identical":
        if notes:
            return "quiet", notes + ["floor copy identical"], []
        return "current", ["pin %s is current with %s; floor copy identical" % (pin, ref)], []
    # Not shown identical and not yet a failure (report-only states): say so,
    # never "current".
    notes.append("the floor copy is %s%s" % (copy, " (%s)" % detail if detail else ""))
    return "quiet", notes, []


def render(level, lines, commits, root):
    """The JSON object to print, or None for silence."""
    name = os.path.basename(root or "") or "repo"
    body = "; ".join(lines)
    if level == "silent":
        return None
    if level == "current":
        return {"systemMessage": "%s: %s: %s" % (TAG, name, body)}
    if level == "quiet":
        return {"hookSpecificOutput": {"hookEventName": "SessionStart",
                "additionalContext": "%s: atelier floor, %s: %s. Worth reading the delta when convenient; "
                                     "not urgent." % (TAG, name, body)}}
    if level == "noresult":
        msg = "%s: no result: %s. The atelier floor was NOT checked; do not read this as current." % (TAG, body)
        return {"hookSpecificOutput": {"hookEventName": "SessionStart", "additionalContext": msg},
                "systemMessage": "%s: no result: %s" % (TAG, clip(body, 160))}
    head = "FLOOR OUT OF DATE (%s, %s): %s." % (TAG, name, body)
    ctx = (head + (" Atelier commits the child would inspect, newest first: %s." % " | ".join(commits) if commits else "")
           + " Say so plainly at the top of your first reply, before other work. Do not hand-edit the floor"
           " copy: bump the pin and re-copy the floor verbatim from atelier (PROPAGATION.md).")
    return {"hookSpecificOutput": {"hookEventName": "SessionStart", "additionalContext": ctx},
            "systemMessage": "⚠️ " + clip(head, 300)}


def main():
    try:
        try:
            data = json.load(sys.stdin)
        except Exception:
            data = {}
        cwd = (data.get("cwd") if isinstance(data, dict) else None) or os.getcwd()
        root = child_root(cwd)
        if not root:
            return
        try:
            timeout = float(os.environ.get("FLOORHOOK_TIMEOUT") or TIMEOUT_S)
            if timeout <= 0:
                timeout = TIMEOUT_S
        except ValueError:
            timeout = TIMEOUT_S
        level, lines, commits = verdict(root, timeout)
        out = render(level, lines, commits, root)
        if out is not None:
            print(json.dumps(out, ensure_ascii=False))
    except BaseException as e:      # never a hook error: a failure is a "no result"
        try:
            print(json.dumps({"hookSpecificOutput": {"hookEventName": "SessionStart",
                  "additionalContext": "%s: no result: the hook itself failed (%s). The atelier floor was "
                                       "NOT checked." % (TAG, clip(repr(e), 120))}}))
        except BaseException:
            pass


if __name__ == "__main__":
    main()
    sys.exit(0)
