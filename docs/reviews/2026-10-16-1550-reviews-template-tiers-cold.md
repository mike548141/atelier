# Cold pass — the child reviews template names tiers and seats, not models

**Pass type:** doctrine cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection by whoever takes this pass; a session that cannot honour it stops.
**Status:** BRIEF ONLY — the review has NOT run. Written 2026-10-16 UTC by an Opus
brief-writer; the pass waits for a further cold Fable session that neither the
delta's author nor this brief-writer (nor its orchestrator) started or
instructed; tier checked at selection (rule 4).
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/590-rule-4-cold-pass-queued-template-tiers-not-models.md`.
**Why it earns a review:** the template is copied into every child repository at
creation and tells the child which seat reviews and which applies; a wrong or
undefined seat there misroutes every child's reviews, and a copied file does not
update itself.

## Spawn provenance

- **Author of the work under review:** the queue run whose intent record is
  dated 2026-10-03 01:44 UTC (path in the sibling; not opened by this writer),
  which landed the commit under *What the work is*. The commit carries an Opus
  co-author trailer.
- **Who wrote this brief:** an Opus subagent (`claude-opus-5-5`) dispatched by the
  Mike-opened Opus queue-run session `abe96d8d` on 2026-10-16 UTC, on Mike's
  answer that day that a fresh Opus session writes these briefs. Neither it nor
  its orchestrator authored, started or instructed the authoring run, and
  neither edited the delta. It is **off-tier for review, disclosed: it forms no
  finding and writes no severity**, and it stopped after this brief and its
  sibling.
- **Who takes the review:** a further cold Fable session, not yet started, that
  passes rule 4's criterion. It repeats its own provenance in its verdict and, if
  it runs under an orchestrator, discloses that shape as rule 4 requires.
- ⚠️ **Exposure, disclosed** (rule-2 material met before writing). This writer
  read: the queue pointer in full; the landing commit's subject, `--stat`,
  message body (the author's own account of why) and diff, and the same for the
  next commit on the same file (160/610's delta); the template file at HEAD in
  full; `REVIEW.md` down to § *Whether work earns a review*; the ask halves,
  above the first divider, of two 2026-10-04 briefs as format models; filename
  listings of `docs/reviews/` and `docs/roadmap/`, and path greps over
  `docs/reviews/` that name prior verdicts without reading them; and its
  auto-loaded cross-session memory index (one-line notes, some on review tiers).
  Its orchestrator read the `docs/SESSIONS.md` index tail (entries through
  2026-10-16, including the authoring runs' one-paragraph summaries) and the
  2026-10-16 session record's close section, and passed this writer nothing
  evaluative beyond the pointer list. What this writer suspects is in the sibling.

## What the work is

Landing commit (diff it; review the path at HEAD):

- `77fc609` (2026-10-03) — templates: the reviews README names tiers, not models
  (200/100 C8)

Delta path: `docs/build/templates/docs/reviews/README.md` — the opening paragraph
of § *Reviews* and the closing paragraph of § *Format*. The next commit on the
file, `ebb358b` (same day, 160/610's delta), changed § *When to write one*; it is
a non-goal here.

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code,
tests and live behaviour. The lenses organise it; they do not bound it.
Non-goals are the only narrowing and are themselves reviewable.

Whether a child session, holding only this file, can tell who reviews, who
applies, and who decides — and whether what it is told is what `REVIEW.md` and
`ECONOMICS.md` say. Read the file at HEAD and diff `77fc609`. List every phrase
that names a seat or a capability ("a more capable model", "the principal-named
review tier", "the builder", "the workhorse seat", "review-tier sessions") and,
for each, find where atelier defines it and whether a child can reach that
definition. Test against cases: a child created from this template before any
tier ruling exists in it; an adopter outside this estate with one model and no
named tier; a child whose principal names the builder's own tier for review; a
child whose review is of its own doctrine (rule 3/4); a child that has the file
but no copy of atelier (the header's "enough to act on without opening atelier").

**Non-goals:** the trigger list in § *When to write one* (160/610's subject);
whether review should be tiered at all (ruled doctrine). Both are read only for
consistency with the delta.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself first.
   The change swaps model names for roles; test whether each role word carries
   the same meaning the model name did, more, or less — and whether the
   surrounding sentence still reads true with the role in it.
2. **Correctness & quality.** Every sentence of the file that says who acts on a
   review, read against `REVIEW.md` § *Why review, and who reviews*, rules 3–4,
   lifecycle step 4, and `ECONOMICS.md` (grep it for the seat words). Does the
   file agree with itself, first paragraph to last (V5)? Do its `<atelier-path>`
   pointers resolve to the anchors named?
3. **Completeness / harvest.** Every other surface stamped into children or
   shipped to adopters that still names a model where a role is meant: grep
   `docs/build/templates/`, `skills/`, `commands/` and `README.md` for model
   names. How does a change to this template reach children already created —
   `stampscan`, the create-repo skill, `CHANGELOG.md`, a template version? Is
   anything owed so existing children notice (V3)?
4. **Security & privacy** — mandatory. Design altitude: can the new wording route
   a review of security-relevant work to a seat the doctrine does not intend, or
   let the author's own seat review and apply its own doctrine? Code altitude:
   none (prose). `/security-review` is discharged by grounds — a landed prose
   delta; the session's pending diff is other passes' drafts — say so.

## Re-run obligation

Re-run, do not read. Lift invocations from `.githooks/pre-commit`,
`tools/floor.py` and `.github/workflows/ci.yml` rather than guessing.

- the floor on both planes at HEAD (`python3 tools/floor.py --plane hook --root
  <root> --tools <root>/tools`, then `--plane ci --root <root>`), exit codes read
  explicitly
- `python3 tools/stampscan.py --warn --root . .` and `python3 tools/blockscan.py
  --check --warn --root .` — the template carries a stamp header
- the model-name grep in lens 3, with counts recorded per surface

## House rules for this run

- Name your own worktree in the verdict. Run **no git command that writes** there;
  read-only git (`log`, `show`, `diff`, `blame`) is fine. Probes, scratch
  children and checkouts of older commits go in a private clone under your
  scratchpad, named by your prefix.
- One heavy process at a time on a shared machine: the full Python suite at most
  once, foreground. Never point a scanner at another repository on the machine.
- `/security-review` reads the session's pending diff. Discharge it by grounds for
  this landed delta and do the code-altitude read by hand against the OWASP
  catalogue, or keep the tree clean whenever you spawn it.
- Absolute ISO-8601 dates from `date -u`. Prose wrapped at ≤ 100 columns. NZ
  English. Never quote a secret, placeholder token, email address or personal
  detail — the repo is public; describe and locate instead.
- Review deep, not fast: a finding needs a probe or a re-driven claim behind it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the deferred material lives in the sibling .deferred.md beside this brief under the rule-1 split, opened only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`,
`docs/sessions/`, every prior verdict in `docs/reviews/`, the queue pointer named
above, this brief's sibling (same path, `.deferred.md`), and the commissioning
item `100-r2-found-eleven-live-contradictions.md` with every other item under
`docs/roadmap/200-anti-slop-invariant-registry-promote-rec/`.

