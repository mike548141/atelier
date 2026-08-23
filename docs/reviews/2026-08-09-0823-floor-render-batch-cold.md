# Cold pass — the floor-render batch (third render state + PS5 pathscan promotion + C1F3 floorfleet strip)

**Pass type:** code cold pass (rule-4 queued — the delta applies ruled
decisions, so the applier's judgement produced it).
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04).

## Spawn provenance

- **Author of the work under review:** the session that landed the delta on
  2026-08-06 (see *What the work is*).
- **Who spawned this review:** the principal (Mike), in a session he opened on
  2026-08-09 and pointed at the review queue — rule 4's worked example. His
  words: *"Please do any review work that waiting."*
- **Author's non-involvement:** the taker session authored no part of this
  delta, was neither started nor instructed by the authoring session, and wrote
  this brief as the non-author taker. Rule 4's single criterion is met, and the
  tier was checked at selection.
- **Orchestration shape:** the review runs under an orchestrator holding a
  context partition — the intent-record references are withheld from this brief
  and handed to the reviewer only after its own findings are durably written.

## What the work is

Code landed 2026-08-06, reviewed at HEAD:

1. [`tools/floor.py`](../../tools/floor.py) and
   [`tools/floorfleet.py`](../../tools/floorfleet.py) — a third render state,
   the PS5 pathscan promotion, and the C1F3 floorfleet strip.
2. Their two test files — the suite grew 1178 → 1200 across the batch.
3. [`.github/workflows/ci.yml`](../../.github/workflows/ci.yml) — the bespoke
   pathscan step retired.
4. [`.atelier-floor.json`](../../.atelier-floor.json) — the pathscan scope.
5. The reworded 2026-07-19 line in
   [`docs/decisions/README.md`](../decisions/README.md).
6. The `CHANGELOG.md` entry that landed with them.

## Scope

Widest the work admits: the intent the batch claims to apply, the design of
the render state and the promotion, the code, the tests (a wrong test verifies
nothing), and real behaviour exercised live. **Non-goals:** none narrows the
delta. The reviewer does not decide findings' dispositions; residue joins the
principal's ruling round per house practice.

## The four lenses

1. **Approach & assumptions** — name the load-bearing assumptions yourself
   first. Is a third render state the right mechanism for whatever it renders?
   Does promoting pathscan into the floor change any consumer's contract?
2. **Correctness & quality** — run the suites and the tools live; check the
   CI workflow change against what the floor actually covers now (did retiring
   the bespoke step lose any coverage the floor did not pick up).
3. **Completeness / harvest** — what should the batch have covered and did
   not; does anything duplicate what `floor.py` / `floorfleet.py` already had?
4. **Security & privacy** — mandatory, at code altitude: unsafe input paths,
   shell-out handling, anything the render state prints that it should not.
   atelier is PUBLIC — verify nothing in the delta or your verdict joins a
   private repo's name to its posture. The house security scanner reads
   pending diffs; this is a landed-delta review, so state the reach case that
   applied.

## Re-run obligation

Re-run, do not read, at least: the full test suites (house invocations live in
[`.githooks/pre-commit`](../../.githooks/pre-commit) — lift them, do not
guess), the suite-count claim 1178 → 1200 at the landing commits, the floor
render in all three states where they can be provoked read-only, and pathscan
under the floor scope in `.atelier-floor.json`.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the intent-record refs are orchestrator-held under the rule-1 context partition, handed over only after the reviewer's findings are durably written -->

Rule 2 bars: `docs/ROADMAP-DONE.md`, `docs/sessions/`, and every prior verdict
in `docs/reviews/`. The intent record for this delta (the rulings the batch
applies) is held by the orchestrator and will be provided on receipt of your
committed findings. Reconcile after, never anchor before.

## Process

