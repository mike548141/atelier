- [ ] 🔎 **`PROPAGATION.md` calls a parent enforcing what its children do not
      a defect, while atelier's CI deliberately runs checks only atelier can
      run.** Found 2026-11-16 UTC by the `020/220` census, slice 2. `stampscan`,
      `blockscan` and the signature checks run on atelier and on no child, by
      design: they check what only the parent holds. The rule's text does not
      carve that class out, so read literally it calls the design a defect.
      **Owed:** say in the rule which checks are parent-only by nature and
      why, so the rule and the practice agree. Not fixed in passing.
