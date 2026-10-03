- [ ] 🔎 **`GUARDS.md` § Adoption assumes every guard can install
      advisory-first, and a guard with no advisory form cannot** `[S][doctrine]`
      Found 2026-10-03 by the G3 build (`150`). The section says adoption is
      "a deferment at repo granularity: the guard installs advisory-first,
      with a reason and an expiry". `leakscan` has no advisory form (E6a,
      `SECRETS.md`), and `floor.py` refuses a dated block. So a new
      *blocking* leakscan rule has no lawful adoption-time deferment. Its
      only adoption path is acceptance at file granularity, in the commit
      that meets it. For G3 that is 152 files across 7 children.
      Children float at `floor.yml@main`, so that commit is forced by their
      next CI run, not chosen at a pin bump.
      **Proposed text, from the build, not applied:** "A guard with no
      advisory form cannot install advisory-first. It adopts by acceptance
      at file granularity in the same commit, each item reasoned and, where
      content can change, bound to its hash. A deferment form for such a
      guard is the principal's call." Whether that is the rule, or whether
      E6a gets an adoption-time exception, is a ruling. It is the first
      decision in PR #97.
