# Cold pass — the 2026-08-17 ruling round applied to doctrine

**Pass type:** doctrine cold pass (REVIEW.md rule 4 — the delta rewrites the
apex, the review rules, the record and guard doctrine and the floor block that
every child stamps; its wording is the applying session's own, produced from
rulings the principal gave in a few words each).
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04). Checked
at selection: a session that cannot honour the bar stops rather than takes.
**Status:** BRIEF WRITTEN, REVIEW NOT RUN. The next cold session that passes
rule 4's criterion and the tier bar takes it — see *Spawn provenance*.

## Spawn provenance

- **Author of the work under review:** the session that applied the rulings on
  2026-08-17 (wt: `rulings-0817`, landing commit `7388012`, merged to `main`
  in PR #27; Opus tier per the commit trailer). The same session had earlier
  orchestrated the two cold passes whose findings the rulings answer, so it is
  the author of the application *and* the party that asked for the rulings.
- **Who wrote this brief:** an atelier session Mike opened 2026-08-17 at 0955
  UTC on the **Fable** tier under his standing cold-session instruction (*do
  any review work, any Fable-dependent work, write briefs for reviews that
  need them; a brief-writer never runs its own brief*). It authored no part of
  this delta, was neither started nor instructed by the authoring session, and
  has edited no file this delta touches. It wrote this brief from the diff of
  the seven delta paths at `7388012` and from the queue pointer; it did **not**
  open the board section `290-…` that carries the rulings, the intent record,
  or any board item the landing commit updated.
- ⚠️ **Two disclosures, both about the brief-writer.**
  1. **It read the `docs/SESSIONS.md` tail** at session onramp, before this
     brief was commissioned. The last index entries there summarise, in the
     author's words, the two cold passes that produced the findings these
     rulings answer, and the ruling round itself. That is rule-2 barred
     material and it was read. It is why the board section and the intent
     record were left unopened, and why the seeded questions in the sibling
     are held to what the diff shows.
  2. **It read the landing commit's message in full.** The message is the
     author's account of what each ruling meant and why the application takes
     the shape it does. Generate your own reading of the diff before you weigh
     anything this brief says about it.
- **Who takes the review:** the next cold session meeting rule 4's single
  criterion — a session the author neither started nor instructed — on the
  Fable tier, checked at selection. The taker repeats its own provenance in the
  verdict: how it was spawned, and its non-involvement with both the authoring
  session and this brief-writing session.
- **Orchestration shape:** the deferred material sits in the sibling
  `2026-08-17-1000-ruling-round-application-cold.deferred.md` (rule 1's split).
  Recommended: run under an orchestrator that holds the sibling's bytes and
  releases them only after the reviewer's findings are durably written. Under
  the delta's own new clause, an off-tier orchestrator is permitted only if it
  forms no finding and the arrangement is disclosed in the claim, the pointer
  and the verdict — this pass is a first-hand test of whether that clause is
  followable as written. A taker working by hand opens the sibling as a
  deliberate second act after its findings are committed, and says so. Fold in
  and delete when the verdict lands.

## What the work is

One commit, `7388012`, seven doctrine paths, three rulings. Reviewed at HEAD.

**Ruling one — the orchestrator-tier clause.** `docs/method/REVIEW.md` rule 4
gains a paragraph stating what the named review tier binds: *the judgement
that forms findings, not every hand the pass passes through*. A pass may run
as reviewer-plus-orchestrator; the reviewer is on the named tier without
exception; an orchestrator that holds the context partition, releases the
deferred sibling and commits the records may be off-tier on two conditions —
it forms no finding and writes no severity, and the arrangement is disclosed
in the claim, the pointer and the verdict's provenance, before the findings.
Absent either, the stop clause applies unchanged. Grounding cited inline: a
2026-08-17 run that used the shape, disclosed it, and asked.

**Ruling two — the always-confirm-floor exception.** `docs/method/00-APEX.md`
§ *The principal's authority is absolute* keeps its existing wording that an
approval extracted without a what/why/impact account *stands but is
challengeable*, and gains one exception paragraph: where the approval is an
always-confirm floor stop, the re-briefing must come **before** the
irreversible action, never as a challenge after it. Restated in one sentence
each in `REVIEW.md` rule 3, the `PROPAGATION.md` floor block, and the
byte-identical stamp in `docs/build/templates/CLAUDE.md`.

**Ruling three — a home for an earned rule, and for its class.**
`docs/method/RECORD.md` gains § *An approval is not the whole ruling — the
reservations go in beside it*: when a recommendation is approved with
reservations, the reservations are recorded verbatim beside the approval and
each becomes a check the build must answer. `docs/method/GUARDS.md` gains
§ *A rule with no home is not a rule*: a rule stated only in a record (commit
message, session record, board item) governs nothing, because rule 2 bars a
cold reviewer from records and no onramp loads them; the test is *name the
surface a future session reads it on*. `docs/method/COMMUNICATION.md` keeps
the grounded instance and points at both.

The commit also updated the board items in `290-…` and the queue pointer; the
pointer scopes this pass to the seven paths and deliberately not to the commit.

## Scope

Widest the work admits. This delta's subject is **rulings given in a few words
each, rendered into doctrine by the party that asked for them**, so the
reviewable question is not only whether each paragraph is well written but
whether it says what was ruled — no more, no less — and whether what it adds
composes with the rules already on those pages. In scope: whether the
orchestrator-tier clause's two conditions are checkable by a later reader
from the durable record alone, and what "forms no finding" excludes in
practice (does choosing which reviewer to spawn, which surfaces to release,
or how to word the release message form a finding?); whether the
always-confirm exception's list of floor stops matches the floor as it is
defined elsewhere in the apex and in `AUTONOMY.md`, or introduces a second
list; whether *stands-but-challengeable* plus *re-brief before acting at the
floor* is a coherent pair or a rule and its negation with a boundary drawn
between them; whether the RECORD.md section states a rule or a story
(grounding paragraphs are evidence, not the rule — is the rule extractable in
one sentence?); whether GUARDS.md's test is applicable by a session that has
just written a commit message, or only recognisable in hindsight; whether the
COMMUNICATION.md clause now duplicates or merely points; and whether the
templates stamp is byte-identical to the PROPAGATION block at HEAD, and every
child that will re-stamp it can render the added sentence without a floor red.

**Non-goals, and neither fences the risk:** the rulings themselves are the
principal's and are not under review — only their rendering into doctrine;
and no finding is decided by the reviewer (rule 3), so the findings go to the
principal's next ruling round.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself
   first. Then: each of the three rulings is applied as *additive prose* — a
   new paragraph, a new section, an added sentence — and nothing on those pages
   was removed or reworded to make room. Is that the right shape, or does the
   apex paragraph now carry a rule, an exception to it, and the pre-existing
   waiver clause in one run of prose that a reader must parse in order? The
   orchestrator-tier clause is written as a permission; consider whether the
   same ruling reads more safely as a definition of *reviewer* (the party on
   the tier) with the orchestrator falling out as whatever is left. The GUARDS
   section states that a rule written only to a record reaches nobody —
   apply that test to this delta itself: does each of the three rules now sit
   on a surface a session actually loads (which method docs are read on
   demand, and which are onramp)?
2. **Correctness & quality.** Read the diff of all seven paths, then read the
   whole of each touched section as it now stands — a diff hides what it did
   not touch. Check that the apex exception's enumerated floor stops agree
   with the always-confirm floor as defined in the apex's own earlier text and
   in `AUTONOMY.md`; check that REVIEW rule 3's one-sentence restatement and
   the PROPAGATION sentence say the same thing as the apex paragraph, and that
   the templates stamp is byte-identical (`tools/stampscan.py`, and the test
   that asserts it). Check the orchestrator clause against REVIEW rule 1's
   existing description of the context partition — the two now describe the
   same arrangement; do they agree on who may hold the sibling and when it is
   released? Check the RECORD.md section's cross-references resolve and that
   the grounding it narrates is dated consistently with what it claims.
3. **Completeness / harvest.** Every surface that states the pre-exception
   rule or describes the orchestrator arrangement: `00-APEX.md` (any other
   paragraph on extracted approvals), `REVIEW.md` (rules 1, 3, 4 and *The
   lifecycle*), `PROPAGATION.md`, the templates, `AUTONOMY.md`, `GUARDS.md`,
   `RECORD.md`, `COMMUNICATION.md`, `CHANGELOG.md` (the *Changed* entry
   landed one commit later, `613132e` — check it covers all three rulings and
   agrees with the doctrine text), and `docs/build/` and any skill or
   template that restates the floor. Does any surface still carry the
   pre-ruling wording that the ruling changed? Did the ruling round have more
   asks than three, and are the unapplied ones queued visibly for a session
   that was not there?
4. **Security & privacy** — mandatory. atelier is PUBLIC. The delta names a
   principal by role and cites dates and a run shape; check nothing in the
   seven paths names a private repo, a machine path, or a person beyond the
   published identity the repo already carries. The always-confirm exception
   is itself a security-posture rule (it governs the moment before an
   irreversible action): test whether its wording could be read as *permitting*
   an extracted approval to be acted on at the floor once re-briefed a single
   time, and whether that is the ruling. The house security scanner reads the
   session's pending diff whatever path it is aimed at; this is a landed-delta
   review, so state the reach case that applied rather than assuming one. If
   the lens has no surface beyond these, discharge it in one explicit line
   with grounds.

## Re-run obligation

Re-run, do not read:

- The floor on **both** planes at HEAD, and the full Python and node suites.
  Lift the invocations from [`.githooks/pre-commit`](../../.githooks/pre-commit)
  and `.github/workflows/ci.yml` rather than guessing them.
- The byte-identity claim: `docs/build/templates/CLAUDE.md`'s stamped block
  against `docs/method/PROPAGATION.md`'s floor block, via `tools/stampscan.py`
  and the templates test — say what the tool reports and how many lines it
  compared.
- The grounding claims inside the doctrine text: the apex paragraph says a
  cold pass found the *stands-but-challengeable* wording was a derivation, and
  rule 4 says a 2026-08-17 run used the orchestrator shape and asked. Those
  claims point into barred material; in phase 1 note them as claims and
  verify them at reconcile, when the sibling names where they live.
- `plainscan` over the seven paths (advisory): the delta adds several long
  sentences to onramp-adjacent doctrine; report the count it adds, if any,
  as a measurement rather than a finding.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the deferred material lives in the sibling .deferred.md under the rule-1 split, opened only after the reviewer's findings are durably written -->

Rule 2 bars: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`,
every prior verdict in `docs/reviews/` (the apex-authority and reply-gate
passes especially — the findings these rulings answer), the board section
`docs/roadmap/290-…/`, and the intent record for this delta. Sweep the tree
with `python3 tools/coldsweep.py`, whose default exclusion is exactly that
set; if you use `--include-barred`, disclose it. The sibling `.deferred.md`
holds those references and the brief-writer's seeded questions; open it after
your findings are committed. Reconcile after, never anchor before. A taker
whose own onramp has already read the `SESSIONS.md` tail discloses that in
the verdict, as this brief-writer has.

Reading the *doctrine* is not barred — the seven paths at HEAD and every
method doc they cross-reference are the delta and its context. What is barred
is the author's narrative of why, and the findings that prompted it.

## Process

Append your verdict below a `---` divider in this file: provenance repeated,
per-lens answers, findings with stable IDs (prefix `RR`) and severities
(MAJOR / MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL
line with counts, and a follow-up checklist. Then open the sibling; append a
reconcile section; fold the sibling in below it and delete the sibling;
finalise. Update the queue pointer
(`docs/roadmap/160-doctrine-review-owed/230-rule-4-cold-pass-queued-the-0817-ruling-round.md`)
and rebuild the index in the same commit. Findings on this delta are the
principal's to decide (rule 3): record them, apply nothing.

---

# Verdict — RR cold pass (phase 1)

**Run:** 2026-08-17, opened 13:26 UTC, phase-1 verdict written 13:46 UTC.
**Reviewed at:** HEAD `574f133` (main + the claim commit); delta landed at
`7388012`. **Overall: PASS-WITH-FINDINGS — 0 MAJOR / 3 MODERATE / 5 minor /
3 notes.** Nothing applied, nothing fixed (rule 3).

## Provenance and disclosures

- **How this reviewer was spawned.** A Fable-tier reviewer subagent, spawned by
  an orchestrator session that Mike opened 2026-08-17 at 1321 UTC on the Fable
  tier under his standing cold-session instruction (do any reviews and any
  Fable-dependent work; write any briefs required). The orchestrator wrote none
  of the delta and none of this brief; it formed no finding and wrote no
  severity — every finding, severity and word below is the reviewer's. This
  reviewer was neither started nor instructed by the authoring session
  (`rulings-0817`, Opus) nor by the brief-writing session (0955 UTC, Fable), and
  has edited no file the delta touches.
- **The arrangement is the one rule 4's new clause describes**, and it is
  disclosed in the claim commit (`574f133`), in the queue pointer's TAKEN line,
  and here — before the findings. **What the orchestrator did**, recorded so a
  later reader can check condition one from the record rather than take it on
  attestation: it wrote a common reviewer-instruction file (process only: the
  rule-2 bar, the barred-path list, the coldsweep-only rule, the re-run
  invocations, the deliverable shape, the two-phase sibling release); it moved
  the `.deferred.md` sibling out of the tree; and its per-pass prompt named the
  finding prefix, the pass-specific barred paths, the delta, and added one
  directed request — to say in the provenance whether the rule-4 clause was
  followable in this reviewer's own case, marked "evidence, not a seeded
  question — form your findings first". That request echoes the brief's own
  sentence on the point and did not move a finding. **Both hands were on the
  Fable tier**, so the clause's off-tier permission was *not* exercised in this
  run — this pass is evidence that the reviewer-plus-orchestrator shape and its
  disclosure conditions are followable, not evidence about an off-tier
  orchestrator.
- **Rule 2 exposure.** Not opened: `docs/SESSIONS.md`, `docs/sessions/`,
  `docs/ROADMAP-DONE.md`, any other file under `docs/reviews/`, and the board
  section `290-…` (I listed its filenames and read the checkbox glyphs of its
  index lines in `docs/ROADMAP.md` — no titles, no bodies — to answer lens 3's
  "were the unapplied asks queued visibly"). Read: the landing commit's
  **subject line only** (via `git log --format=%s`, never the body); the claim
  commit's full message (it is the disclosure the clause requires); the queue
  pointer 230; the CHANGELOG entry the brief names. Every tree sweep ran through
  `tools/coldsweep.py` via a wrapper that always adds the pass-specific
  exclusions; `--include-barred` was never used. Sibling briefs and pointers of
  the parallel passes were not opened; one hook-plane pointerscan line quoted
  the first sentence of pointer 240 (a parallel pass's pointer) — a title, no
  finding.
- **Security scanner reach case.** `/security-review` and every pending-diff
  scanner read the session's pending diff, which in this shared tree is other
  passes' in-flight work; this is a landed-delta review, so neither was run.
  Lens 4 is discharged by the floor's own scanners at HEAD (below).

## Re-run ledger (re-run, not read)

| What | Result | Counts measured |
|---|---|---|
| Floor, hook plane (`floor.py --plane hook`) | exit 0 | 10 enforced ✅, 4 warn-only 👁️, 1 enforced with advisories; sizescan 2 size-advisories (`ROADMAP.md` 338 lines, `SESSIONS.md` 273); pointerscan 1 grammar finding on pointer 240 (not this pass); plainscan tree tally 5357 |
| Floor, CI plane (`floor.py --plane ci`) | exit 0 | secretscan 22 advisory (entropy), leakscan clean with `local-term×3` in the tally; harvestscan −43 net record lines (under gate); plainscan tree tally 5388 |
| Python suite (`unittest discover -s tools`) | exit 0 | 1344 tests, OK, 328 s |
| Node suite (`node --test instruments/*.test.js`) | exit 0 | 235 pass, 0 fail, 0 skipped |
| Templates test (`tools.test_templates`) | exit 0 | 44 tests OK, incl. `test_stamped_block_matches_canonical` |
| `stampscan` (tree, and the template alone with `--json`) | exit 0 | 1 stamped block, kind `identical`, canonical region `floor`, **61 lines compared**; 117 files suppressed by `.stampscanignore` on the tree run |
| `plainscan` over the seven paths, in a scratch clone | pre-delta 225 · landing 233 · HEAD 237 | the delta adds **9 P3 (long-sentence) findings and removes 1** — net **+8**; P1/P2/P4 unchanged. The floor-block sentence in the template grew from 36 to **58 words** (the PROPAGATION copy sits in a fence and is not counted). The +4 from landing to HEAD are later commits, not this delta |

No suite result looked like interference; nothing was re-run twice.

## Lens 1 — approach & assumptions (named before weighing the brief)

Load-bearing assumptions I named first: (a) the delta says what was ruled and
no more — unverifiable to me in phase 1, so I reviewed *what the paragraphs
now bind* rather than what was said; (b) additive prose is the right shape —
attackable, see RR6; (c) the seven paths are the whole application — checked
by sweep (lens 3), true for the extracted-approval rule and the orchestrator
arrangement, not quite for the floor list (RR8); (d) each ruling was
"applied" once — the CHANGELOG entry (`613132e`) covers all three and agrees
with the doctrine text; (e) the pass was owed at all — REVIEW § *The
lifecycle* closes an application without a queued pointer when the passes it
applies returned no MAJOR; whether these did is barred material, noted for
reconcile; over-queuing is not a defect.

*Additive shape.* Rulings two and three landed as clean insertions; ruling one
was inserted mid-paragraph inside rule 4, splitting the grounding sentence
from the provenance sentence it used to lead into. The apex paragraph now runs
rule → exception → waiver, and the waiver's "But once the account has been
offered" now contrasts against the exception rather than the extracted-
approval sentence it was written against (RR6).

*Permission vs definition.* The clause already defines the reviewer by
function (reads the delta, answers the lenses, assigns severities, writes the
reconcile) — the definition the lens asks for is there. The permission wording
is defensible because it carries an obligation a bare definition would not
(the three-place disclosure). What neither shape settles is the middle: the
hands that are neither reviewer nor the three named orchestrator acts (RR2,
RR5).

*The delta's own test, applied to the delta.* Ruling two sits on the apex
(onramp) and in the floor block every child stamps — reaches every session.
Ruling one sits in rule 4, which every cold taker is pointed at — reaches its
readers. Ruling three sits in `RECORD.md` and `GUARDS.md`, both read on demand;
`RECORD.md`'s section is adjacent to the ADR and board sections a recording
session reads, so it is findable at the moment it governs; `GUARDS.md`'s rule
governs the moment a session writes "this is a rule we've earned" into a
commit message or close — nothing at that moment points to it (`RECORD.md` §
*The why lives at the site* is where commit messages are governed). It passes
its own literal test (it is on a doctrine surface) but its findability at the
point of use is thin — folded into RR4's follow-up rather than a separate
finding.

## Lens 2 — correctness & quality

- **Floor-stop lists.** The apex exception enumerates seven stops; the apex's
  own earlier paragraph enumerates the same seven; the PROPAGATION block and
  template enumerate eight (adding *widening your own grant* and *installing
  an unapproved tool*); `AUTONOMY.md` § *Always confirm* enumerates eleven
  bullets including *deploy-on-push when not routine*. The exception's list is
  the narrowest, and the apex classes grant-widening as a **governance ruling**
  where AUTONOMY and the floor block class it as a **floor stop** — RR1.
- **Rule 3, PROPAGATION, template vs the apex paragraph.** They say the same
  thing (order fixed at the floor; before, never after). Template ≡ PROPAGATION
  byte-for-byte (61 lines, stampscan; templates test). Rule 3's sentence sits in
  a rule about governance rulings, where a floor stop rarely arises (RR10).
- **Rule 4 clause vs rule 1's partition.** They agree: rule 1 says the deferred
  bytes stay with the orchestrator and reach the reviewer "on receipt of its
  committed findings"; rule 4 says "after the findings are durably written";
  rule 2 defines committed as durably written to the draft. Same holder, same
  release point.
- **RECORD.md cross-references and dating.** § *An approval…* cites "the
  verbatim rule above" — **there is no such rule in `RECORD.md`** (RR3). Its
  `GUARDS.md` § reference resolves. Dates are consistent across the three
  surfaces: earned 2026-08-15, ruled 2026-08-17 ("two days" in COMMUNICATION),
  guard live 2026-08-09→2026-08-15 ("six days" in RECORD, matching the reply-
  plane dates in COMMUNICATION).
- **Coherent pair or rule-and-negation?** Coherent. The base rule permits
  challenge and obedience "in either order"; the exception fixes the order at
  the floor and expressly keeps "not a licence to refuse". The extracted
  approval still *stands* at the floor — what changes is that it may not be
  *acted on* until re-briefed. The boundary is the floor, and the floor is the
  one place the difference is unrecoverable; that is a boundary with a reason,
  not a negation.
- **RECORD.md: rule or story?** Extractable in one sentence — the bold opener
  is the rule; the grounding paragraph is evidence. Its consequences bullet the
  operative content (verbatim capture; reservation = check).
- **GUARDS.md: applicable prospectively?** Yes — the test ("name the surface a
  future session reads it on") is answerable at commit-message time. Its
  grounding sentence overstates on two counts (RR4).
- **COMMUNICATION.md: duplicates or points?** Points, and says why it points —
  but RECORD.md then retells the same instance anonymised (RR7).

## Lens 3 — completeness / harvest

Swept (coldsweep) for every surface stating the extracted-approval rule:
apex, REVIEW rule 3, PROPAGATION block, template — all carry the exception;
`AUTONOMY.md` uses "obedience extracted" as a term pointing at the apex and
needs no restatement. Every surface describing the orchestrator arrangement:
REVIEW rules 1 and 4 and § *When to review* — consistent. Surfaces restating
the **floor list**: `skills/session-onramp/SKILL.md` § 2 carries the list with
neither the informed-confirmation clause nor the new ordering sentence, and
stampscan does not watch it (RR8). CHANGELOG *Changed* entry: present at
`613132e`, covers all three rulings, agrees with the text. The ruling round
had **seven** items, not three: four are ✅ on the index and three remain open
🎯 — visible to a session that was not there.

## Lens 4 — security & privacy

Leakscan clean on both planes at HEAD (`local-term×3` are the known published-
identity lines); the seven paths' new text names the principal by role only,
one date and one run shape, no machine path, no private repo. Reach case:
stated above — no pending-diff scanner was run. **The single-re-brief reading:**
the exception says "supplies the missing account and asks again, and if the
principal rules the same way it acts" — one complete re-brief and a same
ruling is enough. That is not a hazard: a re-briefed approval is by
construction an *informed* one, which is what the floor block already requires
of every floor confirmation ("first"), so the exception is followed the moment
the ordinary floor rule is. What the wording leaves to the surrounding text is
that the re-brief must be *complete* ("unprompted, plain, complete" — the
waiver paragraph); it does not need restating. Whether that single-pass shape
is the ruling is for reconcile. Discharged with grounds beyond that.

## Findings

**RR1 · MODERATE — the exception restates the floor list, and the restated
list is narrower than the floor.** `00-APEX.md` § *The principal's authority…*
exception paragraph enumerates seven stops (public, destructive/irreversible,
secrets, spend, safety, lockout, new trust surface). `AUTONOMY.md` § *Always
confirm* and the PROPAGATION floor block both list **widening your own grant**
as a floor stop (AUTONOMY: "the agent *records* a grant, never *originates*
one"); the apex's earlier paragraph classes it as a governance ruling instead.
Before this delta that mismatch was harmless — "the rule binds them all". Now
the exception's scope *is* the floor-stop set, and read literally an extracted
approval to widen the agent's own grant may be acted on and challenged after.
The floor is defined once in `AUTONOMY.md`; the apex now carries two
abbreviated copies and `PROPAGATION.md` § *One statement, stamped copies*
names three independent statements as the defect. *Reproduce:* compare
`00-APEX.md` lines 80–88 and 111–115 with `AUTONOMY.md` § *Always confirm* and
`PROPAGATION.md` lines 112–120. *Suggested shape (principal's call):* the
exception says "where the approval is an always-confirm floor stop
(`AUTONOMY.md` § *Always confirm* is the list)" and enumerates nothing; and the
apex's governance/floor classification of grant-widening is reconciled with
AUTONOMY's.

**RR2 · MODERATE — the clause's first condition is an attestation, not a
check, and its boundary is undrawn.** `REVIEW.md` rule 4: "the orchestrator
forms no finding and writes no severity". A later reader can verify condition
two from the record (claim, pointer, verdict) but condition one only if the
orchestrator's reviewer-facing instructions are in the record — and nothing
requires that. In this very run the orchestrator wrote a common instruction
file, chose the pass-specific barred paths, and appended a directed provenance
request; none of that is durable unless the reviewer transcribes it (as done
above). Nor does the clause say which acts are "orchestration" and which are
judgement: authoring the spawn prompt, scoping the barred set, choosing what
the reviewer may open at reconcile, answering mid-flight questions, and — most
sharply — reading and *endorsing* the verdict at commit ("commits the records"
is listed as non-finding work; `skills/queue-run` says "read what you endorse
before it lands"). *Suggested shape:* the verdict's provenance carries the
orchestrator's reviewer-facing instructions verbatim or by attached file, and
the clause names what orchestrator direction may contain (process: paths,
tools, barred set, deliverable shape, release timing) and may not (any
question about the delta, any pointer to where risk lives, any request to
revise a finding).

**RR3 · MODERATE — `RECORD.md` § *An approval is not the whole ruling* leans
on "the verbatim rule above", and no such rule exists on that surface.**
Line 195: "The reservation goes down as it was said (the verbatim rule
above)". The only "verbatim" in `RECORD.md` above it is the session-index
*relocation* rule (line 58) and a quoted-token anecdote (line 79). A coldsweep
for `verbatim|own words|word for word|as he said` finds the practice of
capturing the principal's words verbatim in **board items only** (`README.md`
of several sections, "The ruling, verbatim") — records, the exact class
`GUARDS.md`'s new section says governs nothing. So the delta's own test fails
on the rule the delta's first consequence rests on. *Suggested shape:* home the
verbatim-capture rule (in `RECORD.md`, one sentence, grounded in the board
practice) and re-point the reference; or drop the parenthetical.

**RR4 · minor — `GUARDS.md` § *A rule with no home* grounds itself on two
overstatements.** "Rule 2 bars a cold reviewer from reading records" — rule 2
bars four named stores; commit messages and board items are not in its text
(the pointer discipline keeps a reviewer out of the intent record, which is
narrower). "No onramp loads them" — this repo's onramp loads the `SESSIONS.md`
tail and the board index, and a board item is read by whoever takes it. The
accurate ground is narrower and still carries the rule: a record is read once,
by one reader, or by none — never by every session it was meant to govern, and
never by a cold reviewer of the delta it concerns. *Follow-up beside it:* the
rule governs the moment a commit message or close is written, and nothing at
that moment points to it — a one-line pointer from `RECORD.md` § *The why
lives at the site* (commit messages) or the put-away checklist would close the
findability gap.

**RR5 · minor — "orchestrator" is now overloaded across surfaces without a
cross-reference.** `ECONOMICS.md` § *The orchestrated-run tier split*: "the
capable tier orchestrates and reviews"; `skills/queue-run/SKILL.md` step 1:
"Do not proceed off-tier". Rule 4: an orchestrator "may be off-tier". These are
different roles — the queue-run orchestrator judges at merge, rule 4's forms no
finding — but a batched run of cold passes (REVIEW § *When to review*, batched
path) is both at once and meets both texts. Also: the clause names two hands
(reviewer, orchestrator) where the live practice has three — the brief-writer,
who writes the seeded questions, is bound by neither sentence. *Suggested
shape:* one clause naming which orchestrator the permission is for, and a word
on the brief-writer's tier.

**RR6 · minor — apex paragraph order.** The waiver paragraph opens "But once
the account has been offered", written against the extracted-approval sentence
that now sits a paragraph above the exception; the "But" now reads against the
exception. Rule, exception and waiver run as one sequence a reader must parse
in order. *Suggested shape:* place the exception after the waiver paragraph, or
re-anchor the waiver's opener ("Once the account has been offered — in either
case —").

**RR7 · minor — the instance is now told twice.** `COMMUNICATION.md` says
"This clause keeps the **instance** … it is not the rule's home", and
`RECORD.md`'s grounding paragraph then retells the same instance anonymised
(guard recommended, approved with reservations, four words kept, six days
live) without pointing at the COMMUNICATION clause as its source. Two
narratives of one incident, one of them un-cited. *Suggested shape:* RECORD's
grounding paragraph becomes one sentence plus a pointer to `COMMUNICATION.md`
§ *The meta-rules* (the reply-plane clause).

**RR8 · minor — a third, unstamped restatement of the floor now lags the
canonical block by two sentences.** `skills/session-onramp/SKILL.md` § 2 lists
the floor stops with neither "each such confirmation is an *informed* one" nor
the new ordering sentence; stampscan verifies exactly one stamped block (the
template), so this copy is unwatched. Pre-existing shape; the delta widened
the gap on a security-posture rule the skill exists to carry to plugin-only
adopters. *Suggested shape:* stamp it (a `stampscan` header naming
PROPAGATION's floor region) or point it at the block.

**RR9 · note — "an approval alone never closes a recommendation" is universal
as written** (`RECORD.md` § *An approval…*, closing paragraph); it is true of
approvals given *with* reservations, and false of the plain case the board's
own "I accept your recommendation. Proceed." records. One qualifier fixes it.

**RR10 · note — rule 3's floor sentence is reachable but rare.** Rule 3 is
about governance rulings on findings; a floor stop arises there only when a
finding recommends a floor action and the ruling on it is the confirmation.
The sentence is not wrong; it is a 42-word addition (plainscan P3) to a rule
where the case is uncommon. Measurement, not a defect.

**RR11 · note — the floor-block sentence is now 58 words**, stamped into every
child's `CLAUDE.md` on its next re-stamp; plainscan P3 in each, warn-only, no
floor red (wrapscan clean at HEAD, no dates or refs in the sentence). Net +8
P3 across the seven paths at landing. Measurement.

## Claims into barred material — noted for reconcile

1. `00-APEX.md`: "a cold pass found the *stands-but-challengeable* wording was
   the author's derivation rather than a recorded ruling, and … the
   pause-and-re-brief and act-now readings diverged".
2. `REVIEW.md` rule 4: "a 2026-08-17 run put two passes on Fable reviewers
   under an Opus orchestrator, disclosed it that way, and asked; the ruling
   accepted the passes".
3. `GUARDS.md`: "Two of the three recorded instances were found by a reviewer
   looking for something else."
4. `RECORD.md` / `COMMUNICATION.md`: earned 2026-08-15; "four words of
   approval"; "six days"; "two days in a commit message".
5. Whether the exception's single-re-brief shape, and the exception's
   enumerated scope, are what was ruled (RR1, lens 4).
6. Whether the passes these rulings answer returned a MAJOR (whether this
   pointer was owed under § *The lifecycle*'s close rule).

## Overall

**PASS-WITH-FINDINGS — 0 MAJOR / 3 MODERATE (RR1, RR2, RR3) / 5 minor (RR4–RR8)
/ 3 notes (RR9–RR11).** The three rulings are rendered on the surfaces named,
the copies agree with their canonical text, the floor is green on both planes
and both suites pass at HEAD. The MODERATEs are all of one kind: a rule stated
by restatement or by reference to something not on the surface — a floor list
re-enumerated narrower than the floor, a condition checkable only by
attestation, a cross-reference to a rule that has no home.

## Follow-up checklist (for the principal's ruling round; apply nothing here)

- [ ] RR1 — exception scope: refer to `AUTONOMY.md`'s floor by name, drop the
      enumeration; reconcile the apex's grant-widening classification.
- [ ] RR2 — rule 4 clause: require the orchestrator's reviewer-facing
      instructions in the verdict's provenance; name what orchestrator
      direction may and may not contain.
- [ ] RR3 — home the verbatim-capture rule in `RECORD.md`; re-point the
      reference.
- [ ] RR4 — narrow GUARDS' grounding sentence; add a pointer at the commit-
      message / put-away moment.
- [ ] RR5 — disambiguate the two orchestrators; say the brief-writer's tier.
- [ ] RR6 — re-order or re-anchor the apex waiver paragraph.
- [ ] RR7 — RECORD grounding → one sentence + pointer to COMMUNICATION.
- [ ] RR8 — stamp or point the session-onramp skill's floor list.
- [ ] RR9–RR11 — one qualifier; two measurements to note.
- [ ] Reconcile: verify the six barred claims above against the sibling's
      references; append `### Reconcile` beneath this verdict, never revising
      it.