Sweep with rule 2's default bar plus these (`<root>` is your worktree):

```sh
Q=docs/roadmap/160-doctrine-review-owed
python3 tools/coldsweep.py --root <root> \
  --also-exclude $Q/590-rule-4-cold-pass-queued-template-tiers-not-models.md \
  --also-exclude docs/reviews/2026-10-16-1550-reviews-template-tiers-cold.deferred.md \
  --also-exclude docs/roadmap/200-anti-slop-invariant-registry-promote-rec \
  <pattern>
```

`--include-barred` only with disclosure in the verdict. The delta and the doctrine
it must agree with are never barred.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list. Then
append your verdict below a `---` divider in THIS file: provenance repeated (how
you were spawned, your tier, what you read), per-lens answers, findings with
stable IDs (prefix `TT`: `TT1`, `TT2`, …) and severities (MAJOR / MODERATE /
minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL line with counts, a
re-run ledger with commands and results, and a follow-up checklist. Commit it
before opening the sibling. If an orchestrator holds the sibling outside the
tree, it releases it on your committed findings.

**Phase 2.** Open the sibling; append `### Reconcile` beneath your verdict:
per-finding notes against its seeded questions and the intent record, any finding
formed at reconcile marked as such, and the overall line restated. Never revise
phase-1 text. Fold the sibling in below the reconcile and delete it.

Findings on doctrine are the principal's to decide (rule 3): record all, apply
nothing; counsel per finding is welcome, labelled as counsel.

---

# Verdict — phase 1 (2026-10-17 UTC)

## Provenance, repeated

- **Reviewer:** a fresh `claude-fable-5-1` subagent — the principal-named review
  tier (rule 4, ruling 2026-08-04), checked at selection. Spawned 2026-10-17 UTC by
  a Fable orchestrator that authored neither the delta nor this brief, holds the
  `.deferred.md` sibling outside this tree until these findings are committed, and
  forms no finding and writes no severity (rule 4's reviewer-plus-orchestrator
  shape, disclosed here before the findings). The authoring run (2026-10-03) and
  the Opus brief-writer (2026-10-16) started and instructed neither of us.
- **Worktree:** `/Users/mike/worktrees/atelier-review-1017`, branch `review-1017`,
  HEAD `e3346c5` (carries `8acfff1`). No git write of any kind; this brief file is
  the only file edited. The 11 `.deferred.md` deletions in `git status` are the
  orchestrator's context partition, untouched.
- **What I read:** the delta file at HEAD in full and its `77fc609` diff; `ebb358b`
  for consistency only; `REVIEW.md` in full; `ECONOMICS.md` § the billing states,
  the standing default, § *One doctrine, tiered authority* and § *The
  orchestrated-run tier split*; the child templates `docs/ECONOMICS.md` and
  `CLAUDE.md` (grep); `skills/create-repo/SKILL.md` (grep for the stamp steps);
  `tools/test_templates.py` § `ReviewsTemplateTest`; `tools/stampscan.py`'s marker
  grammar and `.stampscanignore`; `tools/pins.py` (grep); `PROPAGATION.md` (grep
  for how a template change reaches children); `.githooks/pre-commit`, `ci.yml`
  and `tools/floor.py`'s usage. Nothing barred was opened: no prior verdict, no
  session record, no `ROADMAP-DONE.md`, not the queue pointer, not the sibling,
  not the 200/ items.
- ⚠️ **Exposure, disclosed.** The rule-2 sweep for the seat coinages printed one
  line each from ~20 other `160/` queue pointers (their tier boilerplate, not
  evaluative text) and one `CHANGELOG.md` line; the CI-plane floor printed a
  2026-08-09 brief's *filename* in a secretscan advisory. My auto-loaded
  cross-session memory index carries one-line notes, some on review tiers. No
  `--include-barred` sweep was run.
- **Machine load.** Load averages ran 43 → 172 during this pass from other
  sessions' test runs. On the orchestrator's instruction, no test suite was run
  (neither `unittest discover` nor `node --test`; the brief's re-run list names
  neither), and every scanner ran alone, in the foreground, under `nice -n 10`.

## Load-bearing assumptions, named first (lens 1)

1. **A role word carries the model name's meaning for every child.** It does not.
   The delta swaps "Fable" for "the principal-named review tier" and "Opus" for
   "the builder" / "the workhorse seat". The model names were wrong in a stale
   way; the role words are undefined in a different way — defined nowhere a child
   holding only this file can reach (TT3), while the sentence around them keeps a
   precondition the parent explicitly rejects (TT1).
2. **"The workhorse seat" is "the builder".** Only on the common path. The parent
   says "apply fixes back on the building model" and escalates doctrine-text and
   first-of-kind builds to the capable tier; the file's two paragraphs name two
   different appliers (TT2).
3. **The header's promise holds after the delta.** "Narrowing-free: may compress
   the parent, never contradict it" — TT1 is a contradiction a one-model adopter
   meets in the first sentence; TT4 is a compression that drops the half of the
   rule with the widest blast radius.
4. **The commit's own account is accurate.** Partly: the header does not promise
   "nothing that can go stale" (no such sentence exists in it); the delta "notes
   that findings on self-authored doctrine are the principal's" — true, and half of
   the rule-3/4 pair (TT6).

## Per-lens answers

**Lens 1 — approach & assumptions.** The approach is right: a copied file must not
carry a model name that a plan change or a model generation retires, and the
parent (`ECONOMICS.md`: "no seat is reserved for the top model by its name") is
the authority the delta cites. The execution is a rename, not a re-read of the
sentences the names sat in. Test cases from the brief: *(a) a child created before
any tier ruling* — the file names a "principal-named" tier but says neither where
the naming lives (the child's own `docs/ECONOMICS.md` says seat→model is
person-local) nor what to do when none exists; *(b) an adopter with one model* —
reads "a more capable model … reviews" as a practice it cannot run, while the
parent says the same model in a fresh session delivers most of the value; *(c) a
principal who names the builder's own tier* — "a more capable model (the
principal-named review tier)" is then self-contradictory in one clause; *(d) a
child reviewing its own doctrine* — told the decision is the principal's, not told
the spawn must be a non-author's (TT4), and told at the end to apply fixes on the
workhorse seat (TT2); *(e) a child with no atelier copy* — every pointer is to
atelier; the floor's own words cannot be resolved locally (TT3).

