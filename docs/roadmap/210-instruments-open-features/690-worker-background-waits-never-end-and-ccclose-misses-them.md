- [ ] 🔎 **Workers leave background wait loops that can never end, and `ccclose` does not
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
