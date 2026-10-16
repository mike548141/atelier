# Cold pass — one unambiguous review-pointer state, and its two detectors

**Pass type:** doctrine and code cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection by whoever takes this pass; a session that cannot honour it stops.
**Status:** BRIEF ONLY — the review has NOT run. Written 2026-10-16 UTC by an Opus
brief-writer; the pass waits for a further cold Fable session that neither the
delta's author nor this brief-writer (nor its orchestrator) started or
instructed; tier checked at selection (rule 4).
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/690-rule-4-cold-pass-queued-the-pointer-state.md`.
**Why it earns a review:** the queued-review glyph is how every session sizes the
cold-review queue — the obligation rule 4 creates. A legend that admits two
counts, or a detector that misses one shape, lets an owed review go unrun; and
`board.py` and `pointerscan` run in every child's floor, so a change to either
reaches the fleet at its next run.

## Spawn provenance

- **Author of the work under review:** the queue run whose intent record is
  dated 2026-10-05 11:20 UTC (path in the sibling; not opened by this writer).
  Both commits carry a model-unnamed co-author trailer (a dispatched worker, which
  the pointer counts as the run's authorship).
- **Who wrote this brief:** an Opus subagent (`claude-opus-5-5`) dispatched by the
  Mike-opened Opus queue-run session `abe96d8d` on 2026-10-16 UTC, on Mike's
  answer that day that a fresh Opus session writes these briefs. Neither it nor
  its orchestrator authored, started or instructed the authoring run, and
  neither edited the delta. Its orchestrator did add a claim sub-bullet to this
  pass's pointer and to six others, whose state lines are in this delta's
  domain. It is **off-tier for review, disclosed: it forms no finding and writes
  no severity**, and it stopped after this brief and its sibling.
- **Who takes the review:** a further cold Fable session, not yet started, that
  passes rule 4's criterion. It repeats its own provenance in its verdict and, if
  it runs under an orchestrator, discloses that shape as rule 4 requires.
- ⚠️ **Exposure, disclosed** (rule-2 material met before writing). This writer
  read: the queue pointer and six other `160` pointers in full; both commits'
  subjects, `--stat` and message bodies (the author's account, with measurements
  over board history and over other repositories); the diffs of the legend,
  `pointerscan.py` and `board.py`; grep counts of queued-pointer line shapes in
  the generated index at HEAD; `REVIEW.md` down to § *Whether work earns a
  review*; the ask halves of two 2026-10-04 briefs as format models; filename
  listings of `docs/reviews/` and `docs/roadmap/`, and path greps over
  `docs/reviews/` that name prior verdicts without reading them; and its
  auto-loaded cross-session memory index (one-line notes, some on pointer
  grammar and on fleet blast radius). Its orchestrator read the `docs/SESSIONS.md`
  index tail (entries through 2026-10-16, including the authoring runs'
  one-paragraph summaries) and the 2026-10-16 session record's close section, and
  passed this writer nothing evaluative beyond the pointer list. What this writer
  suspects is in the sibling.

## What the work is

Landing commits (diff these; review the paths at HEAD):

- `b02c56d` (2026-10-05 UTC) — board: a review pointer's glyph means
  queued-and-unrun, and the verdict takes it off (130/020)
- `952f78a` (2026-10-05 UTC) — board: a glyph inside a code span is a mention,
  never a lifted flag (130/020); both landed in merge `388ca84`

Delta paths: `docs/roadmap/README.md` (the legend paragraph), `tools/pointerscan.py`
(detector 3, both halves), `tools/test_pointerscan.py`, `tools/board.py`
(`CODE_SPAN_RE` and `index_line`), `tools/test_board.py`, and the state lines
`b02c56d` rewrote — fifteen items under `160-doctrine-review-owed/` and one under
`210-instruments-open-features/`. Later commits by other runs have since touched
`pointerscan.py` (directory walk, allow-marker kinds, finding IDs): review at HEAD
and attribute with `git blame`.

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code,
tests and live behaviour. The lenses organise it; they do not bound it.
Non-goals are the only narrowing and are themselves reviewable.

**The rule.** Read the legend at HEAD as a session sizing the queue would. Count
the queue at HEAD every way the legend's words permit — index lines by shape,
item state lines by marker and flag, `pointerscan`'s `queued_state` — and record
each count with the command that produced it. List every state-line shape a
queued pointer actually wears on the board today, including the claim
sub-bullets added since, and say which the legend names. Check the legend against
`REVIEW.md` rule 4 and lifecycle step 4, and against `method/COMMUNICATION.md` on
the decision mark it borrows.

**The detectors.** Drive `landed_findings` and `unmarked_findings` on crafted
items: a RAN stamp in each case and spacing; a dated stamp with a time suffix; a
cycle outcome in lower case; a further-pass pointer that quotes its predecessor's
RAN stamp; a claim sub-bullet; an item about pointers whose title says
"queued"; a title with a leading eye-flag; an allow-marker. Drive `index_line` on
code spans: doubled backticks, an unbalanced backtick, a glyph inside link text,
a glyph in the title itself. Re-run the commit's history measurement ("768 item
versions … exactly 27") against this repo's own git history.

**Non-goals:** the fleet measurements in the commit messages — the house rules
below forbid pointing a scanner at other repositories, so discharge them with
grounds and judge the design's blast radius from the code instead. Checking each
rewritten state line against its own verdict needs the verdicts, so it is
reconcile-step work (rule 2), done in phase 2.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself first —
   among them, that a glyph count is the right queue measure, that a RAN stamp is
   the reliable mark of a landed verdict, and that a detector can be warn-only on
   a rule whose miss leaves an owed review unrun.
2. **Correctness & quality.** Read the delta and its tests whole; run the crafted
   cases above and record a table (input → detector → expected → actual). Do the
   new tests fail against `b02c56d^` and `952f78a^`? Does `b02c56d`'s rewrite of
   sixteen state lines change only what its message says (diff each)?
3. **Completeness / harvest.** Every other surface that says how to count or
   close the queue: `REVIEW.md`, `CONCURRENCY.md`, the review-brief skill, the
   onramp skill, `tools/README.md`, `ROADMAP.md`'s own header. Do they agree with
   the legend (V3, V5)? Does `board.py`'s marker map treat the queued glyph as a
   marker and as a flag consistently with `pointerscan`?
4. **Security & privacy** — mandatory. Code altitude, against the OWASP
   catalogue: regular-expression cost on long or adversarial item text (both
   new patterns run on every item in every child); any path by which item text
   steers the generator's output beyond its line. Design altitude: a warn-only
   guard on an obligation — can a queued review disappear from every count
   without any check going red? `/security-review`: discharge by grounds (landed
   delta; the pending diff is other passes' drafts) and do this read by hand.

## Re-run obligation

Re-run, do not read. Lift invocations from `.githooks/pre-commit`,
`tools/floor.py` and `.github/workflows/ci.yml` rather than guessing.

- `python3 tools/pointerscan.py --selftest` and `python3 tools/board.py
  --selftest`; `python3 -m unittest tools.test_pointerscan tools.test_board`;
  the full Python suite at most once, foreground
- `python3 tools/pointerscan.py --root <root> .` and `python3 tools/board.py
  --check --root <root>` at HEAD, exit codes and tallies recorded
- the history measurement, in your clone, with the script kept in your scratchpad
- the floor on both planes at HEAD

## House rules for this run

- Name your own worktree in the verdict. Run **no git command that writes** there,
  and never edit a board item or the index — crafted items go in your clone.
  Read-only git is fine.
- One heavy process at a time on a shared machine: the full suite at most once,
  and the history walk as its own step. Never point a scanner at another
  repository on the machine.
- Absolute ISO-8601 dates from `date -u`. Prose wrapped at ≤ 100 columns. NZ
  English. Never quote a secret, placeholder token, email address or personal
  detail — the repo is public; describe and locate instead.
- Review deep, not fast: a finding needs a probe or a re-driven claim behind it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the deferred material lives in the sibling .deferred.md beside this brief under the rule-1 split, opened only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`,
`docs/sessions/`, every prior verdict in `docs/reviews/`, the queue pointer named
above, this brief's sibling (same path, `.deferred.md`), and the commissioning
items under `docs/roadmap/130-a-closed-cycle-can-keep-its-and-pointers/` and
`docs/roadmap/320-child-filed-findings-via-pointing-up/` item 460. The other
`160` items are part of the delta: read their state lines, not their verdicts.

