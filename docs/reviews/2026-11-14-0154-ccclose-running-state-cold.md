# Cold pass — `ccclose` tells a still-running subagent from a cut one

**Board:** `docs/roadmap/160-doctrine-review-owed/1260-rule-4-cold-pass-queued-ccclose-running-state.md`
**Status:** PASS-WITH-FINDINGS (0 MAJOR, 2 MODERATE, 2 minor, 1 note). Act 1 run 2026-11-22 UTC by
a Fable 5.1 reviewer under off-tier orchestrator `1e1c5269`, in the principal's weekly drain of
2026-11-23 NZDT (drain session `eca14b23`); act 2, the reconcile against the sibling, follows its
release. Every finding is the principal's to decide (rule 3); nothing applied. Brief written
2026-11-14 UTC by session `947ac694`, a headless Opus 5.5 brief-writer.

**Pass type:** code cold pass, per `docs/method/REVIEW.md` rule 4 (a close check whose pass is read
as "safe to close" is doctrine by function, rule 3).
**Tier:** Fable 5.1, the principal-named review tier, checked at selection by whoever takes the
pass. A session that cannot run on it stops (rule 4).
**Size of this pass:** small: about 40 lines of code, 90 lines of tests and 40 lines of design note
and manual in one commit.
**Why it earns a review:** `ccclose` is what a session runs to answer "ready to close?", and its
subagent check guards the teardown hazard `docs/method/CONCURRENCY.md` names: closing, or removing a
worktree, under an agent that is still working. The delta adds a judgement made from a clock. The
worst failure is a working agent read as finished or as dead, so a close or a teardown goes ahead
under it; the second worst is a line pasted into a record as fact that says an agent is alive or
dead when it is not.

## Spawn provenance

- **Author of the work under review:** a principal-opened Opus 5.5 queue run, session `d0ca5d24`,
  2026-11-09 UTC, and the worker it dispatched, which wrote the code (per the queue pointer). The
  author queued this pass and does not take it.
- **Who wrote this brief:** session `947ac694` (`claude-opus-5-5`), a headless brief-writer started
  2026-11-14 UTC by an estate health sweep, orchestrator session `58027096` (Opus), on the
  principal's instruction that a brief is written for every review known to be owed. Neither wrote
  any of this delta. **Off-tier for review, disclosed: the brief-writer forms no finding and writes
  no severity**, and stops after writing. It ran no review and used no Fable model.
- **Barred from running this pass:** session `947ac694` and session `58027096` (whoever writes a
  brief does not run it), and session `d0ca5d24` with everything it started.
- **Contact, disclosed (rule 4):** the brief-writer's only instruction came from `58027096`: the
  item number, the pointer's opening sentence, and the rules of the sweep. It carried no framing of
  the work. The brief-writer had no contact with the author session or its workers.
- **Who reviews:** a fresh Fable 5.1 session started for this pass alone, by a session that passes
  rule 4's criterion. An orchestrator may hold the context partition and commit the records
  off-tier, only if it forms no finding, writes no severity, and is disclosed in the claim, the
  pointer and the verdict.
- ⚠️ **Brief-writer's exposure, disclosed** (rule-2 and author-account material met before writing):
  its launch prompt; `skills/review-brief/SKILL.md` whole; the queue pointer whole and the pointer
  of `160/1350`; the intent record `210/380` whole, **including its DONE note** (the author's
  account); the delta's code, design-note, manual and `CHANGELOG.md` hunks and the test names; the
  later diff of `50547442` on `instruments/ccclose`; commit subjects through `git log`; the brief,
  sibling and session log of an earlier brief-writer (`2026-11-09-0207-ccclose-worktree-variables`,
  read for house form, no verdict in it); the tail of `docs/SESSIONS.md`, one session file and the
  pointer of `160/1250` and the opening 40 lines of the `160/1240` brief (no verdict in it), for
  record form; the paragraph of `docs/method/CONCURRENCY.md` the acceptance test names; the
  results of the re-run lines below. It did **not** open any prior verdict or any delta commit's
  message body. Its harness also loaded user-level and repo instruction files and a memory index,
  which hold private context this brief does not carry. Everything evaluative it formed is in the
  sibling.

