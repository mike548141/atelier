# Cold pass — indexscan's date rule

**Pass type:** code cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection by whoever takes the pass.
**Status:** BRIEF ONLY — the review has NOT run. Written 2026-10-17 UTC by an Opus
brief-writer; the pass waits for a further cold Fable session that neither the
delta's author nor this brief-writer (nor its orchestrator) started or instructed.
Tier is checked at selection (rule 4).
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/810-rule-4-cold-pass-queued-indexscan-date-rule.md`.
**Why it earns a review:** `indexscan` is on the floor registry for every child (warn-only). The
delta adds a new finding kind that reads dates and times from index lines and file names,
changes the guard's allow-marker grammar to a scoped one, and adds a line-bound exemption form.
A guard is doctrine by function (rule 3).

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
  bodies** (the author's own account, including measurements over the session index); the
  subjects and `--stat` of later commits on the same files; `REVIEW.md` rules 1–4; three
  user-local templates — the ask halves of the 2026-10-16 expected-toolbox and scanner-rule-gates
  briefs and the whole expected-toolbox sibling, seeded questions included (another pass's
  framing); `tools/floor.py`'s indexscan entry and the declaration lines of the declaring indexes
  (grep only); the commissioning item's head line; filename-level greps of `docs/reviews/` (no
  file there opened); and its harness-loaded memory index and instruction files. It did not open
  the intent record, `docs/SESSIONS.md`, `docs/sessions/`, `docs/ROADMAP-DONE.md` or any file
  under `docs/reviews/`. Its orchestrator passed it an instruction set and no evaluative content
  about the delta; what the orchestrator read is its own to disclose in its claim. Everything
  evaluative is in the sibling.

## What the work is

Landing commit and merge (diff the commit; review the paths at HEAD, `8acfff1` or later):

- `1c24781` (2026-10-16 08:27 UTC) — tools: indexscan flags an index line dated before the file
  it links (320/430); landed in merge `da3227d` (2026-10-16 08:53 UTC)

Delta paths: `tools/indexscan.py` (the module docstring's MISDATED bullet, THE DATE RULE and its
two following sections, the allow-marker section; `ALLOW_RX` now `scope="one"`, `DATE_KIND`,
`LEAD_LINK_RX`, `TEXT_STAMP_RX`, `NAME_STAMP_RX`, `Tally.dated_lines`, `parse_allow_scoped`,
`discover`'s marker filter, `_clock`, `_real_date`, `_entry_path`, `_misdated`, `check_dates`,
its call in `check_index`, the clean head, `--help` text, `--json` and selftest),
`tools/test_indexscan.py` (the `DateRule` class), `tools/test_allowmarker.py` (indexscan's pinned
`ALLOW_RX`), `tools/test_report.py` (two indexscan line pins) and `tools/README.md` (the date-rule
paragraphs, the exit codes and *What it cannot see*).

**Later commits on the same files — not this delta; do not attribute them to it.**
`tools/indexscan.py`, `tools/test_indexscan.py` and `tools/test_allowmarker.py` are unchanged
since the merge; confirm that. `72a68cc`, `f4afb7a` and `e3e8a4f` (2026-10-16) touch
`tools/README.md` or `tools/test_report.py` outside this delta's hunks (160/850, 830, 840). The
guard itself landed earlier as its own pass (160/700, from `8d10487`); its unlisted-entry rule is
that pass's subject, not this one's.

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code, tests and live
behaviour. The lenses organise it; they do not bound it. Non-goals are the only narrowing and are
themselves reviewable.

Derive, from `LEAD_LINK_RX`, `TEXT_STAMP_RX`, `NAME_STAMP_RX` and `_entry_path` at HEAD, exactly
which index lines are compared and which are not, independently of the delta's tests
(`EVIDENCE.md` § 15 is the reason). Pay attention to:

- **What counts as a dated line.** List markers and indentation; link text with leading
  emphasis, an icon or a status glyph before the date; reference-style links; angle-bracket and
  percent-encoded destinations, anchors and query strings; absolute and `../` destinations; a
  link into a subdirectory entry; destinations that land on `exclude=`d or unmatched names; the
  middle dot and its spacing; `UTC` and other zone words; `~` placement.
- **The comparison.** Date against date, time against time: which clock each side is in
  (`docs/method/CONVENTIONS.md`), what `HHMM` means in the file name (start) and in the line, the
  same-day rule, the midnight boundary, impossible dates and times, a file name with a counter
  instead of a time.
- **The direction rule.** The delta checks "not earlier" and states why. Say what that rule
  cannot catch, and whether the docs' list of blind spots is complete.
- **The marker grammar change.** `ALLOW_RX` moved to the shared grammar's `scope="one"`. Re-parse
  every existing `indexscan:allow` marker in the tree at `1c24781^` and at HEAD and say whether
  any changes meaning; check the colon-ending-entry special case in `parse_allow_scoped`; check
  that the line-bound form cannot exempt a line other than its own and that the unscoped form
  never exempts a date finding.
- **Bounded reading.** The index is now read three times; the docstring claims the date rule
  holds nothing beyond its findings. Check against the house's bounded-guard rules and the cap.
- **Reach.** `indexscan` is warn-only on both planes for every child. Say what a child with a
  dated index sees on its next run, and how a later flip to blocking would land. Measure only in
  this repo and in scratch fixtures; never run a scanner over another repo.

**Non-goals:** the unlisted-entry rule and the declaration grammar (160/700). How the date rule
uses the declaration is in scope.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself first. The central one:
   that an index line can never be legitimately dated earlier than the file it links. Others:
   that a file name's date and time are its start; that the leading link is the entry the line
   describes; that a warn-only tripwire with no current findings earns its cost.
2. **Correctness & quality.** Read `check_dates`, `_misdated`, `_entry_path` and
   `parse_allow_scoped` whole, with the `DateRule` tests; diff `1c24781`. Build a line-shape table:
   shape, compared or not, finding or not, and a counter-example line wherever the behaviour and
   the docs disagree. Check whether each new test fails on `1c24781^` and whether the fixtures
   were derived from the regexes or from the same reading that wrote them.
3. **Completeness / harvest.** `tools/README.md`'s indexscan section; the declaring indexes in the
   tree (`tools/README.md`, `docs/decisions/README.md`, `instruments/README.md` and the session
   index — the last is barred until phase 2, see below); `tools/floor.py`'s indexscan entry and
   its `why=`; `docs/method/RECORD.md` on how the session index is kept; `CHANGELOG.md`.
4. **Security & privacy** — mandatory. Regex cost on adversarial long lines (the link and stamp
   patterns, the chunked reading of over-long lines); what finding text echoes from the index
   into public CI logs; that markers and declarations cannot be used to silence other guards.
   Build counter-examples from synthetic values only. `/security-review` is discharged by grounds
   (a landed delta; the pending diff is not the work) — say so, and deliver the code-altitude read
   by hand against the OWASP catalogue.

## Re-run obligation

Re-run, do not read. Lift floor invocations from `.githooks/pre-commit`, `tools/floor.py` and
`.github/workflows/ci.yml` rather than guessing.

- `python3 -m unittest tools.test_indexscan tools.test_allowmarker tools.test_report -v`;
  `python3 tools/indexscan.py --selftest`
- `python3 tools/indexscan.py --warn --root . .`, the same without `--warn`, and with `--json`,
  exit codes read explicitly (its output names entries and line numbers, not line text)
- the line-shape table, driven at `1c24781^`, `1c24781` and HEAD in a scratch clone over
  synthetic indexes, comparing stdout, stderr and exit code
- the marker re-parse at `1c24781^` and HEAD over every `indexscan:allow` marker in the tree
- the floor on both planes at HEAD; the full Python suite once, foreground

## House rules for this run

- Name the worktree you work in. Run no git command that writes there; read-only git is fine.
  Probes and older checkouts go in a private clone under your session scratchpad, named by your
  prefix. Never open another `docs/reviews/2026-10-16-*` or `docs/reviews/2026-10-17-*` file — it
  is another pass's framing.
- **The session index is barred, and it is this rule's main real input.** Running the scanner
  over the tree is fine. Re-driving any claim about the index's content (how many of its lines
  are dated later than their file, and why) needs `docs/SESSIONS.md` itself: do that at phase 2,
  or with a script of your own whose output carries counts only and no line text, disclosed in
  the verdict. Never open the file before your phase-1 findings are committed.
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
`docs/reviews/2026-10-17-0930-indexscan-date-rule-cold.deferred.md`, the landing commit's and
merge's message bodies (read subject, stat and diff only), and the commissioning item `430` in
`docs/roadmap/320-child-filed-findings-via-pointing-up/`.

Sweep with `python3 tools/coldsweep.py --root <your worktree> --also-exclude
docs/roadmap/160-doctrine-review-owed/810-rule-4-cold-pass-queued-indexscan-date-rule.md
--also-exclude docs/reviews/2026-10-17-0930-indexscan-date-rule-cold.deferred.md
--also-exclude
docs/roadmap/320-child-filed-findings-via-pointing-up/430-no-floor-check-catches-an-orphaned-session-detail-file.md
<pattern>`; `--include-barred` only with disclosure. Reading the delta is never barred.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list. Then append your
verdict below a `---` divider in THIS file: provenance repeated (how you were spawned, your tier,
what you read), per-lens answers, the standing checklist V1–V7 each answered or discharged with
grounds, the line-shape table, findings with stable IDs (prefix `DM`: `DM1`, `DM2`, …) and
severities (MAJOR / MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL line
with counts, a re-run ledger, and a follow-up checklist. Then STOP and commit phase 1 unrevised
before opening the sibling.

**Phase 2.** Open the sibling; append `### Reconcile` beneath your verdict: per-finding notes
against the seeded questions and the intent record, any finding formed at reconcile marked as
such, and the overall line restated. Never revise phase-1 text. Then fold the sibling in below
the reconcile and delete it.

Findings on self-authored doctrine are the principal's to decide (rule 3; a guard is doctrine by
function): record all, apply nothing; counsel per finding is welcome, labelled and kept beneath
it.
