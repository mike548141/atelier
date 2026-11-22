# Cold pass — a floor `disabled` entry takes an end date, and reviewscan's not-in-scope line

**Board:** `docs/roadmap/160-doctrine-review-owed/1270-rule-4-cold-pass-queued-disabled-end-date-and-reviewscan-scope.md`
**Status:** REVIEWED, both acts, 2026-11-22 UTC, by a Fable 5.1 reviewer under drain session
`eca14b23` (orchestrator `92ba9071`); PASS-WITH-FINDINGS, 0 MAJOR · 5 MODERATE · 8 minor · 1
note; every finding awaits the principal's decision (rule 3). Brief written 2026-11-14 UTC by a
headless Opus 5.5 brief-writer (`cclive` lists it as session `48ef9c3e`).

**Pass type:** code cold pass, per `docs/method/REVIEW.md` rule 4 (a gate and a guard's report
line are doctrine by function, rule 3).
**Tier:** Fable 5.1, the principal-named review tier, checked at selection by whoever takes the
pass. A session that cannot run on it stops (rule 4).
**Size of this pass:** medium: one commit, 13 files, about 456 lines added and 32 removed, of which
about 210 are code in three tools (`floor.py`, `floorfleet.py`, `reviewscan.py`), about 215 are
tests, and the rest docs and board.
**Why it earns a review:** both halves sit on a silent-failure surface. `floor.py` decides whether
a check runs in every child's commit hook and CI; `floorfleet` is the one view that shows a
lowered check across the fleet; `reviewscan`'s green line is read as "every design record states
its review". The worst failures: a config shape that lets a check be switched off with less
visibility than before, or a lowering the fleet view shows as healthy; and a scan that judged
nothing still reading as a pass on any surface that displays it. The change reaches every child
on its next CI run, since children run the floor from `main`.

## Spawn provenance

- **Author of the work under review:** a principal-opened Opus 5.5 queue run, session `d0ca5d24`,
  2026-11-09 UTC, and the worker it dispatched, which wrote the commit (per the queue pointer). The
  author queued this pass and does not take it.
- **Who wrote this brief:** a headless brief-writer (`claude-opus-5-5`; `cclive` lists it as session
  `48ef9c3e`), started 2026-11-14 UTC by an estate health sweep, orchestrator session `58027096`
  (Opus), on the principal's instruction that a brief is written for every review known to be
  owed (Mike, 2026-11-14, verbatim: *"include all briefs are written where we know a fable
  review is required"*). Neither wrote any of this delta. **Off-tier for review, disclosed: the
  brief-writer forms no finding and writes no severity**, and stops after writing. It ran no review
  and used no Fable model.
- **Barred from running this pass:** session `48ef9c3e` and session `58027096` (whoever writes a
  brief does not run it), and session `d0ca5d24` with everything it started.
- **Contact, disclosed (rule 4):** the brief-writer's only instruction came from `58027096`: the
  item number, the pointer's opening sentence, and the rules of the sweep. It carried no framing of
  the work. The brief-writer had no contact with the author session or its worker.
- **Who reviews:** a fresh Fable 5.1 session started for this pass alone, by a session that passes
  rule 4's criterion. An orchestrator may hold the context partition and commit the records
  off-tier, only if it forms no finding, writes no severity, and is disclosed in the claim, the
  pointer and the verdict.
- ⚠️ **Brief-writer's exposure, disclosed** (rule-2 and author-account material met before writing):
  its launch prompt; `skills/review-brief/SKILL.md`; the queue pointer whole; **both intent
  records whole**, including the author's landing notes (`320/800` from line 8, `320/770` from
  line 26); **the delta's commit message body**, read through `git show` before the diff; parts of
  `020/170`; the unrun brief for `160/1250` and its sibling's opening (read for house form); the
  delta and current code at HEAD. It opened **no prior verdict file**. Its harness also loaded
  user-level and repo instruction files and a memory index, which hold private context this brief
  does not carry. Everything evaluative it formed is in the sibling.

## The acceptance test

The principal's word on lowering a check is a pick from options a session offered, an answer and
not a ruling in his own words. Print it, and the option text around it, from the worktree root:

```
sed -n '120,121p' docs/roadmap/020-policy-as-code-programme-five-tracks-mik/170-f1-rebuild-the-block-vs-advise-model-from-base.md
```

His pick is the quoted label, *"Allow if declared + expiring"*; the rest of the line is the
offering session's reading of it. Test the delta against that label and against how
`docs/method/GUARDS.md` § *Ruled 2026-11-09: a repo may lower a check's response, declared and
expiring* carries it. The two problems the delta answers, as filed before it, are:

```
sed -n '1,7p' docs/roadmap/320-child-filed-findings-via-pointing-up/800-a-floor-disabled-entry-has-no-end-date.md
sed -n '1,25p' docs/roadmap/320-child-filed-findings-via-pointing-up/770-hand-up-reviewscan-reads-numbered-decision-records-as-none.md
```

`320/770` lines 1–25 are a private child's report, stated class-only, written before the work:
evidence, not the author's account. The rest of both records is the author's account and is barred
until phase 2.

## What the work is

One commit on `main`, authored 2026-11-09 UTC (stamped 2026-11-10 NZDT):

- **`06248fba`** — `tools: reviewscan says not-in-scope over zero records; floor disabled takes an
  end date`.

Read it body-free: `python3 tools/coldsweep.py --root . --commit 06248fba` (subject, stat and diff,
never the body; board files left out). Plain `git show` prints the body before the diff, and
reading is atomic (`REVIEW.md` rule 1), so it is barred. Check first that your tree has the delta:
`git merge-base --is-ancestor 06248fba HEAD` exits 0.

Delta paths, read at the commit and at HEAD:

- `tools/floor.py`: `_load_disabled`, the `Config.disabled_review_by` map, the `Result.undated`
  field, the disabled branch of `run`, the disabled branch of `render`, the module docstring's
  `disabled` paragraph.
- `tools/floorfleet.py`: `_disabled`, `ChildFloor.disabled_review_by`, the disabled lines of
  `render`.
- `tools/reviewscan.py`: `NUMBERED_NAME`, `count_unread_numbered`, the zero-record branch of
  `_render`, the `unread_numbered_records` JSON key, the docstring paragraph.
- Tests: `tools/test_floor.py`, `tools/test_floorfleet.py`, `tools/test_reviewscan.py`,
  `tools/test_report.py` (the reviewscan line pin, now fed one record).
- Docs: `tools/README.md` (two paragraphs), `docs/method/GUARDS.md` (the lowering table's
  `disabled` row and the paragraph below it), `CHANGELOG.md` (the 2026-11-10 entry).

