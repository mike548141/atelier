- [ ] 🔎 **The withdrawn-review convention rests on a premise that now has a
      counterexample.** `docs/reviews/withdrawn/README.md` rule 5 states that
      findings die with the pass, on this reasoning: *"If a finding is real, the
      accepted pass finds it independently — and that is the point of the
      redo."* Three of the quarantined 2026-07-26 findings were indeed re-found
      independently by the accepted passes, which is the rule working. The
      inversion finding above was not. It is real, it is still live, and it
      survived only because a later research sweep happened to read the
      quarantine directory.
      **What this does and does not license.** It does not argue for reinstating
      rejected passes — the tier bar is Mike's and the rejection stands, content
      unassessed. It argues that *findings die* and *findings are re-found* are
      two claims, and the convention states the second as the ground for the
      first while nothing checks it. One instance grounds a clause, not a build
      (`PROPAGATION.md` rung 2), so the cheapest honest answer is a sentence in
      the withdrawn README saying the re-finding is an expectation rather than a
      guarantee, and that a quarantined pass may be read for defects once its
      accepted replacement is written.
      **This is instance one.** Recorded so a second instance has something to
      join, not built.