**Lens 2 — correctness & quality.** Each sentence that names who acts, read
against the parent:
- "a **more capable model** (…) reviews" — `REVIEW.md` § *Why review*: capability
  "is the multiplier on top, not the precondition"; independence is the core
  "even when the reviewer is the same model in a new session". Contradiction
  (TT1).
- "(the principal-named review tier)" — matches `ECONOMICS.md`'s standing default
  ("the named tier for review") and rule 4's "the tier the principal names". The
  concept is right; the term is a coinage (TT3).
- "The builder then applies the findings on ordinary code" — matches lifecycle
  step 4 and `ECONOMICS.md` line 35 ("apply fixes back on the building model").
- "findings on self-authored doctrine are the principal's to decide (`REVIEW.md`
  rule 3)" — correct, and the rule number resolves. The citation is the file's
  only bare `REVIEW.md` without `<atelier-path>`; the child template set ships no
  `REVIEW.md` of its own, so the reader resolves it only through the next
  sentence's pointer (style, folded into TT3).
- "apply fixes back on the workhorse seat" — narrower than the parent's "building
  model", and carries no doctrine caveat (TT2).
- V5 within the file: paragraph 1 and the closing paragraph disagree on the
  applier (TT2); the reviewer is named three ways in 80 lines (TT3).
