# 2026-11-26 23:57 UTC — work run: the bar gate, the dequeue round, two silent-count fixes

**Session:** `4ce066ba` (messaging name `atelier-c1`), Claude Opus 5.5, principal-opened by
`/atelier:work plan` then `/atelier:work run` with no brief, so the prompt's default order.
Orchestrator; four workers (one Opus, three Sonnet), each in its own worktree
`atelier-qr-4ce0-<slug>` or read-only. One other live session in this repo
(`4ccec293`, on the primary checkout); this run took worktrees and touched the primary
checkout only for claims and fast-forward pulls. No Fable model and no review-tier subagent ran.

## What was done

- **`460/040`, the dequeue round** (Opus worker, read-only; orchestrator spot-checked). Of 140
  open `160/` items, 45 are passes still owed (91 already ran and wait on rulings on their
  findings). 8 fail the bar, 6 fold into another pass, 2 cannot be told, 29 keep. Recorded on
  the item; nothing dequeued. The item stays claimed until his answer lands.
- **`460/070`** filed: the bar's text decides a least-privilege change both ways.
- **`460/030` step 1** (Sonnet worker): `pointerscan` checks a new pointer's intent record for
  three labelled answers (`Commitment:`, `Worst failure:`, `Why the floor misses it:`) or a
  `review: not warranted` line, and flags a second open pass on a subject with an unbriefed
  one. Reports only: left warn-only on purpose until its own pass runs. Its review folds into
  `160/1880` (widened). Still owed: the blocking wiring, and the ranking step in the repo that
  holds the real queue reader.
- **`115/420`** (Sonnet worker), closed: the floor's CI plane compares `CLAUDE.md`'s
  visibility line with `.atelier-floor.json`'s, soft. Probe over the local siblings: 11
  agree, 0 disagree; 20 declare no `visibility` in their config, so are not compared.
  `review: not warranted`, on the item.
- **`115/560`** (Sonnet worker), closed: reproduced, then git mode counts the untracked files
  its skip names drop; `conflictscan` gains the count. Review folds into `160/1860` (widened).
- Full suite before each landing: tools 3559, 3614 and 3631 tests, all OK;
  instruments node suite exit 0 each time.

## Found

- **The plan's triage was too shallow.** It named `320/010` and `320/450` as buildable from
  their index lines; read in full, every open part of each waits on the principal. The
  index's 🎯 marks only the state line; an item can carry its ask deep in the text.
- **This run's own brief to the dequeue worker was wrong**: it said a briefed pass is no
  dequeue candidate. A brief costs Opus and the pass Fable, and the item names briefed passes
  as first candidates. Corrected on the item.
- **A push ran mid-rebase**: `git rebase … | tail` hid the rebase's exit code from the `&&`
  chain, so the first of two rebased commits was pushed before the conflict on the index was
  resolved. Harmless here (that commit was complete and tested; the second followed minutes
  later), but the class is the known one: never pipe a command whose exit gates the next.

## Left open, for the principal

- The dequeue list (`460/040`): one question, put at the close.
- `160/1870` fails the re-check rule by name but carries his typed approval; only he can
  release it.

## Why it stopped

**Economics.** Four items landed; every other open item this run read in full waits on the
principal (an answer, a date, or evidence), and finding the next buildable one costs reading
many items each time. A fresh session with the `460/040` answer in hand does that cheaper.

## At the close: his answers

Put as one device call of three questions (answers, not rulings; verbatim on `460/040`):
the list, *"Drop 8, merge 6 (Recommended)"*; `160/1870`, typed, *"Release it as per your
recommended option - but to clarify we now have a better definition than just "are there any
major findings""*; four briefed design passes in a private child, typed, *"Run them at the next
drain (presumably Monday). Reviews of designs unblock the work to create and test the
feature"*. Applied by an Opus worker and landed: 8 closed as not warranted (three briefs and
1870's marked retired), 6 folded into their partners, 1870 released. The drain queue no longer
lists any of them. His correction of the re-check framing is `460/080`, for a fresh session.
`460/040` closed.

**Loose ends outside this repo, for the estate root's next session:** the drain config's
`extra` list still carries the entry for 1870's brief (harmless: the item is closed, so the
queue no longer lists it READY), and 1870's held-back sibling still sits in the user-local held
folder. Both can go; this session did not edit the estate root, where another session was live.

## Addendum 2026-11-28: resumed after a machine crash, and checked

The principal asked the session to resume after a crash and check its work. Nothing was in
flight: every commit of the session is on `origin/main`, the floor is green on a later head,
no worktree, branch, stash or claim of the session remains, and every item it closed or
dropped is still closed (`460/070` and `460/080` were since built by another session). The
drain queue lists none of the dropped passes. One correction to the loose ends above: the
released pass's held-back sibling stays as record, as for the other retired briefs; only the
drain config's `extra` entry is owed, now queued in the estate root's own board.
