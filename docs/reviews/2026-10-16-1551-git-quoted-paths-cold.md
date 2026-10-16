# Cold pass — guards read git-quoted paths

**Pass type:** code cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection by whoever takes the pass.
**Status:** BRIEF ONLY — the review has NOT run. Written 2026-10-16 UTC by an Opus
brief-writer; the pass waits for a further cold Fable session that neither the
delta's author nor this brief-writer (nor its orchestrator) started or instructed.
Tier is checked at selection (rule 4).
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/760-rule-4-cold-pass-queued-quoted-paths.md`.
**Why it earns a review:** git rewrites some file names before printing them, and
a guard that parses the rewritten form either misses the file or reads the wrong
name. This delta changed how four blocking guards and two board tools read
paths from git, on the staged plane every commit passes through; a residual miss
is a commit no guard read.

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
  `--stat`, the `report.py` diff and publishscan's plane hunk, **and both message
  bodies** (the author's own account); the subjects and `--stat` of later commits
  on the same files; `REVIEW.md` rules 1–4, the four lenses, the checklist and the
  lifecycle; the ask halves of two 2026-10-04 briefs as templates; `docs/reviews/`
  filenames and filename-level greps (no prior verdict opened); the names, not
  contents, of the commissioning board items — including a later item whose
  filename describes a defect on this surface; and its harness-loaded memory
  index. Its orchestrator read the `docs/SESSIONS.md` index tail through
  2026-10-16 (including the authoring run's one-paragraph summary) and the
  2026-10-16 session record's close section, and passed on no evaluative content
  beyond the pointer list and a one-line note naming a later shared staged-diff
  reader and staged real line numbers. Everything evaluative is in the sibling.

## What the work is

Landing commits (diff these; review the paths at HEAD):

- `c1cef10` (2026-10-05 18:56 UTC) — publishscan: read the tip and staged planes
  NUL-delimited (260/120); landed in merge `e71d40c` (2026-10-05 18:58 UTC)
- `4dfaf8d` (2026-10-05 21:52 UTC) — tools: read git's quoted paths correctly in
  the staged-plane guards (115/260); landed in merge `68e9baf` (2026-10-05
  21:53 UTC)

Delta paths: `tools/report.py` (`unquote_c`, `diff_header_path`, `nul_paths`),
`tools/conflictscan.py`, `tools/leakscan.py`, `tools/secretscan.py`,
`tools/board.py`, `tools/harvestscan.py`, `tools/publishscan.py`, their tests
(`test_report.py`, `test_conflictscan.py`, `test_leakscan.py`,
`test_secretscan.py`, `test_board.py`, `test_harvestscan.py`,
`test_publishscan.py`) and `tools/README.md`.

**Later commits on the same surfaces — not this delta; do not attribute them to
it.** The staged-diff path in three of these guards was rewritten after landing,
so the delta's header reader may no longer be the code that runs. Review the
delta's own claims at the landing commits and at HEAD, and say which a finding
rests on:

- `39a74b9` (2026-10-16) — read the staged diff by its structure, not by how a
  line looks (115/280): a shared staged-diff reader in `report.py`
  (`parse_added_lines`, `staged_added`) now used by conflictscan, leakscan and
  secretscan
- `f4afb7a` (2026-10-16) — conflictscan and leakscan report a staged finding at
  its real file line
- `f9ccba8`, `72a68cc`, `1c24781`, `e3e8a4f` (2026-10-16) — edit pins in
  `test_report.py` for sizescan, indexscan and licenscan, not the path readers

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code, tests
and live behaviour. The lenses organise it; they do not bound it. Non-goals are the
only narrowing and are themselves reviewable.

For every place in the six tools where a path comes from git, at HEAD: which git
command, with `-z` or not, with `-c core.quotePath=false` or not, through which
reader. Then drive file names through each plane in a scratch repo: non-ASCII
(composed and decomposed forms), a space, a trailing space, a tab, a newline, a
double quote, a backslash, a leading dash, a name that is only digits, bytes that
are not UTF-8, a name beginning `b/` or containing ` b/`, and a file whose added
content line begins `++ b/` (it prints as `+++ b/…` in a diff). Repeat under
repository and user config the guards do not pin: `diff.noprefix`,
`diff.mnemonicPrefix`, `diff.srcPrefix`/`dstPrefix`, `color.diff=always`,
`diff.external`, `core.precomposeUnicode`. For each: is the file read, under its
real name, and does a planted marker, leak or secret in it get reported? Whether
`unquote_c`'s UTF-8 `replace` decoding and `nul_paths`' surrogate-escape decoding
give the same string for the same non-UTF-8 name, and whether either can then be
opened. Whether publishscan's own NUL reader and `report.nul_paths` are two
readers of one thing. **Non-goal:** the choice to read the staged header with
`core.quotePath=false` rather than a `-z` path list joined to the diff.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself first.
   Among them: that git's quoting rules are exactly the set `unquote_c` undoes;
   that the default `b/` prefix is the only one a guard will meet; that a
   trailing TAB on a header always and only marks a name with a space.
2. **Correctness & quality.** Read the three helpers, each call site, and the new
   tests whole; diff both commits. Build the per-plane, per-name table above at
   the landing merges and at HEAD. Check that the tests fail on the pre-change
   code as the commit bodies say, and that the fixtures pin the git config they
   depend on.
3. **Completeness / harvest.** Every other place in `tools/` and `instruments/`
   that reads paths from git output without `-z` (`grep -n "ls-files\|diff
   --cached\|ls-tree\|--name-only" tools/*.py instruments/*`); `tools/filewalk.py`;
   `tools/README.md`'s description of the planes. Did the fix reach every reader
   of the class, or only the ones the triggering case touched?
