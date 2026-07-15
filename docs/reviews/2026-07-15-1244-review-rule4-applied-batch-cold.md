# Cold review — REVIEW rule 4 applied batch (the F1–F8 application)

**Scope:** the doctrine hunks of commit `c4a73c4` (2026-07-15) — the
application of Mike's ruled findings F1–F8 from the rule-4 cold pass:
(1) `docs/method/REVIEW.md` — rule 4 restated as the single spawn criterion
with the named paths as examples that must pass it; the author's handoff;
the provenance requirement; the `⏳` licence; the batched-queue carve-out;
the applier seam in *Applying decisions*; rule 3's doctrine-by-function list
gaining the behaviour-stamping template/skill item; lead-in verbs; wording.
(2) `docs/method/MODEL-ECONOMICS.md` — the §Triggering-reviews sweep. Review
both edited docs at HEAD, whole, plus the delta. The ROADMAP/SESSIONS hunks
in the same commit are bookkeeping, in scope only for consistency with the
doctrine text.

**Sequencing (an application review — REVIEW.md *Applying decisions*):** this
review cannot fully honour rule 2, because the delta's companion hunks in
`docs/reviews/2026-07-15-1202-review-rule4-cold.md` carry the prior verdict's
decision stamps. So: (1) read this brief **only above the first `---`
divider** (use a limited read); (2) review the edited doctrine at HEAD plus
the doctrine hunks of `c4a73c4`, committing your findings to a durable draft
*first*; (3) only then open the deferred section below, the verdict-file
hunks, and the prior verdict's §Decision, and check **fidelity to the
rulings**: does the applied text encode each of the eight rulings faithfully
— nothing added the principal didn't rule, nothing ruled that the text
drops? Fidelity gaps are findings. Name any residual exposure rather than
denying it.

**Commissioning provenance (rule 4 / F5):** this brief is written by a
**non-author** — a fresh session the principal opened and pointed at the
queued `⏳` item ("do any review work queued"); neither the rule's author
session nor the applier (commissioning) session started or instructed it.
The reviewer is a cold spawn of that taking session, which read the prior
verdict file to scope this brief and is therefore itself ineligible to
review. The verdict must repeat this provenance (rule 4: no trail ⇒
unauditable ⇒ non-compliant).

**This is self-authored doctrine (by function)** — an application of
self-authored doctrine inherits rule-4 status. All findings are the
principal's to decide (rule 3): recommend, apply nothing.

**Re-run live proofs in scope:** the application commit claims floor green
(247 tests · sizescan · linkscan). Re-run them.

**Run all three lenses** (approach & assumptions · correctness/honesty ·
completeness/harvest), deep not fast; findings get stable IDs (F1…) with
severity MAJOR/MEDIUM/LOW. Append your verdict to this file below the second
`---` divider.

---

## Deferred — taker's questions (open only after your attack surface is committed)

- Q1. Rule 4 now bars the applier from spawning the application review, and
  each application inherits rule-4 status in turn. Iterated across a cycle
  that stays open (MAJOR at each pass), does the criterion converge — do
  enough eligible spawners remain — or does it manufacture a regress the
  close rule doesn't terminate?
- Q2. The provenance requirement — "the brief states it, the verdict repeats
  it" — is that auditable in practice, or does it relocate self-certification
  into the brief? And is the worked example now baked into rule 4 (F8) a
  grounding, or an instance detail that will go stale in a shareable doc?
- Q3. The criterion-plus-examples restatement (F1) — do the three recast
  examples each actually pass the criterion as now worded, and does the
  batched-queue carve-out compose with MODEL-ECONOMICS' batching guidance
  without a seam?
- Q4. Single-sourcing (F4) — is rule 3's list now the sole definition site
  for doctrine-by-function, or does any other doc (MODEL-ECONOMICS,
  templates, skills) still carry its own restatement?

---

## Verdict — applied-batch cold pass 2026-07-15

**Reviewer provenance & process disclosure.** Repeating the brief's
commissioning provenance per rule 4: this brief was written by a
**non-author** — a fresh session the principal opened and pointed at the
queued `⏳` item ("do any review work queued"); neither the rule's author
session nor the applier (commissioning) session started or instructed it.
This reviewer is a cold spawn of that taking session — which had read the
prior verdict to scope the brief and was therefore itself ineligible. Against
rule 4's criterion: the applied delta's author (the applier session) neither
started nor instructed this review. Compliant.

Two sequencing exposures, disclosed rather than denied (both are also
recorded in the draft committed before any deferred material was opened):

- **E1.** The instructed brief read (`limit ~55`) returned lines 51–55 — the
  deferred-section heading and the opening lines of Q1 — past the first
  divider at line 49. Overlap with Q1 is claimed as convergence below.
