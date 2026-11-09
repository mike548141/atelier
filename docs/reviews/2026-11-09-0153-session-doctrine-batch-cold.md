# Cold pass — five session-doctrine additions the principal approved in one list (360/010, 320/110, 420/010, 280/050, 410/010)

**Pass type:** doctrine cold pass, per `docs/method/REVIEW.md` rule 4 (self-authored doctrine that
governs every later session).
**Tier:** Fable 5.1, the principal-named review tier, checked at selection by whoever takes the
pass. A session that cannot run on it stops (rule 4).
**Status:** BRIEF ONLY. Not run. Held for the principal's explicit approval of the Fable pass.
Written 2026-11-09 UTC by session `d16dc612`, a headless Opus 5.5 brief-writer.
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/1140-rule-4-cold-pass-queued-session-doctrine-batch.md`
(barred until phase 2).
**Size:** medium: six commits, wording only, three method files; five rules to test against their
approved lines and the sibling doctrine.
**Why it earns a review:** These rules decide when a session asks the principal, what it announces
on a shared host, how sessions talk to each other and where a session with no repo records. A wrong
rule costs the principal's attention or a silent collision in every later session.

## Spawn provenance

- **Author of the work under review:** a principal-opened Opus 5.5 queue run, session `722ac2e2`,
  2026-11-09, in its ruling round, and the Sonnet worker it dispatched, which wrote the work (per
  the queue pointer). The author queued this pass and does not take it.
- **Who wrote this brief:** session `d16dc612` (`claude-opus-5-5`), a headless brief-writer started
  on 2026-11-09 by coordinating session `74f2b8cd` (Opus 5.5). `74f2b8cd` built none of this delta
  and forms no finding; its launch prompt was the only instruction, and it carried item numbers, the
  owed-or-not test and house rules, no framing of the work. **Off-tier for review, disclosed: the
  brief-writer forms no finding and writes no severity**, ran no review and used no Fable model.
  Neither was started or instructed by the author. Whoever writes a brief does not run it (the
  principal's rule), so both are barred from this pass.
- **Who reviews:** a session on Fable 5.1 that passes rule 4's criterion, started once the principal
  has approved the Fable pass. **Barred from reviewing:** session `722ac2e2` and every worker it
  dispatched; `d16dc612`; `74f2b8cd`.
- **The principal's approval of this brief:** his request, 2026-11-09, verbatim: *"Check all the
  repo's, any work that requires a fable review but does not have a brief written yet I want you to
  write those briefs then finish this session when thats all done"*. That approves the brief only;
  the Fable gate on the pass is unchanged.
- **Contact, disclosed (rule 4):** the brief-writer had no contact with `722ac2e2` or its workers.
- ⚠️ **Brief-writer's exposure, disclosed** (rule-2 and author-account material met before writing):
  `skills/review-brief/SKILL.md` and `docs/method/REVIEW.md` whole; the house-form brief
  `docs/reviews/2026-11-06-2027-secretscan-exempt-private-keys-cold.md` lines 1–728, verdict
  included (another surface); the queue pointer whole; the intent records' answer and closing notes,
  by extraction; commit subjects and file lists; the delta's `CHANGELOG.md` entries; the results of
  the re-run lines; parts of the delta's own files at HEAD (outlines, constants, comments). It
  opened no commit message body of this delta, and did not open `docs/SESSIONS.md`, `docs/sessions/`
  or the prior verdict on this subject. Its harness loaded user-level and repo instruction files and
  a memory index, which hold private context this brief does not carry. Everything evaluative is in
  the sibling, by count here: a held-back sibling with one pointer block, 2 questions and 1 fact.

## The acceptance test

*"Approve all 20"*, on 2026-11-09, after reading a one-line summary of each of twenty items,
approving the recommendation on each. The recommendation approved, item by item:
- `360/010`: adopt rules 1 and 2 (an owner marker on anything launched on a shared host; a wider
  session-open announcement); rule 3 stays deferred.
- `320/110`: add the gate before the ask device in `COMMUNICATION.md`: no decision is manufactured
  where an explanation would do.
- `420/010`: generalise park-and-proceed into a standing rule with an away mode he can declare; the
  notification question later.
- `280/050`: adopt "talk to decide, write to hold" as the channel design.
- `410/010`: a thin home-directory onramp, with "move to the repo before recording" as the default
  for shaping work; the privacy line travels with any output.

The offered option's words were written by the authoring session and put to the principal; the
quoted pick is his. Recorded as an answer, not a ruling in his words: where the delta's wording goes
past what he picked, say so. These are claims to test, not settled scope.

## What the work is

Six commits on `main`, wording only: one per item and one changelog commit.

Commits on `main`: `2d685d7c`, `96b8be7b`, `1db64e22`, `12a0433c`, `8edaf16c`, `22347dd1`. The
landing commit is `22347dd1`. **Check your tree has it before reading anything:** `git merge-base
--is-ancestor 22347dd1 HEAD` exits 0, and an orchestrator merges `origin/main` into the review
branch before it spawns.

Delta paths: `docs/method/CONCURRENCY.md`, `docs/method/COMMUNICATION.md`, `docs/method/RECORD.md`,
`CHANGELOG.md`. Read each at HEAD and read each commit body-free, scoped to paths so board records
stay barred:

```
python3 tools/coldsweep.py --root . --commit 2d685d7c --path docs/method/CONCURRENCY.md
python3 tools/coldsweep.py --root . --commit 96b8be7b --path docs/method/COMMUNICATION.md
python3 tools/coldsweep.py --root . --commit 1db64e22 --path docs/method/COMMUNICATION.md --path docs/method/CONCURRENCY.md
python3 tools/coldsweep.py --root . --commit 12a0433c --path docs/method/CONCURRENCY.md
python3 tools/coldsweep.py --root . --commit 8edaf16c --path docs/method/RECORD.md
python3 tools/coldsweep.py --root . --commit 22347dd1 --path CHANGELOG.md
```

Plain `git show` is barred: it prints the message body before the diff, and reading is atomic (rule
1). Commits since the delta on these paths:

```
git log --oneline 22347dd1..HEAD -- docs/method/CONCURRENCY.md docs/method/COMMUNICATION.md docs/method/RECORD.md CHANGELOG.md
```

At `457615cc` this printed 14 commit(s). Read anything new the same way.

**Claims the work makes (extracted from its own changelog entry and files, not evaluated):**

- `CONCURRENCY.md` § *Beyond the repo*: an owner marker on anything launched on a shared host; a
  wider open-of-session announcement; a rate-limited API's lockout named as a disguised collision.
- `COMMUNICATION.md` § *Asking for a ruling*: a settled matter is a record, an open one a decision,
  absent evidence adds "find out first".
- `COMMUNICATION.md` § *When to ask*: sort a question by what it blocks; park and proceed on
  branch-blocking ones; proceed on a named assumption only where recoverable and never on a floor
  item; away as a mode he declares.
- `CONCURRENCY.md` § *Talk first*: talk to decide, write to hold; talk-first never reaches a cold
  reviewer.
- `RECORD.md` § *A session with no repo*: a thin onramp, move to the repo before recording, a plain
  close in the reply, the privacy line travelling with any output.

## Scope

The widest the work admits: intent, decisions, assumptions, design, docs, code, test code and live
behaviour. The lenses organise it; they do not bound it. Anything not named a non-goal is in scope.

**Non-goals:** the deferred third rule of `360/010`, the harness-notification question, and the
person-local onramp file, which the delta says it did not build, except where a claim depends on
them.

## The four lenses

1. **Approach & assumptions** — name the load-bearing assumptions yourself, first, and damage each
with a probe or confirm it by re-driving. Ask whether this is the right problem, solved at the right
altitude.
2. **Correctness & quality** — does the work do what its claims above say; honest about done versus
stubbed; any overclaim or silent scope cut, each recorded against the text that makes it.
3. **Completeness / harvest** — every surface that states the rule (V3), one home (V4), no
contradiction with sibling doctrine (V5), tests that would stay green on a broken check, what
already exists that this ignored.
4. **Security & privacy** — mandatory. Doctrine text. The surfaces it can move are privacy of what
is announced across sessions and what a session with no repo records. No code changed, so
`/security-review` has nothing to read: discharge it in one line.

Run the standing checklist V1–V7 unasked (`REVIEW.md` § *The standing checklist*).

## Re-run obligation

Re-run, do not read. The brief-writer ran each line once, on 2026-11-09 UTC, from the worktree root
at `457615cc`; results are in the sibling. Read exit codes explicitly. Check `uptime` first and run
heavy lines under `nice -n 10`. Python is the `python3` on `PATH` (the tests need 3.10 or later;
`/usr/bin/python3` is 3.9 on this machine and some modules fail at import).

- `nice -n 10 python3 tools/floor.py --plane ci --root .`

## House rules for this run

- **Live systems:** read-only reads of live systems as needed; **no live writes**. A check that
  would need a write is marked NOT RUN in the verdict, with what it would have shown.
- Probes run on scratch copies and synthetic fixtures under your scratchpad only, deleted when you
  finish. Never mutate the worktree's `tools/` or `instruments/`.
- Name your own review worktree in the verdict; it is read-only to you except for THIS file. Other
  sessions may be live: touch nothing outside your worktree and scratchpad.
- Read-only git only, beyond committing this one file at the end of each phase (or handing it to the
  orchestrator to commit).
- Child repos are read-only and counted, never named: quote no child's name, path or excerpt.
- One heavy process at a time; foreground, long timeout. Never run an installed tool by bare name
  from `PATH`: use the worktree's own copy.
- `/security-review` reads the session's pending diff, not this delta. Aim it at the code by
  reproducing the diff in a scratch clone, or discharge it by grounds, never with this brief or its
  sibling dirty. Over markdown its clean pass is empty; weigh it as nothing.
- This pass is pending while you run it: anything you write to the session log, the pointer or a
  commit subject before phase 2 names the sibling by file and count only.
- Absolute ISO 8601 dates from `date -u`; prose wrapped at ≤ 100 columns; NZ English. This repo is
  PUBLIC: quote no secret, placeholder token, email address, child repo name or path.
- Review deep, not fast: a finding needs a probe or a re-driven claim behind it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content; the
deferred material lives in the sibling .deferred.md under the rule-1 split, opened only after the
reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`, every prior
verdict in `docs/reviews/`, this brief's sibling
(`2026-11-09-0153-session-doctrine-batch-cold.deferred.md`), every delta commit's message body, the
queue pointer
`docs/roadmap/160-doctrine-review-owed/1140-rule-4-cold-pass-queued-session-doctrine-batch.md`, and
the intent records beyond their titles:

