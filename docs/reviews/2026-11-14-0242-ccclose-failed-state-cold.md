# Cold pass — `ccclose` names a `failed` agent as its own state

**Board:** `docs/roadmap/160-doctrine-review-owed/1350-rule-4-cold-pass-queued-ccclose-failed-state.md`
**Status:** BRIEF ONLY, not run. Written 2026-11-14 UTC by session `6321275c`, a headless Opus 5.5
brief-writer. Queued, waiting on the principal's explicit approval of Fable work; this brief is not
that approval.

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