Sweep with rule 2's default bar plus these (`<root>` is your worktree):

```sh
Q=docs/roadmap/160-doctrine-review-owed
python3 tools/coldsweep.py --root <root> \
  --also-exclude $Q/690-rule-4-cold-pass-queued-the-pointer-state.md \
  --also-exclude docs/reviews/2026-10-16-1550-queued-glyph-state-cold.deferred.md \
  --also-exclude docs/roadmap/130-a-closed-cycle-can-keep-its-and-pointers \
  --also-exclude docs/roadmap/320-child-filed-findings-via-pointing-up \
  <pattern>
```

That bars all of section 320, wider than the one item; say so if you read past
it. `--include-barred` only with disclosure in the verdict.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list. Then
append your verdict below a `---` divider in THIS file: provenance repeated (how
you were spawned, your tier, what you read), per-lens answers, findings with
stable IDs (prefix `PO`: `PO1`, `PO2`, …) and severities (MAJOR / MODERATE /
minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL line with counts, a
re-run ledger with commands and results, and a follow-up checklist. Commit it
before opening the sibling. If an orchestrator holds the sibling outside the
tree, it releases it on your committed findings.

**Phase 2.** Open the sibling; append `### Reconcile` beneath your verdict:
per-finding notes against its seeded questions and the intent record, the
state-line-against-verdict check, any finding formed at reconcile marked as such,
and the overall line restated. Never revise phase-1 text. Fold the sibling in
below the reconcile and delete it.

Findings on the legend are doctrine and the principal's to decide (rule 3); the
code findings are recorded the same way here, since the taker is not the author.
Record all, apply nothing; counsel per finding is welcome, labelled as counsel.
