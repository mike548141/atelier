# Cold pass — five session-doctrine additions the principal approved in one list (360/010, 320/110, 420/010, 280/050, 410/010)

**Pass type:** doctrine cold pass, per `docs/method/REVIEW.md` rule 4 (self-authored doctrine that
governs every later session).
**Tier:** Fable 5.1, the principal-named review tier, checked at selection by whoever takes the
pass. A session that cannot run on it stops (rule 4).
**Status:** PASS RAN 2026-11-16 UTC on Fable 5.1, act 1 and reconcile written:
PASS-WITH-FINDINGS (0 MAJOR, 2 MODERATE, 5 minor, 3 note, SDB1–SDB10); sibling and review log
folded below the reconcile. Brief written 2026-11-09 UTC by session `d16dc612`, a headless Opus
5.5 brief-writer.
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
(`2026-11-09-0153-session-doctrine-batch-cold.deferred.md`, now folded below the reconcile),
every delta commit's message body, the
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


---

## Verdict — act 1, 2026-11-16 UTC

**Overall: PASS-WITH-FINDINGS.** 0 MAJOR, 2 MODERATE, 6 minor, 2 note (SDB1–SDB10). The five
rules say what their picks say and reconcile with the sibling doctrine on every pointer but one;
the findings are rules the one-line approval did not name, one cross-reference that reaches no
rule and conflicts with a sibling, and wording that outruns its evidence. Every finding is the
principal's to decide (rule 3): recorded, nothing applied. Counsel sits beneath each, labelled.

### Provenance (V7)

- **Reviewer:** Fable 5.1 (`claude-fable-5-1`), the principal-named review tier, checked at
  selection. Ran on 2026-11-16 UTC in the review worktree
  `/Users/mike/worktrees/fable/atelier-160-1140-0848/atelier`, HEAD `e0e4632f`, with
  `git merge-base --is-ancestor 22347dd1 HEAD` exit 0.
- **Spawn:** a headless orchestrator session (Opus 5.5), itself started by drain session
  `1e053526` (Opus 5.5). Both are rule-4 off-tier orchestrators: they hold the context partition,
  form no finding and write no severity. The orchestrator wrote no part of the brief or the delta.
  Not started or instructed by any barred session: `722ac2e2` or any worker it dispatched,
  `d16dc612`, `74f2b8cd`. No contact from any of them during the pass.
- **Under:** the principal's API-credit drain order of 2026-11-16, verbatim: *"I want to use
  things other than my weekly budget to clear as many fable reviews as possible like using fable
  drain. I thought we could start by using up all the API credits I have."* and *"As always you
  must ensure that nothing harms the integrity or quality of the review process and verdicts, for
  example if the review is done by API it must be as good as running it locally"*.
- **The spawn prompt, in substance (process only):** the worktree path; the brief path and the
  instruction to follow it; the finding prefix `SDB`; the partition (the sibling removed from the
  worktree, its path to be sent after act 1 is committed, no other barred record before then); a
  running log at a named path outside the repo, commands and evidence only, appended to the brief
  at the fold; what may be written (the log, act 1 below a divider, the Status line); no commit,
  push or live write; load rules (`uptime`, `nice -n 10`, one process); public-safety rules (ids
  only, no private repo name or path, "principal"); the shape of act 1 and act 2. It carried no
  question about the delta, no pointer to where risk lives, and no request to shape a finding.
  The release message is owed at act 2 and will be recorded there.
- **What I read before writing** (rule 2): the brief whole; `docs/method/REVIEW.md` lines 25–566;
  the six delta commits body-free with `tools/coldsweep.py --commit … --path …` (each exit 0,
  "message body not printed", 0 board-store and 0 barred files touched); the three method files'
  touched sections at HEAD and the sections their pointers reach; `CHANGELOG.md` 960–991;
  `docs/method/README.md`, `skills/session-onramp/SKILL.md`, `docs/build/templates/CLAUDE.md`
  (grep); the session-open prompt at HEAD and as blobs at `22347dd1` and `457615cc`; the four
  group READMEs (`docs/roadmap/{360,280,420,410}-*/README.md`, not on the barred list); board
  items `320/820` (lines 1–3, 45–55) and `180/090` (lines 1–12), not barred. Commit `2a6d7a41`
  body-free. I skipped the onramp's session-log step (rule 2) and opened no barred record. Every
  sweep ran through `coldsweep` with the brief's six `--also-exclude` paths; no `--include-barred`.
- **Exposure, disclosed:** my harness loaded user-level and repo instruction files and a memory
  index, which hold private context this verdict does not carry; none of it gives an account of
  this delta. The board index (`docs/ROADMAP.md`) lines for the four groups were met in sweeps:
  titles and states only.

