#!/usr/bin/env python3
"""plain-reply — a Stop hook that refuses to let an unreadable reply stand.

WHAT THIS IS
------------
Claude Code fires the `Stop` hook when the assistant finishes a turn, and hands
it `last_assistant_message` — the exact text about to be the final word of the
reply. This hook lints that text and, if it breaks the plain-language rules the
principal has already stated, returns `{"decision": "block", "reason": ...}`.
The turn does not end; the reason comes back as instruction and the reply gets
rewritten before the principal ever reads it.

WHY IT EXISTS
-------------
The rules were already written down and dated in `~/.claude/CLAUDE.md` and in
atelier's `COMMUNICATION.md`. Measured across 6,704 replies in 1,094 session
transcripts, they were broken in 37% to 67% of replies depending on the rule,
and the rate did not fall after they were written. Reference-ID density rose.
Doctrine alone was not a control. This is the control.

ONE SOURCE, NO VENDORED POLICY
------------------------------
The rules are NOT reimplemented here. This file imports `scan_text` from
atelier's `tools/plainscan.py` — the same engine the pre-commit floor and CI
run against committed prose. A rule fixed once is fixed on both planes. That is
`floor.py`'s registry lesson applied to the conversational surface.

Point it at atelier with ATELIER_TOOLS, or leave it to find the default path.

FAILING OPEN, DELIBERATELY
--------------------------
Every other gate in this estate fails CLOSED, and this one does not. The
difference is what is at stake: secretscan failing open lets a credential into
history for good, while this failing open lets one clumsy reply through. A
linter that can wedge a session is worse than the defect it catches, so any
error here — missing engine, bad JSON, unreadable input — exits 0 and stays
silent. The trade is stated, not accidental.

THE ANTI-DEADLOCK GUARD
-----------------------
A Stop hook that blocks unconditionally can loop: block, rewrite, block again,
forever. So the hook remembers, per session, the last text it blocked. If the
rewrite is still failing after MAX_BLOCKS attempts on one turn, it lets the
reply through with the findings appended as a visible note. The principal sees
the mess AND sees that the wall fired — which is honest, and is the shape a
gate should take when it cannot win.
"""

from __future__ import annotations

import hashlib
import json
import os
import sys
import time
from pathlib import Path

# Rules that block a reply. P2 (unexpanded acronym) is deliberately NOT here in
# the first cut: conversation legitimately carries terms the principal uses
# himself all day, and a glossary is a document-level escape a chat turn has no
# equivalent for. It stays measurable via plainscan on the repo plane.
BLOCKING_RULES = {"P1", "P3", "P4"}

# Chat is looser than doctrine prose, and pretending otherwise would make the
# wall unusable. The repo plane's limits are 35 words / 40 chars; these are the
# CHAT limits, set wider so the hook fires on genuinely unreadable output
# rather than on ordinary density. Both are house calls, both are the
# principal's to set — see plainscan.py's P3 note on why no published
# plain-language standard supplies a number to borrow.
CHAT_SENTENCE_LIMIT = 45
CHAT_ASIDE_LIMIT = 60

MAX_BLOCKS = 2
# Overridable so the suite never touches the live counter. Without this the
# tests shared one state file with the running install AND with each other, so
# a session id reused across runs carried its block count forward and the
# give-up path fired early — the suite failed roughly one run in three, which
# is the kind of flake that gets re-run rather than read.
STATE = Path(os.environ.get("PLAIN_REPLY_STATE")
             or Path.home() / ".claude" / ".plain-reply-state.json")
STATE_TTL = 6 * 3600


def _engine():
    """Import atelier's rule engine. Returns None if unavailable (fail open)."""
    candidates = [Path(__file__).resolve().parent.parent]   # tools/, beside us
    env = os.environ.get("ATELIER_TOOLS")
    if env:
        candidates.insert(0, Path(env))
    candidates.append(Path.home() / ".pets" / "atelier" / "tools")
    for c in candidates:
        if (c / "plainscan.py").is_file():
            sys.path.insert(0, str(c))
            try:
                import plainscan
                return plainscan
            except Exception:
                return None
    return None


def _load_state() -> dict:
    try:
        d = json.loads(STATE.read_text(encoding="utf-8"))
    except Exception:
        return {}
    now = time.time()
    return {k: v for k, v in d.items()
            if isinstance(v, dict) and now - v.get("at", 0) < STATE_TTL}


def _save_state(d: dict) -> None:
    try:
        STATE.parent.mkdir(parents=True, exist_ok=True)
        STATE.write_text(json.dumps(d), encoding="utf-8")
    except OSError:
        pass


ADVICE = {
    "P1": "spell out what the reference means the first time you use it, "
          "or drop the code and name the thing",
    "P3": "split it — one idea per sentence",
    "P4": "finish the sentence, then give the aside its own sentence "
          "(or hang it off the end with a dash)",
}


def _reason(findings) -> str:
    lines = ["Your reply breaks plain-language rules the principal has already "
             "stated. Rewrite it and answer again — same content, readable on "
             "first pass. Do not mention this hook, do not apologise, just send "
             "the better reply.", ""]
    for f in findings[:8]:
        lines.append(f"  [{f.rule}] {f.detail}")
        lines.append(f"        “{f.excerpt}”")
        lines.append(f"        → {ADVICE[f.rule]}")
    if len(findings) > 8:
        lines.append(f"  … and {len(findings) - 8} more of the same kinds.")
    return "\n".join(lines)


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return 0

    text = payload.get("last_assistant_message") or ""
    if not isinstance(text, str) or len(text.strip()) < 200:
        return 0                                   # short acks are not the problem

    engine = _engine()
    if engine is None:
        return 0                                   # fail open, stated above

    try:
        findings = [f for f in engine.scan_text(
            text,
            sentence_limit=CHAT_SENTENCE_LIMIT,
            aside_limit=CHAT_ASIDE_LIMIT,
            rules=BLOCKING_RULES,
        ) if f.rule in BLOCKING_RULES]
    except Exception:
        return 0

    session = str(payload.get("session_id") or "unknown")
    state = _load_state()

    if not findings:
        # A clean reply ends the streak. This is the ONLY reset, and it has to
        # be here: without it the counter would carry across unrelated turns
        # and the wall would stop firing after two bad replies in one session.
        if state.pop(session, None) is not None:
            _save_state(state)
        return 0

    sig = hashlib.sha256(text.encode("utf-8", "replace")).hexdigest()[:16]
    entry = state.get(session) or {}
    count = entry.get("count", 0) + 1
    if count > MAX_BLOCKS:
        # Give up rather than wedge the session. Say so out loud.
        state.pop(session, None)
        _save_state(state)
        note = "\n\n".join([
            "",
            "> ⚠️ **plain-reply**: this reply still breaks "
            f"{len(findings)} plain-language rule(s) after {MAX_BLOCKS} rewrites. "
            "Letting it through rather than wedging the session.",
        ])
        print(json.dumps({
            "hookSpecificOutput": {
                "hookEventName": "Stop",
                "additionalContext": note,
            }
        }))
        return 0

    state[session] = {"sig": sig, "count": count, "at": time.time()}
    _save_state(state)

    print(json.dumps({"decision": "block", "reason": _reason(findings)}))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        sys.exit(0)                                # fail open, always
