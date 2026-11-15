# Cold pass — `sweepscan`: where sibling worktrees exist, a commit names its files (warn-only, no date)

**Board:** `docs/roadmap/160-doctrine-review-owed/1400-rule-4-cold-pass-queued-sweepscan.md`
**Status:** PASS RUN, act 1 written 2026-11-15 UTC by a Fable 5.1 cold reviewer under drain
session `21a271a5` (verdict below: FAIL, 1 MAJOR); act 2 (reconcile) follows the sibling's release.
Brief written 2026-11-14 UTC by a headless Opus 5.5 brief-writer (`cclive` lists it as session
`b769469b`), which ran no review.

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

---

## Verdict — act 1 (cold pass, Fable 5.1), 2026-11-15 UTC

### Provenance (rule 4, V7)

- **Reviewer:** Fable 5.1 (`claude-fable-5-1`), the principal-named review tier, checked at
  selection. The reviewer alone read the delta, answered the lenses, formed every finding and set
  every severity below.
- **Spawn:** a headless per-pass orchestrator (Opus 5.5) started me; it was itself started by drain
  session `21a271a5` (Opus 5.5). Both are rule-4 off-tier orchestrators: they hold the context
  partition, form no finding and write no severity. Neither wrote this brief or the delta; session
  `21a271a5` wrote no brief, no delta, and started no brief-writer for this pass. I was not started
  or instructed by any barred session (`b769469b`, `58027096`, `d0ca5d24` or anything it started).
- **Standing order:** the principal's weekly Fable drain, invoked as `/fable-drain` on 2026-11-16
  06:53 NZDT (2026-11-15 17:53 UTC); approval lapses at the reset, 2026-11-15 23:00 UTC, and a pass
  already running at the reset may finish.
