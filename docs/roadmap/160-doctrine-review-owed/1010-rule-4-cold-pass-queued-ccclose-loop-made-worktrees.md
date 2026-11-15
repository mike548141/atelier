- [ ] 🎯 **Rule-4 cold pass queued: `ccclose` expands a `for` loop's
      literal word list and counts the worktree adds it cannot resolve
      (`210/360`).** `ccclose`'s identifiers block is pasted into records
      as fact, so the authoring session (a principal-opened Opus 5.5 queue
      run, session deeac927, 2026-11-03, which dispatched the Sonnet worker
      that wrote the code) queues this and does not take it. The pass for
      the change it extends, `160/993`, is still queued; one session may
      take both.
      *Tier:* Fable, the principal-named review tier, checked at selection.
      *Pass type:* code cold pass, per `method/REVIEW.md` rule 4.
      *Delta, scoped to paths:* `instruments/ccclose`,
      `instruments/ccclose.test.js`, `instruments/ccclose.design.md`,
      `instruments/man/ccclose.1`, `CHANGELOG.md` (the commit that closes
      `210/360`, on `main`, 2026-11-03).
      *Intent record:*
      [`../210-instruments-open-features/360-ccclose-drops-a-loop-made-worktree-without-saying-so.md`](../210-instruments-open-features/360-ccclose-drops-a-loop-made-worktree-without-saying-so.md).
      📝 BRIEF WRITTEN 2026-11-09 by session 84e3aa7f (Opus 5.5), a headless
      brief-writer started by coordinating session 74f2b8cd:
      `docs/reviews/2026-11-09-0126-ccclose-loop-worktrees-cold.md`, with its
      `.deferred.md` sibling. Neither session may run the pass. Review NOT
      run. The pass waits for a criterion-passing cold Fable session and the
      principal's explicit permission for Fable work.
      🔒 CLAIMED 2026-11-15T21:41Z UTC for the cold pass, in Mike's weekly Fable drain (his
      `/fable-drain` order, 2026-11-16 06:53 NZDT; approval lapses at the reset,
      2026-11-15 23:00 UTC). Orchestrator: a headless Opus 5.5 session started by drain
      session 21a271a5, a rule-4 off-tier orchestrator that holds the context partition,
      forms no finding and writes no severity. Reviewer: Fable 5.1, tier checked at
      selection, spawned by that orchestrator. Neither is a barred session (deeac927 and
      what it started, 84e3aa7f, 74f2b8cd). The sibling is held out of the worktree until
      act 1 is committed. The item's "waits for the principal's explicit permission for
      Fable work" is met by that drain order.
      ❌ PASS RAN 2026-11-15 UTC (Fable 5.1 reviewer, act 1 committed before the sibling
      opened, act 2 folded with the sibling): **FAIL — 1 MAJOR, 2 MODERATE, 3 minor, 2 notes**
      (`CW1`–`CW8`, verdict in the brief). Standing MAJOR, `CW1`: a `for` loop is one command
      with one result, so one result stands for every worktree it names; a failed iteration
      lists a worktree that was never made, and a failing last one hides every one that was.
      🎯 **The principal's to rule (rule 3; recorded, nothing applied):** MAJOR first. `CW1` as
      above. MODERATE: `CW2` the loop scanner reads no quotes, so the word "for" in a commit
      message leaves a loop open and a later add is expanded into guessed paths; `CW3` the
      `FOR_HEAD` pattern backtracks in cubic time on a long whitespace run. Then minor `CW4`
      (nested loops expand without a cap), `CW5` (an arithmetic `for ((…))` loop is half
      read), `CW6` (the count line's unit and causes), notes `CW7`, `CW8`, each with counsel in
      the verdict. One awareness point from the reviewer: `CW1`'s counsel reads git's result
      text, which widens what the block treats as evidence, a design choice. *Recommendation,
      for one bulk ask:* approve the counselled fixes as a list, `CW1`–`CW3` first, landed
      together with their fixture tests. *Routing:* fixes land in atelier (`instruments/ccclose`,
      its tests, design note and man page, `CHANGELOG.md`), then a re-pass on the fix.
