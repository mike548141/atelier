- [~] (claimed 2026-11-03-1130, wt: atelier-qr-deea-ccclose)
      🔎 **`ccclose --identifiers` drops a worktree made in a shell loop,
      and the block does not say it dropped anything.** Found 2026-11-03 on
      queue run 4c65083c's own close, hours after `210/330` landed. The run
      made eight worktrees with `for n in a b; do git worktree add …
      /abs/atelier-qr-4c65-$n …; done`. `210/330` resolves a `$VAR` only from
      a literal assignment and drops one it cannot resolve, by design, so a
      loop variable is dropped: the block listed 5 worktrees of the 13 the run
      made and put away. Nothing false was printed, which is what `210/330`
      was for, but a block pasted as the record's identifiers now under-counts
      silently. **Shapes:** print a count line, "N worktree adds not resolved
      (a variable with no literal assignment)", so the reader knows to fill
      them in; or expand a `for` loop's literal word list.
