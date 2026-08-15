- [ ] **Single-source the scanner harness, re-grounded on Mike's own upstream
      test.** The finding already exists: GA1, a minor raised by the 2026-08-05
      guards-and-allowances cold pass and still awaiting its ruling round. It
      reads that the reason-required loader is ten per-scanner copies, *"the
      propagation mechanism the build's own survey diagnosed"*, and counsels
      single-sourcing it or recording standalone copies as the decided design —
      *"either answer, not silence."* This item does not restate that finding;
      it adds the evidence that has landed since, and the test that decides it.
      **What landed since.** On 2026-08-09 the duplication produced exactly the
      defect it predicted: a shared parsing rule, copied per scanner, silently
      voided nine live allow-markers across three children. A voided marker and
      an absent one produce identical output, so it survived a review that had
      explicitly triaged one of the affected lines. The fix took fourteen regex
      sites across twelve files. Beyond the loader, the divergence is already
      real rather than latent: `datescan` requires a word boundary and a
      non-empty reason where several siblings accept a bare substring match.
      **A second gap, found while writing this section.** `plainscan` has no
      allow-marker grammar at all — no marker constant, no reason parser, no
      suppression path. So a verbatim principal quote, which must not be
      reworded, cannot be exempted from its long-sentence rule at any
      granularity. Two findings in this section's own README are exactly that
      and are left standing. Tolerable while the check is warn-only; less so
      since its repo plane was rescoped to the prose Mike reads, which is what
      board files are. A shared grammar would give it one for free.
      **The test that decides it is Mike's own** (2026-07-19, on fixing upstream
      rather than accumulating downstream mitigations): a fix is downstream when
      correcting it requires patching N separate locations and the next
      correction will require N more. Ten to eleven copies, fourteen sites, is
      that signature.
      **Scope, if funded:** one ignore-file loader, one allow-marker grammar,
      one exit and reporting contract, and namespaced finding identifiers so a
      rule stays individually suppressible. The precedent is unanimous on the
      last point — every mature engine consolidated the engine and kept the
      rules granular. **Explicitly not in scope:** merging any two guards'
      *intents*. No precedent found does that, and one suppression would then
      silence a whole concern.
