# Cold pass — `ccclose` names a `failed` agent as its own state

**Board:** `docs/roadmap/160-doctrine-review-owed/1350-rule-4-cold-pass-queued-ccclose-failed-state.md`
**Status:** ACT 1 WRITTEN 2026-11-22 UTC: **FAIL** (1 MAJOR, 1 MODERATE, 5 minor, 2 notes), by a
Fable 5.1 cold reviewer under orchestrator session `98afb222` (drain session `eca14b23`). Act 2, the
reconcile with the sibling, is pending. Every finding is the principal's to decide (rule 3). Brief
written 2026-11-14 UTC by session `6321275c`, a headless Opus 5.5 brief-writer.

**Pass type:** code cold pass, per `docs/method/REVIEW.md` rule 4 (a close check whose pass is read
as "safe to close" is doctrine by function, rule 3).
**Tier:** Fable 5.1, the principal-named review tier, checked at selection by whoever takes the
pass. A session that cannot run on it stops (rule 4).
**Size of this pass:** small: about 15 lines of code, 60 lines of tests and 30 lines of design note,
manual and changelog in one commit.
**Why it earns a review:** `ccclose` is what a session runs to answer "ready to close?", and its
subagent check is pasted into close records as the account of how each agent ended. The delta adds
a state that overrides two other kinds of evidence: the agent's own transcript and, for a
foreground agent, the `tool_result` on its launch. The worst failure is an agent read as `failed`
when it is not (a live or finished agent called dead, so a record states a false death or a session
redoes or abandons good work); the second worst is the opposite, a dead agent still passing as
reported, so a close goes ahead over lost work.

## Spawn provenance

- **Author of the work under review:** a principal-opened Opus 5.5 queue run, session `d0ca5d24`,
  2026-11-09 UTC, and the worker it dispatched, which wrote the code (per the queue pointer). The
  author queued this pass and does not take it.
- **Who wrote this brief:** session `6321275c` (`claude-opus-5-5`), a headless brief-writer started
  2026-11-14 UTC by an estate health sweep, orchestrator session `58027096` (Opus), on the
  principal's instruction that a brief is written for every review known to be owed. Neither wrote
  any of this delta. **Off-tier for review, disclosed: the brief-writer forms no finding and writes
  no severity**, and stops after writing. It ran no review and used no Fable model.
- **Barred from running this pass:** session `6321275c` and session `58027096` (whoever writes a
  brief does not run it), and session `d0ca5d24` with everything it started.
- **Contact, disclosed (rule 4):** the brief-writer's only instruction came from `58027096`: the
  item number, the pointer's opening sentence, and the rules of the sweep. It carried no framing of
  the work. The brief-writer had no contact with the author session or its workers.
- **Who reviews:** a fresh Fable 5.1 session started for this pass alone, by a session that passes
  rule 4's criterion. An orchestrator may hold the context partition and commit the records
  off-tier, only if it forms no finding, writes no severity, and is disclosed in the claim, the
  pointer and the verdict.
