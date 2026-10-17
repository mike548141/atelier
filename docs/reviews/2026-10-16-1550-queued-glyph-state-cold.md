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

---

# Verdict — rule-4 cold pass, prefix `PO`, RAN 2026-10-17 UTC

**Overall: PASS-WITH-FINDINGS — 1 MAJOR · 3 MODERATE · 6 minor · 2 note.** The two
detectors do what the delta says, and the commit's history measurement reproduces
exactly. The legend does not: read as it asks to be read, it counts the live queue
three different ways, and the board wears a shape the legend never names — one the
legend's own author wrote eleven minutes after landing it (PO1).

## Provenance, repeated (rule 4; V7)

- **Reviewer:** a fresh `claude-fable-5-1` subagent — Fable, the principal-named
  review tier, checked at selection — spawned on 2026-10-17 by a principal-opened
  `claude-fable-5-1` orchestrator session. Shape, disclosed in the claim sub-bullet
  on the queue pointer and here: reviewer-plus-orchestrator, both seats Fable. The
  orchestrator authored none of the delta and none of the brief, holds the
  `.deferred.md` sibling outside the worktree and the harness scratchpad, forms no
  finding and writes no severity, and commits this file after each phase. Neither
  seat was started or instructed by the authoring run (the 2026-10-05 queue run)
  or by the brief-writer's 2026-10-16 session.
- **Worktree:** `atelier-review-1017` (branch `review-1017`), shared with two other
  reviewers and read-only to this pass except for this file. HEAD moved under the
  pass as the orchestrator landed other passes' verdicts (`181f5d3` at open,
  `46fec06` by the end of phase 1), so every count below names the commit it was
  taken at. Crafted items, old checkouts and the history walk ran in a private
  clone under the session scratchpad, prefix `PO`; no git command that writes ran
  in the worktree.
- **What this pass read:** the brief; the two commits' subjects, `--stat` and their
  code, test and legend diffs (**message bodies not read** — barred until phase 2);
  `docs/roadmap/README.md`, `tools/pointerscan.py` whole, `tools/board.py` to its
  index-plane reader, both test modules through the diffs and their runs;
  `docs/method/REVIEW.md` whole; `CONCURRENCY.md` § *Claiming work* and the rule-4
  synergy paragraph; `COMMUNICATION.md`'s 🎯 lines; `tools/README.md` § pointerscan;
  `tools/floor.py`'s board and pointerscan registry entries; the queue-run skill's
  loop and the review-brief skill's § *Running it*; `RECORD.md` by grep;
  `.wrapscanignore`; the hook and CI floor invocations; the generated index at
  three commits; the state lines of every `160` pointer and the `700` and `580`
  pointers in full as live specimens.
- ⚠️ **Exposure, disclosed.** (1) One early grep over every item file, before this
  pass switched to `coldsweep`, printed the first 200 characters of the state
  lines of two barred items (`130/010`, `320/460`) and of `320/420`; no body was
  read. (2) The `580` pointer, read in full as a live specimen, had acquired its
  own close sub-bullet at `46fec06` while this pass ran: one sentence summarising
  another pass's verdict (its counts and the gist of its MAJOR). That is a prior
  verdict's summary read before phase 1 — not this delta's, and its verdict file
  was not opened. (3) `pointerscan` ran clean at HEAD, so it printed no excerpt of
  the queue pointer. (4) No `--include-barred` sweep ran. (5) The auto-loaded
  cross-session memory index (one-line notes, some on pointer grammar and the
  board) was in context, as the brief-writer disclosed for itself. Nothing from the
  sibling, `docs/SESSIONS.md`, `docs/sessions/`, `docs/ROADMAP-DONE.md`, the `130`
  section, item `320/460` or any file under `docs/reviews/` was read.

## Lens 1 — approach and assumptions (named by this pass first)

- **A1 — a glyph count is the right measure of the queue.** It is, only if the
  glyph has one shape and one position. At `46fec06` it has two positions (bullet
  marker; state prefix after `[ ]`) and the legend's count rule names one. → PO1.
- **A2 — a dated RAN stamp or a stated cycle outcome is the reliable mark of a
  landed verdict.** Grounded on the house's closes: re-driven over 809 item
  versions it fires on exactly the 27 items the delta names and on nothing else.
  It is vocabulary-bound, though: the house's own lower-case "the cycle stays
  open", "RAN on <date>" and "the review ran <date>" all miss (PO5), and a further
  pass quoting its predecessor's stamp fires (PO6). Reliable on the corpus, brittle
  by construction, and advisory — the right posture for that pairing.