- Pointers: `<atelier-path>/docs/method/REVIEW.md` and `…/ECONOMICS.md` exist;
  "atelier ADR 2026-07-15" is `docs/decisions/2026-07-15-1327-timestamps-utc-at-rest.md`;
  `CONCURRENCY.md`'s record-identifier rule is at its line 214; `reviewscan`
  exists and keys on the vocabulary the file names. All resolve.
- No line exceeds 100 columns; the file is wrapscan-clean on both planes.

**Lens 3 — completeness / harvest.** Model-name grep over the child-facing
surfaces, counts per surface: `docs/build/templates/` 0 · `skills/` 0 ·
`commands/` 0 · `README.md` 0 (case-insensitive, co-author trailers excluded;
confirmed by the rule-2 `coldsweep` run, which lists none of those paths). The
remaining model names under `docs/method/` (APEX 1, CONCURRENCY 1, ECONOMICS 2,
GLOSSARY 1, REVIEW 3) are the "currently Fable" grounding sites the parent keeps
deliberately. Harvest of the delta's own class is complete. Reaching children
already created is not: the file is a *marked* pointer, not a stampscan-stamped
block — the tree's only `stamp:begin` is the `CLAUDE.md` template (stampscan:
"1 stamped block verified") — so `stampscan` in a child never compares this
file; `pins.py` reads pins, not template content; `CHANGELOG.md` carries no entry
for `77fc609` (0 matches); the `create-repo` skill copies the template at
creation only. The sole channel to an existing child is `PROPAGATION.md`'s
pin-bump `git log` read of the commit subject, then a hand re-copy. Whether any
child still carries "Fable"/"Opus" was not checked — other repositories are out
of this pass's bounds (TT5). Nothing mechanical pins "no model name in the
template set"; `ReviewsTemplateTest` pins the header, the trigger, the prose
clause and the placeholder only (TT6, counsel).