## The acceptance test

No record the brief-writer read carries a ruling of the principal's on this design. Judge it against
`instruments/ccclose.design.md` (the agent-states table and the paragraph under it),
`instruments/man/ccclose.1` (*Subagents finished*), and the hazard in `docs/method/CONCURRENCY.md`
§ *Orchestrated queue runs* (*Teardown waits for the worker to stop*) that the check exists to
guard.

## What the work is

- **`1bc89816`** — `ccclose: tell a running subagent from a cut one; decline the 070 third figure`.

Delta paths, read at the commit and at HEAD:

- `instruments/ccclose`, `instruments/ccclose.test.js`, `instruments/ccclose.design.md`,
  `instruments/man/ccclose.1`, `CHANGELOG.md`

First confirm the tree holds the delta, then read the commit body-free:

```
git merge-base --is-ancestor 1bc89816 HEAD; echo $?
python3 tools/coldsweep.py --root . --commit 1bc89816 --path instruments/ccclose --path \
  instruments/ccclose.test.js --path instruments/ccclose.design.md --path instruments/man/ccclose.1 \
  --path CHANGELOG.md
```

Plain `git show` is barred: it prints the message body before the diff, and reading is atomic (rule
1). The commit also touches three board records (the intent records listed under *Deferred
reading*); those are barred until phase 2, so always pass `--path`.

Then see what has landed on those paths since, and read anything new the same way, only as far as it
bears on this delta at HEAD: `git log --oneline 1bc89816..HEAD -- instruments/ccclose
instruments/ccclose.test.js instruments/ccclose.design.md instruments/man/ccclose.1`.

## The claims the delta makes

Extracted from the delta, not evaluated here. They are the author's claims to test, not settled
scope. Name your own load-bearing assumptions first (lens 1).

- An agent with no end recorded is *still running* when "its last record is recent by the clock,
  and the parent has not recorded anything FRESH_MS after it"; otherwise it is *cut mid-flight*.
- `FRESH_MS` is ten minutes, "from a census of 3,587 real agent logs (881,904 gaps between
  consecutive records): the 99th percentile gap is 83 s, the 99.9th is 600 s", and "600 s is also
  the longest a single foreground command may run, so a working agent waiting on one is silent for
  at most that".
- "A dead agent reads as running for this long after its last record, and the line says how long
  ago that was."
- "A parent idle while its agent works, or the checking session itself, passes both" tests.
- An agent resumed after its `completed` notification "is judged the same way".
- Running "fails the check like cut, because a close under a working agent is the hazard, but never
  calls a live agent dead".
- The summary line, `--json` `counts` and the identifiers block all carry the new count, zeros
  included.
- `CHANGELOG.md`: `210/070` "was measured and declined: a missing `end_turn` flags 130 completed
  agents for every 50 failed ones".

## Scope

The widest the work admits: intent, decisions, assumptions, design, docs, code, test code and live
behaviour. The lenses organise it; they do not bound it. Anything not named a non-goal is in scope,
and a non-goal that fences off the risk is a finding.

**Non-goals:** `50547442` (`210/400`, the `failed` state, pass `160/1350`) and `6890e9db` (`cclive`,
pass `160/1290`), except as they bear on this delta at HEAD; every other check `ccclose` runs. The
`210/070` decline is in scope as far as the delta states its measurement.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself, before anything else. Is
   a clock on the transcript the right evidence for "alive", and is a fixed bound the right shape,
   against the acceptance test? Is the census a measurement of the thing the bound is used for?
2. **Correctness & quality.** Re-drive the claims above. Record each overclaim against the text that
   makes it, including any claim the delta's tests do not pin.
