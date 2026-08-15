- [ ] **P4 — `rpi` F9, routed upward: the ci plane calls `leakscan` without
      `--require-terms`.** Every child's CI run therefore self-reports "cover not
      guaranteed". The fix belongs in atelier's registry, not any child — it
      pairs with Track D's registry work; the design question is whether CI can
      carry a term list at all (the list lives in `~/.claude/`, outside every
      repo, which is why the ci plane was left structural-only in the first
      place). If it cannot, the honest fix is a rendering change so "structural
      only" stops reading like a defect.
