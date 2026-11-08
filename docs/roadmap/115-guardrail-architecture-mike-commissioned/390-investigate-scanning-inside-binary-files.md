- [ ] 🤔 **Investigate scanning inside binary files.** No guard reads a
      binary's contents beyond image metadata: not pixels, not the insides of
      other formats, and `secretscan` reads no binary at all. So an exemption
      over a binary can only cover the whole file, and a secret or personal
      detail inside one is unseen. Filed 2026-11-09 by queue run 722ac2e2 on
      Mike's answer to the exception-register redraft's Q4 (*"Separate
      investigation"*, an answer to options offered), kept out of that design
      (`160/650`). Scope: which binary kinds the estate actually tracks, what
      each could hide, and what reading them would cost; ranked by value like
      any other work (`020/240`).
