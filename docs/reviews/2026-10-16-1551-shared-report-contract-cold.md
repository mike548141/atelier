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

---

# Verdict — phase 1

**Run:** 2026-10-17 UTC, in worktree `/Users/mike/worktrees/atelier-review-1017`
(branch `review-1017`, HEAD `c68f063` at the start of the pass, `7d06d9d` by its
end — the orchestrator's commits of sibling passes; nothing of mine). Phase-1
findings written before any barred material was opened.

## Provenance, repeated

- **Reviewer:** a cold `claude-fable-5-1` subagent (the principal-named review
  tier, checked at selection), spawned on 2026-10-17 UTC by a Fable orchestrator
  that authored none of the delta and none of this brief, and that holds the
  deferred sibling in a context partition until these findings are committed.
  The reviewer formed every finding and every severity; the orchestrator formed
  none. This session was started and instructed by neither the delta's author
  (the 2026-10-05 queue run) nor the brief-writer, so rule 4's criterion holds.
- **What I read before writing:** this brief; `docs/method/REVIEW.md` whole; the
  landing commit's `--stat`, subject and full diff; `tools/report.py` and
  `tools/test_report.py` at HEAD and at `ffabef3`; `tools/README.md`'s scanner
  sections and the `report.py` section at HEAD; the exit, warn and advisory-count
  parts of `tools/floor.py`; `.githooks/pre-commit`; the invocation lines of
  `.github/workflows/ci.yml`; the fetch lines of the child `floor.yml` template;
  the hand-spelled contract lines of `pointerscan`, `board`, `stampscan`,
  `blockscan`, `signscan`, `publishscan`, `harvestscan`, `reviewscan`; the OSError
  handling of the scanning guards; `allowmarker.IgnoreFileError`; `coldsweep`
  output with every exclusion the brief lists (no `--include-barred`).
- ⚠️ **Exposure, disclosed.** My second git command, `git show ffabef3 --
  <paths>`, printed the landing commit's **message body** before the diff — a
  barred item (the author's own account) — because I stripped only the header
  lines, not the body. I cannot un-read it. What it told me, so the reader can
  weigh it: the author's list of cases it claims byte-identity on (real tree,
  four fixture trees, error cases, cap patched to 0 and 1, `--warn`, `--json`,
  `--staged`, `--disable`, `--check`, `--selftest`), that the pins also pass on
  the pre-change scanners, and that `pointerscan`/`board.py` were left out on
  purpose. I treated each as a claim to re-drive (the re-run ledger below), not
  as settled; no finding below rests on it, and RT1–RT3 came from probes the
  body does not mention. Nothing else barred was opened: no prior verdict, no
  session record, not the queue pointer, not the sibling, not the `115/` section.

## Lens 1 — approach and assumptions (named first, then attacked)

Load-bearing assumptions I name myself:

1. **Every per-guard difference is a parameter; no default can drift in.** True
   for the lines the helpers build (name, tally parts, noun, tail, indent,
   example path, exception tuple are all passed, none defaulted into a guard's
   output). It is **overstated** as a description of the delta: three guards
   (`licenscan`, `publishscan`, `reviewscan`) keep their own wording of the
   missing-root line and `reviewscan` its own per-path refusal, routed through
   `report.broken(name, text)` — so the "single source" has two mechanisms, a
   shared line and a shared prefix around a private line (RT6).
2. **Byte-identical output on the real tree and four fixture trees proves
   equivalence for every child.** It proves the branches those trees reach. I
   re-drove it wider (the ledger): 14 guards × 30–45 invocations each, old
   against new, including the cases the brief names. Zero behavioural
   differences; the only diffs are traceback frames on a forced exception.
   What it cannot prove is that the shared exit-2 paths are **reachable** — and
   for `cannot_read` they are not, in five of nine callers (RT1). Equivalence
   held; the contract the module documents did not.
3. **One shared module lowers the cost of a wrong edit.** Holds, because
   `test_report.py` pins each guard's lines as literals (and I confirmed the
   pins are grounded: they pass unchanged against the pre-change scanners). A
   wrong shared edit fails 14 pins before any child's CI sees it. The residual
   is the one the brief names: a wrong edit that *passes* the pins (a logic
   change in `exit_code`, say) reaches every child at its next run; the
   `test_exit_code_reads_truthiness` pin covers the int/list/bool cases only
   (RT8).