**The files have moved since.** Later commits touched the same tools, among them `aca05c14` and
`641f017f` (a coverage line on every scanner, including reviewscan's not-in-scope branch) and
`55c7d409` (reviewscan header warnings). List them with
`git log --oneline 06248fba..HEAD -- tools/floor.py tools/floorfleet.py tools/reviewscan.py`.
Judge this delta as it stands at HEAD, and whether those later changes kept or undid its claims.

## The claims the delta makes

Extracted from the delta, not evaluated here. They are the author's claims to test, not settled
scope. Name your own load-bearing assumptions first (lens 1).

- A `disabled` entry takes the legacy reason string or `{"why", "review-by"}`, "the spelling
  `advisory` uses"; the bare string still parses.
- "A missing or passed `review-by` warns on the floor line and the `floorfleet` board and never
  changes the exit status"; 🟡 when undated, 🔴 when passed with its age.
- "A date that is present must be a real ISO 8601 one ... because a malformed date is a typo to be
  told about, not debt" (`_load_disabled`'s docstring); `floorfleet` drops a malformed date "so the
  board never compares garbage".
- A reasonless disable stays refused: "the reason is the whole point of making an opt-out visible".
- "The 2026-12-09 bar on `disabled.sizescan` is unchanged" and "still bites whatever date is
  declared".
- `GUARDS.md`: the `disabled` row is now "`review-by`, optional for now ... in the fleet view: yes:
  dated, 🟡 when undated, 🔴 when passed"; "making it a block needs a date and a fleet probe
  first".
- reviewscan: a scan that matches no dated record "prints 'not in scope' (exit unchanged)" and
  "counts any `NNNN-slug.md` records it did not read, instead of 'clean'"; `--json` carries
  `unread_numbered_records`.
- `CHANGELOG.md`: the summary of both halves, and that reading dates from numbered records "stays
  open".

## Scope

The widest the work admits: intent, decisions, assumptions, design, code, test code, docs and
real-world behaviour on a fixture and, read-only, on the local fleet. The lenses organise it; they
do not bound it. Anything not named a non-goal is in scope, and a non-goal that fences off the risk
is a finding.

**Non-goals:** turning the warning into a block (owed separately, by the delta's own account);
whether `scope` or `flags` narrowing counts as lowering (left open for the principal); reading a
numbered record's date from its body or history, or an adoption-pin scope (a policy choice left
open on `320/770`); the coverage-line work of `115/130` as such, except where it changes this
delta's lines; whether the principal's pick was the right one, as distinct from whether the delta
applies it faithfully.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself, before anything else. Is
   warn-first the right shape for a rule whose point is that a lowering expires? Is a parallel map
   (`disabled_review_by`) beside `disabled` the right design, or does it let a reader of
   `disabled` alone miss the date? For reviewscan, is a wording change with the same exit status
   the right minimum, and does "not in scope" say what it means where a reader meets it?
2. **Correctness & quality.** Re-drive each claim above against the code, on fixtures you build:
   every spelling of a `disabled` entry (string, object, partial object, malformed date, past date,
   future date) through `floor.py`'s load, run, render and `--json`, and through `floorfleet`; and
   reviewscan over zero, some and mixed dated and numbered records, on the human line and `--json`.
   Check that no branch changes an exit status the delta says it does not, and that no branch
   lowers or hides a check. The pointer asks two questions of its own; they are in the sibling.
3. **Completeness / harvest.** Every surface that describes a `disabled` entry or reviewscan's
   output (V3): find them with `coldsweep` (below). Candidates beyond the delta's own paths include
   `.github/workflows/floor.yml`, `docs/decisions/2026-10-03-0641-the-exception-register.md`,
   `docs/decisions/0008-enforcement-is-called-not-copied.md` and the floor's `--help` and selftest.
   One home (V4); no contradiction (V5), including between `GUARDS.md`'s table and its text.
4. **Security & privacy**, mandatory: at design altitude, whether the new shape gives a repo a
   quieter way to switch a guard off than it had, including a far-future `review-by`; whether a
   numbered record count or a fleet line can carry a private child's detail onto a public surface.
   At code altitude: config parsing of untrusted JSON (type confusion, a non-string date), and
   `count_unread_numbered`'s tree walk (what it descends into, symlinks, nested worktrees, cost).
   Aim `/security-review` at the delta's Python where it can reach it; it is the floor under the
   lens, never its discharge.

Run the standing checklist V1–V7 unasked (`REVIEW.md` § *The standing checklist*).

## Re-run obligation

Re-run, do not read. The brief-writer ran each line once, on 2026-11-14 UTC, from the worktree
root unless it says `cd tools`, and its results are held in the sibling. Read exit codes
explicitly. Check `uptime` first; run the heavy lines under `nice -n 10`, one at a time, in the
foreground with a long timeout (`test_floor` took about 210 s). Use the `python3` first on the
machine's `PATH` (3.14.6 when written); CI pins 3.12.

```
git merge-base --is-ancestor 06248fba HEAD; echo $?
python3 tools/coldsweep.py --root . --commit 06248fba > /dev/null; echo $?
python3 tools/reviewscan.py --selftest > /dev/null; echo $?
python3 tools/reviewscan.py --root . . ; echo $?
python3 tools/floorfleet.py --selftest > /dev/null; echo $?
cd tools && nice -n 10 python3 -m unittest test_reviewscan; echo $?
cd tools && nice -n 10 python3 -m unittest test_floorfleet; echo $?
cd tools && nice -n 10 python3 -m unittest test_report; echo $?
cd tools && nice -n 10 python3 -m unittest test_floor; echo $?
```

**Read-only live read:** `nice -n 10 python3 tools/floorfleet.py` (no `--remote`) reads the floor
configs of the repos beside this checkout and writes nothing. Its output names private repos:
keep it in your scratchpad and record **counts only** in the verdict, never a repo name. A
`--remote` read is also read-only and is optional; say whether you ran it. Nothing in this pass
writes to a live system; any check that would need a write is NOT RUN, with why.

The delta's recorded proofs (V2): "A read-only probe over 21 sibling floor configs found every one
loads identically before and after", and the fixture reproduction on `320/770` (two numbered
records, "clean" before). Re-check each by the cheapest read-only route (loading each sibling
config under `06248fba^` and `06248fba` from a scratch checkout, never by changing a child) and
say which you could not re-run and why.

## House rules for this run

- **Live systems:** only the read-only fleet read above. No live writes, no push from a child, no
  write to GitHub, no change to any child's config. A check that would need one is marked NOT RUN.
- Name your own review worktree in the verdict. It is read-only to you except for THIS file. Other
  sessions may be live on this machine: touch nothing outside your worktree and scratchpad.
- **Skip the session-log step of the read order** (`CLAUDE.md` step 4; `REVIEW.md` rule 2). If you
  read it anyway, disclose what you met.
- One heavy process at a time, foreground, with a long timeout. Never run an installed tool by bare
  name from `PATH`: use `python3 tools/<x>.py` from your worktree.
- This pass is pending while you run it: anything you write to the session log, the pointer or a
  commit subject before phase 2 names the sibling by file and count only.
- Absolute ISO 8601 dates from `date -u`; prose wrapped at ≤ 100 columns; NZ English. This repo is
  PUBLIC: quote no secret, email address, private repo name or path, and name no child repo.
- Review deep, not fast: a finding needs a probe or a re-driven claim behind it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content; the deferred material lives in the sibling .deferred.md under the rule-1 split, opened only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`, every prior
verdict in `docs/reviews/`, this brief's sibling (a held-back file, now folded below the
verdict under *Deferred sibling*; by count: 12 questions, 11 facts), every item under `docs/roadmap/160-doctrine-review-owed/`
beyond its title, every commit's message body, and these records beyond the `sed` ranges in *The
acceptance test*:

- `docs/roadmap/320-child-filed-findings-via-pointing-up/800-a-floor-disabled-entry-has-no-end-date.md`
  (line 8 onward)
- `docs/roadmap/320-child-filed-findings-via-pointing-up/770-hand-up-reviewscan-reads-numbered-decision-records-as-none.md`
  (line 26 onward)

`020/170` is not barred: its later lines are another session's application of the same pick, not
this delta's account. The delta's own `CHANGELOG.md` entry, docstrings and doc paragraphs carry
the author's account of why; they are the delta, and reading the delta is never barred.

Sweep with `coldsweep`, never a hand-written exclusion:

```
python3 tools/coldsweep.py --root <your-worktree> \
  --also-exclude docs/roadmap/160-doctrine-review-owed \
  --also-exclude docs/roadmap/320-child-filed-findings-via-pointing-up/800-a-floor-disabled-entry-has-no-end-date.md \
  --also-exclude docs/roadmap/320-child-filed-findings-via-pointing-up/770-hand-up-reviewscan-reads-numbered-decision-records-as-none.md \
  'disabled\.|"disabled"|`disabled`|review-by|not in scope|unread_numbered'
```

`--include-barred` only with disclosure in the verdict.

## Process

**Phase 1 (act 1).** Reproduce the floor first; work the lenses, your own assumptions and the re-run
list. Append your verdict below a `---` divider in THIS file: provenance repeated (how you were
spawned, your tier, any orchestrator, what you read, the UTC day), per-lens answers, V1–V7 each
answered or discharged with grounds, each load-bearing assumption damaged or confirmed with its
probe, a per-claim ledger, findings with stable IDs (prefix `DE`: `DE1`, `DE2`, …) and severities
(MAJOR / MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL line with counts, a
re-run ledger and a follow-up checklist. Then STOP: act 1 is committed, unrevised, **before** the
sibling is opened. Edit no other file.

**Phase 2 (act 2).** Open the sibling and the barred records; screen the delta's commit body;
append `### Reconcile` beneath your verdict, with per-finding notes against the sibling's questions
and the author's account, any finding formed at reconcile marked as such, and the overall line
restated. Never revise act-1 text. Then fold the sibling in below the reconcile and delete it.

