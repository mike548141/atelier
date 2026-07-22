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

---

## Verdict — PASS, no MAJOR (committed before any deferred material was opened)

**Provenance restated (rule 4):** this reviewer is the Mike-spawned taker
("please do any review work"); it authored none of the doctrine deltas, the
SL1–SL7 findings, or their application. Everything above this line and in
this section was written without opening the prior verdict file, the
decision-stamp commit, or the applier's intent record. Subject pinned at
`d553045` on ref `92a146f`; two concurrent sessions were live during the
pass (interruption-resilience, v2-plugin-deinstance) — neither branch
touches any in-scope file, so the pass continued on the pinned ref
(the principal delegated the pause/continue call).

**Additional exposure incurred mid-pass, named:** a repo-wide stale-wording
grep surfaced the prior pass's evaluative `SESSIONS.md` index line
(SL1–SL7 summaries), and the record-hygiene check read the CHANGELOG entry
for the application — both after the brief and the core findings were
committed, but before this verdict was. Treated as claims, not facts;
named, not denied.

### Attack surface (named as the first act)

- **A1 — the parity floor genuinely pins the roster (not a green fence).**
  CONFIRMED by re-drive: with the pre-fix skill restored
  (`git checkout d553045^ -- skills/review-brief/SKILL.md`) the suite goes
  red with **2 failures** — the missing `Security & privacy` lens and the
  `three lenses` count-word pin — exactly the SL1 drift class. Restored,
  green. `canonical_lenses()` parses REVIEW.md to exactly
  `['Approach & assumptions', 'Correctness & quality',
  'Completeness / harvest', 'Security & privacy']`; the section-bounded
  regex cannot mistake the independence rules or lifecycle steps for
  lenses, and a renamed section heading fails loud (ValueError), not
  silent-green. Residual accepted: the child-template pin is a literal
  sentence — brittle-but-tripwire, which is the right failure direction
  (reds on any reword, forcing a same-commit look).
- **A2 — the reach-per-shape rewrite keeps lens 4's floor.** CONFIRMED, and
  live-exercised by this very pass: this is a landed-delta review of
  markdown + a stdlib test file, the scanner cannot genuinely be aimed at
  it, and the new text forces exactly what this verdict does — an explicit
  discharge with grounds and a statement of which case applied, rather
  than a silent skip or a definitionally-empty clean pass weighed as
  cover. The discharge line is not an easy out: it is auditable (one
  explicit line in the verdict) and shape-scoped, not mood-scoped.
- **A3 — the skill compresses, never contradicts, the parent.** CONFIRMED
  on a clause-by-clause read of the skill's §3 against REVIEW.md's scope
  mandate + lens list. One compression loss noted as AC2 below.
- **A4 — the template Type replacement removes the standing narrowing
  offer.** CONFIRMED: "correctness only" is gone from every live surface;
  the new Type text routes all narrowing to Non-goals, which the same
  delta makes reviewable. Repo-wide sweep for `three lenses`,
  `run all three`, `correctness only`: only historical records remain
  (prior session index, an old CHANGELOG entry) — correct residue, not
  drift.
- **A5 — the recorded proofs reproduce.** Suite: **Ran 302 tests — OK**
  (claimed 298→302; the 4 new parity tests account exactly). Red leg:
  reproduced (A1). Floors at HEAD: sizescan `--check` rc=0 (advisory
  only), reviewscan clean, linkscan clean, secretscan + leakscan clean on
  every commit this pass made.
- **A6 — record hygiene.** CHANGELOG carries the cycle's entry
  (open-pending-application stated — will need its close stamp when this
  pass lands); ROADMAP pointer was refs-only as rule 4's ceiling demands;
  the intent record is where the evaluative account lives, and it stayed
  unread until after this verdict committed.

### Lens 4 — security & privacy (run manually; scanner discharged)

