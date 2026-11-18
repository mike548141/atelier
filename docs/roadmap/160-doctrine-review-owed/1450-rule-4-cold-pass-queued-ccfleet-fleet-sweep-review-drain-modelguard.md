- [ ] ⏳ **Rule-4 cold pass queued: `ccfleet`, the `fleet-sweep` and
      `review-drain` skills, and `modelguard` (`210/440`).** A first-of-kind
      instrument that starts headless sessions with a permission mode
      across every repo, two skills that reach every plugin user, and a
      hook that denies tool calls, so the authoring session (559edaec, Opus
      5.5, headless, started by an estate health sweep, orchestrator session
      58027096, 2026-11-14) queues this and does not take it or brief it.
      *Tier:* the principal-named review tier, checked at selection.
      *Pass type:* code and design cold pass, per `method/REVIEW.md` rule 4.
      *Delta, scoped to paths:* `instruments/ccfleet`,
      `instruments/ccfleet.example.json`, `instruments/test_ccfleet.py`,
      `instruments/README.md`, `skills/fleet-sweep/`,
      `skills/review-drain/`, `tools/modelguard.py`,
      `tools/test_modelguard.py`, `tools/README.md`, `CHANGELOG.md` (the
      commit that lands `210/440`, on `main`, 2026-11-14).
      *Intent record:*
      [`../210-instruments-open-features/440-ccfleet-per-repo-billed-headless-sessions-and-two-skills.md`](../210-instruments-open-features/440-ccfleet-per-repo-billed-headless-sessions-and-two-skills.md).
      No brief yet: a brief-writer that is not session 559edaec writes it.
      **Widened 2026-11-18 (session 84b7932e, board `450/010`):** the
      delta now also covers the three commits that closed `ccfleet`'s
      generic gaps and added to both skills (`17f158d2`, `d9d1589e`,
      `a025636e`, landed by `a025636e`). Write the brief over the code as it
      stands at that head, so the paid pass reviews what will run. Neither
      session 559edaec nor session 84b7932e (which commissioned the gap
      fixes) writes the brief. **This pass gates the estate's drain switch**
      (`450/010` row 2): the principal chose, 2026-11-18, to switch the
      weekly drain only after this pass is clean, and for this one pass
      *"Normal priority (Recommended)"* (his pick; the rest of `450`'s
      passes are low). **Drain priority: normal (principal, 2026-11-18).**
      **Widened again 2026-11-18:** add `1eb42f54` (three faults the first
      real estate run found: fresh `kit_dir`, failing queue `next`, dry
      passes' `END` line). The brief covers `main` at or after it.