- ⚠️ **Brief-writer's exposure, disclosed** (rule-2 and author-account material met before writing):
  its launch prompt; `skills/review-brief/SKILL.md` whole; the queue pointer of `160/1350` whole;
  the intent record `210/400` whole, **including its DONE note** (the author's account); the delta
  read body-free through `coldsweep`; `instruments/ccclose` at HEAD around the notification parser
  and `judgeAgent`; commit subjects through `git log`; a grep of the state vocabulary across the
  tree; the brief and sibling of the neighbouring pass `2026-11-14-0154-ccclose-running-state`
  (read whole for house form and overlap, no verdict in it, and its sibling names this delta); the
  tail of `docs/SESSIONS.md`, for record form; the results of the re-run lines below. It did
  **not** open any prior verdict or the delta commit's message body. Its harness also loaded
  user-level and repo instruction files and a memory index, which hold private context this brief
  does not carry. Everything evaluative it formed is in the sibling.

## The acceptance test

No record the brief-writer read carries a ruling of the principal's on this design. Judge it against
`instruments/ccclose.design.md` (the agent-states table and the paragraphs under it),
`instruments/man/ccclose.1` (*Subagents finished*), and the hazard in `docs/method/CONCURRENCY.md`
§ *Orchestrated queue runs* (*Teardown waits for the worker to stop*) that the check exists to
guard. A record that a close check writes must not state an agent's end more strongly than the
evidence holds (`REVIEW.md` V1 applies to the tool's output as much as to prose).

## What the work is

- **`50547442`** — `ccclose: name a failed agent notification as its own state`.

Delta paths, read at the commit and at HEAD:

- `instruments/ccclose`, `instruments/ccclose.test.js`, `instruments/ccclose.design.md`,
  `instruments/man/ccclose.1`, `CHANGELOG.md`

First confirm the tree holds the delta, then read the commit body-free:

```
git merge-base --is-ancestor 50547442 HEAD; echo $?
python3 tools/coldsweep.py --root . --commit 50547442 --path instruments/ccclose --path \
  instruments/ccclose.test.js --path instruments/ccclose.design.md --path instruments/man/ccclose.1 \
  --path CHANGELOG.md
```

Plain `git show` is barred: it prints the message body before the diff, and reading is atomic (rule
1). The commit also touches the board index and the intent record `210/400`; those are barred until
phase 2, so always pass `--path`.

Then see what has landed on those paths since, and read anything new the same way, only as far as it
bears on this delta at HEAD: `git log --oneline 50547442..HEAD -- instruments/ccclose
instruments/ccclose.test.js instruments/ccclose.design.md instruments/man/ccclose.1` (empty when
this brief was written, at `461fdf92`).

## The claims the delta makes

Extracted from the delta, not evaluated here. They are the author's claims to test, not settled
scope. Name your own load-bearing assumptions first (lens 1).

- A `failed` notification is "the parent's own word that the agent died", and so governs "whatever
  the agent's own transcript or launch `tool_result` says".
- "A measurement of 3,587 agents found 50 so recorded, none ending on `end_turn`" (code comment,
  design note, manual and changelog).
- It is judged "before the launch's `tool_result`" because "a failed foreground agent still returns
  one".
- `failed` is a fail of the check, counted on its own in the summary line, `--json` `counts` and the
  identifiers block, "with a known zero when none"; "never folded into cut or unknown".
- "An unrecognised status still warns."
- A later `completed` notification supersedes a `failed` one (the latest notification governs).
- `CHANGELOG.md`, on the item's second question: `cctranscript`'s header is left alone because "a
  task notification covers background commands as well as agents, so a count would mix them without
  opening the agent logs"; "one notification arrives in up to three carrier shapes and needs
  de-duplicating by task id"; and a new chip "would change a header line other records compare".

## Scope

The widest the work admits: intent, decisions, assumptions, design, docs, code, test code and live
behaviour. The lenses organise it; they do not bound it. Anything not named a non-goal is in scope,
and a non-goal that fences off the risk is a finding.

**Non-goals:** `1bc89816` (`210/380`, the running state, pass `160/1260`) and `6890e9db` (`cclive`,
pass `160/1290`), except as they bear on this delta at HEAD; every other check `ccclose` runs. The
decline of `cctranscript`'s header change is in scope as far as the changelog states its grounds.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself, before anything else. Is a
   parent's `failed` notification the right evidence for "died", strong enough to outrank a
   `tool_result` and an `end_turn`? Is *fail* the right severity for an agent that is no longer
   running, against the acceptance test? Is the census a measurement of the thing the rule is used
   for?
2. **Correctness & quality.** Re-drive the claims above. Record each overclaim against the text that
   makes it, including any claim the delta's tests do not pin. Both of the queue pointer's questions
   are yours: whether a failed foreground agent is judged correctly before its `tool_result`, and
   whether the count of *failed* can mix agents with background commands.
3. **Completeness / harvest.** Every surface that states the agent states or the notification
   statuses (V3); one home for the census figures (V4); no contradiction between code, design note,
   manual and changelog (V5). Find tests that would stay green on a broken delta by mutating a
   scratch copy.
4. **Security & privacy**, mandatory: at design altitude what this exposes, over-collects or leaks
   by weakness of design (the check reads other sessions' transcripts and prints agent descriptions
   into records); at code altitude the likely vectors for its class, checked against an open
   catalogue (OWASP ASVS or the domain's equivalent), notably text from a transcript steering the
   parse. Aim `/security-review` at code only from a clean tree, as *House rules* says; weigh a clean
   pass over markdown as nothing.

Run the standing checklist V1–V7 unasked (`REVIEW.md` § *The standing checklist*).

## Re-run obligation

Re-run, do not read. The brief-writer ran each line once, on 2026-11-14 UTC, from the worktree root,
under `nice`; its results are held in the sibling. Read exit codes explicitly.
Check `uptime` first and run the heavy lines under `nice -n 10`.

```
nice -n 10 node --test instruments/ccclose.test.js
mandoc -T lint -W style instruments/man/ccclose.1
```

**The census.** The figures "3,587 agents", "50 so recorded" and "none ending on `end_turn`" are
asserted proofs in scope. Re-derive them read-only from the local transcript store if you can,
through `instruments/ccclose` or a scratch script that prints counts only, never content; if the
corpus has moved or the method cannot be recovered, say what you measured instead and how it
differs. The brief-writer did not run this.

**The live proof.** No synthetic fixture shows what the harness really writes when an agent fails.
If your store holds a real `failed` notification, run `instruments/ccclose --session <that id>
--json` from your worktree, read-only, and record the `counts` and the agent's line (state and end
only, no description). If none exists, say so; do not provoke a failure in a live session to make
one. The brief-writer did not run this.

## House rules for this run

- **Live systems:** read-only reads of live systems as needed; no live writes. A check that needs a
  write is marked NOT RUN, with why. No push, no write to GitHub, no network service changed.
- **Never print a secret** or any personal data. Other sessions' transcripts are read only through
  `ccclose` or through a script that prints counts; quote none of their content. Probes use scratch
  copies and synthetic fixtures under your scratchpad, deleted when you finish.
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
`docs/reviews/2026-11-14-0242-ccclose-failed-state-cold.deferred.md` (a held-back file; by count: 8
questions, 3 facts), the neighbouring pass's sibling
`docs/reviews/2026-11-14-0154-ccclose-running-state-cold.deferred.md` (it names this delta), every
other item under `docs/roadmap/160-doctrine-review-owed/` beyond its title, the delta commit's
message body, and this intent record beyond its first line:

- `docs/roadmap/210-instruments-open-features/400-a-failed-agent-notification-is-a-status-ccclose-does.md`

The delta's own comments, design note, manual and `CHANGELOG.md` entry carry the author's account of
why; they are the delta, and reading the delta is never barred.

Sweep with `coldsweep`, never a hand-written exclusion:

```
python3 tools/coldsweep.py --root <your-worktree> \
  --also-exclude docs/roadmap/160-doctrine-review-owed \
  --also-exclude docs/roadmap/210-instruments-open-features/400-a-failed-agent-notification-is-a-status-ccclose-does.md \
  --also-exclude docs/reviews/2026-11-14-0242-ccclose-failed-state-cold.deferred.md \
  --also-exclude docs/reviews/2026-11-14-0154-ccclose-running-state-cold.deferred.md \
  "failed|STOP_STATUS|judgeAgent|task-notification"
```

`--include-barred` only with disclosure in the verdict.

## Process

**Phase 1 (act 1).** Reproduce the floor first; work the lenses, your own assumptions and the re-run
list. Append your verdict below a `---` divider in THIS file: provenance repeated (how you were
spawned, your tier, any orchestrator, what you read, the UTC day), per-lens answers, V1–V7 each
answered or discharged with grounds, each load-bearing assumption damaged or confirmed with its
probe, a per-commit ledger (read body-free yes/no, findings by id), findings with stable IDs (prefix
`FA`: `FA1`, `FA2`, …) and severities (MAJOR / MODERATE / minor / note), an overall PASS /
PASS-WITH-FINDINGS / FAIL line with counts, a re-run ledger and a follow-up checklist. Then STOP:
act 1 is committed, unrevised, **before** the sibling is opened. Edit no other file.

**Phase 2 (act 2).** Open the sibling and the barred records; screen the delta's commit body;
append `### Reconcile` beneath your verdict, with per-finding notes against the sibling's questions
and the author's account, any finding formed at reconcile marked as such, and the overall line
restated. Never revise act-1 text. Then fold the sibling in below the reconcile and delete it.

The work is doctrine by function, so every finding is the principal's to decide (rule 3): record
all, apply nothing. Counsel per finding is welcome, labelled as counsel and kept beneath it.

---

## Verdict — act 1 (phase 1), 2026-11-22 UTC

### Provenance (V7)

- **Reviewer:** Fable 5.1 (`claude-fable-5-1`), the principal-named review tier, checked at
  selection. **Spawned by** orchestrator session `98afb222` (Opus 5.5), a headless per-pass
  orchestrator started by drain session `eca14b23` (Opus 5.5) under the principal's drain order of
  2026-11-23 NZDT. Both are off-tier orchestrators: they hold the context partition, formed no
  finding and wrote no severity. Drain session `eca14b23` wrote no brief and no delta and started no
  brief-writer. Neither of the brief's barred sessions (`6321275c`, `58027096`, `d0ca5d24` and what
  it started) started or instructed this reviewer.
- **Review worktree:** `/Users/mike/worktrees/fable/atelier-160-1350-2221/atelier` at `cc23d6e6`
  (the claim commit). Read-only to the reviewer except this file.
- **Partition:** the sibling `…-cold.deferred.md` was removed from the worktree by the orchestrator
  before this reviewer started (` D` in `git status`); it was not sought anywhere. No prior verdict,
  session log, `ROADMAP-DONE.md`, item under `160/`, the body of `210/400` or the delta commit's
  message body was opened. The `coldsweep` vocabulary sweep ran with the brief's exact exclusions
  (the tool warned the sibling path matches no file, as expected).
- **What was read:** this brief whole; `REVIEW.md` rules 1–2, the four lenses, the re-run rule,
  V1–V7 and the lifecycle; the delta through `coldsweep --commit 50547442` with the five `--path`
  flags (body-free; two board files left out); `instruments/ccclose` at HEAD lines 212–248,
  780–839, 1336–1463, 1655–1684, 1935–1969; `ccclose.design.md` 150–160, 205–264;
  `man/ccclose.1` 226–295, 770–775; `CHANGELOG.md` 529–545; `ccclose.test.js` 1–22, 88–176 and the
  delta's tests; `cctranscript` 53–60, 489–510, 574–620 (the changelog's grounds). Harness and
  memory files loaded by the harness hold private context this verdict does not carry.
