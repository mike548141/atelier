# Cold pass — `ccclose` tells a still-running subagent from a cut one

**Board:** `docs/roadmap/160-doctrine-review-owed/1260-rule-4-cold-pass-queued-ccclose-running-state.md`
**Status:** BRIEF ONLY, not run. Written 2026-11-14 UTC by session `947ac694`, a headless Opus 5.5
brief-writer. Queued, waiting on the principal's explicit approval of Fable work; this brief is not
that approval.

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
