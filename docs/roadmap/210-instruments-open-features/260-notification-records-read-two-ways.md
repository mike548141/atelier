- [ ] 🔎 **A harness notification reads two ways depending on its record
      type** `[S][instruments]`. Found 2026-10-16 by the `250` worker, not
      fixed there. Since `250`, a background-task notification that arrives
      as a user-type record shows in cctranscript as a grey `harness` turn.
      The same notification arriving as an `attachment` or `queued_command`
      record is not read at all, so it is invisible. Neither is wrongly
      credited to the principal, so nothing is misattributed. But one
      event looks different depending on how the harness happened to write
      it. **The work:** decide whether those records should show as harness
      too, keeping exchange numbers stable (the `250` rule), and keep
      `ccclose`'s refs in step.
