- [ ] 🔎 **rpi hand-up: a rollout row backwards; wrapscan blind to split boards**
      `[doctrine][tool]`. Handed up from `rpi` (a public repo, so named) on
      2026-10-17 under `PROPAGATION.md` § *Pointing up*: two findings, RB7 and
      RB8, from the rule-4 cold pass on that repo's board split (its review
      record dated 2026-10-03 1151 UTC; a Fable reviewer under an orchestrator
      that formed no finding, disclosed there). Both were formed against the
      child's tree and this repo's files at `main`; the reviewer did not open
      this repo's own review records, so overlap with them is unverified.
      Consideration and remediation are atelier's; the child stops here.
      **1. The fleet-rollout record has rpi's migration backwards**
      `[doctrine]`. `010/030` tabulates rpi as "`4bd429c` | — → 69 | born split
      — no prior `ROADMAP.md`" and builds on it: rpi "never migrated: it had
      no `ROADMAP.md` before `4bd429c`, so its board was *written* in the
      store form from nothing. That is the stronger evidence for the form — it
      is adoptable without a monolith to convert, which no migration could
      have shown." Measured in the child: the file deleted by `4bd429c` is a
      245-line monolith at the repo **root**, not under `docs/` (the rollout
      method looked for `docs/ROADMAP.md` at the parent commit, found nothing,
      and inferred birth). Its conversion was the least mechanical in the
      fleet: none of its 27 bullets used the checkbox grammar, so a mechanical
      split would have produced zero items, and every state was a judgement
      read off prose glyphs. The child's intent record left this hand-up to
      the principal on 2026-08-17 and it was dropped between the two repos.
      *Suggested shape:* correct the row and the inference that rests on it;
      add the glyph-grammar case as the counter-example to a cut that needs
      no judgement.
      **2. The split made every board body invisible to wrapscan** `[tool]`.
      `wrapscan` exempts any line indented four or more columns as code (its
      documented honest limit). A split board's continuation lines are
      indented four or more by grammar (`harvestscan`'s parser ends an item
      under four), so every item body in every split board in the fleet is
      now exempt. Measured on the child's board by its reviewer: raw lines
      over 85 columns rose 180 → 208 across the split while wrapscan's
      flagged count fell 133 → 38 (what remains is the state lines and the
      legend). The child's advisory-wrapscan ruling, due 2026-10-31, would be
      made on a figure that no longer counts the board. *Suggested shape:*
      count list continuations as prose and exempt only fenced code and
      indented blocks no list item encloses; or state in the rollout record
      that the exemption is now systematic, so a width ruling reads the raw
      count. Adjacent: `010/030` (the rollout record), `320/450` (what the
      index projects from a split item).
      review: not warranted — a hand-up of two findings; the cold pass that
      formed them is itself the review, and the fixes are atelier's to decide.
