# Cold pass — indexscan, a hand-kept index names every file it maps

**Pass type:** code cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection by whoever takes the pass.
**Status:** BRIEF ONLY — the review has NOT run. Written 2026-10-16 UTC by an Opus
brief-writer; the pass waits for a further cold Fable session that neither the
delta's author nor this brief-writer (nor its orchestrator) started or instructed.
Tier is checked at selection (rule 4).
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/700-rule-4-cold-pass-queued-indexscan.md`.
**Why it earns a review:** a new floor guard registered in `tools/floor.py`, which
every child runs at `main` on its next CI run; it defines its own declaration
grammar, its own exemption marker and its own notion of "listed", and the house
adopted it on four of its own indexes in the same landing.

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
  passes rule 4's criterion. The reviewer repeats its own provenance (who spawned
  it, its tier, any orchestration shape) in its verdict.
- ⚠️ **Exposure, disclosed** (rule-2 material met before writing). This
  brief-writer read: the queue pointer in full; the landing commits' subjects,
  `--stat` and diffs of the delta paths, **and their message bodies** (the
  author's own account); the subjects and `--stat` of later commits on the same
  files; the merge's combined diff for `docs/SESSIONS.md` lines 3–13 only;
  `REVIEW.md` rules 1–4, the four lenses, the checklist and the lifecycle; the ask
  halves of two 2026-10-04 briefs as templates; `docs/reviews/` filenames and
  filename-level greps (no prior verdict opened); the names, not the contents, of
  the commissioning board items; and its harness-loaded memory index (one-line
  notes, some about these guards' history). Its orchestrator read the
  `docs/SESSIONS.md` index tail through 2026-10-16 (including the authoring run's
  one-paragraph summary) and the 2026-10-16 session record's close section, and
  passed on no evaluative content beyond the pointer list and a one-line note that
  some guard files changed later. Everything evaluative is in the sibling.

## What the work is

Landing commits (diff these; review the paths at HEAD):

- `8d10487` (2026-10-05 12:19 UTC) — tools: add indexscan — a hand-maintained
  index names every file it maps; landed in merge `5600b0e` (2026-10-05 12:26 UTC)

Delta paths (the pointer's list): `tools/indexscan.py`, `tools/test_indexscan.py`,
`tools/floor.py` (the new registry entry), `tools/README.md` (the catalogue
section, plus the index's own declaration and two allow markers at lines 3–5),
`tools/test_allowmarker.py`, `tools/test_mixed_root.py`, and the declaration and
allow-marker lines in `docs/decisions/README.md`, `instruments/README.md` and
`docs/SESSIONS.md`. Note a fact of the landing: the ten `indexscan:allow` lines in
`docs/SESSIONS.md` (lines 4–13) are absent from both parents of `5600b0e` and
first appear in the merge itself (`git show --cc 5600b0e -- docs/SESSIONS.md`).

**Later commits on the same surfaces — not this delta; do not attribute them to
it.** Review the delta's own claims at HEAD and say which commit a finding rests
on:

- `ffabef3` (2026-10-05) — single-source the scanners' exit contract and report
  lines; converted indexscan's report and exit lines (its own pass is 160/730)
- `1c24781` (2026-10-16) — indexscan flags an index line dated before the file it
  links (320/430); adds a second finding kind and a scoped marker form
- `e3e8a4f` (2026-10-16) — licenscan's warning made real; touches `tools/floor.py`

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code, tests
and live behaviour. The lenses organise it; they do not bound it. Non-goals are the
only narrowing and are themselves reviewable.

Build declared indexes in a scratch clone and compare what the guard reports with
what you judge correct. Cases: an index that maps `.` and lives in that directory;
`dir=` with `..` that stays inside `--root`, and one that escapes through a
symlink; a mapped directory that is gone, empty, or a file; `match=` and
`exclude=` lists with spaces, commas inside a glob, brackets, and case
differences on a case-insensitive filesystem; a subdirectory entry and a file
entry of the same stem; an entry named only inside a fenced block, inside an
indented code block, inside an HTML comment, or in a link with a `#fragment`, a
`?query`, percent-encoding, angle brackets or a title; a reference-style link
whose definition is in another file; an entry named by a passing mention in
prose; two declarations in one file mapping the same directory; a declaration
split across two lines; `before=` with an impossible date and with entries whose
leading date is malformed; an allow marker whose entry name contains a space; a
marker for an entry outside every `match=`. For each: listed, unlisted, exempt,
stale, or exit 2 — and is that the right answer? Whether the opt-in claim holds:
does an undeclared child tree pass with exit 0 and say it checked nothing, on both
planes, and does any file in a child's tree become a declaration by accident?
**Non-goals:** the ruling that chose one generic opt-in check over a
decisions-only build, and the separate ruling owed on flipping it to blocking.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself first.
   Among them: that "any link or code span anywhere counts as listed" is the right
   looseness for the unlisted direction; that leaving listed-but-missing to
   `linkscan` and `pathscan` leaves no gap (check those guards' scope at HEAD —
   `pathscan` is warn-only); that warn-only on both planes still "makes the failure
   cheap", as the floor entry declares under the fourth requirement in
   `docs/method/GUARDS.md`.
