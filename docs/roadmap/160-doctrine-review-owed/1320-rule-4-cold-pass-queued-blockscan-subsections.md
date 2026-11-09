- [ ] ⏳ **Rule-4 cold pass queued: `blockscan` reads edits inside mapped sub-sections, warning until 2027-01-11 (`320/340`, slice 1 of `320/810`).** The authoring session (a
      principal-opened Opus 5.5 queue run, session d0ca5d24, 2026-11-09 UTC,
      which dispatched the worker that wrote it) queues this and does not
      take it.
      *Tier:* Fable, the principal-named review tier, checked at selection;
      the pass waits for his explicit permission for Fable work.
      *Pass type:* code cold pass, per `method/REVIEW.md` rule 4.
      *Delta, scoped to paths:* `tools/blockscan.py`, `tools/test_blockscan.py`, `tools/README.md` — the commit that closes `320/340`, on `main`.
      *Questions worth the pass's time:* whether reading through the nearest mapped ancestor can fire one edit on the wrong bullet; whether the date's flip reaches the `--warn` CI step as intended.
      *Intent record:* `320/340`, `320/810`.
