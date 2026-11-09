- [~] (claimed 2026-11-09-0105, wt: under ~/worktrees/briefs, brief only, session d4a0fcf3) ⏳ **Rule-4 cold pass queued: every scanner's `--selftest` prints only
      its verdict (`320/690`).** The change reaches every child's next CI run
      (the reusable workflow's selftest step runs each scanner's `--selftest`),
      so the authoring session (a principal-opened Opus 5.5 queue run, session
      4c65083c, 2026-11-03, which dispatched the Sonnet worker that wrote the
      code) queues this and does not take it.
      *Tier:* Fable, the principal-named review tier, checked at selection.
      *Pass type:* code cold pass, per `method/REVIEW.md` rule 4.
      *Delta, scoped to paths:* `tools/report.py`, `tools/board.py`,
      `tools/datescan.py`, `tools/pathscan.py`, `tools/spellscan.py`,
      `tools/wrapscan.py`, `tools/conflictscan.py`, `tools/sizescan.py`,
      `tools/stampscan.py`, `tools/test_selftest_quiet.py`, `tools/README.md`,
      `CHANGELOG.md` (the commit that closes `320/690`, on `main`, 2026-11-03).
      *Intent record:*
      [`../320-child-filed-findings-via-pointing-up/690-a-scanner-selftest-prints-fixture-findings-in-the-floors-own-shape.md`](../320-child-filed-findings-via-pointing-up/690-a-scanner-selftest-prints-fixture-findings-in-the-floors-own-shape.md).
