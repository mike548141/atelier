- [ ] ⏳ **Rule-4 cold pass queued: `ccapple` checks the filter before it
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
