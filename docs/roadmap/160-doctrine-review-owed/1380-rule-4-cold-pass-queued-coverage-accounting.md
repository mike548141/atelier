- [ ] ⏳ **Rule-4 cold pass queued: coverage accounting: a scan of nothing no longer reads as clean (`115/130`, eleven scanners).** The authoring session (a
      principal-opened Opus 5.5 queue run, session d0ca5d24, 2026-11-09 UTC,
      which dispatched the worker that wrote it) queues this and does not
      take it.
      *Tier:* Fable, the principal-named review tier, checked at selection;
      the pass waits for his explicit permission for Fable work.
      *Pass type:* code cold pass, per `method/REVIEW.md` rule 4.
      *Delta, scoped to paths:* `tools/report.py` and the eleven scanners and tests the commit names, `docs/method/GUARDS.md`, `CHANGELOG.md` — the commit that lands `report.coverage_line`, on `main`.
      *Questions worth the pass's time:* whether any count can be non-zero over a scan that evaluated nothing; whether the warning fires where a scanner is legitimately out of scope.
      *Intent record:* `115/130`.
