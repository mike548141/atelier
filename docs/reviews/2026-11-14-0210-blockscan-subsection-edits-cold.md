# Cold pass — `blockscan` reads edits inside mapped sub-sections, warning until 2027-01-11

**Board:** `docs/roadmap/160-doctrine-review-owed/1320-rule-4-cold-pass-queued-blockscan-subsections.md`
**Status:** BRIEF ONLY, not run. Written 2026-11-14 UTC by a headless Opus 5.5 brief-writer
(`cclive` lists it as session `99821c6a`). Queued, waiting on the principal's explicit approval of
Fable work; this brief is not that approval.

**Pass type:** code cold pass, per `docs/method/REVIEW.md` rule 4: self-authored guard code, the
first of six staggered checks that turn from warning to blocking on a date in code.
**Tier:** Fable 5.1, the principal-named review tier, checked at selection by whoever takes the
pass. A session that cannot run on it stops (rule 4).
**Size of this pass:** small to medium: one commit, about 430 added lines, of which 207 are the
scanner, 199 its tests, 29 its README section and 13 a `CHANGELOG.md` entry.
**Why it earns a review:** `blockscan` is the guard that keeps the doctrine a child inherits (the
floor block in `PROPAGATION.md` and the scaffold template) in step with the method docs it
summarises. It is a silent-failure surface twice over. A false negative leaves a doctrine edit
unpropagated while every check reads green, which is the exact gap this change closes; a false
positive, or a finding on the wrong bullet, becomes a red CI on 2027-01-11 that no flag can soften,
and the cheapest way past it is an allow marker that then hides real drift. The worst failure is a
check that reports **clean** over a subsection edit it claims to see, or one that, on its date,
blocks honest work and trains its readers to reach for the marker.

## Spawn provenance

- **Author of the work under review:** a principal-opened Opus 5.5 queue run, session `d0ca5d24`,
  2026-11-09 UTC, and the worker it dispatched (per the queue pointer). The author queued this pass
  and does not take it.
