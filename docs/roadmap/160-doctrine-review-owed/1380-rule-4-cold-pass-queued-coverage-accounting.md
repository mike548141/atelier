- [ ] 🎯 **Rule-4 cold pass queued: coverage accounting: a scan of nothing no longer reads as clean (`115/130`, eleven scanners).** The authoring session (a
      principal-opened Opus 5.5 queue run, session d0ca5d24, 2026-11-09 UTC,
      which dispatched the worker that wrote it) queues this and does not
      take it.
      *Tier:* Fable, the principal-named review tier, checked at selection;
      the pass waits for his explicit permission for Fable work.
      *Pass type:* code cold pass, per `method/REVIEW.md` rule 4.
      *Delta, scoped to paths:* `tools/report.py` and the eleven scanners and tests the commit names, `docs/method/GUARDS.md`, `CHANGELOG.md` — the commit that lands `report.coverage_line`, and the later commit that extends it to the remaining scanners and the not-in-scope form, on `main`.
      *Questions worth the pass's time:* whether any count can be non-zero over a scan that evaluated nothing; whether the warning fires where a scanner is legitimately out of scope.
      *Intent record:* `115/130`.
      📝 BRIEF WRITTEN 2026-11-14 by session 2a99cef1 (Opus 5.5), a headless
      brief-writer started by an estate health sweep, orchestrator session
      58027096: `docs/reviews/2026-11-14-0259-coverage-accounting-cold.md`, with
      its `.deferred.md` sibling. It covers both commits named above. Neither
      session may run the pass. Review NOT run. The pass waits for a
      criterion-passing cold Fable session and the principal's explicit
      permission for Fable work.
      🔒 2026-11-22T22:42Z: claimed for the Fable pass by a headless per-pass
      orchestrator, session ea866db1 (Opus 5.5, rule-4 off-tier orchestrator:
      it holds the partition and forms no finding), started by drain session
      eca14b23; the reviewer is a Fable 5.1 subagent, tier checked at
      selection. Neither is barred by the brief. The approval this item waits
      for is his drain order of 2026-11-23, verbatim: *"Start a fable drain or
      whatever it is called now. Target 100% of weekly budget by 11.30am NZT
      todat"*. The held-back sibling is partitioned out of the review tree
      until act 1 is committed.
      ✅ 2026-11-22: PASS RAN. Fable 5.1 reviewer, both acts, orchestrated by session
      ea866db1 for drain session eca14b23; sibling folded, review log opened in
      the brief. Verdict: PASS-WITH-FINDINGS, 0 MAJOR · 2 MODERATE · 5 minor ·
      2 note (`VC1`–`VC9`, `VC9` formed at reconcile). No standing MAJOR. Both
      incidents are caught, not-in-scope is honest, no exit code moved.
      🎯 Owed to the principal (rule 3: guard code and doctrine, so every
      finding is his to rule; nothing applied): `VC1` MODERATE, the
      "scanned nothing" warning fires on every routine code-only commit on the
      hook plane and never says why (reviewer's counsel: say "not in scope
      here" when nothing staged is a file the check reads); `VC2` MODERATE, the
      `GUARDS.md` "every guard" sentence is unenforced and three scanners added
      since print no coverage line (counsel: a floor pin over every registry
      scanner, and bring the three in); minor `VC3` (floor counts a refused
      check as run), `VC4` (two scanners skip the line on findings), `VC6`
      (docs gaps, a dead `§ coverage` citation), `VC7` (a missing pin),
      `VC9` (the head line still says clean on a scan of nothing); notes
      `VC5`, `VC8` (wording). Recommendation: approve all as one fix item,
      `VC1` and `VC2` first. Routing: a fix item under section 115 once he
      rules; the item's title says "eleven scanners" where the delta reached
      twenty (record nit, left as written).
