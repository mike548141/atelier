# Cold pass — the floor's advisory count scoped to its scanner, and three more unsoftenable pins

**Pass type:** code cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection by whoever takes the pass.
**Status:** BRIEF ONLY — the review has NOT run. Written 2026-10-17 UTC by an Opus
brief-writer; the pass waits for a further cold Fable session that neither the
delta's author nor this brief-writer (nor its orchestrator) started or instructed.
Tier is checked at selection (rule 4).
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/860-rule-4-cold-pass-queued-advisory-count-per-scanner.md`.
**Why it earns a review:** it changes how the floor reads the one number that carries a
scanner's non-blocking findings onto the board (a misread is either a silent zero or a
false count on every child's floor), and it widens the set of checks pinned as having no
advisory form — the line between what a child may soften and what it may not.

## Spawn provenance

- **Author of the work under review:** the queue run whose intent record is dated
  2026-10-16 15:01 UTC (an Opus orchestrator with dispatched workers; the pointer counts
  the worker's output as the run's authorship; the commit's trailer names a Sonnet
  model). Not opened here.
- **Who wrote this brief:** an Opus subagent (`claude-opus-5-5`) dispatched on 2026-10-17
  by the Mike-opened Fable review session working in worktree `atelier-review-1017`, on
  Mike's 2026-10-16 answer that a fresh Opus session writes these briefs. It authored
  none of the delta. It is **off-tier for review, disclosed: it forms no finding and
  writes no severity**, and it stops after this brief and its sibling.
- **Who takes the review:** a further cold Fable session, not yet started, that passes
  rule 4's criterion. If it runs as reviewer-plus-orchestrator, rule 4's off-tier
  conditions apply and are disclosed in the claim, the pointer and the verdict. The
  reviewer repeats its own provenance in its verdict.
- ⚠️ **Exposure, disclosed** (rule-2 material met before writing). This brief-writer
  read: its instruction file; the four queue pointers it was assigned (160/860–890) in
  full, and 160/500 in full as the shape of an append line (including that item's
  result line); the staging directory's file listing, and the first 50 lines of one
  peer brief of this batch (160/850) and its append, for shape; the landing commit's
  subject, `--stat`, full diff **and message body** (the author's own account); later-
  commit checks on the delta paths (none found); `tools/floor.py` around the `Scanner`
  fields, the registry's `board` entry and the advisory-count contract comment; three
  templates in full; `docs/reviews/` filenames and filename-level greps (no prior
  verdict opened); and grep-hit lines from a `coldsweep` sweep for the unsoftenable
  vocabulary, which included single lines of the commissioning items 115/290 and
  115/320, of other board items, of `CHANGELOG.md`, of ADR 0008 and of tools. It also
  holds its harness-loaded memory index, and, writing the other three briefs of its
  set, read those deltas' diffs, message bodies and parts of their code (instruments
  only). It did not open the intent record,
  `docs/SESSIONS.md`, `docs/sessions/`, `docs/ROADMAP-DONE.md` or
  `docs/method/REVIEW.md`. What its orchestrator read is the orchestrator's to disclose;
  it passed on an instruction file, three templates and a list of taken prefixes, and
  no evaluative content. Everything evaluative is in the sibling.

## What the work is

Landing commit (diff it; review the paths at HEAD, `2f9cfe4` or later):

- `dc0ed0e` (authored 2026-10-16 16:02 UTC, committed 16:17 UTC) — floor: scope the
  advisory count to its scanner, pin three more unsoftenable checks. A cherry-pick of
  the worker's `fe4f20d`; it reached `main` directly, ahead of `783bdff` (the board
  commit that queued this pass).

Delta paths:

- `tools/floor.py` — `advisory_count_rx` (replacing `ADVISORY_COUNT_RX`),
  `_read_advisory_count`'s new signature and last-match rule, its one call site in
  `run`, the `Scanner.advisory_count` comment, and `_selftest`'s unsoftenable list
- `tools/test_floor.py` — the module docstring's item 2, `RegistryTest.UNSOFTENABLE`
  and its two tests, and the `AdvisoryCountContract` additions
- `tools/licenscan.py` — one comment naming the reader

No later commit touches these three files (checked with `git log dc0ed0e..HEAD`);
confirm that at your HEAD. The count lines the reader consumes are built by
`advisory_count_line` in `tools/secretscan.py` and `tools/licenscan.py`; those builders
are not the delta, but the contract between them and the reader is.

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code, tests and
live behaviour. The lenses organise it; they do not bound it. Non-goals are the only
narrowing and are themselves reviewable.

Probe, at least:

- **The reader against every writer.** For each registered scanner with
  `advisory_count=True`, derive from its source every line it can print to stdout, in
  order, on every exit path (clean, advisory-only, blocking, over-cap, stale marker,
  error). Is the count line always present, always last of its kind, and always in the
  exact wording the new whole-line pattern demands? What does a run that blocks early
  print?
- **What text a scanner does not control.** Paths, finding excerpts and marker
  reasons reach stdout. Which of them can contain a newline, a leading-space run, or
  the scanner's own name followed by the contract wording? Build cases from synthetic
  file names, including ones that place a whole contract-shaped line before *and*
  after the real one.
- **The last-match rule.** Is "the count is printed after every finding line" true of
  every writer at HEAD, and is that ordering pinned by any test or only asserted in a
  comment?
- **The `-1` signal.** A reworded writer now yields `-1` rather than a misread. Trace
  where `-1` lands (the board, the renderers, any exit code) and whether a child sees
  it as loud.
- **The unsoftenable set.** Seven names now appear in two hand-written lists (the
  selftest and the test class). Compare both with the registry at HEAD, with
  `floor.py`'s own docstring on which checks have no advisory form, with
  `tools/README.md`, `docs/method/GUARDS.md`, `docs/method/SECRETS.md` and ADR 0008's
  account of what may re-baseline. Which statement is now authoritative, and do the
  others agree?
- **The config door.** The new test asserts a child asking for an advisory state on any
  of the seven is a `ConfigError`. Is that rejection the registry pin itself, or a
  separate path that could diverge?

**Non-goals:** the decision that boundary and integrity checks have no advisory form at
all (a standing ruling). Whether the new list is complete, and whether its wording
matches that ruling, are in scope.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself first. Among
   them: that a scanner's captured stdout is the only text the reader sees; that a
   printed line is a stable enough contract between self-contained tools; that
   hand-written pin lists catch drift better than a derived one.
2. **Correctness & quality.** Diff `dc0ed0e` on the three paths and read
   `_read_advisory_count`, its call site and the writers whole. Build the writer table
   from *Scope*. Check the regex against `re.MULTILINE` anchoring, trailing `\r`, tabs
   versus spaces, the em dash as a non-ASCII literal, and output decoded with
   `errors="replace"`.
3. **Completeness / harvest.** Every surface that still names `ADVISORY_COUNT_RX`, the
   old unanchored wording, or the old four-name unsoftenable list; the `CHANGELOG.md`;
   whether children reading the floor at `main` need anything to change.
4. **Security & privacy** — mandatory. The count is how advisory secret findings reach
   the board. Can a committed file name make the board under-report a real advisory
   count, or hide a blocking finding behind a plausible count? Synthetic values only;
   never paste a key-shaped literal into the verdict, describe its shape.
   `/security-review` is discharged by grounds (a landed delta; the pending diff is not
   the work) — say so, and do the code-altitude read by hand against the OWASP
   catalogue.

## Re-run obligation

Re-run, do not read. Lift floor invocations from `.githooks/pre-commit`,
`tools/floor.py` and `.github/workflows/ci.yml` rather than guessing.

- `python3 -m unittest tools.test_floor -v`; `python3 tools/floor.py --selftest`;
  `python3 tools/secretscan.py --selftest` and `python3 tools/licenscan.py --selftest`
- the old-versus-new claim, re-driven in a scratch clone: `dc0ed0e^` against `dc0ed0e`
  on a temporary tree whose file names imitate the count line, recording the count each
  reader returns
- your own crafted outputs from *Scope*, fed to `_read_advisory_count` at HEAD
- mutation: in the scratch clone, give one of the seven an advisory form and confirm
  which tests fail
- the floor on both planes at HEAD (`python3 tools/floor.py --plane ci --root .`, and
  the hook plane as `.githooks/pre-commit` invokes it); the full Python suite once,
  foreground

## House rules for this run

- Name the worktree you work in. Run no git command that writes there; read-only git is
  fine. Probes, mutated copies and older checkouts go in a private clone under your
  session scratchpad, named by your prefix.
- One heavy process at a time on a shared machine: the full suite at most once, in the
  foreground. Never point a scanner at any other repo on the machine. Never run an
  installed tool by bare name from `PATH`.
- `/security-review` reads the session's pending diff: discharge it by grounds for this
  landed delta, or keep the tree clean whenever you spawn it — never with this brief or
  its sibling dirty.
- Dates absolute ISO 8601 from `date -u`. Prose wrapped at ≤ 100 columns. NZ English.
  Never quote a secret, placeholder token, email address or personal detail — this repo
  is PUBLIC; describe and locate instead. Counter-example file names that carry a
  key-shaped value are described by shape, not pasted.
- Review deep, not fast: a finding needs a probe or a re-driven claim behind it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the deferred material lives in the sibling .deferred.md, held apart under the rule-1 split and opened only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`,
`docs/sessions/`, every prior verdict in `docs/reviews/`, the queue pointer, this
brief's sibling `docs/reviews/2026-10-17-1010-advisory-count-per-scanner-cold.deferred.md`,
the landing commit's message body (the author's account; read subject, stat and diff
only), and the commissioning items:

