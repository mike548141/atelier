- [~] **ccarchive: bring back a schedule, as a real calendar schedule, not
      a run at every login** (claimed 2026-10-05-0150, wt: atelier-ccarchive-sched) (Mike, 2026-10-05, mid-run, after `210/190` removed
      the installer)

      His words: *"--install-schedule option should not be adding it to login
      items. As I said in the prior session that makes not sense as it is not a
      schedule, it is event based. We should fix that feature so it sets up an
      actual schedule - whatever is suitable on macOS for managing runnign
      scheduled software. I don't know if macOS has something better than cron
      perhaps?"*

      **What the removed installer did:** a launchd agent with `RunAtLoad` (run
      at every login) and `StartInterval` 86400 (every 24 h counted from load).
      The login run is the event-based part he objects to.

      **Researched at filing:** launchd is macOS's own scheduler and Apple's
      replacement for cron. A `StartCalendarInterval` agent runs at a clock time
      and, unlike cron, runs once on the next wake if the Mac slept through it.
      Cron on current macOS is unreliable and needs Full Disk Access. Any
      launchd agent, scheduled or not, is listed under System Settings → Login
      Items → *Allow in the Background*, the allowlist of background jobs, not
      *Open at Login*. So a calendar schedule still shows there, named after
      the program it starts.

      **Conflict to settle before building:** Mike's standing machine-local
      rule since 2026-10-03 is no launchd agent whose program is an interpreter
      running a script. ccarchive is `node` running a script, and `210/190`
      removed the installer on that rule.

      **Mike's ruling, verbatim (2026-10-05):** *"For my install we will keep it
      manual. For re-developing the code in ccarchive --install-schedule
      feature that should use launchd's calendar timer on macOS as you
      described. On ccarchive on Linux we should use whatever is suitable for
      Linux scheduling, again not sure if it has something better than cron"*.
      So: the conflict is settled by his own machine staying manual. The tool
      regains `--install-schedule` for other installs: launchd
      `StartCalendarInterval` on macOS, with no run at login, and the
      Linux-native equivalent on Linux, which is a systemd user timer with
      `OnCalendar` and `Persistent=true`. That catches up a missed run the way
      launchd does after sleep.