**Lens 4 — security & privacy.** *Design altitude.* The wording cannot route a
security-relevant review to an unintended seat: the reviewer is the named tier
and "security & privacy is a must on every review" is retained verbatim. It can
let the author's own seat apply its own doctrine: the closing line sends every
fix to the workhorse seat with no doctrine carve-out, so a child whose workhorse
drafted doctrine text (which the parent says to escalate, but a child may not)
is told to apply the fixes to it itself — the principal's decision stands in
paragraph 1, the application in paragraph 3 does not honour it (TT2). *Code
altitude:* none — prose only; no input path, no secret, no credential, nothing
in the OWASP Top 10 / ASVS catalogue has a surface here. `/security-review`
**discharged by grounds**: the delta landed on 2026-10-03, so the scanner has
no pending diff of the work to read; this session's pending diff is other
reviewers' drafts, which rule 1's SL2 caution forbids aiming it at; and the
scanner excludes markdown, so its clean pass would be definitionally empty.
Privacy: the file names no person, host, address or secret; nothing enters a
public tree that was not there.

## Standing checklist V1–V7

- **V1** — one overclaim found, in the commit message not the file (TT6).
- **V2** — no "live-proven" claim in the delta; the floor it must pass was re-run
  (ledger below) and passes.
- **V3** — swept: the model-name class is clear of every mirror site; the
  change's route to existing children is the gap (TT5).
- **V4** — the child's seat vocabulary has a home (`docs/ECONOMICS.md` template:
  *Workhorse seat*, *Capable seat*); the delta coined a second set instead of
  using it (TT3).
- **V5** — internal contradiction between paragraphs 1 and 3 on the applier
  (TT2); contradiction with the parent on the precondition (TT1).
- **V6** — run, discharged by grounds above.
- **V7** — provenance stated in the brief and repeated above.

## Findings

**TT1 — MODERATE.** *The floor keeps "a more capable model" as the subject of the
house practice; the parent makes capability a multiplier, not a precondition.*
`REVIEW.md` § *Why review*: "independence, different blind spots, and fresh
context deliver most of the value even when the reviewer is the same model in a
new session. Capability is the multiplier on top, not the precondition." The
template's first sentence tells a one-model adopter the practice is something it
cannot do, and tells a child whose principal names the builder's own tier that the
reviewer is both "more capable" and that same tier. The header forbids exactly
this ("may compress the parent, never contradict it"). The words predate the
delta, but the delta rewrote this sentence and left the precondition standing
while removing the one thing — a model name — that made it concrete. *Counsel:*
lead with independence — "an independent session (the tier the principal names,
where one is named; a more capable tier where one exists) reviews…" — so the
sentence is true for every adopter the parent admits.

**TT2 — MODERATE.** *Two appliers in one file, and the closing one can be the
author's own seat.* Paragraph 1: "The builder then applies the findings on
ordinary code; findings on self-authored doctrine are the principal's to decide."
Closing paragraph: "apply fixes back on the workhorse seat." The parent's words
are "apply fixes back on the building model" (`ECONOMICS.md`), and the building
model is the capable tier for doctrine-text and first-of-kind items (§ *The
orchestrated-run tier split*); applying decided doctrine findings "is itself a
doctrine edit" with "an applier that authored neither the doctrine nor the
verdicts" preferred (`REVIEW.md` § *Applying decisions to doctrine*). So the
closing line (i) names a narrower party than the parent, (ii) carries none of
paragraph 1's doctrine carve-out, and (iii) in a child whose workhorse drafted the
doctrine, routes the application to the author's own seat — the lens-4 design
question the brief asked, answered yes. V5 within the file. *Counsel:* make the
closing line agree with paragraph 1 — "apply fixes back on the seat that built
the work; decided doctrine findings go to a hand that wrote neither the doctrine
nor the verdict" — or drop the closing clause and let paragraph 1 carry it.

