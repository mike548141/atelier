- [x] **Parallel-work tooling** (Mike 2026-07-10: make fork-and-merge a *tool*,
      not just doctrine) — built as `tools/worktree.py`
      (`start`/`list`/`land`/`remove`), the one-command delivery of CONCURRENCY's
      worktree-per-line: fork outside iCloud, hygiene view, push+PR back, guarded
      cleanup. Guards encode the doctrine — iCloud-base refusal, branch-off-main,
      stale/dirty flags, no-lose-work on remove. 12 stdlib tests + live-proven on
      atelier itself (start → list → remove round-trip, main tree left untouched).
      Built the same session Mike was handed the worktree recipe to run the
      method/ Fable review as a parallel line.
