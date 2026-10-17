# Cold pass — licenscan's advisory tier, and the floor reading its count

**Pass type:** code cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection by whoever takes the pass.
**Status:** BRIEF ONLY — the review has NOT run. Written 2026-10-17 UTC by an Opus
brief-writer; the pass waits for a further cold Fable session that neither the
delta's author nor this brief-writer (nor its orchestrator) started or instructed.
Tier is checked at selection (rule 4).
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/840-rule-4-cold-pass-queued-licenscan-advisory-tier.md`.
**Why it earns a review:** a publish gate that may never be softened by a child now
lets a class of its findings through with exit 0, the floor's board gains a count read
back from that gate's output, and two registry docstrings that say what may be softened
were rewritten. All of it reaches every child at its next run.

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
  message body** (the author's own account, with a principal quote); the merge's
  re-merge diff, including its two code hunks; the subject, `--stat` **and message
  body** of the later commit on the same files (another pass's subject); two
  2026-10-16 briefs in full as templates; `docs/reviews/` filenames and
  filename-level greps (no prior verdict opened); the title lines of the
  commissioning board items; grep-hit lines naming licenscan in `docs/build/`; and
  its harness-loaded memory index. It did not open the intent record,
  `docs/SESSIONS.md`, `docs/sessions/`, `docs/ROADMAP-DONE.md` or
  `docs/method/REVIEW.md`. What its orchestrator read is the orchestrator's to
  disclose; it passed on an instruction file, three templates and a list of taken
  prefixes, and no evaluative content. Everything evaluative is in the sibling.

## What the work is

Landing commit (diff it; review the paths at HEAD, `b50db0c` or later):

- `e3e8a4f` (2026-10-16 15:35 UTC) — licenscan: make the warning real, and make two
  guard descriptions true; landed in merge `6acefc9` (2026-10-16 15:41 UTC)

**The merge is part of the delta.** Beyond board and record files, `6acefc9` itself
edits `tools/licenscan.py` and `tools/README.md` (a date in each); read it with
`git show --remerge-diff 6acefc9 -- tools/`.

Delta paths: `tools/licenscan.py` (the *two responses* docstring, the exit-code
table, `RESPONSE_*`, `ADVISORY_SEVERITIES`, `ADVISORY_COUNT_PREFIX`, `Finding`'s
`response` and `blocks`, `Report.blocking`/`advisory`, `advisory_count_line`,
`_render_advisory`, `render_human`, the `--json` fields, the exit code, the
selftest), `tools/floor.py` (licenscan's `advisory_count=True` and the docstrings of
the module and `Scanner` about what may be softened), `tools/pathscan.py` (its
STATUS docstring), `tools/test_licenscan.py`, `tools/test_floor.py`,
`tools/test_report.py`'s licenscan pins, and `tools/README.md`'s licenscan section.

**Later commit on the same files — not this delta; do not attribute it to it.**

- `dc0ed0e` (2026-10-16) — floor: scope the advisory count to its scanner, pin
  three more unsoftenable checks (its own pass, 160/860); it rewrites the count
  reader this delta first relied on and touches one comment in `tools/licenscan.py`

Review the count path at HEAD; to judge this delta as landed, run `e3e8a4f` too.
The commit's parent is `2e2da81`, the base of two sibling commits (`f4afb7a`,
`72a68cc`) that also touch `tools/README.md` and, for one, `tools/test_report.py`.

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code, tests
and live behaviour. The lenses organise it; they do not bound it. Non-goals are the
only narrowing and are themselves reviewable.

Enumerate every finding licenscan can raise at HEAD — each kind, the severity each
code path assigns, and the response it therefore gets — and compare that list with
every place that states which findings block (module docstring, README tables,
selftest, tests, `floor.py`'s comments). Then every caller that reads licenscan's
exit code or `--json`: the floor on both planes, CI, any publish or pre-flip gate,
`docs/build/REPO-STANDARD.md`'s publish-time use, a child's hook; for each, what it
did with a `medium` finding before and what it does now. Check that the advisory
count line is printed on every path that can exit 0 or 1 (and what happens at exit
2), that the floor reads it from the right scanner's output, and what the board shows
when the line is missing. On `floor.py`: the docstrings now name an exception to
"boundary checks have no advisory form" — check the registry entry that exception
points at, and whether "may never be softened" still has one meaning across the
registry, `docs/build/templates/CONTRIBUTING.md` and `docs/method/GUARDS.md`. On
`pathscan.py`: check each fact its new STATUS text states against the registry and
`ci.yml`. **Non-goals:** the principal's choice that the warning be real (quoted in
the delta) — but which findings were placed in the advisory class, and how, is in
scope.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself first.
   Among them: that severity is the right key for response; that "a severity not
   named advisory blocks" is fail-safe in practice; that a count line on stdout is
   a sound contract between two tools; that an advisory nobody is forced to read
   is still a control.
2. **Correctness & quality.** Read `tools/licenscan.py` whole at HEAD and diff
   `e3e8a4f` plus the merge's hunks. Build the kind → severity → response → exit
   table from the code, not the prose, and set it beside each prose table. Check
   whether the new tests would fail on `e3e8a4f^` for the reason each test names,
   and whether the `--json` change keeps every old field's meaning.
3. **Completeness / harvest.** Every surface still calling these findings a
   "warn", or stating licenscan's exit codes or what it blocks: the README's other
   sections, `docs/build/`, `docs/method/`, the templates, `CHANGELOG.md`, skills.
   Every surface listing which checks may be softened, against the registry at
   HEAD.
4. **Security & privacy** — mandatory. Licence findings are a publication-safety
   boundary for a public repo. Hunt for a finding that a person would want to stop
   a publish but that now exits 0 — an unknown declaration hiding a copyleft
   licence, a custom LICENSE, a dual-licence expression, an allow-marker reach —
   and for any way a file's content can change the board's count (the line is read
   back from output that echoes repo-controlled paths and messages). Fixtures from
   synthetic values only. `/security-review` is discharged by grounds (a landed
   delta; the pending diff is not the work) — say so, and deliver the code-altitude
   read by hand against the OWASP catalogue.

## Re-run obligation

Re-run, do not read. Lift floor invocations from `.githooks/pre-commit`,
`tools/floor.py` and `.github/workflows/ci.yml` rather than guessing.

- `python3 -m unittest discover -s tools -p 'test_licenscan.py' -v`, the same for
  `test_floor.py`, `test_report.py` and `test_pathscan.py`; `--selftest` for
  `licenscan`, `floor` and `pathscan`
- licenscan at `e3e8a4f^`, `e3e8a4f` and HEAD in a scratch clone, over synthetic
  fixture repos covering every kind in your table: compare stdout, exit code and
  `--json`
- the floor's board on a fixture with advisory licence findings, at `e3e8a4f` and
  at HEAD (so `dc0ed0e`'s change is not charged to this delta)
- the floor on both planes at HEAD; the full Python suite once, foreground

## House rules for this run

- Name the worktree you work in. Run no git command that writes there; read-only
  git is fine. Fixture repos, older checkouts and probes go in a private clone
  under your session scratchpad, named by your prefix.
- One heavy process at a time on a shared machine: the full suite at most once, in
  the foreground. Never point a scanner at any other repo on the machine — the
  delta's estate-wide blast-radius claim is not re-driven that way; reason about it
  from fixtures.
- `/security-review` reads the session's pending diff: discharge it by grounds for
  this landed delta, or keep the tree clean whenever you spawn it.
- Never open another `docs/reviews/2026-10-17-*` brief — it is another pass's
  framing.
- Dates absolute ISO 8601 from `date -u`. Prose wrapped at ≤ 100 columns. NZ
  English. Never quote a secret, placeholder token, email address or personal
  detail — this repo is PUBLIC; describe and locate instead.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the deferred material lives in the sibling .deferred.md, held apart under the rule-1 split and opened only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`,