### The acceptance test, held against the delta (lens 2)

Each section carries "Approved 2026-11-09, `NNN/NNN`, as Mike's pick from options offered, not a
ruling in his words", the shape § *What comes back* requires. What each pick named is in the text:
an owner marker and a wider hello (`360/010`); the record / decision / find-out-first sort before
the device (`320/110`); park-and-proceed with an away mode he declares and the notification
question held (`420/010`); talk to decide, write to hold (`280/050`); a thin person-level onramp,
move to the repo before recording, the privacy line travelling (`410/010`). The non-goals the
delta names (the third `360/010` rule, the notification check, the onramp file, the read-order and
floor-clause re-ordering) are stated as not decided or not built, not rounded up. Where the
wording goes **past** the picks is SDB1.

### Load-bearing assumptions, named and probed (lens 1)

1. *The 2026-08-23 incident grounds rule 1 of § Beyond the repo.* **Confirmed.** The group
   narrative (`docs/roadmap/360-…/README.md`, not barred) records the named container attributed
   at a glance, two random-named ones reported "neither is mine", and the tool restarting its own
   unnamed verifier an hour later. The delta's account matches it.
2. *A rate-limited login produces `Invalid credentials` and a lockout under concurrent probing.*
   **Damaged.** The same narrative records one failed login and reasons that concurrent probing
   "is a lockout"; no visible record shows the error text or an observed lockout (SDB4).
3. *The session-open prompt declares away "in its closing paragraph".* **Damaged.** At `457615cc`,
   `22347dd1` and HEAD the declaration is followed by two further paragraphs (SDB3).
4. *An ask is a stop because "the turn ends".* **Damaged in mechanism, confirmed in effect.** The
   same file, since `2a6d7a41` (2026-11-12), puts the device in the same turn as the account; the
   device waits for him, so the run waits, but no turn ends (SDB6).
5. *"Talk to decide, write to hold" reconciles with law 1.* **Confirmed.** Law 1 (lines 590–595)
   says a message reserves nothing; § Talk first says a message alone never takes a claim and the
   artefact survives the death. The cost clause (two of four rounds were corrections) is the
   existing § *Re-run, don't reason* text (710–716), restated with a pointer.
6. *Talk-first never reaches a cold reviewer.* **Confirmed.** § *What the channel is not* holds the
   "side door into a review" bullet (745–747), which reaches `REVIEW.md` rule 4's disclosed
   contact.
7. *A session with no repo can hand its output to a live session by message.* **Damaged.** § *What
   the channel is not* says the channel "is not a channel for work … Queue, never deliver, in both
   directions", and § Talk first, which the route cites, holds no hand-on rule (SDB2).
8. *The memory store is read by no future session of the repo.* **Confirmed by reasoning only**:
   no doctrine file names the memory store (`grep -ri "memory store"` over `docs/method`: this line
   alone), so there is nothing to contradict; the harness fact could not be re-driven in the repo.
9. *The away cadence has one home.* **Damaged.** `COMMUNICATION.md` § When to ask (424–427) and
   `CONCURRENCY.md` § Orchestrated queue runs (1317–1327) each state the three-step cadence and
   the prompt claim in full; the delta added a pointer and left the copy (SDB3).
10. *The rules the delta adds are the ones he approved.* **Partly damaged.** See SDB1.

### Per-lens answers

