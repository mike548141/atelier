- [ ] 🎯 **Every guard declares the purpose it answers to, and proves it fires
      on its own grounding incidents — Mike's call, and it is the answer to the
      question he actually asked.** The axis is not narrow versus wide. It is
      what a guard is *organised around*: a detectable feature, or the purpose
      the feature proxies for. Neither is safe. Feature-based guards do not
      erode — they are born aimed off, and `datescan` is the measured case. But
      `stampscan` is the most purpose-shaped guard in the tree and enforces the
      **inverse** of its own doctrine, so purpose-shaped is not protective
      either. A purpose-based guard formalised wrongly is worse, because it
      looks principled and nobody re-derives it.
      **The defect is that the organising principle is undeclared.** Every
      registry entry already carries a `why`. It is printed and never compared
      to anything, and the asymmetry is the finding: **the estate demands a
      reason for weakening a guard and no reason for building one.** Read as
      purpose statements the sixteen strings split — some name an outcome, some
      restate the check's own mechanism in a purpose's clothes. The second kind
      has nothing to be tested against.
      **The one time a guard was tested against its purpose it found what eight
      rule-level findings had all missed.** That section labelled itself
      *(reviewer, mandatory)* and is mandated nowhere; it appears in one of 109
      review files.
      **Four fields, each with a working precedent in this tree:** the rule it
      serves, **by citation, never restated** — which would have caught the
      inversion on day one; the grounding incidents plus **a replay proving the
      check fires on them**, already mechanised in two scanners as canary
      suites; the **purpose gap** — what the rule needs that the check does not
      measure — already a convention in 7 of 15 docstrings; and the evidence
      window from item `010`.
      **Citation is not catch.** The accepted review of the inverted guard
      verified that it named its source correctly, and passed the tool.
      **External grounding, and it is unusually strong.** Reward-hacking theory
      gives a near-impossibility result: over all stochastic policies, two
      objectives can be non-divergent only if one of them is constant. A
      non-trivial proxy that can never drift from its goal essentially does not
      exist. So the answer is never a better proxy — it is measuring the gap.
      Property-based testing supplies the empirical half: hand-seeded fault
      studies rank validity-style properties worst, missing five bugs of eight,
      because a suite that only checks *the shape is well-formed* is satisfied
      by an implementation that throws all the data away.
      **A mandatory rationale field is shipped prior art, not a proposal.**
      Clippy requires a *"Why is this bad?"* section on every lint, with a
      *"Known problems"* slot beside it for the scope limits — which is exactly
      the purpose-gap field above. Sonar's rule format goes further: *"Why is
      this an issue?"* is its **only mandatory section**, and a validator errors
      on a rule that omits it. ESLint is the instructive outlier — it enforces
      document *structure* in continuous integration while mandating no
      rationale, and it is also the project that deprecated 77 rules in one
      stroke once their reason for existing had moved to another tool.
      **And the replay has a name in the literature: defect injection.** The
      established way to grade a rule set is to inject the defect class the
      rules exist to catch and count what they miss — every miss is a rule bug,
      and there is no ambiguity, because the injected defect is real by
      construction. The cheap first diagnostic from the same work is one this
      estate could run tomorrow: **what fraction of rules has even one test
      case that exercises it?** It caught two mature analysers at 79% and 73%.
      **A drift definition worth adopting with it.** Large-scale practice
      defines an *effective* false positive as a report nobody acted on,
      whether or not it was correct — so a guard has drifted when it is still
      right and still ignored. That is measurable here, and it is the bar the
      section's cost item says the estate currently has no positive branch for.
      **The honest cost is the same one item `010` names:** on this evidence at
      least four current guards fail the bar today.
