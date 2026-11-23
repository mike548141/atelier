- [x] **Hand-up from a private child: once a launch is detached, nothing
      the session does later clears `ccclose`'s ❌.** Seen 2026-11-22.
      A session ran `ccclose … &` and kept no pid. Hours later
      *Launched work finished* still failed with `detached launch: … — &:
      the command let go of it and nothing shows it finished; stop it by
      its pid or show it ended`. The session then ran
      `pgrep -fl 'ccclose --session'`, which matched nothing, and re-ran
      `ccclose`; the ❌ stayed.
  - Why it cannot clear: leg 3 accepts only `& wait`, a pid printed in
    the same command (`& echo $!`) and checked against the process
    table, or a later `launchctl unload`. A launch with no pid has no
    later proof that counts. The ❌ text says "show it ended", but there
    is no way to do that.
  - Cost: a session that did nothing wrong still cannot reach *ready*,
    and has to explain the ❌ away by hand. That trains sessions to stop
    trusting the check, the same cost as `210/510`.
  - Fix, one of:
    - With no pid, read the process table for the launch's own command
      line. If nothing matches, report *gone, by command line* (weaker
      than a pid, and say so) and do not fail.
    - Or accept a later command whose result shows the process is gone,
      such as a `pgrep -f '<launch command>'` that returned nothing.
    - Or, if neither is wanted, change the ❌ text to say what does
      count, so a session stops looking for a way to "show it ended".
  - Related: `210/510`. That launch was the child's own backgrounded
    `ccclose … &`, started to catch the stray `grep`.
  - Landed from hand-up PR #140 on 2026-11-23 by queue run c7a1e36e,
    renumbered from `210/540`, which a direct landing of a sibling
    hand-up on the same defect had taken first. Same defect class as
    `210/540`; kept as its own item because its evidence differs (a
    `pgrep` that matched nothing, not a PID found earlier).
      Fixed together with `210/540`; its case is form (b).
      ✅ **Done 2026-11-23** (queue run c7a1e36e; a Sonnet worker built it,
      the run read it before landing). Check 15 now accepts, only from calls
      made after the launch's result came back, and only as one simple
      command: (a) a `ps -p` or `kill -0` read of a pid gone, the pid taken
      from the launch's own result (now also `pgrep -l`/`-fl` lines) or from
      a later `pgrep`/`ps` line whose argv is the launch's own; (b) a later
      `pgrep -f` of a two-or-more-word plain substring of the launch command
      that found nothing, shown as "gone, by command line (weaker than a
      pid)"; (c) the launch's own redirect target read showing an exit or
      END line. (b) and (c) count only when the command let go of exactly
      one thing. A pid still in the table at close stays ❌. The ❌ text now
      names all three; the man page and design note say the same and give
      `… & echo $!` as the cheap prevention. Six tests, each with blocked
      fixtures. Covered by the `160/1710` cold pass, whose delta now
      includes this commit.
