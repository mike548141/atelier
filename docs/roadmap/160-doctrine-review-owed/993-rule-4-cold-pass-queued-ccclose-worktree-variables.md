- [ ] 🎯 **Rule-4 cold pass queued: `ccclose` resolves a shell variable in
      a worktree add's path and drops one it cannot, and pins the
      committer-date window (`210/330`, `210/320`).** `ccclose`'s
      identifiers block is pasted into records as fact. So the authoring
      session (a principal-opened Opus 5.5 queue run, session 4c65083c,
      2026-11-03, which dispatched the Sonnet worker that wrote the code)
      queues this and does not take it.
      *Tier:* Fable, the principal-named review tier, checked at selection.
      *Pass type:* code cold pass, per `method/REVIEW.md` rule 4.
      *Delta, scoped to paths:* `instruments/ccclose`,
      `instruments/ccclose.test.js`, `instruments/ccclose.design.md`,
      `instruments/man/ccclose.1`, `CHANGELOG.md` (the two commits that close
      `210/320` and `210/330`, on `main`, 2026-11-03).
      *Intent records:*
      [`../210-instruments-open-features/330-ccclose-lists-a-worktree-path-with-an-unexpanded-variable.md`](../210-instruments-open-features/330-ccclose-lists-a-worktree-path-with-an-unexpanded-variable.md),
      [`../210-instruments-open-features/320-ccclose-misses-author-backdated-commits.md`](../210-instruments-open-features/320-ccclose-misses-author-backdated-commits.md).
      📝 BRIEF WRITTEN 2026-11-09 by session d4a0fcf3 (Opus 5.5, headless,
      started by coordinating session 74f2b8cd; neither authored this delta):
      `docs/reviews/2026-11-09-0207-ccclose-worktree-variables-cold.md`, with
      its `.deferred.md` sibling. Pass size: small. Review NOT run: this pass
      waits for a criterion-passing cold Fable session and the principal's
      explicit permission for Fable work. Neither named session may run it.
      🔒 2026-11-22T22:23Z: claimed for the Fable pass by a headless per-pass
      orchestrator, session a8755ef4 (Opus 5.5, rule-4 off-tier orchestrator:
      it holds the partition and forms no finding), started by drain session
      eca14b23; the reviewer is a Fable 5.1 subagent, tier checked at
      selection. Neither is barred by the brief. The approval this item waits
      for is his drain order of 2026-11-23, verbatim: *"Start a fable drain or
      whatever it is called now. Target 100% of weekly budget by 11.30am NZT
      todat"*. The held-back sibling is partitioned out of the review tree
      until act 1 is committed.
      ✅ PASS RAN 2026-11-22 UTC (Fable 5.1 reviewer under orchestrator
      session a8755ef4, drain session eca14b23; acts 1 and 2 written, the
      sibling and the review log folded into the brief):
      **PASS-WITH-FINDINGS — 1 MAJOR · 1 MODERATE · 3 minor · 3 notes
      (WT1–WT8).** Standing MAJOR, WT1: the "assigned earlier in the
      transcript" rule reads a variable the shell no longer had (shell state
      does not survive a tool call), so `ccclose` can list a worktree at a
      path that was never made. MODERATE WT2: a non-literal reassignment or
      `unset` leaves the earlier literal in force. Minor WT3 (scope-blind
      assignment scan), WT4 (subagent caller passes an empty variable map and
      drops its count), WT5 (the snapshot is untested); notes WT6–WT8
      (wording; `$HOME` and `${VAR:-default}` are dropped, never guessed).
      `210/320` (committer-date window) is sound.
      🎯 Owed to the principal (rule 3, every finding is doctrine by
      function): rule WT1–WT8. Counsel in the brief: for WT1, read variables
      from the same command only, or prove persistence per harness, and open
      a follow-up on the message-file reader (`210/310`), which shares the
      assumption (the reviewer's counsel; the orchestrator forms no view).
      Routing: once ruled, the fixes go to the instruments section (`210`)
      as `ccclose` items.