Append your verdict below a `---` divider in this file: provenance repeated,
per-lens answers, findings with stable IDs (prefix `FR`) and severities
(MAJOR / MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL
line with counts, and a follow-up checklist. Then report; the deferred
references arrive; append a reconcile section and finalise.

---

# Verdict — cold pass on the floor-render batch

**Provenance, repeated.** Reviewer: a cold rule-4 session on the Fable tier,
spawned by this review batch's orchestrator — a Fable session the principal
opened at 2026-08-09 0815 UTC and pointed at the review queue; the reviewer
authored no part of this delta and was neither started nor instructed by the
authoring session. <!-- amended at reconcile: phase 1 misattributed the spawn
to the parallel 0813 queue batch's orchestrator; corrected on the
orchestrator's instruction, own-provenance clause only. -->
The intent-record references were withheld under the
orchestrator's context partition; nothing below this line was written with
them in hand. Rule 2 honoured: no prior verdict, no `docs/ROADMAP-DONE.md`,
no `docs/sessions/`, no `docs/ROADMAP.md` was opened. One disclosure: the
shared review worktree carried an uncommitted modification to a sibling
session's review brief (`2026-08-09-0826-e7-leakscan-build-cold.md`); it was
not opened, and it is the reason the pending-diff security scanner was not
run (see lens 4). A second, incidental exposure: the registry floor's own
secretscan output printed one advisory line naming a reviews-file path with
entropy metadata; no record content was read.

**The delta reviewed.** Commits `be0667e` (C1F3 board strip) and `166fa00`
(third render state + PS5 promotion), landed via merge `7a29430` (which also
carried the reworded 2026-07-19 decisions-index line), reviewed at HEAD
(`5f2e4c7`). Noted: `tools/floor.py` and `tools/test_floor.py` have moved
since the landing under later, separately-ruled commits (`4cab670`,
`c827705` era); those edits are outside this verdict's scope.

## Load-bearing assumptions, named first

1. **The registry is the one source of what runs and how.** Any state the
   board prints must be *derived from the registry entry*, never listed
   beside it, or the list becomes the vendored policy the file exists to end.
2. **A render mark is a cover claim** (EP3's class): identical output for
   materially different cover is the defect, so warn-only wiring may not wear
   the enforcement tick — and the fix may not touch what blocks.
3. **Promotion via `@main` is instant and estate-wide**; its affordability
   rests on warn-only wiring plus the check answering `--selftest`, because
   no child consents per-push.
4. **Board text from repos the operator does not control is hostile input**,
   and one sanitising seam must cover every present and future reader.
5. **The retired CI step's cover is fully reproduced** by registry line +
   `.atelier-floor.json` scope — equivalence is a claim to re-run, not read.

Assumptions 1, 2, 3 and 5 held under attack (evidence below). Assumption 4
holds for the class the ruling named (C0 + DEL) but the *threat* the ruling
answers is wider than that class — FR3.

## Lens 1 — approach & assumptions

The third render state is the right mechanism: derived two ways off the entry
(`--warn` in the plane's argv, `warn_only` where no blocking form exists),
and the two derivations are pinned against the registry's own second
statement of the fact (advisory form == enforced form) in *both* directions —
I verified the pin genuinely bites: a future warn-form wiring that forgot the
flag fails the selftest, and so does a stray `warn_only=True`. Exit-code
semantics are untouched (`Result.failed` keeps warn-only, re-proven live).

Consumer contracts checked: `--json` carries the state in the existing
`state` string, field set unchanged and comparable run to run; `--list` puts
a new word in column 2, and the ci/reusable-workflow selftest loops filter on
`$2!="disabled"` so warn-only checks stay inside the prove-the-instrument
loop (pinned by test, confirmed against both `ci.yml` and
`.github/workflows/floor.yml`). The promotion changes every child's output —
stated plainly in the commit and CHANGELOG as a cost, which is the honest
form. Two design findings: the child default scope for pathscan contradicts
the batch's own records rationale (FR2), and the sanitised class is narrower
than the spoofing threat (FR3).

## Lens 2 — correctness & quality (everything re-run, nothing read)

- **Suite counts at the landing commits**: parent `780fc18` → `Ran 1178
  tests, OK`; `be0667e` → 1184, OK; `166fa00` → 1200, OK; merge `7a29430` →
  1200, OK, with `floor selftest: ok (13 scanners, 0 failure(s))`. The
  1178 → 1200 claim reproduces exactly, and the intermediate commit was green.
- **Suites at HEAD**: Python `Ran 1210 tests … OK` (the +10 are post-landing
  commits); Node `207 pass / 0 fail`. Floor selftest at HEAD: 13 scanners,
  0 failures.
- **Render states, provoked live**: worktree board shows ✅ enforced,
  🟡 partial (leakscan ci cover note), 🟡 enforced + advisory count
  (secretscan, 22), and 👁️ warn-only on exactly harvestscan, pointerscan,
  pathscan — both planes. A scratch fixture provoked ⚠️ advisory with
  `[review by …]`, 🔴 expired with `PASSED, 8 days over`, 🟡 legacy
  migrate-it, ⏭ disabled and ⏭ skipped. `--json` stdout parsed clean with
  the scanners' prose on stderr. Exit codes verified without pipe-masking:
  hook 0, ci 0, advisory/expired fixture 0 (an expired advisory reports, and
  correctly does not block), top-level-array config 1 on `floor.py` (fail
  closed) while the same config renders as one unreadable board row in
  `floorfleet` (the AttributeError fix, exercised live).
- **Pathscan under the floor scope**: registry-driven run clean, 10
  suppressions (`missing-path×10`); the retired step's exact argv re-run
  gives the identical result — the equivalence claim reproduces. The one
  live finding the promotion caught (the 2026-07-19 index line) is fixed at
  the merge and the reworded path
  `docs/build/templates/docs/reviews/README.md` resolves.
- **The board strip, exercised live**: a hostile config carrying ESC/BEL/NUL
  in an advisory `why`, a disabled reason, a local check name and description
  came out of `_read_declarations` with zero control characters; ordinary
  text untouched. `floorfleet` selftest 0 failures.

No overclaim found in the commit messages or CHANGELOG against what the code
does; the one unverifiable figure is FR5.

## Lens 3 — completeness / harvest

- **FR1**: `tools/README.md` documents every registry scanner *except*
  pathscan — the one this batch pushed onto every child.
- The `_days_over` twin (floor/floorfleet) is duplication, but deliberately
  held, its narrowed justification rewritten honestly in this delta, and the
  cross-pin test exists (`test_the_count_reads_the_same_as_the_fleet_board`)
  — acceptable as is.
- stampscan's bespoke `ci.yml` step remains, with stated grounds (ST3 open,
  child-side pin resolution) — a deliberate, recorded non-promotion, not a
  miss of this batch.
- The board's *other* child-authored text surfaces (repo/directory names,
  workflow-derived detail strings) are outside the strip; the merge message
  says this residue is queued as its own item. Verifying that queue entry
  needs `docs/ROADMAP.md`, which rule 2 bars in phase 1 — carried to the
  reconcile step.

## Lens 4 — security & privacy

**Scanner reach case**: this is a landed-delta review, and the only pending
material in the worktree was a sibling session's review brief — exactly the
material REVIEW.md's SL2 caution bars a pending-diff scanner from reading —
so `/security-review` was not run; discharged on those grounds. The
mechanical floor layered under this lens is the registry floor itself,
re-run at HEAD on the ci plane: exit 0, secretscan's 22 advisory findings
all in the known entropy tier.

Code altitude: `_wc` workflow-command encoding unchanged and covering the
new state string; the local-seam symlink and scope-membership guards
re-read and intact; the strip is applied to the parsed document before
every reader, and the shared-function pin (`assertIs`) prevents a second
sanitiser drifting. Findings FR3 (class width) and FR4 (silent key merge)
below. No private repo's name or machine-local term appears in the delta,
and none enters this verdict.

## Findings

- **FR1 · MODERATE (completeness).** pathscan has no entry in
  `tools/README.md`. Every other registry scanner carries a catalogue
  section (harvestscan and pointerscan even state their warn-only exit
  contract there). The promotion lands a new output line on every child's
  hook and CI, and the catalogue a child operator would consult to
  understand it has never heard of the check. One section, same shape as
  its siblings, including its "what it cannot see" residual.
- **FR2 · MODERATE (approach).** The child default scope for pathscan is
  the records tree (`default_scope="docs"`), while this batch's own scope
  rationale — argued twice, in the commit and in `ci.yml`'s comment — is
  that records "name the tree as it stood when written and can never come
  clean without markers that would falsify the record". atelier accordingly
  scoped its own records *out*; children get them *in* by default. On a
  scaffolded child (whose `docs/` holds reviews and session records), the
  promoted check's findings will skew permanently un-actionable, which
  erodes exactly the signal the promotion pays eleven repos' attention to
  buy — and the ruled one-argument flip to blocking would inherit an
  ungateable default estate-wide. The sibling-prose-check analogy is
  weaker than stated: an overlong or misspelled record line can be fixed
  without falsifying the record; a dead path in one cannot. Options for the
  ruling round: a records-excluding default the registry can express, child
  scope declarations before the flip, or accepting the noise deliberately
  on the record.
- **FR3 · MODERATE (security).** `strip_controls` matches the C0 ruling's
  letter (`[\x00-\x1f\x7f]`) but not the threat's width: C1 controls
  (U+0080–U+009F) pass through, and U+009B is a single-character CSI alias
  that xterm-lineage terminals interpret even in UTF-8 mode — a hostile
  `why` of the form `U+009B` + `31m` can still repaint rows on those terminals,
  the exact effect C1F3 closed for `\x1b[`. Bidi overrides (U+202E) also
  survive and can visually reorder a board line on any Unicode terminal.
  Verified by probe against the shipped regex. Severity bounded: the
  attacker is a config author on the operator's own board, and the majority
  of modern emulators ignore C1 — but the board's job is to be believed.
  Recurrence-prevention (the class, not the instance): widen the one seam's
  character class (at minimum `\x80`–`\x9f`; consider the bidi/zero-width
  spoofing set as a named follow-on decision), and add the C1 case beside
  the existing hostile-fixture tests. One seam means one fix covers floor
  and board together.
- **FR4 · minor (security/robustness).** Stripping dict *keys* can merge
  two keys that differ only by control characters — probed live:
  `{"wrap\x07scan": …, "wrapscan": …}` collapses to one entry, the other
  silently dropped. Every affected string is attacker-authored, so the harm
  is self-inflicted, but the design's stated preference elsewhere is loud
  parse errors over silent meaning-changes; a post-strip collision could
  raise `ConfigError` on the floor plane for one line of code.
- **FR5 · note (records honesty).** The CHANGELOG entry says both "eleven
  children get output they did not ask for" and "that repo's row reads
  unreadable, and the other fifteen still render". Eleven children and
  sixteen board rows may both be true under different countings (children
  vs discovered fleet), but the entry does not say so, and estate figures
  have drifted before. Worth one line of reconciliation or a sweep.
- **FR6 · note (render precedence).** In `plan()`, a *local* check absent
  from the current plane renders `skipped` even when the child has also
  declared it `disabled` — the off-plane branch returns before the
  disabled branch. Cosmetic: nothing runs either way, but the board line
  names the weaker of the two true facts.

## Overall

**PASS-WITH-FINDINGS** — 0 MAJOR · 3 MODERATE (FR1, FR2, FR3) · 1 minor
(FR4) · 2 note (FR5, FR6). Every re-run obligation reproduced: the suite
count 1178 → 1200 is exact at the landing commits, the three render states
(and their expiry/legacy/disabled shadings) all provoke correctly with exit
codes intact, the retired pathscan step's cover is byte-equivalent under the
registry, and the board strip does what it claims on the surface it claims.
The three MODERATEs are residue for the principal's ruling round, not blocks:
none falsifies a claim the batch made — FR2 and FR3 are places where the
batch's own stated rationale reaches further than the delta does.

## Follow-up checklist

- [ ] FR1 — write pathscan's `tools/README.md` catalogue section (same
      shape as its siblings; include the warn-only exit contract and the
      records rationale).