- **Orchestrator direction, disclosed:** process only. It named my review worktree, this brief,
  the review-log file I may write outside the repo, the tools to use, the barred set (the
  `.deferred.md` sibling, removed from my worktree and held by the orchestrator; prior verdicts;
  session logs; `ROADMAP-DONE.md`; `160-doctrine-review-owed/` items beyond titles; commit bodies;
  the intent records beyond the brief's `sed` ranges), the deliverable's shape (this act, then
  `### Reconcile`), release timing (sibling released after act 1 is committed), load limits and the
  public-repo rules. It granted the brief's two conditional reads, read-only and counts only: the
  transcript measurement and the fleet probe. It contained no question about the delta, no pointer
  to where the risk lives, and no request to revise a finding. The prompt names paths this public
  repo may not carry, so it is summarised here; it stands verbatim in the orchestrator's transcript
  and in the review log kept outside the repo. No contact from the delta's author or the
  brief-writer reached me.
- **Environment:** `ATELIER_WHOLE_INDEX` was NOT set when I started (`env` grep count 0) and I set
  it only inside probe commands. git 2.50.1 (Apple Git-155). `/usr/bin/python3` is 3.9.6; `python3`
  on PATH is 3.14.6. The tools ran on 3.9 for the scanner and floor selftests and on 3.14 for the
  unit tests (the brief-writer used 3.14; `tools/README.md` line 2741 says the tests need 3.11+).
- **Worktree:** `atelier-160-1400-1939`, a linked worktree detached at `2fb235a6`
  (`f9def52d` is an ancestor). `git worktree list` in it returns 6 entries during this pass, so
  `sweepscan` run inside my tree would count 6; every probe below ran in throwaway repos in my
  scratchpad, never in the review tree. The only pending change in my tree is the orchestrator's
  removal of the sibling.
- **What I read:** this brief whole; `docs/method/REVIEW.md`; the delta through `coldsweep.py
  --commit f9def52d` (subject, stat, diff; the body not printed; its three board files left out);
  `tools/sweepscan.py`, `tools/test_sweepscan.py`, `tools/floor.py` (registry entry at HEAD
  including the later `declares=` block, `HOOK_ONLY`, `plan`, `run`, `Result.failed`),
  `tools/report.py` (`guarded_main`), `.githooks/pre-commit` and `pre-merge-commit`,
  `docs/method/CONCURRENCY.md` §§ The trigger, Integration hygiene, `docs/method/GUARDS.md` lines
  125–145 and 625–645, `tools/README.md` (`sweepscan`, Python floor), `CHANGELOG.md` (the 2026-11-10
  entry), `.github/workflows/*.yml` (Python pin), and the two intent records within the brief's
  ranges only (`060` lines 1–70, `810` lines 1–14). I skipped the session-log step. I opened no
  prior verdict, no session log, no `ROADMAP-DONE.md`, no commit body, and no `160-…` item beyond
  its title. The mirror sweep ran through `coldsweep.py` with the brief's three `--also-exclude`
  paths; no `--include-barred`.

### Scope and the pinned bound

The bound is pinned to **`f9def52d`** (`tools: warn when a commit in a multi-worktree repo takes the
whole index`), the only commit touching `tools/sweepscan.py` or `tools/test_sweepscan.py`, judged as
landed and as it stands at HEAD `2fb235a6`. `git log --oneline f9def52d..HEAD -- tools/floor.py
tools/test_floor.py` lists `ba55be27`, `49f3d407`, `b74cd5ef`, `6b6110c9`, `55f23034`; the
`declares=` block is not the delta and is read here only as a claim about this check.

### Per-lens answers

**Lens 1 — approach and assumptions.** The commit's *form* is the right thing to read: the probe
table below shows git hands the hook a `next-index-` index exactly for the forms that carry only
the named paths, and the filing's own account is that more printed text failed. An environment
variable is the right marker for this plane: `pre-commit` runs before the message is written, so no
trailer can reach it (confirmed; `commit-msg` is a later hook on the same commit). Two assumptions
do not hold as stated. (a) **The scope test is wider than the risk.** A linked worktree has its own
index: a path staged in a sibling worktree is invisible to `git diff --cached` in the main checkout
(probed, 1 vs 0). The staged-sweep incident can happen only where two sessions share one index, the
main checkout, which the worktree count reaches by proxy; yet the check charges every commit in a
linked worktree too, which no sibling can sweep. The noise that grounds "warn-only, no date" is
measured over that wider population, and the fraction made from linked worktrees cannot be read
from transcripts (SV4). (b) **"Replaying" is read from a ref that outlives the replay.**
`REBASE_HEAD` survives a hand-resolved rebase's completion, so the exemption keeps firing on fresh
commits (SV1). The no-date posture is a measured conclusion in direction (most commits take the
whole index, by my count too) but not in the figures or the population (SV4, SV5).

**Lens 2 — correctness and quality.** Every form a session uses was driven as a real commit through
a `core.hooksPath` hook, from the main checkout and from a linked worktree, and through the real
`.githooks/pre-commit` → `floor.py` → `sweepscan` chain: the form table holds, the floor passes the
hook's environment through unchanged, path-scoped commits are clean and leave the rest staged, the
marker clears, a broken scan exits 2 and blocks through the floor despite `warn_only`. Two exempt
paths exempt more or less than they say: a clean `git merge --no-ff` reaching the hook through
`pre-merge-commit` **warns** (MERGE_HEAD is not yet visible there), where the docstring says a merge
is exempt (SV2); a fresh commit during a stopped rebase, and every commit after a resolved one, is
**exempt** (SV1). The `plan()` change moves no other entry's state on either plane (WA7).

**Lens 3 — completeness and harvest.** The rule and the marker have no mirror outside `tools/`:
`CONCURRENCY.md` § Integration hygiene already tells a session to commit by pathspec in a shared
checkout and names a worktree as "the only index of one's own", but neither it, `GUARDS.md`, any
skill prompt, nor the child template names `sweepscan` or `ATELIER_WHOLE_INDEX`, and nothing says
when the marker is legitimate; nothing records its use (SV3). The tests cover every form the
docstring names except the `pre-merge-commit` path it names (SV2) and the post-rebase state (SV1).
The measurement cannot be re-derived from the record: the method is unstated (SV5).

**Lens 4 — security and privacy.** Inputs the hook trusts: `GIT_INDEX_FILE` (its basename),
`ATELIER_WHOLE_INDEX` (any non-empty value), `git worktree list`, and four replay refs. The one
**fail-open on an inherited state** is SV1: a stale `REBASE_HEAD`, left by a routine operation,
makes every later commit print a clean "replaying" line. A crafted `GIT_INDEX_FILE` whose basename
starts `next-index-` also prints a false clean (probed), but it costs the committer the same
deliberate act as the marker and so adds no exposure (N2). The marker inherited from a parent shell
or harness setting silences the check with one unrecorded clean line (SV3). The incident class is a
public repo publishing a peer's work under the wrong commit, and the delta's own records carry
counts only: I read the whole diff and found no transcript line, path or session content.
`/security-review`: **NOT RUN, discharged with grounds.** It reads the session's pending diff; in my
tree that is this brief and the removed sibling, which `REVIEW.md` forbids scanning, and it cannot
be aimed at a landed commit. Its clean pass would in any case be empty for the Python it could not
reach.

### V1–V7

- **V1** No claim stronger than its evidence: breached three times — "a merge … is exempt;
  `pre-merge-commit` hands over to this same hook" (SV2); "replaying commits already written"
  (SV1); the four percentages as stated (SV5).
- **V2** Re-run every proof: the re-run list reproduces (ledger below); the mechanism table
  reproduces; the fleet probe reproduces in direction (22 of 22 exit 0, 2 would warn); the
  transcript measurement reproduces in direction, not in figure (SV5).
- **V3** Swept to every mirror: not done; no doctrine, skill or template mirror exists (SV3a).
- **V4** One fact, one home: the `GIT_INDEX_FILE` table stands in the docstring, `tools/README.md`
  and `CHANGELOG.md` unstamped; the registry comment points at the docstring. Note N7, not a
  finding.
- **V5** No internal contradiction: the `declares.rule` pointer reaches `CONCURRENCY.md` § The
  trigger, whose "two more blind spots" paragraph holds the pathspec rule, so the reference reaches
  its rule. README's "What it cannot see" agrees with the docstring and the `purpose_gap`. The
  docstring contradicts the tool's behaviour on merges (SV2).
- **V6** Security and privacy: lens 4 above; the scanner discharged with grounds.
- **V7** Provenance: stated above and in the brief.

### Load-bearing assumptions — WA1–WA9

| # | Result | Probe |
|---|---|---|
| WA1 | **Confirmed** | Scratch repo, hook printing `basename $GIT_INDEX_FILE`: plain, `--amend`, `--allow-empty` → `index`; `-a`, `-i <p>` → `index.lock`; `-o <p>`, `-- <p>`, bare `<p>`, `--amend -o`, `--amend -- <p>`, `--amend --only` → `next-index-<pid>.lock`. Each matched the docstring's table on git 2.50.1. |
| WA2 | **Confirmed** | Same forms from a linked worktree: `GIT_DIR` is `.git/worktrees/<name>` (absolute), the index basename follows the same table, `git worktree list` from inside counts 2. |
| WA3 | **Confirmed** | The repo's real `.githooks/pre-commit` and `pre-merge-commit`, `ATELIER_TOOLS` pointed at my worktree's `tools/`, in a scratch repo with a sibling: plain commit → `⚠ … (1 staged path(s), 2 worktrees)`, count 1; `git commit -- a` → `✓ … names its files`, `b` left staged; the same from the linked worktree via `git -C`; marker → `✓ … declared`. The floor passes the environment through (`subprocess.run` with no `env=`) and `--root` is the hook's `rev-parse --show-toplevel`. |
| WA4 | **Confirmed** | `ATELIER_WHOLE_INDEX=1 sh -c 'sh -c "git commit …"'` → declared. Also `=0` → declared (any non-empty), empty → not set. Nothing records it (SV3). |
| WA5 | **Damaged** | Fresh commits while a rebase is stopped are exempt (two in a row); after `rebase --continue` finishes, `REBASE_HEAD` remains and every later fresh commit is exempt (SV1). A clean `merge --no-ff` through `pre-merge-commit` is *not* exempt (SV2). Conflicted merge, cherry-pick and revert resolutions are exempt and git refuses partial commits under them. |
| WA6 | **Damaged at one edge** | Unlocked worktree whose directory is gone → `prunable`, not counted; **locked** worktree whose directory is gone → counted live until unlocked and pruned (SV6). A live one never dropped out. |
| WA7 | **Confirmed** | Scratch clone, `floor.py --list` on hook and ci at `f9def52d~1` and `f9def52d`, for atelier and for a child-like config with a hook-only `local` check: the only diff is the added `sweepscan` line (hook `warn-only`, ci `skipped`); the local check lists `skipped` on ci before and after. |
| WA8 | **Confirmed** | Bogus inherited `GIT_DIR` → exit 2 (`git worktree list failed`); root not a repo → exit 2. A stub `sweepscan.py` exiting 2 in a scratch copy of `tools/`, through the real floor on the hook plane: `❌ sweepscan warn-only`, `BLOCKED by: … sweepscan …`, "exit 2 means the scan itself could not run"; floor rc 1; the commit did not land. |
| WA9 | **Confirmed in direction, damaged in figure** | Counted over this machine's transcripts (one process, counts only, nothing written): whole-index share 94 % (atelier, all time), 75 % (atelier, 2026-11-01 to the landing day), 85 % (largest other repo folder), 94 % (all other repos). The delta's 88 %, 46 %, 97 %, 79 % are not reproduced; the method is unstated (SV5). "Fires on most commits" holds in every slice I cut. |

### Per-claim ledger

| Claim (brief § *The claims*) | Verdict |
|---|---|
| The signal: index file name per form | **Holds** (WA1, WA2). |
| "Only `next-index-` … carried set is exactly what the commit named" | **Holds**; the trust is in a basename the committer controls (N2). |
| "The check is free: no output is parsed" | **Holds**. |
| Marker: env var because `pre-commit` precedes the message; any non-empty value; nothing records it | **Holds as stated**; the admitted gap is the finding (SV3). |
| Scope: more than one live worktree; bare and prunable do not count | **Holds**, locked-removed edge aside (SV6). |
| "A merge, cherry-pick, revert or rebase is replaying … exempt; `pre-merge-commit` hands over" | **Fails** for the clean merge on the path it names (SV2); **over-holds** for rebase (SV1). |
| Does not make an index safe; cannot stop a deliberate foreign path-scope; worktree list is a proxy | **Holds**, and the proxy is wider than the risk (SV4). |
| No date: "a commit's form is not in git history"; the four figures; "noise, not a gate" | Form-not-in-history **holds**; figures **not reproduced**; "most commits" **holds** (SV5, SV4). |
| Exit codes 0 / 2 | **Holds** (WA8). |
| Registry: skipped on CI; `HOOK_ONLY` named | **Holds** (WA7; selftest and `test_floor` pin it). |
| "Every case drives a real commit through a hook" | **Holds** for `CommitFormTest`; `CliTest` drives none (it fakes the env), which the docstring's word "every" overstates slightly (note N8). |

### Findings

**SV1 — MAJOR.** `replaying()` reads `REBASE_HEAD`, and `REBASE_HEAD` outlives the rebase. After
a hand-resolved rebase finishes with `git rebase --continue` (merge backend, `rebase -i`, and the
onramp's `git pull --rebase --autostash`), the ref remains while `rebase-merge/` is gone, `git
status` says nothing, `--abort` and `--quit` refuse ("no rebase in progress"), and it clears only on
the next *clean* rebase or an explicit `update-ref -d`. Every fresh plain commit in that checkout
from then on prints `✓ sweepscan clean — replaying commits already written.` with a zero count:
the brief's named worst case, a clean line printed for a commit that may have swept, with no end,
after a routine house operation in the very checkout the check exists for. While a rebase is
genuinely stopped, a fresh commit (not `--continue`) is exempt too, so the stopped state is a sweep
window the check waives. Live exposure read 2026-11-15 ~20:00 UTC, counts only: no replay ref in
atelier's main checkout, its 6 linked worktrees, 22 children's main checkouts or their 3 linked
worktrees, so nothing is silenced today. `test_sweepscan.py` has no rebase case.
*Counsel:* test the rebase **state directory** (`git rev-parse --git-path rebase-merge` /
`rebase-apply` exists) instead of `REBASE_HEAD`; keep `MERGE_HEAD`, `CHERRY_PICK_HEAD` and
`REVERT_HEAD` (removed at completion, and git refuses a partial commit under them anyway); add a
conflict → `--continue` → fresh-commit-warns test.

**SV2 — MODERATE.** A clean `git merge --no-ff` is not exempt on the path the docstring names. At
`pre-merge-commit` time `GIT_INDEX_FILE` ends `index` and `rev-parse --verify MERGE_HEAD` fails, so
the check warns "takes the whole index (1 staged path(s), 2 worktrees)" on an automatic merge. The
docstring, README and CHANGELOG say a merge is exempt and that `pre-merge-commit` hands over to
this hook; the one merge test drives `merge --no-commit` then `git commit`, the `pre-commit` path
with MERGE_HEAD present, never the hook it names (V1, V2). Frequency is low in this house, which
lands by `--ff-only`, but the claim is false where it is tested least.
*Counsel:* either have `.githooks/pre-merge-commit` export a marker the floor passes through (e.g.
`ATELIER_HOOK=pre-merge-commit`) and exempt on it, or state the limit honestly; add a
`pre-merge-commit` test either way.

**SV3 — MODERATE.** The marker is ungoverned and unrecorded. (a) Nothing says when
`ATELIER_WHOLE_INDEX=1` is legitimate: doctrine already implies "only in a worktree you own"
(`CONCURRENCY.md`: a worktree is "the only index of one's own"; the shared checkout commits by
pathspec), but neither `CONCURRENCY.md`, `GUARDS.md`, any skill prompt nor the child template names
the check or the marker (coldsweep: no hit outside `tools/`, the CHANGELOG and the registry) — V3.
(b) A declared commit counts **0** advisories and leaves one `✓` line in a 108-line hook wall
(measured on a tiny repo), so a set-and-forgotten marker (a harness `env` setting, an exported
shell) is indistinguishable from a deliberate one on every surface the board and `floorfleet` read;
the docstring admits "this scanner cannot tell". Confirmed inherited two shells up. `=0` counts
as declared.
*Counsel:* count declared commits on their own advisory line so the board sees them; state the
marker's grant conditions beside the pathspec rule in `CONCURRENCY.md` § Integration hygiene; treat
`0`/`false`/`no` as not set.

**SV4 — MODERATE (the principal's call; counsel beneath).** The scope test charges commits the
check has no reason to fire on, and the no-date posture rests on that count. A sibling worktree
cannot stage into another worktree's index (probed), so a commit from a linked worktree can be
swept only by a session sharing *that* worktree, which doctrine forbids and whose orchestrated form
has one committer. The filed incident lives in the shared main checkout; the worktree count reaches
it by proxy, as the filing says, but the proxy also taxes every linked-worktree commit. The 88 %/
97 % that ground "noise, not a gate" are measured over that whole population, and the linked-
worktree share cannot be read from transcripts (the session folder keeps its start path after a
session enters a worktree), so the true noise floor is unknown. The delta departs from the
principal's words ("warnings at first and then move to blocking action"; `810`'s Shape, "a dated
constant per check") and says so in Claude's records (CHANGELOG, docstring, README, registry
comment), which he does not read; whether the call was put to him on the board is checked at
reconcile (the commit's board-file hunks are barred in act 1).
*Counsel:* a free sharper signal exists: whether the commit's index is the common one
(`git rev-parse --git-dir` equals `--git-common-dir`; in a linked worktree `GIT_DIR` is
`.git/worktrees/<name>`). Charging only shared-checkout commits when worktrees > 1 would shrink the
noise to the population at risk and let the dated-constant shape he chose be revisited on a real
number.

**SV5 — minor.** The measurement cannot be re-derived from the record. My count (one niced process,
counts only, 5,099 transcript files, 8.9 GB): atelier 2,543 `git commit` lines all time, 94 % whole
index; 536 from 2026-11-01 to the landing day, 75 %; largest other repo folder 4,111, 85 %; all
other repos 15,239, 94 %. The delta's 2,510/88 %, 373/46 %, 3,530/97 %, 157/79 % come from an
unstated classification and window, and the docstring's "this month" is a relative date in undated
code. The direction holds in every slice; the figures as written are not reproducible (V1, V2).
*Counsel:* record the method (what counts as "named", the window, the file set) beside the
figures, or state "most" and drop them.

**SV6 — minor.** `live_worktrees()` counts a **locked** worktree whose directory is gone as live
(porcelain prints no `prunable` for a locked entry); the docstring's "a removed worktree stops
charging" holds only for unlocked ones. Edge case; it errs toward warning.

**Notes (no severity).** N1 `--json` prints `"clean": true` beside `"finding": true`; no consumer
reads it today. N2 a crafted `GIT_INDEX_FILE` basename `next-index-*` yields a false clean; same
deliberate act as the marker, no new exposure. N3 the `⚠` line sits in ~108 lines of hook output;
the floor's summary repeats it as a `🟡` line, which is the mitigation. N4 `--amend` and
`--allow-empty` plain forms warn; consistent, noisy. N5 a stale `GIT_INDEX_FILE` in a shell makes a
hand run warn; harmless. N6 `test_sweepscan.py` needs Python ≥ 3.10 (`dict | None` at import);
`tools/README.md` documents that the tests need 3.11+, so not a defect. N7 the form table is
copied unstamped into README and CHANGELOG (V4). N8 `CliTest` fakes the hook environment rather
than driving a commit; "every case" overstates by four tests.

### Overall

**FAIL** — 1 MAJOR (SV1), 3 MODERATE (SV2, SV3, SV4), 2 minor (SV5, SV6), 8 notes. The check reads
the right signal and the floor wiring is sound (WA1–WA3, WA7, WA8 confirmed); it fails on the
exemption that switches it off for good after a routine rebase, and on a merge claim its own test
does not reach. All findings are on self-authored guard code and go to the principal (rule 3);
none is applied by the session that built the work.

### Re-run ledger (V2)

| Line | Result |
|---|---|
| `git merge-base --is-ancestor f9def52d HEAD` | exit 0 |
| `coldsweep.py --root . --commit f9def52d` | 6 files, body not printed, 3 board files left out |
| `sweepscan.py --selftest` | `selftest OK` (3.9) |
| `sweepscan.py --root .` | `no commit in progress`, count 0, exit 0 |
| `floor.py --selftest` | `ok (21 scanners, 0 failure(s))` (3.9) |
| `python3 -m unittest test_sweepscan` (cwd `tools/`) | 11 tests OK in 11.2 s (3.14); fails to import on 3.9, documented |
| `python3 -m unittest test_floor` (cwd `tools/`) | 255 tests OK in 250 s (3.14); tree clean after |
| Mechanism table | reproduced (WA1, WA2) |
| Transcript measurement | run under the orchestrator's grant; direction reproduced, figures not (SV5) |
| Fleet probe | run read-only under the grant: 22 children, 22 exit 0, 2 would warn |

### Follow-up checklist

- [ ] SV1 to the principal with the counsel; a rebase test lands with any fix.
- [ ] SV2: pick "exempt on a hook marker" or "state the limit"; add the `pre-merge-commit` test.
- [ ] SV3: grant conditions in `CONCURRENCY.md`; a counted line for declared commits; reject `0`.
- [ ] SV4: the principal's call on scope and on the dated-constant shape, with the index-ownership
      signal as the option on the table.
- [ ] SV5: record the method beside the figures or drop them; de-relativise "this month".
- [ ] SV6: a line in the docstring, or count only entries whose directory exists.
- [ ] Act 2: reconcile against the sibling, the intent records and the commit body; check where the
      no-date call was put to the principal.