- `docs/roadmap/360-concurrency-beyond-the-repo-mike-commissioned/010-name-what-you-launch-then-widen-the-announcement.md`
- `docs/roadmap/320-child-filed-findings-via-pointing-up/110-proposal-the-ask-device-manufactures-decisions.md`
- `docs/roadmap/420-when-to-ask-mike-commissioned/010-an-ask-stops-the-whole-run-decide-when-to-ask.md`
- `docs/roadmap/280-cross-session-channel-mike-commissioned/050-talk-first-the-channel-as-first-preference.md`
- `docs/roadmap/410-sessions-without-a-repo-mike-commissioned/010-no-doctrine-covers-a-session-with-no-tree.md`

The delta's docstrings, comments, ADR text, `tools/README.md` and `CHANGELOG.md` entries carry the
author's account of why; they are the delta, and reading the delta is never barred.

Sweep with `coldsweep`, never a hand-written exclusion:

```
python3 tools/coldsweep.py --root <your-worktree> \
  --also-exclude docs/roadmap/160-doctrine-review-owed/1140-rule-4-cold-pass-queued-session-doctrine-batch.md \
  --also-exclude docs/roadmap/360-concurrency-beyond-the-repo-mike-commissioned/010-name-what-you-launch-then-widen-the-announcement.md \
  --also-exclude docs/roadmap/320-child-filed-findings-via-pointing-up/110-proposal-the-ask-device-manufactures-decisions.md \
  --also-exclude docs/roadmap/420-when-to-ask-mike-commissioned/010-an-ask-stops-the-whole-run-decide-when-to-ask.md \
  --also-exclude docs/roadmap/280-cross-session-channel-mike-commissioned/050-talk-first-the-channel-as-first-preference.md \
  --also-exclude docs/roadmap/410-sessions-without-a-repo-mike-commissioned/010-no-doctrine-covers-a-session-with-no-tree.md \
  '<pattern>'
```