- **Review log:** a running record of every command, read and result was kept outside the repo and
  is the audit trail of this verdict (REVIEW.md § *A verdict is only as trustworthy as the method*).
  The method and every check are summarised below so a third party can repeat them.

### Method

In order: (1) floor: ancestry of `50547442`, the since-log on the delta paths (seven later commits,
read only at HEAD as code), the commit body-free; (2) code at HEAD around the notification parser,
the transcript reader and `judgeAgent`/`checkSubagents`; the design note, man page and changelog;
(3) the re-run lines; (4) the census, re-derived read-only from the local transcript store with
`ccclose`'s own exported parser (`readTranscript`, `taskNotifications`, `judgeAgent`), counts only;
(5) the live proof on an old session; (6) probes of `judgeAgent` and mutations of a scratch copy of
the instrument against its tests; (7) the security lens by hand. Left out: `/security-review` (see
V6) and the whole suite of every other instrument (not in scope).

### Lens 1 — approach and assumptions, named first

- **A1. A `failed` notification is terminal for the agent.** DAMAGED. The delta treats it as "the
  parent's own word that the agent died" and reads it ahead of every other evidence. In the local
  store, 98 agents ever carried a `failed` notification; **48 of them were resumed afterwards** (48
  of 48 have transcript records after the notification, up to 509 minutes later), **all 48 later
  received a `completed`**, and 47 of the 48 end on `end_turn`. Resume-after-failure is the
  ordinary recovery path in this store, not an edge. See FA1.