The work is a gate and a guard's report, doctrine by function, so every finding is the principal's
to decide (rule 3): record all, apply nothing. Counsel per finding is welcome, labelled as counsel
and kept beneath it.

---

## Verdict (act 1, written 2026-11-22 UTC before the sibling was opened)

**Overall: PASS-WITH-FINDINGS — 0 MAJOR · 5 MODERATE · 6 minor · 1 note.** The delta does what
its two items asked, in the shape both filed, and every recorded proof reproduces. The findings
are about force and vocabulary, not mechanics: the new end date has weaker governance than the
advisory date it copies, a date nobody can reach reads as the healthiest line on the board, the
"not in scope" wording now collides with the house's coverage vocabulary, the count is absent on
the plane every commit runs, and the warn-first staging is itself an undated deferment of the
rule it serves. All are the principal's to rule (rule 3); counsel sits under each, labelled.

### Provenance (V7)

- **Reviewer:** Fable 5.1, the principal-named review tier, checked at selection. Review
  worktree: `/Users/mike/worktrees/fable/atelier-160-1270-2049/atelier`, at `32c35772`
  (`06248fba` is an ancestor: `git merge-base --is-ancestor` exit 0).
- **Spawn:** a headless per-pass orchestrator, session `92ba9071` (Opus 5.5), itself started by
  drain session `eca14b23` (Opus 5.5). Both are rule-4 off-tier orchestrators: they held the
  context partition, formed no finding and wrote no severity. Neither wrote the brief or any of
  the delta. I was not started or instructed by `48ef9c3e`, `58027096` or `d0ca5d24`.
- **Approval:** the principal's drain order of 2026-11-23 NZDT (2026-11-22 UTC), verbatim:
  *"Start a fable drain or whatever it is called now. Target 100% of weekly budget by 11.30am NZT
  todat"*.
- **What I read:** this brief; `docs/method/REVIEW.md` (lenses, checklist, rule 4); the three
  `sed` ranges in *The acceptance test*, exactly; the delta body-free through `coldsweep`
  (subject, stat, diff; 3 board files left out); the three tools, `report.py`, the four test
  files, `GUARDS.md` §§ 417–470, 522–569, 594–603, `tools/README.md`, `CHANGELOG.md`'s entry,
  the adopter template, the guards census rows, both workflows, and `docs/ROADMAP.md`'s index
  rows for 320/770, 320/800 and 160/1270 (titles and state only). Later commits named by the
  brief were read as subject and stat only (`git show --format='%h %s' --stat`). **Not read:**
  any session log, any prior verdict, the sibling, any commit body, the two records past their
  ranges, any item under `160/` past its title. The mirror sweep ran through `coldsweep` with the
  brief's three `--also-exclude`s (350 hits over 748 files; 1013 files excluded as barred); I did
  not pass `--include-barred`. The fleet board's footer printed the folder it searched; nothing
  from that read is recorded here but counts.
- **Review log:** a running record of every command, read and probe was kept outside the tree
  and is folded in at phase 2.

### Load-bearing assumptions, named first, then tested

| # | Assumption | Result |
|---|---|---|
| A1 | The pick needs reason AND end date; warn-first is a staging, and a staging needs a date | Damaged: the staging is undated (DE5) |
| A2 | The `disabled` date behaves exactly like the `advisory` date | Damaged: no `kind`, no move-later report (DE1); the board drops a malformed one (DE6) |
| A3 | A far-future date must not read healthier than no date | Damaged: it is the calmest line (DE2) |
| A4 | Every reader of `disabled` carries the date | Confirmed: floor line, floor `--json`, board, board `--json` (`asdict`) all carry it; only `moved_later` does not (DE1) |
| A5 | "not in scope" is distinguishable from "clean" on every surface the old word was read | Partly: human line and `--json` yes; the floor's board line is `✅ reviewscan enforced` either way (DE11); the words contradict the coverage line (DE3) |
| A6 | The new walk obeys the bounded-walk discipline and does not double-count | Damaged in the small: a third `rglob`, descends into `.git/` and nested worktrees (DE8) |
| A7 | No non-string `why` or `review-by` is silently accepted as valid | Partly: non-string dates are refused; non-string reasons pass as their repr (DE7) |

### Per-lens answers

1. **Approach.** Warn-first is a defensible fleet shape and the one the item filed (320/800 line
   4); its defect is that nothing dates it (DE5). The parallel map is the right design and every
   rendering reader carries it (A4), but the one *governance* reader, `moved_later`, was not
   taught it and `kind` is refused (DE1). For reviewscan, a wording change at the same exit
   status was the minimum option 320/770 offered and is faithful to it; the word chosen has since
   been given a precise, opposite meaning by the coverage work (DE3), and the board line a CI
   reader meets is unchanged (DE11).
2. **Correctness.** Every spelling and type of a `disabled` entry was driven through load, run,
   render, `--json`, `--list` and the board (ledger below): the parser's refusals are right, no
   branch touches an exit status, the sizescan bar still bites a dated entry, the `--list` state
   column is unchanged so both workflows' `awk` filters still skip a disabled check. Defects:
   the count is never computed on the staged plane (DE4); the board states "no end date" for a
   date the floor refuses (DE6); a non-string reason passes (DE7).
3. **Completeness.** Mirror sites: `tools/README.md`, `floor.py`'s docstring, `GUARDS.md`'s table
   and paragraph and `CHANGELOG.md` all carry the new spelling consistently. The adopter template
   never describes `disabled` at all (DE10). The docstring sentence 320/770 falsified still
   stands (DE9). The walk is a duplicate of one the tool already makes (DE8).
4. **Security & privacy.** *Design altitude:* the new shape does give a repo a quieter line than
   it had: before, every disabled check printed the same way; now a repo that writes
   `"review-by": "2999-01-01"` prints the calmest line on the board, calmer than a repo that
   wrote nothing (DE2). A count and a date carry no child detail onto the public board; the
   `why` text was already printed there. *Code altitude:* untrusted JSON is type-checked for the
   date and not for the reason (DE7); the tree walk follows no symlink but does enter `.git/` and
   nested worktrees (DE8). `/security-review`: **NOT RUN**, with grounds under V6.

### The standing checklist

- **V1** — Two claims outrun their evidence: the numbered count on the hook plane (DE4) and the
  "all predate the convention" sentence (DE9). The rest hold (ledger).
- **V2** — Every re-run line re-run, every one exit 0 (ledger). The sibling-config proof
  reproduces with 23 configs where the record said 21: all 23 load identically under
  `06248fba^` and `06248fba`, 0 errors. The 320/770 fixture reproduces as fixture B.
- **V3** — Swept with `coldsweep`. Updated: README, docstring, GUARDS, CHANGELOG. Unaffected and
  checked: both workflows' `--list | awk` filters (probe: the disabled row is still dropped),
  `docs/decisions/0008` (a frozen record; its "with a stated reason" is history). Silent: the
  adopter template (DE10). The census rows GRD17/GRD18 cite `_load_advisory` and `moved_later`
  only, which is accurate, and is DE1 seen from the other side.
- **V4** — One fact, one home: the spelling is stated in the docstring, README and GUARDS table,
  in agreement; `_days_over` stays a pinned twin by prior decision. Discharged.