- **E2.** A composition sweep (`grep ⏳ docs/`) matched `docs/SESSIONS.md`
  lines 88–89, which summarise the prior verdict's F1–F8 and the rulings in
  compressed form, before my draft hit disk. My attack-surface candidates
  were formed before that sweep ran, but that ordering lives in-session, not
  on the record — so everything overlapping those summaries is likewise
  claimed as convergence, not independence.

**Scope covered.** REVIEW.md and MODEL-ECONOMICS.md at HEAD, whole; the
doctrine hunks of `c4a73c4` via `git show`; ROADMAP and SESSIONS hunks for
consistency with the doctrine text; 00-APEX, CONCURRENCY, PROPAGATION,
ci.yml and the build/ layer for composition; the prior verdict's §Decision
as the fidelity source, opened only after the draft was committed. All three
lenses run. Nothing applied anywhere — self-authored doctrine, all findings
the principal's (rule 3). The only files touched: this verdict and the
scratchpad draft.

### Attack surface (as committed to the draft, pre-deferred)

- A1. Does the single criterion actually close the laundering path — is
  "instructed" tight enough to catch framing travelling through the `⏳`
  pointer itself, which the author/applier writes and the taker reads before
  writing the brief?
- A2. Does the applier-seam inheritance compose with the close rule without
  contradiction (an unterminated queue obligation) or leak (licence to skip
  queueing)?
- A3. Does "examples that must pass the test" leave any path safe-by-name
  anywhere else in the corpus?
- A4. Is doctrine-by-function now genuinely single-sourced in rule 3, with
  rule 4's reference live and the lists no longer divergent?
- A5. Companion-sweep completeness — does any passage still license an author
  spawn or "the building model's call" for doctrine?
- A6. Is the provenance requirement auditable in practice, tested against the
  live instance?
- A7. Do the recorded proofs (247 tests · sizescan · linkscan) reproduce at
  HEAD?
- A8. Are the bookkeeping hunks consistent with the doctrine they record —
  including the live `⏳` pointer's own content against rule 4's handoff
  spec?

### Fidelity to the rulings (prior verdict §Decision, F1–F8)

Checked ruling-by-ruling against the applied text at HEAD:

- **F1 ✅ faithful.** The enumeration is replaced by the single criterion as
  the test ("the review comes from a session the author neither started nor
  instructed"), the three paths recast as examples that must each pass it,
  and the author-scheduled-batch failure mode named in the rule; the
  batched-queue bullet carries the matching carve-out. Nothing weaker than
  the ruling; the added sentence ("fails it whatever the batch is called")
  is the ruling's own content restated, not an addition.
- **F2 ✅ faithful.** Handoff encoded: queue the `⏳` pointer naming the
  delta and the intent record, stop; the taker writes the brief.
- **F3 ✅ faithful.** MODEL-ECONOMICS §Triggering reviews and REVIEW §When to
  review both drop "the building model's call" and gain the rule-4
  exception (the qualifier moved into §When to review's lead, as ruled);
  the applier seam states the application inherits rule-4 status and the
  applier queues, never spawns.
- **F4 ✅ faithful.** Rule 3's list gains the behaviour-stamping
  template/skill item; rule 4 cites "(rule 3's definition, single-sourced
  there)" without restating. Repo-wide grep confirms no third definition
  site (see Q4 below).
- **F5 ✅ faithful.** Provenance requirement in rule 4: brief states who
  spawned and the author's non-involvement, verdict repeats it; no trail ⇒
  unauditable ⇒ non-compliant.
- **F6 ✅ faithful.** Lead-in verbs aligned on *spawn* ("however the review
  was spawned … who may spawn it"). One residue of the commission family
  survives elsewhere — see finding F4 below (LOW; the ruling's scope was the
  lead-in, so this is residue, not a fidelity gap).
- **F7 ✅ faithful.** The clumsy possessive is gone; rule 4 now uses rule 3's
  "self-authored" phrasing ("whose wording the author's own judgement
  produced").
- **F8 ✅ faithful, with a note.** Rule 4 names the `⏳` convention and
  licenses any criterion-passing spawner to take a queued item. The ruling
  said the pass that produced the prior verdict "is recorded in the rule as
  the worked example"; the applied text genericises it ("the principal
  opening a fresh session and pointing it at the queue is the worked
  example") while the rule's dateline parenthetical ("sharpened by this
  rule's own cold pass, ruled the same day") carries the instance
  provenance. Both halves present; the genericisation is defensible — and
  answers Q2's staleness worry — so: faithful, no finding.

**Nothing added the principal didn't rule; nothing ruled that the text
drops.** The one genuinely new composition issue the application created
(the applier seam's interaction with the pre-existing close rule) is outside
the rulings' scope and is finding F1 below.

### Reconciliation with the taker's deferred questions

- **Q1 (regress/convergence)** → converges with my A2/F1 (and E1 discloses I
  glimpsed Q1's opening). Answer: spawner supply is not the binding
  constraint — the criterion only excludes sessions the latest delta's
  author started or instructed, and fresh principal-opened or neutral
  sessions are unbounded. The close rule bounds the MAJOR dimension (no
  MAJOR ⇒ close; MAJOR count not falling ⇒ escape valve to the principal),
  so the regress terminates. What the text leaves ragged is the *terminal*
  application: the applier-seam sentence queues unconditionally while the
  close rule cancels ceremony for a no-MAJOR pass — finding F1. The real
  cost of the loop is principal attention per cycle, which the escape valve
  already caps.
- **Q2 (provenance auditability)** → provenance is assertion-based: session
  identity never reaches git metadata, so "neither started nor instructed"
  cannot be mechanically verified. But the requirement does not merely
  relocate self-certification — it moves the assertion from the author (the
  party whose compliance is the named residual risk) to the taker (no stake
  in the wording), and converts silence into a durable, falsifiable record.
  That is the strongest audit surface available short of transcript
  archival. The worked example: ruled in (F8), and applied in generic form —
  the instance dateline lives in the rule's parenthetical, so the shareable
  text won't stale. Adequate; no finding.
- **Q3 (examples pass; batching composes)** → the principal passes trivially;
  a neutral working session passes by definition; "a scheduled batch" passes
  only when a non-author queued and scheduled it, and the rule now says
  exactly that, naming the failing case. MODEL-ECONOMICS' batching guidance
  composes by pointer ("the exception is self-authored doctrine … REVIEW
  rule 4"). The residual seam is not in §Triggering reviews but in
  §Sub-agents: its paraphrase drops half the criterion — finding F3.
- **Q4 (single definition site)** → yes. Repo-wide grep for the definition's
  fingerprints ("doctrine by function", "govern(s) future agent behaviour",
  "stamps behaviour") hits only REVIEW.md among doctrine/templates/skills;
  the other hits are ROADMAP/SESSIONS narration and historical review
  records, which quote rather than define. No template or skill carries a
  restatement.

### Findings

- **F1 — MEDIUM — the applier seam queues unconditionally while the close
  rule cancels ceremony for a no-MAJOR pass, and nothing conditions one on
  the other.** Evidence: REVIEW.md *Applying decisions* — "the applier does
  not spawn the application review either: it queues the `⏳` pointer for a
  non-author to take" (unconditional), then three sentences later "it closes
  when a pass returns no MAJOR finding — … and that application does not
  spawn another full ceremony." Every application inherits rule-4 status, so
  one reader queues a pointer after *every* application including the
  terminal one (unterminated ceremony); another reads the close rule as
  licence to skip queueing after a MAJOR pass. Reviewer's counsel: condition
  the seam ("while the cycle is open — see the close rule below") or make
  the close rule state explicitly that the terminal ruled application closes
  without a queued pointer. The principal decides.
- **F2 — MEDIUM — the `⏳` pointer is an unregulated framing channel: rule 4
  specs the handoff as *naming* the delta and the intent record, but the
  live pointer carries the applier's per-finding account of the application,
  read by the taker before the brief is written.** Evidence: rule 4 —
  "queue the review pointer (ROADMAP `⏳`, naming the delta and the intent
  record) and stop"; the live item (docs/ROADMAP.md, the rule-4 entry) is a
  17-line evaluative summary in the applier's framing ("rule 4 restated as
  the single spawn criterion … companions swept … wording cleaned"). Rules
  1–2's deferral machinery never reaches the pointer, so author/applier
  framing that the brief must defer can travel undeferred through the queue
  itself — the same mechanism REACH exhibited, one channel over. Reviewer's
  counsel: make the pointer spec a ceiling as well as a floor (delta ref +
  intent-record ref, nothing evaluative), routeing the author's account into
  the intent record where the reviewer's deferral discipline governs when
  it is read. The principal decides.
- **F3 — LOW — MODEL-ECONOMICS §Sub-agents paraphrases rule 4 as "a
  non-author starts the review", encoding only "started" and dropping "nor
  instructed".** Evidence: MODEL-ECONOMICS lines 57–59. A single-doc reader
  could hand an author-written brief to a fresh session and call it
  compliant — the same single-doc-reader class the prior pass's F3 flagged;
  the sweep caught §Triggering reviews but not this earlier paraphrase
  (convergence per E2). Reviewer's counsel: align the paraphrase to the full
  criterion ("a session the author neither started nor instructed").
- **F4 — LOW — the commission family survives the spawn alignment in
  "commissioning provenance" (REVIEW.md rule 4), undefined against the
  now-canonical verb.** Evidence: REVIEW.md line 112 vs the F6-aligned
  lead-in. Possibly deliberate (the provenance *record* vs the spawn *act*),
  but the distinction is nowhere drawn (convergence with prior F6 per E2).
  Reviewer's counsel: either draw the pair explicitly or complete the sweep
  to "spawn provenance".
- **F5 — LOW — ROADMAP's legend defines `[ ]`/`[x]`/`[~]` but not `⏳`,
  which rule 4 has just made a load-bearing queue marker.** Evidence:
  docs/ROADMAP.md lines 10–12 vs rule 4's handoff. A session reading only
  the legend has no semantics for `⏳` (who may take it, that the taker
  writes the brief); the live item mitigates by spelling it out inline
  (convergence with prior F8 per E2 — the ruling closed the rule-side
  naming; the legend side wasn't ruled). Reviewer's counsel: one legend
  clause — "`⏳` review queued for a non-author to take (REVIEW rule 4)".
- **F6 — LOW — rule 4's criterion tests non-involvement of "the author",
  singular, but an application chain accretes stake-holders and the text
  never says whose non-involvement an application review must test.**
  Evidence: rule 4's criterion vs this brief's own provenance, which tested
  both the rule author and the applier — stricter than the text requires.
  Reviewer's counsel: state it — for an application review the delta's
  author (the applier) is the criterion's subject at minimum, prior authors
  where practical (convergence with Q1's chain framing per E1).
- **F7 — LOW — wording: "the spawn must be a non-author's whichever path the
  economics favour" garden-paths without a comma.** Evidence:
  MODEL-ECONOMICS §Triggering reviews, line 207. Reviewer's counsel: comma
  before "whichever".

### Proofs re-run (A7)

All reproduce at HEAD, matching and exceeding the commit's claim:

- `python3 -m unittest discover -s tools -p 'test_*.py'` — **Ran 247 tests …
  OK** (the claimed 247).
- `node --test instruments/*.test.js` — 34 pass, 0 fail.
- All six scanner `--selftest`s OK (leakscan, secretscan, licenscan,
  linkscan, signscan, sizescan).
- Tree scans clean: secretscan · leakscan (structural) · licenscan
  (Apache-2.0) · linkscan · `sizescan --check`.

### Overall

The load-bearing fix is sound: the single criterion genuinely replaces the
enumeration, the examples are subordinated to the test, the laundering path
is named and closed, and all eight rulings are encoded faithfully with
nothing smuggled in. The two MEDIUMs are composition debts the application
created or inherited at its seams (close-rule interaction; the pointer as an
undeferred framing channel), not defects in what was ruled. Per the close
rule, a no-MAJOR pass closes the cycle — what remains is the principal's to
decide into the backlog.

**PASS-WITH-FINDINGS — 0 MAJOR · 2 MEDIUM · 5 LOW.**

---

## Decision (Mike, 2026-07-15) — F1–F7 ruled as counselled; applied; cycle closed

Mike accepted the reviewer's counsel on all seven findings. Applied same day
by the taking session — which wrote this brief and spawned the reviewer, and
authored neither rule 4, the prior verdict, nor the applied batch under
review; named, not hidden. The 0-MAJOR pass had already closed the ceremony
(close rule), so this terminal application queues no pointer — the first
exercise of the F1 fix it applies.

- **F1 [fixed]** — the applier seam conditioned on the cycle being open; the
  terminal application (applying the rulings of a no-MAJOR pass) closes
  without a queued pointer, per the close rule.
- **F2 [fixed]** — rule 4's handoff spec is now a ceiling as well as a
  floor: the `⏳` pointer carries refs only (delta + intent record), no
  evaluative account — that belongs in the intent record, where the
  reviewer's deferral discipline governs when it is read.
- **F3 [fixed]** — MODEL-ECONOMICS §Sub-agents' paraphrase aligned to the
  full criterion ("a session the author neither started nor instructed").
- **F4 [fixed]** — "commissioning provenance" → "spawn provenance"; the
  commission family is gone from the rule.
- **F5 [fixed]** — the ROADMAP legend now defines `⏳`: review queued for a
  non-author to take; any criterion-passing spawner may take it; the taker
  writes the brief.
- **F6 [fixed]** — the application-review subject stated: rule 4's criterion
  tests the *delta's* author (the applier) at minimum, prior authors in the
  chain where practical.
- **F7 [fixed]** — the comma before "whichever".

0 MAJOR at the pass ⇒ the ceremony closed on this ruled application; no
further pass is owed.
