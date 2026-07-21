# Findings draft — scope mandate + lens 4 cold pass (deltas f9db922 + a059e49)

Reviewer: fresh-context subagent (Fable), spawned by the non-author taker.
Drafted BEFORE opening: the intent record, the author commit bodies
(`git show --format=` used throughout), and any prior verdict in `docs/reviews/`.

## Contamination disclosure — read first

Executing lens 4's scanner instruction (`/security-review`, as the brief's
instruction 3 directs) caused the harness to inject the ENTIRE brief file into
this reviewer's context — including the below-divider deferred section (seeded
questions SQ1–SQ6) and the taker's brief-commit message — before this draft was
written. That is a forced breach of the rules-1–2 deferral, caused by complying
with the doctrine under review. Sequencing that is verifiable from the session
transcript:

- Named BEFORE the leak (my own first act): assumptions A1 (lens-count
  coherence), A2 (lens-4 executability on prose / discharge escape), A3
  (scanner-instruction runnability in the cold-pass shape), A4 (widest-scope vs
  "scoped and short"), A5 (harness portability of a vendor command), A6 (cited
  rulings verifiable only in deferred material).
- Found BEFORE the leak (sweep results): `skills/review-brief/SKILL.md:53`
  still counting three lenses; `docs/build/templates/CONTRIBUTING.md:43` still
  carrying the old three-part scope sentence; CHANGELOG "three lenses" hit
  classified as a dated historical record.
- Arrived only WITH the leak: SQ5's specific "where possible" angle (drafted
  below as SL6, attributed as seeded, not mine).

Also disclosed: a grep sweep for lens references legitimately hit the one-line
`docs/SESSIONS.md:132` index entry for the authoring session (author-written
summary). The session record itself was not opened.

## Load-bearing assumptions (lens 1, named cold)

A1–A6 as above; attacked throughout the findings.

## Scanner execution evidence (brief instruction 3)

- Run attempted in the worktree at HEAD (`a0d24d7`), tree clean.
- The skill computed "pending changes on the current branch" = the taker's
  brief file only. The in-scope deltas (f9db922 + a059e49, landed on `main`)
  were NOT in the diff it analysed. "Over the in-scope diff" is not an
  operation the house instance supports for landed work.
- The skill's own hard exclusion 16 excludes all findings in markdown
  documentation files — the entire diff class of doctrine reviews. Its result
  here: no vulnerabilities (all changed files markdown; definitionally
  excluded). Folded in as a clean-pass claim, weighed accordingly: for this
  work class it is a no-op floor.
- Repo scanner floor re-run independently, all green at HEAD: secretscan 0,
  leakscan 0, licenscan 0 (Apache-2.0), linkscan 0, reviewscan 0 (1
  post-2026-07-21 decision record carries a review line), sizescan --check 0
  (advisory only).

## Findings

### SL1 — MAJOR — the review-brief skill still stamps the three-lens structure

`skills/review-brief/SKILL.md:53–59`: "**The three lenses**, run all three" —
no lens 4, no security & privacy anywhere in the file, no scope-mandate
sentence, no scanner clause. The file's own header (lines 6–13) declares it a
stamped copy that "may compress the parent, never contradict it" and records
that this exact drift class was caught once already (2026-07-19 cold-pass F3).
It now contradicts the parent on the delta's two central claims: the lens
count and the mandatory lens. This is the point-of-use surface — briefs
written via the skill will omit the lens the delta made mandatory. In scope by
the delta's own rule ("every other surface that states, counts, or relies on
the lens structure or review scope — templates, skills…"); the delta updated
`method/README.md`'s count but missed the skill. Lens 3 failure with fleet
blast radius (plugin-bundled).

### SL2 — MAJOR — the scanner sentence cannot be executed as written in the doctrine's own primary review shapes, and executing it breaches the independence structure

`docs/method/REVIEW.md:157–162`: "the reviewer runs it … over the in-scope
diff". Live evidence from this pass (first live execution of the rule):

1. **Wrong diff.** A rule-4 cold pass reviews a landed delta on a clean tree;
   `/security-review` reads pending branch changes. Here it analysed the brief
   file, not the work. A design-time review (which this doctrine explicitly
   champions) has no diff at all. In the two review shapes this repo most
   runs, the instruction misfires.
2. **Deferral breach.** The skill injected the full brief — deferred section
   included — into the cold reviewer's context. Complying with lens 4's
   sentence forcibly violated rules 1–2. The mechanical floor, run where the
   text mandates it, destroys the independence the same document constructs.
3. **Null floor for doctrine.** The scanner's own rules exclude markdown
   documentation entirely; for doctrine reviews the "mechanical floor layered
   under this lens" is definitionally empty, and the text does not say so —
   a reviewer can report "scanner clean" and appear to have added evidence
   when the tool was incapable of finding anything in this work class.