- [ ] FR2 — rule the child default scope for pathscan: records-excluding
      default, per-child scope declarations before any blocking flip, or
      accept the noise on the record.
- [ ] FR3 — widen `strip_controls`' class at the one seam (C1 at minimum;
      bidi/zero-width as a named decision) + hostile-fixture tests for the
      new class.
- [ ] FR4 — decide whether a post-strip key collision should raise
      `ConfigError` on the floor plane.
- [ ] FR5 — one-line reconciliation of the eleven-children vs sixteen-row
      figures (or a sweep, per house practice on estate figures).
- [ ] FR6 — optional: let `disabled` win the state column for off-plane
      local checks.
- [ ] Reconcile step (phase 2): read the intent records; verify the
      board-text residue item is genuinely queued in the ROADMAP.

## Reconcile — post-verdict, against the intent record

*Written after the phase-1 verdict above was durably committed. Source: the
orchestrator-held reference — `docs/ROADMAP-DONE.md` § "The floor-render
batch — three states, PS5, and the C1F3 strip (done 2026-08-06)", that
section only; every other record stayed barred. Nothing above this heading
was revised except the provenance clause, amended in place on the
orchestrator's instruction and marked as such.*

### Applied as ruled?

- **Third render state (ruled 2026-08-04)** — applied as ruled, in full. The
  record's shape (derived off the argv or `warn_only`, pinned both
  directions, exit codes untouched, no shared wording with E6b's note, a
  child's `advisory` declaration winning the state column) is exactly what
  the delta ships and what my lens-2 re-runs exercised live. Agreement.
