# Cold pass — allow-markers that name a kind, and finding IDs

**Pass type:** code cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection by whoever takes the pass.
**Status:** BRIEF ONLY — the review has NOT run. Written 2026-10-16 UTC by an Opus
brief-writer; the pass waits for a further cold Fable session that neither the
delta's author nor this brief-writer (nor its orchestrator) started or instructed.
Tier is checked at selection (rule 4).
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/750-rule-4-cold-pass-queued-marker-kinds-and-ids.md`.
**Why it earns a review:** an allow-marker is the house's exemption hatch on every
guard, and this delta changed what one exempts in three guards and printed, on
every finding line of nine, the exact token a reader is told to copy into a
marker. A wrong scope rule silences more than intended; a wrong ID teaches every
reader to write the wrong exemption.

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
  `--stat`, the `allowmarker.py` and `report.py` diffs, the leakscan, spellscan
  and sizescan hunks of the ID commit, **and both message bodies** (the author's
  own account); the subjects and `--stat` of later commits on the same files;
  `REVIEW.md` rules 1–4, the four lenses, the checklist and the lifecycle; the ask
  halves of two 2026-10-04 briefs as templates; `docs/reviews/` filenames and
  filename-level greps (no prior verdict opened); the names, not contents, of the
  commissioning board items; and its harness-loaded memory index. Its orchestrator
  read the `docs/SESSIONS.md` index tail through 2026-10-16 (including the
  authoring run's one-paragraph summary) and the 2026-10-16 session record's close
  section, and passed on no evaluative content beyond the pointer list and a
  one-line note naming four later changes to these files. Everything evaluative
  is in the sibling.

## What the work is

Landing commits (diff these; review the paths at HEAD):

- `db1aa4d` (2026-10-05 19:02 UTC) — tools: allow-markers honour a named kind in
  licenscan, sizescan, pointerscan (115/080)
- `ded8d32` (2026-10-05 19:36 UTC) — tools: print a namespaced finding ID on every
  finding line (115/080)
- both landed in merge `2b261e6` (2026-10-05 19:46 UTC)

Delta paths: `tools/allowmarker.py` (`covers`, `is_blanket`); `tools/report.py`
(`finding_id`, `with_id`, `finding_dicts`); the scanners the two commits touch —
`licenscan`, `sizescan`, `pointerscan` (marker kinds), and `datescan`,
`leakscan`, `licenscan`, `linkscan`, `pathscan`, `pointerscan`, `secretscan`,
`sizescan`, `spellscan` (IDs); their tests `test_allowmarker.py`,
`test_licenscan.py`, `test_pointerscan.py`, `test_sizescan.py`,
`test_report.py`; `tools/README.md`; `CHANGELOG.md`.

**Later commits on the same surfaces — not this delta; do not attribute them to
it.** Several change the very kinds this delta made addressable; review the
delta's rule and IDs at HEAD and say which commit a finding rests on:

- `f9ccba8` (2026-10-16) — sizescan: no hatch silences cold content (115/270)
- `72a68cc` (2026-10-16) — sizescan: the size advisory removed, and the hatches
  it leaves inert named (115/270 c) — the `size-advisory` kind goes
- `e3e8a4f` (2026-10-16) — licenscan: the warning made real (an advisory tier)
- `1c24781` (2026-10-16) — indexscan gains a scoped marker kind
  (`date-mismatch`), though `ded8d32` left indexscan without an ID by definition
- `b609b4b` (2026-10-05), `4dfaf8d` (2026-10-05), `39a74b9` and `f4afb7a`
  (2026-10-16) — test runners, quoted paths, the staged-diff reader, staged line
  numbers, on several of the same scanners

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code, tests
and live behaviour. The lenses organise it; they do not bound it. Non-goals are the
only narrowing and are themselves reviewable.

**The scope rule.** For licenscan, sizescan and pointerscan at HEAD, enumerate
every marker form the shared grammar accepts — none, bare, unscoped, a scope
naming one kind, a scope naming a kind in another case, a scope with a typo, a
list scope naming two kinds, a scope naming a kind the scanner later dropped —
and record which kinds each exempts and how the suppression tally counts it.
Whether "any other scope exempts every kind" is the safe default for a guard;
whether `is_blanket` and `covers` agree for every input; whether the three
scanners' `FINDING_KINDS` match what they actually emit. **The IDs.** For each of
the nine scanners: is the printed kind exactly what that scanner's marker accepts
(round-trip it: copy the ID into a marker and confirm that finding, and only it,
goes)? Cases: a spellscan word with an apostrophe, hyphen, capital or non-ASCII
letter; a leakscan or secretscan finding in a path name, where no line can carry
a marker; a sizescan file carrying two kinds; a finding whose rule name contains
characters the marker grammar rejects. Whether appending `  [<scanner>:<kind>]`
breaks any consumer that parses finding lines — `tools/floor.py`, CI workflows,
`floorfleet`, instruments, the child templates. **Non-goals:** the principal's
pick of "both" (fix markers and print IDs), and item 1 of `115/230` that the
"any other scope" branch defers to — though the deferral itself is reviewable.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself first.
   Among them: that an additive rule keeps every live marker meaning what it
   meant; that "the kind is exactly the marker's scope" holds for every guard;
   that leaving conflictscan, wrapscan, indexscan, reviewscan, publishscan and
   harvestscan without IDs is a definition, not a gap.
2. **Correctness & quality.** Read `covers`, `is_blanket`, the three scanners'
   marker paths and the ID helpers whole; diff both commits. Build the
   marker-form table and the per-scanner round-trip table. Check the `--json`
   shape (`id` last; sizescan's `ids` list) against any reader of it.
3. **Completeness / harvest.** `tools/README.md`'s marker and ID sections,
   `docs/method/GUARDS.md` on exemptions, `CHANGELOG.md`'s entries, the shared
   grammar's own docstring, and every scanner using its own scope logic instead of
   `covers`: do they describe one rule?
4. **Security & privacy** — mandatory. An exemption hatch that widens silently
   is a bypass of the guard it sits on; hunt the marker that exempts more than it
   names. Also: does an ID ever echo matched content into CI logs — spellscan's
   word, a leakscan machine-local term, a secret fragment — beyond what the line
   already printed? Never quote such content. `/security-review` is discharged
   by grounds (a landed delta; the pending diff is not the work) — say so, and
   deliver the code-altitude read by hand against the OWASP catalogue.

## Re-run obligation

Re-run, do not read. Lift floor invocations from `.githooks/pre-commit`,
`tools/floor.py` and `.github/workflows/ci.yml` rather than guessing.

- `python3 -m unittest tools.test_allowmarker tools.test_report
  tools.test_licenscan tools.test_sizescan tools.test_pointerscan -v` at HEAD and
  at `2b261e6` in a scratch clone
- the back-compat claims at landing, on this repo and your own fixtures only:
  `db1aa4d^` against `db1aa4d` per marker form, and `ded8d32^` against `ded8d32`
  with the trailing ID and the JSON `id`/`ids` fields stripped (the commits'
  sibling-repo runs are not re-run — never point a scanner at other repos; say so)
- `python3 -m unittest tools.test_floor -v` (its advisory-count contract)
- every touched scanner's `--selftest`; the floor on both planes at HEAD; the full
  Python suite once, foreground

## House rules for this run

- Name the worktree you work in. Run no git command that writes there; read-only
  git is fine. Probes, fixtures and older checkouts go in a private clone under
  your session scratchpad, named by your prefix.
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
brief's sibling
`docs/reviews/2026-10-16-1551-marker-kinds-finding-ids-cold.deferred.md`, and the
commissioning items `080`, `230` and `270` in
`docs/roadmap/115-guardrail-architecture-mike-commissioned/` (barred as a section).

Sweep with `python3 tools/coldsweep.py --root <your worktree> --also-exclude
docs/roadmap/160-doctrine-review-owed/750-rule-4-cold-pass-queued-marker-kinds-and-ids.md
--also-exclude docs/reviews/2026-10-16-1551-marker-kinds-finding-ids-cold.deferred.md
--also-exclude docs/roadmap/115-guardrail-architecture-mike-commissioned
<pattern>`; `--include-barred` only with disclosure. Reading the delta is never
barred.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list. Then
append your verdict below a `---` divider in THIS file: provenance repeated (how
you were spawned, your tier, what you read), per-lens answers, the standing
checklist V1–V7 each answered or discharged with grounds, both tables, findings
with stable IDs (prefix `MK`: `MK1`, `MK2`, …) and severities (MAJOR / MODERATE /
minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL line with counts, a
re-run ledger, and a follow-up checklist. Then STOP and commit phase 1 unrevised
before opening the sibling.

**Phase 2.** Open the sibling; append `### Reconcile` beneath your verdict:
per-finding notes against the seeded questions and the intent record, any finding
formed at reconcile marked as such, and the overall line restated. Never revise
phase-1 text. Then fold the sibling in below the reconcile and delete it.

Findings on self-authored doctrine are the principal's to decide (rule 3; a
guard is doctrine by function): record all, apply nothing; counsel per finding is
welcome, labelled and kept beneath it.
