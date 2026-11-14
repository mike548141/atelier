# Sibling to the ccclose-running-state cold pass — held under rule 1's split

Sibling of `docs/reviews/2026-11-14-0154-ccclose-running-state-cold.md`, held under
`docs/method/REVIEW.md` rule 1's split. **Open only after the phase-1 findings in the brief are
committed.** Written 2026-11-14 UTC by the brief-writer, session `947ac694` (Opus 5.5), named in the
brief's provenance; it forms no finding and assigns no severity. Fold this file in below the
reconcile and delete it at phase 2.

## Re-run results held back from the brief

Run once by the brief-writer, 2026-11-14 UTC, from the worktree root at `58f612b7`, Node v24.18.0,
machine load averages about 10 on 12 cores:

- `nice -n 10 node --test instruments/ccclose.test.js`: 111 tests, 111 pass, exit 0
  (ℹ duration_ms 152780.551952).
- `mandoc -T lint -W style instruments/man/ccclose.1`: no output, exit 0.
- The live proof: not run (the brief-writer had no subagent of its own to observe).

## Prior records on nearby surfaces (named by filename, not opened unless the brief says so, not exhaustive)

- `docs/reviews/2026-10-17-1010-ccclose-close-checker-cold.md`
- `docs/reviews/2026-10-18-0506-close-covers-subagents-cold.md`
- `docs/reviews/2026-10-18-0517-queue-run-carries-the-brief-cold.md` (QK12, the finding `210/380`
  answers)

## Seeded questions (the brief-writer's suspicions, a floor not a fence)

1. The bound is a per-gap percentile, but the risk is per agent. An agent that writes thousands of
   records meets many gaps; if 0.1% exceed 600 s, how likely is a long-lived working agent to hit
   one while a close check runs and be called cut (dead)? Is the 99.9% figure the right statistic
   for "a working agent reads as running"?
2. "600 s is the longest a single foreground command may run": an agent can also wait on things
   that are not a foreground command (its own foreground subagent, a background command it waits
   for, a monitor, a scheduled wake-up, a permission prompt). Is a working agent silent past ten
   minutes in any of those, and called cut?
3. The parent-clock test (`parent.last - a.lastTs > FRESH_MS`): a busy live parent that keeps
   writing while its agent waits on one long command. At exactly what silence does a working agent
   flip to cut, and is the boundary pinned on both sides?
4. Is the census reproducible? Nothing in the delta names the script, the corpus or its date, and a
   reader cannot re-derive 83 s, 600 s or "130 completed for every 50 failed" (V1, V2).
5. `lastTs` is the newest timestamp of any record in the agent's file. Does the harness ever append
   a record to a dead agent's transcript (a queue or progress record, a resume stub), which would
   read a dead agent as fresh?
6. Clock: `now` is the checking machine's wall clock, the timestamps are the harness's. A check run
   on a transcript copied from another machine, or with clock skew, and the `Math.max(0, …)` that
   hides a future timestamp: does a negative age read as fresh?
7. Two states fail the same way, and the identifiers block is pasted into records. Does "still
   running" in a closed session's record say something false the moment the record is committed,
   and does the doctrine around close say what a session does on *running* versus *cut*?

## Facts held back from the brief

- Later commit `50547442` (`210/400`) places the `failed` check before the launch's `tool_result`
  and before the running test; its own pass is `160/1350`. `6890e9db` (`cclive`) touches the same
  file; pass `160/1290`.
- The intent record's DONE note states the bound and the census figures in the same
  words as the delta's comments, and adds a live proof: a real run on the author's own session
  "read its four live agents as running and its four finished ones as reported". That proof is
  recorded nowhere else the brief-writer found.
