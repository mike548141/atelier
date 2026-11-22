# Cold pass — `ccclose` names a `failed` agent as its own state

**Board:** `docs/roadmap/160-doctrine-review-owed/1350-rule-4-cold-pass-queued-ccclose-failed-state.md`
**Status:** ACT 2 WRITTEN 2026-11-22 UTC: **FAIL** (1 MAJOR, 2 MODERATE, 5 minor, 2 notes; FA10
formed at reconcile), by a Fable 5.1 cold reviewer under orchestrator session `98afb222` (drain
session `eca14b23`). Act 1 is commit `acd77c18`, unrevised. The sibling is folded in below
the reconcile and the review log appended at the end. Every finding is the principal's to decide
(rule 3). Brief written 2026-11-14 UTC by session `6321275c`, a headless Opus 5.5 brief-writer.

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
`docs/reviews/2026-11-14-0242-ccclose-failed-state-cold.deferred.md` (now folded below; by count: 8
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

### Reconcile — act 2 (phase 2), 2026-11-22 UTC

Opened after act 1 was committed (`acd77c18`): the sibling (8 questions, 3 facts, its re-run
results), the delta commit's message body, the intent record `210/400` whole, and the neighbouring
pass `160/1260`'s brief and sibling where they name this delta; the two older `ccclose` verdicts
were grepped for "failed" only. Act-1 text above is unrevised. Four of the sibling's questions were
already findings formed cold (Q1 = FA1, Q2 = FA8, Q5 = FA3, Q6 = FA2 and FA5); the other four were
probed here, counts only, and one new finding is marked as formed at reconcile.

- **Q1 (resume after a failure) → FA1 stands.** The sibling's suspicion is the act-1 MAJOR, and the
  measurement goes further than the question: 48 agents in the store were resumed after a `failed`
  and every one later completed, so the case is routine, not hypothetical.
- **Q2 (severity) → FA8 stands.** No surface in the delta says what a session does on *failed*; a
  doctrine-wide sweep for a close rule on it was not run. The comparison with *stopped on purpose*
  is apt and is the principal's to weigh.
- **Q3 (the foreground claim) → the claim holds; a new finding, FA10.** The harness does write
  notifications for foreground agents: 24 of 71 foreground agents in the 163 parents have one, and
  the one failed foreground agent in the store has a `failed` notification and a `tool_result`, so
  the fixture shape is real and the ordering is right for it. The sibling's second half is where the
  gap is: `judgeAgent` never reads the launch `tool_result`'s `is_error`.
- **Q4 (background commands) → sound, by fixture and by store.** A synthetic parent with a `failed`
  for a non-agent id and a `failed` for a path-shaped id (`../../<agent id>`) beside a `completed`
  agent gives `failed: 0`, the agent `reported`, check pass; `checkSubagents` only ever looks an id
  up from the directory listing. In the store, 315 non-agent ids carry a latest `failed` and none
  collides with an agent id. The changelog's grounds concede mixing for a count from the parent log
  alone, which is `cctranscript`'s case, not `ccclose`'s.
- **Q5 (mirror sites) → FA3 stands** for the check-table row (:154) and the cut row (:237). The
  `unconsumed` row (:234, "a status the tool does not know") stays correct, since `failed` is no
  longer unknown. No other contradiction was found between code, design note, manual and changelog.
- **Q6 (the census) → FA2 and FA5 stand.** The figures are re-derivable: this verdict's ledger
  gives the method (`ccclose`'s exported parser over the local store, latest notification per id,
  agents = ids with an `agent-<id>.jsonl`), and it reproduces 50 and 0 with the agent total moved to
  3,915. The override of an `end_turn` has no observed case at rest; "whatever the agent's own
  transcript says" is grounded only on the 50 whose transcripts all stop short of `end_turn`.
- **Q7 (status spelling) → sound.** A raw-line census of every `<status>` in the store: completed
  34,966; failed 1,285; killed 359; stopped 80; "running" 26; plus 28 lines that are regexes or
  prose. On a genuine carrier (attachment, queue enqueue or user text opening with the tag)
  `running` occurs 0 times, so the 26 are quoted text. No other spelling of a failure exists; the
  author's account ("the other statuses seen are `completed`, `killed` and `stopped`") holds on the
  carriers.
- **Q8 (which notification governs) → sound.** Over 9,981 carrier notifications in the 163 parents:
  0 records carry more than one block; 55 ids change status; in every one the last by file order is
  also the last by timestamp, and no two statuses share the latest timestamp.
- **Fact 1 (the DONE note repeats the census in the delta's words; no run on a real failed agent)**
  is consistent with FA5, and the live proof above closes the gap it names. **Fact 2** (the
  neighbour's sibling notes the ordering) raises no conflict. **Fact 3** (no later commit at brief
  time): seven have landed since; read as code at HEAD, none alters the `failed` branch.
- **The author's account** (commit body and DONE note) calls `failed` "the one clean signal of a
  dead agent" and does not mention a resume; FA1 is the direct contradiction. Its grounds for
  leaving `cctranscript` alone are confirmed above. Its re-run results (111 tests green at
  `461fdf92`) agree with the 153 green at HEAD; the suite grew with the later commits.

**FA10 (MODERATE, formed at reconcile from sibling Q3). A foreground agent whose launch
`tool_result` is an error, with no notification, reads `reported`, a pass.** `hasResult` (1392)
tests only that a `tool_result` exists; `is_error` is never read in `judgeAgent`, though check 15
reads it for every other launch (1951). Probe on the exported function: foreground, launch result
present, no note, transcript stopping on a `tool_use` → "reported (tool_result on the launch; its
own transcript stops short of end_turn)", status pass. The store holds one real case: a foreground
agent with an error launch result, no notification and a transcript short of `end_turn`. That is the
brief's second-worst failure, a dead agent passing as reported, on the very path the delta's
ordering claim reasons about. The code predates the delta; the delta's claim about foreground
agents is what brings it into scope (lens 2, the pointer's first question). V1. *Counsel:* an error
launch result with no notification is at most a warn, with the error named; or treat it as `failed`
when the harness's own result says the agent errored.

**Overall, restated: FAIL — 1 MAJOR (FA1), 2 MODERATE (FA2, FA10), 5 minor (FA3–FA7), 2 notes
(FA8, FA9).** Record all, apply nothing: every finding is the principal's (rule 3).

## Deferred sibling, folded below the verdict (orchestrator, 2026-11-22)

*Released to the reviewer only after its act-1 findings were committed (locally `acd77c18`, the
hash the reviewer's text cites; landed as `9105eb8a` when rebased before this fold); folded
here verbatim (headings demoted two levels, 1 line(s) over 100 columns wrapped at word boundaries,
no word changed) and the sibling file removed, per the brief. The orchestrator, headless Opus 5.5
session `98afb222` started by drain session `eca14b23`, held the partition, formed no finding and
wrote no severity; drain session `eca14b23` wrote no brief and no delta and started no
brief-writer for this pass.*

### Sibling to the ccclose-failed-state cold pass — held under rule 1's split

Sibling of `docs/reviews/2026-11-14-0242-ccclose-failed-state-cold.md`, held under
`docs/method/REVIEW.md` rule 1's split. **Open only after the phase-1 findings in the brief are
committed.** Written 2026-11-14 UTC by the brief-writer, session `6321275c` (Opus 5.5), named in the
brief's provenance; it forms no finding and assigns no severity. Fold this file in below the
reconcile and delete it at phase 2.

#### Re-run results held back from the brief

Run once by the brief-writer, 2026-11-14 UTC, from the worktree root at `461fdf92`, Node v24.18.0,
machine load averages about 7 on 12 cores:

- `nice -n 10 node --test instruments/ccclose.test.js`: 111 tests, 111 pass, exit 0
  (ℹ duration_ms 122301.906914).
- `mandoc -T lint -W style instruments/man/ccclose.1`: no output, exit 0.
- The census and the live proof: not run (the brief-writer forms no finding, and re-deriving the
  census is the reviewer's measurement to make).

#### Prior records on nearby surfaces (named by filename, not opened unless the brief says so, not
exhaustive)

- `docs/reviews/2026-10-17-1010-ccclose-close-checker-cold.md`
- `docs/reviews/2026-10-18-0506-close-covers-subagents-cold.md`
- `docs/reviews/2026-11-14-0154-ccclose-running-state-cold.md` (the neighbouring pass, `160/1260`)

#### Seeded questions (the brief-writer's suspicions, a floor not a fence)

1. **A resume after a failure.** An agent resumed by `SendMessage` after its `failed` notification,
   whose transcript is growing again and has no new notification yet: the `failed` test runs before
   the running test, so does a working agent read as *failed*? The design note's running paragraph
   says the check "never calls a live agent dead". The only supersession test is a later
   `completed` notification; the `completed` branch has a resume path, the `failed` branch has none.
2. **Severity.** A failed agent is no longer running, so the teardown hazard the check guards does
   not apply to it. As a fail it blocks the close for every session that ever had one, even one that
   saw the failure and redid the work; *stopped on purpose* is a pass for a comparable reason. Is
   fail the right level, and does any doctrine around close say what a session does on *failed*?
3. **The foreground claim.** The test gives the failed foreground agent a `failed` notification in
   the queue-operation shape and a clean `tool_result`. Does the harness actually write a
   `task-notification` for a foreground agent? If not, a failed foreground agent reaches
   `hasResult` and reads as *reported*; the code never looks at the launch `tool_result`'s
   `is_error`. Probe with a fixture of a foreground agent whose launch result is an error and which
   has no notification.
4. **Background commands.** Notes are keyed by task id, and only ids with a file under `subagents/`
   are judged, so a background command's `failed` notification seems unable to enter the count.
   Confirm by fixture, including an id collision, and check that the changelog's reason for leaving
   `cctranscript` alone does not quietly concede the same mixing for `ccclose`.
5. **A mirror site.** The design note's *cut mid-flight* row still reads "no completed, killed or
   stopped notification", while the manual's matching sentence was changed to "completed, killed,
   stopped or failed". Is that a V3/V5 contradiction, and are there others (the design note's line
   about "a status the tool does not know", the `unconsumed` row)?
6. **The census.** "None ending on `end_turn`" is the delta's evidence, yet the code and one test
   make `failed` override an `end_turn`. If no real case was observed, on what is "whatever the
   agent's own transcript says" grounded? Nothing in the delta names the script, the corpus or its
   date, so can anyone re-derive 3,587 and 50 (V1, V2)?
7. **The status spelling.** The match is exact and case-sensitive on `failed`. Does the harness ever
   write another word for the same end (`error`, `failure`, a capitalised form)? Those fall to the
   unknown warn. A status census of the local store, counts only, would settle it.
8. **Which notification governs.** "The latest per agent governs" is implemented as the last one in
   file order, not by timestamp, and the same notification arrives in up to three carrier shapes.
   Can a `failed` and a `completed` for one agent land out of time order, or within one record as
   two blocks, so the wrong one governs?

#### Facts held back from the brief

- The intent record's DONE note states the census figures and the `cctranscript` grounds in the same
  words as the delta's changelog and comments. It records no run on a real failed agent; the
  finding that opened the item came from measuring a different item (`210/070`).
- The neighbouring pass `160/1260` (the running state, `1bc89816`) names this delta a non-goal; its
  sibling notes that this delta places the `failed` test before the launch's `tool_result` and
  before the running test.
- At brief time no commit after `50547442` touched the four delta paths; HEAD was `461fdf92`.

## Review log (reviewer, verbatim; private while the pass ran, opened at the fold)

*Form fixes only: headings demoted two levels; 8 line(s) over 100 columns wrapped at word
boundaries, no word changed. No public-repo gate blocked a token, so no placeholder was needed.*

### Review log — atelier 160/1350 — ccclose names a `failed` agent as its own state

Reviewer: Fable 5.1 (claude-fable-5-1), spawned by orchestrator session 98afb222 (Opus 5.5),
started by drain session eca14b23 (Opus 5.5). Worktree:
/Users/mike/worktrees/fable/atelier-160-1350-2221/atelier. Brief:
docs/reviews/2026-11-14-0242-ccclose-failed-state-cold.md. Sibling removed from the tree by the
orchestrator (git status shows ` D` on it); not sought anywhere.

Method (planned order): (1) brief whole, REVIEW.md rules + lenses + V1–V7 + lifecycle; (2) floor:
ancestry, since-log, coldsweep --commit body-free; (3) code at HEAD around the notification parser
and judgeAgent; design note, man page, CHANGELOG entry; (4) later commits on the delta paths, body-
free, as far as they bear on `failed`; (5) re-run lines (tests, mandoc); (6) census re-derivation,
counts only; (7) live proof, counts/state only; (8) test mutation on a scratch copy; (9) security
lens incl. transcript-steers-parse probe; (10) verdict. Left out: session log, ROADMAP-DONE,
docs/reviews prior verdicts, sibling(s), 160/* items beyond title, 210/400 beyond first line, the
commit's message body (rule 2 / brief § Deferred reading).

#### Act 1

- 2026-11-22T22:22Z `uptime`: load 6.45 8.03 16.35 (falling). `date -u` = Sun Nov 22 22:22:45 UTC.
- `git status --short`: only ` D docs/reviews/…failed-state-cold.deferred.md` (the partition).
  HEAD = cc23d6e6 (claim commit).
- Read brief lines 1–237 whole. Read REVIEW.md 25–154 (rules 1–2), 302–607 (lenses, re-run,
  V1–V7, lifecycle, method-record ruling). datescan --help read for form.
- `git merge-base --is-ancestor 50547442 HEAD` exit 0: tree holds the delta.
- `git log --oneline 50547442..HEAD -- <4 delta paths>`: 7 commits (1568acce ccopen twin, 54f91ad3
  grep is own command, 8556061a ms age / 3m test, e4d572d1 list asks etc, 20fd0f09 block close while
  launched still runs, b68cf410 retire one-file index, 74a0ceaf child pin/floor). Each to be read
  body-free only as far as it bears on the failed state.
- coldsweep --commit 50547442 with the 5 --path flags: subject+stat+diff printed, body not; 2 board
  files left out (ROADMAP.md, 210/400). Delta: judgeAgent gains a `failed` branch between the
  STOP_STATUS branch and `hasResult`; `zero` gains failed:0; status fails on counts.failed; summary
  and identifiers lines gain `· F failed`; design table gains the ❌ failed row and the ❌ line/count
  text; man page gains the fail paragraph and "same six counts"; CHANGELOG entry at 529–545 (two
  bullets: the state, and cctranscript left alone); tests: new check-12 test with 3 agents and a
  judgeAgent unit test, plus `failed: 0` added to 7 existing deepEquals.
- `git merge-base --is-ancestor 1bc89816 50547442` exit 0: the running state landed BEFORE the
  delta (02:00 vs 02:59 NZDT 2026-11-10). Pre-delta states: reported, stopped, unconsumed, running,
  cut = 5; `failed` is the SIXTH. CHANGELOG.md:530 says "a fifth agent state"; man page :772 says
  "the same six counts, failed included". Candidate finding (V5 contradiction, minor).
- Read ccclose at HEAD: 212–248 (NOTE_BLOCK, notificationText, taskNotifications: three carriers;
  user text must open with the tag), 780–839 (transcript reader: `t.notes.set(id,{status,ts})` on
  any line containing the tag, latest wins; toolResults keyed by tool_use_id), 1336–1463 (SHORT,
  STOP_STATUS, FRESH_MS, readAgent, runningVerdict, judgeAgent, checkSubagents), 1655–1684 and
  1935–1969 (check 15: TERMINAL includes failed; judgeLaunched reads t.notes by task id).
- Read design note 205–264; man page 226–295. Vocabulary sweep via coldsweep (brief's exact line;
  it warned the sibling path matches no file, as expected since it is removed) filtered to
  instruments/CHANGELOG/ROADMAP: hits listed above.
- Candidate (V3/V5): ccclose.design.md:154 (check table row 12, "fails when" column) still reads
  "no finished final turn and no completed, killed or stopped notification": `failed` not added.
  ccclose.design.md:237 (❌ cut row) still "no completed, killed or stopped notification" while the
  man page :264 was updated to "completed, killed, stopped or failed". Also CHANGELOG :539–545
  (cctranscript left alone) — grounds to check against cctranscript.
- Candidate (V4): the census sentence "3,587 agents … 50 … none ending on end_turn" is stated in
  four places in the delta (ccclose:1396–1398 comment, design :235, man :260–261, CHANGELOG
  :532–533)
  and a fifth board home exists (docs/roadmap/210-instruments-open-features/070-…:48 "50 of …", seen
  only as a sweep hit line, not opened). No stamped copy; brief lens 3 asks for one home.
- `mandoc -T lint -W style instruments/man/ccclose.1`: no output, exit 0.
- `nice -n 10 node --test instruments/ccclose.test.js` from the worktree root: tests 153, pass 153,
  fail 0, exit 0, duration 424,683 ms. Output in scratchpad test-run.txt (deleted at the end).
- Read test fixtures ccclose.test.js 88–176 (transcript(), json(), finishedTurns/cutTurns, agent(),
  noteText + the three carriers viaAttachment/viaQueue/viaUser, toolResult, agentLines) and 1–22
  (SCRIPT = __dirname/ccclose; `cc = require('./ccclose')`). Fixture notes carry a fixed timestamp
  at(-20); agents' records at -50…-47: every fixture has the agent's last record BEFORE the note.
- ccclose exports (line 3063–3065) include taskNotifications, readTranscript, judgeAgent: the census
  reuses the tool's own parser rather than a re-implementation.
- CENSUS (read-only; scratch scripts census.js, census2.js; counts only; store = the local
  ~/.claude/projects transcript store). Corpus now: 3,915 agent-*.jsonl files (delta said 3,587: the
  store has grown), 1,614 parent transcripts. `grep -l -F '<status>failed</status>'` → 163 parents,
  1,045 lines. Via readTranscript + taskNotifications over those 163:
  · task ids whose LATEST notification is failed: 365; of these 50 have an agent-<id>.jsonl and 315
    do not (background commands etc.). Agent ids are all hex; non-agent ids are other tokens (1
    hex).
  · the 50 failed agents: stop_reason end_turn 0; stop_sequence 45, tool_use 3, null 1, refusal 1.
    judgeAgent at HEAD → failed for all 50. Foreground among them: 1, and it HAS a tool_result on
    its
    launch (the ordering claim's case: n=1, confirmed). → "3,587 / 50 / none end_turn" REPRODUCES
    (50 and 0 exactly; the agent total has moved to 3,915).
  · ids that carried failed on some line but whose latest is NOT failed: 48, all superseded by
    `completed`, all 48 agents (0 non-agents). 48/48 have transcript records AFTER the failed note
    (max gap 509 min); 48/48 got a completed AFTER the failed; 47/48 end on end_turn.
    → resume-after-failed is the normal recovery path in this store (48 of 98 agents that ever
    failed), and 47 agents with a failed notification ended on end_turn.
  · of the 50 latest-failed agents, 2 have records after the note (both within 60 s: tail records).
  · failed-note carriers: queue-operation 414, attachment 138, user 105 (all three shapes occur).
- PROBE FA1 (probe-fa1.js on the exported judgeAgent): A failed@-60min + agent wrote 5 s ago →
  `failed`; B same with completed → `running`. C failed@-3h + agent last wrote -1h → `failed`; D
  same
  with completed → `cut`. E failed + end_turn + foreground tool_result → end text "failed (the
  parent
  recorded a failed notification)", no mention of the contrary evidence.
- CHANGELOG grounds for leaving cctranscript alone checked against instruments/cctranscript 53–60,
  489–510, 574–620 (notification = harness turn; no status count; three carriers) and the census
  (315 non-agent failed ids vs 50 agents): grounds hold.
- /security-review NOT RUN: it scans the session's pending diff; this tree's only pending change is
  the deletion of the sibling (` D …deferred.md`), whose removed lines ARE the deferred content, so
  running it would feed the sibling to the reviewer (REVIEW.md lens 4, SL2 class). Discharged by
  grounds; code-altitude read done by hand (parser 230–248, reader 812–833, judgeAgent).
- LIVE PROOF: `CCCLOSE_GH=/usr/bin/false node <worktree>/instruments/ccclose --session <parent
  .jsonl path> --root <scratch git repo> --json` on the oldest session holding a failed agent
  (parent last modified 139 days ago, so not live; root = an empty scratch repo so check 14 fetches
  nothing). Exit 1, stderr empty. subagents: status fail; counts {agents 1, reported 0, stopped 0,
  unconsumed 0, running 0, cut 0, failed 1}; summary "1 agent(s) · 0 reported · 0 stopped on purpose
  · 0 finished, result never consumed · 0 still running · 0 cut mid-flight · 1 failed"; the agent:
  state failed, status fail, end "failed (the parent recorded a failed notification)", requestShape
  null (its meta has none). Descriptions not printed. Ages of the 50 candidates' parents: 21–139
  days.
- MUTATION (scratch copy of instruments/{ccclose,ccclose.test.js,cctranscript,cclive};
  `node --test --test-name-pattern failed`): baseline 5 pass, 1 fail (check 14, needs pins.py from
  the repo layout; unrelated). M1 failed branch moved after hasResult → +1 fail (check-12 failed
  test). M2 `|| counts.failed` removed from status → +1 fail. M3 failed only when !finished → +1
  fail (judgeAgent unit test). M4 failed only when nothing follows the note (resume-aware) → no
  change; pattern "check 12" 7/7 pass. So the ordering, the fold and the override are pinned; the
  resume-after-failed case is pinned in neither direction.
- Captures deleted from scratch after logging: failed-parents.txt, census-candidates.json,
  live-pick.txt, live-out.json, live-err.txt, test-run.txt. Scripts (census.js, census2.js,
  probe-fa1.js) and the mut/ copy kept until act 2 ends, then deleted.
- Mirror sweep for the state vocabulary ("cut mid-flight|stopped on purpose") over README.md,
  instruments/README.md, docs/method, docs/build, skills, CLAUDE.md: two hits, both about sessions
  (CONCURRENCY.md:268, CLAUDE.md:18), none states the agent states. Design :154 quoted verbatim.
- 2026-11-22T22:45Z act 1 appended to the brief below `---`; Status line updated to ACT 1 WRITTEN,
  FAIL (1 MAJOR FA1, 1 MODERATE FA2, 5 minor FA3–FA7, 2 notes FA8–FA9). Scratchpad also holds the
  orchestrator's own files (commit-claim.log, msg-claim.txt): not touched.
- Gates on the brief after the verdict: datescan clean exit 0 (460 lines read); wrapscan exit 0 but
  it scanned nothing (docs/reviews is in .wrapscanignore), so width was checked by hand in
  characters: three tables converted to bullet lists and five paragraphs rewrapped at 100 columns;
  0 lines over 100 after the divider; reviewscan clean exit 0; leakscan clean exit 0. Pre-existing
  brief-writer lines over 100 (3, 42, 77, 122, 139, 192, 202, 212) left as they are: not mine.
- Act-1 findings: FA1 MAJOR (no resume test on the failed branch; a resumed agent reads failed),
  FA2 MODERATE (census claim measured over the wrong population), FA3 minor (design :154 and :237
  not updated), FA4 minor (changelog "fifth" vs six), FA5 minor (census in four homes, unstamped),
  FA6 minor (failed line names no contrary evidence), FA7 minor (user-record carrier can forge a
  failed that nothing rebuts), FA8 note (why a failed agent blocks the close is unstated), FA9 note
  (check 15 reads failed as ended/pass, check 12 as fail; later commit, consistency question).
  Overall FAIL. Nothing applied; nothing committed; only the brief and this log written.
- ACT 1 SAVED. Sibling not opened. Waiting for the act-2 message with the sibling's path.

#### Act 2

- 2026-11-22 act 2 released by the orchestrator (act 1 committed as acd77c18, brief only). Opened:
  the held sibling (8 questions, 3 facts; its re-run results: 111 tests pass at 461fdf92, mandoc
  clean, census and live proof not run); the delta commit body (`git log -1 --format=%b 50547442`);
  the intent record 210/400 whole (DONE note of 2026-11-10); the neighbouring pass 0154 brief and
  sibling where they name this delta; older ccclose verdicts grepped for "failed" only.
- Sibling Q1 = FA1, Q2 = FA8, Q5 = FA3, Q6 = FA2/FA5 (independently formed in act 1). Q3, Q4, Q7,
  Q8 are new probes, run below with counts only.
- Q7 (census: `grep -o -h -E '<status>[^<]{1,30}</status>'` over all parents, raw lines):
  completed 34,966; failed 1,285; killed 359; stopped 80; running 26; `(\w+)` 14;
  `completed|killed|stopped` 12; "Warning " 2. census4.js over the 13 parents with a running line:
  running on a genuine carrier 0 → quoted text. No other failure spelling.
- Q8 (census3.js over the 163 failed parents): 9,981 carrier notifications; 0 multi-block records;
  55 ids with a status change; 0 where file order differs from timestamp order; 0 equal-timestamp
  conflicts; 0 notes without a timestamp.
- Q3 (census3/4): foreground agents in those parents 70–71 (census3 counted meta files, census4 by
  shape), 24 with a notification; 1 with an is_error launch result and no notification, transcript
  not end_turn; 25 with neither result nor note. judgeAgent probe (foreground, result present, no
  note, stop null, blocks tool_use) → reported/pass "…stops short of end_turn". `is_error` appears
  in
  ccclose only at 220, 725–750, 824, 1929–1951, 2264, 2652: never in judgeAgent. → FA10 MODERATE,
  formed at reconcile.
- Q4 fixture (scratch HOME-free: a synthetic parent + one agent, run via --session <path> --root
  <empty scratch repo>, CCCLOSE_GH=/usr/bin/false): failed notes for `bg-task-1` and
  `../../a1111111`, completed for a1111111 → status pass, counts failed 0, agent reported.
- Opened for reconcile: 0154 brief (Status BRIEF ONLY, no verdict; names this delta a non-goal at
  :116) and its sibling :53 (notes the ordering); 2026-10-18-0506 verdict :346, :433, :759 (an
  earlier census: 44 of 52 stop_sequence agents were notified failed) — read as grep lines only.
- 2026-11-22 Reconcile appended; Status → ACT 2 WRITTEN, FAIL (1 MAJOR, 2 MODERATE, 5 minor, 2
  notes). Sibling not folded, nothing deleted in the repo (orchestrator's job). Scratch cleared:
  census*.js, probe-fa1.js, mut/, fixture/, fxroot/. Orchestrator's own scratch files left alone.
- Final gates after the reconcile rewrap: datescan clean, leakscan clean, 0 lines over 100 after the
  divider; act-1 text unrevised (diff vs acd77c18 removes only the 4 Status lines). ACT 2 SAVED.
