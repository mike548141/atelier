- [ ] ⏳ **Rule-4 cold pass queued: a floor `disabled` entry takes an end date, warn-first (`320/800`), and reviewscan's not-in-scope line (`320/770`).** The authoring session (a
      principal-opened Opus 5.5 queue run, session d0ca5d24, 2026-11-09 UTC,
      which dispatched the worker that wrote it) queues this and does not
      take it.
      *Tier:* Fable, the principal-named review tier, checked at selection;
      the pass waits for his explicit permission for Fable work.
      *Pass type:* code cold pass, per `method/REVIEW.md` rule 4.
      *Delta, scoped to paths:* `tools/floor.py`, `tools/floorfleet.py`, `tools/reviewscan.py`, their tests, `tools/test_report.py`, `tools/README.md`, `docs/method/GUARDS.md`, `CHANGELOG.md` — the commit that lands `320/800`, on `main`.
      *Questions worth the pass's time:* whether the new shape can lower a check silently; whether a zero-record scan can still read as a pass anywhere it is displayed.
      *Intent record:* `320/770`, `320/800`, `020/170`.
      📝 BRIEF WRITTEN 2026-11-14 by a headless Opus 5.5 brief-writer (session 48ef9c3e,
      started by an estate health sweep, orchestrator session 58027096; neither authored this
      delta): `docs/reviews/2026-11-14-0154-disabled-end-date-reviewscan-scope-cold.md`, with
      its `.deferred.md` sibling. The delta is one commit, `06248fba`; later commits have
      touched the same tools, and the brief asks the pass to judge it as it stands at HEAD.
      Pass size: medium. Review NOT run: it waits for a criterion-passing cold Fable session
      and the principal's explicit permission for Fable work. Neither named session may run it.
