- [ ] ⏳ **Rule-4 cold pass queued: `ccclose` resolves a shell variable in
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
