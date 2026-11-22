- [ ] 🎯 **Rule-4 cold pass queued: `pathscan` skips a child's inlined floor
      region, and `conflictscan` reports tool-call markup as an advisory
      (`320/610`, `320/490`).** Both scanners reach every child's next CI
      run, so the authoring session (a principal-opened Opus 5.5 queue run,
      session 4c65083c, 2026-11-03, which dispatched the Sonnet worker that
      wrote the code) queues this and does not take it.
      *Tier:* Fable, the principal-named review tier, checked at selection.
      *Pass type:* code cold pass, per `method/REVIEW.md` rule 4.
      *Delta, scoped to paths:* `tools/pathscan.py`, `tools/test_pathscan.py`,
      `tools/conflictscan.py`, `tools/test_conflictscan.py`, `tools/floor.py`,
      `tools/test_floor.py`, `tools/README.md`, `.conflictscanignore`,
      `CHANGELOG.md` (the two commits that close `320/610` and `320/490`:
      `24ac5b8`, `92dd817`, on `main`, 2026-11-03).
      *Intent records:*
      [`../320-child-filed-findings-via-pointing-up/610-the-floor-names-a-path-no-child-can-resolve.md`](../320-child-filed-findings-via-pointing-up/610-the-floor-names-a-path-no-child-can-resolve.md),
      [`../320-child-filed-findings-via-pointing-up/490-tool-call-markup-leaks-into-written-files-and-no-scanner-sees-it.md`](../320-child-filed-findings-via-pointing-up/490-tool-call-markup-leaks-into-written-files-and-no-scanner-sees-it.md).
      📝 BRIEF WRITTEN 2026-11-09 by session d4a0fcf3 (Opus 5.5, headless,
      started by coordinating session 74f2b8cd; neither authored this delta):
      `docs/reviews/2026-11-09-0207-floor-region-skip-markup-rule-cold.md`,
      with its `.deferred.md` sibling. Pass size: medium. Review NOT run: this
      pass waits for a criterion-passing cold Fable session and the
      principal's explicit permission for Fable work. Neither named session
      may run it.
      🔒 2026-11-22T20:04Z: claimed for the Fable pass by a headless per-pass
      orchestrator, session e55d14f5 (Opus 5.5, rule-4 off-tier orchestrator:
      it holds the partition and forms no finding), started by drain session
      eca14b23; the reviewer is a Fable 5.1 subagent, tier checked at
      selection. Neither is barred by the brief. The approval this item waits
      for is his drain order of 2026-11-23, verbatim: *"Start a fable drain or
      whatever it is called now. Target 100% of weekly budget by 11.30am NZT
      todat"*. The held-back sibling is partitioned out of the review tree
      until act 1 is committed.
      ✅ 2026-11-22T21:05Z: PASS RAN (Fable 5.1 reviewer; orchestrator session e55d14f5,
      off-tier, held the partition, formed no finding), acts 1 and 2 complete
      and the sibling folded:
      [`docs/reviews/2026-11-09-0207-floor-region-skip-markup-rule-cold.md`](../../reviews/2026-11-09-0207-floor-region-skip-markup-rule-cold.md).
      **Verdict: PASS-WITH-FINDINGS — 0 MAJOR, 2 MODERATE (FK1, FK2),
      5 minor (FK3–FK6, FK10), 3 note (FK7, FK8, FK9).** No MAJOR stands.
      All six re-run lines green (full suite 3382 tests OK).
      🎯 Owed to the principal (rule 3: the work is doctrine by function, so
      every finding is his to rule; nothing applied). Plain briefing: the
      scanner change skips a child's copied floor text because "another check
      covers it", but that other check does not run in children (FK1); and
      the new tool-markup warning has no date when it starts blocking (FK2).
      Ask: apply the reviewer's counsel to all ten as listed in the verdict's
      follow-up checklist, with FK2's start-blocking date his to set.
      Recommendation: approve all ten in one go (FK1 by naming the real
      checker, `pins --floor`/`floorhook`, and its tier in the three
      surfaces; FK2 with a printed `TOOL_MARKUP_BLOCKS_FROM` date; FK7–FK9
      record only). Routing: a fix session in atelier once ruled; any re-pass
      only if he asks.
