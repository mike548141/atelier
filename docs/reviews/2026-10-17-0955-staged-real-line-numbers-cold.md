# Cold pass — staged findings reported at their real file line in conflictscan and leakscan

**Pass type:** code cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection by whoever takes the pass.
**Status:** BRIEF ONLY — the review has NOT run. Written 2026-10-17 UTC by an Opus
brief-writer; the pass waits for a further cold Fable session that neither the
delta's author nor this brief-writer (nor its orchestrator) started or instructed.
Tier is checked at selection (rule 4).
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/830-rule-4-cold-pass-queued-staged-real-line-numbers.md`.
**Why it earns a review:** it changes the data shape two blocking guards scan on the
pre-commit hot path — the guard that keeps personal data out of a public repo and the
guard that keeps conflict markers out of every child — and every child's hook runs
it at its next commit.

## Spawn provenance

- **Author of the work under review:** the queue run whose intent record is dated
  2026-10-16 15:01 UTC (an Opus orchestrator with dispatched workers; the pointer
  counts the workers' output as the run's authorship; the commit's trailer names a
  Sonnet model). Not opened here.
- **Who wrote this brief:** an Opus subagent (`claude-opus-5-5`) dispatched on
  2026-10-17 by the Mike-opened Fable review session working in worktree
  `atelier-review-1017`, on Mike's 2026-10-16 answer that a fresh Opus session writes
  these briefs. It authored none of the delta. It is **off-tier for review,
  disclosed: it forms no finding and writes no severity**, and it stops after this
  brief and its sibling.
- **Who takes the review:** a further cold Fable session, not yet started, that
  passes rule 4's criterion. The reviewer repeats its own provenance in its
  verdict.
- ⚠️ **Exposure, disclosed** (rule-2 material met before writing). This
  brief-writer read: the four queue pointers it was assigned (160/820–850) in full,
  and 160/500 in full as the shape of an append line; the first lines of pointers
  160/790, 160/800 and 160/860; the landing commit's subject, `--stat`, diff **and
  message body** (the author's own account); the merge's re-merge diff stat (board
  and record files only); the subjects and `--stat` of later commits on the same
  files; two 2026-10-16 briefs in full as templates, one of them for a neighbouring
  leakscan pass (its list of later commits names this delta); `docs/reviews/`
  filenames and filename-level greps (no prior verdict opened); the title lines of
  the commissioning board items; single grep-hit lines from `tools/secretscan.py`
  and `tools/report.py` locating the staged readers; and its harness-loaded memory
  index. It did not open the intent record, `docs/SESSIONS.md`, `docs/sessions/`,
  `docs/ROADMAP-DONE.md` or `docs/method/REVIEW.md`. What its orchestrator read is
  the orchestrator's to disclose; it passed on an instruction file, three
  templates and a list of taken prefixes, and no evaluative content. Everything
  evaluative is in the sibling.

## What the work is

Landing commit (diff it; review the paths at HEAD, `b50db0c` or later):

- `f4afb7a` (2026-10-16 15:28 UTC) — tools: conflictscan and leakscan report a
  staged finding at its real file line; landed in merge `a1ba8c8` (2026-10-16
  15:31 UTC), whose own changes beyond the commit are board and record files only

Delta paths: `tools/conflictscan.py` (the new `scan_lines`, `scan_text` as its
wrapper, `staged_added_lines`, the staged branch of `_main`), `tools/leakscan.py`
(`scan_lines`'s and `scan_text`'s docstrings, `staged_added_lines`, the staged
branch of `_main`), `tools/test_conflictscan.py`, `tools/test_leakscan.py`, and the
staged-diff paragraph of `tools/README.md`.

The commit's parent is `2e2da81`, the same base as two sibling commits merged after
it (`e3e8a4f`, `72a68cc`, each its own pass); both also touch `tools/README.md`.
It builds on `39a74b9` (2026-10-16, the shared staged-diff reader
`report.staged_added`, its own pass). No later commit touches either guard file at
the time of writing; confirm at your HEAD and review the paths there.

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code, tests
and live behaviour. The lenses organise it; they do not bound it. Non-goals are the
only narrowing and are themselves reviewable.

Derive, from `report.staged_added` at HEAD, exactly which number it yields for an
added line, and test the claim "its real line number in the file the commit
produces" across diff shapes: a line below unchanged lines; two and more hunks;
hunks that also delete lines; a new file; a deleted file; a rename with edits; a
mode-only change; a file with no trailing newline; CRLF content; a git-quoted path;
an added line that looks like a diff header; a binary file. For each guard, what
the staged plane now reports and what it reported at `f4afb7a^`. Then the
behaviour beyond the number: does any rule in either guard read neighbouring
lines, carry state across lines, or depend on line 1 (a header-scoped marker, a
file-level allow, conflictscan's open-conflict state), and did handing it
non-consecutive line numbers change what it finds, not only where? Does the path
filter and `.leakscanignore`/glob handling see the same set as before? The README
now speaks for "all three guards": check the third against its code. The
whole-blob `scan_text` wrappers remain for other callers: who still calls each,
and with what numbering? **Non-goals:** the shared reader itself (`39a74b9`'s
pass) — but whatever this delta assumes about it is in scope.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself first.
   Among them: that only the reported number changes; that what held for a joined
   blob holds for a list of numbered pairs; that the whole-tree plane is untouched
   because it never used the staged reader.
2. **Correctness & quality.** Read both guards' staged paths and their tests whole;
   diff `f4afb7a`. Build a table of the diff shapes above against each guard:
   expected line, reported line at `f4afb7a^`, at `f4afb7a`, at HEAD. Check
   whether the new tests construct real staged diffs or hand-built pairs, and
   whether they would fail on the old code for the reason the test names.
3. **Completeness / harvest.** `tools/README.md` and each guard's module
   docstring; any doc in `docs/method/` that describes how a staged finding is
   located; other scanners with a staged plane that still number by blob; the
   `--json` output of both guards (does a consumer read `line`?).
4. **Security & privacy** — mandatory. These are blocking guards: hunt for any
   input on which the change makes either guard miss a finding it caught before,
   or report it against a line a person would not look at. Build fixtures from
   synthetic values only — never a real term-list entry or personal detail, and
   never quote one in the verdict. `/security-review` is discharged by grounds (a
   landed delta; the pending diff is not the work) — say so, and deliver the
   code-altitude read by hand against the OWASP catalogue.

## Re-run obligation

Re-run, do not read. Lift floor invocations from `.githooks/pre-commit`,
`tools/floor.py` and `.github/workflows/ci.yml` rather than guessing.

- `python3 -m unittest discover -s tools -p 'test_conflictscan.py' -v`, the same
  for `test_leakscan.py` and `test_report.py`; `python3 tools/conflictscan.py
  --selftest` and `python3 tools/leakscan.py --selftest`
- the staged plane, re-driven: in a scratch clone, stage each diff shape from
  *Scope* with synthetic findings and run both guards' staged mode at `f4afb7a^`,
  `f4afb7a` and HEAD; compare stdout, stderr, exit code and `--json`
- the "whole-tree output byte-identical" claim: both guards at `f4afb7a^` and
  `f4afb7a` over the repo tree and a fixture tree with findings
- the floor on both planes at HEAD; the full Python suite once, foreground

## House rules for this run

- Name the worktree you work in. Run no git command that writes there; read-only
  git is fine. Staged fixtures, older checkouts and probes go in a private clone
  under your session scratchpad, named by your prefix — never stage anything in
  the review worktree.
- One heavy process at a time on a shared machine: the full suite at most once, in
  the foreground. Never point a scanner at any other repo on the machine.
- `/security-review` reads the session's pending diff: discharge it by grounds for
  this landed delta, or keep the tree clean whenever you spawn it.
- Never open another `docs/reviews/2026-10-17-*` brief — it is another pass's
  framing.
- Dates absolute ISO 8601 from `date -u`. Prose wrapped at ≤ 100 columns. NZ
  English. Never quote a secret, placeholder token, email address or personal
  detail — this repo is PUBLIC; describe and locate instead. Fixture lines in the
  verdict are described by shape, not pasted, where they would trip the guards on
  commit.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the deferred material lives in the sibling .deferred.md, held apart under the rule-1 split and opened only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`,