Scanner discharge, grounds per the rule under review: landed-delta shape,
nothing pending for `/security-review` to read, and its exclusions bar
markdown — a clean pass would be definitionally empty. Manual pass:
`LensRosterParityTest` is stdlib-only (`re`, `unittest`, `pathlib`),
reads two repo files, no exec/network/input surface; the doctrine and
template prose leak nothing (leakscan structural + local, green); no
over-collection at design altitude — the delta *narrows* what a reviewer
feeds the scanner (never a brief carrying deferred material), a privacy
improvement in its own right.

### Findings

- **AC1 (LOW, quality)** — `docs/build/templates/CONTRIBUTING.md:44` is
  **122 columns**, introduced by the SL3 hunk — the same >80-col defect
  class SL7 fixed in REVIEW.md in the same commit. House prose wraps at
  ~80 (ambient tolerance runs 81–85); this is the widest line in any
  in-scope file and sits in a template children copy. Non-semantic.
  *Counsel: rewrap; one-line fix, no meaning touched.*
- **AC2 (LOW, completeness)** — the skill's scanner clause omits the
  exclusion-barred caution ("a clean pass over a barred file class is
  definitionally empty — weigh it as nothing") that the parent states and
  this cycle live-proved. A skill-guided reviewer holding a markdown diff
  could aim the scanner, get a clean pass, and weigh it as a real floor.
  Compression is the skill's sanctioned mode and the full doctrine is one
  pointer away, so this is LOW, not a contradiction. *Counsel: half a
  sentence at the next skill touch; not worth a solo commit.*

No MAJOR. Per the close rule this pass is **terminal**: the cycle closes,
AC1–AC2 go to the backlog for the principal's decision, and this
application does not spawn another full ceremony.

### Reconcile — what the deferred material changed

Nothing overturned; one finding sharpened. Opened after the verdict above
was committed (`35e2856`): the prior verdict + decision stamps, the intent
record + addendum, and `913c81a`.

- **Every [fixed] stamp corroborated independently.** All seven SL rulings
  match what this pass verified at HEAD *before* reading them: SL1's parity
  floor (red leg re-driven here), SL2's reach-per-shape rewrite with the
  permissive grant restored — confirmed against the follow-up's "decide
  mandate vs permissive to match the grant" — SL3/SL4's template sweeps,
  SL5's "short in ceremony, never in scope", SL6's grounds burden, SL7's
  reflow. The prior pass's follow-up counsel ("consider a mechanical parity
  check… this drift class has now shipped twice") is exactly what landed.
- **AC1 sharpened, severity unchanged (LOW).** SL7 fixed a ~90-char wrap
  artefact and a stub; SL3's own edit introduced a 122-col line in
  CONTRIBUTING — the fixing commit re-shipped the class it was fixing, in a
  different file. Same counsel: one-line rewrap.
- **AC2 confirmed in-bounds.** The rulings put both live-proven cautions in
  REVIEW.md (done) and "the scanner clause" in the skill (done); the
  exclusion-barred caution's absence from the *skill* contradicts no
  ruling — it is compression loss at the point of use, LOW as filed.
- The two-hop spawn account and the applier's claims in the intent record
  are consistent with the evidence trail this pass re-ran; no claim was
  taken on trust that had not already been reproduced.

**Final: PASS, no MAJOR — the cycle closes.** AC1–AC2 to the backlog for
the principal (rule 3); no further ceremony spawned, per the close rule.

---

## Decisions — 2026-07-22, the principal

Mike ruled on AC1–AC2 (mid-turn, same day): **"agreed I accept both per
your counsel"** — both **[fixed]**, applied by the reviewing session
(sanctioned by the backlog item's own `review: not warranted` line —
line-level mechanical application):

- **AC1 [fixed]** — CONTRIBUTING template line rewrapped (122 → ≤80 cols),
  no meaning touched.
- **AC2 [fixed]** — the skill's scanner clause gains the exclusion-barred
  caution (a clean pass over a barred file class is definitionally empty —
  weigh it as nothing).

Re-proven: suite 302 green after both edits (the lens-roster parity pins
unaffected); no line in either file exceeds the house wrap tolerance.
