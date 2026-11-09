- [x] **Adoption is a chicken-and-egg problem and I improvised twice.** A repo
      whose existing content already fails the gate **cannot commit the change
      that installs the gate**. It happened on two repos and I resolved it with a
      one-time `--no-verify`, documented in each commit — defensible once, but it
      is now an undocumented pattern that will recur on *every* future adoption
      (including the 3 public repos, if adopted). Idea: a documented adoption
      path — either a sanctioned one-time bootstrap, or an `--adopt` mode that
      installs the hygiene checks advisory-first and tightens once the repo
      re-baselines. **Decide the pattern before the next adoption, not during
      it.**
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
