- [x] 🔎 **Workers leave background wait loops that can never end, and `ccclose` does not
      🔒 Claimed by session a2097e54 (`atelier-b2`, Opus 5.5), principal-opened by
      `/atelier:work run`.
      (claimed 2026-11-27-1226, wt: atelier-qr-a209-waits)
      see a subagent's background shells** `[S][tool+doctrine]`. Handed to atelier
      2026-11-27 by a child queue run (class only), measured there the same day: its
      worker subagents left 21 background shells running, the oldest 5 h 10 min, until
      the principal saw them in the agent map. Two shapes:
      1. `until ! pgrep -f "<pattern>" …; do sleep 4; done`: `pgrep -f` matches the
         loop's own shell command line, which contains the pattern, so the loop never
         ends (16 of the 21, one started about every 2 minutes).
      2. `until grep -q "^done" <file>` (or `"^exit="`): waiting for a line the watched
         command never writes (5 of the 21).
      All were killed after the workers had finished. Earlier in that run, `ccclose`'s
      *Launched work finished* check reported 0 background commands not ended while some
      of these were running, so the close check does not count a subagent's background
      shells.
      **Owed, both halves:**
      1. The dispatch text (`CONCURRENCY.md` § *Orchestrated queue runs*, the worker
         bounds a run hands out) says: never poll with `pgrep -f` on a pattern the loop
         itself contains (bracket one character, `[m]ake`, or wait on the PID); never wait
         on a marker the watched command does not itself print; give every wait a
         timeout.
      2. `ccclose` counts background shells a subagent started, not only the main
         session's, and reports any still running.
      **Not fixed in passing:** filed under `CLAUDE.md`'s rule that a defect is reported
      first.
      **Done 2026-11-27** (session a2097e54, built by its Sonnet worker, branch
      `qr-a209-waits`): both halves.
      1. Doctrine: `CONCURRENCY.md` § *Orchestrated queue runs* gains *A wait the worker
         writes must be able to end* beside the long-check poll (three rules: no `pgrep -f`
         on a pattern the loop contains, no waiting on a line the command does not print,
         a timeout on every wait), grounded in the measurement above (class only); the
         dispatch skeleton `session-open/dispatch-brief.md` gains the bound and its
         grounding row. No heading renamed.
      2. Tool: `ccclose` check 15 leg 2 reads each `subagents/agent-<id>.jsonl` for
         `run_in_background` Bash calls and judges them by the same rule (`readSubagentShells`,
         `checkLaunched`). Grounded by a census of the stored logs: 140 subagent background
         launches, and once the agent's log and the parent's `<task-notification>`s are read
         together every one is ended or stopped, 21 of them only in the parent's log, so an
         end counts from either. They fold into the `background` count (no new field), print
         as `subagent <id8>: <command>`, and an unreadable agent log makes the line unknown.
         4 new tests (the loop that never ends blocks; ended in either log passes; unreadable
         log warns; `--identifiers` carries it); man page, design doc (§ check 15 leg 2) and
         CHANGELOG updated.
      **Gap, stated:** only the background leg is read from a subagent's log; a detached
      `&` or `nohup` a subagent ran is left to leg 1's process read (which cannot see Apple
      platform binaries). A shell still running reads "no terminal notification", which cannot
      tell a loop that never ends from a command legitimately still working.
      Commitment: a doctrine rule workers' dispatches carry, and a close check sessions trust
      to say nothing they launched is still running.
      Worst failure: the check reads a subagent's shell as ended, or reads nothing, and a
      session declares "ready to close" over a loop that runs for hours (the very failure
      measured), or a rule that steers workers to a wait form that still never ends.
      Why the floor misses it: it fails silent (a clean line reads the same as a blind spot),
      the tests use synthetic fixtures of a record shape the harness may change, and a
      still-running shell is indistinguishable from a legitimate one by the log alone.
      Cold pass owed (the orchestrator queues the pointer).