- **Lens 1 — approach.** Right problem, right altitude: each rule lands in the file that holds its
  neighbours (the channel section, the asking section, the record's onramp/close rules), with
  pointers rather than restatement in all but the one case above. The altitude of `420/010` is the
  one to watch: it writes binding behaviour (proceed on assumption; floor items queue) from a
  one-line pick, which is a briefing question, not a design fault.
- **Lens 2 — correctness and honesty.** Done versus stubbed is stated plainly in every section
  ("Not decided", "not built", "not settled here"). Overclaims: the closing-paragraph location
  (SDB3), the lockout as observed fact (SDB4), two in-quotes paraphrases (SDB5), "the turn ends"
  (SDB6). No silent scope cut found: the onramp file is named as not built, but the approved thing
  is left with no owner (SDB10).
- **Lens 3 — completeness and harvest.** V3: no skill, template or README restates these rules, so
  nothing is out of step; `skills/session-onramp/SKILL.md` already points at § Beyond the repo (for
  `cclive`, a later commit). V4: one copy too many (SDB3). V5: one pointer reaches no rule and
  conflicts with a sibling (SDB2); every other pointer was followed to the rule it names (log).
  Tests: no test pins these sections; nothing could stay green on a broken rule because no check
  reads them, which is honest for wording-only doctrine. Already existing and ignored: nothing
  found; the cost clause and the side-door bullet are cited, not duplicated.
- **Lens 4 — security and privacy.** `/security-review` discharged: no code changed and the
  scanner's exclusions bar markdown; its pass would be empty, so it was not run. Design altitude:
  the delta widens what a session *announces* (hosts, jobs, shared files, services, and a login)
  and what a repo-less session *carries* into a repo. The second is answered in the text (the
  privacy line travels; abridge and say so; § *The record is public*; `DATA-PROTECTION.md`). The
  first is half answered: hellos are volatile by law 1, but the channel's own rule says a message
  can be kept as primary source and must be abridged on the way into the record, and § Beyond the
  repo neither cites it nor says a login is named by role (SDB7). The delta's own text names no
  host, container, account or private repo. Adjacent, outside the delta: SDB9.

### Standing checklist V1–V7

- **V1** No claim stronger than its evidence: SDB3, SDB4, SDB5, SDB6.
- **V2** Re-run: the brief's one line re-run, exit 0 (ledger below); every "grounded" claim in the
  delta that a non-barred record can reach was checked (assumptions 1–7). The `320/110` grounding
  (seven asks, three on clean items) lives only in the barred item: checked at act 2.
- **V3** Mirror sites swept (log); none restates these rules. Discharged.
- **V4** One home: SDB3 (the away cadence and the prompt claim, twice).
- **V5** Contradictions: SDB2 (hand-on by message versus "queue, never deliver"; a pointer that
  reaches no rule), SDB6 (turn ends versus same turn), SDB8 (local date at rest versus
  `CONVENTIONS.md` UTC-at-rest). Every other cross-reference reached the rule it names.
- **V6** Security and privacy: run at design altitude above; SDB7, SDB9.
- **V7** Provenance: stated in the brief and repeated above.

### Per-commit ledger

| Commit | Path(s) | Read body-free | Findings |
| --- | --- | --- | --- |
| `2d685d7c` | `CONCURRENCY.md` § Beyond the repo; hello bullet | yes | SDB1, SDB4, SDB7 |
| `96b8be7b` | `COMMUNICATION.md` § Asking for a ruling, decision block | yes | SDB1, SDB8 |
| `1db64e22` | `COMMUNICATION.md` § When to ask; `CONCURRENCY.md` orchestrated bullet | yes | SDB1, SDB3, SDB5, SDB6, SDB8 |
| `12a0433c` | `CONCURRENCY.md` § Talk first; cue 3 | yes | SDB1 (least), SDB8 |
| `8edaf16c` | `RECORD.md` § A session with no repo | yes | SDB1, SDB2, SDB8, SDB10 |
| `22347dd1` | `CHANGELOG.md` | yes | none; its summary matches the sections |

### Findings

**SDB1 — MODERATE.** Rules the one-line picks did not name, approved as a list of twenty
(rule 3: an approval stands, and is open to challenge on the briefing). Each is sound on its face;
the point is that he has not been shown them. Per item, what the text adds beyond the pick:
- `420/010` (pick: park-and-proceed as a standing rule, an away mode, notification later):
  *proceeding on an assumption only where recoverable, named in the record*; *a floor item never
  proceeds on assumption, it queues*; *his "don't stop to ask" does not lift the floor*; *a
  whole-run question is asked first, while he is likely present*; the reversible-default row.
- `320/110` (pick: the gate before the device): *when he answers the frame, stop asking in that
  shape and re-examine the form*.
- `410/010` (pick: thin onramp, move to the repo before recording, privacy line travels): the
  hand-on routes; *nothing reusable is left only in the memory store*; a standing scratch repo
  "considered and not adopted"; tree-bound rules "do not bind in form".
- `280/050` (pick: talk to decide, write to hold): the cost clause, the no-answer rule and the
  cold-reviewer bullet; these restate existing rules with pointers, so least past the pick.
- `360/010` (pick: rules 1 and 2): the rate-limited-API paragraph, which the group narrative
  already carries as a candidate surface.
*Counsel:* one re-brief listing these additions, item by item, in plain words; the text can stand
meanwhile, since none conflicts with a sibling rule except as SDB2 records. The floor-item and
recoverable-assumption rules are the two worth his eye: they bind every unattended run.

**SDB2 — MODERATE.** `RECORD.md` § A session with no repo, *Hand-on* (lines 259–262): a route
is "a message to a live session in that repo (`CONCURRENCY.md` § *Talk first*)". § Talk first is
the rule for a session that *meets another's work*; it holds no hand-on rule, so the pointer reaches
nothing for what it cites (V5). And § *What the channel is not* (CONCURRENCY 741–743) says the
channel "is not a channel for work … changes do not cross at all … Queue, never deliver, in both
directions", which the route contradicts as written. *Counsel:* keep the route and say what the
message carries: a pointer to where the output rests and what it is, never the output itself, so
the receiving session queues it as its own item; cite § *What the channel is not* and § *The
channel crosses publication boundaries too* instead of § Talk first.

**SDB3 — minor.** `COMMUNICATION.md` 424–425 and `CONCURRENCY.md` 1322–1324 both say the
session-open prompt declares away "in its closing paragraph". At `457615cc`, `22347dd1` and HEAD
the declaration (*"Try not to stop and ask me questions … I won't be here to answer for several
hours"*) is followed by two further paragraphs (V1). The same two sites each state the three-step
cadence in full, where the delta added a pointer and left the copy (V4). *Counsel:* cite the
paragraph by its words, not its position; cut the `CONCURRENCY.md` copy to the pointer, which that
section's own closing litany bullet says is its rule.

**SDB4 — minor.** `CONCURRENCY.md` 237–239: "Two sessions probing one login inside the same
window produce `Invalid credentials` and a lockout", written as observed. The non-barred record
shows one failed login and the inference that concurrent probing would lock out; neither the error
text nor an actual lockout is recorded there (V1). Reconciled against the item at act 2.
*Counsel:* "would produce … a lockout", and drop the quoted string unless the item records it.

**SDB5 — minor.** `COMMUNICATION.md` 398 and 419 put *"don't stop to ask"* and *"I won't be here
for several hours"* in quotation marks beside "His message" and "When he says". His recorded words
are *"Try not to stop and ask me questions until you have done all the work. I won't be here to
answer for several hours"* (the prompt; the `420` group README). A paraphrase in quotes reads as
his words (V1; `attribscan` passes because it reads commits, not doctrine). *Counsel:* quote
verbatim, or drop the quotation marks and say "a message not to stop and ask".

**SDB6 — minor.** § When to ask's heading and opening (389–393) say an ask is a stop because
"the turn ends and everything behind the question waits". Since `2a6d7a41` the same file says
the account and the device go in the same turn and the session does not end its turn between them.
The effect (the run waits on him) holds; the mechanism named does not (V5). *Counsel:* "the device
waits for him, and everything behind it waits with it".

**SDB7 — minor.** § Beyond the repo (240–242) says to "name that login in the announcement". A
login is an account identifier; a hello is volatile by law 1, yet § *The channel crosses
publication boundaries too* (717–725) says a message may be kept as primary source and is abridged
on the way into the record. The section neither cites that rule nor says the login is named by
role (which account class, on which host), not by value (V6). *Counsel:* "name it by role", plus
the pointer.

**SDB8 — note.** The five "(Approved 2026-11-09 …)" lines carry his local date unmarked; the
landing commits are 2026-11-08 UTC and `CHANGELOG.md` writes "2026-11-09 (his date)".
`CONVENTIONS.md` has UTC at rest, local labelled where doubtable. *Counsel:* "(his date)" on each,
or the UTC date.

**SDB9 — note, outside the delta.** The group narrative that grounds § Beyond the repo names a
child repo beside a secret-store action and a login rate-limit detail, which is the join
`RECORD.md` § *The record is public* regulates. It predates the delta and is not the delta's; it
is flagged by class for the principal to weigh, and not quoted here.

**SDB10 — minor.** The approved onramp (`410/010`, "a thin home-directory onramp") binds a
repo-less session to read a file that does not exist, and the text leaves it "the person's to
create" with no board item and no owner; the `410` group holds only the closed `010`. In this house
a session writes such files on his word, so the rule binds on nothing until someone is tasked.
*Counsel:* a board item for the person-local build, recorded by pointer only (the instance stays
out of the repo, as the section says).

### Re-run ledger

| Command (from the worktree root, `python3` 3.14.6) | Result |
| --- | --- |
| `git merge-base --is-ancestor 22347dd1 HEAD` | exit 0 |
| `git log --oneline 22347dd1..HEAD -- <four delta paths>` | 66 commits (the brief counted 14 at `457615cc`) |
| `tools/coldsweep.py --commit <sha> --path …` × 6 | each exit 0; body not printed; 0 barred files |
| `uptime` before the heavy line | load 5.55 5.17 4.57 |
| `nice -n 10 python3 tools/floor.py --plane ci --root .` | exit 0; every enforced check ✅; 🟡 secretscan 28 and 🟡 leakscan 3 advisory, none on a delta file |
| `git diff --stat 22347dd1 HEAD -- <three method files>` | 356+/138−; delta sections unchanged except cue 3 and the `cclive` paragraph |
| `coldsweep` sweeps (ten patterns, six `--also-exclude`) | mirror sites as logged; no `--include-barred` |
| `/security-review` | NOT RUN: no code; markdown excluded; would be empty |
| Live systems | none needed; none read |

Children: 0 read (none in scope).

### Follow-up checklist

- [ ] The principal rules on SDB1–SDB10 (rule 3); counsel above is counsel only.
- [ ] Act 2: open the sibling and the barred records on release; screen the six commit bodies;
      reconcile SDB4 and the `320/110` grounding against the item; append `### Reconcile`.
- [ ] If SDB1's re-brief is taken, one list to him, item by item, in plain words.
- [ ] Any application of rulings here is a doctrine edit and earns its own cold pass unless this
      pass's MAJOR count (0) closes the cycle (`REVIEW.md`, *when the cycle stops*).

### Reconcile — act 2, 2026-11-16 UTC

**Release message, recorded by the receiver (rule 4):** after act 1 landed on `main` as
`4067468c`, the orchestrator sent, in substance: act 1 is committed unrevised; the held sibling may
be read at its path outside the worktree, plus the barred records and the commit bodies, per Phase
2; append `### Reconcile` only, never revising act-1 text; keep the log; do not fold or delete (the
orchestrator folds); same house rules; run the date and wrap scanners; end with "ACT 2 SAVED". It
carried no question about the delta, no pointer to risk and no request to revise a finding.

**Opened at act 2:** the sibling (one pointer block, two questions, one fact, one re-run result, as
the brief counted); the queue pointer `160/1140`; the five intent records whole; the six commit
bodies (`git log -1 --format=%b`); `docs/SESSIONS.md` by grep for the five item ids only (one
filing-day entry, 2026-09-29, not opened). No prior verdict opened: none bears on these sections.

**The sibling's questions, answered.**
- *Queue pointer: do the two sentences added beyond the approved lines (`320/110`, `420/010`)
  follow from them?* Both come from the intent records, not from the writer: the frame-answer
  rule is `320/110`'s own analysis ("nothing tells a session to re-examine the form when a
  principal answers the frame"), and "his message did not lift the floor" is `420/010`'s first
  bullet. They follow from the items; they are not in the one-line picks. That is SDB1's case,
  and it is wider than two sentences: `420/010`'s "candidate shape, none chosen" lists seven
  rules, and the delta carries six of them (all but the notification check) under a pick that
  named two. The commit bodies say so plainly, so the author's account is honest; the gap is in
  what the principal was shown.
- *Queue pointer: can talk-first reach a cold reviewer?* No, as written: § Talk first bars it
  and the pointer reaches § *What the channel is not*'s side-door bullet and `REVIEW.md` rule 4
  (act 1, assumption 6). `280/050` itself names `280/040` as the constraint. No finding.
- *Brief-writer 1: does a new section restate a rule homed elsewhere?* One: the away cadence and
  the prompt claim, in `COMMUNICATION.md` § When to ask and `CONCURRENCY.md` § Orchestrated queue
  runs (SDB3). The cost clause and the side-door bullet are cited with pointers, not restated.
- *Brief-writer 2: what did he approve, and does the longer text stay inside it?* He approved,
  per each item's 💬 line, "the recommendation on this item" after a one-line summary, in one
  *"Approve all 20"*. The longer text stays inside the **items** (every rule traces to a candidate
  or an analysis line there) and goes past the **lines** (SDB1). `410/010`'s "scratch repo not
  adopted" does follow from the pick, which chose two of the item's three candidates.
- *The held fact* (one list, one-line summaries) is confirmed by the five 💬 lines.
- *Re-run:* the sibling's `floor.py --plane ci` exit 0 with 28 `secretscan` advisories at
  `457615cc` matches mine at `e0e4632f` (exit 0, 28 advisories).

**Per-finding notes against the records and the author's account.**
- **SDB1 — stands, MODERATE.** Sharpened: the additions are the items' own candidates, carried
  into doctrine by a worker that read them, and each commit body lists what it adds. Nothing was
  invented; what is missing is his sight of them. The re-brief is cheap because the list already
  exists in the bodies.
- **SDB2 — stands, MODERATE.** `410/010` names `280/050` ("talk first to a live session in that
  repo") as a candidate route, so the pointer is the item's framing; the conflict with "queue,
  never deliver" and the pointer reaching no hand-on rule are unchanged. The item also names
  `310/140` (a PR as carrier), which the delta leaves open.
- **SDB3 — stands, minor.** The commit body says "the session-open prompt is untouched", which is
  true; the "closing paragraph" claim was inherited from the `160/900` QK7 wording in
  `CONCURRENCY.md` and copied, not checked.
- **SDB4 — revised at reconcile: note, not minor.** `360/010` carries the sentence word for word,
  with "`Invalid credentials` and a lockout", and says it "happened in the commissioning incident,
  twice over". The delta follows its intent record. What remains is that the item's own evidence
  sits in a private child's records, which this pass cannot reach; the group narrative records one
  failed login. The counsel narrows to: cite the item.
- **SDB5 — stands, minor.** The in-quotes paraphrases are the item's: `420/010` writes *"I won't
  be here for several hours"* in italics and *"don't ask"*; his words are in the group README and
  the prompt. The drift started at the item and the delta carried it into doctrine.
- **SDB6 — stands, minor; not the delta's fault.** `2a6d7a41` post-dates the landing by three
  days; the sentence was true when written and is stale at HEAD. Recorded against HEAD.
- **SDB7 — stands, minor.** "name that login in the announcement" is the delta's own sentence;
  the item's rate-limit bullet asks for a line on the surface, not for the login in the hello.
- **SDB8 — stands, note.** The items' 💬 lines date the answer "2026-11-09" without a zone; the
  delta copied the item date.
- **SDB9 — stands, note, outside the delta.** The intent record and the group narrative both
  carry the join, by name; flagged by class, not quoted.
- **SDB10 — stands, minor.** The DONE line says "the home-directory onramp itself is his, and
  personal, so it is not built here"; honest, and no item tracks it.

**Commit bodies screened:** five bodies give the account their diffs show, each naming the
approval as a pick and not a ruling, each naming what it leaves open; the changelog commit has
no body. No body claims more than its diff. No finding formed at reconcile; one revised (SDB4).

**Overall line, restated:** PASS-WITH-FINDINGS — 0 MAJOR, 2 MODERATE (SDB1, SDB2), 5 minor
(SDB3, SDB5, SDB6, SDB7, SDB10), 3 note (SDB4, SDB8, SDB9). Every finding is the principal's to
decide; nothing applied.

## Deferred sibling, folded below the verdict (orchestrator, 2026-11-16)

The text below is the brief's held-back sibling,
`2026-11-09-0153-session-doctrine-batch-cold.deferred.md`, copied verbatim. It was removed from
the review worktree before the reviewer started, held outside the tree until act 1 was committed
(`4067468c`), then released to the reviewer for act 2. The orchestrator forms no finding and has
not edited it; the sibling file itself is deleted in the fold commit, so the brief carries the
whole record.

# Deferred reading for `2026-11-09-0153-session-doctrine-batch-cold.md`

Open only after your act-1 findings are committed (`docs/method/REVIEW.md` rule 1). Fold into the
brief below the reconcile, then delete this file. A floor, never a fence.

## The queue pointer's questions (the author's framing, verbatim)

> whether the two sentences the writer added beyond the approved lines (in `320/110` and `420/010`)
follow from them; whether talk-first can reach a cold reviewer.

## The brief-writer's questions

1. Does any new section restate a rule already homed elsewhere in `docs/method/`?
2. When the approved line was a one-line summary, what did the principal actually approve, and does
the longer text stay inside it?

## What the brief-writer held back

- The approval was given in one list after one-line summaries, per each item's note.

## Re-run results (2026-11-09 UTC, at `457615cc`)

`floor.py --plane ci`: exit 0, with 28 `secretscan` advisories reported and not blocking.

## Review log (reviewer, verbatim; private while the pass ran, opened at the fold)

# Review log — atelier 160/1140, session-doctrine batch cold pass (prefix SDB)

Reviewer: Fable 5.1. Worktree: /Users/mike/worktrees/fable/atelier-160-1140-0848/atelier
Brief: docs/reviews/2026-11-09-0153-session-doctrine-batch-cold.md
Started 2026-11-16T08:50Z. Commands, files, evidence only.

## Act 1

- 08:50Z `uptime`: load 3.56 4.84 4.34 (16 GB laptop, several passes). `date -u` = 2026-11-16.
- `git status --short`: only ` D docs/reviews/...deferred.md` (sibling removed on purpose). HEAD e0e4632f.
- `git merge-base --is-ancestor 22347dd1 HEAD` exit 0: landing commit present.
- `git log --oneline 22347dd1..HEAD -- <4 delta paths>`: 66 commits (brief said 14 at 457615cc). Must
  read the three method files at HEAD and diff the delta sections against the delta commits.
- `python3 --version` = 3.14.6 on PATH. `tools/coldsweep.py --help` read: --commit prints subject,
  stat, diff, never body; --path scopes.
- `grep -rn "SDB1\b" docs/reviews`: only this brief. Prefix free.
- Read brief lines 1-224 whole.
- Read `docs/method/REVIEW.md` lines 25-300 (rules 1-4), 302-566 (lenses, re-run, V1-V7, lifecycle,
  open-record ruling 2026-11-15).
- Six delta commits read with `tools/coldsweep.py --root <W> --commit <sha> --path <paths>` exactly
  as the brief lists; every run exit 0, "message body not printed", 0 board-store files, 0 barred
  files touched. Diffs noted:
  - 2d685d7c CONCURRENCY.md +49/-1: new `## Beyond the repo` (rules 1-2, rate-limited API para,
    "Not decided, and not built"); hello bullet gains "Off-repo claims ... ride in the same hello".
  - 96b8be7b COMMUNICATION.md +24: "First, establish that there is a decision" block inserted in
    § Asking for a ruling before "Use the harness's structured decision device".
  - 1db64e22 COMMUNICATION.md +46 new `## When to ask` (table, three bullets, away mode, not
    decided); CONCURRENCY.md orchestrated-run "When to ask is per run too" bullet points at it.
  - 12a0433c CONCURRENCY.md +37/-1: `### Talk first` inserted before `### What the channel carries`;
    cue 3 "Ask, when a channel exists" gains "and asks the owner before it works around".
  - 8edaf16c RECORD.md +42: new `## A session with no repo` before `## Decisions`.
  - 22347dd1 CHANGELOG.md +26: "Added (2026-11-08 — five session-and-ask doctrine additions)".
- Scratch script `/tmp/sdb-scratch/sweep.sh` (coldsweep with the brief's six --also-exclude, -i)
  swept: park and proceed; away mode phrases; talk first; owner marker/Beyond the repo; session with
  no repo; find out first; "negoitate"; "when to ask rather than if"; "don.t stop to ask";
  rate-limited. Hits: the three method files, CHANGELOG 972-991, docs/ROADMAP.md index lines,
  group READMEs 360/410, `skills/session-onramp/SKILL.md:46` (Beyond the repo, cclive), 
  `instruments/cclive.design.md` (3), `docs/method/PROPAGATION.md:853` (talk-first message),
  board items 310/140, 320/820, 160/1290. No skill or template restates park-and-proceed or the
  away cadence. "when to ask rather than if" appears nowhere outside the barred item (the 420 group
  README carries it, in a longer quote).
- Read at HEAD: CONCURRENCY.md 60-85 (cue 3), 200-251 (Beyond the repo), 564-662 (channel, laws,
  Talk first, hello), 693-716 (cost clause), 717-733 (publication boundaries), 734-757 (what the
  channel is not), 851-912 (Surviving an interrupted session), 1300-1335 (orchestrated-run bullets);
  COMMUNICATION.md 14-33, 214-260, 330-433; RECORD.md 234-275, 497-543; AUTONOMY.md 40-60,
  140-165; DATA-PROTECTION.md headings; 00-APEX.md account lines (grep); CONVENTIONS.md UTC rows;
  docs/method/README.md 43-47, 60-64, 105-109; skills/session-onramp/SKILL.md 25-70;
  docs/method/session-open/session-open-prompt.md tail (HEAD, and the blob at 22347dd1 and
  457615cc via `git show <sha>:<path>`, which prints no commit message); group READMEs
  docs/roadmap/{360,280,420,410}-*/README.md whole (not on the barred list); board item 320/820
  lines 1-3, 45-55 and 180/090 lines 1-12 (not barred).
- `git diff --stat 22347dd1 HEAD -- <3 method files>`: 356+/138-. Hunks touching the delta's own
  sections: CONCURRENCY cue 3 (expanded, 2d685d7c's clause kept), Beyond the repo (cclive paragraph
  added, 6197df86). § Talk first, hello bullet, COMMUNICATION decision block and § When to ask,
  RECORD § A session with no repo: no hunks since landing. `coldsweep --commit 2a6d7a41 --path
  docs/method/COMMUNICATION.md` read body-free: the account-then-device rule now "in the same turn".
- Re-run: `uptime` load 5.55; `nice -n 10 python3 tools/floor.py --plane ci --root <W>` exit 0,
  output in /tmp/sdb-scratch/floor.out: every enforced check ✅ except 🟡 secretscan (28 advisory)
  and 🟡 leakscan (3 advisory); no advisory names a delta file (grep of the output). datescan,
  wrapscan, spellscan enforced and ✅.
- Cross-references reached (V5): § What the channel is not holds the "side door into a review"
  bullet (CONCURRENCY 745-747); § Surviving an interrupted session holds "write the open question
  into the durable record" (880-886); § Claiming work holds orphan claims on evidence never a timer
  (537, 906); § Re-run, don't reason holds the four-rounds/two-corrections cost (710-716); § The
  record is public and DATA-PROTECTION.md exist; COMMUNICATION's calibration pattern/instance split
  is lines 14-33; CONCURRENCY orchestrated-run bullet 1317-1327 points at § When to ask.
- Evidence checks: group README 360 records the named-vs-random container attribution and the tool
  restarting its own unnamed verifier (matches § Beyond the repo rule 1); it records ONE failed
  login against a rate-limited API and infers a lockout; no error text. The session-open prompt's
  away paragraph is followed by two more paragraphs at 457615cc, 22347dd1 and HEAD. 420 README
  quotes his words: "Try not to stop and ask me questions until you have done all the work. I
  won't be here to answer for several hours". Tests: no tools/test_*.py pins these sections
  (grep "When to ask|Talk first|Beyond the repo|no repo" over tools/test_*.py: none).
- Candidate findings formed (evidence above): one-line picks vs rules added (rule 3 informed
  approval); RECORD hand-on by message vs § What the channel is not "queue, never deliver" and
  § Talk first not holding a hand-on rule; "closing paragraph" false at landing and HEAD, and the
  away cadence stated twice; `Invalid credentials` + lockout stronger than the visible record;
  two in-quotes paraphrases of his words; "the turn ends" vs the 2026-11-12 same-turn rule;
  a login named in a hello with no by-role/abridge clause; local approval date unmarked at rest;
  the approved onramp file has no item or owner; the grounding narrative's repo-to-posture join
  (outside the delta, by class).
- Left out: the 66 later commits beyond their hunks on the delta sections (read by diff, not one
  by one); `/security-review` (no code; discharged); the barred item files, sibling, commit
  bodies, SESSIONS.md, docs/sessions/, prior verdicts (rule 2, act 2). No live system read was
  needed. Scratch: /tmp/sdb-scratch (sweep.sh, floor.out), deleted at the end of act 1.
- 08:59Z act 1 appended to the brief below a `---` divider; Status line updated (ACT 1 WRITTEN
  2026-11-16 UTC, PASS-WITH-FINDINGS 0/2/6/2). Scanners on the brief, each by worktree path with
  `--root <W>`: datescan exit 0 (479 lines read), reviewscan exit 0 (1 brief keeps deferred
  material out), leakscan exit 0 (0 findings); wrapscan and spellscan exit 0 but read 0 files
  (docs/reviews is in their ignore files), so widths were checked by awk: 0 prose lines > 100
  columns after rewrapping five of my own lines. `git status --short`: only the brief modified and
  the sibling deleted. Scratch /tmp/sdb-scratch removed. ACT 1 SAVED; waiting for the sibling path.

## Act 2

- Release message received after act 1 was committed on main (4067468c), process only: the held
  sibling's path (one file outside the worktree), the barred records and commit bodies now open;
  append `### Reconcile` only; keep logging; no fold, no delete; same house rules; run the date
  and wrap scanners; end with "ACT 2 SAVED". No question about the delta, no pointer to risk.
- Read: the sibling whole (pointer block, 2 questions, 1 fact, re-run: floor exit 0 with 28
  secretscan advisories at 457615cc); queue pointer 160/1140 whole; the five intent records whole;
  six commit bodies via `git log -1 --format='%s%n%n%b'`; `grep` of docs/SESSIONS.md for the five
  ids (one 2026-09-29 filing entry; not opened). No prior verdict opened.
- Evidence found: 420/010's "candidate shape, none chosen" lists seven rules; the delta carries six;
  its first bullet has "His message did not lift the floor" and the italic "I won't be here for
  several hours". 320/110's analysis has the frame-answer sentence; its candidate rule block is the
  three-way sort. 360/010 carries "`Invalid credentials` and a lockout ... happened in the
  commissioning incident, twice over" verbatim. 410/010 names 280/050 and 310/140 as candidate
  hand-on routes and its DONE line says the onramp "is his, and personal, so it is not built here".
  Each item's 💬 line: "Approve all 20" after one-line summaries. Commit bodies list the additions
  and the open parts; 22347dd1 has no body.
- Reconcile appended: SDB4 revised to note (follows its intent record); all others stand; no new
  finding. Overall restated: 0 MAJOR, 2 MODERATE, 5 minor, 3 note.
- Scanners on the brief after act 2: datescan, wrapscan, leakscan, reviewscan (exit codes in the
  shell output); widths by awk: 0 prose lines > 100 columns. `git status --short`: brief modified,
  sibling deleted, nothing else. ACT 2 SAVED.
