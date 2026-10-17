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

---

## Verdict — phase 1 (cold pass, prefix `CK`)

**Overall: PASS-WITH-FINDINGS — 0 MAJOR · 3 MODERATE · 7 minor · 4 note.**

### Provenance, repeated

- **Spawn.** A fresh `claude-fable-5-1` subagent, spawned 2026-10-17 UTC by a Fable
  orchestrator that authored neither the delta nor this brief and that holds the
  `.deferred.md` sibling outside this reviewer's reach until phase 1 is committed.
  Rule 4's criterion is met: the delta's author (the 2026-10-05 queue run) neither
  started nor instructed this session. The orchestrator forms no finding and
  writes no severity; the arrangement is disclosed here, in the claim and in the
  pointer, per rule 4's reviewer-plus-orchestrator clause.
- **Tier.** Fable, the principal-named review tier (ruling 2026-08-04), checked at
  selection.
- **Worktree.** `/Users/mike/worktrees/atelier-review-1017`, branch `review-1017`,
  HEAD `7fd2077` (`8acfff1` confirmed an ancestor). No git command that writes was
  run there; the probe clone lives under this session's scratchpad.
- **What was read before the findings.** This brief; the two landing commits'
  subjects, `--stat` and diffs on the three delta paths (message bodies **not**
  read — they stay in the barred set); the merge commit's `CHANGELOG.md` and
  `docs/ROADMAP.md` hunks (diff only); `REVIEW.md`, `EVIDENCE.md` and
  `skills/review-brief/SKILL.md` whole at HEAD; `PRINCIPLES.md` §6;
  `PROPAGATION.md` § *When a rule keeps breaking*, § *One statement, stamped
  copies* and the head of the child doctrine block; `00-APEX.md` § *Honesty is
  absolute*; `docs/build/templates/docs/reviews/README.md` whole and the
  `CONTRIBUTING.md` template's *Review* section; `skills/queue-run/SKILL.md`
  § *Taking a ⏳ review item*; `tools/test_templates.py`'s lens-parity block;
  `tools/coldsweep.py`'s docstring, `tools/floor.py --help`, `.githooks/pre-commit`,
  `.github/workflows/ci.yml`, `.stampscanignore`.
- ⚠️ **Carve-out used, disclosed.** The brief permits the mining record's
  pre-annotation text as the checklist's cited source; this reviewer read
  `git show b910962:docs/sessions/2026-07-22-1036-invariant-candidates.md` in
  full before forming findings. The `b8aba22` annotation was not opened.
- ⚠️ **Filename exposure, disclosed.** Finding-ID existence was checked with
  `grep -l` over `docs/reviews/*.md`: the output is filenames only, no verdict
  content was printed or opened; the `2026-10-16-15*` names were filtered from
  the listing. `git status` showed the 21 deleted `.deferred.md` paths by name.
- **Harness-loaded context, disclosed.** The user-level memory index was in
  context at spawn; one line there notes that finding-prefix collisions are
  unguarded. CK8 below was formed from the grep result, but the reader should
  know the prompt existed.
- **Sweeps.** Every tree search ran through `tools/coldsweep.py` with the three
  `--also-exclude` paths the brief names; no `--include-barred` run. The barred
  set — prior verdicts, `docs/SESSIONS.md`, `docs/sessions/` (save the carve-out),
  `docs/ROADMAP-DONE.md`, the queue pointer, the sibling, and the `200/` items
  `020`, `050`, `110` — stayed closed.

### Floor reproduced first

Both planes at HEAD, under `nice -n 10`, one at a time, foreground:
`floor.py --plane hook` exit 0 and `--plane ci` exit 0 — every enforced check
clean; the two `pathscan` warn-only findings are pre-existing and outside the
delta (a decisions record and the session-open prompt); `secretscan`'s 23 CI-plane
advisories are the standing advisory tier. `stampscan --warn --root . .` clean,
one stamped block verified (the templates `CLAUDE.md` floor). `linkscan --root .
docs/method skills` clean. Tool suite and instrument suite: see the ledger.

