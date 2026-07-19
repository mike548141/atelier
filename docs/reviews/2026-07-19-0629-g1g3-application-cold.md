# Cold pass — the applied batch of the G1–G3 rulings (delta `578d84d`)

- **Date/time**: 2026-07-19 0629 UTC
- **Spawn provenance (rule 4)**: taken from the ROADMAP `⏳` queue by a session
  Mike spawned with "do any review work". This session authored **none** of:
  the doctrine under the chain (REVIEW.md and the review-trigger/sizescan
  deltas), the 0407 combined pass, the batch that applied its F1–F9 rulings,
  the 0544 applied-batch pass that produced G1–G3, or the application of
  Mike's G1–G3 rulings now under review. The author/applier queued the `⏳`
  pointer and stopped; this brief is taker-written.
- **Named exposure**: the taker read the `⏳` ROADMAP item and the one-line
  `SESSIONS.md` entry tails before claiming — both carry the applier's
  evaluative summary (e.g. "re-proven both legs"). That is framing leak
  beyond bare refs; it is named here, and every such claim is treated as a
  claim to re-run, not a fact. Additionally, an application review cannot
  fully honour rule 2: the delta itself contains hunks to the prior verdict
  files. Sequence per REVIEW.md: review the non-verdict files at HEAD and
  commit findings first; open the verdict-file hunks and applier's log after.

## What the work is (refs only)

Commit `578d84d` — the application of Mike's 2026-07-19 ruling ("yes take all
three") on the 0544 pass's G1–G3 findings. In-scope files at HEAD:

- `docs/build/templates/workflows/floor.yml` (G1 — pin-slot rewording)
- `tools/test_templates.py` (G2 — placeholder-inventory test)
- `docs/sessions/2026-07-18-0820-review-the-design-not-only-the-build.md`
  (G3 — dated one-liner)
- `CHANGELOG.md`, `docs/ROADMAP.md`, `docs/SESSIONS.md` (records of the batch)

**Deferred below the divider** (opened only after this reviewer's findings are
committed): the delta's hunks to
`reviews/2026-07-19-0544-combined-applied-batch-cold.md` and
`reviews/2026-07-19-0407-review-trigger-sizescan-combined-cold.md` (decision
stamps + correction addenda), and the applier's session-log addenda
(`sessions/2026-07-19-0407-…` and `…-0544-…`).

## Ask

Run all three lenses on the applied delta:

1. **Approach & assumptions** — name the load-bearing assumptions first, then
   attack them. Does each applied fix actually discharge the finding it claims
   to? Is the rewording/test the right mechanism, or a patch over the class?
2. **Correctness & quality** — re-run every live proof in scope rather than
   reading it: the 275-test suite; the prove-the-stamp grep **both legs on a
   full scaffold** (red without the fix, green with); G2's bite proof
   (re-introducing a stamp token must turn the suite red). Honest-labelling
   check on the addenda: corrections dated, originals standing.
3. **Completeness / harvest** — anything the rulings required that the batch
   skipped; anything the new test should cover and doesn't; record hygiene
   (CHANGELOG/ROADMAP/SESSIONS consistent with the delta).

Cycle context: this pass is terminal if it returns no MAJOR (close rule) —
report findings either way; decisions are Mike's (rule 3: the chain is
self-authored doctrine).

---

## Deferred material (open only after findings are committed)

- `git show 578d84d -- docs/reviews/2026-07-19-0544-combined-applied-batch-cold.md`
- `git show 578d84d -- docs/reviews/2026-07-19-0407-review-trigger-sizescan-combined-cold.md`
- `git show 578d84d -- docs/SESSIONS.md docs/sessions/2026-07-19-0407-combined-cold-pass-taken.md docs/sessions/2026-07-19-0544-applied-batch-cold-pass-taken.md`
- The authors seeded no questions; there is no author-written ask anywhere in
  this file. Everything above the divider is taker-written.

---

## Verdict — PASS, no MAJOR (committed before any deferred material was opened)

**Provenance restated (rule 4):** this reviewer is the Mike-spawned taker
("do any review work"); it authored none of the doctrine, the F1–F9 batch,
the G1–G3 findings, or their application. Everything above this line was
written without opening the delta's verdict-file hunks or the applier's
session-log addenda.

### Attack surface (named as the first act)

- **A1 — the reword discharges G1's mechanism**: removing the stamp token,
  rather than teaching the stamp step to fill floor.yml's pin, is the right
  fix only if the pin should *not* be auto-stamped.
- **A2 — "re-proven both legs on a full scaffold"** is a proof claim, so it
  is stale-able: re-run, not read.
- **A3 — G2's test actually guards the grep**: its vocabulary must equal the
  grep's, and it must go red on exactly the G1 class.
- **A4 — the reword is functionally neutral**: comments only; the adopter
  guidance (how to pin) survives.
- **A5 — G3's addendum is honest**: dated, original standing, and its two
  claims (the F6 qualification exists; the Rejected section already carries
  the honesty) are checkable.
- **A6 — records match the delta** (CHANGELOG/ROADMAP/SESSIONS).

### Lens 1 — approach & assumptions

