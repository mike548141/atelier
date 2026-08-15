- ⏳ **Rule-4 review queued (tier: Fable; pass type: code cold pass, the
  EP application; the EP cycle's three MAJORs keep it open past this).**
  *Delta:* `tools/floor.py` + `tools/floorfleet.py` +
  `tools/pre-commit.sample` + `.githooks/pre-commit` +
  `.github/workflows/floor.yml` + `.github/workflows/ci.yml` +
  `docs/build/templates/workflows/floor.yml` +
  `docs/build/templates/CONTRIBUTING.md` +
  `docs/decisions/0008-enforcement-is-called-not-copied.md` (Decision 6 +
  the Consequences control clause) + the four test files (suite
  1164 → 1178) + the CHANGELOG entry (landed 2026-08-06, this commit) +
  the 2026-08-09 bite-now follow-up on the same surfaces
  (`tools/floor.py` validate + `tools/test_floor.py`, Mike's ruling at
  the close walk-through — the legacy-spelling exemption removed for
  never-softened scanners; delta widened per the landing-commit rule).
  *Intent record:*
  [ADR 0008 cold pass](../../reviews/2026-07-26-2215-adr0008-enforcement-propagation-cold.md)
  (EP1–EP10) + the 2026-08-04 ruling, harvested with the item to
  [`ROADMAP-DONE.md`](../../ROADMAP-DONE.md) § *The EP application*.
  - [ ] 🛑 **The application pass RAN 2026-08-09 and the cycle stays OPEN — a
        new MAJOR stands.** The rule-4 Fable cold pass (taker: a Mike-spawned
        session, claimed 0815 UTC) returned PASS-WITH-FINDINGS — 1 MAJOR /
        1 MODERATE / 2 minor / 4 note; every re-run reproduced (suites at
        HEAD 1210 Python + 207 node, 1164 → 1178 at the landing commits,
        floor validate green both planes, the hook driven live in a scratch
        repo through clean / planted-secret / fail-closed / bite-now) →
        [`reviews/2026-08-09-0824-ep-application-cold.md`](../../reviews/2026-08-09-0824-ep-application-cold.md).
        AP1 (MAJOR): the ADR 0008 control clause names branch protection +
        signed commits + registry review as what makes the floating `@main`
        call safe — a live read shows `main` carries no branch protection
        and no rulesets, signing verification is warn-first, and nothing
        machine-checks the control. Reconcile classified AP1 as a
        *descendant of EP7* — the clause EP7 counselled, now first-checked
        and failing live — while EP1–EP3's substance verified closed at
        HEAD and every in-scope [fixed] claim held. AP2 (MODERATE): ADR
        0008 Decision 2 and the docstring say sizescan has no advisory
        form; the registry, selftest and CONTRIBUTING say it does. AP1–AP8
        join Mike's ruling round; the application of whatever is ruled
        earns its own queued pointer.
