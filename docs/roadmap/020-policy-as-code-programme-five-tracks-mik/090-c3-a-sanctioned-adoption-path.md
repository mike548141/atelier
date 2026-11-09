- [x] **C3 — a sanctioned adoption path.** A repo whose existing content
      already fails the gate **cannot commit the change that installs the
      gate.** It happened twice during the rollout and was resolved with a
      documented one-time bypass — defensible once, but it is now an
      undocumented pattern that recurs on *every* future adoption. Decide the
      pattern before the next adoption, not during it: either a sanctioned
      bootstrap, or an adopt mode that installs the hygiene checks
      advisory-first and tightens on re-baseline.
      - [x] ✅ **Closed 2026-11-09 as delivered — the sanctioned adoption path exists.**
            Re-verified: `tools/floor.py` (the "NOTHING IS SILENTLY ABSENT" block,
            about lines 96-123) declares `advisory` per check with a required `why` and
            `review-by` (C1); `skills/create-repo/SKILL.md` step 6 sends a repo that
            must re-baseline to `.atelier-floor.json` advisory, never to a dropped
            scanner; `docs/method/GUARDS.md` § *Adoption* decides the pattern (a
            deferment at repo granularity, with a reason and an expiry). The one gap
            this item left, a guard with no advisory form (leakscan), is not part of
            it and is carried by `020/410`. The same sentence in `GUARDS.md` that
            called C3 "the open build" is corrected in this commit.
