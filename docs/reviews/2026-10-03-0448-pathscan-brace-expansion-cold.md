# Cold pass — pathscan's brace expansion and inline `./` skip

**Pass type:** code cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection: this pass's reviewer and orchestrator are both `claude-fable-5-1`.
**Status:** BRIEF WRITTEN 2026-10-03 0448 UTC; the review runs under the
orchestration below, by a reviewer that is not the brief-writer.
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/490-rule-4-cold-pass-queued-pathscan-brace-expansion.md`.
**Why it earns a review:** pathscan is the guard that says a path a doctrine
file cites still exists. A change to what it counts as a path reference decides
both what it stops flagging and what it can no longer see; a wrong skip is a
stale reference that reads as clean.

## Spawn provenance

- **Author of the work under review:** the 2026-10-03 queue run (an Opus
  orchestrator with dispatched workers) that landed the commits named under
  *What the work is*. This brief-writer was not that session, was neither
  started nor instructed by it, and has edited none of the delta's paths.
- **Who wrote this brief:** an atelier session Mike opened on 2026-10-03 with
  the prompt "Do all cold reviews and any other work dependent on fable", on
  the Fable tier (`claude-fable-5-1`), orchestrating seven rule-4 passes queued
  by that run. It wrote this brief from the queue pointer, the landing commits'
  subjects and `--stat` file lists, and the delta paths' names; it did not open
  the intent record or the pull request.
- **Who takes the review:** a fresh Fable subagent (`claude-fable-5-1`) spawned
  by the brief-writer with this brief as its only framing. It is not the
  author's session and was not instructed by the author. The reviewer repeats
  its own provenance in the verdict.
- **Orchestration shape, disclosed per rule 4:** reviewer-plus-orchestrator. The
  orchestrator holds the `.deferred.md` sibling outside the worktree and
  outside the harness scratchpad (subagents can read the scratchpad), commits
  the reviewer's phase-1 findings unrevised, then releases the sibling's text by
  message; the reviewer appends a reconcile section; the orchestrator folds the
  sibling in and updates the pointer. The orchestrator forms no finding and
  writes no severity. Both seats are Fable, so the off-tier clause is not
  invoked; the shape is stated anyway so the record is auditable.
- ⚠️ **Brief-writer's exposure, disclosed** (rule-2 material it met before
  writing): this session found the pointer on `main`; earlier in the sitting
  the authoring run had told it over the cross-session channel that a pathscan
  change was held as a draft pull request for the principal's ruling, and the
  landing merge's subject says the principal ruled. Earlier in the same sitting
  this session commissioned read-only inventories of the board's open items and
  of every verdict in `docs/reviews/`, for a ruling round; the summaries it
  received include prior findings on pathscan. Those summaries are author-side
  framing this pass must meet cold; every line of them that bears on this delta
  has been moved to the sibling and kept out of this brief. It also ran pathscan
  once over the whole tree to identify a standing warn-only finding on the hook
  plane, and read the finding list's first eight lines. The brief-writer read
  the 2026-09-25 batch's staged-plane brief as a formatting template, the
  session index entries of 2026-09-19 to 2026-10-01, and, as doctrine at onramp,
  `docs/method/REVIEW.md`, `docs/method/00-APEX.md` and
  `docs/method/COMMUNICATION.md` § *Asking for a ruling* at HEAD.

## What the work is

Landing commits (diff these; review the paths at HEAD — the worktree carries
`main` at `57b9764` or later, which includes the delta):

- `e5b44fe` (2026-10-03) — merge of `acb2c78`: pathscan expands brace groups and
  skips inline-span command invocations (pull request 96)

Delta paths:

- `tools/pathscan.py` — candidate extraction: brace-group expansion, and the
  skip for an inline code span that is a `./` command invocation
- `tools/test_pathscan.py` — its tests

`tools/README.md` § *pathscan*, `tools/floor.py` and the workflows are not in
the merge's file list; whether they still describe and wire the tool correctly
is yours to establish. Note that a separate merge the same day (`5d087ec`)
single-sourced pathscan's allow-marker and ignore-file code into
`tools/allowmarker.py`; that change is another pass's subject, but its effect on
this delta's behaviour is in scope.

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code,
tests and live behaviour. The lenses organise it; they do not bound it.
Non-goals are the only narrowing and are themselves reviewable.

Driven, not read: build a fixture doctrine tree whose prose cites paths in every
brace shape — a single group, two groups in one path, a nested group, an empty
alternative, a group with spaces, an unbalanced brace, a brace inside a fenced
block, a shell-style `${VAR}` and a `{{ template }}` that are not path groups, a
group whose expansions partly exist and partly do not — and every inline `./`
shape: a real command invocation, a real relative path that happens to start
with `./`, a `./` path with arguments, a `./` inside a longer span. Run pathscan
with `--json` over that tree at the landing commit's parent and at HEAD in a
scratch clone and diff the outputs; every difference is either a declared
behaviour change or a finding. Then run it over this repo's gated scope at both
commits and account for every finding that appeared or disappeared.
**Non-goals:** whether pathscan should block rather than warn, and the board
items that commissioned the change.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself.
   Expanding a brace group presumes the braces are a path shorthand: find the
   text that is not, and record what the tool now reports. Skipping an inline
   `./` span presumes it is a command, not a citation: find the stale path the
   skip now hides.
2. **Correctness & quality.** Read all of `tools/pathscan.py` and its tests.
   Run `--selftest`, `python3 -m unittest tools.test_pathscan` (or the form the
   suite actually uses — lift it from CI), the full Python suite once in the
   foreground with a long timeout, and every state in *Scope*. Check the
   expansion is bounded on a pathological input.
3. **Completeness / harvest.** Every surface that says what pathscan catches
   and does not: `tools/README.md`, the module docstring's false-negative list,
   `--help`, the floor registry `why`, `CHANGELOG.md`. Do they describe the two
   new behaviours and their residuals?
4. **Security & privacy** — mandatory. The tool reads files named by argv and a
   scope declaration and prints path text from them: check an expansion that
   resolves outside the root, a group that explodes combinatorially, and control
   or bidi characters in a cited path. The house scanner is discharged by
   grounds (landed delta; the pending diff is this brief) — say so, and deliver
   the code-altitude read by hand, against the OWASP catalogue.

## Re-run obligation

Re-run, do not read. A recorded proof is a claim that can be stale at the commit
that recorded it; a proof you have not re-run is not one you can close on. Lift
floor invocations from `.githooks/pre-commit`, `tools/floor.py` and
`.github/workflows/ci.yml` rather than guessing.

- `python3 tools/pathscan.py --selftest`; pathscan's unit tests; the full
  Python suite once (foreground, long timeout)
- the floor on both planes at HEAD
- the fixture-tree `--json` diff and the gated-scope diff, parent against HEAD

## House rules for this run

- You work in the review worktree `/Users/mike/worktrees/atelier-review-430`
  (branch `review-430-1003`), read-only except for THIS brief file. Never open
  another `docs/reviews/2026-10-03-*` file — each is another pass's verdict on a
  sibling delta. Run **no git command that writes** there (no add, commit,
  stash, checkout, worktree, reset, clean). Read-only git (`log`, `show`,
  `diff`, `blame`) is fine. Before you start, confirm the delta is present:
  `git -C /Users/mike/worktrees/atelier-review-430 merge-base --is-ancestor
  e5b44fe HEAD` must exit 0; if it does not, stop and report. Mutation probes,
  fixture trees and checkouts of older commits go in your own clone: `git clone
  /Users/mike/worktrees/atelier-review-430 <scratchpad>/PX/probe` under the
  session scratchpad.
- One heavy process at a time on this machine: run the full suite at most once,
  in the foreground with a long timeout (allow 20 minutes); if a memory-probe
  test times out, re-run that test file alone before recording it. Never scan
  any tree outside the worktree or your scratch clone, and never point a
  scanner at the machine's other repos. Other sessions are live on this machine
  and in this repo's primary checkout; touch nothing there.
- `/security-review` is **discharged by grounds**: it reads the session's
  pending diff, which here is this brief, and this is a landed-delta review.
  State that line in your lens-4 answer and deliver the code-altitude read by
  hand.
- Dates in your verdict are absolute ISO-8601 from `date -u` (the hook-plane
  `datescan` reds relative words such as "yesterday" or "next week" and would
  block the orchestrator's commit). Wrap prose at ≤ 100 columns. NZ English.
  Never quote a secret, a placeholder token, an email address, a private
  repo's name or any personal detail — this repo is PUBLIC; describe, don't
  quote.
- Review deep, not fast. A finding needs a probe or a re-driven claim behind it,
  not reasoning alone; a clean lens needs the trail that earned it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the deferred material lives in the sibling .deferred.md, held by the orchestrator outside the worktree under the rule-1 split and released only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`,