3. **Completeness / harvest.** Every surface that states the agent states (V3); one home for the
   bound and its census (V4); no contradiction between code, design note, manual and changelog
   (V5). Find tests that would stay green on a broken delta by mutating a scratch copy.
4. **Security & privacy**, mandatory: at design altitude what this exposes, over-collects or leaks
   by weakness of design (the check reads other sessions' transcripts and prints agent
   descriptions into records); at code altitude the likely vectors for its class, checked against
   an open catalogue (OWASP ASVS or the domain's equivalent). Aim `/security-review` at code only
   from a clean tree, as *House rules* says; weigh a clean pass over markdown as nothing.

Run the standing checklist V1–V7 unasked (`REVIEW.md` § *The standing checklist*).

## Re-run obligation

Re-run, do not read. The brief-writer ran each line once, on 2026-11-14 UTC, from the worktree root,
under `nice`; its results are held in the sibling. Read exit codes explicitly.
Check `uptime` first and run the heavy lines under `nice -n 10`.

```
nice -n 10 node --test instruments/ccclose.test.js
mandoc -T lint -W style instruments/man/ccclose.1
```

**The live proof.** The design note states that the checking session's own still-working agents
show as running until they end. Re-drive it on your own session, read-only: start one subagent of
your own that does nothing but wait (a cheap tier is fine; it forms no finding), run
`instruments/ccclose --session "$CLAUDE_CODE_SESSION_ID" --json` from your worktree while it waits
and again after it reports, and record both `counts`. The author's own record of a live run sits in
a barred record; compare against it in phase 2 only. The brief-writer did not run this; it had no
subagent to observe.

## House rules for this run

- **Live systems:** read-only reads of live systems as needed; no live writes. A check that needs a
  write is marked NOT RUN, with why. No push, no write to GitHub, no network service changed.
- **Never print a secret** or any personal data. Other sessions' transcripts are read only through
  `ccclose` or through synthetic fixtures; quote none of their content. Probes use scratch copies
  and synthetic fixtures under your scratchpad, deleted when you finish.
- Name your own review worktree in the verdict. It is read-only to you except for THIS file. Other
  sessions may be live on this machine: touch nothing outside your worktree and scratchpad. Child
  repos are read-only and reported by count only, never by name or path.
- One heavy process at a time, foreground, with a long timeout. Never run an installed tool by bare
  name from `PATH`: use `instruments/<x>` or `python3 tools/<x>.py` from your worktree.
- `/security-review` reads the session's pending diff, not this delta. Aim it at the code by
  reproducing the diff in a scratch clone, or discharge it by grounds and do the code-altitude read
  by hand, never with this brief or its sibling dirty.
- This pass is pending while you run it: anything you write to the session log, the pointer or a
  commit subject before phase 2 names the sibling by file and count only.
- Absolute ISO 8601 dates from `date -u`; prose wrapped at ≤ 100 columns; NZ English. This repo is
  PUBLIC: quote no secret, email address, private repo name or path.
- Review deep, not fast: a finding needs a probe or a re-driven claim behind it.

**Reviewer's start-up reading:** skip the session-log step of the repo's read order; the log is on
rule 2's barred list.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content; the deferred material lives in the sibling .deferred.md under the rule-1 split, opened only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`, every prior
verdict in `docs/reviews/`, this brief's sibling
`docs/reviews/2026-11-14-0154-ccclose-running-state-cold.deferred.md` (a held-back file; by count: 7
questions, 2 facts), every other item under `docs/roadmap/160-doctrine-review-owed/` beyond its
title, every delta commit's message body, and these intent records beyond their first line:

- `docs/roadmap/210-instruments-open-features/380-ccclose-classes-a-running-subagent-as-cut.md`
- `docs/roadmap/210-instruments-open-features/070-finished-counts-logs-not-successes-and-a-dead.md`
- `docs/roadmap/210-instruments-open-features/400-a-failed-agent-notification-is-a-status-ccclose-does.md`

The delta's own comments, design note, manual and `CHANGELOG.md` entry carry the author's account of
why; they are the delta, and reading the delta is never barred.

Sweep with `coldsweep`, never a hand-written exclusion:

```
python3 tools/coldsweep.py --root <your-worktree> \
  --also-exclude docs/roadmap/160-doctrine-review-owed \
  --also-exclude docs/roadmap/210-instruments-open-features/380-ccclose-classes-a-running-subagent-as-cut.md \
  --also-exclude docs/roadmap/210-instruments-open-features/070-finished-counts-logs-not-successes-and-a-dead.md \
  --also-exclude docs/roadmap/210-instruments-open-features/400-a-failed-agent-notification-is-a-status-ccclose-does.md \
  --also-exclude docs/reviews/2026-11-14-0154-ccclose-running-state-cold.deferred.md \
  'FRESH_MS|runningVerdict|still running|judgeAgent'
```

`--include-barred` only with disclosure in the verdict.

## Process

**Phase 1 (act 1).** Reproduce the floor first; work the lenses, your own assumptions and the re-run
list. Append your verdict below a `---` divider in THIS file: provenance repeated (how you were
spawned, your tier, any orchestrator, what you read, the UTC day), per-lens answers, V1–V7 each
answered or discharged with grounds, each load-bearing assumption damaged or confirmed with its
probe, a per-commit ledger (read body-free yes/no, findings by id), findings with stable IDs (prefix
`LV`: `LV1`, `LV2`, …) and severities (MAJOR / MODERATE / minor / note), an overall PASS /
PASS-WITH-FINDINGS / FAIL line with counts, a re-run ledger and a follow-up checklist. Then STOP:
act 1 is committed, unrevised, **before** the sibling is opened. Edit no other file.

**Phase 2 (act 2).** Open the sibling and the barred records; screen the delta's commit body;
append `### Reconcile` beneath your verdict, with per-finding notes against the sibling's questions
and the author's account, any finding formed at reconcile marked as such, and the overall line
restated. Never revise act-1 text. Then fold the sibling in below the reconcile and delete it.

The work is doctrine by function, so every finding is the principal's to decide (rule 3): record
all, apply nothing. Counsel per finding is welcome, labelled as counsel and kept beneath it.

---

# Verdict — act 1 (cold, before the sibling)

## Provenance

- **Reviewer:** Fable 5.1 (`claude-fable-5-1`), the principal-named review tier, tier checked at
  selection. Run 2026-11-22 UTC, 22:17 to 22:40.
- **How spawned:** as a subagent of a headless per-pass orchestrator, session `1e1c5269` (Opus 5.5),
  itself started by drain session `eca14b23` (Opus 5.5). Both are rule-4 off-tier orchestrators:
  they hold the context partition, form no finding and write no severity. `eca14b23` wrote no brief
  and no delta and started no brief-writer for this pass. Neither is `947ac694`, `58027096` or
  `d0ca5d24`, and I was started and instructed by none of those three.
- **The order I run under:** the principal's weekly drain of 2026-11-23 NZDT, verbatim: *"Start a
  fable drain or whatever it is called now. Target 100% of weekly budget by 11.30am NZT todat"*.
- **Orchestrator direction, as received (process only):** the item, the worktree path, the brief
  path, the rule to read `REVIEW.md` and skip the session-log step, the partition (the sibling
  removed from the worktree; do not look for it elsewhere), what I may write (this file; a review
  log outside the repo), no commit or push, no live writes, the load rule, the public-repo rule, the
  live-proof instruction and the two-act shape. It carried no question about the delta, no pointer
  to where risk lives and no request to shape a finding. The sibling's release will be recorded in
  act 2.
- **Worktree:** `/Users/mike/worktrees/fable/atelier-160-1260-2216/atelier`, read-only to me except
  this file. `git status` at start: the sibling shown as deleted (the partition), nothing else.
- **What I read, in order:** the brief whole; `docs/method/REVIEW.md` whole; the delta `1bc89816`
  through `coldsweep --commit` with the five `--path`s (subject, stat, diff; no body; the four
  board-store files left out); at HEAD `instruments/ccclose` 225–275, 775–835, 1320–1475, 1885–1927,
  1930–1995, 2840–2870; `instruments/ccclose.test.js` 17–30, 90–120, 150–180, 839–915;
  `instruments/ccclose.design.md` 215–262; `instruments/man/ccclose.1` 225–290;
  `docs/method/CONCURRENCY.md` 1045–1095; `instruments/cclive` 23–58, 710; `cclive.design.md` 85–88;
  `instruments/README.md` 23. Commit subjects only for `1bc89816..HEAD` on the delta paths. No
  session log, no prior verdict, no board item beyond its title, no commit body, no sibling. The
  harness also loaded user-level and repo instruction files and a memory index before the brief;
  nothing in them is an account of this delta.
- **The review log** (method, commands, evidence, kept as I worked) is outside the repo at
  `~/.claude/fable-drain/notes/atelier-160-1260-2216.md`; its act-1 entries predate the sibling's
  release.

## Method

Floor first (`merge-base --is-ancestor`, the suite, the man-page lint), then lens 1 by naming my
own assumptions before any probe, then lenses 2–4 against the delta at the commit and at HEAD,
then the brief's sweep, the live proof, and mutation probes on a scratch copy of `instruments/`
(deleted at the end of the pass). Every test or probe ran under `nice -n 10`, one heavy process at
a time, foreground, after `uptime` (load 4.50 at start, 5.06 before the suite). Left out: the
census itself (not reproducible from the repo, see LV3) and `/security-review` (discharged below).

## Lens 1 — approach and assumptions, named first

- **A1. A transcript's clock is evidence of life.** Confirmed as far as it goes: an agent's own
  file grows as it works (readAgent takes the newest timestamp of any record, test.js 839–870 and
  the live proof below). Its limit is the silence of a working agent: a tool call, a long thought,
  a wait. The delta sets that limit from a census and from the harness's 600 s foreground cap. The
  census is the right population (gaps *between* records are the silences of agents that went on
  to write again), and it reports a 0.1 % tail above the bound: LV2.
- **A2. A fixed bound is the right shape.** Partly confirmed. One bound, one home (`FRESH_MS`),
  shared by `cclive` and `ccopen` by `require`, never copied: sound. But the bound sits exactly on
  the harness's own cap, and the test is strict (`> FRESH_MS`), so an agent waiting on a command
  that runs to the cap is called cut the instant the command returns late by any overhead: LV2.
- **A3. The parent's record is a second, independent signal.** Damaged. Every parent record
  predates the judgement, so `parent.last − a.lastTs > FRESH_MS` can only hold when
  `now − a.lastTs > FRESH_MS` already does. Probe: a grid of 4,375,336 cases with the parent's last
  record anywhere from 30 minutes back up to the judgement instant changed the verdict against a
  parent-less judgement in 0 cases; only a parent record *later than* `now` flips it: LV1.
- **A4. The census measures the thing the bound is used for.** Mostly: live silences, yes;
  but under what load, on what date, on whose machine, by what method is recorded nowhere: LV3.
- **A5. Running must fail the check.** Confirmed against the acceptance test: the hazard in
  `CONCURRENCY.md` § *Teardown waits for the worker to stop* is a close or removal under a working
  agent, and the delta keeps ❌ for running (M6 below shows two tests pin it).

## Lens 2 — correctness; the claims re-driven

| Claim (brief § *The claims*) | Result |
|---|---|
| Running = recent by the clock AND parent silent after it | Clock half holds; parent half never decides (LV1) |
| `FRESH_MS` = 10 min from the census; 600 s = the foreground cap | Figures consistent across five surfaces; not re-runnable (LV3); the cap is a harness fact that can move |
| A dead agent reads as running for ≤ 10 min, and the line says how long | Confirmed (live proof: "last grew 27 s ago"); the opposite error is unstated (LV2) |
| A parent idle while its agent works passes both | Confirmed, trivially: the parent test cannot fail there (LV1) |
| A resumed agent is judged the same way | Confirmed (test.js 902–915; M5 pins it) |
| Running fails like cut, never calls a live agent dead | First half confirmed (M6); second half an overclaim (LV2) |
| Summary line, `--json` `counts`, identifiers carry the count, zeros included | Confirmed (tests 661–668, 695–698, 710–713, 831–834, 1214; live proof shows `running: 1`) |
| `210/070` declined: 130 completed per 50 failed | Not re-drivable; stated in `CHANGELOG.md` only (LV3) |

## Lens 3 — completeness and harvest

- Every surface stating the agent states was updated (design table, bound paragraph, status rule,
  summary format, man page, CHANGELOG); the sweep found no stale "shows as cut" text (V3).
- The bound has one code home; the *census* has none (V4, LV3).
- Tests that stay green on a broken delta (scratch copy, four `210/380` tests by name): M1 delete
  the parent test → only the unit test at test.js 891 fails, and its fixture is a parent record ten
  minutes in the future (LV1); M3 drop `Math.max(0, …)` → green; M4 switch "s"/"min" at 100,000 s →
  green (LV4). Pinned: M2 `>` to `>=` (boundary), M5 drop running in the resumed branch, M6 running
  no longer fails the check.
- Check 15 (`20fd0f09`, outside scope) has its own `running` state for Bash background launches and
  harness tools; it does not judge `Agent` launches (ccclose 1889–1925), so no agent gets two
  verdicts at HEAD. Noted, not a finding.
- Outside scope, seen in passing: at HEAD the design table's *cut mid-flight* row still reads "no
  completed, killed or stopped notification" while the man page says "or failed" (from `50547442`,
  pass `160/1350`). Not this delta's.