- **A3 — a detector may be warn-only on a rule whose miss leaves a review unrun.**
  The delta gives grounds (judgement-adjacent text). What the design does not do is
  put the count anywhere a drop would show: the index prints no queue size, and
  the one silent path — ticking `[x]` on an unrun pointer — is by construction
  outside every detector. → PO3.
- **A4 (unstated) — the legend's reader writes the shape the legend's author
  wrote.** Falsified by the author's own run: `680` (commit `78cc660`, eleven
  minutes after `b02c56d`) and `690` (this pass's own pointer, in the landing
  merge `388ca84`) were both written `- [ ] ⏳`, a shape the legend never names.
- **A5 (unstated) — "eye-flags are never state, the marker alone is" and "a pass
  running under a claim keeps the glyph" are compatible.** They are not: a claimed
  item's marker is `[~]`, so a kept glyph can only live in the prefix, where the
  legend says glyphs are flags. `pointerscan` resolves this one way (prefix is
  state), `board.py` the other (prefix glyph is a lifted flag; `⏳` is in `FLAGS`).
  → PO1, PO2.
- **The non-goals are sound.** Fleet measurement is forbidden by the house rules
  and is judged from the code (PO10); the state-line-against-verdict check needs
  the verdicts and is phase-2 work.

## Lens 2 — correctness and quality

**The queue, counted every way the legend's words permit** (`git grep` against the
named commit, so the moving tree cannot shift it):

| Count | `b02c56d` | `388ca84` (merge) | `46fec06` |
|---|---|---|---|
| index lines `- ⏳` ("the index's `- ⏳` lines") | 12 | 12 | **0** |
| index lines `- [ ] … ⏳` (glyph lifted as a flag) | 2 (both backticked mentions) | 2 (`680`, `690`) | **19** |
| index lines `- [~] ⏳` (a claimed pass) | 0 | 0 | 0 |
| any `⏳` in the index (incl. 2 section headings) | 16 | — | 21 |
| item files with `- ⏳` as marker | 12 | 12 | **0** |
| item files with `- [ ] ⏳ **…**` | 0 | 2 | **19** |
| `pointerscan.queued_state` true | 12 | 14 | **19** |
| `[ ]` items whose title says "queued" with no `⏳` | — | — | 48 (all carry a landed stamp) |

So at `46fec06` a session reading the legend literally counts **0**, a session
reading "on a state line" loosely counts **19**, and `pointerscan` counts **19**
while `board.py` renders all 19 as `[ ]` work with an eye-flag. The two shapes
coexisted from the landing merge onward (`580` was `- ⏳` until its verdict landed
at `46fec06`; the 19 are `680`–`890`, every pointer queued after the legend).

**State-line shapes a queued pointer wears at `46fec06`, and whether the legend
names them:**