`docs/sessions/`, every prior verdict in `docs/reviews/`, the queue pointer
`docs/roadmap/160-doctrine-review-owed/490-rule-4-cold-pass-queued-pathscan-brace-expansion.md`
(it carries the author's framing and this pass's claim line), pull request 96's
description and comments, and:

- `docs/sessions/2026-10-03-0144-queue-run-handups-and-tool-defects.md` (the
  intent record)
- every item under `docs/roadmap/320-child-filed-findings-via-pointing-up/`
  (the commissioning items are among them)
- every item under `docs/roadmap/160-doctrine-review-owed/` and
  `docs/roadmap/200-anti-slop-invariant-registry-promote-rec/` (pointers that
  carry prior pathscan verdicts' outcome lines)

Sweep with `python3 tools/coldsweep.py --root
/Users/mike/worktrees/atelier-review-430 --also-exclude
docs/roadmap/320-child-filed-findings-via-pointing-up --also-exclude
docs/roadmap/160-doctrine-review-owed --also-exclude
docs/roadmap/200-anti-slop-invariant-registry-promote-rec <pattern>` — rule 2's
default bar plus the items above; check each `--also-exclude` path exists before
relying on it, and use `--include-barred` only with disclosure in the verdict.
Reading the *delta* is never barred: the code, its tests, the README entry and
the registry are the subject. What is barred is the author's narrative of why,
and the verdicts that recorded it.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list.
Then append your verdict below a `---` divider in THIS file: provenance repeated
(how you were spawned, your tier, what you read, at which SHA), per-lens
answers, findings with stable IDs (prefix `PX`: `PX1`, `PX2`, …) and severities
(MAJOR / MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL
line with counts, a re-run ledger with the commands and their results, and a
follow-up checklist. Then STOP and report to the orchestrator that phase 1 is
written. Do not open the sibling (it is not in the tree); do not edit the queue
pointer, the board, or any file but this one.

**Phase 2.** On receipt of the sibling's text, append `### Reconcile` beneath
your verdict: per-finding notes against the seeded questions and the intent
record, any finding formed at reconcile marked as such, and the overall line
restated. Never revise phase-1 text. The orchestrator folds the sibling in below
your reconcile.

Findings are the principal's to decide (rule 3): record all, apply nothing;
your counsel per finding is welcome, labelled as counsel and kept beneath the
finding.

---

## Verdict — phase 1 (written 2026-10-03 0556 UTC)

**Overall: PASS-WITH-FINDINGS — 0 MAJOR, 3 MODERATE, 5 minor, 3 notes.** The two
behaviours do what they say on the shapes they were built for, and this repo's gated
scope is unchanged by them. The findings are about what the delta costs elsewhere: a
64-fold work multiplier with no per-file ceiling, three new ways a stale path reads as
clean, and no reader-facing surface that says so.

### Provenance

- Reviewer: `claude-fable-5-1` (Fable tier), a subagent spawned by the brief-writer with
  this brief as its only framing. Not the author's session, not instructed by it.
- Read at worktree HEAD `56e5687` (delta `e5b44fe` confirmed an ancestor, exit 0): all of
  `tools/pathscan.py`, the delta's hunk of `tools/test_pathscan.py` plus its
  `BoundedMemory` class, the pathscan entry in `tools/floor.py`, `tools/README.md`
  § *pathscan*, `.atelier-floor.json`, `.githooks/pre-commit`, the test and floor lines of
  `.github/workflows/ci.yml`, and the top of `CHANGELOG.md`.
- Scratch clones under the session scratchpad: `parent` at `0ed44a3` (the merge's first
  parent, which already contains `5d087ec`), `landing` at `e5b44fe`, `probe` at `56e5687`.
- ⚠️ **Exposure, disclosed.** (a) I read the commit message of `acb2c78`, which is author
  narrative. (b) The merge's `--stat` showed the names of barred files. (c) One whole-root
  `--include-records` run printed file names, line numbers and path tokens from three other
  `docs/reviews/2026-10-03-*` files, and a pre-suppression run printed tokens from line 44
  of a barred `320/` item. I opened none of those files; scanner output was the only
  contact. (d) I read `CHANGELOG.md` line 1798 to account for a disappeared finding.
- ⚠️ **Interrupted and resumed.** The orchestrator paused this pass for a budget check and
  resumed it with an instruction to economise. Consequences are in the re-run ledger: the
  full suite is incomplete and the floor was not re-run by me.

### Lens 1 — approach and assumptions

Load-bearing assumptions, and what the probes found:

1. *A brace group with a comma is path shorthand.* False for a quantifier or a format
   string (PX5).
2. *A group without a comma is a placeholder, so the whole token can go.* The token's
   directory prefix was a live claim and was checked before (PX3).
3. *A `./` token opening a span is a command.* A span holding only a `./`-led path is a
   citation, and it is skipped too (PX2).
4. *64 alternatives per token bounds the work.* It bounds one token, not a line or a
   file (PX1).
5. *Adding `{` and `}` to the lookbehind only stops mid-token resync.* It also hides any
   path written directly against a brace (PX4).

### Lens 2 — correctness and quality

Selftest and the 127 unit tests pass. The fixture tree (54 lines, every shape in *Scope*)
gave 25 findings at the parent and 96 at HEAD; `landing` and `probe` outputs are
identical, so nothing after the merge changed behaviour. The intended cases are right:
each alternative is checked, a missing one is caught, nested and runaway groups are
skipped, `${VAR}` is skipped whole. Regex timing is linear on every hostile shape tried
(4.2 MB of unclosed groups: 0.36 s). Expansion of one very wide group is cheap, because
each alternative replaces the group. The defect is the multiplier across tokens (PX1).

**Gated scope, parent against HEAD: no difference.** One finding both sides (a `../`
path in `docs/method/session-open/`), ten allow-marker suppressions both sides. The
gated scope holds two `./` spans; neither was a candidate before or after, because a
`./` lead defeats the top-directory leg and neither ends in a known extension.
Wider `docs` scope: one finding disappeared (an allow marker added to the line, tree
change not tool change) and two new findings appear at HEAD on that same line, both
suppressed by that marker. Whole root with records: one record line in `CHANGELOG.md`
stopped being truncated and now resolves, which is the declared behaviour.

### Lens 3 — completeness

Only the module docstring's step 3 describes the two behaviours. See PX8.

### Lens 4 — security and privacy

`/security-review` is **discharged by grounds**: it reads the session's pending diff,
which here is this brief, and this is a landed-delta review. Code-altitude read by hand:

- Injection into output (OWASP A03): new channel, PX6.
- Resource exhaustion (denial of service): PX1.
- Path traversal (A01): an expansion can resolve outside the root, but so could a literal
  `..` token at the parent; existence only, no content read (PX10).
- No new file reads, no deserialisation, no subprocess, no network, no secrets handled.
  JSON output escapes control characters correctly.

### Findings

**PX1 — MODERATE. The expansion cap is per token; nothing caps a line or a file.**
One 1.09 MB line of 25,000 tokens, each expanding to exactly 64 alternatives: the parent
finished in 0.31 s at 20.7 MB peak; HEAD took 141.9 s at 1.82 GB peak and emitted
1,600,000 findings. A brace-free line of the same size costs 2.4 s and about 60 MB on
both. `CHANGELOG.md` records the ruling that every guard runs in bounded memory; this
tool's `BoundedMemory` test pins file count only, so the suite stays green. pathscan runs
whole-tree on every child's hook.
*Counsel:* cap findings or expansions per file, counted not dropped, and add a content-size
memory test.

**PX2 — MODERATE. The `./` skip hides a stale citation whenever the span holds only the
path.** Fixture lines D03, D04, D14, D15 and D17: a span such as a `./`-led doctrine file
or tool path that does not exist was flagged at the parent and is clean at HEAD. The
unit test pins the no-argument form as skipped. Nothing in the skip tells a command from
a citation; an argument after the token would. Live cost in this repo's gated scope today
is zero (see lens 2); children are unmeasured.
*Counsel:* require trailing arguments, or keep checking when the token starts with a known
top directory after the `./`.

**PX3 — minor. A comma-less group now discards the whole token, including a directory
prefix that used to be checked.** B19 and B20: a templated file under a directory that
does not exist was flagged at the parent (the truncated directory) and is clean at HEAD.
The commit message says the change only drops findings in its two classes; this is
outside them.

**PX4 — minor. A path written directly against `{` or `}` is no longer seen.** B15, B16,
B17: a tight template or set notation around a missing path was flagged at the parent and
is clean at HEAD. The spaced form (B14) is still caught. Undocumented.

**PX5 — minor. Non-path brace text yields targets nobody wrote, and the finding does not
show the source text.** B21: a quantifier after `docs/x` reports `docs/x3.md`. B35: a
format string reports `tools/name`. `Finding.target` is commented as the token as
matched; it is now an expansion, so a reader searching the line for the target finds
nothing.
*Counsel:* name the written token in the detail.

**PX6 — minor. Control and bidirectional characters now reach the terminal through a
group.** The group body accepts any character except braces, whitespace and `/`; the old
token class could not carry these. B37: `od` on the human output shows a raw escape byte
inside the printed target, and a right-to-left override alongside it. `--json` is safe.
The changelog shows the house already strips such characters in `floorfleet`.

**PX7 — minor. Span detection is line-local parity, so the skip is inconsistent.** D16: a
`./` token after a *closing* backtick, on a line that begins inside a wrapped span, is
skipped. D09 and D10: the same command in a double-backtick span, or in a span that wraps
to the next line, is still flagged. The stated rationale is same text, same answer.

**PX8 — MODERATE. No reader-facing surface describes the two behaviours or their
residuals.** `tools/README.md` § *pathscan* and its *What it cannot see* line, `--help`,
the registry `why` and `CHANGELOG.md` say nothing of brace expansion or the `./` skip. The
docstring's false-negative list does not name PX2, PX3, PX4, spaced groups, or nested and
unbalanced groups. Separately, the docstring's STATUS paragraph still says the tool is not
in the floor registry, which the registry contradicts; I did not establish when that went
stale.

**PX9 — note. The truncation class survives in three shapes.** A group with a space after
the comma (B08), a nested group under a deeper prefix (B06) and an unbalanced brace (B10)
still truncate at the brace, exactly as at the parent. At HEAD the tool still emits the
truncated token on the commissioning item's own line 44, pre-suppression.

**PX10 — note. Existence probing outside the root is pre-existing; expansion multiplies
it.** A literal `docs/../../` token reports missing at the parent too. One token can now
make 64 such probes (B27).

**PX11 — note. Test gaps.** `--selftest` exercises neither behaviour. No test sits on the
boundary: exactly 64 alternatives passes and yields 64 findings from one token (B26).

### Re-run ledger

| Command | Result |
|---|---|
| `merge-base --is-ancestor e5b44fe HEAD` | exit 0 |
| `python3 tools/pathscan.py --selftest` (probe) | `selftest OK`, exit 0 |
| `python3 -m unittest discover -s tools -p test_pathscan.py` | Ran 127 tests, OK |
| Suite chunk 1 (8 files) | Ran 25, 26, 43, 20, 39, 68, 137, 118 — all OK |
| Suite chunk 2 (10 files) | Ran 37, 134, 60, 73, 11, 3, 19, 33, 15, 30 — all OK |
| Suite chunk 3 (10 files) | ❌ **not run** — interrupted, then dropped on instruction |
| Fixture `--json` diff, parent / landing / HEAD | 25 / 96 / 96; 15 gone, 86 new, 10 same |
| Gated-scope diff, tools and trees crossed | 1 → 1, suppressed 10 → 10, no difference |
| Mutation: rename `instruments/install` away | both tools flag line 42 only |
| Pathological line, parent / HEAD | 0.31 s, 20.7 MB / 141.9 s, 1.82 GB |
| Floor, both planes at HEAD | ❌ **not re-run by me** |

⚠️ The suite is 19 of 29 files, 1,018 tests, all OK. Every test file that imports pathscan
is among them (`test_pathscan`, `test_floor`, `test_allowmarker`, `test_licenscan`,
`test_mixed_root`). The unrun files are `test_reviewscan`, `test_secretscan`,
`test_signfleet`, `test_signscan`, `test_sizescan`, `test_spellscan`, `test_stampscan`,
`test_templates`, `test_worktree` and `test_wrapscan`. The orchestrator states the pushed
floor at `57b9764` is green; that is its statement, not a proof I re-ran. The only floor
line I drove is pathscan's own, by hand, over the gated scope.

### Follow-up checklist

- [ ] PX1: rule on a per-file ceiling and a content-size memory test.
- [ ] PX2: rule on whether a bare `./` path in a span is a command or a citation.
- [ ] PX3, PX4: accept as stated residuals, or restore the lost checks.
- [ ] PX5, PX6: name the written token in the finding; sanitise the human rendering.
- [ ] PX7: accept or align the span cases.
- [ ] PX8: harvest into the README, `--help`, the false-negative list and the changelog.
- [ ] Run the ten unrun test files and the floor on both planes before this pass closes.

### Reconcile (written 2026-10-03, after the sibling's release)

**Overall, restated: PASS-WITH-FINDINGS — 0 MAJOR, 3 MODERATE, 5 minor, 3 notes.** No
severity moves. One phase-1 sentence is corrected below (PX9), and one observation is
formed at reconcile.

Read in phase 2, and nothing else: the sibling's text, the intent record's two pathscan
passages (the build-and-hold section and the addendum), items `320/010` and `320/170`,
and pull request 96's description (it has no comments). No suite and no new probe was
run; every answer below rests on what phase 1 drove.

**Seeded questions.**

1. *Does expansion turn one finding into N, and is the count honest?* Yes to both. Each
   missing alternative is its own finding, duplicates on a line collapse (B32), and the
   suppressed tally counts each one. The pull request's "57 to 59" matches what I
   measured as two new pre-suppression findings on the `docs` scope. What `--json` lacks
   is any link from an expanded target back to the text as written (PX5).
2. *Does the `./` skip hide a stale path that used to be flagged, and is that stated?*
   Yes, it hides one (PX2), and no, the docstring's false-negative list does not say so
   (PX8). The intent record shows the case it was built for: a command whose script sits
   under the child's own tools directory. The skip is wider than that case, because it
   also takes a span holding only a path.
3. *Did the standing `session-open-prompt.md:15` finding change?* No. It is the single
   gated finding at the parent and at HEAD, same line, same target.
4. *What was ruled, and does the code do that and no more?* The principal chose
   expand-and-check over exclude, on the recommendation, conditional on a check against
   the requesting transcript, which the item records as done. The merged code matches the
   pull request's description. Two things sit outside what the ruling was briefed on:
   - The description offered one decision, expand or exclude. The `./` skip rode on the
     same branch, and `320/170` is a report with no ruling of its own on that ask.
   - The description said no findings were removed. That is true of atelier's tree. It
     did not say the change can remove findings elsewhere (PX2, PX3, PX4), nor name the
     cost in PX1. The commit message's "only drop or reshape findings in these classes"
     is contradicted by PX3 and PX4.
   *Counsel:* the ruling stands; these are grounds for a re-brief, not for treating it as
   void.
5. *Is the expansion bounded?* Per token, yes, at 64. Per line and per file, no (PX1).

**Per-finding notes.**

- **PX1.** The intent record's addendum has the principal restating, the same day, that
  guards stream at any scale. That makes PX1 the finding to rule first. I hold it at
  MODERATE because the input must be hostile or machine-generated to reach it.
- **PX2.** Confirmed against intent as wider than the commissioned case. Unchanged.
- **PX3, PX4.** Neither item asked for these losses; the item's own smaller candidate
  (exclude the brace) would have produced PX3's loss for every brace token, so
  expand-and-check is still the better shape. Unchanged.
- **PX5, PX6, PX7, PX10, PX11.** Nothing in the intent material bears on them. Unchanged.
- **PX8.** Prior pass `PS8` asked for an honest false-negative list and `FR1` for a README
  entry; both were applied then. This delta re-opens the same gap for its two behaviours.
  Unchanged.
- **PX9 — corrected, phase-1 text left as written.** The last sentence said the tool
  still emits the truncated token on the item's line 44, implying a surviving truncation.
  Having read the line: the item quotes the truncated form literally, as its own
  example, so that token is written text, not a truncation at HEAD. The three surviving
  shapes (B06, B08, B10) stand; the item also records the trailing-slash question as
  deliberately untouched.
- **Prior `SP7`** (each Markdown file read whole) is adjacent to PX1 and still unruled;
  PX1 is a separate mechanism, the findings list rather than the read.

**Formed at reconcile — PX12, note.** `320/010` line 44, in this public repo, quotes a
private child's own file names, and its new allow marker says so. Whether those names
are acceptable to publish is outside this delta and is the principal's call; recorded
here only because the delta's landing added the marker that draws attention to the line.

Counts with the reconcile note included: 0 MAJOR, 3 MODERATE, 5 minor, 4 notes. Still
owed before this pass closes: the ten unrun test files and the floor on both planes.

## Folded sibling — released after the phase-1 findings were committed

The `.deferred.md` sibling the orchestrator held outside the worktree, folded in
verbatim at close; the reviewer met it only in phase 2.

# Deferred sibling — pathscan's brace expansion and inline `./` skip (PX)

Held by the orchestrator outside the worktree and outside the harness
scratchpad. Released to the reviewer only after its phase-1 findings are
committed. Folded into the verdict file at close.

## 1. The queue pointer's own framing (author's words)

> Rule-4 cold pass queued: pathscan's brace expansion and inline `./` skip
> (`320/010` class C, `320/170`). The run authored this itself (its dispatched
> workers' output counts as the run's authorship). It was queued at landing,
> and the run neither takes it nor spawns a reviewer for it. Tier: Fable, the
> principal-named review tier, checked at selection. Pass type: code cold pass,
> per `method/REVIEW.md` rule 4. Delta, scoped to paths: `tools/pathscan.py`
> and `tools/test_pathscan.py`, from PR #96, merged on `main` on 2026-10-03.
> Intent record: `docs/sessions/2026-10-03-0144-queue-run-handups-and-tool-defects.md`.

## 2. Intent record and commissioning items (read in phase 2)

- `docs/sessions/2026-10-03-0144-queue-run-handups-and-tool-defects.md`
- `docs/roadmap/320-child-filed-findings-via-pointing-up/010-*.md` (class C)
  and `170-*.md`
- pull request 96 (its description, and the principal's ruling on it)

## 3. What the authoring run said to the orchestrator (channel, verbatim)

> New draft PR #96 holds a pathscan change for Mike's ruling, because 320/010
> class C turned out to be unruled. Add it to your ruling-round list if useful.

No message announced the 160/490 pointer; the orchestrator found it on `main`.
The landing merge's subject reads "(PR #96, Mike ruled)". Nothing else from that
run was read.

## 4. Prior findings and seeded questions (the orchestrator's, labelled)

Prior pathscan verdicts (from inventory summaries):

- 2026-07-26 pathscan S2 pass (`PS`, ruled 2026-08-04 "fund the rescope", all
  applied): PS1 CI scanned `docs` only and three anchors false-positived on
  docs-relative shorthand; PS4 the baseline was about 97 % records, so only the
  doctrine surface can be gated; PS8 the docstring's "every cited occurrence"
  overclaimed (a single-segment `templates/` citation yields no candidate). The
  minors asked for an honest false-negative list in the docstring: emphasis,
  multi-line placeholders, TODO masking, indented code.
- 2026-08-06 D1 application pass (`PD`, ruled): tests placed after `main()`
  (fixed); the burn-down denominator; pathscan and linkscan double-reporting one
  defect (accepted).
- 2026-08-09 floor-render batch (`FR`, ruled 2026-08-23): FR1 no README
  catalogue entry (fixed); FR2 the child default scope included records (fixed
  with a records-excluding default and `--include-records`).
- 2026-09-25 secretscan-stream / pathscan-roots pass (`SP`, unruled): SP5
  declared-roots type validation gaps; SP6 a symlink can escape the lexical
  check; SP7 each Markdown file is still read whole; SP8 the README omits the
  roots.
- Board `320/310` (open 🎯): should pathscan block instead of warn — "decide
  after `320/010`'s declared roots ship; measure what is left".
- A standing warn-only finding on the hook plane at
  `docs/method/session-open/session-open-prompt.md:15` (a `../atelier/…` path),
  recorded as pre-existing by HF10, AK5 and TR10 on 2026-09-25, and still
  present at `57b9764`.

Seeded questions (the orchestrator's): (1) Does brace expansion turn one
finding into N, and is the count honest in the tally and `--json`? (2) Does the
inline `./` skip hide a stale relative path that used to be flagged — a new
false negative — and is that residual stated in the docstring list PS8 asked
for? (3) Did the standing `session-open-prompt.md:15` finding change? (4) What
did the principal actually rule on pull request 96, and does the merged code do
that and no more? (5) Is the expansion bounded?