## Lens 4 — security and privacy

- **Design altitude.** The check reads the session's own `subagents/` directory beside its
  transcript and prints each agent's description and end into a record; the delta adds a relative
  time ("N s ago") and nothing else. No new collection, no new surface. The description printing
  predates the delta.
- **Code altitude** (ASVS V5 input handling, V7 output into records, by hand): the only new inputs
  are record timestamps, already parsed with `Date.parse` and dropped unless finite (ccclose 1360–
  1362, 809–812); the new line is built from numbers; no shell, no path, no HTML. `FRESH_MS` is a
  constant. Clean.
- **`/security-review`: discharged by grounds.** It reads the session's pending diff, not a path;
  this worktree is dirty with the sibling's removal and, from act 1, with this brief, so an aim
  would scan deferred material (the SL2 class); the delta is landed, 41 lines of JS whose new
  inputs are the timestamps above. A scratch-clone reproduction would weigh as nothing beyond the
  hand read. Exposure: none.

## Standing checklist

- **V1** — LV1 (a mechanism described that never decides), LV2 (an error direction denied), LV3 (a
  measurement with no record).
- **V2** — Suite and lint re-run (ledger below). Live proof re-driven. Census NOT RUN: no method in
  the tree to re-run (LV3).
- **V3** — Swept with `coldsweep` (brief's command plus `cut mid-flight|3,587|881,904`): 109 hits
  over 747 files, 1006 excluded as barred; the sibling exclusion matched nothing (removed on
  purpose). No stale mirror. Discharged.
- **V4** — `FRESH_MS` one home, consumers `require` it. The census figures: five copies, no home
  (LV3).
- **V5** — Code, comment, design note, man page and CHANGELOG agree with each other on the
  mechanism and disagree with the code's effective behaviour (LV1); the design note's "never calls
  a live agent dead" disagrees with the man page's "only the second says the agent is dead" and
  with the census tail (LV2). Cross-references: `CONCURRENCY.md` § *Orchestrated queue runs*
  reaches the teardown rule the check guards; `cclive.design.md` 85–88 reaches `FRESH_MS` in
  `ccclose` and names it as the source.
- **V6** — Lens 4 above.
- **V7** — Provenance above; the brief's § *Spawn provenance* matches what I observed.

## Per-commit ledger

| Commit | Read body-free | Findings |
|---|---|---|
| `1bc89816` ccclose: tell a running subagent from a cut one; decline the 070 third figure | yes (`coldsweep --commit`, five `--path`s) | LV1, LV2, LV3, LV4, LV5 |
| `50547442`, `6890e9db` (non-goals) | subjects only; their effect read at HEAD | none |
| `20fd0f09` check 15 | subject; HEAD 1885–1995 read for the `running` vocabulary | none |
| `8556061a`, `e4d572d1`, `54f91ad3`, `1568acce`, `b68cf410`, `74a0ceaf` | subjects only | none; other checks |

## Findings

**LV1 — MODERATE.** *The parent-clock test never decides a verdict; four surfaces describe it as a
second signal.* `runningVerdict` (ccclose 1377–1384) returns null when `now − a.lastTs > FRESH_MS`,
then when `parent.last − a.lastTs > FRESH_MS`. Every parent record is written before the judgement,
so `parent.last ≤ now` and the second inequality implies the first: the second test can only bite
on a parent record stamped later than the judgement. Probe: 4,375,336 cases, 0 differences from a
parent-less judgement (review log). Mutation M1 (line deleted): the only failing test is
`judgeAgent: the freshness test reads the agent clock and the parent clock` (test.js 884–899),
whose fixture is `parent(T + F)` judged at `now = T`, a parent record ten minutes in the future.
Yet the code comment ("two tests against evidence in the data", 1371–1376), the design table
(236), the man page (268–270) and `CHANGELOG.md` (704–705) all state the parent half as a working
condition. The verdict a user gets is a clock and nothing more. No hazard opens (the clock-only
verdict is identical), which is why this is not MAJOR; the apex's honesty burden is why it is not
minor. *Counsel:* either remove the second test and the four statements, or make it a signal that
can occur (for example, the parent wrote a notification or turn after the agent's last record and
the agent has been silent longer than some bound shorter than `FRESH_MS`) and pin it with a fixture
that can happen.

**LV2 — MODERATE.** *The bound's error is stated in one direction only, and one surface denies the
other.* The delta's own census says 0.1 % of the gaps between consecutive records of agents that
went on to write again exceed 600 s (about 882 of 881,904). During such a gap a live agent falls
through to `cut mid-flight: last turn is a tool_use with no result after it` (1425–1428), which the
man page itself reads as "says the agent is dead" (272–273). The design note says the check "never
calls a live agent dead" (245); the code comment says a working agent "is silent for at most"
600 s (1345–1346) while the test is strict at exactly 600 s, so a command run to the harness's own
cap plus any overhead already crosses it (test.js 888–890 pins `T − F − 1` as cut). The brief names
a line pasted into a record saying an agent is dead when it is not as the second-worst failure;
`CONCURRENCY.md` 1050–1095 is explicit that a quiet tree is never evidence of *stopped*, and this
line would be read as exactly that evidence. The close is still blocked (both states are ❌), so
the teardown hazard is held by the gate, not by the line. *Counsel:* state both error directions
wherever one is stated (code comment, design note, man page), drop "never calls a live agent dead",
and consider either a margin above the harness cap or a cut line that carries the silence length
("silent 11 min; cut, or a long wait") so the record does not assert death from a clock.

**LV3 — minor.** *The census has no home.* Its figures (3,587 logs, 881,904 gaps, 83 s, 600 s;
130 completed per 50 failed for `210/070`) appear in `instruments/ccclose` 1343–1345,
`ccclose.design.md` 240–242, `man/ccclose.1` 275–277, `CHANGELOG.md` 706–712 and
`cclive.design.md` 85–88, with no date, population, machine or method anywhere in the tree, and the
`210/070` figure in the CHANGELOG alone. A reviewer cannot re-run it (V2 NOT RUN), an adopter of
this public repo inherits one estate's number as a constant, and a re-census has five copies to
update with none marked as the copy (V4). The second grounding, the harness's 600 s foreground cap,
is a release-dependent fact stated as a constant. *Counsel:* one dated census record in the design
note (method, population, date, the command), the other four pointing at it; the cap stamped as a
harness fact with the version it was read from.

**LV4 — minor.** *Two cosmetic branches are unpinned.* `Math.max(0, …)` (a record stamped after
the judgement would print a negative age) and the 90 s switch from seconds to minutes survive
mutation (M3, M4); the end-to-end tests match only `\d+ (s|min) ago`. There is also no end-to-end
test of a *foreground* agent with no `tool_result` that is fresh, the shape the live proof below
exercised; the code path is shared, so this is a gap in the pins, not in the behaviour.

**LV5 — note.** `checkSubagents` calls `judgeAgent(a, t)` with no `now`, so a `--session` read of
a past session judges its agents against the wall clock, not the transcript's end (`gather` builds
`w.last` from the transcript for a non-live session, 2853, but check 12 does not use it). A session
whose transcript ended within the last ten minutes with a cut agent reads *running* until the
clock passes; the man page's "run ccclose again to settle it" covers it. Recorded for the
principal's awareness; no action proposed.

