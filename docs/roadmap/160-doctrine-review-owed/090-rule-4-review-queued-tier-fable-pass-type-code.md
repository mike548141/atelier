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
      `[~]` **RULED 2026-08-23** — the live ruling round ran by structured
      asks; dispositions in the verdict file (§ *Rulings — 2026-08-23*).
      AP1: re-word to the truth by appended amendment, boundary check
      queued; branch protection deliberately not enabled. Application in
      flight on wt: ruling-round-0823.
      - ⏳ **Rule-4 cold pass queued — the AP rulings applied.** The ADR
        amendment is doctrine by function; the applier authored neither the
        EP delta nor the AP verdict (Mike directed the application in the
        live ruling round, 2026-08-23, structured asks). Queued in the
        application's landing commit; the applier neither takes nor spawns
        it. *Tier:* Fable, checked at selection. *Pass type:* code+doctrine
        cold pass.
        *Delta — scoped to paths:* the 2026-08-23 amendment at the foot of
        `docs/decisions/0008-enforcement-is-called-not-copied.md` (AP1
        truth re-word; AP2 list correction) · `tools/floor.py` (the
        softenable-set docstring) · `.github/workflows/floor.yml` (the two
        `env:`-routed signature steps, AP3) · `tools/leakscan.py` +
        `tools/test_leakscan.py` (the explicit-terms-path error, AP4) ·
        the queued items `115/180`, `020/340`.
        *Intent record:* § *Rulings — 2026-08-23* in
        `docs/reviews/2026-08-09-0824-ep-application-cold.md`.
      `[~]` **CLAIMED 2026-09-25 0705 UTC for the review run** (wt:
      review-batch-0925; brief
      `docs/reviews/2026-09-25-0715-ap-rulings-applied-cold.md`) by a
      Mike-opened `claude-fable-5-1` session ("Please deliver all fable
      dependent work, and work that would be best delivered using fable") that
      authored none of the delta. Shape, disclosed per rule 4:
      reviewer-plus-orchestrator, both seats Fable — this session writes the
      refs-only brief and holds the `.deferred.md` sibling outside the worktree;
      a fresh Fable subagent it spawns forms every finding and severity. The
      sibling, the intent record and prior verdicts stay unopened by the
      reviewer until its phase-1 findings are committed. Provenance and exposure
      go in the verdict.
      - [ ] 🛑 **The pass RAN 2026-09-26 and the cycle stays OPEN — a MAJOR
            stands.** The rule-4 Fable cold pass (taker: a fresh
            `claude-fable-5-1` subagent under a `claude-fable-5-1` orchestrator
            — the shape disclosed in the claim above; the sibling, the intent
            record and prior verdicts opened only after the phase-1 findings
            were committed) returned FAIL — 2 MAJOR · 2 MODERATE · 2 minor · 2
            note →
            [`2026-09-25-0715-ap-rulings-applied-cold.md`](../../reviews/2026-09-25-0715-ap-rulings-applied-cold.md)
            (sibling folded in and deleted). AR1 (MAJOR, security): the
            2026-08-23 amendment says main has no branch protection and no
            ruleset and that signing is warn-first, re-affirmed at the amendment
            — but a ruleset carrying deletion, non-fast-forward and
            required-signatures rules (admin bypass always) has been active
            since 2026-08-09 and was on the board from 2026-08-15, so the ADR
            every child inherits at @main misstates its own control clause at
            writing and at HEAD; AR2 (MODERATE): floorfleet's boundary row cites
            the stale sentence as its authority and never reads the bypass; AR8
            (MAJOR) formed at reconcile. Findings are the principal's to decide
            (rule 3); nothing was applied.
