- [ ] 🎯 **F1 — rebuild the block-vs-advise model from base. REBUILT
      2026-08-05 as [`method/GUARDS.md`](../../method/GUARDS.md); STAYS OPEN until
      the two rulings below are Mike's** (the P6 precedent — the work is
      delivered, the ruling is what remains owed), picked up under
      Mike's instruction to apply his three allowance rules (narrow · noisy ·
      reasoned) to every scanner — the rules are the stated intent this entry
      deliberately left blank so the cold pass would not be steered, and the
      pass has since run and been ruled. FG1–FG6 all discharged; FG4's prior-art
      check moved two claims (Semgrep carries the full three-way split as
      distinct fields and computes severity from likelihood × impact; CVSS v4.0
      quarantines time-varying metrics into its Threat group, independently
      grounding the expiry rule). Rule-4 `⏳` queued below — self-authored
      doctrine, so the review is not this session's to take.
      **🎯 TWO THINGS OWED TO MIKE, both recorded and neither assumed:**
      **(1)** the model supersedes **E6d(i)**'s escalate-only *wording* — the
      substance is kept, the direction-constraint is replaced by the
      provenance-constraint FG2 ruled as the hypothesis to test, and the test
      is written out in the doc. E6d(ii)/(iii) untouched. **(2)** D1's
      consequence, below. Account:
      [`sessions/2026-08-05-1150-guard-governance-allowances.md`](../../sessions/2026-08-05-1150-guard-governance-allowances.md).
      Origin: E6d's
      **escalate-only** ruling. **That ruling stands** (Mike, 2026-08-02) —
      nothing is reverted and no work is blocked on this. But Mike is no
      longer confident it was the right call, so the model underneath it is
      rebuilt from first principles rather than patched. Recorded as an open
      action at his instruction, not as a reversal.

      **The decomposition Mike gave is finer than the one E6d encodes.** E6d
      tiers on confidence × impact. Mike splits it three ways:
      (1) how confident are we that the **identification** is correct — is
      this actually a secret; (2) *given* the identification is true, what is
      the **probability** of a risk or issue eventuating; (3) given it is
      true, what is the **impact** if it does. E6d collapses (2) into (3). A
      correctly-identified credential can carry low probability of harm —
      already rotated, expired, scoped to nothing — and that is a different
      question from how bad the harm would be. Whether the split changes the
      response model is the review's to say, not this entry's.

      **The vocabulary Mike named, recorded as scope — not as answers:**
      **DRY for policy-as-code** — children *run* the shared guards from
      atelier and never copy them out; they may *add* their own for needs the
      shared set does not cover · **a child cannot reduce a shared guard**,
      but may reason about exclusions and acceptance · **declare acceptance
      or deferment** — today one spelling covers both · **report a false
      positive** — a route back to the guard's owner · **resolve vs scope vs
      soften** — three responses to a finding, with no written taxonomy ·
      **side-stepping** — a guard not wired in, overruled, or ignored.

      **Existing items that are instances of this frame** (mapped here, not
      moved — each keeps its own home and owner): run-not-copy is ADR 0008,
      landed, with the repo-local seam for the *add your own* half still at
      **zero adopters (D4)** · cannot-reduce is REPO-STANDARD's
      narrow-not-contradict layering · acceptance-and-deferment is C1's
      `why` + `review-by` and `disabled`'s reason, plus **C2** retiring the
      17 · false-positive reporting is **E1–E4**, every one of them found ad
      hoc with no route back · resolve-vs-scope-vs-soften is what **Track A**
      met as scope fail-opens and C1 met as advisory · side-stepping is
      **C4** (`--no-verify` unobserved), the Actions-disabled blind spot,
      Track A's scope-covering-nothing, and an advisory that never expires ·
      **adoption/first-contact is C3** and the two `--no-verify`-bootstrapped
      children — a repo meeting a guard its existing content already fails,
      twice resolved by documented bypass (mapped in by the FG1 ruling,
      2026-08-03: the cold pass found the original list was steady-state
      only, and adoption is the case a model built without it would distort
      around). That these open items are one frame is the finding; the
      frame is Mike's, not an agent's synthesis of it.

      **Deliberately not pre-solved.** Mike asked for the review to run on the
      *origin problem and possible solutions*, ahead of any design — review as
      an input, not a gate. No candidate model is written here on purpose: an
      entry that proposed one would steer the pass it is queuing, which is the
      breach this file has now recorded three times.

      🎯 **REVIEWED 2026-08-03 (rule-4 Fable design/intent cold pass):
      PASS-WITH-FINDINGS — 0 MAJOR / 2 MODERATE / 1 minor / 3 notes.
      FG1–FG6 await Mike's ruling (REVIEW rule 3); they are counsel feeding
      the rebuild at pickup, per the review-as-input instruction.** The
      frame survives attack and matches the state of practice
      (confidence · likelihood · impact is the canonical scanner/risk
      structure; repo-declared impact is CVSS's environmental score in
      another vocabulary). Headlines: FG1 — the instance mapping
      under-counts; C3 (adoption/first-contact) is the missing case a
      steady-state-only model would distort around, and P3 sits on the
      boundary undeclared. FG2 — the split does change the response model:
      the downgrade lane escalate-only forbids already exists spelled as
      exemption, so the durable invariant is provenance (declared, reasoned,
      expiring), not direction. FG3 — granularity is a missing axis;
      acceptance vs deferment are already distinct at line vs check level.
      Full findings + reconcile:
      [F1 intent cold pass](../../reviews/2026-08-03-0657-f1-guard-governance-intent-cold.md).
      Intent record:
      [`2026-08-02-2340-guard-governance-frame`](../../sessions/2026-08-02-2340-guard-governance-frame.md).

      **FG1–FG6 RULED 2026-08-03 (Mike, plain-language walk-through; every
      finding as counselled). These bind the rebuild at pickup:**
      **FG1** — C3 is mapped into the instance list above, and the rebuilt
      model must *state* whether posture-by-visibility (P3) is inside or
      outside its scope — either answer, never silence.
      **FG2** — the rebuild's working hypothesis is **provenance, not
      direction**: tool-initiated lowering of a response stays forbidden; a
      declared, reasoned, expiring, principal-visible lowering is lawful
      (C1's existing machinery — a downward claim rots, so it carries
      expiry; an upward move needs none). A hypothesis to *test* at design,
      not inherit; E6d stands unchanged until the rebuild lands.
      **FG3** — the model's vocabulary gains the granularity axis (line /
      check / repo) and the definitions the one-spelling ambiguity blurred:
      **acceptance is indefinite with a reason; deferment is temporary with
      an expiry**.
      **FG4** — the axes are checked against prior-art vocabulary (CVSS
      exploitability/impact/environmental, CodeQL precision ×
      security-severity, Semgrep confidence × severity) at pickup, verified
      then rather than trusted from the pass.
      **FG5** — the false-positive route is a pointer-carrying
      specialisation of PROPAGATION's resolved-upward rule, never a second
      original.
      **FG6** — the F1 pointer's "design/intent pass per REVIEW.md §" line
      is handed to the funded pointer-grammar build as a boundary specimen
      (procedural pass-type vs evaluative steering); the build decides the
      boundary with its corpus, not this entry.
