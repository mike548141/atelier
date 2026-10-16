# Cold pass — the standing reviewer checklist, and a test cannot falsify its own code

**Pass type:** doctrine cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection by whoever takes the pass.
**Status:** BRIEF ONLY — the review has NOT run. Written 2026-10-16 UTC by an Opus
brief-writer; the pass waits for a further cold Fable session that neither the
delta's author nor this brief-writer (nor its orchestrator) started or instructed.
Tier is checked at selection (rule 4).
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/710-rule-4-cold-pass-queued-checklist-and-test-rule.md`.
**Why it earns a review:** two rules that bind every future review and every test
written as evidence, landed in the review doctrine itself, in the evidence
doctrine, and in the skill that carries the review rule into other repos — so a
wrong word here is inherited by the very passes that would catch it.

## Spawn provenance

- **Author of the work under review:** the queue run whose intent record is dated
  2026-10-05 11:20 UTC (an Opus orchestrator with dispatched workers; the pointer
  counts the workers' output as the run's authorship). Not opened here.
- **Who wrote this brief:** an Opus subagent (`claude-opus-5-5`) dispatched by a
  Mike-opened Opus queue-run session (id prefix `abe96d8d`) on 2026-10-16 UTC, on
  Mike's answer that day that a fresh Opus session writes these briefs. It
  authored none of the delta. It is **off-tier for review, disclosed: it forms no
  finding and writes no severity**, and it stops after this brief and its sibling.
- **Who takes the review:** a further cold Fable session, not yet started, that
  passes rule 4's criterion. The reviewer repeats its own provenance in its
  verdict.
- ⚠️ **Exposure, disclosed** (rule-2 material met before writing). This
  brief-writer read: the queue pointer in full; both landing commits' subjects,
  `--stat`, diffs, **and message bodies** (the author's own account); the
  subjects and `--stat` of later commits on the same files; `REVIEW.md` rules 1–4,
  the four lenses, the checklist section under review and the lifecycle, at
  onramp; the ask halves of two 2026-10-04 briefs as templates; `docs/reviews/`
  filenames and filename-level greps (no prior verdict opened); the names, not
  contents, of the commissioning board items; and its harness-loaded memory index.
  Its orchestrator read the `docs/SESSIONS.md` index tail through 2026-10-16
  (including the authoring run's one-paragraph summary) and the 2026-10-16 session
  record's close section, and passed on no evaluative content beyond the pointer
  list. Everything evaluative is in the sibling.

## What the work is

Landing commits (diff these; review the paths at HEAD):

- `90c42ec` (2026-10-05 12:05 UTC) — review: V1-V7 become the standing checklist
  every review runs unasked (200/050)
- `be9a3ae` (2026-10-05 12:29 UTC) — evidence: a test cannot falsify its own
  code's assumption (200/020)
- both landed in merge `930d3d8` (2026-10-05 12:31 UTC)

Delta paths: `docs/method/REVIEW.md` § *The standing checklist — seven checks
every review runs unasked*; `skills/review-brief/SKILL.md` § *Running it and
landing the verdict* (one paragraph); `docs/method/EVIDENCE.md` § 15.

**Later commits on the same files — not this delta.** `b572594` (2026-10-16) —
mints "agreement is not corroboration" in `EVIDENCE.md`; it edits § 13, not § 15,
but sits in the same document. No later commit touches `REVIEW.md` or the skill.
The same authoring run also annotated the mining record the checklist links to,
in `b8aba22` (2026-10-05, board 200/110) — a records commit outside this delta.

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code, tests
and live behaviour. The lenses organise it; they do not bound it. Non-goals are the
only narrowing and are themselves reviewable.

**The checklist.** Whether each of V1–V7 points at a home that, at HEAD, actually
states that check (lens 2, the re-run section, `PRINCIPLES.md` § 6, `EVIDENCE.md`
§ 9, `PROPAGATION.md` § *One statement, stamped copies*, lens 4, rule 4) and says
the same thing; whether V5's claim to be canonical is true; whether the
"discharged in one line with grounds" clause is borrowed faithfully from lens 4
or widens it; whether "a brief need not list them" contradicts anything the
skill's brief template or `docs/build/` review templates still require; whether
the section's attribution ("Approved by the principal 2026-07-23, item by item")
and its counts and finding IDs are supported. **The skill.** Whether the
one-paragraph compression in `SKILL.md` honours its own header — a stamped copy
that "may compress the parent, never contradict it" — and whether any other
stamped or mirrored review surface (child templates, the plugin bundle,
`docs/build/templates/`) was owed the same line. **§ 15.** Test the rule against cases:
a test of an internal pure function; a test of a library call whose source is
vendored; a test against a recorded wire capture that is itself stale; a
property-based or differential test; a test pinned to a published specification
rather than to source. Does the text say which of these meet "an authority
outside your own code"? Whether its three risk sites and three grounding instances
are stated at no more detail than the public board item carries, and whether the
"> 2 promotion rule" it cites says what § 15 says it does. **Non-goals:** the
principal's approval of the seven checks and his ruling to mint § 15 — the wording
around them, their placement and their consistency are the subject.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself first.
   Among them: that an always-loaded list of pointers changes reviewer behaviour
   when its homes are elsewhere; that `EVIDENCE.md` rather than `REVIEW.md` is the
   right single home for the test rule; that "mutation-verified means wired, not
   right" generalises from three instances in one child repo.
2. **Correctness & quality.** Read both sections and the skill paragraph whole;
   diff each commit. Check every pointer and link resolves (V1–V7 targets, the
   `../sessions/` link, `PROPAGATION.md` anchors). Check § 15's tier word against
   § 2's definitions.
3. **Completeness / harvest.** Every surface that tells a reviewer what to run:
   `skills/review-brief/SKILL.md` whole, `docs/build/templates/` and any reviews
   template, the plugin bundle, `CLAUDE.md` onramps, `CONTRIBUTING.md`. Every
   surface that defines test evidence: `EVIDENCE.md` § 14, `docs/build/` testing
   guidance, `REVIEW.md`'s "a wrong test verifies nothing" line. Do they agree?
4. **Security & privacy** — mandatory. § 15 cites a private child repo's
   commit and its incidents in a public repo. Check every detail it carries
   against what the public board item already publishes, and whether any
   identifier, host, device or person could be inferred. Never quote such a
   detail in the verdict — describe and locate it. `/security-review` is
   discharged by grounds (a prose doctrine delta, already landed; markdown is
   outside that scanner's reach) — say so.

## Re-run obligation

Re-run, do not read. Lift floor invocations from `.githooks/pre-commit`,
`tools/floor.py` and `.github/workflows/ci.yml` rather than guessing.

- the lens-roster parity claim in `90c42ec`'s body: `python3 -m unittest
  tools.test_templates -v` (its `canonical_lenses` parser must still read four
  lenses), then add a temporary fifth numbered item under the checklist heading in
  a scratch clone and see whether the parser is fooled
- `python3 tools/stampscan.py --warn --root . .` and `python3 tools/linkscan.py
  --root . docs/method skills` at HEAD
- verify each cited finding ID exists by filename-level grep only (`grep -l`),
  before phase 1; open the verdicts only after
- the floor on both planes at HEAD; the full Python suite once, foreground

## House rules for this run

- Name the worktree you work in. Run no git command that writes there; read-only
  git is fine. Probes and scratch trees go in a private clone under your session
  scratchpad, named by your prefix.
- One heavy process at a time on a shared machine: the full suite at most once, in
  the foreground. Never point a scanner at any other repo on the machine.
- `/security-review` reads the session's pending diff: discharge it by grounds for
  this landed delta, or keep the tree clean whenever you spawn it.
- Dates absolute ISO 8601 from `date -u`. Prose wrapped at ≤ 100 columns. NZ
  English. Never quote a secret, placeholder token, email address or personal
  detail — this repo is PUBLIC; describe and locate instead.
- The checklist links its grounding to a mining record under `docs/sessions/`
  (barred below). It predates this delta, but the authoring run annotated it in
  `b8aba22`. You may read its pre-annotation text before phase 1 as the cited
  source — `git show b910962:docs/sessions/2026-07-22-1036-invariant-candidates.md`
  — and must disclose that you did; the `b8aba22` annotation waits for phase 2.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the deferred material lives in the sibling .deferred.md, held apart under the rule-1 split and opened only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`,