`docs/sessions/`, every prior verdict in `docs/reviews/`, the queue pointer, this
brief's sibling `docs/reviews/2026-10-17-0955-licenscan-advisory-tier-cold.deferred.md`,
the message bodies of `e3e8a4f` and `dc0ed0e` (read subject, stat and diff only),
the queue pointer `160/860`, and items `290` and `320` in
`docs/roadmap/115-guardrail-architecture-mike-commissioned/` (the commissioning
item, and a follow-up filed at the same merge).

Sweep with `python3 tools/coldsweep.py --root <your worktree> --also-exclude
docs/roadmap/160-doctrine-review-owed/840-rule-4-cold-pass-queued-licenscan-advisory-tier.md
--also-exclude docs/reviews/2026-10-17-0955-licenscan-advisory-tier-cold.deferred.md
--also-exclude
docs/roadmap/160-doctrine-review-owed/860-rule-4-cold-pass-queued-advisory-count-per-scanner.md
--also-exclude
docs/roadmap/115-guardrail-architecture-mike-commissioned/290-three-guards-describe-a-response-tier-their-code-lacks.md
--also-exclude
docs/roadmap/115-guardrail-architecture-mike-commissioned/320-three-small-floor-test-and-contract-gaps.md
<pattern>`; `--include-barred` only with disclosure. Reading the delta is never
barred.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list. Then
append your verdict below a `---` divider in THIS file: provenance repeated (how
you were spawned, your tier, what you read), per-lens answers, the standing
checklist V1–V7 each answered or discharged with grounds, the kind → response
table, findings with stable IDs (prefix `LA`: `LA1`, `LA2`, …) and severities
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
