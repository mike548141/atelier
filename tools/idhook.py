#!/usr/bin/env python3
"""idhook -- open every session by showing the two ids the principal uses.

Why (board 210/490): the principal, 2026-11-22, verbatim: "when a new session
opens it must print the session ID (what other sessions would use to
communicate with that session) and session transcript ID to the transcript so
that I see both from the time I first start a new session". They are two
different things:

  - the name: what another session passes to `SendMessage` (`atelier-df`).
    Claude Code keeps it in `<config>/sessions/<pid>.json`, field `name`,
    beside `sessionId`. A name can change later; this shows it at open.
  - the transcript id: the session UUID, the name of its transcript file,
    which `cctranscript` and `ccclose --session` take.

  idhook.py      SessionStart hook: reads the hook JSON on stdin (session_id,
                 transcript_path), prints one JSON object: a `systemMessage`
                 for the principal and `additionalContext` asking the model to
                 print both as the first line of its first reply (the path
                 that shows on every surface). Never blocks; always exits 0.
  CLAUDE_CONFIG_DIR   the user-level dir (default ~/.claude).

The name file may land a moment after the hook starts, so the read retries for
up to RETRY_S seconds; if it never appears the name prints as "not yet
assigned" with where to look, never a guess.
"""
import glob
import json
import os
import sys
import time

TAG = "idhook"
RETRY_S = 2.0


def user_dir():
    return os.environ.get("CLAUDE_CONFIG_DIR") or os.path.join(os.path.expanduser("~"), ".claude")


def find_name(session_id, wait=RETRY_S):
    """The messaging name of the session whose registry record has this id."""
    deadline = time.monotonic() + wait
    pattern = os.path.join(user_dir(), "sessions", "*.json")
    while True:
        for p in glob.glob(pattern):
            try:
                with open(p, encoding="utf-8") as f:
                    rec = json.load(f)
            except (OSError, ValueError):
                continue
            if isinstance(rec, dict) and rec.get("sessionId") == session_id:
                name = rec.get("name")
                if isinstance(name, str) and name:
                    return name
        if time.monotonic() >= deadline:
            return None
        time.sleep(0.2)


def render(session_id, transcript, name):
    shown = name or "not yet assigned (ListAgents shows it)"
    line = "🆔 Messaging name: %s · Transcript id: %s" % (shown, session_id)
    if transcript:
        line += " · Transcript: %s" % transcript.replace(os.path.expanduser("~"), "~", 1)
    ctx = ("%s: %s. The principal wants both ids visible from the start of every session "
           "(atelier board 210/490): print this line, as it stands, as the first line of your "
           "first reply." % (TAG, line))
    return {"hookSpecificOutput": {"hookEventName": "SessionStart", "additionalContext": ctx},
            "systemMessage": line}


def main():
    try:
        try:
            data = json.load(sys.stdin)
        except Exception:
            data = {}
        if not isinstance(data, dict):
            data = {}
        sid = data.get("session_id") or os.environ.get("CLAUDE_CODE_SESSION_ID")
        if not sid:
            return 0
        out = render(sid, data.get("transcript_path"), find_name(sid))
        print(json.dumps(out, ensure_ascii=False))
    except BaseException:       # a hook error helps no one; say nothing
        pass
    return 0


if __name__ == "__main__":
    sys.exit(main())
