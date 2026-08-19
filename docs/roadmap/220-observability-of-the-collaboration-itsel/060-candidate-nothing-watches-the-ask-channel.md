- [ ] **Candidate — nothing watches the ask channel, so the ruling-ask rule is
      write-time discipline only.** `COMMUNICATION.md` § *Asking for a ruling*
      (landed 2026-08-19) makes the structured device the default channel for
      decisions and rulings. No plane can see whether a session obeyed it:
      `plainscan` reads committed prose, and an ask lives in the reply, not the
      repo. The reply plane that once watched agent output is unwired (Mike,
      2026-08-15) and its remedy — not its detection — is what failed.
      **What is conceivable, stated as conjecture rather than a design:** the
      transcript records tool calls, so device-asks are countable after the
      fact; whether a *prose* ask is separable from an ordinary reply is
      unprobed, and that is the question this item turns on. `cctranscript`
      is the instrument to try it against before anything is built
      (`010-…`/`020-…` above are its two siblings in this section).
      Unfunded. Do not price a detector off this text — probe first.