- **V5** — Four internal contradictions: DE1 (GUARDS' date-governance text vs a date it does not
  govern), DE3 (the output's first line vs its coverage line, and vs GUARDS §594–603), DE5
  (GUARDS' ruling text vs its table), DE6 (the board vs the floor on a malformed date). Cross-
  references reached: `(320/800)` and `(020/170)` in GUARDS and README land on the open item and
  the pick line respectively.
- **V6** — `/security-review` NOT RUN: it reads the session's *pending* diff, and the only pending
  change in this worktree is the removal of the barred sibling, so aiming it would feed me rule-2
  material; the landed delta is not pending. The code-altitude pass was done by hand (lens 4).
- **V7** — Stated above.

### Per-claim ledger

| Claim (the delta's words) | Result |
|---|---|
| Legacy string or `{"why","review-by"}`; the bare string still parses | Holds (probe: 33 cases) |
| Missing or passed date warns on the floor line and the board, never changes exit | Holds: rc 0 in all four fixtures; `--json` carries `undated`, `expired`, `days_over` |
| 🟡 when undated, 🔴 when passed | Holds on the board; on the floor line undated keeps `⏭` with a `⚠️` note (DE10) |
| A present date must be a real ISO 8601 one | Holds for `floor.py`; `floorfleet` drops instead of reports (DE6) |
| A reasonless disable stays refused | Holds for blank/absent/null `why` (`validate`); a non-string `why` passes as its repr (DE7) |
| The 2026-12-09 bar on `disabled.sizescan` is unchanged and bites a dated entry | Holds (`test_floor` pins it; `validate` calls `disabled_barred` before any date logic) |
| GUARDS: `review-by` optional for now; fleet view dated/🟡/🔴 | Holds as written; is the staging DE5 names |
| reviewscan: zero matches print "not in scope", exit unchanged | Holds; the words collide with the later coverage vocabulary (DE3) |
| Counts `NNNN-slug.md` records it did not read; `--json` carries `unread_numbered_records` | Holds on the tree plane; **false on `--staged`** (DE4); over-counts in the single-file shape and across nested trees (DE8) |
| CHANGELOG: reading dates from numbered records stays open | Holds (320/770 open on the index) |

### Findings

**DE1 — MODERATE — the `disabled` end date is outside the date governance the `advisory` date
has.** `_load_disabled` refuses `kind` (probe: `has unknown key(s): kind`), and `moved_later`
loads only `advisory` from HEAD and iterates only `cfg.advisory` (`floor.py` 2595–2625). Probe: a
scratch repo whose HEAD declared both dates as 2027-01-01, with both moved to 2030-01-01 in the
working copy, got the move-later note for the advisory and nothing for the disabled check.
`GUARDS.md` § *Who may move a deferment's date* says an unlabelled `review-by` the children are
held to reads as a mandate and that a mandate moving later is reported at the commit. So the
*harder* opt-out now carries a date a child may push out silently, forever. V5; lens 1.
*Counsel:* accept `kind` on the `disabled` object with the same `DATE_KINDS`, extend
`moved_later` to `disabled_review_by`, pin both with tests; or write into GUARDS why a disabled
date is exempt.

**DE2 — MODERATE — a date nobody can reach reads as the healthiest line.** Board: `⏭ b disabled
until 2999-01-01 — obj` beside `🟡 a disabled — no end date …`; floor line: `[review by
2999-01-01]`, indistinguishable from `[review by 2027-03-01]`. No horizon check exists for either
`disabled` or `advisory` (the gap is pre-existing on `advisory`; the delta copies it onto the
check that is off entirely). Against the pick's own word, *expiring*, a 2999 date expires in form
only, and it is the one new way this shape makes a disabled check *quieter* than before (lens 4,
design altitude). *Counsel (the horizon is the principal's number):* refuse, or mark 🟡, a
`review-by` more than N months out, on both lanes; or print the span on the line so a long one is
seen.

**DE3 — MODERATE — "not in scope" now says the opposite of what the house means by it, and the
output disagrees with itself.** Fixture B (two numbered records): line 1 `✓ reviewscan not in
scope for decision records — 0 … matched (2 numbered … not read …)`; line 3 `coverage: 0 file(s)
opened · 0 check(s) run — ⚠️ scanned nothing: … covers nothing.` Since the delta, `GUARDS.md`
§594–603 and `report.coverage_line(not_in_scope=…)` define "not in scope" as *"the guard did not
fail to look, it had nothing to check"*, with no alarm. Over a repo with 167 numbered records the
guard had plenty to check and could not; that is the alarm case, and the `✓` glyph plus the
phrase claim the benign one. `--json` carries `scanned_nothing: true` but no `in_scope`. Two
states collapse into one wording: an empty decisions dir (fixture A, genuinely nothing) and a
numbered-only one (fixture B, the gap). V5; lens 1. *Counsel:* fixture A takes
`coverage_line(not_in_scope="no dated decision records")` and `coverage_dict(in_scope=False)`;
fixture B keeps the alarm vocabulary, loses the `✓`, and says "read none of N records: named by
number, no date to gate on".

**DE4 — MODERATE — the count is never computed on the plane every commit runs.** `main`'s
`--staged` branch calls `_render` without `unread_numbered` (`reviewscan.py` 777–778). Probe: a
scratch repo with one numbered record staged printed the not-in-scope line with no count and
`"unread_numbered_records": 0`, a known zero that reads as "none". The CHANGELOG, README and
docstring state the count without qualifying the plane. On the tree plane the count appears only
in the zero-match branch; a mixed repo (this one: 8 numbered, 8 dated) never hears of its numbered
records on the human line, only in `--json`. V1. *Counsel:* count staged paths whose parent is a
decisions dir and whose name matches `NUMBERED_NAME`; test it; qualify the docs or print the
count on the clean line too.

**DE5 — MODERATE — the warn-first staging is itself an undated deferment of the rule it serves.**
`GUARDS.md` §526–531 carries the pick as *"a lowering with no end date is not a lowering this
model allows"*; the table at §547 says `review-by` is *"optional for now"*; §566 says *"making it
a block needs a date and a fleet probe first"*, and names no date and no item but the open
320/800. The house dated its own earlier stagings (C1's horizon 2026-09-01; the sizescan bar
2026-12-09); this one has no end. The fleet probe the paragraph asks for was run here read-only:
22 repo rows, 3 `disabled` entries fleet-wide, all three undated (🟡 as of 2026-11-22), none
dated, none expired; under `06248fba^` and `06248fba` all 23 sibling configs load identically.
So a block
would turn three entries red and nothing else; the cost is known and small. The item filed
warn-first (320/800 line 4) before the work, so this is disclosed staging, not a hidden cut, and
the principal has not ruled on the staging itself: his pick was *"Allow if declared + expiring"*.
V5; lens 1. *Counsel:* add a dated bar in the pattern of `DISABLED_BARRED_FROM` (warn until the
date, block after), with the date his; and put to him in one line whether warn-first until that
date is what his pick meant.

**DE6 — minor — the board tells a false story about a malformed date.** `floorfleet._disabled`
drops a `review-by` that is not a real ISO date and the board then prints `🟡 … disabled — no end
date` (probe: `"soon"`, an ISO-shaped day that does not exist in its month, an integer, and an
object with an unknown key all render so). Each of those is a `ConfigError` in `floor.py`, so the
child's floor is blocked while its board row says "add a date". The `_advisories` twin passes the
string through and `_days_over` prints "date unreadable"; `tools/README.md` §3156 states the house
rule for the wrapscan twin: *"An unreadable value is reported, never dropped"*. An object with no
`why` renders in the healthy `⏭ … until` style with an empty reason. V5. *Counsel:* keep the raw
string and print `review-by unreadable: 'soon'`, as the advisory and wrapscan lanes do.

**DE7 — minor — a non-string reason passes the "stated reason" gate as its repr.** Probe: legacy
`5`, `null`, `["a"]` and object `"why": 7`, `"why": {"a": 1}` load as reasons `"5"`, `"None"`,
`"['a']"`, `"7"`, `"{'a': 1}"`; `_load_advisory` has the same `str(decl.get("why"))`. Dates are
type-checked (`true`, an integer, a list are refused); `review-by` of `""`, `null` or `false` is
silently undated, indistinguishable from an omission. Lens 4, code altitude; pre-existing for the
legacy string, copied into the object form. *Counsel:* require `why` to be a non-blank string in
both loaders; treat a present-but-falsy `review-by` as the typo it is.

**DE8 — minor — a third full walk that enters `.git/` and nested worktrees, and counts the whole
directory in the single-file shape.** `count_unread_numbered` repeats the `rglob("docs/decisions")`
`find_records` and `find_briefs` already make (three walks per run; 42 / 14 / 10 ms on this tree,
unbounded elsewhere). Fixture G: records under `.git/x/docs/decisions` and `.worktrees/w1/…` were
counted (3 where the repo holds 1); `find_records` shares the walk, so it would *read* a dated
record there too (pre-existing). Fixture D: naming one numbered file reported `3 numbered …
not read`. Symlinks are not followed (fixture H), consistent with `find_records`. Lens 4, code
altitude; tests cover none of these shapes. *Counsel:* collect numbered names during
`find_records`'s walk, skip `.git` and registered worktrees, count only the named file in the
file shape.

**DE9 — minor — a sentence the hand-up falsified still stands.** `reviewscan.py` §83–84: records
named under the numeric scheme *"all predate the convention and are skipped by construction"*.
320/770 §16–19 measured 167 such records on one child with eleven from the last 30 days. The
delta appended a sentence after it rather than correcting it. V1. *Counsel:* "in this repo they
predate the convention; a child's may not (320/770)".

**DE10 — minor — the two surfaces and the adopter's home drift.** Floor line: mark stays `⏭` and
the note carries `⚠️ no end date … (020/170); warning only`; board: the mark is `🟡`;
`GUARDS.md`'s table describes the board only. The floor-line note cites `020/170`, an atelier
board number no child can resolve (advisory lines cite none). The adopter template
(`docs/build/templates/CONTRIBUTING.md` §58–100) documents `advisory`'s `review-by` and `kind` and
never shows a `disabled` entry, so a new adopter learns the new spelling only from `tools/README.md`
or the module docstring. V3. *Counsel:* one mark per state on both surfaces; drop the board
number from the child-facing line; add the `disabled` object to the template beside `advisory`.

**DE11 — minor — where a CI reader meets it, nothing changed.** Over a numbered-only tree the
floor's board line is `✅ reviewscan enforced`, identical to a full-cover clean; the new words are
in the scanner's passthrough stdout only. The floor reads a scanner's exit and its advisory count,
never its coverage line, so this is systemic to 115/130 and not the delta's doing, but it is the
worst case the brief names and the surface the brief's lens 1 asks about. *Counsel:* the floor
reads `scanned_nothing` from each scanner's coverage line (or `--json`) and marks the row 🟡 as
it does `partial`; one mechanism for every scanner.

**DE12 — note — the fleet, for the record.** Read-only local board: 22 rows; 3 `disabled` entries,
all undated, none expired; 4 advisory lines; 23 sibling floor configs load identically under the
parent and the delta commit (the record said 21; the fleet has grown). A `--remote` read was not
run: the local read answered every question this pass had, and the remote one adds a network
read with no new fact about the delta.

### Re-run ledger

| Line | Exit | Note |
|---|---|---|
| `git merge-base --is-ancestor 06248fba HEAD` | 0 | |
| `coldsweep --root . --commit 06248fba` | 0 | 717 lines; body not printed |
| `reviewscan --selftest` | 0 | |
| `reviewscan --root . .` | 0 | clean — 8 records, 254 briefs; coverage 262/262 |
| `floorfleet --selftest` | 0 | |
| `unittest test_reviewscan` | 0 | 70 tests, 14.7 s |
| `unittest test_floorfleet` | 0 | 127 tests, 17.5 s |
| `unittest test_report` | 0 | 110 tests, 14.6 s |
| `unittest test_floor` | 0 | 260 tests, 301 s under `nice -n 10`, load 9–10 |
| `floorfleet` (local, no `--remote`) | 0 | counts only, capture deleted |
| sibling configs under `06248fba^` / `06248fba` | — | 23 / 23 identical, 0 errors |
| `/security-review` | NOT RUN | pending diff is the barred sibling's removal (V6) |

Fixtures and probe scripts lived in the session scratchpad only; no file in the tree or in any
child was changed. Load was checked before each heavy run (`uptime`: 6.6–9.9).

### Follow-up checklist

- 🎯 Principal: DE5 (warn until a date, then block; is warn-first what the pick meant), DE2 (a
  horizon for `review-by`, both lanes), DE1 (may a child move a disabled date; `kind` on it).
- Build session, after his word: DE1, DE3, DE4, DE6, DE7, DE8, DE9, DE10; DE11 as its own item
  under 115/130.
- Act 2: reconcile against the sibling's 12 questions and 11 facts, the two records' author
  accounts and the commit body; nothing above is revised.

### Reconcile (act 2, 2026-11-22 UTC; act 1 is committed at `449f64a5` and unrevised)

Opened after act 1 landed: the sibling (12 questions, 11 facts, written 2026-11-14 UTC against
`58f612b7`), `320/800` from line 8, `320/770` from line 26, and the delta's commit body through
`git log -1 --format=%B 06248fba`. The body names its worker as Sonnet 5.5 in its trailer; the
brief's "Opus 5.5 queue run and the worker it dispatched" stands.

**Against the pointer's two questions.** Q1 (can the new shape lower a check silently): no new way
to switch a check *off* silently; one new way to make an off check *quieter* than before, the
far-future date (DE2), and one way to keep it quiet, a date pushed later with no line (DE1). Q2
(can a zero-record scan still read as a pass anywhere it is displayed): yes, on the floor's board
line, which is `✅ reviewscan enforced` either way (DE11), and in its own first glyph (DE3).

**Against the brief-writer's questions.**

- Q3 → DE11 and DE3, as found independently. The wording is visible only in reviewscan's own
  stdout (the hook's passthrough and the CI log), never on the floor's row.
- Q4 → the second half of DE4: for a repo that mixes the schemes the count lives only in `--json`;
  the gap `320/770` names shows only where no dated record matched. The author's landing note
  says so itself (*"the gap shows but is not closed"*), so this is disclosed scope, and DE4's
  hook-plane half, where the count is never computed, is the part the author did not know.
- Q5 (numbered records kept outside `docs/decisions/`): not probed in act 1. `find_records` has
  the same boundary, so the scan's scope and the count's scope coincide and the line claims nothing
  about trees it does not read ("0 … matched"). No finding; a repo that keeps records elsewhere is
  out of reviewscan's reach by construction, before and after the delta.
- Q6 → DE8, point for point: other checkouts' records under the tree are counted (fixture G),
  symlinks are not followed (fixture H), and the walk is a third full `rglob`.
- Q7 → DE7. Sharpened by the question: `_load_advisory` *refuses* a falsy `review-by` ("needs a
  `review-by` date") where `_load_disabled` reads it as undated; so the two spellings the delta
  says are shared differ on exactly this input. That contrast belongs in DE7's counsel: treat a
  present-but-falsy date as the typo it is, on both lanes the same way.
- Q8 → DE6, as found.
- Q9 → DE2, as found; `advisory` has no cap for the shape to have copied, which is why DE2 names
  both lanes.
- Q10 → DE5. The sibling's fact 7 and my fleet read agree: three `disabled` entries, all undated.
  Nothing carries the owed block to a date; `320/800`'s open line says the same in the author's
  words: *"the rule (`020/170`) says a lowering must expire, and a warning does not enforce
  that."*
- Q11 → **DE13, formed at reconcile (minor).** The heading *"Ruled 2026-11-09"* in `GUARDS.md`
  predates the delta: `git log -S` traces it to `44f66053` (2026-11-09), and `06248fba`'s GUARDS
  hunk does not touch it, so it is not this delta's. What is the delta's: the commit body calls
  the pick *"the rule that a lowering be declared, reasoned and expiring (320/800, 020/170)"*,
  and the author's `320/800` landing note *"the rule (`020/170`) says"*, with no 💬 mark and no
  "an answer, not a ruling", where `COMMUNICATION.md` §356–376 says the record states which it
  was. `GUARDS.md`'s own body says *"Mike answered"*. The CHANGELOG entry carries neither word.
  *Counsel:* the heading's class is the principal's to name (it predates the delta; an item of
  its own); the delta's two records can take the 💬 mark where they are next touched.
- Q12 → **DE14, formed at reconcile (minor).** No test pins the not-in-scope line's exact text
  (`grep` over `tools/test_*.py` for its wording: 0 files); `NotInScopeTest` asserts substrings
  ("not in scope", "2 numbered"), and the delta moved `test_report.py`'s reviewscan pin onto a
  one-record fixture, so the pin class that exists to hold a scanner's line stable now covers the
  branch the delta did not change and not the one it did. *Counsel:* a second pin in
  `TestScannerLinePins` for the zero-record output, zero briefs and one brief.

**Against the facts.** 1: reproduced; `test_floor` is 260 tests now (255 then) and took 301 s on a
loaded machine (209 s then); nothing failed. 2, 3: reproduced (probe cases "obj no why", "why
null", "obj empty", "obj date empty/null/false"). 4: reproduced on this repo itself (`--json`:
8 unread, "clean" on the human line). 5, 6: reproduced as fixtures B and E. 7: reproduced as
counts (22 rows, 3 undated `disabled`, none expired); I did not record which check. 8: checked
at act 2, atelier's own config has no `disabled` key. 9: reproduced; 254 briefs now (234 then).
10: see DE13. 11: consistent with the `--json` rows read in act 1 (`undated`, `review_by`,
`expired`, `days_over` present on the disabled row).

**Against the author's account.** The commit body's claims are the CHANGELOG's and were tested in
the ledger; its sibling probe ("21 … loads identically before and after") reproduces at 23. Its
*"so no repo goes red"* is DE5's premise, confirmed by the fleet read (three entries would turn
🟡, as they have) and left undated by the author on purpose, with the block kept open. `320/770`'s
note that the fix is *"the third option"* and *"minimum"* is accurate and is the shape DE3 and DE4
find wanting at the edges, not in substance. Nothing in the account changes a severity.

**Overall, restated: PASS-WITH-FINDINGS — 0 MAJOR · 5 MODERATE · 8 minor · 1 note** (DE13 and
DE14 added at reconcile; DE1–DE12 unchanged).

## Deferred sibling, folded below the verdict (orchestrator, 2026-11-22)

The text below is the brief's `.deferred.md` sibling, verbatim, held out of the review tree until
the reviewer's act 1 was committed (`449f64a5` on main) and released to the reviewer for act 2
only. Orchestrator session `92ba9071` folded it here unchanged and removed the sibling file; it
forms no finding and assigns no severity. The sibling's own headings are kept as written.

# Held back — a floor `disabled` entry takes an end date, and reviewscan's not-in-scope line

Opened only once the reviewer's own findings are durably written (`REVIEW.md` rule 1). A floor,
never a fence. Written by the brief-writer (`cclive` lists it as session `48ef9c3e`), which did not
author the delta. Nothing here is a finding: these are questions, and facts read off the machine.

## The pointer's own questions

1. Can the new shape lower a check silently?
2. Can a zero-record scan still read as a pass anywhere it is displayed?

## The brief-writer's questions

3. The zero-record line begins with the same ✓ glyph as the clean line, and the exit is 0 (fact
   5). Where the floor, CI or `floorfleet` shows reviewscan by exit status, does a not-in-scope run
   still render as a pass? Is the wording change visible anywhere but reviewscan's own output?
4. A repo with one dated record and many numbered ones prints "clean", and the human line does not
   mention the numbered records it skipped; only `--json` carries the count (fact 4). Is the gap
   `320/770` names closed for a repo that mixes the two schemes, or only for a repo with none
   dated?
5. `count_unread_numbered` looks only in `docs/decisions/` directories. A repo that keeps numbered
   records elsewhere gets "not in scope" with no count. Does the line then claim more than it
   knows?
6. `count_unread_numbered` walks `rglob("docs/decisions")` under each path. In a repo with nested
   worktrees or vendored trees under it, does it count other checkouts' records, follow symlinks,
   or cost a full tree walk on every run?
7. `review-by: ""` and `review-by: 0` load as undated, not refused (fact 3), while the docstring
   says a date that is present must be a real one. Is a falsy non-date "present"? Does the same
   hold for `advisory`, whose spelling this claims to share?
8. `floorfleet._disabled` drops a malformed date and shows the entry as 🟡 "no end date", while
   `floor.py` refuses the same config outright. Does the fleet board then describe a repo whose
   floor cannot load as merely undated?
9. Nothing caps how far ahead `review-by` may be set. Is a `disabled` entry dated decades ahead an
   expiring lowering under the principal's pick, *"Allow if declared + expiring"*? Does `advisory`
   have a cap this shape should have copied?
10. The local fleet holds three `disabled` entries, all undated, all the same check (fact 7). Is
    "warn-first so no repo goes red" grounded in a measured cost, and does anything carry the owed
    block to a date?
11. The pick in `020/170` line 121 is an answer, but `320/800` calls it "the rule" and the
    `GUARDS.md` heading reads "Ruled 2026-11-09" (fact 10). Does the delta's prose carry a pick as
    a ruling, against `COMMUNICATION.md`'s answer/ruling marks? (The heading may predate the
    delta; say which.)
12. `test_report.py`'s reviewscan pin was changed to feed one record, so the pin no longer covers
    the zero-record output. Does any test pin the not-in-scope line's exact text, as the clean line
    is pinned?

## Facts read off the machine (2026-11-14 UTC, worktree at `58f612b7`)

1. Re-run lines, all exit 0: `test_reviewscan` 70 tests OK; `test_floorfleet` 127 OK; `test_report`
   110 OK; `test_floor` 255 OK (about 209 s); `reviewscan --selftest`; `floorfleet --selftest`;
   `coldsweep --commit 06248fba`; `merge-base --is-ancestor 06248fba HEAD`. Python 3.14.6.
2. A `disabled` object with no `why`, a blank `why`, or `{}` is refused by `Config` load:
   "disabling 'spellscan' needs a stated reason". A blank string is refused the same way.
3. `{"why": "x", "review-by": ""}` and `{"why": "x", "review-by": 0}` both load, with no entry in
   `disabled_review_by`, so both read as undated.
4. reviewscan on a fixture with one dated record (with a review line) and two `NNNN-slug.md`
   records: exit 0, head line "✓ reviewscan clean — 1 post-2026-07-21 decision record(s) carry a
   review line; …", no mention of the two numbered records.
5. reviewscan on a fixture with only two numbered records: exit 0, "✓ reviewscan not in scope for
   decision records — 0 post-2026-07-21 dated record(s) matched (2 numbered NNNN-slug record(s) not
   read: they carry no date to gate on); nothing was checked for a review line. …"
6. reviewscan on a fixture with only one pre-boundary dated record: exit 0, the not-in-scope line
   with no count.
7. `floorfleet.py` (local, no `--remote`): exit 0; three `disabled` lines, all 🟡 "no end date",
   all `licenscan`; none dated, none expired. (Repo names withheld: this file is public.)
8. atelier's own `.atelier-floor.json` has no `disabled` key.
9. `reviewscan --root . .` on atelier: exit 0, "clean — 8 post-2026-07-21 decision record(s) …;
   234 review brief(s) …". atelier also holds `NNNN-slug.md` records (for example
   `docs/decisions/0008-enforcement-is-called-not-copied.md`), not counted on that line.
10. `020/170` lines 120–121 mark the principal's 2026-11-09 word with 💬 as an answer to options a
    queue run offered, "an answer, not a ruling", and quote the pick. `GUARDS.md` line 489:
    "### Ruled 2026-11-09: a repo may lower a check's response, declared and expiring".
11. `floor.py --json` serialises each result by `__dict__`, so `undated`, `review_by`, `expired`
    and `days_over` appear on every result, disabled or not.

The probe script is not in the tree; each fact above is reproducible from the brief's re-run lines
or a fixture of a few lines.

## Review log (reviewer, verbatim; private while the pass ran, opened at the fold)

Form fixes at the fold, by the orchestrator: allow-markers appended to five lines that commit gates
read as a phone number or as dates (probe values and a ruling's line range); no word of the log
changed.

# Review log: atelier 160/1270 cold pass (Fable 5.1)

Worktree: /Users/mike/worktrees/fable/atelier-160-1270-2049/atelier (HEAD 32c35772)
Reviewer: Fable 5.1, spawned by per-pass orchestrator 92ba9071 (Opus 5.5), under drain
session eca14b23 (Opus 5.5). Public-safe log: commands, files, evidence only.

## Act 1

- 2026-11-22T20:50Z `uptime`: load 6.62 11.29 11.59 (high; several passes run). One heavy
  process at a time under `nice -n 10`.
- `git merge-base --is-ancestor 06248fba HEAD` -> exit 0 (delta in tree). HEAD 32c35772.
  `git status --short`: only ` D docs/reviews/...deferred.md` (the held sibling, removed on
  purpose by the orchestrator).
- python3 on PATH: 3.14.6 (brief wrote against 3.14.6; CI pins 3.12).
- Read brief in full (272 lines). Read docs/method/REVIEW.md: outline, § four lenses, § standing
  checklist V1-V7, § what the verdict names.
- Printed the acceptance-test lines exactly as the brief names them: `sed -n '120,121p'` of
  020/170 (the pick *"Allow if declared + expiring"*, option text: written reason AND end date,
  visible in the fleet view); `sed -n '1,7p'` of 320/800; `sed -n '1,25p'` of 320/770. Nothing
  beyond those ranges.
- `python3 tools/coldsweep.py --root . --commit 06248fba` -> exit 0; 717 lines captured to
  scratchpad `delta.txt` (subject, stat, diff; body not printed; 3 board files left out). Read in
  full. Stat: 10 files, +429/-28.
- `git log --oneline 06248fba..HEAD -- tools/floor.py tools/floorfleet.py tools/reviewscan.py`:
  14 later commits touch the three tools (ef4972e6 .. 55c7d409, incl. aca05c14, cf648679,
  ba55be27). 641f017f (named by the brief) is NOT in that list; checked separately below.

### My load-bearing assumptions (named before reading HEAD or any account)
A1. The principal's pick requires BOTH a reason and an end date for any lowering; the delta makes
    the date optional (warn). The delta's own filing (320/800 L1-7) names warn-first as the shape.
    So the question is whether warn-first is a faithful staging of the pick or a quiet weakening,
    and whether the path to the block is dated/tracked.
A2. The end date on `disabled` should behave exactly like the end date on `advisory` (same parser
    rules, same horizon rules, same expiry comparison, same marks), else V5 bites.
A3. A far-future `review-by` must not read as healthier than an undated one on any surface.
A4. The parallel map `disabled_review_by` must be carried by EVERY reader of `disabled` that
    renders or exports it (floor render, floor --json, floorfleet render, floorfleet --json if any,
    hook output), else a reader of `disabled` alone misses the date.
A5. reviewscan's "not in scope" must be distinguishable from "clean" on every surface where the
    old "clean" was read: the human line, --json, the floor's one-line summary of the scanner,
    and the coverage line added later (aca05c14).
A6. `count_unread_numbered` must obey the bounded-memory / bounded-walk rule the same tool
    already honours (test class `BoundedMemory`, 020/380), and must not double-walk or descend
    into .git / nested worktrees.
A7. Untrusted config: every non-string `why`/`review-by` type is either refused or treated
    exactly as the bare-string legacy, never silently accepted as a date.

### Reads at HEAD (32c35772)
- tools/floor.py: Advisory class 380-406 (expired: `review_by < today`); _today/_days_over
  1423-1470; _load_disabled 1526-1570; _load_advisory 1573-1660 (requires why AND review-by,
  accepts `kind`); Config.load tail 2100-2135; validate 2220-2235 (blank disabled reason refused;
  disabled_barred); Result 2272-2330 (undated field); moved_later 2595-2625 (loads ONLY `advisory`
  from HEAD, iterates ONLY cfg.advisory); run disabled branch 2655-2675; render 2994-3080;
  --list 3701-3709 (prints name/state/origin/decl/why; state column unaffected by a date).
- tools/floorfleet.py: ChildFloor 266-310 (disabled_review_by field); _today/_days_over 863-890;
  _advisories 894-913 (passes a malformed date THROUGH as a string); _disabled 916-937 (DROPS a
  malformed date); _read_declarations 1003-1070; render 1342-1430; --json via dataclasses.asdict
  (1887-1907), so disabled_review_by is in the JSON.
- tools/reviewscan.py: BOUNDARY 129, RECORD_NAME 138, docstring 78-92 (still says numbered
  records "all predate the convention"); find_briefs/find_records/count_unread_numbered 405-480
  (three separate `rglob` walks); run 554-566; _render 591-661 (zero-record branch prints a
  hand-rolled "✓ ... not in scope" line then `report.coverage_line(0,0)` with NO `not_in_scope=`);
  main 740-790: the `--staged` branch calls _render WITHOUT `unread_numbered`.
- tools/report.py: clean_head 542; suppressed_line 593; coverage_line 609-644 (`not_in_scope=`
  form: "not in scope here: <why>", no alarm); coverage_dict 646-660 (`in_scope`).
- docs/method/GUARDS.md: § Who may move a deferment's date 417-470 (kind label; "a dated
  advisory ... takes an optional kind"; moved-later report); § Ruled 2026-11-09 522-540 ("a <!-- leakscan:allow:nz-phone: a ruling's date and a line range, not a phone number -->
  lowering with no end date is not a lowering this model allows"); lowering table 544-549;
  disabled paragraph 566-569 ("warning only; making it a block needs a date and a fleet probe
  first"); coverage vocabulary 594-603 ("not in scope" = "the guard did not fail to look, it had
  nothing to check").
- docs/build/templates/CONTRIBUTING.md 58-100: describes `advisory` (why, review-by, kind), scope
  and flags; never describes a `disabled` entry's spelling. skills/: no `disabled` mention.
- docs/method/census/2026-11-16-1204-...md rows GRD17, GRD18, GRD20, GRD24 (177-188): GRD17/18
  cite `_load_advisory`/`moved_later` only; GRD20 "enforced, partial".
- .github/workflows/floor.yml 126 and ci.yml 103: `--list | awk '$2!="disabled" && $3!="local"'`.
- docs/ROADMAP.md 439, 441: 320/770 and 320/800 both still open `[ ]`; 262: 160/1270 `[~] ⏳`.
- CHANGELOG.md 715-727: the delta's entry; no later entry on a disabled block date.
- Later commits named by the brief: `git show --format='%h %s' --stat 641f017f` (subject+stat
  only): touches report.py and 9 scanners, NOT reviewscan.py. aca05c14: touches reviewscan.py
  (+8) and report.py (coverage line/dict). 55c7d409: reviewscan header warnings.

### Probes (scratchpad scripts; fixtures under the scratchpad only)
- probe_floor_load.py (floor.Config.load, 33 cases). Results: legacy string OK undated; legacy
  ""/"  " -> ConfigError "needs a stated reason" (validate); legacy int/null/list -> accepted,
  reason "5"/"None"/"['a']"; object full future/past/today -> OK with date; object no date -> OK <!-- datescan:allow: a fixture's probe value named in the reviewer's log, not a relative date -->
  undated; object no why / why null / {} -> ConfigError needs reason; why int/dict -> accepted as
  "7"/"{'a': 1}"; review-by ""/null/false -> OK silently undated; true/int/list/"next week"/
  "2999-01-01T00:00" -> ConfigError not ISO; "2026-02-31"/"0000-01-01" -> ConfigError not real; <!-- datescan:allow: deliberately invalid probe dates fed to the parser, quoted in the log -->
  `kind` key -> ConfigError unknown key; unknown scanner -> ConfigError; disabled=null/[]/0 -> {};
  disabled="x" -> ConfigError must be an object.
- probe_fleet.py (floorfleet._disabled, render, asdict, _read_declarations with a fake reader):
  malformed "soon", impossible "2026-02-31", int date, unknown-key object ALL render as <!-- datescan:allow: a deliberately invalid probe date, quoted in the log -->
  "🟡 ... disabled — no end date" (the floor would ConfigError on each); an object with no why
  renders "⏭ f disabled until 2999-01-01 — " (empty reason; the floor refuses it); 2999 renders
  as the calmest line "⏭ b disabled until 2999-01-01"; today's date -> "until" (not expired);
  past -> "🔴 ... EXPIRED 2020-01-01 (2517 days over)". asdict keys include disabled_review_by.
  _read_declarations wiring carries both maps.
- probe_reviewscan.sh (8 fixtures A-H): A empty dir -> "✓ not in scope ... 0 matched" + coverage
  "⚠️ scanned nothing ... covers nothing", exit 0. B numbered-only -> same with "(2 numbered ...
  not read)"; --json unread_numbered_records=2, coverage.scanned_nothing=true, no in_scope key.
  C numbered + 1 brief -> not-in-scope line, coverage "1 file(s) opened · 1 check(s) run" (no
  alarm). D single-file base naming ONE numbered record among three -> "3 numbered ... not read".
  E pre-boundary dated + numbered -> counts only the numbered. F odd names: counted
  `2026-0722-x.md`, `2026-07-x.md`; not counted `0001.md`, `00001-x.md`, `ADR-0001-x.md`,
  `2026-07-22.md` (the last is neither read nor counted). G: records under `.git/x/docs/decisions`
  and `.worktrees/w1/docs/decisions` ARE counted (3) — rglob descends into both; find_records
  shares the walk so it would read dated records there too (pre-existing). H: a symlinked tree is
  not followed (count 0), consistent with find_records.
- probe_floor_cli.sh (floor.py --plane ci on 4 disabled fixtures + a numbered-only tree), all
  rc=0: legacy "⏭ spellscan disabled (no prose here) ⚠️ no end date — ... (020/170); warning
  only"; future "[review by 2027-03-01]"; far "[review by 2999-01-01]" (indistinguishable from
  near-future); past "🔴 ... [review by 2020-01-01 — PASSED, 2517 days over]". --list prints
  `spellscan disabled fleet decl 1/5 ...`; the awk filter still drops it (count 0). --json rows
  carry review_by/expired/days_over/undated as claimed. Over the numbered-only tree the floor's
  board line is "✅ reviewscan enforced"; "not in scope" appears only in the passthrough stdout.
- probe_staged.sh: scratch git repo, one numbered record staged, `reviewscan --staged` -> "not in
  scope ... 0 matched" with NO numbered count; --json unread_numbered_records: 0. Walk cost on
  this worktree: find_records 42 ms, find_briefs 14 ms, count_unread_numbered 10 ms; 1 decisions
  dir here.
- moved_later probe (scratch git repo, HEAD has advisory+disabled review-by 2027-01-01, working
  copy moves both to 2030-01-01): moved_later -> note for the advisory only; nothing for the
  disabled date.
- reviewscan --root . --json . on the worktree: unread_numbered_records 8 (atelier's own 0001-0008
  ADRs), never mentioned on the human "clean" line (8 dated records matched).

### Re-run ledger (brief's list, from the worktree root / tools as the brief says)
- `git merge-base --is-ancestor 06248fba HEAD` -> 0
- `coldsweep --root . --commit 06248fba` -> 0
- `reviewscan --selftest` -> 0 · `reviewscan --root . .` -> 0 ("clean — 8 ... 254 brief(s)";
  coverage 262/262) · `floorfleet --selftest` -> 0
- `unittest test_reviewscan` -> 0, Ran 70 OK · `test_floorfleet` -> 0, Ran 127 OK ·
  `test_report` -> 0, Ran 110 OK · `test_floor` -> see below
- V2 sibling proof (v2_siblings.py: `git archive` of tools/ at 06248fba^ and 06248fba into
  scratch; every `*/.atelier-floor.json` beside the main checkout loaded by both): 23 configs
  found (the proof said 21), 23 load identically, 0 differ, 0 errors; 3 disabled entries across
  the fleet, 0 with a review-by. Names kept in scratch; counts only here.
- V2 fixture reproduction on 320/770 (two numbered records, "clean" before): re-driven as
  fixture B (now "not in scope", 2 counted). Under 06248fba^ the old wording is in the delta's
  own `-` lines of test_report.py ("clean — 0 post-... record(s)"), so the "before" is read from
  the delta, not re-run (the old tool is in scratch/old if needed).
- `unittest test_floor` -> exit 0, Ran 260 tests in 301 s (nice -n 10; load 9.8 before, 9.9
  after). `DisabledEndDateTest` present at HEAD (grep count 1).
- Live fleet read: `nice -n 10 python3 tools/floorfleet.py` (local, no --remote) -> exit 0, to
  scratch; counts: 22 repo rows; 4 lines containing " disabled" of which 3 are
  "🟡 ... disabled — no end date", 0 EXPIRED, 0 "until", 0 barred; 4 advisory lines. Capture
  deleted (`ls` confirms). Its footer printed the search folder; not recorded.
- `/security-review` NOT RUN: the session's pending diff is only the removal of the barred
  sibling (`git status`: ` D ...deferred.md`); aiming the scanner would feed me rule-2 material.
  Code-altitude pass done by hand (type confusion probe, tree-walk probe, symlink probe).
- 2026-11-22T21:12Z act 1 appended to the brief (verdict, provenance, assumptions table, lens
  answers, V1-V7, claim ledger, DE1-DE12, re-run ledger, follow-ups). Overall PASS-WITH-FINDINGS:
  0 MAJOR, 5 MODERATE (DE1-DE5), 6 minor (DE6-DE11), 1 note (DE12).
- Status line updated to "ACT 1 WRITTEN ... reconcile (act 2) is owed". Gates run on the brief:
  see next entry.
- Gates on the brief (from the worktree root): `datescan --root . <brief>` first found 2 in my
  text (a relative "today" in DE5; the probe value "2026-02-31" quoted in DE6); both reworded, no <!-- datescan:allow: quotes a probe value and names a reworded word, in the log -->
  marker added; re-run -> "✓ datescan clean", 540 lines read, exit 0. `spellscan` and `wrapscan`
  exclude docs/reviews by their ignore files (coverage: 0 files), so they apply nothing here; a
  hand grep of my section for common US spellings found none; all non-table lines in my section
  measured ≤ 100 characters after one paragraph rewrap (awk's byte lengths over-count the em
  dashes and section signs).
- Tree state at the end of act 1: only the brief modified, plus the orchestrator's removal of the
  sibling; no other file touched; no commit, no push.
- ACT 1 SAVED 2026-11-22T21:13Z. Waiting for the orchestrator's message with the sibling's path.

## Act 2 (released by the orchestrator after act 1 landed at 449f64a5)

- `git status`: act 1 committed by the orchestrator (HEAD 449f64a5 includes it); the sibling
  still shows ` D` in the worktree (held outside the tree). Read the held sibling (12 questions,
  11 facts), `git log -1 --format=%B 06248fba` (body; trailer names Sonnet 5.5 as the worker),
  320/800 from line 8, 320/770 from line 26.
- `git log --format='%h %ad %s' -S'Ruled 2026-11-09: a repo may lower' -- docs/method/GUARDS.md`
  -> 44f66053 2026-11-09 (pre-delta); `git show --format= 06248fba -- docs/method/GUARDS.md |
  grep -c 'Ruled 2026-11-09'` -> 0. COMMUNICATION.md 356-376: ⚖️ ruling verbatim / 💬 answer
  "an answer, not a ruling", the record says which.
- `grep -l 'not in scope for decision records' tools/test_*.py` -> 0 files (no exact pin).
- atelier `.atelier-floor.json` keys: docs, licence, scope, visibility; no `disabled` (fact 8).
- Mapping: Q1->DE2/DE1; Q2->DE11/DE3; Q3->DE11,DE3; Q4->DE4 (mixed-repo half); Q5->no finding
  (scan and count share the docs/decisions boundary); Q6->DE8; Q7->DE7 (sharpened: advisory
  refuses a falsy date, disabled reads it as undated); Q8->DE6; Q9->DE2; Q10->DE5; Q11->DE13
  (new, minor: commit body and 320/800 landing note call the pick "the rule" with no 💬 mark;
  the GUARDS heading predates the delta); Q12->DE14 (new, minor: no exact-text pin of the
  not-in-scope line; test_report's pin moved to the one-record fixture). Facts 1-11 all
  reproduce or are consistent (counts differ only by growth: 260 tests, 254 briefs, 23 configs).
- `### Reconcile` appended to the brief; act 1 text untouched. Overall restated:
  PASS-WITH-FINDINGS, 0 MAJOR, 5 MODERATE, 8 minor, 1 note.
- Status line set to "REVIEWED, both acts ... 0 MAJOR · 5 MODERATE · 8 minor · 1 note". Gates on
  the final brief from the worktree root: datescan exit 0 clean (whole file read); spellscan and
  wrapscan exit 0 (docs/reviews is in their ignore files, so coverage 0; US-spelling grep of my
  sections by hand found none; all non-table lines in my sections ≤ 100 characters).
- Tree at close: only the brief modified (` M`) plus the orchestrator's sibling removal
  (` D`); the sibling was neither folded, copied into the tree nor deleted by me; no commit, no
  push. Scratch fixtures remain only under the session scratchpad; the fleet capture was deleted
  in act 1.
- ACT 2 SAVED 2026-11-22T21:18Z.
