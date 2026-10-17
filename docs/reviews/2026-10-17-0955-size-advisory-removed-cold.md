# Cold pass — sizescan's size advisory removed, and the hatches it leaves inert

**Pass type:** code and doctrine cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection by whoever takes the pass.
**Status:** BRIEF ONLY — the review has NOT run. Written 2026-10-17 UTC by an Opus
brief-writer; the pass waits for a further cold Fable session that neither the
delta's author nor this brief-writer (nor its orchestrator) started or instructed.
Tier is checked at selection (rule 4).
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/850-rule-4-cold-pass-queued-size-advisory-removed.md`.
**Why it earns a review:** it removes a signal from a floor guard every child runs,
rewrites which of that guard's hatches still exempt anything (one of them on the
harvest-integrity gate), reports a new class of "inert" hatch, and edits
`docs/method/RECORD.md`'s account of what keeps the session index lean.

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
  160/790, 160/800 and 160/860; the landing commit's subject, `--stat`, diff on the
  doctrine, comment and pin paths and the first 220 lines of the `tools/sizescan.py`
  diff, **and message body** (the author's own account, with principal quotes); the
  merge's re-merge diff stat (board and record files only); two 2026-10-16 briefs in
  full as templates; `docs/reviews/` filenames and filename-level greps (no prior
  verdict opened); the title lines of the commissioning board items; grep-hit lines
  naming the retired advisory in `CHANGELOG.md`, `tools/README.md` and two tests,
  and naming sizescan in `docs/method/RECORD.md` and `tools/floor.py`; and its
  harness-loaded memory index. It did not open the intent record,
  `docs/SESSIONS.md`, `docs/sessions/`, `docs/ROADMAP-DONE.md` or
  `docs/method/REVIEW.md`. What its orchestrator read is the orchestrator's to
  disclose; it passed on an instruction file, three templates and a list of taken
  prefixes, and no evaluative content. Everything evaluative is in the sibling.

## What the work is

Landing commit (diff it; review the paths at HEAD, `b50db0c` or later):

- `72a68cc` (2026-10-16 15:28 UTC) — sizescan: remove the size advisory, and name
  the hatches it leaves inert (115/270 c); landed in merge `da85210` (2026-10-16
  15:45 UTC), whose own changes beyond the commit are board and record files only

Delta paths: `tools/sizescan.py` (read whole at HEAD; about 680 lines changed),
`tools/test_sizescan.py`, `tools/test_report.py`'s sizescan pins and round-trip,
`tools/README.md`'s sizescan section, two passages of `docs/method/RECORD.md` (the
session-index bullet and the cold-content signal paragraph), and comments in
`tools/pins.py` (`MAX_CLAUDE_MD_BYTES`) and `tools/blockscan.py`
(`MAX_MAPPED_FILE_BYTES` and the BOUNDED MEMORY docstring).

The commit builds on `f9ccba8` (2026-10-16, no hatch silences the cold-content gate;
its own pass, 160/790). Its parent is `2e2da81`, the base of two sibling commits
(`f4afb7a`, `e3e8a4f`) merged before it; `e3e8a4f` also edits `tools/test_report.py`
and `tools/README.md`. No later commit touches the delta paths at the time of
writing; confirm at your HEAD.

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code, tests
and live behaviour. The lenses organise it; they do not bound it. Non-goals are the
only narrowing and are themselves reviewable.

Build the full hatch table from the code at HEAD: every marker spelling the shared
allow grammar accepts (unscoped, each scope in `FINDING_KINDS` including the
retired `size-advisory`, an unknown scope, no reason, a body-only mention, a
leftover `budget=N`), every `.sizescanignore` glob shape, on every file class the
tool walks (the roadmap, the other current-truth names, each archive store, a store
outside the default directories). For each: does it exempt anything, is it reported
as inert, how is it counted on the `suppressed:` line and in `--json`, and what did
`72a68cc^` do with it. Then the scope change: which files the tool reads, and how
far into each, before and after; is any file now unread that a gate used to see?
Check `--check` and bare exit codes on each class, the `--json` shape against every
consumer (the floor's registry entry and its advisory form, tests, anything that
read `reference` or `over`), and the per-finding line pins. On the doctrine side:
what each edited `RECORD.md` passage now says detects the defect it describes, and
whether the rest of `RECORD.md` agrees; whether the reworded `pins.py` and
`blockscan.py` comments still ground their ceilings without the number they used to
cite. **Non-goals:** the principal's decision to remove the advisory (quoted in the
delta) — but what the removal leaves undetected, and how the delta says so, is in
scope.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself first.
   Among them: that reporting an inert hatch is safer than accepting or rejecting
   it; that keeping a retired scope name is needed to stop a stale marker widening;
   that "caught at review" is a real detector for prose-shaped cold content.
2. **Correctness & quality.** Read `tools/sizescan.py` and its tests whole at HEAD;
   diff `72a68cc`. Record the hatch table from *Scope* with a counter-example line
   wherever the code and the docstring disagree. Check that the new tests would
   fail on `72a68cc^` for the reason each test names.
3. **Completeness / harvest.** Every surface that still names the size advisory,
   the reference points, the budget marker or "line count is advisory": the README,
   `docs/method/` (RECORD, GUARDS, PROPAGATION), the templates and create-repo skill,
   `CHANGELOG.md` (is an entry owed, and do older entries now read as current?),
   `test_allowmarker.py`, and children that may carry a now-inert marker.
4. **Security & privacy** — mandatory. The privacy angle is small; the integrity
   angle is not. Hunt for any marker or glob that now exempts an archive store's
   harvest-integrity check where it did not before, or stops exempting one where it
   did, and for any file a gate no longer reads. Fixtures from synthetic content
   only. `/security-review` is discharged by grounds (a landed delta; the pending
   diff is not the work) — say so, and deliver the code-altitude read by hand
   against the OWASP catalogue.

## Re-run obligation

Re-run, do not read. Lift floor invocations from `.githooks/pre-commit`,
`tools/floor.py` and `.github/workflows/ci.yml` rather than guessing.

- `python3 -m unittest discover -s tools -p 'test_sizescan.py' -v`, the same for
  `test_report.py`, `test_allowmarker.py`, `test_pins.py` and `test_blockscan.py`;
  `python3 tools/sizescan.py --selftest`
- sizescan at `72a68cc^`, `72a68cc` and HEAD in a scratch clone, bare and with
  `--check`, over a synthetic fixture tree carrying every row of your hatch table:
  compare stdout, exit code and `--json`
- `python3 tools/sizescan.py --check --root . .` on this repo at HEAD, exit code
  read explicitly
- the floor on both planes at HEAD; the full Python suite once, foreground

## House rules for this run

- Name the worktree you work in. Run no git command that writes there; read-only
  git is fine. Fixture trees, older checkouts and probes go in a private clone
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
brief's sibling `docs/reviews/2026-10-17-0955-size-advisory-removed-cold.deferred.md`,
the landing commit's message body (read subject, stat and diff only), and items
`270` and `330` in `docs/roadmap/115-guardrail-architecture-mike-commissioned/`
(the commissioning item, and a finding filed at the same merge on a passage this
delta edits).

Sweep with `python3 tools/coldsweep.py --root <your worktree> --also-exclude
docs/roadmap/160-doctrine-review-owed/850-rule-4-cold-pass-queued-size-advisory-removed.md
--also-exclude docs/reviews/2026-10-17-0955-size-advisory-removed-cold.deferred.md
--also-exclude
docs/roadmap/115-guardrail-architecture-mike-commissioned/270-three-defects-found-adding-finding-ids.md
--also-exclude
docs/roadmap/115-guardrail-architecture-mike-commissioned/330-record-md-rotation-trigger-has-no-signal.md
<pattern>`; `--include-barred` only with disclosure. Reading the delta is never
barred.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list. Then
append your verdict below a `---` divider in THIS file: provenance repeated (how
you were spawned, your tier, what you read), per-lens answers, the standing
checklist V1–V7 each answered or discharged with grounds, the hatch table, findings
with stable IDs (prefix `SZ`: `SZ1`, `SZ2`, …) and severities (MAJOR / MODERATE /
minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL line with counts, a
re-run ledger, and a follow-up checklist. Then STOP and commit phase 1 unrevised
before opening the sibling.

**Phase 2.** Open the sibling; append `### Reconcile` beneath your verdict:
per-finding notes against the seeded questions and the intent record, any finding
formed at reconcile marked as such, and the overall line restated. Never revise
phase-1 text. Then fold the sibling in below the reconcile and delete it.

Findings on self-authored doctrine are the principal's to decide (rule 3; a
guard is doctrine by function, and `RECORD.md` is doctrine): record all, apply
nothing; counsel per finding is welcome, labelled and kept beneath it.
