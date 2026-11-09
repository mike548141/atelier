- [x] 🎯 **Confidence on a fact: stored field, or computed? Mike's call, and it
      has never been put to him.** Mike named confidence in his own vocabulary
      on 2026-08-15 — *"what is our confidence level in the fact"* — as part of
      the provenance metadata he has discussed alongside the time dimension. The
      only build that faced the question decided it unilaterally: a child repo's
      2026-08-09 decision record rejected a stored confidence score on the
      ground that *"we cannot defend the numbers, and a scale we invented would
      be a claim stronger than its evidence... The method is the fact; a policy
      can map methods to weights when a policy exists and has to justify
      itself."* That reasoning is the agent's, not a ruling. Under the
      informed-principal duty it is exactly the shape of decision that should
      not have settled at build altitude.
      **Three readings are consistent with the record, and they build different
      things.** (a) *Computed* — store acquisition method and record time, no
      confidence field; a policy maps method to weight when a policy exists.
      (b) *Stored and coarse* — a ranked field, defensible because categorical
      rather than numeric. (c) *A decision bar, not data* — confidence governs
      whether an inferred fact is admitted at all, which is how Mike used it in
      his 2026-08-09 allergen ruling.
      **Counsel: (a), with (b) available where confidence genuinely varies
      within a single method.** External practice agrees — the systems that ship
      express confidence as source plus method plus a coarse rank, and a bare
      per-fact confidence number is a documented anti-pattern. But the counsel
      is not the ruling, and the child repo owns the fix either way under the §9
      scope clause.
  - [ ] 💬 **Mike's answer, 2026-11-09 (to options queue run 722ac2e2 offered; an answer,
        not a ruling):** *"Work it out from the source"*: confidence is computed from how a fact was obtained, with a rough rank only where one method varies.
  - [x] ✅ **DONE 2026-11-09 — APPLIED** by queue run 722ac2e2 (a Sonnet worker, read by the orchestrator before landing): `PRINCIPLES.md` §9 and a pointer in `EVIDENCE.md` §3. House rule only; a child builds it.
