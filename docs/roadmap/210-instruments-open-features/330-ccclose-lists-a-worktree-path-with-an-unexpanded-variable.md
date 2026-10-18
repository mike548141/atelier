- [ ] 🔎 **`ccclose` lists a worktree whose path held a shell variable
      under a made-up path.** Found 2026-10-18 on a queue run's own close.
      The run created a worktree with `W=<abs path> && git worktree add
      --detach $W origin/main`. The identifiers block listed it as
      `~/.pets/atelier/$W (detached) — worktree put away`: the literal
      `$W`, joined to the command's cwd. The real worktree was listed
      correctly on its own line from `git worktree list`, so nothing was
      lost, but the block is pasted as fact and now carries one entry
      that never existed. **The likely fix:** `worktreeAdds` resolves
      variables the way `210/310`'s message-file reader does (a literal
      assignment earlier in the transcript), and drops a path it cannot
      resolve rather than guessing one.