- **Who wrote this brief:** a headless brief-writer (`claude-opus-5-5`; `cclive` lists it as session
  `99821c6a`), started 2026-11-14 UTC by an estate health sweep, orchestrator session `58027096`
  (Opus), on the principal's instruction that a brief is written for every review known to be owed
  (Mike, 2026-11-14, verbatim: *"include all briefs are written where we know a fable review is
  required"*). Neither wrote any of this delta. **Off-tier for review, disclosed: the brief-writer
  forms no finding and writes no severity**, and stops after writing. It ran no review and used no
  Fable model.
- **Barred from running this pass:** session `99821c6a` and session `58027096` (whoever writes a
  brief does not run it), and session `d0ca5d24` with everything it started.
- **Contact, disclosed (rule 4):** the brief-writer's only instruction came from `58027096`: the
  item number, the pointer's opening sentence, and the rules of the sweep. It carried no framing of
  the work. The brief-writer had no contact with the author session or its worker.
- **Who reviews:** a fresh Fable 5.1 session started for this pass alone, by a session that passes
  rule 4's criterion. An orchestrator may hold the context partition and commit the records
  off-tier, only if it forms no finding, writes no severity, and is disclosed in the claim, the
  pointer and the verdict.
- ⚠️ **Brief-writer's exposure, disclosed** (rule-2 and author-account material met before writing):
  its launch prompt; `skills/review-brief/SKILL.md`; the queue pointer whole; **the intent records
  `320/340` and `320/810` whole**, including the author's landing notes; **the message body of
  `6a4eeee2`** (met through `git show`, before the body-free read); the delta through
  `git show` and `tools/coldsweep.py --commit`; the later `641f017f` change to `blockscan.py`
  body-free; the CI step; commit subjects through `git log`; and the unrun brief
  `2026-11-14-0158-cclive-machine-wide-live-work-cold.md` and the head of its sibling, read for
  house form. It opened **no prior verdict** and no session record. Its harness also loaded
  user-level and repo instruction files and a memory index, which hold private context this brief
  does not carry. Everything evaluative it formed is in the sibling.

## The acceptance test

Two sources, one his and one not:

- **His words** (2026-11-09, quoted in `tools/README.md` and the module docstring, and in the first
  bullet of `320/810`): *"all six, warnings at first and then move to blocking action. With a
  staggered turn on of each so they dont all hit at once"*. That is the order for the check's
  posture: warn first, then block, on a staggered date.
- **The defect it closes:** the rule compares only the lines between a mapped heading and the next
  heading of any level, so an edit inside an unmapped subsection of a mapped section changes
  nothing it can see. The intent record `320/340` found this by running the rule over its own
  sitting's doctrine commits, and records that the non-recursive slice exists for a reason: in
  `00-APEX.md` a section and its own subsection answer to *different* bullets.

The design (derive membership from the heading tree, by nearest mapped ancestor, rather than map
each subsection or add an opt-in `recursive: true`) and the date 2027-01-11 are **the run's
choices, not his**; the delta says so itself. Whether they are the right ones is yours to attack.

## What the work is

One commit on `main`. First confirm your tree has it:

```
git merge-base --is-ancestor 6a4eeee2 HEAD || echo "MISSING 6a4eeee2"
```

Nothing may print. If something does, merge `origin/main` into the review branch before starting,
because a tree without the delta has nothing to review. Read it body-free:

```
python3 tools/coldsweep.py --root . --commit 6a4eeee2 \
  --path tools/blockscan.py --path tools/test_blockscan.py \
  --path tools/README.md --path CHANGELOG.md
```

Plain `git show` is barred: it prints the message body before the diff, and reading is atomic
(rule 1). Always pass `--path`: the board commits that closed `320/340` and queued this pass are
barred until phase 2. Review each delta path at HEAD too. One later commit touched the scanner, an
unrelated coverage line (`641f017f`, board `115/130`, which wraps the new-side reader); read it the
same way where it meets this delta. Confirm what has landed since:

```
git log --oneline 6a4eeee2..HEAD -- tools/blockscan.py tools/test_blockscan.py \
  tools/blockscan_map.json .github/workflows/ci.yml
```

On 2026-11-14 UTC that printed only `641f017f`. Read `tools/blockscan_map.json`, the two
`blockscan` steps in `.github/workflows/ci.yml` and the mapped method docs as context: they are
what the check runs over.

## What the delta claims (extracted, not evaluated)

- **The gap is closed on both co-change planes.** `--staged` and `--against` compare every unmapped
  `##`-or-deeper subsection whose nearest mapped ancestor is the mapped heading; `--check` has
  nothing to compare.
- **The apex case still holds.** A subsection mapped to another bullet, or one beneath such a
  subsection, answers to that bullet alone, by the same nearest-ancestor reading `check_unmapped`
  uses.
- **Same remedies as a violation**: move the bullet in both the floor region and the template, or a
  reasoned `blockscan:allow` marker in the changed subsection or either new bullet. Both bullets
  moving reports `moved`, not a finding.
- **A separate finding kind**, `subsection`, so the two can be counted and judged apart.
- **A subsection added or removed in the commit counts as changed.** A mapped heading new in the
  commit is left to the direct rule.
- **The date**: until `SUBSECTION_WARN_UNTIL` (2027-01-11, UTC) the finding warns and exits 0; on
  and after it, it exits 1. No flag, environment variable or map key moves the date, and `--warn`
  does not soften it, so the CI step `--against HEAD^ --warn` turns red on that date.
- **`--json`** carries a `subsection` block (count, blocking, until), and `clean` turns false only
  from the date.
- **Atelier-only**, outside `tools/floor.py`'s registry: a child has no map, so a child's exit is
  unchanged.
- **Probes recorded:** 21 of 21 child checkouts exit 2 before and after; replayed over atelier's
  doctrine history, 14 of 124 commits would have warned, all real subsection edits; tests include
  the day of the turn.

## Scope

The widest the work admits: intent, decisions, assumptions, design, docs, code, test code and live
behaviour on this machine, including how the date reaches CI. The lenses organise it; they do not
bound it. Anything not named a non-goal is in scope.

**Non-goals:** the five other checks of `320/810` and their dates (their own passes are owed or
done); the direct co-change rule as it stood before this commit, except where the new check leans
on it or inherits its wiring; `641f017f`'s coverage line beyond where it wraps this delta's reader.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself, then attack at least
   these by probe:
   - **A1.** The nearest mapped ancestor is always the bullet a subsection edit answers to: no edit
     fires on the wrong bullet, fires twice, or fires on none.
   - **A2.** Keying a subsection by its heading text and its occurrence under one parent identifies
     the same subsection on the old and new sides, so a rename, reorder, insertion or duplicate
     heading neither hides a change nor invents one.
   - **A3.** Heading detection (fences, levels, setext, indentation) is the same in the new reader
     as in the rule's own slice and in `check_unmapped`, so the three agree on what a subsection
     is.
   - **A4.** `--against HEAD^` on CI sees every commit that reaches `main`, so on 2027-01-11 a
     subsection edit cannot land green.
   - **A5.** The date flips on the UTC day it names, on every runner, and nothing at run time moves
     it.
   - **A6.** Deriving membership from the headings is better than either candidate the item named.
   Ask too whether this is the right problem at the right altitude: is a dated, unsoftenable
   block the right shape for a check whose remedy is a hand-moved bullet?
2. **Correctness & quality.** Diff the commit; drive the scanner against scratch repos with a
   scratch map and scratch docs you build, on both planes, with the date patched both sides of the
   flip. Record each overclaim against the text that makes it: the module docstring, the help
   text, the README section, the exit-code table and the `CHANGELOG.md` entry.
3. **Completeness / harvest.** Every surface that states the date, the exit codes or the `--warn`
   posture says the same thing (V3, V4, V5). Tests that would stay green on a broken change:
   mutate the code in a scratch copy, never the worktree. Is a fresh fleet probe before the flip
   recorded anywhere it will be seen?
4. **Security & privacy** — mandatory. The scanner reads git objects at a revision the caller
   names, prints heading text and map paths, and runs on CI over every push. Check that the new
   finding's detail goes through the same control and bidi escaping as the rest of the output,
   that a hostile heading or map entry cannot widen what is read or printed, and whether a
   subsection-only edit is a new way past the guard. Weigh against OWASP ASVS input-handling and
   output-encoding items, checked, not recalled. `/security-review` reads the session's pending
   diff, not this delta: aim it only at a scratch clone holding the delta as pending changes, or
   discharge it by grounds.

Run the standing checklist V1–V7 unasked (`REVIEW.md` § *The standing checklist*).

## Re-run obligation

Re-run, do not read. The brief-writer ran each line below once on 2026-11-14 UTC, from the worktree
root, in the foreground, under a load average near 5 on 12 cores; its results are held in the
sibling. Read exit codes explicitly. `python3` on `PATH` is 3.14.6 on this machine.

- `cd tools && python3 -m unittest test_blockscan` (about 35 s under that load)
- `python3 tools/blockscan.py --selftest; echo $?`
- `python3 tools/blockscan.py --root . --check; echo $?`
- `python3 tools/blockscan.py --root . --against HEAD^ --warn; echo $?`, and the same with `--json`
- The recorded probes: the 21-child exit-2 probe and the 124-commit replay. Neither command is
  recorded; rebuild both, and say where your counts differ and why.

Run the tool from your worktree, never by bare name from `PATH`.

## House rules for this run

**Live systems:** none is needed. Child checkouts on this machine may be **read** for the fleet
probe; any probe that would write to a real repo, board or CI is **NOT RUN**: build the case in
your scratchpad and say which probes you could not build.

- Never print a secret, and name no private repo, host, client or private path. This repo is
  PUBLIC; a child seen in the fleet probe is referred to by count or type only.
- Name your own review worktree in the verdict; it is read-only to you except for THIS file. Other
  sessions are live on this machine: touch nothing outside your worktree and scratchpad, and delete
  your scratch repos when you finish.
- No git command that writes in the worktree beyond committing this one file at the end of each
  phase (or handing it to an orchestrator to commit). Never mutate the worktree's `tools/`.
- One heavy process at a time, foreground, long timeout, `uptime` first.
- This pass is pending while you run it: anything you write to the session log, the pointer or a
  commit subject before phase 2 names the sibling by file and count only.
- Skip the session-log step of the repo's read order: `docs/SESSIONS.md` is barred (below).
- Absolute ISO 8601 dates from `date -u`; prose wrapped at ≤ 100 columns; NZ English.
- Review deep, not fast: a finding needs a probe or a re-driven claim behind it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content —
the deferred material lives in the sibling .deferred.md under the rule-1 split, opened only
after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`, every prior
verdict in `docs/reviews/`, the queue pointer above, this brief's sibling
`docs/reviews/2026-11-14-0210-blockscan-subsection-edits-cold.deferred.md`, the message body of
`6a4eeee2`, the intent record
`docs/roadmap/320-child-filed-findings-via-pointing-up/340-blockscans-map-cannot-see-a-subsection.md`
beyond its opening paragraph (the defect as found), and
`docs/roadmap/320-child-filed-findings-via-pointing-up/810-build-six-checks-warn-first-staggered.md`
beyond its first bullet (the principal's 2026-11-09 words).

The delta's own text carries the author's account of why (the module docstring above all); it is
the delta, and reading the delta is never barred.

Sweep with `coldsweep`, never a hand-written exclusion:

```
python3 tools/coldsweep.py --root <your-worktree> \
  --also-exclude docs/roadmap/160-doctrine-review-owed/1320-rule-4-cold-pass-queued-blockscan-subsections.md \
  --also-exclude docs/roadmap/320-child-filed-findings-via-pointing-up/340-blockscans-map-cannot-see-a-subsection.md \
  --also-exclude docs/roadmap/320-child-filed-findings-via-pointing-up/810-build-six-checks-warn-first-staggered.md \
  --also-exclude docs/reviews/2026-11-14-0210-blockscan-subsection-edits-cold.deferred.md \
  '<pattern>'
```

`--include-barred` only with disclosure in the verdict.

## Process

**Phase 1 (act 1).** Read the acceptance test; reproduce the floor first; work the lenses, the
assumptions A1–A6 and your own, and the re-run list. Append your verdict below a `---` divider in
THIS file: provenance repeated (how you were spawned, your tier, what you read, the UTC day you ran
on), per-lens answers, the standing checklist V1–V7 each answered or discharged with grounds, each
load-bearing assumption damaged or confirmed with its probe, a commit ledger (`6a4eeee2`: read
body-free yes/no, findings by id), findings with stable IDs (prefix `SU`: `SU1`, `SU2`, …) and
severities (MAJOR / MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL line with
counts, a re-run ledger and a follow-up checklist. Then STOP: act 1 is committed, unrevised,
**before** the sibling is opened.

**Phase 2 (act 2).** Open the sibling and the barred records; screen the commit body; append
`### Reconcile` beneath your verdict: per-finding notes against the sibling and the author's
account, any finding formed at reconcile marked as such, and the overall line restated. Never
revise act-1 text. Then fold the sibling in below the reconcile and delete it.

**Who applies a finding.** `blockscan` is guard code that enforces doctrine (judged by function,
`REVIEW.md` rule 3): the author applies nothing on its own, and neither does the reviewer. Record
all; the findings are the principal's to decide, after a plain-language account. Counsel per
finding is welcome, labelled as counsel and kept beneath it.