The sentence needs an execution shape per review type: what to point the
scanner at for landed work (e.g. a checkout/branch state where the delta is
pending, or an explicit "scanner inapplicable: <grounds>" discharge mirroring
the lens's own one-line shape), and a warning that the reviewer must not run
it over a brief containing deferred material before drafting.

### SL3 — MEDIUM — CONTRIBUTING template still carries the pre-delta scope sentence

`docs/build/templates/CONTRIBUTING.md:42–44`: "a more capable model reviews
approach, assumptions and real-world behaviour, not just correctness" — the
same house-practice sentence the delta amended in
`templates/docs/reviews/README.md`, unamended here: no security & privacy, no
scope mandate. Fleet-propagating at pin bump; a child's CONTRIBUTING and its
reviews README will describe two different review scopes.

### SL4 — MEDIUM — "correctness only" survives as a legitimate review Type in the very file the delta amended

`docs/build/templates/docs/reviews/README.md:58`: the Format section still
offers **Type** = "approach + assumptions" vs "correctness only". Under the
amended top paragraph of the same file, security & privacy is "a must on every
review" and non-goals are the only legitimate narrowing — a "correctness only"
type is a standing narrowing offer that bypasses the non-goals mechanism. The
delta edited lines 15–24 and left line 58 contradicting them.

### SL5 — MEDIUM — the widest-scope mandate and "scoped and short" are left unreconciled, and the only narrowing lever sits in warm hands

`docs/method/REVIEW.md:126–137` (non-goals the only legitimate narrowing;
anything not named out of scope is in scope) vs `REVIEW.md:357` ("Either way
the review stays **scoped and short**"). The delta closed the "no source code"
escape but left the older economy sentence as an available counter-cite for a
reviewer wanting to shrink scope. Sharper: in warm (non-rule-4) reviews the
brief — and therefore the non-goals — is typically author-written; the delta
makes non-goals the *sole* legitimate narrowing without extending to them the
attackability it grants the rest of the brief's framing (rule 1 makes the
brief's framing attackable, but the scope paragraph does not say the reviewer
may treat a non-goal itself as a finding when it fences off the risk).

### SL6 — LOW — the live-exercise impossibility claim carries no grounds burden (seeded: SQ5 arrived via the scanner leak)

`docs/method/REVIEW.md:130–133`: "exercised live where doing so is possible
and re-run from the work's own claims where it is not". Partial mitigation is
built in (the re-run duty remains), but a claim of impossibility itself needs
no stated grounds — unlike every other discharge in the delta ("one explicit
line with grounds", "review: not warranted — <grounds>"). Same shape, one
line: "wasn't possible" should be a stated, disagreeable judgement, not a
blank.

### SL7 — LOW — wrap artefacts introduced by the delta

- `docs/build/templates/docs/reviews/README.md:24`: "…with grounds). The
  builder (usually Opus) then applies" — ~90-char line in an otherwise
  ~80-wrapped file (introduced by f9db922, preserved by a059e49).
- `docs/method/REVIEW.md:162–164`: "…Where the work / genuinely has no /
  security or privacy surface…" — a three-word stub line left by a059e49's
  insertion.

Cosmetic, but this is doctrine others template from.

## Per-lens summary (draft)

- **Lens 1 (approach & assumptions)**: the scope mandate and lens-4 design are
  sound and well-shaped (discharge-with-grounds mirrors existing shapes;
  vendor command generalised correctly in the child template via "e.g.").
  A3 falsified in practice → SL2. A4 partially falsified → SL5.
- **Lens 2 (correctness & quality)**: the three delta files do what they claim
  at HEAD; `method/README.md` count updated; no overclaim found in the delta
  text itself; cosmetic wrap defects SL7.
- **Lens 3 (completeness / harvest)**: two missed surfaces (SL1, SL3) and one
  intra-file contradiction left standing (SL4), all inside the delta's own
  declared scope rule.
- **Lens 4 (security & privacy)**: the delta is prose in a public repo; no
  personal data, no secrets (scanner floor green at HEAD; leakscan/secretscan
  clean). Design-altitude defect: the scanner instruction itself creates an
  information-flow breach of the review's independence structure when executed
  in the cold-pass shape (SL2.2) — a privacy-of-process defect in the
  doctrine's own terms. Executed, not recalled: live run evidence above.

Draft verdict inclination: PASS-WITH-FINDINGS (2 MAJOR · 3 MEDIUM · 2 LOW).

## Reconcile addendum (written after opening deferred material)

- SQ1 ≙ A4/SL5 (assumption named pre-leak; finding drafted pre-open). Covered.
- SQ2 ≙ A2: considered and deliberately not a standalone finding — the
  one-line discharge is a stated, disagreeable judgement (the delta's own
  "no one can disagree with a blank" logic); the real hollowing vector is the
  point-of-use skill omitting the lens entirely (SL1).
- SQ3 ≙ A3/SL2, extended by live evidence the seed did not anticipate: the
  scanner run breaches the deferral structure itself.
- SQ4 ≙ A1 sweep → SL1; sweep went wider than the seed and also caught SL3.
- SQ5 → SL6, attributed as seeded (arrived via the scanner leak pre-draft;
  disclosed in the draft header).
- SQ6: template compresses the parent without narrowing; "e.g." genericises
  the vendor command correctly for scanner-less harnesses; SL4 goes beyond
  the seed (the "correctness only" Type line contradicts the amended
  paragraph in the same file).
- Intent record's framing note (re-derive the gaps, don't take the account):
  honoured — the gap audit re-derived independently from the pre-delta text
  visible in the diffs (no security/privacy/OWASP mentions pre-delta;
  scope enumerated, never mandated). Gaps were real; lens-4-as-number choice
  verified correct (all pre-existing lens-1/2/3 references remain valid).
- Commit bodies: A6 discharged — the 2026-07-21 principal rulings cited in
  the delta text are corroborated by the intent record and both commit
  bodies. One escalation found: the a059e49 body records a *permissive*
  grant ("If it is useful I'm happy for you to use it"); the delta text
  encodes a *mandate* ("the reviewer runs it"). Folded into SL2 — the
  mandatory phrasing is the delta's own encoding choice, and it is the
  mandate that forces the misfire.
- Prior verdicts (2026-07-15 / 2026-07-19 files): not opened beyond the
  in-repo anchors the delta cites — the citations resolve to pre-existing
  REVIEW.md text and the skill's own header; nothing in scope required
  re-litigating closed cycles (brief non-goal).