| Shape | Items | Named by the legend? |
|---|---|---|
| `- ⏳ **title**` (marker) | 0 (12 at `b02c56d`) | yes — the only one |
| `- [ ] ⏳ **title**` (glyph in the prefix, unclaimed) | 19 | **no** |
| `- [~] ⏳ (claimed …) **title**` (the tests' claimed shape) | 0 | implied ("keeps it"), never written outside `test_pointerscan.py` |
| state line unchanged + an in-body line reading `` `[~]` **CLAIMED 2026-10-17 …** `` | 21 (every briefed pass, added 2026-10-17) | **no** — and not `CONCURRENCY.md`'s claim grammar either (the claim edits the checkbox line) |
| `- [ ] 🛑 **…queued…**` + RAN stamp (landed, MAJOR stands) | 9 | the legend says 🎯 for a ruling owed |
| `- [ ] 🎯 **…queued…**` + RAN stamp (landed) | ~37 | yes |
| `- [ ] **…queued…**` + RAN stamp, no flag (`460`, `510`) | 2 | no — and the delta wrote them |

**Crafted cases, driven through `scan_text` at HEAD** (expected = what the legend
and the docstrings promise; `queued_state` shown for the first item):

| Input | Expected | Actual | `queued_state` |
|---|---|---|---|
| `- ⏳ **…queued…**` + "The pass RAN 2026-09-26" | state | state ✅ | True |
| same, "RAN  2026-09-26" (two spaces) | state | state ✅ | True |
| same, "RAN 2026-09-26-0700" (time suffix) | state | state ✅ | True |
| same, "RAN 2026-09-26T07:00Z" | state | **silent** | True |
| same, "RAN on 2026-09-26" | state | **silent** | True |
| same, "The pass ran 2026-09-26" (lower) | state | state ✅ | True |
| same, "The review ran 2026-09-26" | state | **silent** | True |
| same, "Five … cold passes ran 2026-08-05" | state | state ✅ | True |
| same, "the cycle CLOSES on this pass" | state | state ✅ | True |
| same, "the cycle closes on this pass" | state | **silent** | True |
| same, "the cycle stays open" | state | **silent** | True |
| same, "the cycle is OPEN" | state | **silent** | True |
| further pass: `- ⏳ **…queued: the application…**` quoting "the first pass RAN 2026-09-26 and the cycle stays OPEN" | silent | **state** (false fire) | True |
| further pass with a verdict link and PASS-WITH-FINDINGS only | silent | silent ✅ | True |
| `- [ ] ⏳ **…queued…**`, no stamp (the live 19) | silent | silent ✅ | True |
| `- [ ] ⏳ **…queued…**` + RAN | state | state ✅ | True |
| the `700` shape: `- [ ] ⏳` + in-body backticked `[~]` CLAIMED line | silent | silent ✅ | True |
| `- [~] ⏳ (claimed …) **…queued…**` | silent | silent ✅ | True |
| `- [~] ⏳ (claimed …)` + RAN | state | state ✅ | True |
| `- [~] (claimed …) **…queued…**`, no glyph | silent | silent ✅ | False |
| `- [x] ⏳ **…**` + RAN | silent | silent ✅ | False |
| `- [X] ⏳ **…**` + RAN | silent | silent ✅ | True (never reached: `is_pointer` lowers) |
| `- [ ] 🛑 **Rule-4 cold pass queued: x.**` | state | state ✅ | False |
| `- [ ] 🎯 🔥 **Rule-4 cold pass queued: x.**` | state | state ✅ | False |
| `- [ ] **Rule-4 review queued (tier: …)**` | state | state ✅ | False |
| `- [ ] **Rule-4 cold pass owed on …**` | state | state ✅ | False |
| `- [ ] **Queued: rule-4 cold pass on X.**` | state | **silent** | False |
| `- [ ] **Review (cold) queued on X.**` | state | **silent** | False |
| `- [ ] 🎯 **…queued…**` + "REVIEWED 2026-09-26: PASS-WITH-FINDINGS" (detector 2's own landing vocabulary) | silent | **state** (false fire) | False |
| `- [ ] 🎯 **…queued…**` + "the verdict is below" (`_RESOLVED`) | silent | **state** (false fire) | False |
| `- [ ] 🎯 **…queued…**` + "the cycle closes on this pass" (lower) | silent | **state** (false fire) | False |
| prose item: `- [ ] 🔎 **A review queued at close is lost when the session dies.**` | silent | **state** (false fire) | False |
| prose item: `- [ ] 🔎 **The queued-review glyph on 27 items …**` | silent | silent ✅ | False |
| `- [ ] 🔎 **What a `` `⏳` `` review pointer becomes …**` | silent | silent ✅ | False |
| doubled backticks round the glyph | silent | silent ✅ | False |
| one unbalanced backtick before the glyph, no later tick | silent | silent ✅ | False |
| a warm review's pointer per `REVIEW.md` step 1: `- [ ] **Review queued: the widget design.** Brief: …` | silent | **state** | False |
| allow-marker, unscoped / `:state:` | silent, suppressed 1 | silent, suppressed 1 ✅ | — |
| allow-marker `:grammar:` | state, suppressed 1 | state, suppressed 1 ✅ | — |
| fenced example; ordinary open work | silent | silent ✅ | — |

**`board.index_line` on code spans** (marker `[ ]` unless stated):

| State-line rest | Rendered | Reading |
|---|---|---|
| `🔎 **What a `` `⏳` `` pointer becomes**` | `- [ ] 🔎 [What a pointer becomes]` | mention not lifted ✅ |
| doubled backticks round the glyph | `- [ ] ⏳🔎 […]` | **mention lifted** — the regex pairs the empty spans and leaves the glyph bare (PO9) |
| `🔎 **Fix `` `⏳ handling** 🎯`` ` (one tick, none later) | `- [ ] 🎯⏳🔎 […]` | nothing stripped; glyph lifted (expected) |
| `**The `` `⏳ glyph** is lifted 🎯 — see `board.py` `` ` (odd tick pairs with a later one) | `- [ ] [The glyph]` | **a true 🎯 swallowed** by the mis-paired span (PO9) |
| `**See [the ⏳ queue](roadmap/x.md) now**` | `- [ ] ⏳ [See the queue now]` | link text is not a mention here (PO9, note) |
| `**⏳ Long-running operations need a way back**` (glyph in the title) | `- [ ] ⏳ [Long-running …]` | lifted as a flag, stripped from the title — consistent with FLAGS |
| marker `⏳`, rest also carries `⏳` | `- ⏳ [Rule-4 …]` | `f != marker` holds ✅ |
| `⏳ **Rule-4 cold pass queued: x**` (the live 19) | `- [ ] ⏳ [Rule-4 …]` | the glyph is rendered as a **flag** |
| marker `[~]`, `⏳ (claimed …) **…**` | `- [~] ⏳ (claimed …) [Rule-4 …]` | not a `- ⏳` line |
| `🛑 **Use `` `🎯` `` for a ruling**` | `- [ ] 🛑 [Use for a ruling]` | a backticked 🎯 beside a real 🛑 ✅ |

**Tests against the pre-landing commits** (in the clone: the new test file over the
old tool): `tools.test_pointerscan` at `b02c56d^` — 43 run, **3 fail**, all three in
`QueueStateTest` (landed-still-glyphed, cycle-outcome-alone, queued-without-glyph);
the other seven new cases pass against the old tool because they pin silence.
`tools.test_board` at `952f78a^` — 44 run, **1 fail**, the backticked-glyph case.
Both deltas are therefore tested, and the tests are not vacuous.

**`b02c56d`'s sixteen state-line rewrites, diffed each:** thirteen change the
eye-flag 🛑 → 🎯 and nothing else (`090 260 270 300 320 380 400 450 470 630 650
660` and `210/130`); two drop the flag entirely, 🛑 → none (`460`, `510`), though
both say the principal's rulings walk is still owed — the legend's 🎯 case; one
(`670`, the re-review found as an ordinary open item) becomes `- ⏳` as marker.
Whether that is "only what its message says" is phase-2 work (the message bodies
are barred); the two flag-dropped lines are PO8 regardless.

**Code at HEAD vs the delta** (`git blame`): `_LANDED`, `_TITLE_LEAD`,
`_TITLE_QUEUED`, `queued_state`, `landed_findings` and `unmarked_findings` are
`b02c56d`'s lines unchanged; the `scan_text`/`_item_findings` split is a later
run's allow-kind restructure (`db1aa4d`, `ecdc804`) and preserves the delta's order
(unmarked before the scope test; landed short-circuits cycle). `CODE_SPAN_RE` and
the `bare` line in `index_line` are `952f78a`'s, unchanged.

**The history measurement, re-driven** (clone, HEAD's detectors, every unique
item-file blob in every commit reachable from `b02c56d`, first item per file):
1595 commits; **809** unique item versions (**765** change events — the delta's
"768" is within three of this unit; its method is not recorded, PO12); detector 3a
fires on **exactly 27 distinct items, 44 versions** (four of them — `090`, `260`,
`270`, `300/040` — at five or six versions each, the "earlier versions of four"),
and on no other item; detector 3b fires on **exactly one item, two versions**
(`670`). Re-run to `46fec06`: 1066 versions, the same 27 and the same one, nothing
new — consistent with `pointerscan` clean at HEAD. The claim reproduces.

## Lens 3 — completeness and harvest (V3, V5)

| Surface | Says | Agrees with the legend? |
|---|---|---|
| `REVIEW.md` rule 4 | queue a `⏳` pointer, landing = queuing; the glyph stands on withdrawal | yes |
| `REVIEW.md` lifecycle step 1 | "Add a `[ ]` pointer in the ROADMAP" for a briefed review | **no** — that is the exact shape detector 3b flags (PO4) |
| `REVIEW.md` lifecycle step 4 | "tick the ROADMAP pointer" once decided and consolidated | yes (the legend's `[x]` condition) |
| `CONCURRENCY.md` § Claiming work | a claim edits the item's checkbox line to `[~]` in place | the legend's "keeps it" has no written form under this grammar (PO2) |
| `CONCURRENCY.md` rule-4 synergy | "leaves the `⏳` for a session that did not" | yes, glyph-based |
| `COMMUNICATION.md` | 🎯 — a decision that is the reader's to make | yes; the legend's stamped copy matches (V4) |
| `tools/README.md` § pointerscan | three detectors, the third as the delta describes it | yes (V3 mirror present) |
| `ROADMAP.md` header | points at the legend | yes |
| `RECORD.md` | lists `⏳` among the live state **markers** | marker-form only — silent on the prefix form |
| queue-run skill | "reach a `⏳` review item … leave it" | glyph-based; silent on which position |
| review-brief skill | nothing on the pointer's close state | n/a (RECORD governs) |
| `board.py` | `⏳` is a marker **and** a member of `FLAGS` | treats `[ ] ⏳` as a flag; `pointerscan` treats it as state (PO1) |

V3: the delta's rule reached `tools/README.md` and the tool's own help text; it did
not reach `REVIEW.md` step 1 or `CONCURRENCY.md`'s claim grammar, the two surfaces
that now contradict it. V4: the "has this pass run" fact has two homes inside one
file — `_REVIEWED` (detector 2) and `_LANDED` (detector 3) — with different
vocabularies (PO7). V5: see PO1, PO2, PO4.

## Lens 4 — security and privacy (V6)

- **`/security-review` discharged, with grounds:** it reads this session's pending
  diff, which in this shared worktree is the other reviewers' drafts (the SL2
  class); the delta is landed, so the scanner has nothing of this work to read. The
  read was done by hand against the OWASP catalogue's relevant classes.
- **Code altitude — resource exhaustion (ReDoS):** every new pattern is linear.
  Timed at HEAD: a 400 KB item with one unbalanced emphasis 0.014 s; 50 000 `**`
  tokens under a glyph marker 0.032 s; 100 000 backticks 0.020 s; 100 000
  unbalanced code spans 0.035 s; `index_line` on a 200 KB state line 0.011 s.
  Nothing superlinear; `.+?` and `[^`]*` cannot backtrack catastrophically here.
- **Code altitude — injection / output steering:** item text reaches the generated
  index only through the item's own line (flags, title, claim fragment, copied
  allow-comments — all pre-existing paths; `bare` is used for flags only). No
  path from item text to another item's line, a file path, a shell or an exec.
  The one new steer is the delta's own: a mis-paired backtick on a state line can
  drop a true flag from that line (PO9) — a rendering defect, not a security one.
  Inputs are the repo's own tracked markdown read with `errors="replace"`;
  the file walk is git-enumerated (`filewalk`), so a sibling checkout is not read.
- **Design altitude:** a queued review can leave every count with nothing going
  red — PO3 names the paths. No personal data, secret or credential surface is
  touched; nothing is collected or transmitted.

## Standing checklist

- **V1** — the delta's strongest claims ("exactly 27", "the one re-review and
  nothing else") re-drive true; the legend's claim that the queue "is the count of
  `⏳` state lines — the index's `- ⏳` lines" is stronger than the board bears
  out (PO1). The docstring's "a pointer queuing a further pass has no reason to
  carry [a RAN stamp]" is an assumption, true on the corpus so far (PO6).
- **V2** — every recorded proof in scope re-run: selftests, both test modules, the
  full suite, the floor on both planes, the history measurement (ledger below).
- **V3** — two mirror sites missed (PO4, PO2); `tools/README.md` reached.
- **V4** — two homes for "the pass has run" inside one tool (PO7).
- **V5** — the legend contradicts itself on prefix glyphs (PO1), `REVIEW.md` step 1
  (PO4), and `CONCURRENCY.md`'s claim grammar (PO2).
- **V6** — above; discharged with the hand read.
- **V7** — provenance stated above, repeated from the brief and extended.

## Findings

Doctrine findings (PO1, PO2, PO3, PO4, PO8) are the principal's to decide (rule 3).
The code findings are recorded the same way; nothing is applied. Counsel is
labelled.

**PO1 — MAJOR — The legend admits three counts, and the live board wears the shape
it does not name.** The rule says the queue "is the count of `⏳` state lines — the
index's `- ⏳` lines" and "eye-flags are never state — the marker alone is". At
`46fec06` the index has **0** `- ⏳` lines and **19** `- [ ] ⏳` lines; all 19 are
queued, unrun rule-4 passes. `board.py` lists `⏳` in `FLAGS`, so it renders the
prefix glyph as an eye-flag, which by the legend's own sentence makes those 19
"open work with a flag", not queued reviews; `pointerscan.queued_state` reads the
same prefix as state and counts 19. Three readers, three counts (0, 19, 19-as-flags).
The shape was not a later drift: the delta's author wrote `680` and `690` as
`- [ ] ⏳` within the hour of landing the legend, which is the strongest evidence the
wording did not say what its author meant. This is the miss the brief names — "a
legend that admits two counts … lets an owed review go unrun" — and at `46fec06`
it is three. *Counsel:* pick one position and say it in the legend's count sentence.
The cheapest coherent pick is the marker (`- ⏳`), which `board.py`'s `STATE_RE`,
`RECORD.md`'s marker list and the index's own rendering already assume; then
`pointerscan` should warn on an unclaimed `[ ]` item carrying the glyph in its
prefix (a fourth queue-state miscount, cheap to add beside 3b), and `⏳` should
leave `FLAGS` so the index can never render a queue entry as decoration. If the
prefix form is instead to be lawful, the legend's count sentence and `board.py`'s
marker map must both say so, and "the marker alone is state" must go.

**PO2 — MODERATE — No written claim grammar for a `⏳` item; the only shape that
honours "a pass running under a claim keeps it" lives in a unit test.**
`CONCURRENCY.md` says a claim edits the checkbox line to `[~]` in place; applied to
a `- ⏳` item that replaces the marker and loses the glyph, so the glyph can only
survive in the prefix — the shape `- [~] ⏳ (claimed …)`, written nowhere but
`test_pointerscan.py`. On 2026-10-17 the run that claimed all 21 briefed passes
used a third shape: state line untouched, an in-body line reading `` `[~]`
**CLAIMED …** ``. Under that shape `board.py` surfaces no claim fragment (it only
does so for a `[~]` marker), so "who has this" is invisible in the index for every
live pointer, and under the tests' shape the claimed pass renders as `- [~] ⏳`,
which the legend's literal count (`- ⏳`) excludes — so "keeps it" is not true of
the count either way. *Counsel:* one sentence in the legend naming the claimed
shape, mirrored in `CONCURRENCY.md` § Claiming work beside the `[~]` example, and
a `board.py` selftest line that renders it.

**PO3 — MODERATE — A queued review can disappear from every count with nothing
going red, and no surface prints the count.** Design altitude. `pointerscan` is
warn-only (registry: `warn_only=True`, no blocking form), `harvestscan` is
warn-only, and the index prints no queue size, so a drop is a diff nobody is
asked to read. Three silent paths, probed: (a) edit `- ⏳` to `- [ ] 🎯` with no
stamp — 3b warns only if the title still says "queued"; (b) tick `[x]` on an unrun
pointer — silent by construction (`is_pointer` and 3b both exclude `[x]`), and
indistinguishable from a declined review, which is a legitimate `[x]`; (c) the
PO1 shape — silent to the literal count. The delta's grounds for advisory are
sound for its two detectors; they do not cover the absence of any count surface.
*Counsel:* have `board.py` write one line into the generated preamble — "N reviews
queued" — computed from the marker; then the count is on the session-start read,
a drop is a one-line diff in the commit that caused it, and no scanner has to
block anything.

**PO4 — MODERATE — `REVIEW.md` lifecycle step 1 instructs the exact shape detector
3b flags.** Step 1: "Add a `[ ]` pointer in the ROADMAP." A briefed review's pointer
titled "Review queued: …" with the `[ ]` marker is, to 3b, "a queued review written
as an ordinary open item" (probe row: the warm pointer fires). The legend reserves
`⏳` for rule-4 queues ("for a non-author to take"), so a warm review has no
sanctioned glyph and the detector cannot tell the two apart. V5 between the
lifecycle and the legend; a mirror site the sweep missed (V3). *Counsel:* either
step 1 says `⏳` for any review a non-author will take and `[ ]` only for a review
the author spawns inline (which is then not "queued"), or 3b's title pattern is
narrowed to the rule-4 forms (`Rule-4 … queued`, `cold pass owed`) — the former is
the doctrine fix, the latter the code one; the principal picks.

**PO5 — minor — `_LANDED`'s vocabulary misses the house's own lower-case and
prepositional forms.** Probe rows: "the cycle closes", "the cycle stays open",
"the cycle is OPEN", "RAN on <date>", "the review ran <date>", "RAN <ISO-T>" are
all silent. The lower-case outcome is live house prose (items `460` and `510`
say "the cycle stays open until …", rescued only by their separate `RAN` stamp).
Grounded as the delta grounds `_STEER`: a pattern grows when a real miss shows it
must — this is that showing, in advance of the miss. *Counsel:* `re.I` on the
cycle alternative and an optional `on\s+` before the date.

**PO6 — minor — A further-pass pointer that quotes its predecessor's stamp fires
3a.** The docstring's "a pointer queuing a further pass has no reason to carry" a
RAN stamp is an assumption; the house's application pointers cite "Verdicts
applied: …", and one that writes "the first pass RAN <date> and the cycle stays
OPEN" (the natural sentence) is flagged as landed while genuinely queued. Zero
instances over 1066 historical versions, so this is a shape risk, not a live
defect — recorded so the first instance is not read as the detector working.
*Counsel:* none beyond the allow-marker the tool already offers; note it in the
docstring as the stated residual, as detector 2 does for its own.

**PO7 — minor — "This pass has run" has two homes in one tool, with different
vocabularies (V4).** Detector 2 reads `_REVIEWED` (a verdict link, `REVIEWED
<date>`, `PASS-WITH-FINDINGS`, "the verdict is above/below") and `_RESOLVED`;
detector 3b reads only `_LANDED`. So a `[ ]` item closed in the older vocabulary
("REVIEWED 2026-09-26: PASS-WITH-FINDINGS …", or "taken; the verdict is below")
with a "queued" title fires 3b as unmarked — probe rows above. No live instance
(the 48 title-queued `[ ]` items all carry a `RAN` stamp), but the split means the
two detectors can disagree about one item. *Counsel:* 3b consults `_RESOLVED` and
the `REVIEWED <date>` form as landing evidence too, or the docstring says why not.

**PO8 — minor — The legend's 🎯 rule is applied by neither the delta nor the
closes that followed it.** The legend: `[ ]` "led by 🎯 when what is owed is the
principal's ruling". The delta's own rewrite left `460` and `510` with no flag
while both say the rulings walk is owed; at `46fec06` nine landed pointers whose
MAJOR stands are led by 🛑 (`010/050`, `500`, `530`, `540`, `550`, `580`, `610`,
`620`, `760`), three of them closed on 2026-10-17 under this legend. Eye-flags are
not state, so no count moves — but a rule nobody applies is the class
`PROPAGATION.md` § *When a rule keeps breaking* asks to count, and this is its
evidence. *Counsel:* either the legend admits 🛑 as the "MAJOR stands" lead (the
house's evident practice) and 🎯 for a ruling owed with no MAJOR, or the close
rule in `RECORD.md` names the flag — the legend alone is not where closers look.

**PO9 — minor — `CODE_SPAN_RE` has three edge cases on the state line.** Doubled
backticks round a glyph pair as two empty spans and leave the glyph bare, so the
mention is lifted (`- [ ] ⏳🔎 …`); an odd backtick before a flag that pairs with
a later backtick on the same line swallows the flag (a true 🎯 lost from the
item's own index line); a glyph inside link text is lifted although it is as much
a mention as a backticked one. The first two are the same class the delta fixed
(a mention counted), one layer down; the third is a judgement call. All three are
rendering, line-local, and absent from the live board. *Counsel:* `` (`+)[^`]*?\1 ``
for the span, and strip `LINK_RE` text before lifting flags, if the third is
wanted.

**PO10 — note — Fleet blast radius of `952f78a`, judged from the code.** `board` is
blocking on both planes (`advisory=None`) and children float at `floor.yml@main`,
so any child whose committed index was built before this change and whose state
lines carry a backticked flag glyph goes **red at its next floor run** until it
rebuilds — a parent change that reds a child with no child edit (the class the
house holds for the principal). The remedy is the tool's printed rebuild, one
commit. The delta's message carries the fleet measurement; it is read in phase 2
and reconciled there.

**PO11 — note — Two small legend-file facts.** Line 47 of `docs/roadmap/README.md`
is 106 columns, outside `wrapscan`'s CI path scope (WS1: `docs/method`, `docs/build`,
`docs/decisions` bodies), so no check sees it. The legend's date was written as
`2026-10-06` in `b02c56d` and corrected to `2026-10-05` (the UTC date) in the
landing merge `388ca84` — correct, and the only legend edit since.

**PO12 — minor — The history measurement's method is not recorded.** The docstring
states "768 item versions" and "exactly 27"; the script that produced them is not
in the delta, and the unit is unstated. Re-driven two ways, the item counts
reproduce exactly (27 and 1) and the version count lands within three of one
unit (765 change events) and well off the other (809 unique blobs). A proof that
can only be re-run by guessing its unit is a claim stronger than its evidence
(V1/V2 at the margin). *Counsel:* name the unit in the docstring; the script is
small enough to live beside the selftest or in the session record.

## Re-run ledger

All from the worktree root unless stated; every heavy step under `nice -n 10`, in
the foreground, one at a time. HEAD named per step.

| Step | Command | Result |
|---|---|---|
| floor, CI plane (`46fec06`) | `python3 tools/floor.py --plane ci --root .` | every enforced scanner ✅; `pathscan` 2 warn-only findings (two stale paths in records, unrelated to this delta); exit 0 |
| floor, hook plane (`46fec06`) | `python3 tools/floor.py --plane hook --root . --tools tools` | all ✅ incl. `board` against the staged plane; `pathscan` the same 2; exit 0 |
| board check (`181f5d3`) | `python3 tools/board.py --check --root .` | index current; exit 0 |
| pointerscan (`181f5d3`) | `python3 tools/pointerscan.py --root . .` | clean, 0 suppressed; exit 0 |
| selftests (`46fec06`) | `python3 tools/pointerscan.py --selftest`; `python3 tools/board.py --selftest` | ok (0 failures); board selftest OK; both exit 0 |
| unit modules (`46fec06`) | `python3 -m unittest tools.test_pointerscan tools.test_board` | 87 tests, OK |
| full Python suite, once (`46fec06`) | `python3 -m unittest discover -s tools` | 1916 tests, OK, 862 s under load 18–24; exit 0 |
| `node --test instruments/*.test.js` | not run | not on the brief's list; no instrument is in the delta |
| new tests vs `b02c56d^` (clone) | new `test_pointerscan.py` over the old tool | 43 run, 3 fail (`QueueStateTest`) |
| new tests vs `952f78a^` (clone) | new `test_board.py` over the old tool | 44 run, 1 fail (backticked glyph) |
| history measurement (clone) | `PO-history.py` (scratchpad), every unique item blob reachable from `b02c56d`, then from `46fec06` | 809 / 1066 versions; 3a: 27 items, 44 versions; 3b: 1 item, 2 versions; identical at both ends |
| crafted cases | `PO-probe.py` (scratchpad), tables above | 46 pointer cases, 10 index cases, 6 timings |
| queue counts | `git grep` at `b02c56d`, `388ca84`, `46fec06` | table above |
| `/security-review` | discharged | pending diff is other passes' drafts |
| sweep | `python3 tools/coldsweep.py --root . --also-exclude …` with all four of the brief's exclusions | used for the outcome-vocabulary, claim-line and 🛑-led sweeps; 467 files barred each run; no `--include-barred` |

## Follow-up checklist

- [ ] PO1 — the principal picks the glyph's one position; legend sentence, `FLAGS`,
      and a fourth `pointerscan` state check follow the pick.
- [ ] PO2 — the claimed shape written into the legend and `CONCURRENCY.md`.
- [ ] PO3 — a queue count in the generated preamble (counsel), or a recorded
      decision that the count stays unprinted.
- [ ] PO4 — `REVIEW.md` step 1 reconciled with detector 3b (doctrine or code fix).
- [ ] PO5, PO6, PO7 — `_LANDED` vocabulary, further-pass residual named, 3b consults
      detector 2's landing evidence.
- [ ] PO8 — the 🎯/🛑 lead rule said where closers look, or relaxed.
- [ ] PO9 — `CODE_SPAN_RE` edge cases, if wanted.
- [ ] PO10 — read against the fleet measurement in phase 2.
- [ ] PO12 — the measurement's unit and script recorded.
- [ ] Phase 2: the sixteen rewritten state lines against their verdicts; the
      message bodies against the diff table above; the sibling's seeded questions.
