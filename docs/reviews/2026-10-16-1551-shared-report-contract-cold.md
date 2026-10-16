# Cold pass — one shared exit and reporting contract for fourteen guards

**Pass type:** code cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection by whoever takes the pass.
**Status:** BRIEF ONLY — the review has NOT run. Written 2026-10-16 UTC by an Opus
brief-writer; the pass waits for a further cold Fable session that neither the
delta's author nor this brief-writer (nor its orchestrator) started or instructed.
Tier is checked at selection (rule 4).
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/730-rule-4-cold-pass-queued-the-report-contract.md`.
**Why it earns a review:** the exit code is the only thing the floor and every
child's CI read from a guard. This delta moved fourteen guards' exit paths and
report lines into one module and claimed the move changed nothing; a slip there
turns a broken scan into a pass across the whole estate at its next run.

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
  brief-writer read: the queue pointer in full; the landing commit's subject,
  `--stat`, the `report.py` diff, one converted scanner's diff, **and the message
  body** (the author's own account); the subjects and `--stat` of later commits on
  the same files; `REVIEW.md` rules 1–4, the four lenses, the checklist and the
  lifecycle; the ask halves of two 2026-10-04 briefs as templates; `docs/reviews/`
  filenames and filename-level greps (no prior verdict opened); the names, not
  contents, of the commissioning board items; and its harness-loaded memory index.
  Its orchestrator read the `docs/SESSIONS.md` index tail through 2026-10-16
  (including the authoring run's one-paragraph summary) and the 2026-10-16 session
  record's close section, and passed on no evaluative content beyond the pointer
  list and a one-line note naming four later changes to these files. Everything
  evaluative is in the sibling.

## What the work is

Landing commit (diff it; review the paths at HEAD):

- `ffabef3` (2026-10-05 13:55 UTC) — tools: single-source the scanners' exit
  contract and report lines (115/080 p3); landed in merge `2472696` (2026-10-05
  14:08 UTC)

Delta paths: `tools/report.py` (new), `tools/test_report.py` (new),
`tools/README.md`, and the fourteen converted scanners: `conflictscan`,
`datescan`, `harvestscan`, `indexscan`, `leakscan`, `licenscan`, `linkscan`,
`pathscan`, `publishscan`, `reviewscan`, `secretscan`, `sizescan`, `spellscan`,
`wrapscan` (each `tools/<name>.py`). `pointerscan` and `board.py` were left out.

**Later commits on the same files — not this delta; do not attribute them to
it.** `report.py` has grown from about 170 lines to about 400 since landing.
Review the delta's helpers (`exit_code` to `suppressed_line`) at HEAD; treat the
rest as context:

- `ded8d32` (2026-10-05) — finding IDs: `finding_id`, `with_id`,
  `finding_dicts` (its own pass, 160/750); `db1aa4d` (2026-10-05) — marker kinds
  in licenscan, sizescan, pointerscan (160/750)
- `89ff0d8`, `c1cef10` (2026-10-05) — publishscan `--history` and NUL-delimited
  planes (160/740, 160/760); `4dfaf8d` (2026-10-05) — `unquote_c`,
  `diff_header_path`, `nul_paths` (160/760)
- `39a74b9` (2026-10-16) — a shared staged-diff reader, `parse_added_lines` and
  `staged_added` (115/280); `f4afb7a` (2026-10-16) — staged findings at their real
  file line
- `f9ccba8`, `72a68cc` (2026-10-16) — sizescan's hatches and its size advisory
  removed (115/270); `1c24781` (2026-10-16) — indexscan's date-mismatch kind;
  `e3e8a4f` (2026-10-16) — licenscan's warning made real (an advisory tier). All
  four edit `test_report.py` pins.

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code, tests
and live behaviour. The lenses organise it; they do not bound it. Non-goals are the
only narrowing and are themselves reviewable.

Whether, for each of the fourteen guards at `ffabef3`, every exit path and every
line it printed before is reproduced exactly — and whether the exit code is still
right in the cases nobody tested. Cases: a config error of a class the guard did
not list in its `config_errors` tuple; an unexpected exception (Python's default
uncaught-exception exit is 1, the same as "findings"); `--warn` combined with a
missing root, a missing path, an unreadable file and a failed `git diff` (exit 2
must survive `--warn`); `exit_code` given a value whose truthiness misleads (an
empty tally object, a generator, a count that is a string); a path containing
`..`, a symlink, or a broken symlink in `resolve_targets` and
`refuse_missing_paths`; `--staged` with `./x`, `x/../y` or a Windows-style path;
the over-cap and suppressed lines when counts are zero (known zeros printed);
`--json` output order. Whether the guards that keep their own spelling were the
right ones to leave out, and whether `pointerscan` and `board.py` now diverge from
the contract. Whether a guard file can still be run or vendored alone now that it
imports `report` (search the repo and the child templates for any place a single
scanner file is copied without its siblings). **Non-goal:** the later decision,
in `ded8d32`, to add finding IDs — it has its own pass.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself first.
   Among them: that every per-guard difference is a parameter and no default can
   drift in; that byte-identical stdout, stderr and exit code on the real tree and
   four synthetic trees proves equivalence for every child; that one shared module
   lowers rather than raises the cost of a wrong edit, given that every guard and
   every child now fails together.
2. **Correctness & quality.** Read `report.py`'s delta helpers and
   `test_report.py` whole; diff `ffabef3` per scanner. Build a table: guard, its
   `config_errors` tuple before and after, every exit-2 path before and after,
   `--warn` behaviour on each. Check whether `test_report.py`'s pins were written
   from the old scanners' real output or from the new helpers (the commit says the
   pins also pass on the pre-change scanners: re-run that).
3. **Completeness / harvest.** `tools/README.md`'s contract section;
   `docs/method/GUARDS.md` and `tools/floor.py` wherever they state exit codes or
   the `--warn` spelling (`WARN_MODE_FLAGS`); the advisory-count line `floor.py`
   parses from secretscan; any scanner not converted that still spells the
   contract by hand (`pointerscan`, `board.py`, `stampscan`, `blockscan`,
   `signscan`, `publishscan`'s own paths).
4. **Security & privacy** — mandatory. A guard that exits 0 or 1 when it should
   exit 2 is a silent bypass of every boundary the floor holds. Check also that
   error lines never echo file content (a secret on an unreadable line, a term
   from the machine-local list) and that `import report` cannot be shadowed by a
   file in the scanned tree or the working directory. `/security-review` is
   discharged by grounds (a landed delta; the pending diff is not the work) — say
   so, and deliver the code-altitude read by hand against the OWASP catalogue.

## Re-run obligation

Re-run, do not read. Lift floor invocations from `.githooks/pre-commit`,
`tools/floor.py` and `.github/workflows/ci.yml` rather than guessing.

- `python3 -m unittest tools.test_report -v` at HEAD, and at `ffabef3` in a
  scratch clone
- the byte-identity claim, re-driven at landing: for each of the fourteen
  guards, `ffabef3^` against `ffabef3` on the repo tree and on your own fixture
  trees (clean, findings, suppressed, bad ignore file, missing root, unreadable
  file, `--warn`, `--json`, `--staged`, a forced unexpected exception) — compare
  stdout, stderr and exit code
- every converted scanner's `--selftest`; `python3 tools/floor.py --selftest`
- the floor on both planes at HEAD; the full Python suite once, foreground

## House rules for this run

- Name the worktree you work in. Run no git command that writes there; read-only
  git is fine. Probes and older checkouts go in a private clone under your
  session scratchpad, named by your prefix.
- One heavy process at a time on a shared machine: the full suite at most once, in
  the foreground; the fourteen-guard differential run one guard at a time, under
  `nice`. Never point a scanner at any other repo on the machine.
- `/security-review` reads the session's pending diff: discharge it by grounds for
  this landed delta, or keep the tree clean whenever you spawn it.
- Dates absolute ISO 8601 from `date -u`. Prose wrapped at ≤ 100 columns. NZ
  English. Never quote a secret, placeholder token, email address or personal
  detail — this repo is PUBLIC; describe and locate instead.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the deferred material lives in the sibling .deferred.md, held apart under the rule-1 split and opened only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`,
`docs/sessions/`, every prior verdict in `docs/reviews/`, the queue pointer, this
brief's sibling
`docs/reviews/2026-10-16-1551-shared-report-contract-cold.deferred.md`, and the
commissioning item `080` with its neighbours in
`docs/roadmap/115-guardrail-architecture-mike-commissioned/` (barred as a section).

Sweep with `python3 tools/coldsweep.py --root <your worktree> --also-exclude
docs/roadmap/160-doctrine-review-owed/730-rule-4-cold-pass-queued-the-report-contract.md
--also-exclude docs/reviews/2026-10-16-1551-shared-report-contract-cold.deferred.md
--also-exclude docs/roadmap/115-guardrail-architecture-mike-commissioned
<pattern>`; `--include-barred` only with disclosure. Reading the delta is never
barred.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list. Then
append your verdict below a `---` divider in THIS file: provenance repeated (how
you were spawned, your tier, what you read), per-lens answers, the standing
checklist V1–V7 each answered or discharged with grounds, the per-guard table,
findings with stable IDs (prefix `RT`: `RT1`, `RT2`, …) and severities (MAJOR /
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