4. **The hook and CI planes read nothing but the exit code.** True for exit
   (`Result.failed` is `rc != 0` on enforced and warn-only checks), plus one
   printed line for the two advisory-count carriers. So an error that exits 1
   instead of 2 still blocks (RT4 is a misreport, not a bypass), and an error
   that exits 0 is the only dangerous class — which is exactly RT1 and RT2.
5. **A guard file is never copied alone.** True in practice (children check
   atelier out and run `tools/floor.py`; neither hook nor template vendors a
   file), and the delta is safe on that footing. The code and `floor.py` still
   *say* the opposite in eleven places (RT5).

**Was this the right problem, solved the right way?** Yes. Eleven identical
`main()` wrappers and ten copies of one stderr line were the vendored-policy
shape the registry exists to end, and the move is behaviour-preserving as
claimed. The non-goal (no finding IDs) was honest and is reviewed elsewhere.

## Lens 2 — correctness and quality

`report.py`'s delta helpers (`exit_code` through `suppressed_line`) read whole;
`test_report.py` read whole at both revisions; all fourteen scanner diffs read
line by line. Each call site passes what the old inline code computed; the
`--warn` short-circuit, the `(--warn …)` notice placement (`publishscan`'s
`print()` + line became one `print(WARN_NOTICE)` — same bytes), the
`breakdown`/`disabled` gating, and the `sizescan` `args.check and any(...)`
boolean all reproduce. The per-guard table:

| Guard | config-error tuple (before → after) | exit-2 paths (before = after) | `--warn` |
|---|---|---|---|
| conflictscan | `(IgnoreFileError,)` → same | root · git diff · absolute staged · missing path · cannot read | none |
| datescan | `(IgnoreFileError,)` → same | root · missing path · cannot read (**dead**, RT1) | findings 0; exit-2 paths precede it |
| harvestscan | no wrapper (before or after) | root only | warn-only by construction |
| indexscan | `(IgnoreFileError,)` → same; `ConfigError`, `OSError` inside `_main` | root · missing path · config · cannot read | findings 0; exit-2 paths precede |
| leakscan | `(IgnoreFileError,)` → same | terms path · `--require-terms` · unknown `--disable` · git diff · absolute staged · missing path; no root line (missing root surfaces as missing path) | none |
| licenscan | `(IgnoreFileError,)` → same | not a directory (own wording via `broken`) | none at `ffabef3` |
| linkscan | `(IgnoreFileError,)` → same | root · missing path · cannot read | none |
| pathscan | `(IgnoreFileError, FloorConfigError)` → same | root · missing path · cannot read | findings 0; exit-2 paths precede |
| publishscan | no wrapper; `BadIgnoreFile`/`RuntimeError` inside `run` | root (own wording) · bad ignore · git failure | findings 0; exit-2 paths precede |
| reviewscan | no wrapper | root (own wording) · each missing path (own wording) | none |
| secretscan | `(IgnoreFileError,)` → same | unknown `--disable` · git diff · absolute staged · missing path; no root line | none |
| sizescan | `(IgnoreFileError,)` → same | root · missing path · cannot read | `--check` gates instead |
| spellscan | `(IgnoreFileError,)` → same | root · missing path · cannot read (**dead**, RT1) | findings 0; exit-2 paths precede |
| wrapscan | `(IgnoreFileError,)` → same | root · missing path · cannot read (**dead**, RT1) | findings 0; exit-2 paths precede |

`--warn` never masks an exit 2: in every guard the refusals run before the warn
test, and the differential confirms `missing-root/warn` and `missing-path/warn`
exit 2 on all six warn-capable guards. `--json` key order is unchanged (the
JSON cases are byte-identical old against new). Over-cap and suppressed lines
print known zeros (pinned and observed).