4. **Security & privacy** — mandatory. A file name is attacker-controlled input
   to a guard: hunt the name that makes a blocking guard skip a file, read a
   different file, or crash into an exit code that passes. Check that names are
   never passed to a shell and that a leading dash cannot become a git option.
   `/security-review` is discharged by grounds (a landed delta; the pending diff
   is not the work) — say so, and deliver the code-altitude read by hand against
   the OWASP catalogue.

## Re-run obligation

Re-run, do not read. Lift floor invocations from `.githooks/pre-commit`,
`tools/floor.py` and `.github/workflows/ci.yml` rather than guessing.

- `python3 -m unittest tools.test_report tools.test_conflictscan
  tools.test_leakscan tools.test_secretscan tools.test_board
  tools.test_harvestscan tools.test_publishscan -v` at HEAD, and at `68e9baf` in
  a scratch clone
- the "fails on old code" claim: the new tests run against `c1cef10^` and
  `4dfaf8d^` in a scratch clone
- the byte-identity claim, re-driven on this repo's tree and staged planes only
  (the commits' sibling-repo runs are not re-run — never point a scanner at other
  repos on the machine; say so)
- each touched tool's `--selftest`; the floor on both planes at HEAD; the full
  Python suite once, foreground

## House rules for this run

- Name the worktree you work in. Run no git command that writes there; read-only
  git is fine. Fixture repos with hostile names, config variations and older
  checkouts go in a private area under your session scratchpad, named by your
  prefix; never set global git config.
- One heavy process at a time on a shared machine: the full suite at most once, in
  the foreground. Never point a scanner at any other repo on the machine.
- `/security-review` reads the session's pending diff: discharge it by grounds for
  this landed delta, or keep the tree clean whenever you spawn it.
- Dates absolute ISO 8601 from `date -u`. Prose wrapped at ≤ 100 columns. NZ
  English. Never quote a secret, placeholder token, email address or personal
  detail — this repo is PUBLIC; describe and locate instead.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the deferred material lives in the sibling .deferred.md, held apart under the rule-1 split and opened only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`,
`docs/sessions/`, every prior verdict in `docs/reviews/`, the queue pointer, this
brief's sibling `docs/reviews/2026-10-16-1551-git-quoted-paths-cold.deferred.md`,
the commissioning items `260` and `280` in
`docs/roadmap/115-guardrail-architecture-mike-commissioned/`, and `120` in
`docs/roadmap/260-sharing-public-since-2026-07-10-adr-0005/` (each barred as a
section).

Sweep with `python3 tools/coldsweep.py --root <your worktree> --also-exclude
docs/roadmap/160-doctrine-review-owed/760-rule-4-cold-pass-queued-quoted-paths.md
--also-exclude docs/reviews/2026-10-16-1551-git-quoted-paths-cold.deferred.md
--also-exclude docs/roadmap/115-guardrail-architecture-mike-commissioned
--also-exclude docs/roadmap/260-sharing-public-since-2026-07-10-adr-0005
<pattern>`; `--include-barred` only with disclosure. Reading the delta is never
barred.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list. Then
append your verdict below a `---` divider in THIS file: provenance repeated (how
you were spawned, your tier, what you read), per-lens answers, the standing
checklist V1–V7 each answered or discharged with grounds, the per-plane name
table, findings with stable IDs (prefix `QP`: `QP1`, `QP2`, …) and severities
(MAJOR / MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL line
with counts, a re-run ledger, and a follow-up checklist. Then STOP and commit
phase 1 unrevised before opening the sibling.

**Phase 2.** Open the sibling; append `### Reconcile` beneath your verdict:
per-finding notes against the seeded questions and the intent record, any finding
formed at reconcile marked as such, and the overall line restated. Never revise
phase-1 text. Then fold the sibling in below the reconcile and delete it.

Findings on self-authored doctrine are the principal's to decide (rule 3; a
guard is doctrine by function): record all, apply nothing; counsel per finding is
welcome, labelled and kept beneath it.
