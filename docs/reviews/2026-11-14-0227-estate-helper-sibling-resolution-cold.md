# Cold pass — `estate.py`, one helper for where `../<sibling>` lands

**Board:** `docs/roadmap/160-doctrine-review-owed/1360-rule-4-cold-pass-queued-estate-helper-sibling-resolution.md`
**Status:** BRIEF ONLY, not run. Written 2026-11-14 UTC by a headless Opus 5.5 brief-writer
(`cclive` lists it as session `cdb0c296`). Queued, waiting on the principal's explicit approval of
Fable work; this brief is not that approval.

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
`docs/reviews/2026-11-14-0227-estate-helper-sibling-resolution-cold.deferred.md`, the delta
commit's message body, and the two intent records beyond what *The acceptance test* above
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
