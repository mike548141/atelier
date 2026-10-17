# Cold pass — no hatch silences sizescan's cold-content gate, and the gate lists the items

**Pass type:** code cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection by whoever takes the pass.
**Status:** BRIEF ONLY — the review has NOT run. Written 2026-10-17 UTC by an Opus
brief-writer; the pass waits for a further cold Fable session that neither the
delta's author nor this brief-writer (nor its orchestrator) started or instructed.
Tier is checked at selection (rule 4).
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/790-rule-4-cold-pass-queued-sizescan-cold-content-hatches.md`.
**Why it earns a review:** `sizescan --check` runs on both floor planes in this repo and in every
child. The delta removes every exemption from its cold-content gate, makes a `.sizescanignore`
glob stop skipping hot-path files, and adds a per-item listing with a run-wide cap. A guard is
doctrine by function (rule 3), and this one changes what every child's commit can pass.

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
  bodies** (the author's own account, including a blast-radius measurement); the subjects and
  `--stat` of later commits on the same files; `REVIEW.md` rules 1–4; three user-local
  templates — the ask halves of the 2026-10-16 expected-toolbox and scanner-rule-gates briefs and
  the whole expected-toolbox sibling, seeded questions included (another pass's framing); HEAD
  greps of `tools/sizescan.py`, `tools/floor.py`'s registry, `.sizescanignore`, and short HEAD
  excerpts of `docs/method/GUARDS.md` and `RECORD.md`; the commissioning item's head line;
  filename-level greps of `docs/reviews/` (no file there opened); and its harness-loaded memory
  index and instruction files (one-line notes, some about the guards' history and how children
  receive scanner changes). It did not open the intent record, `docs/SESSIONS.md`,
  `docs/sessions/`, `docs/ROADMAP-DONE.md` or any file under `docs/reviews/`. Its orchestrator
  passed it an instruction set and no evaluative content about the delta; what the orchestrator
  read is its own to disclose in its claim. Everything evaluative is in the sibling.

## What the work is

Landing commit and merge (diff the commit; review the paths at HEAD, `8acfff1` or later):

- `f9ccba8` (2026-10-16 08:09 UTC) — sizescan: no hatch silences cold content, and the gate
  names the items (115/270); landed in merge `ccfad42` (2026-10-16 08:12 UTC)

Delta paths: `tools/sizescan.py` (the module docstring's hatch section, `ALLOW_MARKER`'s comment,
`FINDING_KINDS`'s comment, `_TITLE_CHARS`, `_COLD_LEAD`, `MAX_MATERIALIZED_FINDINGS`, `ColdItem`,
`_item_title`, `Finding.cold_listed` and `cold_hatches`, `_scan_file_metrics`' item slots,
`iter_candidates`' `evaluate_ignored`, `_cold_hatches`, `scan_paths`, `_suppression_line`,
`render_human`, the `--json` fields, the selftest), `tools/test_sizescan.py`,
`tools/test_report.py` (two line pins and the finding-ID round trip's `unexemptable`),
`tools/pointerscan.py` (one docstring heading) and `tools/README.md` (the sizescan section).

**Later commits on the same files — not this delta; do not attribute them to it.** The first
rewrote much of `sizescan.py` on top of this delta (`_cold_hatches` became `_inert_hatches`,
among others). Review the delta as it landed, then say which of its parts are live at HEAD and
whether any later change altered their behaviour.

- `72a68cc` (2026-10-16 15:28 UTC) — sizescan: remove the size advisory, and name the hatches it
  leaves inert (115/270 c); merged in `da85210` (its own pass, 160/850)
- `39a74b9`, `1c24781`, `f4afb7a`, `e3e8a4f` (2026-10-16) — touch `tools/README.md` or
  `tools/test_report.py` outside this delta's hunks (160/800, 810, 830, 840)

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code, tests and live
behaviour. The lenses organise it; they do not bound it. Non-goals are the only narrowing and
are themselves reviewable.

Probe, at least:

- **Every hatch against every file class, at landing.** Hatches: an unscoped `sizescan:allow`
  header, each scope (`cold-content`, `size-advisory`, `harvest-integrity`, an unknown scope), a
  marker with no reason, a marker past the header window, a `.sizescanignore` glob. File classes:
  a metered hot-path file with and without `[x]` items, an archive store, a root-only file outside
  the root. For each, at `f9ccba8^` and at `f9ccba8`: gated or not, advisory or not, what the
  report and `--json` say, and which suppression count moves.
- **What `evaluate_ignored` now reads.** Which files were skipped before and are read now; the
  repo's own `.sizescanignore` entries and what the gate does with the files they match at HEAD;
  how the scanner's file walk and the glob interact.
- **The listing and its cap.** The run-wide slot budget across files and argument order; the
  true count against the listed count; the over-cap line and the `cold_items_over_cap` field;
  the 60-character title, the 85-column claim, multi-byte and control characters in an item's
  text as printed; the unbalanced-fence second pass.
- **The suppressed line.** `files_by_glob` now counts differently; say what the number means at
  landing and at HEAD, and whether two runs stay comparable (`GUARDS.md` rule b).
- **The principal's words.** Separate the quoted ruling in the module docstring from the code
  and wording around it; say where the surrounding text or the behaviour narrows, widens or
  re-reads it, and check the date the docstring gives it.
- **Reach.** `sizescan --check` is in `tools/floor.py`'s registry on both planes. Say how and
  when a child receives this change, and what a child that relied on a hatch now sees. Measure
  only in this repo and in scratch fixtures; never run a scanner over another repo.

**Non-goals:** the principal's ruling that no hatch exempts cold content and that the gate list
the completed items (quoted in the delta). Its encoding, the wording around it, the tests and the
behaviour are in scope.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself first. Ask whether a
   gate with no exemption at all fits `docs/method/GUARDS.md`'s exemption rules, and whether
   reading ignored files to gate them keeps the meaning of an ignore file.
2. **Correctness & quality.** Read `scan_paths`, `iter_candidates`, `_scan_file_metrics` and the
   new tests whole; diff `f9ccba8`. Record the hatch × file-class table from *Scope*. Check
   whether each new test fails on `f9ccba8^` and whether its fixtures were derived from the code
   or from the ruling.
3. **Completeness / harvest.** `tools/README.md`'s sizescan section; `docs/method/GUARDS.md` and
   `docs/method/RECORD.md` where they speak of sizescan or cold content; `CHANGELOG.md`; any
   template, skill or doc that tells a repo to use a hatch for a flat log; the finding-ID round
   trip in `tools/test_report.py`.
4. **Security & privacy** — mandatory. The listing now prints item text from tracked files into
   hook output and public CI logs: check terminal-control and escape sequences, length bounds and
   memory bounds on adversarial input. Build counter-examples from synthetic values only.
   `/security-review` is discharged by grounds (a landed delta; the pending diff is not the work)
   — say so, and deliver the code-altitude read by hand against the OWASP catalogue.

## Re-run obligation

Re-run, do not read. Lift floor invocations from `.githooks/pre-commit`, `tools/floor.py` and
`.github/workflows/ci.yml` rather than guessing.

- `python3 -m unittest tools.test_sizescan tools.test_report -v`; `python3 tools/sizescan.py
  --selftest`; `python3 tools/pointerscan.py --selftest`
- `python3 tools/sizescan.py --check --root . .` and the same with `--json`, exit codes read
  explicitly
- the hatch × file-class table, driven at `f9ccba8^`, `f9ccba8` and HEAD in a scratch clone over
  synthetic fixtures, comparing stdout, stderr and exit code
- the cap, driven with a synthetic tree whose completed items exceed it across several files
- the floor on both planes at HEAD; the full Python suite once, foreground

## House rules for this run

- Name the worktree you work in. Run no git command that writes there; read-only git is fine.
  Probes and older checkouts go in a private clone under your session scratchpad, named by your
  prefix. Never open another `docs/reviews/2026-10-16-*` or `docs/reviews/2026-10-17-*` file — it
  is another pass's framing.
- One heavy process at a time on a shared machine: the full suite at most once, in the
  foreground; fixtures sized to finish in minutes, under `nice`. Never point a scanner at any
  other repo on the machine.
- `/security-review` reads the session's pending diff: discharge it by grounds for this landed
  delta, or keep the tree clean whenever you spawn it.
- Dates absolute ISO 8601 from `date -u`. Prose wrapped at ≤ 100 columns. NZ English. Never quote
  a secret, placeholder token, email address or personal detail — this repo is PUBLIC; describe
  and locate instead.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the deferred material lives in the sibling .deferred.md, held apart under the rule-1 split and opened only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`, every
