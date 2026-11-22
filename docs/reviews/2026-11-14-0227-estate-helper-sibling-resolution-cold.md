# Cold pass — `estate.py`, one helper for where `../<sibling>` lands

**Board:** `docs/roadmap/160-doctrine-review-owed/1360-rule-4-cold-pass-queued-estate-helper-sibling-resolution.md`
**Status:** PASS-WITH-FINDINGS (0 MAJOR, 1 MODERATE, 6 minor, 6 note). Act 1 run 2026-11-22 UTC
by a Fable 5.1 reviewer under off-tier orchestrator `5bb9889e`, in the principal's weekly drain of
2026-11-23 NZDT (drain session `eca14b23`); act 2, the reconcile against the sibling, 2026-11-22
UTC; sibling and review log folded below. Every finding that changes what a scanner reports is the
principal's to decide (rule 3); nothing applied. Brief written 2026-11-14 UTC by a headless Opus
5.5 brief-writer (`cclive` lists it as session `cdb0c296`).

**Pass type:** code cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable 5.1, the principal-named review tier, checked at selection by whoever takes the
pass. A session that cannot run on it stops (rule 4).
**Size of this pass:** small to medium: one commit, `c1af4465`, about 760 added lines, of which 218
are the new helper, 305 its tests, 109 changed in `pins.py` and the rest small call-site edits in
four tools, README sections and one changelog entry.
**Why it earns a review:** the helper sits under two floor scanners, `pathscan` and `linkscan`,
that every child runs through its hook and CI, and under the fleet views `pins`, `floorfleet` and
`signfleet`. It is a silent-failure surface. Every path it adds to `pathscan` can only *drop* a
finding, never raise one, so the worst failure is a missing reference that reads as found: the
scanner goes green on a link no reader can follow. The second worst is a fleet view whose default
search root moves, so that a fleet nobody found prints a plausible count as the whole fleet (the
class `pins.py` already records as PU-5).

## Spawn provenance

- **Author of the work under review:** a principal-opened Opus 5.5 queue run, session `d0ca5d24`,
  2026-11-09 UTC, and the worker it dispatched (per the queue pointer). The author queued this pass
  and does not take it.
- **Who wrote this brief:** a headless brief-writer (`claude-opus-5-5`; `cclive` lists it as session
  `cdb0c296`), started 2026-11-14 UTC by an estate health sweep, orchestrator session `58027096`
  (Opus), on the principal's instruction that a brief is written for every review known to be owed
  (Mike, 2026-11-14, verbatim: *"include all briefs are written where we know a fable review is
  required"*). Neither wrote any of this delta. **Off-tier for review, disclosed: the brief-writer
  forms no finding and writes no severity**, and stops after writing. It ran no review and used no
  Fable model.
- **Barred from running this pass:** session `cdb0c296` and session `58027096` (whoever writes a
  brief does not run it), and session `d0ca5d24` with everything it started.
- **Contact, disclosed (rule 4):** the brief-writer's only instruction came from `58027096`: the
  item number, the pointer's opening sentence, and the rules of the sweep. It carried no framing of
  the work. The brief-writer had no contact with the author session or its worker.
- **Who reviews:** a fresh Fable 5.1 session started for this pass alone, by a session that passes
  rule 4's criterion. An orchestrator may hold the context partition and commit the records
  off-tier, only if it forms no finding, writes no severity, and is disclosed in the claim, the
  pointer and the verdict.
- ⚠️ **Brief-writer's exposure, disclosed** (rule-2 and author-account material met before writing):
  its launch prompt; `skills/review-brief/SKILL.md`; the queue pointer whole; the first part of each
  intent record (`320/180` through its first two sections, `320/660` through the start of its
  addendum); the delta through `tools/coldsweep.py --commit` only (no commit body was read); the
  test names in `tools/test_estate.py`; commit subjects through `git log`; and, for house form, the
  brief `2026-11-14-0158-cclive-machine-wide-live-work-cold.md`, its sibling, its queue pointer and
  its session entry. It opened **no prior verdict**. Its harness also loaded user-level and repo
  instruction files and a memory index, which hold private context this brief does not carry.
  Everything evaluative it formed is in the sibling.

## The acceptance test

Two findings handed up by children, both in `docs/roadmap/320-child-filed-findings-via-pointing-up/`:

- **`320/180`:** the same scanner, over byte-identical files, reported a clean main checkout and a
  red linked worktree, because `../<sibling>` from a worktree climbs into wherever the worktree
  sits. The concurrency doctrine tells sessions to take a worktree by default, so the convention
  broke in the very mode the house prescribes.
- **`320/660`:** an operator who moves child repos into one folder per theme breaks every child's
  `../<sibling>` path and drops grouped children out of `pins`' default fleet view.

The delta claims to close the **tools half** of both and says plainly that it does not close the
rest (below). No ruling of the principal's fixes the design; the shape (one setting, in the same
two carriers as `ATELIER_TOOLS`) was one the child named, unevidenced. Judge the work against the
two problems and against its own claims; whether one helper is the right answer is yours to
attack.

## What the work is

One commit on `main`, `c1af4465` (2026-11-09). First confirm your tree has it:

```
git merge-base --is-ancestor c1af4465 HEAD; echo $?
```

It must print `0`. If not, merge `origin/main` into the review branch before starting, because a
tree without the delta has nothing to review. Read it body-free:

```
python3 tools/coldsweep.py --root . --commit c1af4465 \
  --path tools/estate.py --path tools/test_estate.py --path tools/pathscan.py \
  --path tools/linkscan.py --path tools/pins.py --path tools/test_pins.py \
  --path tools/floorfleet.py --path tools/signfleet.py \
  --path tools/README.md --path CHANGELOG.md
```

Plain `git show` is barred: it prints the message body before the diff, and reading is atomic
(rule 1). Always pass `--path`: the commit also edits the two intent records and the board index,
which are barred beyond what this brief quotes until phase 2.

Review each delta path at HEAD too. On 2026-11-14 UTC no commit after `c1af4465` had touched
`tools/estate.py` or `tools/test_estate.py`, but nine had touched the callers (`pathscan`,
`linkscan`, `pins`, `floorfleet`, `signfleet`, the README). Confirm what has landed since, and
read anything that touches a call into `estate` the same way:

```
git log --oneline c1af4465..HEAD -- tools/estate.py tools/test_estate.py tools/pathscan.py \
  tools/linkscan.py tools/pins.py tools/floorfleet.py tools/signfleet.py tools/README.md
grep -n "estate\." tools/pathscan.py tools/linkscan.py tools/pins.py tools/floorfleet.py tools/signfleet.py
```

## What the delta claims (extracted, not evaluated)

- **One root cause, one answer.** The worktree break and the group-folder break both come from
  reading a checkout's location as if it named the estate; `estate.py` is the one answer, and
  `pins` and `floorfleet` drop their twin `main_checkout` functions for it.
- **`main_checkout` names the main checkout from any linked worktree** through `git rev-parse
  --git-common-dir`, under the file walk's scrubbed git environment (a hook's exported `GIT_DIR`
  cannot redirect it); it returns the path it was given for a non-repo, for no git, and for a
  submodule's or bare repo's worktree, where no main checkout sits at `.parent`.
- **The setting.** `ATELIER_ESTATE_ROOT`, or else git config `hooks.atelierEstateRoot`, in that
  order; empty means unset; unset changes nothing for anyone; a value that is not an absolute
  directory is warned about once on stderr and ignored, "so a typo costs a warning and the old
  behaviour rather than a wrong answer".
- **`landings(root, target)` only ever adds places to look.** It is lexical plus one directory
  listing. From a worktree it reads the same path from the main checkout; with the setting it reads
  a single-climb `../<name>/…` under the estate root and under each group folder (a directory there
  that is not hidden, not a symlink and not a repo). Two or more climbs are left to the physical
  path.
- **`pathscan`:** a `..` token that resolved nowhere else gets one more try through `landings`,
  from the same anchors with the same `.md` retry; it "only ever drops a finding, and it runs only
  for a `..` token that failed everywhere else". A main checkout's results do not change.
- **`linkscan`:** a link target that does not exist but has a landing that does is reported
  `outside-root`, the verdict the same link already gets from a main checkout, so an allow marker
  scoped to `outside-root` holds in both.
- **`pins` `discover`:** with the setting on, a non-repo directory under a search root is walked
  one level deeper and only one; repos are never descended into; hidden and symlinked folders are
  skipped by name; a stderr line says what was walked and skipped. Unset, discovery and its output
  are unchanged. `floorfleet` and `signfleet` share that discovery and the new default root.
- **Cost:** a scan with no failing `..` token never runs git; one with such a token runs it once
  per root, whatever the number of tokens.
- **Stated residual:** existence only, so with two repos of one name in two group folders a
  reference resolves if either carries the file; a host with no parent checkout has nothing to
  land on.
- **Named as not done:** the onramp's drift-check command in the verbatim floor still fails from a
  worktree (`320/180`), and the children's own `../atelier` references (`320/660`) can only follow
  it. Both items stay open.

## Scope

The widest the work admits: intent, decisions, assumptions, design, docs, code, test code and live
behaviour on this machine. The lenses organise it; they do not bound it. Anything not named a
non-goal is in scope.

