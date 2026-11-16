# Cold pass — five session-doctrine additions the principal approved in one list (360/010, 320/110, 420/010, 280/050, 410/010)

**Pass type:** doctrine cold pass, per `docs/method/REVIEW.md` rule 4 (self-authored doctrine that
governs every later session).
**Tier:** Fable 5.1, the principal-named review tier, checked at selection by whoever takes the
pass. A session that cannot run on it stops (rule 4).
**Status:** ACT 1 WRITTEN 2026-11-16 UTC on Fable 5.1: PASS-WITH-FINDINGS (0 MAJOR, 2 MODERATE,
6 minor, 2 note, SDB1–SDB10); act 2 (reconcile) owed once the sibling is released. Brief written
2026-11-09 UTC by session `d16dc612`, a headless Opus 5.5 brief-writer.
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
