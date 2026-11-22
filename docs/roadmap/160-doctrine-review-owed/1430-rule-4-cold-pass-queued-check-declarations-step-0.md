- [ ] 🎯 **Rule-4 cold pass queued: every check states its five declaration fields (`115/120`, step 0).** The authoring session (a
      principal-opened Opus 5.5 queue run, session d0ca5d24, 2026-11-09 UTC,
      which dispatched the worker that wrote it) queues this and does not
      take it.
      *Tier:* Fable, the principal-named review tier, checked at selection;
      the pass waits for his explicit permission for Fable work.
      *Pass type:* code cold pass, first of its kind, per `method/REVIEW.md` rule 4.
      *Delta, scoped to paths:* `tools/floor.py`, `tools/floorfleet.py`, their tests, `tools/README.md`, the status line in `docs/method/GUARDS.md`, `CHANGELOG.md` — the commit that closes step 0 of `115/120`, on `main`.
      *Questions worth the pass's time:* whether a `Declares` citation that resolves actually names the rule it claims; whether an `Unmet` can read as met in any view.
      *Intent record:* `115/120`, the design note in `docs/decisions/`.
      *Brief:* written 2026-11-14 UTC by a headless brief-writer (session 263945c1) for
      an estate health sweep, `docs/reviews/2026-11-14-0318-check-declarations-step-0-cold.md`,
      held-back material in its `.deferred.md` sibling. Waiting on Mike's Fable approval;
      sessions 263945c1, 58027096 and d0ca5d24 may not run it.
      🔒 2026-11-22T22:49Z: claimed for the Fable pass by a headless per-pass
      orchestrator, session cd7d5f1e (Opus 5.5, rule-4 off-tier orchestrator:
      it holds the partition and forms no finding), started by drain session
      eca14b23; the reviewer is a Fable 5.1 subagent, tier checked at
      selection. Neither is barred by the brief. The approval this item waits
      for is his drain order of 2026-11-23, verbatim: *"Start a fable drain or
      whatever it is called now. Target 100% of weekly budget by 11.30am NZT
      todat"*. The held-back sibling is partitioned out of the review tree
      until act 1 is committed.
      ✅ 2026-11-22T23:44Z: PASS RAN (Fable 5.1 reviewer; orchestrator session cd7d5f1e, started
      by drain session eca14b23, formed no finding). Verdict PASS-WITH-FINDINGS: 0
      MAJOR, 2 MODERATE (CD1, CD2), 5 minor (CD3–CD7), 7 notes (CD8–CD14, two formed
      at reconcile). No standing MAJOR. Verdict, reconcile, folded sibling and review
      log are in the brief.
      🎯 Mike's to rule (rule 3, record all, apply nothing), plain:
      CD1: a child's declaration can claim a rule was reviewed with any text at all,
      and its "meets all five" count rises; should `reviewed` have to name a real
      verdict file? Recommended: yes, checked like a citation.
      CD2: six checks still print the allow-marker question as open, though the
      2026-11-12 answers in `GUARDS.md` settled it; who restates them? Recommended:
      the `160/1440` pass or the group-A lane, retiring the four stale statements
      together.
      CD3–CD7: two small reader hardenings (an unparseable test file, symlinks), two
      wrong reasons in the registry, one doc mirror; recommended as one `floor.py`
      lane, in a bulk yes. CD8–CD14: notes carried into the group lanes.
      Routing: findings land in a build lane on `tools/floor.py`; none is applied.
