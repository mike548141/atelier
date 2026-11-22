# 2026-11-22 19:50 UTC — the opening id line drops the transcript path

Session 057cdb77 (`atelier-1d`), primary checkout, inline. One ask.

**Ask.** The principal, verbatim: *"when ccopen runs for a new session I only
want the first two. I dont want "Transcript:
~/.claude/projects/-Users-mike--pets-shed/<id>.jsonl""*.

**Done.** The line comes from `tools/idhook.py` (the `SessionStart` hook,
board `210/490`), not `ccopen`. `render()` no longer takes or prints the
transcript path; the test now asserts the path is absent; `tools/README.md`,
the changelog and the board item say so. `test_idhook` 3/3 green; a live run
prints `🆔 Messaging name: atelier-1d · Transcript id: 057cdb77-…`. The hook
is wired user-level to the primary checkout, so the next session opens with
the short line; this one's own hook had already fired with the old line.

**Open.** Nothing.