## Overall

**PASS-WITH-FINDINGS — 0 MAJOR, 2 MODERATE (LV1, LV2), 2 minor (LV3, LV4), 1 note (LV5).** The
work is doctrine by function (rule 3): every finding is the principal's to decide; nothing applied.

## Re-run ledger

| Line | When (UTC) | Result |
|---|---|---|
| `git merge-base --is-ancestor 1bc89816 HEAD` | 2026-11-22 22:18 | exit 0 |
| `nice -n 10 node --test instruments/ccclose.test.js` (worktree root, foreground) | 22:24–22:31 | exit 0; 153 tests, 153 pass, 0 fail; 431,529 ms |
| `/usr/bin/mandoc -T lint -W style instruments/man/ccclose.1` | 22:22 | exit 0, no output |
| Live proof, during (one haiku agent waiting 180 s): `ccclose --session "$CLAUDE_CODE_SESSION_ID" --json` | 22:23:32 | fail; agents 2 · **running 2** (this reviewer, foreground, "1 s ago"; the waiter, background, "27 s ago"); every other count 0 |
| Live proof, after the waiter reported | 22:31:37 | counts agents 2 · **reported 1** (completed notification) · **running 1** (this reviewer, "5 s ago") |
| The census (3,587 logs) | — | NOT RUN: no method in the tree (LV3) |
| `coldsweep` sweep as the brief prescribes, plus `cut mid-flight\|3,587\|881,904` | 22:21 | 109 hits / 747 files; 1006 barred; no stale mirror |

The env var resolved to the orchestrator's id, `1e1c5269-…`: a subagent inherits its parent's id,
so the read covered the orchestrator's agents, which include this reviewer. The waiter's `completed`
notification landed in the session transcript, so a nested agent's end is read like any other.
Both reads were read-only; `ccclose` makes no file writes (grep for the `fs` write and delete calls
over `instruments/ccclose`: none).

## Follow-up checklist (for the principal; rule 3)

- [ ] LV1: remove the parent-clock test and its four statements, or make it a signal that can occur
- [ ] LV2: state both error directions; drop "never calls a live agent dead"; decide margin or line
- [ ] LV3: give the census a dated home; stamp the 600 s cap as a harness fact
- [ ] LV4: pin the `ago` text and a fresh foreground agent, if wanted
- [ ] LV5: awareness only
- [ ] Act 2: reconcile against the sibling (7 questions, 2 facts) and the barred records
