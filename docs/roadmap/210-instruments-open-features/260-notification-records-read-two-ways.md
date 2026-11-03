- [x] 🔎 **A harness notification reads two ways depending on its record
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

      ✅ **Done 2026-11-03** (queue run 4c65083c, a Sonnet 5.5 worker).
      `cctranscript` now reads the notification the same way whichever record
      carries it. An `attachment` · `queued_command` record with command mode
      `task-notification` (origin absent or its own) is a grey `harness` turn,
      counted in the header chip and found by `--search` as harness. **It
      opens no exchange and has no ref** (`null` in `--json`): `250` kept the
      number for harness text that was already a user record, but this
      channel was never read, so numbering it would have shifted every ref
      already quoted in committed records, which is the thing `250` set out
      to protect. Replies after it keep counting under the exchange they sit
      in. Census of about 980 real records: every one has that command mode,
      a string prompt opening with the tag, and no other shape. Left out on
      purpose: a peer's cross-session message (another agent's words, not a
      harness event), a typed prompt, every other attachment type, and any
      unrecognised mode or origin. `ccclose` needed no code change since it
      never numbered these; a test pins that its exchange numbers and ask
      refs are identical with and without such records. Review queued at
      `160/991`.
