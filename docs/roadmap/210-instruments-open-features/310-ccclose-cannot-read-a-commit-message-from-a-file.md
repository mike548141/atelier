- [x] **DONE 2026-10-18** (wt: atelier-qr-210-310)
      🔎 **`ccclose --identifiers` marks a session's own commit
      "unconfirmed" when the message came from a file.** Found 2026-10-18
      by the worker that built `210/290`, measured on that run's own close.
      The evidence tier reads commit subjects from the command text (`-m`, a
      heredoc, `-F -`). A commit made with `-F <path>`, or with the message
      in a shell variable, leaves no subject in the transcript, so it falls
      to "unconfirmed". This errs the safe way: nothing is over-credited.
      But it makes a careful session hand-check commits it really made. In
      the worker's probe, two recent sessions had most or all of their
      commits unconfirmed this way. **Shapes to weigh:** resolve a literal
      `-F <path>` from an earlier Write call or heredoc in the same
      transcript; for a variable path, say so on the unconfirmed line; or
      have the doctrine prefer `-F -` with a heredoc, which the tool already
      reads.
      ✅ **Fixed 2026-10-18, `e78b6f1`.** A `-F <path>` / `--file=<path>`
      commit is now credited when the session (or a subagent) wrote that
      file itself, with its Write tool or a `cat`/`tee` heredoc. Exact path
      equality after resolving against the command's cwd and any `git -C`,
      never a basename. A `$VAR` path resolves only from a literal
      assignment earlier in the same transcript. Within one transcript the
      latest earlier write wins. Probed on its own session: `692c04a` moved
      from unconfirmed to confirmed. Limits, stated in design note §15.1:
      `echo`/`printf`/editor writes and messages held in a variable are not
      read, and `/tmp` vs `/private/tmp` compare as written. 65 ccclose
      tests, 489 node and 1949 Python tests green. Reviewed with `210/290`
      under `160/960`.
