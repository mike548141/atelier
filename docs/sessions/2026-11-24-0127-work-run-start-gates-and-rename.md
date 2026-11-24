# 2026-11-24 01:27 UTC — A run's start gates, the parked mark, and `/atelier:work-run`

**Session:** `b95c0d98` (messaging name `atelier-69`), Claude Opus 5.5,
principal-opened in the VS Code extension. Orchestrator in worktree
`atelier-b95c-open-gates`; one Sonnet worker in `atelier-b95c-reads` for the
instrument reads, landed by cherry-pick. A peer session (`edf25bd3`, the
review-drain plan mode) was live in the primary checkout throughout.

## What was asked

His words, verbatim: *"Consider if this should be built into the standard
prompt in session-open-prompt or some other way."* The subject was the message
he had added mid-run to queue run 608d8123 the night before (skip work blocked
on him unless something changed; wait for a quiet machine, checking hourly),
plus asking only at a session's start or end and chipping at the backlog of
asks. Mid-turn, verbatim: *"It should also ask the questions from the current
session"*; *"Also I think we should rename the command from /atelier:queue-run
to /atelier:work-run or something else"*; *"We could also consider having
/atelier:work-plan in the same way a parallel session is working on
/atelier:review-plan vs /atelier:review-drain"*. All quoted in full on
`180/220`, `180/230`, `180/240`.

## What happened

- **Recommendation: both places**, by his 2026-11-22 `ccopen` ruling: intent
  in the prompt, measurement in code the prompt runs. His picks (answers):
  *"All four, as drafted (Recommended)"*, *"3 oldest per session
  (Recommended)"*, *"/atelier:work-run (Recommended)"*.
- **Prompt** (`session-open-prompt.md`): wait for a quiet machine (hourly,
  four hours, then one worker at a time), run-gating asks before the wait;
  skip what waits on him unless it changed; ask at the start or once the work
  is done; the close puts this session's questions, then the three oldest.
- **Doctrine**: `COMMUNICATION.md` § *When to ask* (parked questions are not
  re-asked; the backlog is chipped every session), `CONCURRENCY.md` (the
  quiet-machine start gate), the board legend's `💤 PARKED <date>` line.
- **Instruments** (worker): `ccopen` read 8 machine load (busy when the 5-
  and 15-minute averages are both at or over the core count,
  `CCOPEN_MAX_LOAD` overrides) and read 9 waiting on the principal (parked
  items changed since parking); `ccclose` check 16, the three oldest unparked
  asks, informational. ccopen 34 → 47 tests; ccclose 165.
- **Rename**: `skills/work-run/`, its test, and every live mention; records
  keep the old name. An alias was built, then removed before landing: a peer
  session (`edf25bd3`) had his pick for retired command names the same day,
  *"Nothing"* (`450/020`), so the old name simply stops existing.
- **Idea filed**: `/atelier:work-plan` (`180/240`), not built.
- **Cold pass queued**: `160/1780`, waits for his Fable approval.

## Misses, owned

- **The threshold I offered was wrong.** I said `ccfleet`'s gate (2 × cores);
  the 2026-11-23 load of 20–24 on 12 cores sat under it, yet was the case he
  wanted waited out. Built at the core count instead and told him.
- **The backlog figure I gave him was wrong.** I told him 212 asks were
  waiting; the true count is 107 (a regex over the index table counted twice).
  Corrected on `180/220` and to him.

## Left open

- A sweep marking answers he already gave as "not now" with `💤 PARKED`, so
  the read sees them (`180/220`, owed).
- `450/020` (subject, space, action) will move `work-run` to `work run`;
  its table was told.
- `160/1780` cold pass, waiting for Fable approval.

## After the first close

- **Re-check interval a variable** (his words on `180/220`): `ccopen` names
  the wait, `CCOPEN_RECHECK_MIN`, default 30 minutes; the prompt says "check
  again at the interval it gives". Quiet now needs both the 5- and 15-minute
  averages under the threshold, so a momentary dip still reads busy. ccopen
  48 tests. Same review, `160/1780`.
- He confirmed the parallel session's form change will make it `/atelier:work
  run` and `/atelier:work plan`; that is `450/020`'s build, not this session's.
- **The first oldest-asks round found stale asks.** Of the three oldest
  🎯 items, two were already settled (`020/020`: `harvestscan` got the
  delete-only scope and floor wiring on 2026-08-04; `020/140`: every part
  ruled, only building owed). Their marks came off with the evidence, so a
  close round must read each ask's own text before putting it. `020/040`
  is a live ask and was put to him.
- **He said to carry on in a fresh session** without waiting for
  `160/1780` (his words on `180/220`).
- **Miss, owned:** three item edits and a board rebuild were made in the
  shared primary checkout while the peer had staged work there; its staged
  index picked up my counts. Moved to a worktree, its staged index rebuilt
  from its own items (`--from-index`), and the peer told.
- 🛑 **The parked mark is withdrawn** on his answer, verbatim on `180/220`:
  *"I don't want you marking work as "parked" at all, you will infere it
  incorrectly as you have many timtes already in past sessions"*. No sweep;
  the legend and `COMMUNICATION.md` no longer describe it; the reads that
  parse it are owed a redesign without inference or removal (`180/220`).
  Work plan joins the parallel session's command build (`450/020`).
- **Miss, owned: an ask that was not a decision.** `020/040` (a third
  scanner verdict, "clean, N accepted") was put to him as yes/no; his own
  model of 2026-08-09 already settles it. He answered, verbatim, *"Your
  question does not follow doctrine rules for asking questions"*. Recorded
  on the item as work owed, 🎯 removed; the round's sorting duty is owed on
  `180/220`. No further ask was put.
- **Miss, owned, and the worse one:** I read his "I don't want you marking
  work as "parked" at all" as "no parked status", and removed it from the
  legend and doctrine. He corrected it, verbatim on `180/220`: the status
  stays, he parks work through a session, and what he refused was sessions
  inferring parks from his past "not now" answers. Restored the same hour,
  his words quoted; the reads stand as built.
- **One old question per session, from the repo in hand** (his words on
  `180/220`): prompt, doctrine and `ccclose` changed from three to one.
- **The command's name is `/atelier:work run`** (his words on `180/230`);
  `work-run` is the interim skill until `450/020`'s build.
- **Miss, owned: re-asked a question he had just answered elsewhere.** The
  one old question this session put (`160/010`, the transcript-search
  fixes) was answered minutes earlier in the parallel atelier session
  (`f055e6f2`, now `210/580`). He replied, verbatim: *"I'm pretty sure I
  just answered this in the parallel session"*. My close read was from
  before that commit; I did not fetch and check the board and the live
  peer immediately before asking, which `COMMUNICATION.md` § *Asking for a
  ruling* requires. Owed with the round's sorting duty on `180/220`: fetch
  and re-read the item, and check live peers, at the moment of asking.
