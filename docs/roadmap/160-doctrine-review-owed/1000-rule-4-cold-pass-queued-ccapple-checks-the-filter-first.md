- [~] ⏳ **Rule-4 cold pass queued: `ccapple` checks the filter before it
      looks for a store (`210/340`).** `ccapple` reads the principal's
      Apple stores and its exit status is what a caller branches on, so the
      authoring session (a principal-opened Opus 5.5 queue run, session
      deeac927, 2026-11-03, which dispatched the Sonnet worker that wrote
      the code) queues this and does not take it. `ccapple`'s own first
      cold pass, `160/989`, is still queued; one session may take both.
      *Tier:* Fable, the principal-named review tier, checked at selection.
      *Pass type:* code cold pass, per `method/REVIEW.md` rule 4.
      *Delta, scoped to paths:* `instruments/ccapple`,
      `instruments/test_ccapple.py`, `instruments/man/ccapple.1`,
      `CHANGELOG.md` (the commit that closes `210/340`, on `main`,
      2026-11-03).
      *Intent record:*
      [`../210-instruments-open-features/340-ccapple-checks-the-store-before-the-filter.md`](../210-instruments-open-features/340-ccapple-checks-the-store-before-the-filter.md).
      📝 BRIEF WRITTEN 2026-11-09 by session 84e3aa7f (Opus 5.5), a headless
      brief-writer started by coordinating session 74f2b8cd:
      `docs/reviews/2026-11-09-0126-ccapple-filter-first-cold.md`, with its
      `.deferred.md` sibling. Neither session may run the pass. Review NOT
      run. The pass waits for a criterion-passing cold Fable session and the
      principal's explicit permission for Fable work.
      🔒 CLAIMED 2026-11-15T21:29Z UTC for the cold pass, in Mike's weekly Fable drain (his
      `/fable-drain` order, 2026-11-16 06:53 NZDT; approval lapses at the reset,
      2026-11-15 23:00 UTC). Orchestrator: a headless Opus 5.5 session started by drain
      session 21a271a5, a rule-4 off-tier orchestrator that holds the context partition,
      forms no finding and writes no severity. Reviewer: Fable 5.1, tier checked at
      selection, spawned by that orchestrator. Neither is a barred session (deeac927 and
      what it started, 84e3aa7f, 74f2b8cd). The sibling is held out of the worktree until
      act 1 is committed. The item's "waits for the principal's explicit permission for
      Fable work" is met by that drain order.
