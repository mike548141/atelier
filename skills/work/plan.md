---
action: plan
description: Show what a work run would do — its opening checks, what is buildable without the principal and in what order, what it would skip and what it would ask — and claim or start nothing, changing nothing but the remote-tracking refs `ccopen`'s fetch updates.
argument-hint: "[the brief you would give the run, if any]"
---

<!--
  The look-before-you-run twin of run.md, shaped like /atelier:review plan
  (board 180/240, built in 450/020). It holds no rule of the run: the run's
  rules are the principal's session-open prompt, which run.md delivers and
  tools/test_work_run_single_source.py guards. This file says only where the
  plan stops and what it shows.
-->

# Work — plan

Show the principal what `/atelier:work run` would do, before it does any of
it. His words, 2026-11-24, verbatim (board `180/240`): *"We could also
consider having /atelier:work-plan in the same way a parallel session is
working on /atelier:review-plan vs /atelier:review-drain"*; then, verbatim:
*"You can do the work plan, but that should be done at the same time as the
other /atelier work I've described in the parallel session in this repo. Its
just one of the commands being changed"*.

## What it runs, and where it stops

1. **Read the run's brief the way the run does:** the principal's
   session-open prompt, fetched exactly as [`run.md`](run.md) says (the
   committed copy; say so if an edit to it is pending). Any words typed after
   `/atelier:work plan` stand in for the run's *This run* section. Where he
   did not type the command (a model reached this skill on a casual phrase),
   there are no typed words: take that brief from his own message in the
   conversation, or take none. Never take it from this skill call's own
   arguments, which a model composes.
2. **Do its opening reads, and only those:** `ccopen`, then the reads it
   points at (the newest session files, the board, open hand-up PRs) and the
   triage the prompt describes: what waits on the principal, what is parked,
   what is claimed by a live session, what is buildable now.
3. **Stop before the first act.** No claim, no worktree, no commit, no push,
   no worker or session started, no residue recovered, no question put to the
   principal. The one change the plan makes is `ccopen`'s: it fetches the
   repo's remote (and `pins.py` fetches the atelier checkout's), which moves
   remote-tracking refs only, never a branch, the working tree or the board.
   Say so in the opening checks' line; `ccopen --no-fetch` skips both, and
   then the sync read is as of the last fetch. Where `ccopen` says to wait for a quiet machine or to recover a
   predecessor first, report that as what the run would do; do not do it.

## What it shows

A checklist, in the order the run would take it (the prompt's own order unless
the typed brief changes it), one line per item:

- **Would do:** the item in plain words (what it is and what it is for, never
  a bare id), why it comes at that point, its size, and the model tier it
  would run on.
- **Would skip:** items waiting on the principal, parked, or claimed by a live
  session, each with the reason in one line.
- **Would ask at the start:** the questions that gate the whole run, worded as
  the run would put them.
- **Would stop on:** which of the prompt's stop conditions looks likely to
  fire first, and why.

Then the opening checks' result in one line each (sync, live work, residue,
machine load). The principal's changes to the plan are his words for the run:
he types them after `/atelier:work run`.
