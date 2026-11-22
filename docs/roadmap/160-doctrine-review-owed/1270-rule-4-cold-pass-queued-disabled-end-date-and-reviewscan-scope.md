- [ ] 🎯 **Rule-4 cold pass queued: a floor `disabled` entry takes an end date, warn-first (`320/800`), and reviewscan's not-in-scope line (`320/770`).** The authoring session (a
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
      🔒 2026-11-22T20:49Z: claimed for the Fable pass by a headless per-pass
      orchestrator, session 92ba9071 (Opus 5.5, rule-4 off-tier orchestrator:
      it holds the partition and forms no finding), started by drain session
      eca14b23; the reviewer is a Fable 5.1 subagent, tier checked at
      selection. Neither is barred by the brief. The approval this item waits
      for is his drain order of 2026-11-23, verbatim: *"Start a fable drain or
      whatever it is called now. Target 100% of weekly budget by 11.30am NZT
      todat"*. The held-back sibling is partitioned out of the review tree
      until act 1 is committed.
      ✅ 2026-11-22T21:18Z: PASS RAN (Fable 5.1 reviewer; orchestrator session 92ba9071,
      off-tier, held the partition, formed no finding), acts 1 and 2 complete
      and the sibling folded:
      [`docs/reviews/2026-11-14-0154-disabled-end-date-reviewscan-scope-cold.md`](../../reviews/2026-11-14-0154-disabled-end-date-reviewscan-scope-cold.md).
      **Verdict: PASS-WITH-FINDINGS — 0 MAJOR · 5 MODERATE (DE1–DE5) ·
      8 minor (DE6–DE11, DE13, DE14 at reconcile) · 1 note (DE12).** No MAJOR
      stands. All nine re-run lines exit 0; the sibling-config proof
      reproduces (23 configs, the record said 21).
      🎯 Owed to the principal (rule 3: a gate and a guard's report line are
      doctrine by function, so every finding is his to rule; nothing
      applied). Plain briefing: a repo can now give a switched-off check an
      end date, but a child can quietly push that date out (DE1), a date far
      in the future looks healthier than no date at all (DE2), and the
      warn-only stage has no date of its own for when it starts blocking
      (DE5; only 3 such entries exist fleet-wide, all undated). On the scan
      side, "not in scope" reads as all-clear where the house means the
      opposite (DE3), and the commit hook never computes the new count (DE4).
      Ask, in the reviewer's order: DE5 (warn until a date, then block?), DE2
      (a limit on how far out `review-by` may be, on both lanes), DE1 (may a
      child move a disabled date; give it a `kind`). Reviewer's counsel: a
      build session takes DE1, DE3, DE4, DE6–DE10, DE13, DE14 once he has
      ruled; DE11 as its own item under `115/130`; DE12 is record only.
      Routing: a fix session in atelier once ruled; a re-pass only if he
      asks.
