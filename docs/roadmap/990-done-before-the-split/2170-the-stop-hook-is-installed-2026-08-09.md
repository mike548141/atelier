- [x] 🎯 **The `Stop` hook is INSTALLED — 2026-08-09.** `~/.claude/settings.json`
  carries a `Stop` entry running `tools/hooks/plain-reply.py`. Exec form, so no
  shell parses the path, and the interpreter is pinned to `/usr/bin/python3`
  rather than PATH-resolved — a hook must not depend on a login shell's PATH.
  That interpreter is Python 3.9; both files carry
  `from __future__ import annotations`, which is what lets their type hints run
  on it. Pipe-tested on a clean payload and a rule-breaking one before wiring,
  settings re-validated whole. It applies in every repo, which is what Mike
  asked for and is also its main risk: one hook now sits between the agent and
  every reply it writes. The two failure modes to watch stay open in
  ROADMAP.md.