**Non-goals:** the halves the delta names as not done (the floor's drift-check command and the
children's own references), except where the delta's text describes them wrongly; the rest of
`pathscan`, `linkscan`, `pins`, `floorfleet` and `signfleet` beyond what calls into `estate` or
shares its discovery.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself, then attack at least
   these by probe:
   - **SB-A1.** A setting that is wrong but valid (an absolute directory that exists but is not
     the folder the operator means: an archive of old copies, a parent one level too high, a
     folder that holds clones at another commit) cannot make a real miss read as found.
     *(One of the two questions the pointer names.)*
   - **SB-A2.** The worktree resolution cannot escape the operator's folder: no layout of
     worktree, `.git` file, `commondir` or scan root makes `landings` look outside the folder that
     holds the repos, and a repo's own content cannot steer where it looks.
     *(The other question the pointer names.)*
   - **SB-A3.** `landings` only ever adds places to look, so the change can drop a `pathscan`
     finding but never raise one, and a main checkout's results with the setting unset are
     byte-identical to before.
   - **SB-A4.** Reporting a non-existent `linkscan` target as `outside-root` when any landing
     exists is the same verdict the main checkout gives, and never hides a link that is broken
     for every reader in a way the old `missing-file` verdict would have shown.
   - **SB-A5.** "Every non-hidden, non-symlink, non-repo directory under the estate root is a
     group folder" is a safe reading of an operator's working folder.
   - **SB-A6.** `pins` `discover` with the setting on finds every pinned child the operator has,
     counts none twice, and says on stderr enough for a reader to tell a missed group from an
     empty one; with it off, its output is unchanged.
   - **SB-A7.** The per-root view cache (keyed on the root and the environment variable) can never
     serve a stale answer within one process, including when the git config carrier changes.
   Ask too whether this is the right problem at the right altitude: whether a scanner should
   consult the machine's layout at all, given that a GitHub reader 404s on every `../` link
   whatever the layout.
2. **Correctness & quality.** Diff the commit; drive `estate.py`, `pathscan`, `linkscan` and
   `pins` live and against scratch layouts you build (a main checkout with a linked worktree
   elsewhere, a worktree nested inside its main checkout, a bare repo with a worktree, a
   submodule, a group folder, two same-named repos in two groups, a broken setting). Record each
   overclaim against the text that makes it: the module docstring, the `pathscan` and `linkscan`
   docstrings, the `pins` docstring and stderr lines, the three tools' `--help`, the README
   sections and the `CHANGELOG.md` entry. Check the cost claim by counting git runs, not by
   reading.
3. **Completeness / harvest.** Every surface that states the same fact (V3), one home (V4), no
   contradiction between the docstrings, README, changelog and code (V5). Every other tool that
   still reads a sibling or the main checkout its own way. Tests that would stay green on a
   broken change: mutate the code in a scratch copy, never the worktree.
4. **Security & privacy** — mandatory. The helper runs git against directories it is pointed at,
   reads git config, lists a directory it did not choose, and decides existence for paths built
   from file content a contributor controls. Check what a hostile `.git` file, `commondir`, repo
   config or group-folder name can make it run, read, list or print; argument injection into git
   from a path; and what the stderr lines expose of the operator's folder layout. Weigh against
   OWASP ASVS file-handling and input-validation items, checked, not recalled. `/security-review`
   reads the session's pending diff, not this delta: aim it only at a scratch clone holding the
   delta as pending changes, or discharge it by grounds.

Run the standing checklist V1–V7 unasked (`REVIEW.md` § *The standing checklist*).

## Re-run obligation

Re-run, do not read. The brief-writer ran each line below once on 2026-11-14 UTC, from the
worktree root (or `tools/` where shown), in the foreground, under a load average near 5 on 12
cores, with neither carrier of the setting present; its results are held in the sibling. Read exit
codes explicitly. `python3` on `PATH` is 3.14.6 on this machine.

- `cd tools && python3 -m unittest test_estate`
- `cd tools && python3 -m unittest test_pins`
- `cd tools && python3 -m unittest test_pathscan` and `python3 -m unittest test_linkscan`
- `cd tools && python3 -m unittest test_signfleet`
- `python3 tools/pathscan.py --root . .; echo $?` and `python3 tools/linkscan.py --root . .; echo $?`
- `python3 tools/pins.py; echo $?` (read its `pins:` stderr lines)

Run the tools from your worktree by path, never by bare name from `PATH`. Then run the two
scanners from the main checkout too, read-only, and compare the finding sets by file and token;
the main checkout may sit at a different commit, so account for content drift before calling a
difference a finding.

## House rules for this run

**Live systems:** read-only. Running the scanners and `pins` over this repo and the operator's
folder is a read. Setting `ATELIER_ESTATE_ROOT` in your own shell for one command is fine; any
probe that would write git config (`git config --global` or a real repo's config), move a real
repo, or create a group folder in the real working folder is **NOT RUN**: build it in your
scratchpad (scratch repos, a scratch working folder, a scratch `HOME` for global config) and say
which probes you could not build.

- Never print a secret, and quote no private repo name, host, client or private path. This repo is
  PUBLIC; a repo seen in live `pins` output is referred to by count or type only.
- Name your own review worktree in the verdict; it is read-only to you except for THIS file. Other
  sessions are live on this machine: touch nothing outside your worktree and scratchpad, and delete
  your scratch repos and fixtures when you finish.
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
`docs/reviews/2026-11-14-0227-estate-helper-sibling-resolution-cold.deferred.md` (now folded
below; by count: nine questions and a run record), the delta commit's message body,
and the two intent records beyond what *The acceptance test* above
summarises:
`docs/roadmap/320-child-filed-findings-via-pointing-up/180-sibling-path-convention-breaks-in-a-worktree.md`
and
`docs/roadmap/320-child-filed-findings-via-pointing-up/660-grouping-children-into-folders-breaks-the-sibling-convention.md`
(both carry the author's landing notes).

The delta's own text carries the author's account of why (the module docstring above all); it is
the delta, and reading the delta is never barred.

Sweep with `coldsweep`, never a hand-written exclusion:

```
python3 tools/coldsweep.py --root <your-worktree> \
  --also-exclude docs/roadmap/160-doctrine-review-owed/1360-rule-4-cold-pass-queued-estate-helper-sibling-resolution.md \
  --also-exclude docs/roadmap/320-child-filed-findings-via-pointing-up/180-sibling-path-convention-breaks-in-a-worktree.md \
  --also-exclude docs/roadmap/320-child-filed-findings-via-pointing-up/660-grouping-children-into-folders-breaks-the-sibling-convention.md \
  --also-exclude docs/reviews/2026-11-14-0227-estate-helper-sibling-resolution-cold.deferred.md \
  '<pattern>'
```

`--include-barred` only with disclosure in the verdict.

## Process

**Phase 1 (act 1).** Read the acceptance test; reproduce the floor first; work the lenses, the
assumptions SB-A1 to SB-A7 and your own, and the re-run list. Append your verdict below a `---`
divider in THIS file: provenance repeated (how you were spawned, your tier, what you read, the UTC
day you ran on), per-lens answers, the standing checklist V1–V7 each answered or discharged with
grounds, each load-bearing assumption damaged or confirmed with its probe, a per-commit ledger
(`c1af4465`: read body-free yes/no, findings by id), findings with stable IDs (prefix `SB`: `SB1`,
`SB2`, …) and severities (MAJOR / MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS /
FAIL line with counts, a re-run ledger and a follow-up checklist. Then STOP: act 1 is committed,
unrevised, **before** the sibling is opened.

**Phase 2 (act 2).** Open the sibling and the barred records; screen the delta's commit body;
append `### Reconcile` beneath your verdict: per-finding notes against the sibling and the author's
account, any finding formed at reconcile marked as such, and the overall line restated. Never revise
act-1 text. Then fold the sibling in below the reconcile and delete it.

**Who applies a finding.** `estate.py` is ordinary code, but it sits under two floor scanners
every child runs and decides what they call a finding, so treat a finding that changes what a
scanner reports as the principal's to decide (rule 3): record all, apply nothing. Counsel per
finding is welcome, labelled as counsel and kept beneath it.

---

## Act 1 — verdict, 2026-11-22 UTC

### Provenance (rule 4, V7)

- **Reviewer:** Fable 5.1 (`claude-fable-5-1`), tier checked at selection against the brief's
  **Tier** line. The judgement in every finding and severity below is this session's alone.
- **Spawn:** started by headless per-pass orchestrator session `5bb9889e` (Opus 5.5), itself started
  by drain session `eca14b23` (Opus 5.5), under the principal's drain order of 2026-11-23 NZDT
  (verbatim: *"Start a fable drain or whatever it is called now. Target 100% of weekly budget by
  11.30am NZT todat"*). <!-- datescan:allow: the principal's words, quoted verbatim --> Both
  orchestrators are off-tier and disclosed: they hold the context partition, form no finding and
  write no severity. Neither wrote the brief or the delta. I was not started or instructed by
  `cdb0c296`, `58027096` or `d0ca5d24`, the sessions the brief bars, nor by anything `d0ca5d24`
  started.
- **Orchestrator direction, in substance (rule 4 asks the reviewer to record it):** process only.
  The worktree path; `git -C` and absolute quoted paths; `/usr/bin/python3` for scripts; the brief
  and `REVIEW.md` as the rules; the barred set as the brief lists it, with the sibling removed from
  the worktree and git history, other checkouts, scratchpads and tmp out of bounds for it; a running
  work log at one named path outside the brief as the only other file I may write; what I may write
  in the brief (act 1 below a divider, the Status line, wrap at 100 columns, absolute dates, run the
  repo's gates); no commits, no git writes, no mutation of the worktree's `tools/`, no GUI, no live
  writes, read-only live reads allowed (the principal, 2026-11-09, verbatim: *"reads of live systems
  is fine as needed, Reviews that need writes should be de-priortised"*); public-repo hygiene
  (session ids only, no private repo names, hosts, clients or estate facts; live `pins` output by
  count or type only); load rules (`uptime` before heavy steps, `nice -n 10`, one suite at a time,
  single process); stop on a usage-limit error; act 2 only on receipt of the sibling's held path,
  with `### Reconcile` written by me and the fold done by the orchestrator. It carried **no question
  about the delta, no pointer to where the risk lives, and no request about any finding**. The full
  prompt is in the orchestrator's record; the work log (appended at the fold) holds every command.
- **Contact after the spawn:** none from any author session or the brief-writer.
- **Worktree:** `/Users/mike/worktrees/fable/atelier-160-1360-2247/atelier`, HEAD `24b8e2b7`,
  read-only to me except this file. `git merge-base --is-ancestor c1af4465 HEAD` exits 0.
- **Interpreter:** every `python3` line below ran as `/usr/bin/python3` (3.9.6) unless marked; the
  brief-writer's `python3` was 3.14.6, and `test_estate` was re-run under both.
- **What I read, in order:** the brief whole; `docs/method/REVIEW.md` (rules 1–4, the lenses,
  V1–V7); the delta body-free (`tools/coldsweep.py --root . --commit c1af4465` with the brief's ten
  `--path` arguments; coldsweep's footer: 3 board-store files left out, 0 rule-2 files touched); the
  HEAD state of every delta path and of every call into `estate`; `da6d8dfd` body-free (stat, and
  its `tools/test_estate.py` hunk only); the HEAD sources of `filewalk._git_env`,
  `pathscan._exists_under`, `linkscan.resolve`/`_within_root`; `instruments/ccclose` lines 1540–1575
  as file content; the tree-wide `coldsweep` sweeps named below. I skipped the session-log step of
  the read order. I opened no prior verdict, no intent record, no board item, no commit body and not
  the sibling. The harness loaded user-level and repo instruction files and a memory index before
  the brief; nothing in them concerned this delta. One Haiku web-fetch agent read two public OWASP
  ASVS pages for me (read-only, forms no finding).
- **Scope pin:** the delta is the fixed commit `c1af4465`; callers were also read at HEAD
  `24b8e2b7`. One commit after it touched a delta path's tests (`da6d8dfd`, the floor's drift check;
  it has its own queued pass, `160/1540`), none touched `tools/estate.py`.

### Lens 1 — approach and assumptions

**The right problem?** Partly. `320/180` is a real defect in the mode the house prescribes, and the
delta closes it for `..` tokens: the probes and the live comparison agree. But the module's framing,
*"TWO THINGS BROKE THE SIBLING CONVENTION, AND THEY ARE ONE ROOT CAUSE"*, is narrower than the
symptom. The live run from this worktree and from the main checkout, over byte-identical board
files, differs by five `pathscan` findings, none of them a `..` token: an in-repo reference to an
ignored, untracked directory that exists only in the main checkout (SB8). A checkout differs from
its main not only by where it sits but by what untracked content it holds, and the helper cannot see
that.

**The right altitude?** Not argued. `linkscan` already holds that a reader on GitHub gets a 404 on
every `..` link whatever the layout, and uses the helper only to keep its *rule name* stable across
checkouts, which is sound. `pathscan` keeps "exists somewhere on this disk" as the meaning of a `..`
token and makes that meaning layout-robust at the cost of two git runs, a setting with two carriers,
a directory listing, and a wider existence net. The layout-free alternative (an `outside-repo` kind
for a `..` token, allow-markable, no git, no setting) is not weighed anywhere in the delta's text,
and by the delta's own residual a fresh clone in CI still reports every `..` reference, so laptop
and CI disagree by design (SB10). The brief says no ruling fixes the design, so this is counsel, not
a defect.

**Load-bearing assumptions I name myself, then the brief's seven, each with its probe** (fixtures
built in my scratchpad under a scratch `HOME`; the probe scripts and every result are in the work
log):

- **A `.git` entry marks every repo, and a `.git` *directory* marks every checkout** — *Verdict:*
  **Damaged** · *Probe:* A repo made with `--separate-git-dir` has a `.git` file in its main
  checkout; its linked worktree's common dir is not named `.git`, so `main_checkout` falls back to
  the worktree itself and `pathscan` is clean from the main, red from the worktree (SB2). A bare
  `x.git` folder under the estate root has no `.git` entry and is read as a group folder (SB1).
- **A one-climb token names a sibling *repo*** — *Verdict:* **Damaged** · *Probe:* `../README.md`
  from a grouped child lands on `<root>/README.md` and on `<each group>/README.md` (SB1).
- **The main checkout's neighbourhood is the operator's** — *Verdict:* **Holds** · *Probe:* Only a
  write to the worktree's `.git` file or the gitdir's `commondir` moves it (SB-A2 below).
- **The scanned repo's own config cannot make git run code** — *Verdict:* **Holds by reading** ·
  *Probe:* `filewalk._GIT_SAFE` pins `core.fsmonitor=false`; `rev-parse` and `config --get` run no
  hook and no pager under `capture_output`. Not probed with a hostile config.
- **SB-A1 a wrong-but-valid setting cannot make a real miss read as found** — *Verdict:* **Damaged**
  · *Probe:* Setting = the correct root, with `archive/sibling/docs/old.md` a stale copy of a file
  the live sibling lost: `pathscan` from the child goes from 3 findings to 0; `linkscan` goes from
  `missing-file` to `outside-root`, and an `outside-root` allow marker then exits 0. Setting = a
  repo's own path: that repo and its non-repo subfolders become the group folders. Setting one level
  too high: lands through the extra level and through every neighbour of the estate. (SB1)
- **SB-A2 worktree resolution cannot escape the operator's folder; content cannot steer it** —
  *Verdict:* **Holds against content** · *Probe:* Rewriting a worktree's `.git` file (`gitdir:`) or
  its gitdir's `commondir` to another repo moves `main_checkout` and the landings there and drops
  the finding; both need write access to the operator's gitdir. Tracked content cannot carry a
  `.git` file: `git add -A` records the directory as a gitlink (mode 160000), `add -f evil/.git`
  exits 128 "in submodule", `update-index --cacheinfo evil/.git` exits 128 "Invalid path". A path
  never reaches git except as the value of `-C`; `main_checkout(Path("-c"))` falls back cleanly.
- **SB-A3 landings only add; main-checkout results unset are unchanged** — *Verdict:* **Holds** ·
  *Probe:* `pathscan._resolves` appends the new test after every existing anchor returned False;
  from a main checkout with nothing set, `landings` is `[]` (no main, no root). Live: the one `..`
  finding (`tools/README.md:68`) is identical from both checkouts; `linkscan` is 0 and 0. Cost is
  not unchanged (SB3), output is.
- **SB-A4 `outside-root` for a non-existent target is the main checkout's verdict and hides nothing
  the old verdict showed** — *Verdict:* **Holds without the setting; damaged with it** · *Probe:*
  Worktree cases match the main (tests, L1). With the setting and a stale copy, a link dead for
  every live reader reports `outside-root` and an `outside-root` marker silences it; the old
  `missing-file` would have shown (SB1).
- **SB-A5 every non-hidden, non-symlink, non-repo directory under the root is a group folder** —
  *Verdict:* **Damaged** · *Probe:* Archive folders, bare-repo folders and non-repo scratch folders
  all qualify (SB1). On this machine the main checkout's parent holds 33 directories, 30 repos, and
  3 non-repo folders holding nothing, so the setting would change nothing here; the rule is unsafe
  for an operator whose folder holds copies.
- **SB-A6 `discover` finds every pinned child, counts none twice, says enough on stderr; off,
  unchanged** — *Verdict:* **List holds; funnel damaged** · *Probe:* A repo reachable by a symlink
  at level 1 and physically inside a group is listed once and counted twice: stderr says *3 are git
  repos, 3 carry an atelier pin* for two children returned (SB7). Off: output unchanged (fixture and
  live run, no *grouped layout* line). A walked group prints its repo count, a skipped one its name,
  so a missed group is tellable from an empty one.
- **SB-A7 the view cache can never serve a stale answer in one process, including when the git
  config carrier changes** — *Verdict:* **Damaged, in one process only** · *Probe:* Key is `(root,
  $ATELIER_ESTATE_ROOT)`. Set `hooks.atelierEstateRoot` after the first `landings()` call: `[]`
  until `forget()`, then three landings. No shipped tool changes config mid-run; only a test can
  meet it (SB6).

### Lens 2 — correctness and quality

Does what it claims for the `..` case, from a linked worktree anywhere, from a worktree nested
inside its main checkout, from a scan root below the repo top, and for the bare, submodule and
non-repo fallbacks the docstring names. Overclaims, each against the text that makes it:

- `tools/estate.py` COST paragraph: *"runs it once per root"*: two git runs per root (`rev-parse`,
  then `config --get`), counted with a PATH shim; *"A scan with no `..` token that fails to resolve
  never runs git"*: true for `pathscan`, false for `linkscan`, which builds the view on its first
  missing target of any kind (two runs for one in-repo `missing-file` and no `..` link). (SB3)
- `tools/estate.py` docstring line 5: shared by four tools; `tools/README.md` and the code say five
  (`signfleet`). (SB4)
- The three `--help` texts, `pathscan`'s docstring step 5 and the README's `pathscan` paragraph name
  the environment carrier only; the git-config carrier is the one the module exists to add. (SB4)
- STATED RESIDUAL names two same-named repos in two groups; the class is any copy under the root
  (SB1), and a `--separate-git-dir` main checkout is unnamed (SB2).
- `tools/estate.py` *"ONE ROOT CAUSE"*: the untracked-content divergence stays (SB8).

Tests: all five suites green under 3.9.6 and `test_estate` also under 3.14.6 (ledger below). Seven
single-point mutations of a scratch copy: four are caught, three survive (SB6). `--json` and human
output of the scanners were read; `pins` stderr read live.

### Lens 3 — completeness and harvest

- V3/V4: `pins.main_checkout` and `floorfleet.main_checkout` delegate (good). `instruments/ccclose`
  `locateAtelier` (landed 2026-11-14 in `74a0ceaf`, after the delta) re-implements the setting with
  different meaning: environment carrier only, `<root>/atelier` only, no group folders (SB5). Other
  own reads of `--git-common-dir` at HEAD: `tools/deadhook.py:75`, `tools/stashscan.py:84`,
  `tools/treeline.py:82`, `tools/worktree.py:180` (the only one that predates the delta),
  `tools/floorhook.py:126`, `instruments/cclive:146`, `instruments/ccclose` (six sites). Whether
  each wants the main checkout or only the common dir is for the applier; `cclive:142` says it wants
  the parent of the main checkout, which is `estate.parent` in Python terms.
- The setting is documented nowhere a child operator reads (templates, `PROPAGATION.md`, skills);
  that is the open child half and a non-goal, and the pointer's two items stay open as the delta
  says. But `ccclose.1` and `ccopen.1` do document `ATELIER_ESTATE_ROOT`, with `ccclose`'s meaning
  (SB5).
- Term collision: `docs/method/PROPAGATION.md` uses *estate root* for the estate's private root
  repo; the setting uses it for the folder of repos. A setting pointing at that repo is
  valid-looking and reads the repo's subfolders as group folders (SB11).

### Lens 4 — security and privacy (V6)

Checked against OWASP ASVS 4.0.3 V12 and V5 (the 5.0 URLs 404'd; read by the Haiku agent): 12.3.1
(path traversal from filename metadata), 12.3.2 (local file inclusion), 12.3.5 and 5.3.8 (OS
command injection via file metadata; parameterised OS calls). No ASVS item covers symlink following
or disclosing paths on stderr.

- **Argument injection (12.3.5, 5.3.8):** every git call is an argv list with fixed subcommands; the
  only variable is the value of `-C`, taken from the operator's `--root` or the tool's own path,
  never from file content. Config key and `rev-parse` flags are constants. Holds.
- **Traversal / inclusion (12.3.1, 12.3.2):** content controls tokens and link paths; they reach
  only `Path.exists()` under anchors the operator owns plus the landings. A landing is lexical from
  the main checkout, so a many-climb token reads the same absolute path from the main as the
  physical path already did before the delta; no new reach. Group-folder landings are one climb,
  under directories the operator listed by setting the root. Existence checks follow symlinks, as
  `_exists_under` already did; `repo_parents` skips symlinks. Holds; the exposure is the false-found
  class in SB1, not a read of anything.
- **Steering by repo content:** a tracked tree cannot carry a `.git` file (gitlink, invalid path:
  probed), so the `.git`-file and `commondir` steer needs gitdir write access. Holds.
- **Code execution by a hostile repo config:** `core.fsmonitor` pinned false by
  `filewalk._GIT_SAFE`; `rev-parse`/`config --get` run no hooks. Held by reading, not probed.
- **stderr:** `estate` prints the typed value via `repr` (a newline is escaped); `pins` prints group
  and skipped names raw, and a folder named with a newline forges an extra `pins:` funnel line
  (SB9). Operator-owned names, operator's terminal, so a note. The new line discloses folder names
  (up to 12) and the pre-existing line already discloses the search root; nothing new leaves the
  machine.
- **`/security-review`: NOT RUN, by grounds.** The worktree's only pending change is the partition's
  deletion of the barred sibling (`git status --short` shows ` D docs/reviews/…deferred.md`); the
  scanner reads the pending diff and would have printed it to me before act 1.
- Threat enumeration at design altitude is absent from the delta's text (the docstring names cost
  and residuals, not what the helper trusts: the gitdir, the setting's value, the listing). Folded
  into SB1's counsel rather than a separate finding.

### Standing checklist V1–V7

- **V1** No claim stronger than its evidence: SB1, SB3, SB8 (cost and residual wording).
- **V2** Re-run every live-proven claim: ledger below, all re-run; one finding from a re-run (SB8,
  from the main-vs-worktree comparison the brief asked for).
- **V3** Swept to every mirror site: the setting's carriers are stated inconsistently across the
  surfaces that do name it (SB4); child-facing surfaces are the open half, discharged as a non-goal.
- **V4** One fact, one home: `ccclose` is a second home with a different meaning (SB5); *estate
  root* has two meanings (SB11).
- **V5** No internal contradiction: SB3 (text vs measured cost), SB4 (four vs five tools; one vs two
  carriers). Cross-references checked for the rule reached: `320/180` and `320/660` are cited where
  the text describes the problems they name; `PU-5` in `pins` reaches the wrong-denominator class it
  cites.
- **V6** Security and privacy: lens 4 above; scanner discharged by grounds.
- **V7** Provenance: above, and in the brief's own section.

### Per-commit ledger

- **`c1af4465`** — *Read body-free:* yes (`coldsweep --commit`, ten `--path` arguments, no board
  file) · *Findings:* SB1, SB2, SB3, SB4, SB6, SB7, SB8, SB9, SB10, SB11
- **`da6d8dfd` (after the delta; `test_estate.py` hunk only)** — *Read body-free:* yes · *Findings:*
  none here; own pass `160/1540`
- **`74a0ceaf` (after the delta; `ccclose` read as HEAD file content, not as a commit)** — *Read
  body-free:* n/a · *Findings:* SB5

### Findings

- **SB1 — MODERATE.** *Every non-hidden, non-symlink, non-repo directory under the estate root is a
  repo-holding folder, so any copy anywhere under the root makes a real miss read as found, and an
  `outside-root` allow marker then silences a link dead for every live reader.* `tools/estate.py`
  `repo_parents` and `landings`; `tools/linkscan.py` `_resolve_link`. Probe: with the setting at the
  correct root and a stale `archive/sibling/docs/old.md`, `pathscan` from a grouped child drops from
  three findings to none and `linkscan` moves from `missing-file` to `outside-root`, where the
  marker exits 0. Also lands: `../README.md` on `<group>/README.md`; a `bare.git` folder as a group;
  the setting one level too high, through every neighbour of the estate. The STATED RESIDUAL names
  one narrow case of this class. Opt-in and unset by default, which is why not MAJOR; on this
  machine the three candidate group folders are empty. *Counsel:* a group folder is a directory that
  holds at least one repo; a group landing counts only when its first component is a repo
  (`<group>/<name>/.git` exists); where two groups hold a repo of one name, report the ambiguity
  rather than resolve by existence; name the class in the residual. A finding that changes what a
  scanner reports: the principal's to decide (rule 3 shape).
- **SB2 — minor.** *A `--separate-git-dir` repo's linked worktree still diverges from its main
  checkout.* `_checkout_of` requires the common dir to be named `.git`; for this layout it is not,
  `main_checkout(worktree)` returns the worktree, and `pathscan` is clean from the main and red from
  the worktree: the `320/180` defect, kept. Fails safe (a finding stays a finding). Not among the
  named residuals; the docstring's *"Only a directory literally named `.git` sits inside a
  checkout"* is false for it. *Counsel:* name it, or read `core.worktree` from the common dir's
  config.
- **SB3 — minor.** *The COST paragraph is wrong twice.* Measured with a PATH shim: a failing `..`
  token costs two git runs per root, not one; `linkscan` runs both on its first missing target of
  any kind, `..` or not. *Counsel:* fix the words, or defer `root_setting` until a one-climb landing
  is asked for.
- **SB4 — minor.** *The setting is described inconsistently across its own surfaces.* `pins`,
  `floorfleet` and `signfleet` `--help`, `pathscan`'s docstring step 5 and the README's `pathscan`
  paragraph name `ATELIER_ESTATE_ROOT` only; the module, `pins`'s docstring, the README's `estate`
  section and the changelog name both carriers. The module docstring shares the helper with four
  tools, the README with five. An operator who set `hooks.atelierEstateRoot` reads `--help` as
  saying the default root is atelier's parent dir.
- **SB5 — minor** (HEAD state, after the delta). *`instruments/ccclose` `locateAtelier` is a second
  implementation of the setting with a different meaning:* environment carrier only,
  `<root>/atelier` only, no group folders; documented that way in `ccclose.1` and `ccopen.1`. A
  grouped operator who set the config carrier gets *no atelier checkout found* from `ccclose` while
  `pins` finds the fleet. Six further own reads of `--git-common-dir` in `ccclose`, one each in
  `cclive`, `deadhook`, `stashscan`, `treeline`, `worktree`, `floorhook`; which of them want the
  main checkout is for the applier. *Counsel:* one meaning, stated in `estate.py`, copied with a
  stamp where JavaScript cannot import it.
- **SB6 — minor.** *Three behaviours have no test.* Mutations of a scratch copy that leave
  `test_estate` green: `ups == 1` → `ups >= 1` (multi-climb tokens land under the root); the file
  and docs anchors dropped from `_lands_on_a_sibling` (root anchor only); the environment component
  dropped from the view cache key. Also: the cache ignores the git-config carrier within a process
  (SB-A7), reachable only by a test, and `forget()` exists for it.
- **SB7 — minor.** *`pins` grouped funnel counts a repo twice that it lists once.* The `.git` check
  precedes the symlink check at level 1, dedupe is on the returned dict only, so a symlink alias at
  level 1 plus the physical repo in a group prints *3 are git repos, 3 carry an atelier pin* for two
  children. The funnel line is the thing `PU-5` added to make the count honest. *Counsel:* count
  from `found` after the walk.
- **SB8 — note.** *The main checkout and a worktree still disagree over byte-identical files when a
  token names an ignored, untracked path present only in the main.* Live: five `pathscan` findings
  from this worktree and none from the main checkout, all `.claude/worktrees does not exist`, in
  five board files identical in both. Outside the delta's `..` claim, inside `320/180`'s symptom,
  and not a named residual; the *"ONE ROOT CAUSE"* framing overstates. *Counsel:* name it on
  `320/180`.
- **SB9 — note.** *`pins` prints group and skipped folder names raw on stderr;* a name carrying a
  newline forges a second `pins:` line. `estate` prints its value via `repr`. Operator-owned names.
  *Counsel:* `repr` or strip control characters, as `estate` does.
- **SB10 — note.** *The altitude choice is unargued.* `pathscan` keeps disk existence as the meaning
  of a `..` token and buys layout-robustness with git, a setting and a listing; `linkscan` already
  holds that every `..` is a 404 for a GitHub reader; a fresh clone in CI still reports every `..`
  reference by the delta's own residual. The layout-free alternative (an `outside-repo` kind,
  allow-markable, no git) is not weighed in the delta's text. Counsel, since no ruling fixes the
  design; the principal's to weigh.
- **SB11 — note.** *"Estate root" means two things in one repo:* `PROPAGATION.md`'s private root
  repo and this setting's folder of repos. A setting pointing at that repo's path is valid-looking
  and reads the repo's own subfolders as group folders. *Counsel:* a name that says folder-of-repos,
  or one definition in one home.

**Overall: PASS-WITH-FINDINGS — 0 MAJOR, 1 MODERATE, 6 minor, 4 note.** The `..` half of `320/180`
is closed as claimed and the fallbacks are safe; the group-folder half of `320/660` is built on an
existence rule wider than its stated residual, and that is the one change to what a scanner reports
that needs the principal's word before it ships as the convention.

### Re-run ledger (worktree `tools/` as cwd for the suites; `nice -n 10`; foreground; one at a time)

- **`/usr/bin/python3 -m unittest test_estate`** — *Result:* Ran 27 tests in 12.0s, OK · *Exit:* 0
- **same under `python3` 3.14.6** — *Result:* Ran 27 tests in 15.0s, OK · *Exit:* 0
- **`… -m unittest test_pins`** — *Result:* Ran 43 tests in 46.8s, OK · *Exit:* 0
- **`… -m unittest test_pathscan`** — *Result:* Ran 172 tests in 29.0s, OK · *Exit:* 0
- **`… -m unittest test_linkscan`** — *Result:* Ran 89 tests in 9.7s, OK · *Exit:* 0
- **`… -m unittest test_signfleet`** — *Result:* Ran 21 tests in 10.9s, OK · *Exit:* 0
- **`tools/pathscan.py --root . .` from the worktree** — *Result:* 99 findings, all `missing-path`,
  in records and the README's worked example · *Exit:* 1
- **`tools/linkscan.py --root . .` from the worktree** — *Result:* 1571 files, 1656 links, 4
  suppressed by marker · *Exit:* 0
- **`tools/pins.py` from the worktree** — *Result:* 33 entries, 29 git repos, 23 pinned; no *grouped
  layout* line (setting unset in both carriers) · *Exit:* 1
- **`pathscan` from the main checkout (read-only, at `dc07f9d6`, an ancestor; 50 files differ, 23
  under `docs/roadmap`)** — *Result:* 94 findings; the 5 worktree-only ones are SB8; the one `..`
  finding is identical on both sides · *Exit:* 1
- **`linkscan` from the main checkout** — *Result:* 0 findings, same as the worktree · *Exit:* 0

Load averages ran 7–9 on 12 cores through the suites (32 at the start of the pass, before any heavy
step). Scratch fixtures and the scratch `tools/` copy were deleted at the end of act 1.

### Follow-up checklist

- [ ] The principal rules on SB1 (the group-folder rule and the `outside-root` verdict on a
      landing); counsel beneath it. Rule 3 shape: record all, apply nothing until then.
- [ ] SB2, SB3, SB4, SB8: text and residual corrections in `tools/estate.py`, `tools/pathscan.py`,
      `tools/README.md`, the three `--help` strings; `320/180` gains the untracked-content residual.
- [ ] SB5: one meaning for the setting across `estate.py` and `instruments/ccclose`, with its man
      pages.
- [ ] SB6: three tests; SB7 and SB9: `pins` funnel count and stderr quoting.
- [ ] SB10, SB11: counsel for the principal when the child half of `320/660` is designed.
- [ ] Act 2: open the sibling and the barred records on the orchestrator's release, write `###
      Reconcile`, restate the overall line.

### Reconcile (act 2, 2026-11-22 UTC)

Opened on the orchestrator's release, after act 1 was committed as `b02232d3`: the held sibling (its
nine questions and its run record), the queue pointer `160/1360`, the intent records `320/180` and
`320/660` with the author's landing notes, the delta's commit body, and the two prior verdicts that
mention the items (`2026-09-25-0715` HF10 and `2026-11-09-0207`: passing references, nothing to
reconcile). The release message was process only. Act-1 text above is unrevised.

**Against the sibling's questions.** The brief-writer's nine questions and my findings overlap
heavily and disagree nowhere; where they overlap, act 1 carries the probe the sibling did not run.

- Q1 (an oracle in the repo's hands) is SB-A2: steerable only by a write to the gitdir, not by
  tracked content (gitlink / "Invalid path", probed).
- Q2 (two or more climbs from the main) is my L1 probe: `../../x` from a worktree reads the same
  absolute path the physical read from the main checkout already did. No new reach, no finding.
- Q3 (`linkscan` builds the view on any missing target) is SB3, measured: two git runs on one
  in-repo `missing-file` with no `..` link.
- Q4 (`outside-root` swallows `missing-file`) is SB1 and SB-A4. Its question, *was it suppressed
  before, from a main checkout?*: no. From the main checkout the grouped `../sibling` path does not
  exist physically either, so the old verdict was `missing-file`, which an `outside-root` marker
  does not match (L5a: unset exit 1, set exit 0).
- Q5 (the cache key) is SB6 and SB-A7, with one addition the sibling's wording invites: a fleet tool
  scanning several children is served correctly, because the key carries the root and each root's
  view reads that root's config; only a config change for the *same* root within one process is
  stale.
- Q6 (group folder by negation) is SB1 and SB-A5. The sibling names a folder of linked worktrees,
  which I did not: each worktree has a `.git` file, the folder holding them has none, so it is a
  group folder, and a worktree named after a sibling lands a reference at that worktree's commit.
  Same class, worth naming under SB1.
- Q7 (two definitions of a group folder) I did not raise. See SB12 below.
- Q8 (the fallback change for a submodule's or bare repo's worktree) I did not raise. See SB13
  below.
- Q9 (machine-local ignored files) is SB8. The brief-writer saw nine such references on 2026-11-14
  and asked whether it is harvest or a separate item; I saw five on 2026-11-22. The author's own
  account answers the routing: `320/180` was **closed** on 2026-11-16, so SB8's counsel to name it
  there is superseded. It wants its own item.

**Against the author's account** (commit body, `320/180` and `320/660` landing notes):

- The body's *"One root cause: the checkout's location was read as if it named the estate"* is the
  framing SB8 narrows. The author's own probe (29 child main checkouts unchanged; 4 child worktrees,
  `pathscan` findings only fell) is consistent with SB-A3 and does not claim worktree and main now
  agree, so there is no contradiction, only a residual the text does not name.
- *"7 of the 24 fail against the previous scanners"*: the suite had 24 tests on 2026-11-14 (sibling)
  and 27 on 2026-11-22 (`da6d8dfd` added three). Consistent with the run drift in the ledger
  (`test_pins` 37 → 43 with `--floor`; `pathscan` 88 → 99 as the board grew; `pins` 32/29/22 →
  33/29/23). Not re-run against the previous scanners: my mutation m1 is a different cut and happens
  to fail seven of the same suite's tests.
- The author's probe over 29 child main checkouts and 4 child worktrees was **not re-run** (V2): it
  reads 29 private repos under drain load, its results could be stated only as counts, and the class
  it checks is covered by the atelier main-versus-worktree comparison and the fixtures. Recorded as
  read, not verified.
- `320/180`'s closure chose `ATELIER_TOOLS` for the floor's drift check and says why the estate-root
  setting was not used: *"it names the folder, not atelier, and unset (the default) it would need a
  `../` fallback"*. That bears on SB5, SB10 and SB11: the setting's consumers are the three
  scanners, the three fleet views and `ccclose` (with its own meaning), and nothing child-facing.
  The reasoning also supports SB11's point that the name promises more than the folder.
- `320/660` lists *"read a list of group folders"* among the shapes the child named. That shape
  would have avoided SB1's negation rule; the author chose the negation and did not record why.
  Counsel under SB1 stands; the principal's to weigh.
- `320/660`'s landing note repeats the funnel claim (*"printing which group folders it walked and
  what it skipped"*); SB7's double count is not addressed there.
- No prior verdict bears on the findings; none reconciles away.

**Findings formed at reconcile** (from the sibling's floor, probed against the code I had already
read; marked as such):

- **SB12 — note, formed at reconcile.** *Two homes decide what a group folder is.*
  `estate._View.repo_parents` skips hidden, symlinked, non-directory and `.git`-bearing entries
  silently; `pins.discover` tests `.git` first, then hidden and symlinked, names the skipped, and
  warns on an unreadable folder. They differ on a symlinked repo at level 1 (`pins` counts it, as
  before the delta; `estate` would skip it) and on reporting. One fact, two homes (V4); the delta's
  own claim is *one answer*. *Counsel:* `pins` takes its group-folder test from `estate`.
- **SB13 — note, formed at reconcile.** *A behaviour change in `pins.main_checkout` and
  `floorfleet.main_checkout` is unnamed where their readers look.* For a submodule's or a bare
  repo's worktree the old twins returned the common dir's parent (`<super>/.git/modules` or the
  folder holding `x.git`); the new helper returns the path given. The new answer is the safer one,
  and `estate.py`'s `_checkout_of` says so, but the two wrappers' docstrings and the changelog
  present the move as a pure de-duplication. Documentation, not behaviour.

**Overall, restated: PASS-WITH-FINDINGS — 0 MAJOR, 1 MODERATE, 6 minor, 6 note** (act 1's 4 notes
plus SB12 and SB13, formed at reconcile). SB1 is unchanged by anything the sibling or the author's
account holds, and the sibling's own Q4 and Q6 reach the same class without a probe.

## Deferred sibling, folded below the verdict (orchestrator, 2026-11-22)

*Released to the reviewer only after its act-1 findings were committed (locally `b02232d3`, the
hash the reviewer's text cites; it lands under a new hash when rebased at this fold); folded here
verbatim (headings demoted two levels, 0 line(s) over 100 columns wrapped at word
boundaries, no word changed) and the sibling file removed, per the brief. The orchestrator,
headless Opus 5.5 session `5bb9889e` started by drain session `eca14b23`, held the partition,
formed no finding and wrote no severity; drain session `eca14b23` wrote no brief and no delta and
started no brief-writer for this pass.*

### Held back — do not open before your findings are durably written

Sibling of `docs/reviews/2026-11-14-0227-estate-helper-sibling-resolution-cold.md` (`REVIEW.md`
rule 1). Written 2026-11-14 UTC by the brief-writer (`cclive` lists it as session `cdb0c296`),
which authored none of the delta. Open this only after act 1 is committed. Everything here is a
floor, never a fence, and none of it is a finding: the brief-writer read the code once and probed
none of these past what is recorded below.

#### The brief-writer's own questions

1. **An oracle in the repo's own hands (SB-A2).** `main_checkout` and `_View` trust whatever
   `--git-common-dir` prints. A worktree's `.git` file and its `commondir` are local files; can a
   crafted layout name a "main checkout" anywhere on disk, so that `pathscan` reports a `..`
   reference as found because a file of that name exists at an arbitrary place? Is that reachable
   from content a contributor commits, or only from local layout?
2. **Two or more climbs from the main checkout.** The single-climb rule bounds only the
   group-folder landings. The main-checkout landing joins any `rel` onto the main checkout,
   however many `..` it has. Does `../../../x` from a worktree read somewhere the physical path
   from the main checkout would also read (same answer, fine), or somewhere above the operator's
   folder that the delta's "escape" question means?
3. **`linkscan` runs `landings` on every missing target**, not only on a target that leaves the
   repo. `landings` returns nothing for an in-repo target, but builds the per-root view (two git
   runs, `rev-parse` and `config --get` when the environment variable is unset) on first use. Does
   the cost claim ("a scan with no failing `..` token never runs git") hold for `linkscan`, or only
   for `pathscan`, whose call is guarded by `".." in token`?
4. **`outside-root` swallows `missing-file`.** A link that exists only in some *other* same-named
   repo in another group folder, or in an archive the setting points at, now reports
   `outside-root`. If that line carries an `outside-root` allow marker, the finding is suppressed
   entirely. Was it suppressed before the change, from a main checkout, for the same link?
5. **The cache key.** `_VIEWS` is keyed on the scan root and `ATELIER_ESTATE_ROOT` only; the git
   config carrier is read once into the view. Is there any in-process path (tests, a fleet tool
   scanning several children) where the config differs per repo but the key does not?
6. **Group folder by negation.** Every non-hidden, non-symlink, non-repo directory under the
   estate root becomes a place a sibling may land, including a downloads folder, a folder of
   linked worktrees, or a scratch folder holding stale clones of a repo. Is that SB-A1 in another
   form?
7. **Two definitions of a group folder.** `estate.repo_parents` and `pins.discover` each decide
   what a group folder is, with near-identical but separate code (one skips an unreadable folder
   silently, the other warns). One fact, two homes (V4)?
8. **A submodule's or bare repo's worktree.** The delta changes `floorfleet`'s and `pins`'
   `main_checkout` for those two cases from "the common dir's parent" to "the path given". Is that
   behaviour change named anywhere a reader of the fleet tools would see it?
9. **Machine-local files.** From the main checkout, `pathscan` resolved nine in-repo references
   (`.claude/worktrees`, `.claude/settings.json`) that the same scan from a worktree reported as
   missing: ignored local files present only in the main checkout. That is not this delta's `..`
   path, but it is the same class `320/180` reported (same scanner, same content, different
   verdict by checkout). In scope as harvest, or a separate item?

#### What the brief-writer ran, and what it got

All on 2026-11-14 UTC, foreground, load average 3.9 to 5.1 on 12 cores, neither carrier of the
setting present, from the review worktree at `d3293d93` unless stated.

- `cd tools && python3 -m unittest test_estate`: 24 tests, OK, exit 0, about 6 s.
- `test_pins`: 37 tests, OK, exit 0, about 29 s. `test_pathscan`: 172 tests, OK, exit 0, about 13 s.
  `test_linkscan`: 89 tests, OK, exit 0, about 6 s. `test_signfleet`: 21 tests, OK, exit 0, about
  8 s.
- `python3 tools/pathscan.py --root . .`: exit 1, 88 findings. `linkscan`: exit 0, 1230 Markdown
  files, 1620 internal links, 4 suppressed by allow marker (all `missing-file`).
- The same `pathscan` from the main checkout, at `2a6d7a41`: 79 findings. The difference was nine
  in-repo references to ignored local files (question 9) plus line-number drift in one README;
  no `..` reference differed.
- `python3 tools/pins.py`: exit 1 (at least one child not current). Funnel line: 32 entries, 29
  git repos, 22 carry a pin; no grouped-layout line, as expected with the setting unset.
- `git merge-base --is-ancestor c1af4465 HEAD`: exit 0. `git log c1af4465..HEAD` on the two
  `estate` files: empty; on the callers: nine commits.
- The `coldsweep --commit` line in the brief, as written: exit 0. The sweep line with the
  four `--also-exclude` paths: exit 0.

## Review log (reviewer, verbatim; private while the pass ran, opened at the fold)

*Form fixes only: headings demoted two levels; 120 line(s) over 100 columns wrapped at word
boundaries, no word changed. No public-repo gate blocked a token, so no placeholder was needed.*

### Review log — atelier 160/1360, estate.py sibling-resolution cold pass

Reviewer: Fable 5.1 (claude-fable-5-1). Spawned by headless per-pass orchestrator 5bb9889e (Opus
5.5),
started by drain session eca14b23 (Opus 5.5). Worktree:
/Users/mike/worktrees/fable/atelier-160-1360-2247/atelier
Brief: docs/reviews/2026-11-14-0227-estate-helper-sibling-resolution-cold.md
Interpreter for every python step: /usr/bin/python3 (brief says python3; noted).

#### Act 1

- 2026-11-22T22:53:20Z Read brief in full (lines 1-297). Read docs/method/REVIEW.md lines 1-460
  (rules 1-4, lenses, V1-V7).
- uptime at start: load 32 (12 cores). HEAD 24b8e2b7. `git merge-base --is-ancestor c1af4465 HEAD`
  exit 0.
- /usr/bin/python3 is 3.9.6; PATH python3 is 3.14.6 (brief says 3.14.6 on PATH; confirmed).
- `/usr/bin/python3 tools/coldsweep.py --root . --commit c1af4465 --path <10 delta paths>` >
  scratchpad/delta.diff,
  exit 0, 1045 lines; coldsweep footer: body not printed, 3 board-store files left out, 0 rule-2
  files touched.
  Read the whole diff (lines 1-1045). Delta = CHANGELOG +18, tools/README.md +42, estate.py +218
  (new),
  floorfleet -15/+8, linkscan +13, pathscan +33, pins +109/-63, signfleet +7, test_estate.py +305
  (new), test_pins +6.
- `git log --oneline c1af4465..HEAD -- <delta paths>`: 32 commits touch callers/README; only
  da6d8dfd touches
  tools/test_estate.py (+61, FloorDriftCheckFromAWorktree, the onramp half, own pass 160/1540);
  tools/estate.py
  unchanged since c1af4465, so the delta diff IS estate.py at HEAD. `git diff --stat c1af4465 HEAD`
  on callers:
  pins +122 (hunks at 117, 370, 510, 728-838 new --floor subcommand incl. a third
  `estate.parent(atelier)` call
  site, 859, 869: discover() body untouched), pathscan +45 (tally/coverage, not the resolver),
  linkscan +22,
  floorfleet +7.
- `grep -n "estate\." tools/{pathscan,linkscan,pins,floorfleet,signfleet}.py` at HEAD: call sites as
  in the
  delta plus pins.py:798 (--floor). `grep -rln "import estate"`: 5 callers + test_estate.
- filewalk.py:127-143: `_GIT_ENV_DROP = (GIT_DIR, GIT_WORK_TREE, GIT_INDEX_FILE, GIT_PREFIX)`;
  `_GIT_SAFE =
  ("-c", "core.fsmonitor=false")`. GIT_CONFIG_GLOBAL / GIT_CONFIG_NOSYSTEM pass through, so
  test_estate's
  `_hermetic_env` reaches estate's git calls (hermetic against the operator's real global config).
- `from __future__ import annotations`: present in pins, floorfleet, signfleet, pathscan, linkscan,
  filewalk;
  absent in estate.py, which uses only `set[str]` at runtime (3.9-safe) and string annotations
  otherwise.
  `(cd tools && /usr/bin/python3 -c "import estate, pins, pathscan, linkscan, floorfleet,
  signfleet")` -> ok on 3.9.6.
- coldsweep sweep 'ATELIER_ESTATE_ROOT|atelierEstateRoot' (barred excluded; the .deferred.md
  exclusion warns
  "matches no file", expected: it was removed from the worktree): 23 hits. Surfaces:
  CHANGELOG:555-556,
  tools/README.md:1112,1857,3039-3040, estate.py:21-22,55-56, floorfleet.py:1751 (--help),
  pathscan.py:176,
  pins.py:576-577,955, signfleet.py:312, board item 160/1540:19, instruments/ccclose:1545,1561 (+
  test,
  man pages ccclose.1:360,865, ccopen.1:248). No hit in docs/method, docs/build/templates, skills.
- da6d8dfd body-free via coldsweep: stat = CHANGELOG, docs/build/templates/CLAUDE.md,
  PROPAGATION.md, RECORD.md,
  skills/create-repo/SKILL.md, tools/README.md, tools/test_estate.py. Its CHANGELOG hunk: the
  floor's drift
  command finds the parent through ATELIER_TOOLS / hooks.atelierTools, NOT the estate-root setting.
- tools/README.md:3027-3052 estate section at HEAD: "used by pathscan, linkscan, pins, floorfleet
  and signfleet";
  the "What it does not do" paragraph was rewritten by da6d8dfd (drift check not keyed to it).
- tools/estate.py:3-6 docstring: "shared by pathscan, linkscan, pins and floorfleet" (signfleet
  absent).
- pathscan.py:1107-1118 `_exists_under` (exists, or extensionless + .md/.markdown retry);
  linkscan.py:578-584
  `resolve` (leading / -> root-relative, else md_file.parent / path); linkscan.py:686-696
  `_within_root`.
- Own-way main-checkout lookups at c1af4465 (`git grep -n git-common-dir c1af4465 -- tools
  instruments`):
  tools/worktree.py:180, instruments/cclive:146, instruments/ccclose:895,1693. At HEAD also:
  deadhook.py:75,
  stashscan.py:84, treeline.py:82, floorhook.py:126, ccclose:928,1554,2297,2735,2793,2813.
  instruments/ccclose:1547-1571 `locateAtelier` reads env ATELIER_ESTATE_ROOT only (no git-config
  carrier) and
  tries `<root>/atelier` only (no group folders); gained in 74a0ceaf (after the delta).
- --help at HEAD: pins, floorfleet, signfleet say "default: ATELIER_ESTATE_ROOT, else atelier's
  parent dir"
  (git-config carrier not named). pathscan/linkscan --help: 0 mentions of estate/worktree/sibling.
- docs/method/PROPAGATION.md:229,317,323,336-341: "estate root" there means the estate's private
  ROOT REPO, a
  different thing from the folder ATELIER_ESTATE_ROOT names.
- Pre-existing `..` tests: test_linkscan.py:294 `[x](../outside.md)`; test_pathscan.py:941 declared
  root
  `../outside`. test_pins.py:241 WorktreeResolution (PU-5) copies estate.py into its fixture tools/.
- My env: ATELIER_ESTATE_ROOT unset; `git config --get hooks.atelierEstateRoot` from the worktree
  exit 1 (unset).
- PROBES (scratch, scratch HOME, GIT_CONFIG_GLOBAL=empty file, GIT_CONFIG_NOSYSTEM=1,
  PYTHONDONTWRITEBYTECODE=1,
  /usr/bin/python3 3.9.6, importing the worktree's tools/estate.py read-only): scripts
  scratchpad/probe1.py
  (fixtures p1/) and probe2.py (p2/). Results, by layout:
  L1 main+worktree elsewhere: main_checkout(wt)=main; from main/sub too (raw --git-common-dir prints
  ../.git);
     landings(wt, ../sibling/docs/target.md)=[estate/sibling/docs/target.md]; from main []; wt/sub
     climbs
     from the repo top; two climbs from wt -> [L1/etc/hosts] (main.parent.parent/etc/hosts);
     inside-repo [].
     Worktree nested INSIDE main (main/.wt/n): main_checkout=main, landing correct. pathscan
     main/wt/nested/
     wt-sub all (0, []). linkscan main (1, [missing-file, outside-root]).
  L2 bare+worktree: common dir = bare.git -> main_checkout(bw)=bw, landings [] (safe fallback, as
  documented).
  L3 submodule: common dir = super/.git/modules/sub -> main_checkout=sub itself, landings [] (as
  documented).
  L4 --separate-git-dir: common dir = gd/sep.git for BOTH sep and its worktree sepwt;
  main_checkout(sepwt)=sepwt
     (fallback; the main is sep); landings []; pathscan sep (0,[]) vs sepwt (1,[missing-path]) ->
     the 320/180
     divergence persists for this layout. Not named in the residuals. CANDIDATE SB (minor).
  L5 SB-A1: (a) setting=the correct estate root, archive/sibling/docs/old.md stale copy, child in
  themeA
     referencing ../sibling/docs/old.md: pathscan unset (1, 3x missing-path); with setting (0, []).
     landings =
     [estate/sibling/.., estate/archive/sibling/.., estate/sibling/sibling/..,
     estate/themeA/sibling/..]
     (every non-repo dir under the root is a group folder, the non-repo sibling fixture included).
     ../README.md (one-climb FILE token) -> [estate/README.md, archive/README.md, sibling/README.md,
     themeA/README.md]. linkscan with `linkscan:allow:outside-root` marker: unset (1,[missing-file])
     ->
     with setting (0, []): a link dead for every live reader is silenced by an outside-root marker
     once a
     stale copy exists anywhere under the root. CANDIDATE SB (SB-A1/SB-A4/SB-A5).
     (b) setting=a repo's path: repo_parents=[main, main/docs]; (c) one level too high:
     repo_parents=[L5,
     L5/estate], lands through the extra level; (d) a bare.git folder is read as a group folder.
  L6 SB-A2: (a) rewriting wt/.git `gitdir:` to another repo's gitdir -> main_checkout(wt)=that repo,
     landings move to its neighbourhood, pathscan finding dropped. (a2) same via the gitdir's
     commondir file.
     Both need write access to the operator's gitdir, not repo content. (b) tracked content cannot
     carry a
     .git file: `git add -A` records evil as a gitlink (160000); `add -f evil/.git` exit 128 "in
     submodule";
     `update-index --cacheinfo evil/.git` exit 128 "Invalid path". SB-A2 HOLDS against contributor
     content.
     (c) group folder named "x\npins: searched FORGED": pins stderr carries a forged line beginning
     "pins: searched FORGED (1); skipped ..." (names printed raw); estate's warning prints the value
     via repr
     (newline escaped). main_checkout(Path('-c')) -> fallback, no injection ( -C takes it as the
     dir).
  L7 SB-A6: alias -> themeB/alpha symlink at level 1 + physical alpha in group; grouped: returned
     [alpha, standalone] (2) but stderr "3 are git repos, 3 carry an atelier pin" (the .git check
     precedes the
     symlink check, so a symlinked repo at level 1 is counted; dedup is on the list only).
     Ungrouped: 2/2,
     consistent. CANDIDATE SB (minor).
  L8 SB-A7: one-climb token, root in g/main, estate root set by git config AFTER the first
  landings() call:
     before []; after config without forget() [] (STALE); after forget() [L8/sib/docs/t.md,
     L8/g/sib/..,
     L8/sib/sib/..]. Key = (root, env var) ignores the config carrier. Only reachable inside one
     process.
     warn-once: 3 bad values (two equal) -> 2 warning lines.
  L9 cost (PATH shim logging every git argv): pathscan no `..`/resolving `..` -> estate 0 git; one
  failing
     `..` -> rev-parse 1 + config 1 = 2 estate git runs; ten failing tokens in five files -> still
     2.
     linkscan with ONE in-repo missing-file and NO `..` link -> 2 estate git runs; nothing broken ->
     0.
     Docstring says "runs it once per root" and "no `..` token that fails ... never runs git".
     CANDIDATE SB
     (minor, V1). pins --head count inconclusive (fixture exited before discovery; not pursued).
- Live census (read-only, os.scandir on the main checkout's parent; counts only): 34 entries, 33
  dirs, 0 symlinks,
  0 hidden dirs, 30 repos, 3 non-repo non-hidden dirs (= group folders if the setting were set),
  holding 0
  subdirectories and 0 repos. So on this machine the setting would add 3 empty group folders and
  change nothing.
- RE-RUN 1 (worktree tools cwd, PYTHONDONTWRITEBYTECODE=1, nice -n 10, /usr/bin/python3 3.9.6):
  `python3 -m unittest test_estate` -> Ran 27 tests in 12.0s, OK. Load 7.5 before.
- MUTATIONS (scratchpad/mutate.py: fresh copy of tools/ per mutation under scratchpad/tools_mut,
  test_estate run
  there; the 3 FloorDriftCheckFromAWorktree ERRORs in every run are a scratch artefact: they read
  TOOLS.parent/docs/method/PROPAGATION.md, absent beside the copy; they pass in the worktree):
  m1 landings always [] -> 7 failures (suite is live). m3 repos read as group folders -> 1 failure
  (caught).
  m9 linkscan landing branch removed -> 3 failures (caught). m10 pins group walk no longer skips
  atelier -> 1
  failure (caught). UNCAUGHT: m2 `ups == 1` -> `ups >= 1` (multi-climb tokens land under the estate
  root) 0
  failures; m4 pathscan `_lands_on_a_sibling` anchors = [root] only (file and docs anchors dropped)
  0 failures;
  m7 cache key drops the env carrier 0 failures. CANDIDATE SB (test gaps, minor).
- RE-RUNS 2-5 (same form): test_pins Ran 43 in 46.8s OK; test_pathscan Ran 172 in 29.0s OK;
  test_linkscan Ran 89 in
  9.7s OK; test_signfleet Ran 21 in 10.9s OK. Parity: test_estate under PATH python3 3.14.6 Ran 27
  in 15.0s OK.
- RE-RUN 6 worktree: `pathscan.py --root . .` exit 1 (99 findings, all missing-path in docs/roadmap
  records and
  one tools/README.md:68 `../../tools/x.py` worked example; records never come clean per its own
  docstring);
  `linkscan.py --root . .` exit 0 (1571 files, 1656 links, 4 suppressed by missing-file markers).
- RE-RUN 7: `pins.py` exit 1 (58 stdout lines; stderr "searched <root> — 33 entries, 29 are git
  repos, 23 carry
  an atelier pin"; no "grouped layout" line, setting unset). Names withheld.
- RE-RUN 8 main checkout (read-only, at dc07f9d6, an ancestor of wt HEAD 24b8e2b7; 50 files differ,
  23 under
  docs/roadmap): pathscan 94 findings vs wt 99; only-wt 5, all "`.claude/worktrees` does not exist"
  in five board
  files that are byte-identical in both checkouts (diff --stat empty); `.claude/worktrees` is an
  ignored,
  untracked directory present in the main checkout and absent in the worktree. The one `..` finding
  (tools/README.md:68) is identical on both sides. linkscan 0 vs 0. So: `..` tokens now agree across
  checkouts;
  in-repo tokens naming untracked paths still diverge (320/180 symptom by another mechanism, outside
  the
  delta's `..` claim, not named as a residual). CANDIDATE SB (note/minor).
- ASVS (Haiku web-fetch agent, read-only; 5.0 URLs 404, read 4.0.3 V12 and V5): 12.3.1 path
  traversal from
  user-submitted filename metadata; 12.3.2 LFI; 12.3.5 and 5.3.8 OS command injection via file
  metadata /
  parameterised OS calls; no ASVS item on symlink following or on disclosing filesystem paths in
  logs.
- /security-review NOT RUN: `git status --short` in the worktree shows ` D
  docs/reviews/...deferred.md` (the
  partition's deletion) as the only pending change; the scanner reads the pending diff, which would
  print the
  barred sibling. Discharged by grounds; lens 4 run by hand (L6, L9, ASVS above).
- ACT 1 WRITTEN 2026-11-22T23:15Z-23:35Z UTC: appended below a `---` divider to the brief; Status
  line
  replaced (ACT 1 WRITTEN ... PASS-WITH-FINDINGS, 0 MAJOR, 1 MODERATE, 6 minor, 4 note; act 2
  pending).
  Findings SB1 (MODERATE, group-folder existence rule / outside-root marker silences a dead link),
  SB2 (minor, --separate-git-dir worktree still diverges), SB3 (minor, COST paragraph wrong twice),
  SB4 (minor, carriers and tool list inconsistent across surfaces), SB5 (minor, ccclose
  locateAtelier
  second meaning), SB6 (minor, three untested behaviours), SB7 (minor, pins funnel double count),
  SB8 (note, untracked-content divergence), SB9 (note, raw names on pins stderr), SB10 (note,
  altitude
  unargued), SB11 (note, "estate root" two meanings).
- Gates on the brief by path (/usr/bin/python3 tools/<gate>.py --root . <brief>): datescan clean
  (one
  `datescan:allow` marker on the principal's verbatim "11.30am ... todat"); wrapscan and spellscan
  report
  docs/reviews ignored by their ignore files (scanned nothing); linkscan clean (0 links); reviewscan
  clean.
  pathscan on the brief alone flags the brief-writer's own barred-file references (lines 242, 251,
  253) and
  three of my fixture tokens; the tree run excludes docs/reviews by default (0 findings there over
  752
  files), so no marker added. Tables rewritten as bullets and every act-1 line reflowed to <= 100
  columns
  (rewrap.py, fix2.py, fix3.py in the scratchpad); the brief-writer's own over-width lines left as
  written.
- Cleanup: scratch fixtures p1/, p2/, tools_mut/ and all live captures (pins.out/err, scanner
  JSON/text,
  suite outputs) deleted. Left in the scratchpad: my probe scripts and delta.diff (body-free). Files
  there
  that are not mine (commit1.log, commit2.log, land.sh, resolve.sh) were not opened or touched.
- `git status --short`: ` D ...deferred.md` (the partition) and ` M ...cold.md` (this verdict). No
  git writes
  by me. Sibling not opened. Waiting for the orchestrator's release message before act 2.

#### Act 2

- Release message from orchestrator 5bb9889e (process only): act 1 committed as b02232d3 (brief
  only, text
  unrevised); may read the one held file
  /Users/mike/.claude/fable-held/atelier--2026-11-14-0227-estate-helper-
  sibling-resolution-cold.deferred.md plus the barred records the brief names for phase 2; write ###
  Reconcile;
  never revise act 1; do not fold or delete; same rules; end "ACT 2 SAVED". It carried no question
  about the
  delta and no request about any finding.
- Read (all allowed in act 2): the held sibling in full (9 questions + the brief-writer's run record
  of
  2026-11-14: 24 estate tests, 88 pathscan findings vs 79 from the main checkout, nine
  ignored-local-file
  references); board item 160/1360 (pointer, claim); `git log -1 --format=%B c1af4465` (commit
  body);
  docs/roadmap/320-.../180-... and 660-... whole (author's landing notes; 320/180 closed 2026-11-16
  via
  ATELIER_TOOLS, ATELIER_ESTATE_ROOT deliberately not used there); grep of docs/reviews for the
  items: two prior
  verdicts (2026-09-25-0715 line 474/534/579, 2026-11-09-0207 line 246/757), passing mentions only.
- Mapping: Q1->SB-A2, Q2->L1 two-climb probe (no finding), Q3->SB3, Q4->SB1/SB-A4 (answer: not
  suppressed
  before; L5a), Q5->SB6/SB-A7 (+ per-root key serves fleets correctly), Q6->SB1/SB-A5 (+ worktrees
  folder
  named), Q7->SB12 formed at reconcile (two group-folder definitions, V4), Q8->SB13 formed at
  reconcile
  (fallback change unnamed in wrappers/changelog), Q9->SB8 (320/180 closed, so SB8 wants its own
  item).
- Author's 29-checkout / 4-worktree probe NOT re-run (private repos, load, counts-only output; class
  covered by
  the atelier main-vs-worktree comparison and fixtures). Recorded as read, not verified.
- ### Reconcile appended 2026-11-22T23:2xZ-23:4xZ; overall restated PASS-WITH-FINDINGS 0 MAJOR, 1
  MODERATE,
  6 minor, 6 note. `git diff HEAD -- <brief>` shows 0 removed lines (act 1 as committed in b02232d3,
  unrevised). Reconcile reflowed to <= 100 chars (fix4.py, reconcile region only). Gates on the
  brief:
  datescan, wrapscan, spellscan, linkscan, reviewscan all clean. No git writes; sibling not folded
  or deleted.
