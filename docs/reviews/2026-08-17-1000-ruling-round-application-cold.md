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
