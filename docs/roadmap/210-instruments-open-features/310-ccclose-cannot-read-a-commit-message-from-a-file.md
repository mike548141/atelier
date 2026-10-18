- [ ] 🔎 **`ccclose --identifiers` marks a session's own commit
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
