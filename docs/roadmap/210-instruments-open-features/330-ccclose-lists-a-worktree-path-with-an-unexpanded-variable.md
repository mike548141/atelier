- [x] **DONE 2026-11-03** (wt: atelier-qr-4c65-ccclose) 🔎 **`ccclose` lists a worktree whose path held a shell variable
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
      ✅ **Fixed 2026-11-03.** `worktreeAdds` takes the transcript's
      variables and expands `$NAME` / `${NAME}` in the path, and in the `cd`
      or `-C` directory a relative path resolves against, from a literal
      assignment earlier in the same command or the transcript (the
      `210/310` reading). A path it cannot resolve (unset variable,
      `$(...)`, backticks) is dropped, never joined to the cwd; an unknown
      directory drops only a relative path. A prefix assignment
      (`W=/p git worktree add $W`) is not counted, since bash expands `$W`
      before it is set. Tests: resolved assignment, assignment from an earlier
      command, unresolvable dropped, plain literal unchanged, and a transcript
      run with the block printed. Man page and design note updated.
