- [ ] **C3 — a sanctioned adoption path.** A repo whose existing content
      already fails the gate **cannot commit the change that installs the
      gate.** It happened twice during the rollout and was resolved with a
      documented one-time bypass — defensible once, but it is now an
      undocumented pattern that recurs on *every* future adoption. Decide the
      pattern before the next adoption, not during it: either a sanctioned
      bootstrap, or an adopt mode that installs the hygiene checks
      advisory-first and tightens on re-baseline.
