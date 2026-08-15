# Cold pass — the Three Laws and the Zeroth leave the apex

**Pass type:** doctrine cold pass (REVIEW.md rule 4 — the apex is the
highest-stakes self-authored doctrine surface in the repo; the principal
ruled the intent, the agent's judgement produced the wording and the sweep).
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04).
**Status:** BRIEF WRITTEN, REVIEW NOT RUN. The next cold session that passes
rule 4's criterion and the tier bar takes it — see *Spawn provenance*.

## Spawn provenance

- **Author of the work under review:** the session that landed the delta on
  2026-08-15 (wt: `laws-removal-0815`; see *What the work is*).
- **Who wrote this brief:** a cold session Mike opened on 2026-08-15 with
  the standing instruction, verbatim: *"As a cold session please do any review
  work, any work that is fable dependent, and write briefs for any reviews
  that need them. If you write the brief then do not run the review, that
  will require another cold review session."* That session authored no part
  of this delta, was neither started nor instructed by the authoring session,
  wrote this brief from the delta and the queue pointer only (it did not open
  the intent record), and **stopped** — it did not run the review.
- **Who takes the review:** the next cold session that meets rule 4's single
  criterion — a session the author neither started nor instructed — on the
  Fable tier, checked at selection. The taker repeats its own provenance in
  the verdict: how it was spawned, and its non-involvement with both the
  authoring session and the brief-writing session.
- **Orchestration shape:** the deferred material sits in the sibling file
  `2026-08-15-1031-laws-removal-apex-cold.deferred.md` (rule 1's split): the
  intent-record reference, the prior-verdict references, and the
  brief-writer's seeded questions. Recommended: the taker runs the review
  under an orchestrator that holds the sibling's bytes and hands them to the
  reviewer only after its findings are durably written. A taker reviewing by
  hand opens the sibling as a deliberate second act after its findings are
  written, and says so in the verdict. Fold in and delete when the verdict
  lands.

## What the work is

Landed 2026-08-15 on `main` as `71b3e8f` (the removal), preceded by the claim
`4ea0a8f` and followed by the merge `b5da9e5`. Reviewed at HEAD:

1. [`docs/method/00-APEX.md`](../method/00-APEX.md) — the section that held
   the Laws is deleted; the title, § *Why this is level 0*, and every count
   of the apex's parts are reworded to a duo.
2. The restatement surfaces swept in the same commit:
   [`README.md`](../../README.md), [`docs/method/README.md`](../method/README.md),
   [`docs/method/GLOSSARY.md`](../method/GLOSSARY.md) (*Apex*),
   [`docs/method/PRINCIPLES.md`](../method/PRINCIPLES.md) (§0 intro and the
   precedence ladder), [`docs/method/PROPAGATION.md`](../method/PROPAGATION.md)
   (the fail-safe line, the SR2 concern list, and the inlined child floor
   block), the byte-identical stamp in
   [`docs/build/templates/CLAUDE.md`](../build/templates/CLAUDE.md), and
   [`skills/session-onramp/SKILL.md`](../../skills/session-onramp/SKILL.md).
3. Board changes in the same commit: the ruling item
   `docs/roadmap/020-…/210-…` closed, the pointer `215-…` opened, the
   Laws-ladder raw note removed from *Open questions*, and the
   `160-…/140-…` propagation item reworded.
4. The `CHANGELOG.md` *Removed* entry.
5. **What was deliberately left**, per the commit message: historical records
   and prior review verdicts (the history layer), and children's floor blocks
   (they shed the sentence at their next pin bump).

## Scope

Widest the work admits: the ruling as executed against the ruling as given
(the intent is the principal's; the wording, the sweep, and the judgement of
what counts as a restatement surface are the author's), the apex text that
remains and whether it still stands as a complete frame without the third
part, every surface that restated the Laws inside and outside `docs/method/`,
what the removal leaves dangling, and how the change reaches the fleet.
**Non-goals — one, and it does not fence the risk:** the reviewer does not
decide any finding; the apex is principal-ruled doctrine and findings are the
principal's to rule on (rule 3). Counsel may be recorded, labelled as such.
The *decision* to remove the Laws is the principal's and is not under review;
its *execution* is.

## The four lenses

1. **Approach & assumptions** — name the load-bearing assumptions yourself
   first. What did the Laws section carry beyond the Laws themselves (its
   caveats, the "surface a genuine dilemma" instruction, the "sits within the
   agent's own safety values" statement) — and does anything that survives
   the removal now rest on a sentence that is gone?
2. **Correctness & quality** — is the apex text internally consistent as a
   duo? Do the surviving cross-references (glossary, precedence ladder,
   propagation floor block, skill) say the same thing as `00-APEX.md` at HEAD?
3. **Completeness / harvest** — search the whole tree yourself: which
   surfaces still restate the Laws, the Zeroth, or "the three" — doctrine,
   templates, skills, plugin surfaces, `docs/build/`, instrument READMEs? Was
   the sweep checklist the author followed the right checklist? Is the
   history-layer carve-out drawn where the doctrine draws it?
4. **Security & privacy** — mandatory. atelier is PUBLIC; the apex is its
   most-read file. Check the delta and its record surfaces for anything that
   joins a private repo's name to its posture or carries estate detail. If the
   lens genuinely has no surface beyond that, discharge it in one explicit
   line with grounds. The house security scanner reads pending diffs; this is
   a landed-delta review, so state the reach case that applied.

## Re-run obligation

Re-run, do not read: the tree-wide search for every restatement surface (the
commit's own claim is "every restatement surface swept" — test it against a
grep you write yourself, including outside `docs/method/`); the byte-identity
claim between PROPAGATION.md's inlined floor block and
`docs/build/templates/CLAUDE.md`; the floor on both planes at HEAD; and the
propagation lane's behaviour for a child at its next pin bump (read the
mechanism, provoke it read-only if the repo admits it).

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the deferred material lives in the sibling .deferred.md under the rule-1 split, opened only after the reviewer's findings are durably written -->

Rule 2 bars: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`,
every prior verdict in `docs/reviews/`, and the intent record for this delta.
The sibling `.deferred.md` holds those references and the brief-writer's seeded
questions; open it after your findings are committed. Reconcile after, never
anchor before. A taker whose own session onramp has already read the
`SESSIONS.md` tail discloses that in the verdict.

## Process

Append your verdict below a `---` divider in this file: provenance repeated,
per-lens answers, findings with stable IDs (prefix `LR`) and severities
(MAJOR / MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL
line with counts, and a follow-up checklist. Then open the sibling; append a
reconcile section; fold the sibling in below it and delete the sibling;
finalise. Update the queue pointer
(`docs/roadmap/020-policy-as-code-programme-five-tracks-mik/215-rule-4-cold-pass-queued-laws-removal.md`)
and rebuild the index in the same commit.
