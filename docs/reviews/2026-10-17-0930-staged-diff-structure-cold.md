# Cold pass — the staged diff read by its structure

**Pass type:** code cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection by whoever takes the pass.
**Status:** BRIEF ONLY — the review has NOT run. Written 2026-10-17 UTC by an Opus
brief-writer; the pass waits for a further cold Fable session that neither the
delta's author nor this brief-writer (nor its orchestrator) started or instructed.
Tier is checked at selection (rule 4).
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/800-rule-4-cold-pass-queued-staged-diff-structural-reader.md`.
**Why it earns a review:** the three blocking guards that keep credentials, conflict markers
and personal data out of a commit — in this public repo and in every child, on the hook plane —
now read what a commit adds through one new parser, which also decides when a commit is refused
outright (exit 2). A reader that mis-attributes or drops a line is a silent false negative on
those guards; one that refuses a legitimate diff blocks every commit of that shape.

## Spawn provenance

- **Author of the work under review:** the 2026-10-16 queue run whose intent record is dated
  2026-10-16 07:03 UTC (an Opus orchestrator with dispatched workers; the pointer counts the
  worker's output as the run's authorship). The landing commit's trailer names a Sonnet model,
  the merge's an Opus model. Not opened here.
- **Who wrote this brief:** an Opus subagent (`claude-opus-5-5`) dispatched on 2026-10-17 by the
  Mike-opened Fable review session working in the worktree `atelier-review-1017`, on Mike's
  2026-10-16 answer that a fresh Opus session writes these briefs. It authored none of the delta.
  It is **off-tier for review, disclosed: it forms no finding and writes no severity**, and it
  stops after this brief and its sibling.
- **Who takes the review:** a further cold Fable session, not yet started, that passes rule 4's
  criterion. The reviewer repeats its own provenance in its verdict.
- ⚠️ **Exposure, disclosed** (rule-2 material met before writing). This brief-writer read: the
  four queue pointers it was assigned (160/780–810) and, as a shape example, the 160/500 pointer
  with its claim line; the delta lists of eight neighbouring pointers (160/700, 720, 730, 760,
  820, 830, 850, 860); the landing commit's and merge's subjects, `--stat`, diff **and message
  bodies** (the author's own account); the subjects and `--stat` of later commits on the same
  files; `REVIEW.md` rules 1–4; three user-local templates — the ask halves of the 2026-10-16
  expected-toolbox brief and of the 2026-10-16 **scanner-rule-gates brief, whose delta is two of
  this pass's files** (`leakscan.py`, `secretscan.py`), and the whole expected-toolbox sibling,
  seeded questions included (another pass's framing); HEAD greps of `tools/` for every staged-diff
  reader and `--staged` flag, and `tools/floor.py`'s hook and CI arguments; the commissioning
  item's head line; filename-level greps of `docs/reviews/` (no file there opened); and its
  harness-loaded memory index and instruction files (one-line notes, some about these guards'
  history). It did not open the intent record, `docs/SESSIONS.md`, `docs/sessions/`,
  `docs/ROADMAP-DONE.md` or any file under `docs/reviews/`. Its orchestrator passed it an
  instruction set and no evaluative content about the delta; what the orchestrator read is its
  own to disclose in its claim. Everything evaluative is in the sibling.

## What the work is

Landing commit and merge (diff the commit; review the paths at HEAD, `8acfff1` or later):

- `39a74b9` (2026-10-16 08:11 UTC) — tools: read the staged diff by its structure, not by how a
  line looks (115/280); landed in merge `ef75803` (2026-10-16 08:15 UTC)

Delta paths: `tools/report.py` (`STAGED_DIFF_CMD`, `_HUNK_RX`, `DiffReadError`,
`STAGED_DIFF_FAILURES`, `parse_added_lines`, `staged_added`, the module docstring's new
sentence), `tools/secretscan.py`, `tools/conflictscan.py` and `tools/leakscan.py` (each one's
`staged_added_lines` and the `except` in `_main`), their tests `tools/test_report.py`,
`tools/test_secretscan.py`, `tools/test_conflictscan.py`, `tools/test_leakscan.py`, and
`tools/README.md` (the shared-reader paragraph).

**Later commits on the same files — not this delta; do not attribute them to it.**
`tools/report.py` is unchanged since the merge; confirm that.

- `f4afb7a` (2026-10-16 15:28 UTC) — tools: conflictscan and leakscan report a staged finding at
  its real file line (its own pass, 160/830); it changes how two of the three callers use the
  reader's line numbers
- `1c24781`, `72a68cc`, `e3e8a4f` (2026-10-16) — touch `tools/README.md` or `tools/test_report.py`
  outside this delta's hunks (160/810, 850, 840)

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code, tests and live
behaviour. The lenses organise it; they do not bound it. Non-goals are the only narrowing and are
themselves reviewable.

Derive, from git's documented diff format and from `git diff` itself rather than from the
delta's tests (`EVIDENCE.md` § 15 is the reason), every shape `git diff --cached --unified=0`
can emit under `STAGED_DIFF_CMD`, and compare each with what `parse_added_lines` does. Pay
attention to:

- **Header shapes.** New, deleted, renamed, copied, mode-changed, type-changed, binary,
  submodule, symlink and empty files; quoted and non-ASCII paths; a path containing ` b/`, a
  newline or a tab; `/dev/null` on either side.
- **Hunk shapes.** Omitted counts, zero counts (`+0,0`, `-n,0`), `\ No newline at end of file`
  on either side, a hunk header carrying function context, the last hunk of the diff.
- **Bytes.** Undecodable bytes, a lone CR, CRLF files, form feed, NEL and the Unicode line
  separators inside a line, a NUL.
- **Repository state and configuration.** A diff taken mid-merge, mid-rebase or mid-cherry-pick
  with unmerged paths; user, repo and `.gitattributes` settings that change what `git diff`
  prints (prefixes, colour, external diff drivers, text conversion, rename and copy detection,
  `diff.relative`, word-diff, `core.quotePath`). Which does `STAGED_DIFF_CMD` pin, and which can
  still reach the parser?
- **The fail-closed path.** Every input that raises `DiffReadError`: which of them git can
  actually emit for a legitimate commit, and what the hook plane does on exit 2 (does it block,
  and does the message tell the committer what to do).
- **The three callers.** Each lost its own loop and filter, and `secretscan` its own fallback
  for a header without the `b/` prefix; check each caller's downstream use, path filters,
  ignore globs and line numbers at landing, and say what `f4afb7a` later changed.
- **Cost.** The reader now holds the whole staged diff as bytes and every added line in a list;
  measure it on a large staged change, against the house's bounded-guard rules.

**Non-goals:** the guards' detection rules themselves (their patterns, gates and term lists),
which other passes own. How the reader feeds them is in scope.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself first. The central one:
   that a hunk's counts locate its last line whatever the line's text says. Others: that every
   line git writes outside a hunk is safe to ignore; that pinning prefixes in the command removes
   the configuration surface; that refusing an unknown shape is always the safe failure.
2. **Correctness & quality.** Read `parse_added_lines`, `staged_added` and all three callers
   whole; diff `39a74b9`. Build a shape table: shape, what git emits, what the reader yields or
   raises, and a reproducing fixture wherever they differ from a correct reading. Check whether
   the tests' fixtures were produced by real `git diff` runs or written by hand, and whether each
   posed-header test fails on `39a74b9^`.
3. **Completeness / harvest.** `tools/README.md`'s description of the reader and of the three
   guards' staged planes; `docs/method/GUARDS.md`'s claims about what the hook plane catches;
   every other guard with a staged plane (`board.py`, `harvestscan.py`, `publishscan.py`,
   `blockscan.py`, `floor.py`) and whether any still parses diff text by its look.
4. **Security & privacy** — mandatory. This lens is the subject: hunt the staged change whose
   added line a guard does not see, or sees under the wrong file. Build counter-examples from
   synthetic values only — never a real credential, term-list entry or personal detail — and
   never quote one in the verdict. Also check denial of service: a staged change that makes the
   reader refuse every later commit, or run unbounded. `/security-review` is discharged by
   grounds (a landed delta; the pending diff is not the work) — say so, and deliver the
   code-altitude read by hand against the OWASP catalogue.

## Re-run obligation

Re-run, do not read. Lift floor invocations from `.githooks/pre-commit`, `tools/floor.py` and
`.github/workflows/ci.yml` rather than guessing.

- `python3 -m unittest tools.test_report tools.test_secretscan tools.test_conflictscan
  tools.test_leakscan -v`; `python3 tools/secretscan.py --selftest`, `python3
  tools/conflictscan.py --selftest`, `python3 tools/leakscan.py --selftest`
- the shape table, driven: in a scratch repository under your scratchpad, stage each shape and
  run the three guards with `--staged` at `39a74b9^`, `39a74b9` and HEAD; compare stdout, stderr
  and exit code
- the posed-header hole, reproduced on `39a74b9^` and shown closed on `39a74b9`, with a synthetic
  value
- the hook plane end to end in that scratch repository (`.githooks/pre-commit` with this repo's
  tools), including one exit-2 case
- the floor on both planes at HEAD; the full Python suite once, foreground

## House rules for this run

- Name the worktree you work in. Run no git command that writes there; read-only git is fine.
  Scratch repositories, staged fixtures and older checkouts go in a private clone under your
  session scratchpad, named by your prefix. Never open another `docs/reviews/2026-10-16-*` or
  `docs/reviews/2026-10-17-*` file — it is another pass's framing.
- One heavy process at a time on a shared machine: the full suite at most once, in the
  foreground; fixtures sized to finish in minutes, under `nice`. Never point a scanner at any
  other repo on the machine.
- `/security-review` reads the session's pending diff: discharge it by grounds for this landed
  delta, or keep the tree clean whenever you spawn it.
- Dates absolute ISO 8601 from `date -u`. Prose wrapped at ≤ 100 columns. NZ English. Never quote
  a secret, placeholder token, email address or personal detail — this repo is PUBLIC; describe
  and locate instead. Counter-example lines in the verdict are described by shape, not pasted,
  where they would trip the guards on commit.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the deferred material lives in the sibling .deferred.md, held apart under the rule-1 split and opened only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`, every
