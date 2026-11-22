- [ ] **Hand-up from a private child: once a launch is detached, nothing
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