**TT3 — minor.** *The reviewer is named three ways here and a fourth way in the
child's own `ECONOMICS.md`; the lead term is defined nowhere a child can reach.*
This file: "a more capable model", "the principal-named review tier",
"review-tier sessions". The child `docs/ECONOMICS.md` template, which this file
cross-references and which cross-references this file back: "Capable seat — the
orchestrator, reviewer and hard-problem solver … apply fixes back on the
workhorse (see `reviews/README.md`)". The applier likewise: "the builder" and
"the workhorse seat" here, "Workhorse seat" there, "building model" in the
parent. "Principal-named review tier" occurs in no doctrine file (`docs/method/`:
0 hits); it is atelier's *board* vocabulary — ~20 queue pointers under `160/` and
one `CHANGELOG.md` line — which a child never sees. A child created before any
tier ruling, or an adopter outside this estate, meets a term with no referent, is
not told the naming is person-local (its own `ECONOMICS.md` says so) and is not
told what to do when none exists (the parent's answer, for rule-4 passes: stop).
The one bare "`REVIEW.md` rule 3" citation, without `<atelier-path>`, is the same
reachability gap in miniature — the child template set ships no `REVIEW.md`.
V4: one fact, one home. *Counsel:* use the child's own seat names — "the capable
seat (the tier the principal names for review) reviews … apply fixes back on the
workhorse seat (`docs/ECONOMICS.md`)" — and say in one clause where the naming
lives.

**TT4 — minor.** *The rule-3 clause compresses out the two halves that make it
bite.* Rule 3 defines doctrine "by function, not file type" — a validator, a CI
gate, a template or skill that stamps behaviour counts, and "encoding a policy as
code does not keep the escape" — and rule 4 says self-authored doctrine "earns a
cold *spawn*": a review from a session the author neither started nor
instructed. The floor now says the *decision* is the principal's and nothing
about the *spawn*, so a child session holding only this file can warm-spawn the
review of its own doctrine on the named tier, apply nothing, forward the
findings, and read the floor as satisfied — and can read "doctrine" as prose
only. Compression is allowed; silently dropping the spawn test for the category
the parent calls "the widest blast radius in the operating model" is the
narrowing the header warns against. The brief's case *a child whose review is of
its own doctrine (rule 3/4)* is answered half-way. *Counsel:* one clause —
"self-authored doctrine (by function: any rule that governs future agent
behaviour, in prose or code) is reviewed from a session its author neither
started nor instructed, and its findings are the principal's (rules 3–4)".