prior verdict in `docs/reviews/`, the queue pointer, this brief's sibling
`docs/reviews/2026-10-17-0930-staged-diff-structure-cold.deferred.md`, the landing commit's and
merge's message bodies (read subject, stat and diff only), and the commissioning item `280` in
`docs/roadmap/115-guardrail-architecture-mike-commissioned/`.

Sweep with `python3 tools/coldsweep.py --root <your worktree> --also-exclude
docs/roadmap/160-doctrine-review-owed/800-rule-4-cold-pass-queued-staged-diff-structural-reader.md
--also-exclude docs/reviews/2026-10-17-0930-staged-diff-structure-cold.deferred.md
--also-exclude
docs/roadmap/115-guardrail-architecture-mike-commissioned/280-an-added-line-can-pose-as-a-diff-header-in-secretscan.md
<pattern>`; `--include-barred` only with disclosure. Reading the delta is never barred.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list. Then append your
verdict below a `---` divider in THIS file: provenance repeated (how you were spawned, your tier,
what you read), per-lens answers, the standing checklist V1–V7 each answered or discharged with
grounds, the shape table, findings with stable IDs (prefix `SX`: `SX1`, `SX2`, …) and severities
(MAJOR / MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL line with counts, a
re-run ledger, and a follow-up checklist. Then STOP and commit phase 1 unrevised before opening
the sibling.

**Phase 2.** Open the sibling; append `### Reconcile` beneath your verdict: per-finding notes
against the seeded questions and the intent record, any finding formed at reconcile marked as
such, and the overall line restated. Never revise phase-1 text. Then fold the sibling in below
the reconcile and delete it.

Findings on self-authored doctrine are the principal's to decide (rule 3; a guard is doctrine by
function): record all, apply nothing; counsel per finding is welcome, labelled and kept beneath
it.
