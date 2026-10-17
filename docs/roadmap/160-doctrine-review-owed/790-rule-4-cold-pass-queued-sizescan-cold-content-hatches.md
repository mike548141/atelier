- [ ] ⏳ **Rule-4 cold pass queued: no hatch silences sizescan's cold-content
      gate, and the gate lists the items (`115/270` parts a and b).** The run
      authored this itself (its dispatched worker's output counts as the
      run's authorship). It is queued at landing, and the run neither takes
      it nor spawns a reviewer for it. *Tier:* Fable, the principal-named
      review tier, checked at selection. *Pass type:* code cold pass, per
      `method/REVIEW.md` rule 4. *Delta, scoped to paths:* `tools/sizescan.py`,
      `tools/test_sizescan.py`, `tools/test_report.py`, `tools/pointerscan.py`
      and `tools/README.md`, commit `f9ccba8` and merge `ccfad42`, landed on
      `main` on 2026-10-16. *Intent record:*
      [`../../sessions/2026-10-16-0703-queue-run-after-the-sizescan-ruling.md`](../../sessions/2026-10-16-0703-queue-run-after-the-sizescan-ruling.md).
      **Brief WRITTEN 2026-10-17, review NOT run** —
      `docs/reviews/2026-10-17-0930-sizescan-cold-hatches-cold.md` with a
      `.deferred.md` sibling. Written by an Opus brief-writer that authored none
      of the delta (dispatched by the Mike-opened Fable review session, wt
      atelier-review-1017), on Mike's 2026-10-16 answer that a fresh Opus
      session writes these briefs; its exposure is disclosed in the brief. The
      pass stays queued for a further criterion-passing cold Fable session.
