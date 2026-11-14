# Cold pass — `sweepscan`: where sibling worktrees exist, a commit names its files (warn-only, no date)

**Board:** `docs/roadmap/160-doctrine-review-owed/1400-rule-4-cold-pass-queued-sweepscan.md`
**Status:** BRIEF ONLY, not run. Written 2026-11-14 UTC by a headless Opus 5.5 brief-writer
(`cclive` lists it as session `b769469b`). Queued, waiting on the principal's explicit approval of
Fable work; this brief is not that approval.

**Pass type:** code cold pass, per `docs/method/REVIEW.md` rule 4 (the queue pointer's own words).
**Tier:** Fable 5.1, the principal-named review tier, checked at selection by whoever takes the
pass. A session that cannot run on it stops (rule 4).
**Size of this pass:** small: one commit, 7 files outside the board store. `tools/sweepscan.py`
+205 (new), `tools/test_sweepscan.py` +163 (new), `tools/floor.py` +36/−6, `tools/test_floor.py`
+25/−4, `tools/README.md` +25, `CHANGELOG.md` +17.
**Why it earns a review:** it is a new guard on the floor every child floats on at `main`, and it
answers a concurrency incident: a commit that carried another session's staged paths. The worst
failure is a guard that reads as protection and is not: a hook whose clean line ("the commit names
its files", "the whole index is declared", "replaying") is printed for a commit that in fact swept
a peer's work, or a marker that switches the check off for good without anyone seeing it. A second
worst case runs the other way: the `floor.py` change reaches every registry entry, not only this
one, so a mistake there moves what the floor lists on the CI plane for the whole fleet.

## Spawn provenance

- **Author of the work under review:** a principal-opened Opus 5.5 queue run, session `d0ca5d24`,
  2026-11-09 UTC, and the worker it dispatched, which wrote the commit (per the queue pointer). The
  author queued this pass and does not take it.
- **Who wrote this brief:** a headless brief-writer (`claude-opus-5-5`; `cclive` lists it as session
  `b769469b`; `$CLAUDE_SESSION_ID` was unset), started 2026-11-14 UTC by an estate health sweep,
  orchestrator session `58027096` (Opus), on the principal's instruction that a brief is written for
  every review known to be owed (Mike, 2026-11-14, verbatim: *"include all briefs are written where
  we know a fable review is required"*). Neither wrote any of this delta. **Off-tier for review,
  disclosed: the brief-writer forms no finding and writes no severity**, and stops after writing.
  It ran no review and used no Fable model.
- **Barred from running this pass:** session `b769469b` and session `58027096` (whoever writes a
  brief does not run it), and session `d0ca5d24` with everything it started.
- **Contact, disclosed (rule 4):** the brief-writer's only instruction came from `58027096`: the
  item number, the pointer's opening sentence, and the rules of the sweep. It carried no framing of
  the work. The brief-writer had no contact with the author session or its worker.
- **Who reviews:** a fresh Fable 5.1 session started for this pass alone, by a session that passes
  rule 4's criterion. An orchestrator may hold the context partition and commit the records
  off-tier, only if it forms no finding, writes no severity, and is disclosed in the claim, the
  pointer and the verdict.
- ⚠️ **Brief-writer's exposure, disclosed** (rule-2 and author-account material met before writing):
  its launch prompt; `skills/review-brief/SKILL.md`; the queue pointer whole; **both intent records
  whole**, including the author's landing notes (the line ranges barred below); the unrun brief for
  `160/1370` (read for house form). It read the delta through plain `git show`, **so it met the
  commit's message body**, and it read the delta's two new files, `tools/floor.py`'s registry entry
  as it stands at HEAD and the env-handling lines of `tools/report.py` and `tools/floor.py`. It
  opened **no prior verdict file**. Its harness also loaded user-level and repo instruction files and
  a memory index, which hold private context this brief does not carry. Everything evaluative it
  formed is in the sibling.

## The acceptance test

The check answers a child's filing, a proposal re-run at this end, and the principal's choice of six
checks. Print them, from the worktree root:

```
sed -n '1,70p' docs/roadmap/320-child-filed-findings-via-pointing-up/060-proposal-the-floor-requires-a-path-scoped-commit.md
sed -n '1,14p' docs/roadmap/320-child-filed-findings-via-pointing-up/810-build-six-checks-warn-first-staggered.md
```

The first holds the filing (the incident, why "print the path list" is the wrong fix, the
`GIT_INDEX_FILE` mechanism re-run here, the proposal, its three limits and its cost) and, at lines
63–70, the principal's words choosing it. The second holds the plan those words set: *"all six,
warnings at first and then move to blocking action. With a staggered turn on of each so they dont
all hit at once"*, and the **Shape** paragraph (a dated constant per check). Test the delta against
both: does it build the proposal, inside its three limits, and does a check with no blocking date
honour or depart from the principal's words, and if it departs, does the delta say so where he
would see it?

## What the work is

One commit on `main`, authored 2026-11-09 UTC (stamped 2026-11-10 NZDT):

- **`f9def52d`** — `tools: warn when a commit in a multi-worktree repo takes the whole index`.

Read it body-free: `python3 tools/coldsweep.py --root . --commit f9def52d` (subject, stat and diff,
never the body; board files left out). Plain `git show` prints the body before the diff, and
reading is atomic (`REVIEW.md` rule 1), so it is barred. Check first that your tree has the delta:
`git merge-base --is-ancestor f9def52d HEAD` exits 0. The pointer names the bound as "the commit
that adds it, on `main`"; this brief pins it to `f9def52d`, the only commit that touches
`tools/sweepscan.py` or `tools/test_sweepscan.py`. Record the pin in your verdict's scope.

Delta paths (the pointer names the first three; the commit carries all six):

- `tools/sweepscan.py`: `judge`, `live_worktrees`, `replaying`, `staged_count`, the marker
  `ATELIER_WHOLE_INDEX`, the CLI and the selftest.
- `tools/test_sweepscan.py`: real commits through a hook in a throwaway repo.
- `tools/floor.py`: the `sweepscan` registry entry (`hook` only, `ci=None`, `warn_only`,
  `advisory_count`), `HOOK_ONLY`, the selftest's CI-form check, and **a change to `plan()` that
  applies to every entry**: an entry with no form on a plane used to be listed only when it was a
  repo-local check; now any such entry lists as `skipped` or `disabled`.
- `tools/test_floor.py`: the hook-only listing test, the advisory-count contract test, and three
  existing tests widened to skip `HOOK_ONLY`.
- `tools/README.md` (the `sweepscan.py` section) and `CHANGELOG.md` (the 2026-11-10 *Added* entry).

**The registry entry has moved since.** `ba55be27` (`115/120` step 0) added a `declares=` block to
it; `6b6110c9` and `b74cd5ef` widened one `test_floor.py` name list. List them with
`git log --oneline f9def52d..HEAD -- tools/floor.py tools/test_floor.py`. `tools/sweepscan.py` and
its tests are unchanged since landing. Judge the delta as landed and as it stands at HEAD; the
`declares=` block is not the delta, but where it states what the check cannot see, test it as a
claim about this check.

## The claims the delta makes

Extracted from the delta, not evaluated here. They are the author's claims to test, not settled
scope. Name your own load-bearing assumptions first (lens 1).

- **The signal.** "Git hands the hook the index the commit is about to write, and the name of that
  file says which form of commit is running (measured on git 2.x)": a plain commit `.git/index`,
  `-a`/`-i` `index.lock`, `git commit -- paths`/`--only` `next-index-<pid>.lock`. "So only
  `next-index-` is a commit that names its files, and it is the only form whose carried set is
  exactly what the commit named."
- "The check is free: no output is parsed, no message needed."
- **The marker.** An environment variable, because "git runs `pre-commit` BEFORE it writes the
  message", so "no trailer can reach this plane". "Any non-empty value counts." "A session that
  exports it for good has turned the check off for itself, and this scanner cannot tell."
- **Scope.** "A repo with more than one live worktree"; "bare and prunable entries do not count, so
  a removed worktree stops charging". "A merge, cherry-pick, revert or rebase is replaying commits
  already written, so it is exempt; `pre-merge-commit` hands over to this same hook."
- **What it does not do.** It "does not make an index safe"; it "cannot stop a deliberate foreign
  path-scope, only the accidental sweep"; `git worktree list` "is a proxy for concurrency".
- **No date.** "A commit's form is not in git history"; measured over session transcripts' `git
  commit` command lines, "88% of 2,510 in atelier and 97% of 3,530 in one child took the whole
  index", and 46% and 79% in 2026-11 up to the landing. "A check that fires on most commits is
  noise, not a gate, so this
  one is warn-only with no blocking date, on purpose, and that is a finding for the principal, not
  a default."
- **Exit codes.** "0 reported or clean (it has no blocking form) · 2 the scan itself is broken (a
  broken scan is not a pass)."
- **The registry.** "CI cannot read a commit's form, so the registry lists the check as skipped
  there rather than passing over it." `HOOK_ONLY` is "named, not inferred from a None, so a dropped
  `ci=` on any other entry still fails the selftest."
- **Tests.** "Every case drives a real commit through a hook in a throwaway repo."

## Scope

The widest the work admits: intent, decisions, assumptions, the code, the test code, the docs, and
real-world behaviour: real commits of every form, in a throwaway repo with sibling worktrees,
through this repo's own `.githooks/pre-commit` and `tools/floor.py`, not only through the tests'
one-line hook. The lenses organise it; they do not bound it. Anything not named a non-goal is in
scope, and a non-goal that fences off the risk is a finding.

**Non-goals:** the other five checks of `320/810` (their own passes); the `declares=` grammar of
`115/120` as a whole (its own pass), except where this entry's declaration states a fact about this
check; whether sweepscan should block, which is the principal's call, except whether the delta put
that call to him honestly and whether the no-date posture is grounded in what it says it is.

## The four lenses — run all four

1. **Approach and assumptions** (most important). Is the commit's form the right thing to check,
   given the filing's own account of how the incident happened and of why more printed text was
   the wrong fix? Is the worktree count the right scope test? Is an environment variable the right
   marker, against the alternatives the hook plane admits? Is "warn-only, no date" a measured
   conclusion or a default with a measurement beside it?
2. **Correctness and quality.** Does each claim above hold when run, on every commit form a session
   in this house uses, from the main checkout and from a linked worktree? Does the hook see the same
   environment through `floor.py` as through the tests' bare hook? Does every exempt path (named
   files, one worktree, the marker, a replay) exempt only what it says? Does the `plan()` change
   move any other entry's state on either plane?
3. **Completeness and harvest.** Every mirror of the rule and the marker (V3): the house's
   concurrency doctrine, its guard doctrine, skills and templates that tell a session how to
   commit, `floorfleet` and any fleet report that lists states. Whether the tests cover every form
   and exemption the docstring names. Whether the measurement that sets the posture can be
   re-derived, and whether anything records the marker's use.
4. **Security and privacy** — a must. The check reads the environment and runs git in the hook:
   find an input (an inherited or crafted variable, a worktree path, a ref) that makes it print a
   false clean or fail open. The incident class is one session's work published under another's
   commit in a public repo. The measurement was taken over session transcripts: check the delta
   carries counts only and no transcript content. `/security-review` can reach the Python diff: aim
   it at `f9def52d`'s `tools/sweepscan.py` and `tools/floor.py`, as the floor under this lens and
   never its discharge, and only after your findings are committed (this brief has a held-back
   sibling).

## Load-bearing assumptions to attack

Each is a falsifiable claim. Damage it with a probe or confirm it by re-driving; never by reasoning
alone. Build every probe in a throwaway repo in your scratchpad, never in your review tree.

- **WA1.** On every commit form a session uses, git sets `GIT_INDEX_FILE` for `pre-commit`, and its
  file name begins `next-index-` exactly when the commit carries only the paths it named.
- **WA2.** The same holds in a linked worktree, whose index lives under `.git/worktrees/<name>/`.
- **WA3.** The value `sweepscan` reads inside `floor.py` on the hook plane is the value git set for
  the hook, and the git commands `sweepscan` runs see the repo and index the commit is using.
- **WA4.** A set-and-forgotten marker, inherited from a shell, a harness setting or a parent
  session, is visible to the session whose commits it silences.
- **WA5.** `replaying()` exempts only commits that replay work already written, never a fresh commit
  a session authors while a sequencer or merge is in progress or after one was abandoned.
- **WA6.** `live_worktrees()` counts exactly the worktrees a commit could race with: a removed one
  stops counting, a live one never drops out.
- **WA7.** The `plan()` change lists `sweepscan` as `skipped` on CI and moves no other entry's state
  on either plane, in this repo or in a child with a local check.
- **WA8.** A broken scan (git failing in the hook) exits 2 and the floor treats that as broken, not
  as a pass, even though the entry is warn-only.
- **WA9.** The 88% and 97% figures measure what the docstring says they measure, and support "noise,
  not a gate".

## Re-run list (V2)

The brief-writer ran every line once on 2026-11-14 UTC at `461fdf92`, from the worktree root unless
it says otherwise, with git 2.50.1 and Python 3.14.6; each exited 0. Re-run them; a line that no
longer reproduces is a finding.

```
git merge-base --is-ancestor f9def52d HEAD
python3 tools/coldsweep.py --root . --commit f9def52d
python3 tools/sweepscan.py --selftest
python3 tools/sweepscan.py --root .
python3 tools/floor.py --selftest
cd tools && python3 -m unittest test_sweepscan
cd tools && python3 -m unittest test_floor
```

`test_sweepscan` ran 11 tests in about 11 s; `test_floor` ran 255 tests in about 3 minutes and
left the tree clean. The plain run printed `no commit in progress` with a zero advisory count. To
test the behaviour before the delta, read the tools from a scratch checkout of its parent
(`git worktree add <scratch> f9def52d~1`), never by editing your review tree; a worktree you add
changes the count `sweepscan` reads in your review tree, so remove it before any run that depends
on that count.

The delta's recorded proofs (V2), with how each can be re-run:

- **The mechanism table** (`GIT_INDEX_FILE` per form, "measured, git 2.50"): re-run it with a
  `core.hooksPath` hook that prints what it sees, in a throwaway repo. Runnable here.
- **The transcript measurement** (88% of 2,510; 97% of 3,530; 46% and 79% in 2026-11 up to the landing): counted over
  this machine's session transcripts. **NOT RUN unless the session spawning you grants a read-only
  read of them**; if it does, count `git commit` command lines by form only, report counts only,
  quote no line and name no child. If it cannot be re-run, say so and weigh the claim as unverified.
- **The fleet probe** (21 of 21 exit 0; 5 with more than one worktree warn), in the intent records'
  landing notes (barred until phase 2). The child checkouts are not in this repo. **NOT RUN unless
  the session spawning you provides read-only child checkouts**; if it does, run the scanner read-only
  in each, report by exit code only, and name no child.

**Live reads:** none. This pass needs no live system and no network beyond the git remote.

## House rules for this run

- **Live systems:** none. No push from a child, no write to GitHub other than your own commits
  here. A check that would need one is marked NOT RUN.
- Name your own review worktree in the verdict. It is read-only to you except for THIS file. Other
  sessions may be live on this machine: touch nothing outside your worktree and scratchpad. Your own
  worktree counts toward `git worktree list`: say so where a probe's result depends on it.
- **Skip the session-log step of the read order** (`CLAUDE.md` step 4; `REVIEW.md` rule 2). If you
  read it anyway, disclose what you met.
- One heavy process at a time, foreground, with a long timeout. Never run an installed tool by bare
  name from `PATH`: use `python3 tools/<x>.py` from your worktree.
- Never set `ATELIER_WHOLE_INDEX` in your own shell or harness; set it only inside a probe's
  command, and say in the verdict whether it was set in your environment when you started.
- This pass is pending while you run it: anything you write to the session log, the pointer or a
  commit subject before phase 2 names the sibling by file and count only.
- Absolute ISO 8601 dates from `date -u`; prose wrapped at ≤ 100 columns; NZ English. This repo is
  PUBLIC: quote no secret, email address, private repo name or path, transcript line, and name no
  child repo.
- Review deep, not fast: a finding needs a probe or a re-driven claim behind it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content; the deferred material lives in the sibling .deferred.md under the rule-1 split, opened only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`, every prior
verdict in `docs/reviews/`, this brief's sibling
`docs/reviews/2026-11-14-0246-sweepscan-commit-names-files-cold.deferred.md` (a held-back file; by
count: 12 questions, 6 facts), every item under `docs/roadmap/160-doctrine-review-owed/` beyond its
title, every commit's message body, and these records beyond the `sed` ranges in *The acceptance
test*:

- `docs/roadmap/320-child-filed-findings-via-pointing-up/060-proposal-the-floor-requires-a-path-scoped-commit.md`
  (line 71 onward)
- `docs/roadmap/320-child-filed-findings-via-pointing-up/810-build-six-checks-warn-first-staggered.md`
  (line 15 onward)

The delta's own `CHANGELOG.md` entry, docstrings, README section and registry comments carry the
author's account of why; they are the delta, and reading the delta is never barred.

Sweep with `coldsweep`, never a hand-written exclusion:

```
python3 tools/coldsweep.py --root <your-worktree> \
  --also-exclude docs/roadmap/160-doctrine-review-owed \
  --also-exclude docs/roadmap/320-child-filed-findings-via-pointing-up/060-proposal-the-floor-requires-a-path-scoped-commit.md \
  --also-exclude docs/roadmap/320-child-filed-findings-via-pointing-up/810-build-six-checks-warn-first-staggered.md \
  'GIT_INDEX_FILE|ATELIER_WHOLE_INDEX|HOOK_ONLY|next-index|sweepscan'
```

`--include-barred` only with disclosure in the verdict.

## Process

**Phase 1 (act 1).** Reproduce the floor first; work the lenses, your own assumptions, WA1–WA9 and
the re-run list. Append your verdict below a `---` divider in THIS file: provenance repeated (how
you were spawned, your tier, any orchestrator, what you read, the UTC day), the pinned bound,
per-lens answers, V1–V7 each answered or discharged with grounds, each load-bearing assumption
damaged or confirmed with its probe, a per-claim ledger, findings with stable IDs (prefix `SV`:
`SV1`, `SV2`, …) and severities (MAJOR / MODERATE / minor / note), an overall PASS /
PASS-WITH-FINDINGS / FAIL line with counts, a re-run ledger and a follow-up checklist. Then STOP:
act 1 is committed, unrevised, **before** the sibling is opened. Edit no other file.

**Phase 2 (act 2).** Open the sibling and the barred records; screen the delta's commit body;
append `### Reconcile` beneath your verdict, with per-finding notes against the sibling's questions
and the author's account, any finding formed at reconcile marked as such, and the overall line
restated. Never revise act-1 text. Then fold the sibling in below the reconcile and delete it.

The work is a floor check the fleet floats on, written by a queue run; findings go to the principal
with the verdict, in plain words, and none is applied by the session that built the work (rule 4).
Counsel per finding is welcome, labelled as counsel and kept beneath it.
