- [~] (claimed 2026-09-20-0540, wt: qr0919-blockcopy-check) 🎯 **A ruling that changes doctrine has no check that the child
      block's copy of the rule moved with it** — split out of `320/250`
      2026-09-18, which fixed the instance and left the question.
      The standard child doctrine block is the one place a lossy copy of a
      rule is sanctioned, so it is the one place a *falsified* copy is hardest
      to notice: DA1's ruling reworded the ask rule in `COMMUNICATION.md`, and
      the block — plus the scaffold template that stamps it — kept the
      overturned wording for weeks, copied into every child at pin bump.
      This is DA2's class (a duty's other live spellings drift when one is
      corrected) a third time, and the first time the stale spelling was the
      propagating one.
      🎯 **The ask, as the child put it:** should a ruling that changes
      doctrine carry a mechanical check that the block's own copy moved too?
      Nothing is built. Adjacent, not the same: `stampscan` checks a child's
      inlined block against atelier's source, not atelier's block against
      atelier's own method docs; `200/010` is the generic
      hand-maintained-index-stays-true mechanism.
      🎯→✅ **RULED 2026-09-19 by Mike, via the question device: "Build the
      check".** Offered against a doctrine checklist line and leaving it to
      reviews. Spec from the ask he answered: a floor check in atelier that
      fails when a house rule the child doctrine block summarises changes but
      its block bullet (and the scaffold template's copy) does not change in
      the same commit — or that forces an explicit "block still true"
      acknowledgement; false alarms clear with a scoped allow-marker. The
      build is owed; the mapping from block bullet to source section is the
      first design question (the block's bullets already name their source
      docs).
      ✅ **BUILT 2026-09-20 — `blockscan`.** A staged **co-change** rule, not
      a text comparison: a hand-maintained map (`tools/blockscan_map.json`)
      ties each block bullet to the method-doc section(s) it summarises, and
      a commit touching a mapped section must also move that bullet in
      **both** `PROPAGATION.md`'s floor region and the scaffold template — or
      carry `<!-- blockscan:allow: <reason> -->`, reason mandatory. Map
      integrity (every heading and bullet anchor still resolves) is its own
      mode and can never be suppressed. **6 of the floor's 9 bullets are
      mapped**; the other three cite no method-doc section at all.
      **Verified firing, not assumed:** a probe edit inside a mapped section
      produced the violation naming the bullet and both files that did not
      move; the tree was restored immediately.
      🚩 **Wired ADVISORY in atelier's CI only, NOT in the shared floor
      registry** — the worker's call against its dispatch spec, and it is
      right: every path the map names exists only in atelier, so a registry
      line would exit 2 as a config error on every child's hook and CI from
      the moment it merged (the ST3 class `stampscan` already documents).
      **Two residuals, stated rather than hidden:** the pre-commit hook names
      no scanner by design (ADR 0008), so there is no hook-plane seam for an
      atelier-only check and a violation is caught one push later by CI; and
      the map's section extraction is **non-recursive**, which leaves every
      subsection unmapped — filed as `320/340`, with this session's own
      evidence.
      *review: covered by the code cold pass at `160/350`, whose delta list
      names it.*