**TT5 — minor.** *No route from this change to a child already created, and
nothing reports which children still carry the model names.* Verified: the
template carries no `stamp:begin source=` marker, so `stampscan` never compares
it (the tree's one stamped block is the `CLAUDE.md` template); `pins.py` reports
pin distance, not template content; `CHANGELOG.md` has no entry for `77fc609`;
`create-repo` copies at creation. The only channel is the child's pin-bump
`git log` read meeting the commit subject, then a hand re-copy — and the fleet's
children were scaffolded before 2026-10-03. V3 asks whether anything is owed so
existing children notice: a changelog line at minimum; a sweep of the children
for the retired sentence is the real close, and it belongs to a session that may
touch those repositories (this pass may not, and did not). The file's "STAMPED
POINTER" header and `ReviewsTemplateTest`'s "the stamped pointer" docstring
both say *stamped* for a file the stamp scanner does not watch — a claim one
notch stronger than the mechanism.

**TT6 — note.** *The commit message overclaims the header, and the fix has no
mechanical floor.* "Its own header promises it carries nothing that can go stale"
— the header promises a thin floor plus a pointer and "narrowing-free"; no
sentence about staleness exists in it (grep: 0). Harmless to the delta, but V1
is the largest finding class on record and a commit body is the author's
account future readers trust. Separately: nothing pins the delta's class.
`ReviewsTemplateTest` asserts the header, the trigger, the prose clause and the
placeholder; a one-line assertion that no file under `docs/build/templates/`
names a model (co-author trailers aside) would catch the next C8 at commit time
instead of at a cold pass. *Counsel:* add it to `tools/test_templates.py`'s
whole-set inventory.

**Overall: PASS-WITH-FINDINGS — 0 MAJOR · 2 MODERATE · 3 minor · 1 note.**
The delta does what its subject says — no model name remains on any child-facing
surface, and the rule-3 clause it adds is correct — but it renamed within
sentences it did not re-read, leaving a precondition the parent rejects (TT1)
and two appliers in one file (TT2). No MAJOR: every defect is resolvable by a
child that follows the pointer up, and the pointer is intact.

## Re-run ledger

All from `/Users/mike/worktrees/atelier-review-1017` at `e3346c5`, each alone,
foreground, `nice -n 10`, exit codes read explicitly.

- **floor, hook plane** — `python3 tools/floor.py --plane hook --root <wt> --tools
  <wt>/tools`: exit 0; 12 ✅, 4 👁️; pathscan 2 warn-only findings, both
  pre-existing and outside the delta's file.
- **floor, ci plane** — `python3 tools/floor.py --plane ci --root <wt> --tools
  <wt>/tools`: exit 0; secretscan 23 🟡 advisory (entropy, none in the delta's
  file); leakscan 🟡 declared-partial as designed; pathscan the same 2.
- **stampscan** — `python3 tools/stampscan.py --warn --root <wt> <wt>`: exit 0; 1
  stamped block verified (`templates/CLAUDE.md`, identical); the reviews template
  is not a stamped block.
- **blockscan** — `python3 tools/blockscan.py --check --warn --root <wt>`: exit 0;
  clean; 55 unmapped headings advisory, none in the delta.
- **model-name grep** — case-insensitive `fable|opus|sonnet|haiku` over the four
  lens-3 surfaces, co-author trailers excluded: templates 0 · skills 0 ·
  commands 0 · README 0.
- **coldsweep, models** — `python3 tools/coldsweep.py --root <wt>` with the
  brief's three `--also-exclude`s, pattern `\b(Fable|Opus|Sonnet|Haiku)\b`:
  exit 0; 0 hits on the four surfaces; `docs/method/` sites APEX 1, CONCURRENCY 1,
  ECONOMICS 2, GLOSSARY 1, REVIEW 3.
- **coldsweep, coinages** — same exclusions, pattern `principal-named|workhorse
  seat|review-tier session|Capable seat`: exit 0; doctrine files 0; this template
  3; child ECONOMICS template 1; board pointers ~20; CHANGELOG 1.
- **width** — `awk 'length > 100'` over the delta file: 0 lines.
- **datescan / spellscan on this verdict** — single-file runs: both exit 0.
- **not run** — `python3 -m unittest discover -s tools` and `node --test
  instruments/*.test.js`: the orchestrator's instruction under load 43–172, and
  neither is in the brief's re-run list.

## Follow-up checklist

- [ ] TT1 — principal's decision: re-lead the first sentence on independence.
- [ ] TT2 — principal's decision: one applier, with the doctrine carve-out, in
      the closing paragraph.
- [ ] TT3 — principal's decision: adopt the child `ECONOMICS.md` seat names in
      this file; say where the tier naming lives.
- [ ] TT4 — principal's decision: add rule 4's spawn test and rule 3's
      by-function definition to the floor in one clause.
- [ ] TT5 — a `CHANGELOG.md` line for `77fc609`; a child sweep for the retired
      "Fable"/"Opus" sentence, from a session allowed to touch those repos;
      decide whether "stamped" is the right word for an unstamped pointer.
- [ ] TT6 — a template-set assertion that no model is named (`test_templates.py`).
- [ ] Phase 2: reconcile against the sibling once released.