**The pins' grounding** (the brief's question): the landed `test_report.py`
copied into the `ffabef3^` clone passes all 32 tests against the pre-change
scanners, so the literals were written from the old output, not from the new
helpers. V2 holds for that claim.

## Lens 3 — completeness and harvest

- `tools/README.md`'s `report.py` section is accurate for the delta; the
  per-scanner "Exit codes" sentences (about a dozen) stay hand-spelled (RT10).
- `docs/method/GUARDS.md` states no exit code and no `--warn` spelling —
  nothing to sweep there (discharged by grep for exit/warn/stderr).
- `tools/floor.py`: `WARN_MODE_FLAGS` untouched; its comment that *every*
  scanner with a warn form prints the shared notice is false for `stampscan`
  (RT6). The advisory-count line `floor.py` parses was not taken into
  `report.py` and now has two copies (`secretscan`, `licenscan` since
  `e3e8a4f`, 2026-10-16) — RT6.
- Unconverted guards still spelling the contract by hand: `pointerscan` (root
  and per-path refusals, its own `suppressed:` line, a different "path does not
  exist" shape — first path only, raw argument), `board.py` (`✗ board: root …`),
  `stampscan`, `blockscan`, `signscan`. README names the first two as
  deliberate; the rest are outside the floor registry.
- Left-out spellings (leakscan's clean head, indexscan's cap-less over-cap line,
  datescan's tally-less findings path): the right call for a
  behaviour-preserving part, and the test file says "pinned, not endorsed".
  Counsel: a later deliberate output change can unify them; none hides a defect.

## Lens 4 — security and privacy (mandatory)

`/security-review` is **discharged by grounds**: the work is a landed delta and
this session's pending diff is other reviewers' drafts (and this one); aiming
the scanner at it would read their briefs and scan none of the work. The read
below is by hand against the OWASP Top 10 / ASVS classes that bear on a CLI
guard: injection, path handling, output/log injection, sensitive data in error
output, and dependency/shadowing.

- **Silent bypass by exit code** — the brief's headline threat. Two live cases,
  both pre-existing, both now sitting behind a shared helper that claims to
  close them: an unreadable file on the two boundary guards (RT1) and a
  `--staged` scope spelled `./x` (RT2). Neither reaches the wired hook or CI
  plane (analysis in each finding).
- **Injection:** every subprocess is a list argv with no shell; nothing from the
  tree reaches a command line. Discharged.
- **Output / terminal injection:** `report.broken` writes its message raw.
  The house already treats control characters in config-authored text as a
  real class (floor.py FR3, ruled 2026-08-23; publishscan's ingest seam), and
  an `.xignore` glob is tracked config that lands by PR — RT3.
- **Sensitive data in error lines:** `cannot_read` prints a path and
  `strerror` only; `IgnoreFileError` prints the offending globs (config, not
  content); `TermsPathError` prints the term-list path, which is a
  home-directory path (RT9); `DiffReadError` — a later commit's — prints up to
  60 characters of a diff line (RT9). No error line prints scanned content
  from this delta's helpers.
- **Module shadowing:** probed. A planted `report.py` in the working
  directory, in the scanned tree and on `PYTHONPATH` is **not** loaded when a
  scanner runs as a script: the tools directory is inserted at `sys.path[0]`
  and no stdlib or site-packages module of that name exists on this machine.
  Discharged with that probe; the residual is a `report.py` planted *inside*
  the tools directory, which is the repo itself.
- **Design altitude:** the delta exposes nothing new and collects nothing; it
  narrows the surface where a wrong line could be written. No threat
  enumeration was recorded with the work — for a refactor of printed strings I
  do not raise that as a finding.

## Standing checklist V1–V7

- **V1 (no claim stronger than evidence):** the "behaviour-preserving" claim
  held under a wider re-drive than the author's; the module docstring's
  "the exit-2 stderr lines for … an unreadable file" is stronger than the
  code (RT1); "single-sourced" is slightly stronger than the delta (RT6).
- **V2 (re-run every live-proven claim):** re-run, not read — ledger below.
  All reproduce.
- **V3 (changed rule swept to every mirror):** the import was added without
  sweeping the "copyable alone" claims (RT5); README's exit-code sentences
  unswept (RT10). Child templates carry no scanner text to sweep.
- **V4 (one fact, one home):** two homes for the advisory-count line and
  about a dozen for the exit-code prose (RT6, RT10).
- **V5 (no internal contradiction):** code that imports three siblings beside
  comments saying it imports none (RT5); `floor.py`'s "every scanner prints
  this notice" beside `stampscan`'s different notice (RT6).
- **V6 (security on every review):** lens 4 above; `/security-review`
  discharged by grounds, hand read delivered.
- **V7 (rule-4 provenance in brief and verdict):** present in both; the
  exposure above is disclosed where a reader meets it.

## Findings

**RT1 — MODERATE.** The shared `cannot_read` exit-2 path is dead code in five
of its nine callers. On a tree holding an unreadable file (mode 000),
`secretscan`, `leakscan`, `datescan`, `spellscan` and `wrapscan` print
`✓ … clean` and exit 0; `conflictscan`, `indexscan`, `linkscan`, `pathscan` and
`sizescan` exit 2 as the contract says. Cause: the bounded-memory rewrites
(`8fbb341` 2026-09-19 for secretscan, `886524f` 2026-09-20 for the others)
wrapped each per-file read in `except OSError: return []`, documented as
matching a mid-walk race, which also swallows a never-readable file. Not
introduced by this delta — but the delta single-sourced the helper, documented
"an unreadable file" as one of the exit-2 lines in `report.py`'s docstring and
`README`'s `report.py` section, and pinned the helper's text while five callers
can never reach it. Plane analysis, why MODERATE not MAJOR: the hook runs the
boundary guards `--staged` (reads the diff, not files) and CI runs them on a
fresh checkout (everything readable), so no wired plane is bypassed; hand runs
and a child's subtree runs are. Counsel (labelled): count the swallowed files
on the `suppressed:` line and exit 2 when the count is non-zero, or state the
race exemption in the contract and drop the claim; the test is one
`chmod 000` fixture per guard.

**RT2 — MODERATE.** `--staged` scoping by `./sub`, `docs/../sub` or a
Windows-style path scans nothing and exits 0 with `✓ clean` on `secretscan`,
`leakscan` and `conflictscan` (probed at HEAD and in both revisions; `sub/`
on the same staged key exits 1). This is the silent-success class
`refuse_absolute_staged` exists to close, closed for the one spelling the
helper's docstring names. `README`'s own private-repo recipe
(`leakscan --staged tiki/`) is one `./` away from silent cover. Pre-existing;
the consolidation was the moment the helper's name promised more than its
test. Counsel: normalise each prefix (`posixpath.normpath`), refuse one that
is absolute or escapes the root after normalising, and print the number of
staged files in scope so a run that covered nothing says so.

**RT3 — MODERATE.** `report.broken` writes its message to stderr with control
characters intact, so `refuse_missing_paths`, `cannot_read` and every
`broken(name, str(e))` carry an ESC sequence from a path or an ignore-file glob
straight to the committer's terminal or the CI log (probed: `\x1b[2J\x1b[H`
survives). The `.xignore` file is tracked config that a PR can land, and
`allowmarker.load_ignore_globs` does not strip it. The house ruled this class
worth closing for `.atelier-floor.json` (floor.py FR3, 2026-08-23) and
`publishscan` closes it at its ingest seam; the shared module is now the one
place that closes it for all fourteen. Counsel: `CONTROL_CHARS_RE.sub("", …)`
in `broken()`, with a pin.

**RT4 — minor.** Exit 2 is not what a broken scan returns in two classes. (a)
An **unreadable ignore file** gives a traceback and exit 1 on `leakscan`,
`secretscan`, `licenscan` and `publishscan` (the load happens outside their
`OSError` guard), exit 2 on the rest. (b) Any **uncaught exception** gives
Python's traceback and exit 1 — the same code as "findings". `guarded_main`
re-raises by design and `test_guarded_main_never_swallows_other_errors` pins
that. Fail-closed in effect (`Result.failed` is `rc != 0`), misreported in
code. Counsel: catch `Exception` in `guarded_main`, print the traceback and
return 2 — that keeps "never swallow" (the trace is printed) and makes the
code honest; the pin would be reworded, which is the principal's call.

**RT5 — minor.** Eleven sites still say a scanner is self-contained or
copyable alone while it imports `filewalk`, `allowmarker` and now `report`:
`floor.py:719-720` (the design justification for the printed advisory line),
`test_floor.py:1294`, `linkscan.py:296`, `pathscan.py:174, 687, 1121`,
`datescan.py:501`, `spellscan.py:506`, `wrapscan.py:398`, `stampscan.py:451`,
`reviewscan.py:166`, `secretscan.py:67, 640`. The first two imports broke the
claim before this delta; the delta added the third without a sweep (V3/V5).
No behaviour risk — nothing vendors a file — but a reader of `floor.py:719`
is told a design reason that is no longer true.

**RT6 — minor.** The contract is not quite single-sourced. Three guards keep
private wording of the missing-root line (`licenscan` "not a directory",
`publishscan`/`reviewscan` "--root X is not a directory") and `reviewscan` a
per-path refusal, via `broken`; `stampscan` prints a warn notice that differs
from the one `floor.py` says every scanner prints ("drift not blocking");
`pointerscan` and `board.py` are unconverted (README says so); and the
advisory-count line `floor.py` parses now exists twice (`secretscan`,
`licenscan`, the latter from `e3e8a4f` 2026-10-16). Harvest, not defect:
each is a line a future shared edit will miss.

**RT7 — minor.** A target containing `..` resolves outside `--root` and is
scanned without a word (differential `dotdot-path`: exit 0 on eleven guards).
`resolve_targets` promises "never the caller's cwd"; nothing promises "never
outside the root", and the ignore file and anchors of the root then govern a
tree they were not written for — the same mismatch `010/110` closed for cwd.
Pre-existing. Counsel: refuse a resolved target that is not under the root
unless given absolute.

**RT8 — note.** `exit_code(blocking: object)` accepts anything: a generator or
an empty-but-truthy tally object returns 1, `None`, `""` or `0.0` return 0.
All nineteen call sites at HEAD pass an `int` or a `bool` (grepped), so no
live defect; the pin covers int/list/bool only. Counsel: type it `int | bool`.

**RT9 — note.** Two error lines carry local detail to stderr: `TermsPathError`
prints the term-list path (a home-directory path) and `DiffReadError`
(`39a74b9`, not this delta) prints up to 60 characters of a diff line. The
first is pre-existing and reaches CI only under `--require-terms`; the second
fires only on a diff git did not write. Named, not raised beyond a note.

**RT10 — note.** `tools/README.md` keeps about a dozen hand-spelled copies of
the exit-code contract (lines 242, 406, 472, 534, 663, 777, 910, 953, 1001,
1133, 1231, 1287, 1387 at HEAD) beside the new `report.py` section. Single-
sourcing the code was the natural moment to make the prose one stamped copy
with pointers (V4). Each copy is currently correct.

## Overall

**PASS-WITH-FINDINGS — 0 MAJOR · 3 MODERATE · 4 minor · 3 note.**

The delta does what it claims: byte-identical stdout, stderr and exit code on
every converted guard under a wider re-drive than the author's, pins grounded
in the old output, selftests and both floor planes green at HEAD. The findings
are about what the consolidation inherited and now vouches for — three
shared exit-2 promises that the code does not keep everywhere (RT1, RT2, RT4),
one house-ruled class it is now the right place to close (RT3), and claims the
import left stale (RT5, RT6).

## Re-run ledger

| Claim / step | How re-run | Result |
|---|---|---|
| `python3 -m unittest tools.test_report -v` at HEAD | worktree, `nice -n 10` | 70 tests OK |
| the same at `ffabef3` | scratch clone `RT/new` | passes (32 tests, the landed file) |
| pins pass against the pre-change scanners | landed `test_report.py` + `report.py` copied into clone `RT/old` at `ffabef3^` | 32 tests OK; copies removed after |
| byte-identity, 14 guards | `RT/rtdiff.py`: `ffabef3^` vs `ffabef3`, one guard at a time under `nice`; trees: clean, findings, suppressed, bad ignore file, unreadable file, unreadable ignore file, symlinks (good and broken), the real tree (clone `RT/new`); variants: `--json`, `--warn`, `--check`, `--staged` (with `sub/`, `./sub`, `docs/../sub`, a Windows path, an absolute path, not-a-repo), missing root (± `--warn`), missing path (± `--warn`), `../` path, absolute path, unknown `--disable`, no terms / `--require-terms` / bad `--terms`, `--expect` mismatch, cap patched to 0 and 1 (± `--json`), forced exception, `--selftest` | 0 behavioural differences across ~520 paired runs; only traceback frames differ on the forced exception |
| every converted scanner's `--selftest`; `floor.py --selftest` | HEAD, by path | all 15 exit 0 |
| the floor on both planes at HEAD | `floor.py --plane hook --root .` and `--plane ci --root .` | both exit 0 (CI board: 23 secretscan advisories, leakscan cover note) |
| full Python suite, once | `python3 -m unittest discover -s tools -p 'test_*.py'` under `nice`, foreground; moved to background by the harness at 600 s | see the line below the ledger |
| `import report` shadowing | planted `report.py` in cwd, scanned tree, `PYTHONPATH` | not loaded; no stdlib/site module named `report` |
| control characters through `broken` | in-process probe | passed through raw |
| coldsweep (`report\.py`, helper names, "copyable alone", the stampscan notice) | with the brief's three `--also-exclude`s, no `--include-barred` | 12 / 19 / 1 hits, all cited above |

Full suite result — **not readable, stated honestly.** The run completed and
the harness reported exit 0, but I had piped it through `tail -6`, so the
reported code is the pipe's and the `Ran N tests … OK` summary was lost
behind the subprocess output that flushed after it. The one permitted run is
spent, so I record the pass as **unverified** rather than claimed. Evidence that
does stand: `test_report` green at HEAD (70 tests), every selftest and both
floor planes green at HEAD, and the pushed floor on `main` is the all-clear the
house relies on. Owed: one `python3 -m unittest discover -s tools -p 'test_*.py'
> log 2>&1; echo $?` by whoever next holds the machine (follow-up below).

## Follow-up checklist (for the principal's decision — nothing applied)

- [ ] RT1 — decide: count-and-exit-2 for an unreadable file, or document the
      swallow and drop the claim (five guards, one fixture each)
- [ ] RT2 — normalise and refuse non-canonical `--staged` prefixes; print files
      in scope
- [ ] RT3 — strip control characters in `report.broken`
- [ ] RT4 — `guarded_main`: traceback + exit 2 on an uncaught exception; move
      the ignore-file load inside the `OSError` guard on four guards
- [ ] RT5 — sweep the eleven "copyable alone" sites (or make them true)
- [ ] RT6 — fold the three private root lines, stampscan's notice and the
      second `advisory_count_line` into `report.py`, or record why not
- [ ] RT7 — refuse a target that resolves outside `--root`
- [ ] RT8 — type `exit_code` as `int | bool`
- [ ] RT9 — nothing owed; noted
- [ ] RT10 — one stamped home for the exit-code prose in `tools/README.md`
- [ ] Re-run the full Python suite once with its summary captured to a file
      (this pass's run lost the summary to a pipe — ledger above)
