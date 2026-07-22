# Cold pass — the applied SL1–SL7 batch (delta `d553045`)

- **Date/time**: 2026-07-22 0244 UTC
- **Spawn provenance (rule 4)**: taken from the ROADMAP `⏳` queue by a session
  Mike opened and pointed at the queue ("please do any review work"). This
  session authored **none** of: the scope-mandate/lens-4 doctrine deltas
  (`f9db922`, `a059e49`), the 2026-07-21 cold pass that produced SL1–SL7, or
  the application of Mike's accept-all ruling now under review (`d553045`).
  The applier queued the `⏳` pointer and stopped; this brief is taker-written.
- **Named exposure**: at selection the taker read (a) the ROADMAP `⏳` pointer,
  (b) `d553045`'s commit message — which carries the applier's evaluative
  account of SL1–SL7 ("red leg proven", "suite 298→302 all green") — and
  (c) `docs/method/REVIEW.md` in full at HEAD, unavoidable twice over: it is
  needed to run the process and it is the primary artefact under review.
  Every evaluative claim in (b) is treated as a claim to re-run, not a fact.
  An application review cannot fully honour rule 2 — the sequence per
  REVIEW.md § Applying decisions: review the edited files at HEAD and commit
  findings *first*; open the prior verdict, decision stamps, and applier's
  intent record after. The residual exposure is named, not denied.

## What the work is (refs only)

Commit `d553045` — the application of Mike's 2026-07-22 accept-all ruling on
the 2026-07-21 cold pass's SL1–SL7 findings. In-scope files at HEAD:

- `docs/method/REVIEW.md` (SL2 — lens-4 scanner sentence rewritten
  reach-per-shape; SL5 — "scoped and short" reconciled, non-goals reviewable;
  SL6 — live-exercise impossibility states grounds; SL7 — reflow/rewrap)
- `skills/review-brief/SKILL.md` (SL1 — scope mandate + four-lens roster
  incl. security & privacy)
- `tools/test_templates.py` (SL1 — `LensRosterParityTest` mechanical parity
  floor)
- `docs/build/templates/CONTRIBUTING.md` (SL3 — review sentence carries the
  whole commitment)
- `docs/build/templates/docs/reviews/README.md` (SL4 — "correctness only"
  Type replaced with commitment-shape semantics)

**Deferred below the divider** (opened only after this reviewer's findings are
committed): the prior verdict file
`reviews/2026-07-21-2158-review-scope-security-lens4-cold.md`, the decision
stamps (`913c81a`), and the applier's intent record
`sessions/2026-07-21-2208-scope-lens4-cold-pass.md` (+ addendum).

## Ask

Run all four lenses on the applied delta; scope is the whole commitment.

1. **Approach & assumptions** — name the load-bearing assumptions first, then
   attack them. Does each applied fix discharge the finding class it claims
   to, or patch the instance? In particular: does the parity test genuinely
   pin skill↔doctrine lens parity (or is it a trivially-green fence)? Does
   the reach-per-shape scanner sentence keep lens 4's floor, or does the
   discharge line open an easy out?
2. **Correctness & quality** — re-run every live proof in scope rather than
   reading it: the full suite (claimed 302, all green); the parity test's
   red leg (revert the skill hunk → the suite must go red); the repo floors
   (linkscan, sizescan, reviewscan, secretscan/leakscan via the hooks).
   Honest-labelling check: is the skill still a compression that never
   contradicts the parent (its own stamped-copy rule)?
3. **Completeness / harvest** — anything the rulings required that the
   application skipped; any template or sibling doc carrying the retired
   wording the sweep missed; record hygiene consistent with the delta.
4. **Security & privacy** — per the (new) lens-4 text itself: this is a
   landed-delta review of markdown doctrine + a stdlib-only test file; the
   harness scanner (`/security-review`) reads pending diffs and its
   exclusions bar markdown, so it cannot genuinely be aimed at this work —
   discharged on those grounds, per the rule under review. The lens still
   runs manually: injection/exec surface of the new test code, and
   design-altitude leakage in the doctrine/template text.

Cycle context: MAJORs were present in the prior pass, so this application
inherited rule-4 status; this pass is **terminal if it returns no MAJOR**
(close rule) — report findings either way; decisions are Mike's (rule 3:
the chain is self-authored doctrine).

---

## Deferred material (open only after findings are committed)

- `docs/reviews/2026-07-21-2158-review-scope-security-lens4-cold.md`
- `git show 913c81a` (decision stamps + queue records)
- `docs/sessions/2026-07-21-2208-scope-lens4-cold-pass.md`
- The author seeded no questions; there is no author-written ask anywhere in
  this file. Everything above the divider is taker-written.
