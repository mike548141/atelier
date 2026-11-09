- [~] (claimed 2026-11-09-0105, wt: under ~/worktrees/briefs, brief only, session d4a0fcf3) ⏳ **Rule-4 cold pass queued: `pathscan` skips a child's inlined floor
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
