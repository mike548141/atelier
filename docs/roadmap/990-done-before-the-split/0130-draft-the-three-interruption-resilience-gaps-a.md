- [x] **Draft the three interruption-resilience gaps as one doctrine change**
      (landed `9c11525`, 2026-07-22) —
      - **Gap 1 (high): the resume-state carrier doesn't exist at the cut.**
        The session log is written at *close*; interruptions precede close, so
        a cut session leaves a clean tree but no *intent*. Fix: a durable
        in-flight breadcrumb (extend the claim line — `at: <step>, waiting on
        <X>`), updated as work moves. Overlaps the queue-run strand's per-item
        close (line ~122); reference, don't duplicate.
      - **Gap 2 (medium): decision-limbo.** A pending `🎯` question lives only
        in volatile chat; a dropped window loses it. Fix: write the open
        question into the record before blocking on it.
      - **Gap 3 (low): the recovery procedure isn't in method.** The cmd+Q
        sweep is twice-grounded (session 45, 2026-07-20) but lives in a session
        log. Fix: distil the checklist (tree/sync/stashes/orphan worktrees/
        reflog-after-close/respect sibling lanes) into CONCURRENCY, plus a
        resumer tell — did the last session close clean or die mid-flight?
      Cycle: cold pass PASS-WITH-FINDINGS 0M/3M/2L, closed terminal
      2026-07-22 (`reviews/2026-07-22-0257-interruption-resilience-cold.md`).