`docs/sessions/` (save the carve-out above), every prior verdict in
`docs/reviews/`, the queue pointer, this brief's sibling
`docs/reviews/2026-10-16-1551-standing-checklist-test-rule-cold.deferred.md`, and
the commissioning items `050`, `020` and `110` in
`docs/roadmap/200-anti-slop-invariant-registry-promote-rec/` (barred as a section).

Sweep with `python3 tools/coldsweep.py --root <your worktree> --also-exclude
docs/roadmap/160-doctrine-review-owed/710-rule-4-cold-pass-queued-checklist-and-test-rule.md
--also-exclude docs/reviews/2026-10-16-1551-standing-checklist-test-rule-cold.deferred.md
--also-exclude docs/roadmap/200-anti-slop-invariant-registry-promote-rec
<pattern>`; `--include-barred` only with disclosure. Reading the delta is never
barred.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list. Then
append your verdict below a `---` divider in THIS file: provenance repeated (how
you were spawned, your tier, what you read), per-lens answers, the standing
checklist V1–V7 each answered or discharged with grounds — running the checklist
under review on its own text is in scope — findings with stable IDs (prefix `CK`:
`CK1`, `CK2`, …) and severities (MAJOR / MODERATE / minor / note), an overall
PASS / PASS-WITH-FINDINGS / FAIL line with counts, a re-run ledger, and a
follow-up checklist. Then STOP and commit phase 1 unrevised before opening the
sibling.

**Phase 2.** Open the sibling; append `### Reconcile` beneath your verdict:
per-finding notes against the seeded questions and the intent record, any finding
formed at reconcile marked as such, and the overall line restated. Never revise
phase-1 text. Then fold the sibling in below the reconcile and delete it.

Findings on self-authored doctrine are the principal's to decide (rule 3): record
all, apply nothing; counsel per finding is welcome, labelled and kept beneath it.