prior verdict in `docs/reviews/`, the queue pointer, this brief's sibling
`docs/reviews/2026-10-17-0930-sizescan-cold-hatches-cold.deferred.md`, the landing commit's and
merge's message bodies (read subject, stat and diff only), and the commissioning item `270` in
`docs/roadmap/115-guardrail-architecture-mike-commissioned/`.

Sweep with `python3 tools/coldsweep.py --root <your worktree> --also-exclude
docs/roadmap/160-doctrine-review-owed/790-rule-4-cold-pass-queued-sizescan-cold-content-hatches.md
--also-exclude docs/reviews/2026-10-17-0930-sizescan-cold-hatches-cold.deferred.md
--also-exclude
docs/roadmap/115-guardrail-architecture-mike-commissioned/270-three-defects-found-adding-finding-ids.md
<pattern>`; `--include-barred` only with disclosure. Reading the delta is never barred.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list. Then append your
verdict below a `---` divider in THIS file: provenance repeated (how you were spawned, your tier,
what you read), per-lens answers, the standing checklist V1–V7 each answered or discharged with
grounds, the hatch × file-class table, findings with stable IDs (prefix `HX`: `HX1`, `HX2`, …)
and severities (MAJOR / MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL line
with counts, a re-run ledger, and a follow-up checklist. Then STOP and commit phase 1 unrevised
before opening the sibling.

**Phase 2.** Open the sibling; append `### Reconcile` beneath your verdict: per-finding notes
against the seeded questions and the intent record, any finding formed at reconcile marked as
such, and the overall line restated. Never revise phase-1 text. Then fold the sibling in below
the reconcile and delete it.

Findings on self-authored doctrine are the principal's to decide (rule 3; a guard is doctrine by
function): record all, apply nothing; counsel per finding is welcome, labelled and kept beneath
it.
