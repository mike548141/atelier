- [ ] 🎯 **Rule-4 cold pass queued: `ccclose` lists board ids in number
      order (`210/370`).** `ccclose`'s identifiers block is pasted into
      records as fact, so the authoring session (a principal-opened Opus 5.5
      queue run, session deeac927, 2026-11-03, which wrote it inline) queues
      this and does not take it. Small enough to take with `160/1010`.
      *Tier:* Fable, the principal-named review tier, checked at selection.
      *Pass type:* code cold pass, per `method/REVIEW.md` rule 4.
      *Delta, scoped to paths:* `instruments/ccclose`,
      `instruments/ccclose.test.js`, `CHANGELOG.md` (the commit that closes
      `210/370`, on `main`, 2026-11-03).
      *Intent record:*
      [`../210-instruments-open-features/370-ccclose-sorts-board-ids-as-text.md`](../210-instruments-open-features/370-ccclose-sorts-board-ids-as-text.md).
      📝 BRIEF WRITTEN 2026-11-09 by session 84e3aa7f (Opus 5.5), a headless
      brief-writer started by coordinating session 74f2b8cd:
      `docs/reviews/2026-11-09-0126-ccclose-board-order-cold.md`, with its
      `.deferred.md` sibling. Neither session may run the pass. Review NOT
      run. The pass waits for a criterion-passing cold Fable session and the
      principal's explicit permission for Fable work.
      🔒 CLAIMED 2026-11-15T21:31Z UTC for the cold pass, in Mike's weekly Fable drain (his
      `/fable-drain` order, 2026-11-16 06:53 NZDT; approval lapses at the reset,
      2026-11-15 23:00 UTC). Orchestrator: a headless Opus 5.5 session started by drain
      session 21a271a5, a rule-4 off-tier orchestrator that holds the context partition,
      forms no finding and writes no severity. Reviewer: Fable 5.1, tier checked at
      selection, spawned by that orchestrator. Neither is a barred session (deeac927 and
      what it started, 84e3aa7f, 74f2b8cd). The sibling is held out of the worktree until
      act 1 is committed. The item's "waits for the principal's explicit permission for
      Fable work" is met by that drain order.
      ✅ PASS RAN 2026-11-15 UTC (Fable 5.1, both acts; act 1 `fcce3da1`):
      **PASS-WITH-FINDINGS** — 0 MAJOR, 0 MODERATE, 1 minor, 1 note; unchanged at reconcile.
      No standing MAJOR. Verdict, folded sibling and review log in
      `docs/reviews/2026-11-09-0126-ccclose-board-order-cold.md`.
      🎯 Mike's to rule (rule 3), both small: **CO1** (minor) — the lists' number order is
      pinned only by a unit test of the comparator; reverting the one line that wires it in
      leaves every test green. Recommended: take it, add one end-to-end `--identifiers` test
      with a three- and a four-digit id in one section. **CO2** (note) — "each digit run
      compares as a number, as `board.py` does" overstates parity in mechanism (outcomes agree
      on every real id). Recommended: no change, or reword CHANGELOG if it is touched again.
      Routing: a CO1 fix is atelier instrument work (`instruments/ccclose.test.js`); no other
      repo is affected.