- **PS5 / D1 (ruled FUND THE RESCOPE 2026-08-04, promotion deferred to
  cycle close)** — applied as ruled: bespoke step retired, scope moved to
  `.atelier-floor.json`, `--warn` in the template, flip not smuggled
  (verified), equivalence reproduced by re-run. Agreement — with one
  reframing consequence for FR2 below.
- **C1F3 (ruled STRIP C0 CONTROLS AT PARSE 2026-07-28, "both floor and
  board")** — the board half applied as ruled: C0 + DEL, one seam, the
  floor's own function shared rather than twinned. Agreement on
  faithfulness; FR3's point is about the ruling's class, not the
  application.

### The MODERATEs — priced by the rulings, or new?

- **FR1 (catalogue gap)** — genuinely new. Nothing in the intent record
  mentions `tools/README.md`; the promotion's documentation surface was
  neither ruled on nor priced. Stands as written.
- **FR2 (records-tree default scope)** — reframed, severity unchanged. The
  intent record names "a `docs` default for children" as part of the ruled
  shape, so the applier did not invent the default: the delta applies the
  ruling as ruled, and phase 1's wording ("the batch's own scope rationale")
  should be read as counsel *against a ruled choice*, not as an application
  defect. The record does not engage the tension — the same section carries
  both the records-can-never-come-clean rationale and the records-tree
  default for children, without argument connecting them — so the finding is
  new counsel on a ruled decision, and the decision is the principal's.
- **FR3 (C0-only strip vs the wider spoofing threat)** — genuinely new. The
  ruling's own words scope it to C0; the record prices no wider class. The
  implementation is faithful to the ruling; the residue (C1 controls, bidi
  overrides — probed live in phase 1) needs its own ruling, same seam.

### What the record resolves from my checklist

- The board-text residue I could not verify in phase 1 (ROADMAP barred) is
  confirmed by the record as queued, and named more precisely than my
  lens-3 sketch: `classify`/`_live_yaml` and the caller-`ref` detail line.
  My "repo/directory names, workflow-derived detail strings" is the same
  class; the record's enumeration supersedes mine. Checklist item
  discharged at the strength the record supports — the record *says*
  queued; the ROADMAP entry itself remains unverified by me, per the bar.

### Divergences and residual non-reproductions

- The record's branch-time verification says "ci plane exit 1 byte-identical
  to the fork's pre-existing term findings". My HEAD re-run has ci plane
  exit 0 — not a conflict: the pre-existing findings were resolved after the
  landing (scoped markers, 2026-08-09), and the record describes the branch
  fork, not HEAD. No action.
- One record claim I did not reproduce: "floorfleet `--check` exit 0". The
  brief's re-run table did not name it, and re-running it would read repos
  outside this review's tree; stated rather than silently skipped.
- The record's "same 1 finding, same 10 suppressions" matches my re-run
  (finding since fixed at the merge, 10 suppressions reproduced). Its
  "0.18s" timing claim was not re-measured; nothing rests on it.

### Post-reconcile additions (clearly marked)

- **FR2a · note (post-reconcile addition, rides with FR2).** The intent
  record states the child `docs` default in nine words and carries no
  grounds for it, while carrying full grounds for the atelier scope that
  excludes records. When FR2 reaches the ruling round, the record's own
  asymmetry is the cleanest statement of the gap: the default was ruled,
  but not argued.

No finding's severity changed at reconcile. FR2's framing sharpened
(counsel on a ruled default, not an application defect); FR1 and FR3 are
confirmed new; FR4–FR6 are untouched by the record. The overall line stands:
**PASS-WITH-FINDINGS — 0 MAJOR · 3 MODERATE · 1 minor · 2 note**, plus
post-reconcile note FR2a. Verdict finalised.

## Rulings — 2026-08-23 (structured asks, the live ruling round)

Ruled by Mike through `AskUserQuestion`. The FR2 fork was re-asked in
plain terms after his "I dont understand this" on the first framing —
the re-ask carried the checker's purpose, the history-files wrinkle,
and the three scopes in lay language; he then ruled:

- **FR2** — ruled: records-excluding default for children, matching the
  rationale atelier applied to itself; a child can widen deliberately.
  FR2a's intent-record note rides with the application.
- **FR1, FR3, FR4, FR5, FR6** — ruled: fix as recommended (the missing
  catalogue section; the C1 control-byte widening now with the bidi set
  queued as its own decision; a loud config error on post-strip key
  collisions; the one-line count reconciliation; disabled rendered over
  skipped).

Application follows; tags gain [fixed] as each lands verified.

**Applied 2026-08-23** (wt: ruling-round-0823): FR1–FR6 [fixed] (FR2 as a
records-excluding default built into pathscan; FR3's bidi set queued at
020/350); FR2a discharged in the registry comment. Terminal application of
a 0-MAJOR pass — the item closes without a queued pointer (160/080 [x]).
