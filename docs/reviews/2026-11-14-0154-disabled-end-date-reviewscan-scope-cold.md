# Cold pass — a floor `disabled` entry takes an end date, and reviewscan's not-in-scope line

**Board:** `docs/roadmap/160-doctrine-review-owed/1270-rule-4-cold-pass-queued-disabled-end-date-and-reviewscan-scope.md`
**Status:** BRIEF ONLY, not run. Written 2026-11-14 UTC by a headless Opus 5.5 brief-writer
(`cclive` lists it as session `48ef9c3e`). Queued, waiting on the principal's explicit approval of
Fable work; this brief is not that approval.

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
verdict in `docs/reviews/`, this brief's sibling
`docs/reviews/2026-11-14-0154-disabled-end-date-reviewscan-scope-cold.deferred.md` (a held-back
file; by count: 12 questions, 11 facts), every item under `docs/roadmap/160-doctrine-review-owed/`
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