`docs/sessions/`, every prior verdict in `docs/reviews/`, the queue pointer, this
brief's sibling `docs/reviews/2026-10-17-0955-staged-real-line-numbers-cold.deferred.md`,
the landing commit's message body (read subject, stat and diff only), and items
`300` and `310` in `docs/roadmap/115-guardrail-architecture-mike-commissioned/`
(the commissioning item, and a finding filed at the same merge on a neighbouring
behaviour).

Sweep with `python3 tools/coldsweep.py --root <your worktree> --also-exclude
docs/roadmap/160-doctrine-review-owed/830-rule-4-cold-pass-queued-staged-real-line-numbers.md
--also-exclude docs/reviews/2026-10-17-0955-staged-real-line-numbers-cold.deferred.md
--also-exclude
docs/roadmap/115-guardrail-architecture-mike-commissioned/300-two-staged-guards-report-the-wrong-line-number.md
--also-exclude
docs/roadmap/115-guardrail-architecture-mike-commissioned/310-conflictscan-open-conflict-state-runs-across-hunks.md
<pattern>`; `--include-barred` only with disclosure. Reading the delta is never
barred.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list. Then
append your verdict below a `---` divider in THIS file: provenance repeated (how
you were spawned, your tier, what you read), per-lens answers, the standing
checklist V1–V7 each answered or discharged with grounds, the diff-shape table,
findings with stable IDs (prefix `RN`: `RN1`, `RN2`, …) and severities (MAJOR /
MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL line with
counts, a re-run ledger, and a follow-up checklist. Then STOP and commit phase 1
unrevised before opening the sibling.

**Phase 2.** Open the sibling; append `### Reconcile` beneath your verdict:
per-finding notes against the seeded questions and the intent record, any finding
formed at reconcile marked as such, and the overall line restated. Never revise
phase-1 text. Then fold the sibling in below the reconcile and delete it.

Findings on self-authored doctrine are the principal's to decide (rule 3; a
guard is doctrine by function): record all, apply nothing; counsel per finding is
welcome, labelled and kept beneath it.