2. **Correctness & quality.** Read `indexscan.py` and its tests whole; diff
   `8d10487`. Drive every case in *Scope* and record a table. Check the exit-2 set
   in the docstring against the code, and that `--warn` never downgrades exit 2.
   Check the line-chunking path for long lines, and the stale-allow logic when two
   markers name the same entry.
3. **Completeness / harvest.** The four adopted indexes at HEAD: is each
   declaration right for what that index actually catalogues, and is every allow
   marker's stated cause still open? (`tools/README.md` lines 4–5 point at two
   open findings by ID — check they still stand by filename-level grep only, and
   open the verdicts only after phase 1.) Does `tools/README.md`'s catalogue
   section agree with the code, and do `docs/method/GUARDS.md` and the floor's
   other descriptions name the new guard where they list guards?
4. **Security & privacy** — mandatory. The guard reads every Markdown file in a
   tree it does not trust and resolves paths a committed file chooses. Probe
   `dir=` and link targets for escape outside `--root` (`..`, absolute paths,
   symlinks, `file:` and other schemes), regex cost on adversarial lines, and
   whether its output can echo file names from outside the repo. `/security-review`
   is discharged by grounds (a landed delta; the pending diff is not the work) —
   say so, and deliver the code-altitude read by hand against the OWASP catalogue.

## Re-run obligation

Re-run, do not read. Lift floor invocations from `.githooks/pre-commit`,
`tools/floor.py` and `.github/workflows/ci.yml` rather than guessing.

- `python3 -m unittest tools.test_indexscan tools.test_allowmarker
  tools.test_mixed_root -v`, and `python3 tools/indexscan.py --selftest` if the
  guard has one (check `--help`)
- the landing claims: decisions and instruments indexes clean; the tools
  catalogue's two gaps allow-marked; the session index's unlisted count — re-run
  `python3 tools/indexscan.py --root <tree> .` at `8d10487`, at `5600b0e` and at
  HEAD in a scratch clone, and say which numbers reproduce
- the undeclared-tree pass: a fresh scratch repo with no declaration, both planes
- `python3 tools/floor.py --list --plane hook` and `--plane ci`, then the floor on
  both planes at HEAD; the full Python suite once, foreground

## House rules for this run

- Name the worktree you work in. Run no git command that writes there (no add,
  commit, stash, checkout, worktree, reset, clean); read-only git is fine.
  Probes, older checkouts and scratch trees go in a private clone under your
  session scratchpad, named by your prefix.
- One heavy process at a time on a shared machine: the full suite at most once, in
  the foreground. Never point a scanner at any other repo on the machine.
- `/security-review` reads the session's pending diff: discharge it by grounds for
  this landed delta and do the code-altitude read by hand, or keep the tree clean
  whenever you spawn it.
- Dates absolute ISO 8601 from `date -u`. Prose wrapped at ≤ 100 columns. NZ
  English. Never quote a secret, placeholder token, email address or personal
  detail — this repo is PUBLIC; describe and locate instead.
- Reading `docs/SESSIONS.md` is barred (below) except lines 3–13, the delta's own
  declaration and markers: read them with `sed -n '3,13p' docs/SESSIONS.md` and
  nothing wider. Running the guard prints session file names; that is permitted.
  Disclose both in your verdict.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the deferred material lives in the sibling .deferred.md, held apart under the rule-1 split and opened only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md` (save the
carve-out above), `docs/sessions/`, every prior verdict in `docs/reviews/`, the
queue pointer, this brief's sibling
`docs/reviews/2026-10-16-1551-indexscan-guard-cold.deferred.md`, and the
commissioning items, barred with their whole board sections so no path runs past
the column budget:

- item `010` in `docs/roadmap/200-anti-slop-invariant-registry-promote-rec/`
- item `430` in `docs/roadmap/320-child-filed-findings-via-pointing-up/`

Sweep with `python3 tools/coldsweep.py --root <your worktree> --also-exclude
docs/roadmap/160-doctrine-review-owed/700-rule-4-cold-pass-queued-indexscan.md
--also-exclude docs/reviews/2026-10-16-1551-indexscan-guard-cold.deferred.md
--also-exclude docs/roadmap/200-anti-slop-invariant-registry-promote-rec
--also-exclude docs/roadmap/320-child-filed-findings-via-pointing-up
<pattern>`; `--include-barred` only with disclosure. Reading the delta is never
barred.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list. Then
append your verdict below a `---` divider in THIS file: provenance repeated (how
you were spawned, your tier, what you read), per-lens answers, the standing
checklist V1–V7 each answered or discharged with grounds, findings with stable IDs
(prefix `IX`: `IX1`, `IX2`, …) and severities (MAJOR / MODERATE / minor / note),
an overall PASS / PASS-WITH-FINDINGS / FAIL line with counts, a re-run ledger with
commands and results, and a follow-up checklist. Then STOP and commit (or have
your orchestrator commit) phase 1 unrevised before opening the sibling.

**Phase 2.** Open the sibling; append `### Reconcile` beneath your verdict:
per-finding notes against the seeded questions and the intent record, any finding
formed at reconcile marked as such, and the overall line restated. Never revise
phase-1 text. Then fold the sibling in below the reconcile and delete it.

Findings on self-authored doctrine are the principal's to decide (rule 3): record
all, apply nothing; counsel per finding is welcome, labelled and kept beneath it.