- **A1 holds.** Auto-stamping a CI pin would freeze every child to
  scaffold-day atelier and make the pin an accident instead of a decision;
  the pin slot in plain words, filled deliberately by an adopter, is the
  correct division. The fix removes the *vocabulary collision*, which was
  the whole defect.
- **A3's design question examined and held.** The template set legitimately
  carries ~25 adopter-facing angle-bracket tokens (`<name>`, `<year>`,
  `<pin>`, `<YYYY-MM-DD>`…) — a shape-based ban would false-positive on all
  of them. Pinning the exact (file, token) pairs of the *stamp vocabulary*
  is the contract the prove-the-stamp grep actually enforces; the test pins
  precisely that. Sound.

### Lens 2 — correctness: every proof re-run, none read

- ✅ **Suite**: `Ran 275 tests … OK` (274→275 checked: test_templates.py
  19→20 test methods).
- ✅ **G1 red leg**: full template-set copy in scratch, unstamped —
  11 grep hits (matches the recorded 11).
- ✅ **G1 green leg**: the six stamp surfaces filled per the skill's step 5 —
  grep exit 1, zero hits, **with floor.yml present in the tree** (the leg
  that was previously unsatisfiable).
- ✅ **G2 bite**: re-adding `# ref: <SHA>` to floor.yml turns
  `TemplateSetPlaceholderInventoryTest` red; revert restores green.
- ✅ **A4**: the delta touches comment lines only; YAML semantics unchanged;
  the pin guidance ("set a commit SHA here…") survives, with the G1 pointer
  explaining *why* no token.
- ✅ **A5 / G3**: addendum dated 2026-07-19, labelled discretionary, original
  text standing; REVIEW.md carries the "structural in intent … conventional
  in fact" qualification; the ROADMAP queues the F6 artefact item; the 0820
  Rejected section's "deferred, not rejected on merit" honesty is where the
  addendum says it is.
- ✅ **A6**: no stale `# ref: <SHA>` description survives outside historical
  records; sizescan `--check` clean at HEAD.

### Lens 3 — completeness / harvest

- Nothing the rulings required is missing: G1 reword + both-legs re-proof,
  G2 set-wide pin, G3 one-liner, the correction addenda, CHANGELOG entry,
  fleet re-stamp correctly *held* behind this open cycle.
- **N1 (note, not a finding against this delta):** the stamp vocabulary now
  lives in three places — the in-repo pair (`PLACEHOLDERS` /
  `STAMP_INVENTORY`, mechanically pinned to each other by the suite) and the
  create-repo skill's fill step + prove-the-stamp grep, which are
  machine-local (`~/.claude/skills/`) and synced by prose only. No in-repo
  test can reach them. If create-repo ever ships into the plugin bundle,
  add the vocabulary sync test in the same change. Until then the exposure
  is one prose rule, named here.

### Findings

**None of MAJOR, MEDIUM, or LOW severity.** One note (N1 above) for the
backlog's judgement, no action owed by this delta. Per the close rule, a
pass with no MAJOR is terminal for the cycle — subject to Mike's ruling.

---

## Reconcile — deferred material opened after the verdict commit (`bf5a5b9`)

The delta's verdict-file hunks (0544 decision stamps, the 0407 correction
addendum) and the applier's session-log addenda were opened only now.
Reconciliation: **no discrepancy in either direction.**

- The applier's recorded proofs match my independent re-runs exactly — red
  leg 11 hits, green leg grep exit 1 with floor.yml present, suite 274→275,
  and the bite turning *exactly* `TemplateSetPlaceholderInventoryTest` red.
- The correction addenda are as my A5 check found the G3 one: dated,
  labelled, originals standing, `9d95644`'s immutable message named rather
  than hidden.
- Severity arithmetic is consistent across records: the 0544 pass was
  1 MAJOR (G1) · 0 MEDIUM · 1 LOW (G2) · 1 note (G3, withdrawn as a defect,
  taken as discretionary) — matching the CHANGELOG entry, and Mike's "yes
  take all three" matches the [fixed] stamps.
- Nothing in the deferred material weakens, contradicts, or would have
  redirected the findings above. The verdict stands: **PASS, no MAJOR.**

## Taker's counsel (labelled as such — the decisions are Mike's, rule 3)

This is the cycle's first no-MAJOR pass, so per the close rule it is the
**terminal** one: the cycle (0407 → application → 0544 → application → this
pass) closes on your ruling, no further ceremony spawned. Counsel:

- **Close the cycle.** Every proof in the chain now re-runs clean and the
  false-proof record is corrected by addenda.
- **N1 → accept as named** (no code change owed): the create-repo skill's
  fill step + grep vocabulary is machine-local and cannot be pinned by an
  in-repo test; the verdict records the exposure. If create-repo ships into
  the plugin bundle later, the vocabulary sync test belongs in that change —
  a one-line note on that future work item is the only artefact worth making
  now.
- **Consequence of closing**: the fleet re-stamp item's hold lifts — it
  becomes an ordinary open ROADMAP item (children pick up the reworded
  floor.yml and re-prove their stamps at pin bump).