`--include-barred` only with disclosure in the verdict.

## Process

**Phase 1 (act 1).** Read the acceptance test; reproduce the floor first; work the lenses, your own
assumptions and the re-run list. Append your verdict below a `---` divider in THIS file: provenance
repeated (how you were spawned, your tier, any orchestrator, what you read, the UTC day you ran on),
per-lens answers, V1–V7 each answered or discharged with grounds, each load-bearing assumption
damaged or confirmed with its probe, a per-commit ledger (each of the six commits: read body-free
yes/no, findings by id), findings with stable ids (prefix `SDB`: `SDB1`, `SDB2`, …) and severities
(MAJOR / MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL line with counts, a
re-run ledger (commands and results, children by count only) and a follow-up checklist. Then STOP:
act 1 is committed, unrevised, **before** the sibling is opened. Edit no other file.

**Phase 2 (act 2).** Open the sibling and the barred records; screen the delta commits' bodies;
append `### Reconcile` beneath your verdict: per-finding notes against the sibling's questions and
the author's account, any finding formed at reconcile marked as such, and the overall line restated.
Never revise act-1 text. Then fold the sibling in below the reconcile and delete it.

Every finding on this delta is the principal's to decide (rule 3): record all, apply nothing.
Counsel per finding is welcome, labelled as counsel and kept beneath it.