### Lens 1 — approach and assumptions

Load-bearing assumptions, named first and then tested:

1. *An always-loaded pointer list changes reviewer behaviour when its homes are
   elsewhere.* Plausible and unmeasured. The record's own headline is that the
   two largest classes are the ones the practice already catches best, so the
   list's value is the reminder, not a new rule. Nothing counts compliance: no
   check reads a verdict for a V1–V7 block, and V7 says so of itself (CK12).
2. *`EVIDENCE.md`, not `REVIEW.md`, is the right single home for the test rule.*
   Holds. The rule is about what a test is evidence *of* (a tier question, §2),
   and `REVIEW.md` already carries the reviewer-side half ("a wrong test verifies
   nothing"); the two are not linked (CK13).
3. *"Mutation-verified means wired, not right" generalises from three instances
   in one child repo.* The letter of the >2 rule is met; the breadth is one
   codebase, two instances on one day, and the mining record itself applied a
   breadth test the text does not mention (CK11).
4. *A belief about an external system is `ai-inference`.* Only when un-sourced —
   §2 says so; §15 drops the condition and then prescribes two primary-tier
   remedies where §13 already holds the ladder (CK1, the top finding).
5. *The checklist's grounding is auditable at the record.* Partly: the counts
   match, every cited ID resolves to a file, but the "full citation list" the
   section promises is not in the pre-annotation record (CK4).

### Lens 2 — correctness and quality

- **Pointers and links.** Every V-line target exists at HEAD and says what the
  line says: V1 → lens 2 ("any overclaim") and `00-APEX.md` ("never emit a claim
  stronger than its evidence"); V2 → § *Re-run every "live-proven" claim*; V3 →
  `PRINCIPLES.md` §6, which does hold the sweep's surface list; V4 →
  `EVIDENCE.md` §9 and `PROPAGATION.md` § *One statement, stamped copies* (both
  anchors resolve); V6 → lens 4; V7 → rule 4 ("the brief states its spawn
  provenance … and the verdict repeats it"). The `../sessions/…` link resolves;
  `linkscan` agrees.
- **The borrowed clause.** "Discharged in one line with grounds, the shape lens 4
  already uses" is faithful: lens 4 reads "discharges in one explicit line with
  grounds". It is widened from one lens to seven lines, and says so.
- **Counts and IDs against the record (pre-annotation).** ~30 / ~9 / ~10 / ~9 /
  ~18 / ~8 / 3 match the record's cluster table and candidate lines; "330
  findings across 47" matches; "recurred more than twice" matches the record's
  `> 2` rule and V7's exact 3. Every cited ID resolves to at least one verdict
  file by `grep -l`. Three qualifications: six IDs carry no pass qualifier and
  two of them match more than one pass (CK8); `conventions-utc F1` matches two
  files, the at-rest and the applied pass — the record distinguishes them and
  the checklist's "(MAJOR)" picks the at-rest one; and the "full citation list"
  is promised, not present (CK4).
- **"Approved by the principal 2026-07-23, item by item."** Not verifiable from
  anything phase 1 may open: the pre-annotation record (committed 2026-07-23
  10:12 UTC) presents V1–V7 as 🎯 candidates awaiting approval; the approval
  must sit in the annotation, the board items or the records, all barred.
  Carried to reconcile, not found against.
- **V5's canonical claim.** Partly overstated (CK7).
- **The skill paragraph.** Compresses without contradicting: V2's "every
  recorded proof" for "every recorded 'live-proven' or 'verified' claim", V6
  without the scanner clause. The header's promise holds. What does not hold is
  that anything watches the copy (CK5).
- **§15's tier word.** Checked against §2: misassigned when the belief is
  sourced (CK1). The `>2 promotion rule` it cites says what §15 says it does —
  `PROPAGATION.md` § *When a rule keeps breaking*: "act at the third instance".
- **§15 against the brief's cases.** An internal pure function: the operative
  rule does not reach it, the heading does (CK10). A vendored library: "your own
  code" is ambiguous — the source is in-tree but not the author's; readable as
  "read the library's source". A stale wire capture: a capture is primary at
  capture time and §10's refresh-on-trigger governs its staleness; §15 is
  silent. A property-based or differential test: a reference implementation
  *is* an outside authority; §15 does not say so. A test pinned to a published
  specification: official-guidance tier under §2; §15 names only source and
  wire (CK1). The text answers one of five.
- **Mechanics.** Both delta sections wrap under 100 columns (the two over-long
  lines in the files are pre-existing: an allow-marker line and the skill's
  front-matter). Dates absolute. NZ English (`spellscan` clean).

### Lens 3 — completeness and harvest

- **Surfaces that tell a reviewer what to run.** `skills/review-brief/SKILL.md`
  carries the checklist. The child floor —
  `docs/build/templates/docs/reviews/README.md`, which compresses scope and lens
  4 to the same altitude — does not; the `CONTRIBUTING.md` template's *Review*
  section points at that README and no further; `skills/queue-run/SKILL.md`
  governs who may take a pass, not what it runs; `commands/` and the plugin
  manifest carry no review-run text. A child reviewer acting on the template
  floor alone never meets V1–V7 (CK2).
- **Surfaces that define test evidence.** `EVIDENCE.md` §14 (an instrument's
  self-report is a claim; drive it through a known failure) and §15 are
  complementary, not duplicated. `REVIEW.md`'s "a wrong test verifies nothing"
  agrees with §15 and does not point at it (CK13). `docs/build/` carries no
  testing guidance that §15 would contradict.
- **Mirrors of the lens roster.** `test_templates.py` pins the lens roster and
  the count words between `REVIEW.md`, the skill and the reviews template; the
  new V-roster has no equivalent pin and sits outside `stampscan`'s one watched
  block (CK5).
- **The records surface.** `CHANGELOG.md` names §15's sign-off as owed; the
  doctrine text does not (CK3).

### Lens 4 — security and privacy

- `/security-review`: **discharged by grounds** — the delta is landed prose,
  markdown is outside that scanner's reach (its clean pass would be
  definitionally empty), and this session's pending diff is other reviewers'
  draft verdicts, which the scanner must never read. Not run.
- Hand read against the OWASP Top 10 / ASVS catalogue: the delta introduces no
  input path, no authentication or authorisation surface, no secret handling, no
  executable; nothing on the catalogue reaches prose. Discharged.
- Privacy at design altitude: §15's grounding parenthetical narrates a private
  child repo's internals — a test's name, a harness output field, a commit hash
  that resolves nowhere public, a hardware detail — beyond what the rule needs.
  A cold sweep finds none of these details anywhere else in the public tree, so
  §15 is their sole public surface. No host, device identity, address or person
  is inferable; the repo's name is already public in both files' bearing
  notes, and a private-repo commit hash has one precedent in `CHANGELOG.md`
  (`806eb10`), so the class is not new (CK9, minor). The checklist's citations
  are finding IDs and dates already public in `docs/reviews/`. The comparison
  against the public board item is deferred: the brief both asks for it (lens
  4) and bars the item (deferred section) — resolved by deferring (CK14).

### The standing checklist, run on the delta itself

- **V1** — bites: the "full citation list" claim (CK4) and §15's tier
  assignment (CK1).
- **V2** — every recorded proof in scope was re-run; see the ledger. None
  failed to reproduce.
- **V3** — bites: the reviews-README template and the CONTRIBUTING template
  were not swept (CK2); the skill copy is unwatched (CK5).
- **V4** — bites: V3's inline surface list beside its pointer (CK6); V5's
  "no other home" (CK7).
- **V5** — bites: §15's status disagrees between `EVIDENCE.md` and
  `CHANGELOG.md`/the board (CK3); §15's heading disagrees with its body's
  scope (CK10).
- **V6** — run; discharged above with grounds; one privacy finding (CK9).
- **V7** — stated in the brief (*Spawn provenance*) and repeated above.
  Discharged.

### Findings

**CK1 — MODERATE.** `EVIDENCE.md` §15 assigns `ai-inference` to every belief
about an external system regardless of how it was obtained ("it is the author's
`ai-inference` about someone else's primary"), where §2 sets a claim's tier by
the weakest source it materially rests on and names `official-guidance` for a
belief read from vendor documentation. It then names two remedies — "read the
library's source, or capture the wire" — both primary-tier, where §13 already
holds the whole ladder and sets the rung by the stakes. The effect: a test
pinned to a published specification, or a differential test against a reference
implementation, has no answer in the text, and a reader climbs to primary on a
throwaway test because the rule says so. The asyncssh instance it cites would
have been caught at the documentation rung.
*Counsel (reviewer's, not a decision):* "treat it as `ai-inference` until
grounded, and ground it on §13's ladder to the rung the stakes set; 'an
authority outside your own code' is any rung above recall that the author did
not write — a specification, the vendor's documentation, the source, a capture,
a reference implementation."

**CK2 — MODERATE.** The checklist binds "every review" and was swept to one
mirror site (the skill) but not the other surface that tells a reviewer what to
run: the child floor at `docs/build/templates/docs/reviews/README.md`, which
compresses scope and lens 4 at the same altitude and now omits the seven lines,
and the `CONTRIBUTING.md` template's *Review* section that points only there.
`PRINCIPLES.md` §6 — V3's own home — names the templates as a sweep surface.
A child reviewer acting on the floor "enough to act on without opening atelier"
never meets V1–V7. This is V3 failing on the commit that minted V3.
*Counsel:* one sentence in the reviews-README template, a pointer not a copy
("run atelier's standing checklist, `REVIEW.md` § *The standing checklist*,
unasked"), and the parity pin of CK5 extended to it.

**CK3 — MODERATE.** §15's status disagrees across surfaces. `EVIDENCE.md`
presents it as settled ("minted at the third, on the principal's ruling of
2026-08-03"); the same merge's `CHANGELOG.md` entry says "his sign-off on its
wording is owed", and the board leaves item `200/020` open as 🎯. `EVIDENCE.md`
§6 — "flag draft, proposed, or in-flight material as such" — is breached on
`EVIDENCE.md`'s own surface, and the rule binds every test written as evidence
across the estate from the moment it landed, with no status line. The ruling
to mint is a non-goal; the wording's status is not.
*Counsel:* whichever the principal rules, one surface is wrong today. Either a
one-line status in §15 until the wording is signed off, or the `CHANGELOG`
line retired when this pass's decisions land.

**CK4 — minor.** The section says "Counts and finding IDs are the record's; its
full citation list for each line lives there." The record at the version this
pass may read lists partial IDs per line ("Occurrences incl.", "e.g.": V1 names
ten of ~30, V5 twelve of ~18) and refers to an appendix that is not in the file.
V1 applied to the line that cites V1. *Reconcile:* the `b8aba22` annotation may
have supplied it — to be checked at phase 2; if it did, this finding closes.
*Counsel:* "its citations for each line live there" — promise what is there.

**CK5 — minor.** The V-roster now has a stamped copy in
`skills/review-brief/SKILL.md` that nothing watches: `stampscan` verifies one
block in the whole tree (the templates `CLAUDE.md` floor — the skill's header is
a prose comment, not a marked block), and `tools/test_templates.py` pins the
lens roster and its count words but not the checklist. This is the SL1 drift
class — a roster landing in the parent while the skill taught the old one —
re-opened on a second roster the day the first roster's pin was celebrated.
Probe (ledger): the lens parser is correctly bounded, so the new section cannot
corrupt the existing pin; it simply has none of its own.
*Counsel:* a `canonical_checklist()` beside `canonical_lenses()`, reading the
`**Vn — …**` bullets of the section, with the skill and (per CK2) the template
asserted to name each.

**CK6 — minor.** V3 points at `PRINCIPLES.md` §6 "which holds the sweep's
surface list" and restates a different list beside it — "child templates,
skills, sibling docs, READMEs" (the record's wording). §6's list is `docs/`,
the plugin surfaces `skills/` and `commands/`, the templates, and children's
inlined floor blocks; it does not name READMEs, and V3 does not name
`commands/` or the child blocks. Two lists, one subject — V4 applied to V3.
*Counsel:* drop the inline list, or make it a pointer-free compression of §6's.

**CK7 — minor.** V5 claims "No other home states this; this line is canonical."
`REVIEW.md` § *What review is not* already names "the sibling docs checked" as
part of a verdict's trail, and `PROPAGATION.md` § *One statement, stamped
copies* holds the copy-must-not-contradict-parent half. Canonical is
defensible; "no other home states this" is not quite true, and a false
uniqueness claim is the thing V4 exists to catch.
*Counsel:* "the fullest statement; § *What review is not* and `PROPAGATION.md`
carry halves of it."

**CK8 — minor.** Six cited IDs carry no pass qualifier (`CF1`, `CF2`, `IR1`,
`SL1`, `SA1`, `SA7`) and rely on prefix uniqueness the corpus does not hold:
by filename-level grep `CF1` occurs in three verdict files and `CF2` in two —
the `CF` prefix is used by both the 2026-07-20 concurrency-flip pass and the
2026-08-17 channel-doctrine pass. `conventions-utc F1` likewise matches two
files (the at-rest and the applied pass). The record disambiguates; the
checklist, which says it does not restate the record, inherits the ambiguity.
*Counsel:* qualify every ID with its pass slug, as `post-method B7` already is.

**CK9 — minor (privacy, minimisation).** §15's grounding parenthetical carries
more of a private child repo than the rule needs: a test's name in quotation
marks, a harness output field and its value, a commit hash of the private repo
(which resolves nowhere public), and a hardware detail (a dual-supply power
test and its rail label). Nothing identifying is inferable and the class has a
public precedent; but the three risk-site bullets already carry the rule, and
the narration is the sole public surface for each of those details (cold
sweep: no hit elsewhere). Deferred half: whether the public board item
publishes the same — phase 2.
*Counsel:* keep the dates and the shape ("a wrong reading of an SSH library's
key-loading default, encoded as the invariant"; "a capture harness on the wrong
hook reporting zero everywhere"), drop the names, the field and the hash.

**CK10 — minor.** The heading — *A test cannot falsify its own code's
assumption* — is universal; the operative rule is scoped to "where the belief
is about an **external** system". Read against the heading, a test of an
internal pure function appears to need "an authority outside your own code"
that cannot exist for it. The brief's case list exposes it; the text does not
resolve it.
*Counsel:* scope the heading ("…its own belief about an external system") or
add one sentence: an internal belief is falsified by the review, not by a
second source.

**CK11 — note.** The >2 promotion is met on the letter — three instances — and
its breadth is one child repo, two of the three on one day. `PROPAGATION.md`'s
rule sets no breadth test, but the mining record that grounds the checklist
applied one ("three findings, all from one review of one codebase in one
session — meets the number, fails the spirit"). §15 sits between those cases.
*Counsel:* say the breadth in the text so a cross-repo instance is looked for
rather than assumed.

**CK12 — note.** The checklist's load-bearing assumption — that an always-loaded
list changes what reviewers do — has no measurement: nothing reads a verdict for
a V1–V7 block, and the delta's own V7 line records that its field is unbuilt.
`PROPAGATION.md`'s rung 2 would be a `reviewscan` warning on a verdict with no
checklist block. A future ruling, recorded here so the count can start.

**CK13 — note.** `REVIEW.md` § *What a review actually checks* says "a wrong
test verifies nothing" and does not point at §15, which is now the doctrine's
account of *how* a test is wrong. One pointer, no copy.

**CK14 — note (on the brief).** Lens 4 asks that §15's details be checked
"against what the public board item already publishes" while the deferred
section bars that item until phase 2. Resolved by deferring the comparison
(CK9's second half); recorded because the brief's framing is itself
reviewable.

### Re-run ledger

| Claim or proof | How re-run | Result |
|---|---|---|
| The floor at HEAD, hook plane | `nice -n 10 python3 tools/floor.py --plane hook --root . --tools tools` | exit 0; all enforced checks clean; pathscan ×2 warn-only, pre-existing, outside the delta |
| The floor at HEAD, CI plane | `… --plane ci --root . --tools tools` | exit 0; secretscan 23 advisory (standing tier); leakscan structural cover only, as CI declares |
| Lens-roster parity (the landing commit's claim, per the brief) | `python3 -m unittest tools.test_templates -v` | 44 tests OK; `canonical_lenses` reads four lenses |
| Probe A — a fifth numbered item under the checklist heading | scratch clone under the session scratchpad, item inserted, `LensRosterParityTest` run | 4 OK — the parser is bounded to § *What a review actually checks* and is not fooled |
| Probe B (control) — the same item inside the lens section | same clone | 2 failures, as designed: the pin fires on a real fifth lens |
| Stamp drift | `python3 tools/stampscan.py --warn --root . .` | clean; one stamped block verified (templates `CLAUDE.md`); the skill's copy is not a marked block (CK5) |
| Internal links on the delta surfaces | `python3 tools/linkscan.py --root . docs/method skills` | clean; the `../sessions/…` link and both `PROPAGATION.md` anchors resolve |
| Every cited finding ID exists | `grep -l` per ID over `docs/reviews/*.md`, filenames only | all 20 resolve; collisions noted (CK8) |
| Counts, corpus size, `>2` rule, V7's "unbuilt field" | pre-annotation record via `git show b910962:…` (carve-out) | match; the "full citation list" does not (CK4) |
| The `>2 promotion rule` says what §15 says | `PROPAGATION.md` § *When a rule keeps breaking* read at HEAD | "act at the third instance" — matches |
| §15's incident details elsewhere in the public tree | `coldsweep` with the brief's excludes | 0 hits; sole public surface (CK9) |
| Private-repo commit hashes already public | `coldsweep` for `ros \`<sha>\`` | one precedent, `CHANGELOG.md` (CK9 downgraded to minor) |
| Full Python tool suite | `nice -n 10 python3 -m unittest discover -s tools -p 'test_*.py'`, once | exit 0 — 1916 tests OK in 732 s; under machine load it overran the harness's 600 s foreground cap and was backgrounded by the harness, not by this reviewer; no other heavy process ran until it finished |
| Instrument suite | `nice -n 10 node --test instruments/*.test.js`, once | exit 0 — 447 pass, 0 fail, 0 skipped |
| `/security-review` | not run | discharged by grounds (lens 4) |

### Follow-up checklist

- [ ] CK1 — §15's tier sentence and its two-remedy clause, against §2 and §13
      (principal's decision).
- [ ] CK2 — the reviews-README and CONTRIBUTING templates owed the checklist
      pointer (principal's decision; the sweep itself is mechanical once ruled).
- [ ] CK3 — one status for §15 across `EVIDENCE.md`, `CHANGELOG.md` and the
      board (principal's decision on which surface is right).
- [ ] CK4 — re-check at phase 2 against the `b8aba22` annotation; close if the
      list exists.
- [ ] CK5 — a checklist-roster parity test beside the lens one (ordinary code
      once ruled; a worker may build it).
- [ ] CK6, CK7, CK8, CK10 — wording (principal's decision; one commit).
- [ ] CK9 — compare against the board item at phase 2; then trim or keep.
- [ ] CK11, CK12, CK13 — recorded for the count; no action this cycle.
- [ ] CK14 — note for the brief-writer template: a lens-4 comparison target
      must not sit in the deferred set.
- [ ] Reconcile at phase 2; overall line restated there.