- `docs/roadmap/115-guardrail-architecture-mike-commissioned/320-three-small-floor-test-and-contract-gaps.md`
- `docs/roadmap/115-guardrail-architecture-mike-commissioned/290-three-guards-describe-a-response-tier-their-code-lacks.md`

Sweep with `python3 tools/coldsweep.py --root <your worktree> --also-exclude
docs/roadmap/160-doctrine-review-owed/860-rule-4-cold-pass-queued-advisory-count-per-scanner.md
--also-exclude docs/reviews/2026-10-17-1010-advisory-count-per-scanner-cold.deferred.md
--also-exclude
docs/roadmap/115-guardrail-architecture-mike-commissioned/320-three-small-floor-test-and-contract-gaps.md
--also-exclude
docs/roadmap/115-guardrail-architecture-mike-commissioned/290-three-guards-describe-a-response-tier-their-code-lacks.md
<pattern>`; `--include-barred` only with disclosure in the verdict. Reading the delta is
never barred.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list. Then append
your verdict below a `---` divider in THIS file: provenance repeated (how you were
spawned, your tier, what you read), per-lens answers, the standing checklist V1–V7 each
answered or discharged with grounds, the writer table, findings with stable IDs (prefix
`AV`: `AV1`, `AV2`, …) and severities (MAJOR / MODERATE / minor / note), an overall
PASS / PASS-WITH-FINDINGS / FAIL line with counts, a re-run ledger, and a follow-up
checklist. Then STOP and commit phase 1 unrevised before opening the sibling. Edit no
other file.

**Phase 2.** Open the sibling; append `### Reconcile` beneath your verdict: per-finding
notes against the seeded questions and the intent record, any finding formed at
reconcile marked as such, and the overall line restated. Never revise phase-1 text.
Then fold the sibling in below the reconcile and delete it.

Findings on self-authored doctrine are the principal's to decide (rule 3; a guard is
doctrine by function): record all, apply nothing; counsel per finding is welcome,
labelled and kept beneath it.