- **A2. It outranks a foreground `tool_result`.** CONFIRMED on the evidence available: of the 50
  agents whose latest notification is `failed`, one is foreground, it has a `tool_result` on its
  launch, and its transcript does not end on `end_turn` (n = 1).
- **A3. It outranks an `end_turn`.** NOT EXERCISED LIVE. No agent whose *latest* notification is
  `failed` ends on `end_turn` (0 of 50), so the override the unit test pins never fires at rest in
  this store. The 47 agents with a `failed` notification that do end on `end_turn` were superseded
  by `completed`, so the latest-governs rule, not the override, decides them.
- **A4. Fail is the right severity for an agent that is no longer running.** A judgement, not
  measured. The design gives the hazard for *running* ("a close under a working agent") and leaves
  the reason for `failed` unstated (FA8). As a lost-work signal it is consistent with `cut`.
- **A5. The census measures the population the rule governs.** DAMAGED. The figures count agents
  whose *latest* notification is `failed`; the rule as written ("whatever the agent's own transcript
  … says") governs every agent that *has* a `failed` notification, and 47 of those end on
  `end_turn`. See FA2.

### Lens 2 — correctness: the delta's claims, re-driven

- **Census figures** ("3,587 agents", "50 so recorded", "none ending on `end_turn`"): 50 and 0
  REPRODUCE exactly for latest-`failed` agents; the store holds 3,915 agent logs at this read (it
  has grown). The wording overclaims: FA2.
- **Judged before the launch's `tool_result`; a failed foreground agent still returns one:** code
  order confirmed (lines 1393–1406); live n = 1 confirms; mutation M1 (branch moved after
  `hasResult`) is caught by the tests.
- **A fail, counted apart, known zero, never folded into cut or unknown:** confirmed in code (1433,
  1455, 1459–1461, 2572), in `--json` and `--identifiers`; mutation M2 caught; the live proof shows
  `failed: 1` and exit 1.
- **An unrecognised status still warns:** confirmed (1417–1418) and pinned by the `weird` status in
  the test.
- **A later `completed` supersedes a `failed`:** confirmed (reader 812–816, latest wins; unit test).
  The store shows 48 such supersessions, every one an agent resumed after failing: FA1's case while
  it runs.
- **Changelog: `cctranscript` left alone, three grounds:** the grounds hold. `cctranscript` treats
  a notification as a harness turn and counts no status (489–620); 315 of the 365 latest-`failed`
  task ids are not agents, so a parent-log count would mix them 6:1; all three carriers occur
  (queue-operation 414, attachment 138, user 105).

Both of the queue pointer's questions: (a) a failed foreground agent IS judged before its
`tool_result` (confirmed); (b) check 12's count of *failed* CANNOT mix in background commands, since
it iterates `agent-*.jsonl` files and only looks a notification up by that id (agent ids in the
store are all hex; the 314 non-agent ids are other tokens, 1 hex), so no collision was observed.

### Lens 3 — completeness and harvest

Surfaces that state the agent states (V3): code, design note, man page, changelog, tests. The design
note is updated in its states table but not in two other places (FA3). No README, method doc or
skill states the agent states (swept: `README.md`, `instruments/README.md`, `docs/method`,
`docs/build`, `skills`, `CLAUDE.md`: the two hits of "cut mid-flight" are about sessions, not
agents). One home for the census (V4): FA5. Tests that stay green on a broken delta: mutations M1–M3
are each caught; M4, a resume-aware `failed`, is caught by nothing, so the resume case is unpinned
either way (FA1).

### Lens 4 — security and privacy (V6)

- **`/security-review`: NOT RUN, discharged by grounds.** It scans the session's pending diff; this
  worktree's only pending change was the deletion of the sibling, whose removed lines are the
  deferred content, so running it would have fed the sibling to the reviewer before act 1 (the SL2
  class). The code-altitude read was done by hand against the parser (230–248), the reader (812–833)
  and `judgeAgent`, with OWASP ASVS V5 (input validation) as the catalogue for "text steers the
  parse".
- **Design altitude.** The check reads other sessions' transcripts and prints each agent's
  description into records: pre-existing, and the delta adds no new field; the `failed` end line
  carries no transcript text. The design has no threat line for the notification carriers; FA7.
- **Code altitude.** The one vector of the class is text that reaches the parent transcript as a
  plain `user` record opening with `<task-notification>`: it sets any status for any id (the
  `viaUser` fixture pins that this is accepted). `failed` is the first state designed to outrank
  every other evidence, so a forged `failed` is the one verdict nothing rebuts (FA7, minor). No
  injection into a shell or path: the id is only used as a `Map` key and to build an `agent-<id>`
  filename inside a directory derived from the transcript path; the regex takes `[^<\s]+`, so `..`
  or `/` in an id could in principle name a path outside `subagents/`, but `checkSubagents` iterates
  the directory listing and looks ids up, never the reverse, so no file outside it is opened.

### Standing checklist V1–V7

- **V1** No claim stronger than its evidence: FA1, FA2, FA6.
- **V2** Re-run: ledger below; every line re-run, two reproduced, one reproduced with a moved
  corpus.
- **V3** Mirror sites: FA3 (two places in the design note); other surfaces swept, none hold the
  rule.
- **V4** One fact, one home: FA5.
- **V5** No internal contradiction: FA3, FA4; FA9 (note).
- **V6** Security and privacy: lens 4 above; FA7.
- **V7** Provenance: stated above and in the brief.

### Per-commit ledger

- `50547442` (the delta): read body-free, yes (`coldsweep --commit`, five `--path`). Findings
  FA1–FA8.
- `1bc89816`, `6890e9db` (non-goals): subjects only. No finding; the order of `1bc89816` bears on
  FA4.
- The 7 later commits on the delta paths: subjects only; their effect read as code at HEAD. FA9
  (note, `TERMINAL` at 1665).

### Findings

**FA1 (MAJOR). A `failed` notification is read as the agent's end even when the agent was resumed
after it, so a resumed agent reads `failed` while it is working, and a resumed-then-cut agent reads
`failed` rather than `cut`.** `judgeAgent` (1400–1402) returns `failed` on the notification alone;
the `completed` branch (1407–1416) tests for records after the notification and hands a resumed
agent to `runningVerdict` or calls it cut. Probe on the exported function: a `failed` note an hour
old with the agent's transcript grown 5 s ago returns `failed`; the same shape with `completed`
returns `running`; a resume cut an hour ago returns `failed` against `cut`. The store shows the
case is real: 48 agents were resumed after a `failed` and ran up to 509 minutes later. While one
runs, the summary and the identifiers block say "1 failed" and a session may redo or abandon good
work: the brief's worst failure, and the design's own rule that the check "never calls a live agent
dead (210/380)" (design :245). The resume case is pinned by no test (M4). Breaks: the acceptance
test (an end stated more strongly than the evidence holds), V1, V5 (design :235 vs :236–237).
*Counsel:* give the `failed` branch the `completed` branch's resume test: records after the note ⇒
`runningVerdict`, else "resumed after its failed notification and cut mid-flight"; `failed` only
when nothing follows the note. Pin both directions in `ccclose.test.js`, with a fixture whose agent
records post-date the note (every current fixture's records pre-date it).

**FA2 (MODERATE). The census claim "none ending on `end_turn`" is stated as a property of a
`failed` notification but measured over agents whose latest notification is `failed`.** 47 agents
in the store carry a `failed` notification and end on `end_turn` (after a resume and a later
`completed`). The sentence appears in four places (code 1396–1398, design :235, man :260–261,
changelog :532–533) and is used to justify reading the notification ahead of the transcript, so the
population it excludes is exactly the one the override would misjudge. V1; lens 1 A5. *Counsel:*
restate as "of agents whose last notification is `failed`, none ends on `end_turn`; 48 others were
resumed after a `failed` and completed", in the one home FA5 asks for.

**FA3 (minor). The design note contradicts itself on which notifications end an agent.** Row 12 of
the check table (design :154, "an agent with no finished final turn and no completed, killed or
stopped notification") and the ❌ cut row (:237, "no completed, killed or stopped notification")
were not updated; the man page was (:264, "completed, killed, stopped or failed"). V3, V5.

**FA4 (minor). The changelog calls `failed` "a fifth agent state"; it is the sixth.** `1bc89816`
(still running) is an ancestor of the delta, so the states before it were reported, stopped,
unconsumed, running, cut; the man page (:772) says "the same six counts". V5.

**FA5 (minor). The census figures have four homes and none is stamped a copy.** The store already
holds 3,915 agent logs, so "3,587" is stale in four places at once; `FRESH_MS`'s own census
(1343–1349, design :240) adds a fifth "3,587". V4. *Counsel:* one home (the design note), the
others pointing at it.

**FA6 (minor). The `failed` end line names no contrary evidence.** When the agent's own transcript
ends on `end_turn`, or a foreground `tool_result` exists, the line still reads only "failed (the
parent recorded a failed notification)", whereas the `reported` line says "; its own transcript
stops short of end_turn" when its evidence conflicts (1405). The unit test pins the override with no
disclosure. V1 at the line a record pastes. *Counsel:* append "though its own transcript ends on
end_turn" / "though its launch returned a tool_result" when true.

**FA7 (minor, security, design altitude). A plain `user` record opening with the tag is a
notification carrier, and `failed` is the first state no other evidence can rebut.** Any text that
reaches the parent transcript as a user record (a pasted prompt, a message from another session)
can set `failed` for an agent id and the agent is recorded dead whatever its transcript says. The
carrier predates the delta (the `viaUser` fixture pins it, and the store shows 105 genuine `failed`
notes arrived that way, so it cannot simply be dropped); the delta widens its effect and the design
carries no threat line for the carriers. *Counsel:* name the carrier in the end line, or require the
attachment or queue carrier before `failed` overrides a finished transcript; add the threat line.

**FA8 (note). Why a `failed` agent, which is not running, blocks the close is unstated.** The design
and manual give the hazard for running ("a close under a working agent", design :244, man :272–273)
and nothing for `failed`; as a lost-work signal it matches `cut`, but a reader of the ❌ cannot tell
whether the record asks for a redo, an acknowledgement or nothing. *Counsel:* one sentence in the
design note; the principal's call whether lost work is a blocker or a warning.

**FA9 (note, formed on a later commit, not under review). Check 15 reads a `failed` notification on
launched work as "ended", a pass (`TERMINAL`, 1665; 1957), while check 12 reads it on an agent as a
fail.** Raised as a consistency question for the principal; the asymmetry may be intended (a
background command's failure is its result; an agent's is lost work).

### Overall

**FAIL — 1 MAJOR (FA1), 1 MODERATE (FA2), 5 minor (FA3–FA7), 2 notes (FA8, FA9).** The build does
what its tests pin and the live proof shows; the rule it pins is wrong for the ordinary recovery
path the store shows, and its census is worded over the wrong population.

### Re-run ledger

- `git merge-base --is-ancestor 50547442 HEAD`: exit 0.
- `git log --oneline 50547442..HEAD -- <delta paths>`: 7 commits (the brief saw none at
  `461fdf92`).
- `nice -n 10 node --test instruments/ccclose.test.js`, from the worktree root: 153 tests, 153
  pass, 0 fail, exit 0, 425 s.
- `mandoc -T lint -W style instruments/man/ccclose.1`: no output, exit 0.
- Census (read-only, counts only, `ccclose`'s own exported parser over the local store): 163
  parent transcripts carry the tag; 365 task ids have `failed` as their latest notification, 50 of
  them agents and 315 not; of the 50 agents, 0 end on `end_turn` (stop reasons: stop_sequence 45,
  tool_use 3, null 1, refusal 1); 48 further agents had a `failed` superseded by `completed`, all 48
  with records after the `failed`, 47 ending on `end_turn`; 3,915 agent logs in the store.
- Live proof: `ccclose --session <path> --root <empty scratch repo> --json` with
  `CCCLOSE_GH=/usr/bin/false`, on a session last written 139 days ago: exit 1; counts
  `{agents 1, reported 0, stopped 0, unconsumed 0, running 0, cut 0, failed 1}`; the agent: state
  `failed`, status `fail`, end "failed (the parent recorded a failed notification)"; no stderr.
- `/security-review`: NOT RUN; the pending diff was the sibling's deletion (lens 4).

### Follow-up checklist (for the principal's decision; nothing applied)

- [ ] FA1: resume-aware `failed` branch and tests in both directions.
- [ ] FA2 + FA5: restate the census over its true population, in one home, copies stamped.
- [ ] FA3, FA4: the two design-note rows and the changelog count.
- [ ] FA6: contrary evidence on the `failed` line.
- [ ] FA7: a threat line for the carriers; whether `failed` needs a stronger carrier.
- [ ] FA8, FA9: the principal's word on what a `failed` agent means for a close.
