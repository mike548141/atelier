- [ ] 🎯 **Rule-4 cold pass queued: `blockscan` reads edits inside mapped sub-sections, warning until 2027-01-11 (`320/340`, slice 1 of `320/810`).** The authoring session (a
      principal-opened Opus 5.5 queue run, session d0ca5d24, 2026-11-09 UTC,
      which dispatched the worker that wrote it) queues this and does not
      take it.
      *Tier:* Fable, the principal-named review tier, checked at selection;
      the pass waits for his explicit permission for Fable work.
      *Pass type:* code cold pass, per `method/REVIEW.md` rule 4.
      *Delta, scoped to paths:* `tools/blockscan.py`, `tools/test_blockscan.py`, `tools/README.md` — the commit that closes `320/340`, on `main`.
      *Questions worth the pass's time:* whether reading through the nearest mapped ancestor can fire one edit on the wrong bullet; whether the date's flip reaches the `--warn` CI step as intended.
      *Intent record:* `320/340`, `320/810`.
      📝 BRIEF WRITTEN 2026-11-14 by session 99821c6a (Opus 5.5), a headless
      brief-writer started by an estate health sweep, orchestrator session
      58027096: `docs/reviews/2026-11-14-0210-blockscan-subsection-edits-cold.md`,
      with its `.deferred.md` sibling. Neither session may run the pass. Review NOT
      run. The pass waits for a criterion-passing cold Fable session and the
      principal's explicit permission for Fable work.
      🔒 2026-11-22T20:54Z: claimed for the Fable pass by a headless per-pass
      orchestrator, session b5776fd4 (Opus 5.5, rule-4 off-tier orchestrator:
      it holds the partition and forms no finding), started by drain session
      eca14b23; the reviewer is a Fable 5.1 subagent, tier checked at
      selection. Neither is barred by the brief. The approval this item waits
      for is his drain order of 2026-11-23, verbatim: *"Start a fable drain or
      whatever it is called now. Target 100% of weekly budget by 11.30am NZT
      todat"*. The held-back sibling is partitioned out of the review tree
      until act 1 is committed.
      ✅ PASS RAN 2026-11-22T21:24Z (both acts, Fable 5.1 reviewer; orchestrator
      b5776fd4 for drain session eca14b23 formed no finding):
      **PASS-WITH-FINDINGS**, 0 MAJOR, 4 MODERATE, 7 minor, 6 notes
      (`SU1`–`SU17`; `SU15`–`SU17` formed at reconcile). Verdict, reconcile,
      folded sibling and the reviewer's log are in the brief. No standing
      MAJOR: the check closes the gap `320/340` found and follows his
      warn-then-block order; what falls short is the CI plane and the words
      around it.
      🎯 Owed to the principal (rule 3: guard code that enforces doctrine;
      nothing applied). In plain terms, before 2027-01-11 when the check
      starts blocking: `SU1` CI compares only a push's last commit, so an
      earlier commit in the same push lands green on the flip day (counsel:
      compare against the push base, or say CI reads one commit); `SU5` the
      weaker, derived signal blocks while the direct rule stays advisory
      (counsel: align the two dates); `SU2` `--check` still calls these
      edits invisible; `SU3` under `--warn` the output says "not blocking"
      and exits 1. Then the minors `SU4`, `SU6`, `SU7` (M7 test first),
      `SU8`, `SU9`, `SU14` (schedule the pre-flip fleet probe), `SU15`;
      notes `SU10`–`SU13`, `SU16`, `SU17` need no ruling. Recommendation:
      approve all four MODERATEs and the minors as counselled. Routing: a
      build session in atelier applies what he rules, then a fresh cold
      re-check before 2027-01-11.
