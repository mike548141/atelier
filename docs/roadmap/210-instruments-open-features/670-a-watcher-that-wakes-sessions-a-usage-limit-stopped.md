- [ ] 🔧 **Make a watcher, run outside every Claude session, that finds the sessions a
      usage-limit stop left idle and, once the budget is back, tells each to resume its
      planned work.** A child built a working prototype in the estate root on 2026-11-27 (shed
      `fleet/limit-watch/`: `limit-watch.py` and its README; first installed as a LaunchAgent,
      tested, then unloaded on the principal's pick). Bring it home as an atelier instrument,
      generic and public, beside `ccfleet`; the prototype's private wording stays in the root.

      **His words, 2026-11-27 (a child queue run), verbatim:** *"can you set
      some kind of timer/watcher or something outside of the claude session that can check if
      the claude sessions have paused because they ran out of budget in about 3% remaining, and
      tell all the claude sessions what happended and to resume their work as planned"* ·
      *"But obviously the watcher cant be a claude session itself as they will all stop when we
      run out of budget"* · then, after it was built: *"Keep that code etc because we will have
      this situation again - but how about you push it to a suitable repo. I wonder if that is
      more the atelier repo than shed. And dont we already have code some what like this to
      resume sessions as a fable review drains the budget just before 12pm and then you pick up
      and finish the in-progress reviews after the budget resets at 12pm NZT"*.

      **What the prototype does (measured 2026-11-27).** Plain Python, first on a 10-minute launchd
      timer (now a sleeping loop), so it runs while every session is blocked. (1) A top-level transcript whose last
      message is the API error `rate_limit` is a stopped session (found 10 real stops from
      November, all headless passes). (2) None stopped: exit, nothing spent. (3) One tool-less
      Haiku `claude -p` probe, no transcript kept; refused means wait. (4) Budget back: one
      headless Haiku relay with only `ListAgents` and `SendMessage` messages each stopped
      session still live, by the messaging name the id hook printed in its transcript. Each
      stop is woken once (a state file). Proven: the probe from a shell and under launchd; the
      relay's delivery; an idle interactive session wakes on a message. Not proven: the probe's
      output while the budget is really spent.

      **What already exists, and the overlap.** `ccfleet` knows the reset (`reset_utc`; a
      drive or drain starts nothing once it is reached, exit 3) and `ccfleet resume` finishes a
      headless pass a limit cut off, but only when an operator runs it after the reset (the
      weekly drain's "resume on his word"). Nothing watches, and nothing reaches an
      interactive session. So the new piece is the watch and the wake; resuming a headless
      pass stays `ccfleet resume`'s, and stays on his word.

      🛑 **No startup, login, background or cron item — ever** (his words the same day,
      verbatim, after macOS reported the prototype's LaunchAgent as a new background item:
      *"I DO NOT WANT YOU DOING THINGS LIKE THAT you need a better way - for example you could
      use native sleep/wait commands in python, zsh, bash or whatever rather than messing up
      my macOS environment by installing geenric scripts as startup/login items"*). The
      prototype was unloaded and is now one ordinary process that sleeps between checks,
      started and stopped by hand. The instrument is built that way, and a guard that refuses
      a session installing a launchd, login or cron item is owed beside it, since a rule in
      memory has not held.

      💬 **His answer on the guard, 2026-11-27 (AskUserQuestion, a child queue run; an answer,
      not a ruling), verbatim:** *"queue it build later. But it seems very wasteful to run it
      before every command, how many other things are slowing down work by checking every
      command before we run it? / We need to think of a better guard than that because that is
      wasteful lazy design practices, for example perhaps it is a guard that runs at the end of
      the session (like the existing hooks or session close command) to check the session didnt
      do anything stupid (not allowed) like thiis."* And on the prototype: *"So I specified I
      wanted time based and you did event based"*. So the guard is queued, and its design
      starts from a close-time or end-of-session check (beside `ccclose`), not a hook on every
      command.

      🔎 **Measured for his question, 2026-11-27:** the two user-level `PreToolUse` guards on
      `Bash` took about 0.58 s (`modelguard`) and 0.90 s (`secretguard`) a call, timed over 5
      calls each with interpreter start included; the session that measured it made 218 `Bash`
      calls, so roughly 2 to 5 minutes of a 4-hour session, depending on whether the harness
      runs the two in parallel (not checked). A third such guard would add the same again.

      🔎 **And on resources, for his follow-up (verbatim: *"not just do they slow things down
      but do they waste resources like memory, CPU cycles etc"*), measured 2026-11-27** with
      `/usr/bin/time -l`, 3 runs each, one `Bash` payload: `modelguard` about 0.45 s CPU
      (user and system), 17 MB peak memory, 830M instructions a call; `secretguard` about
      0.5 s CPU, 16 MB, 810M; a bare `python3 -I -c pass` about 0.26 s CPU, 12 MB, 390M. So
      about half the CPU and two-thirds of the memory is interpreter start, paid on every
      command: the two guards cost about 1 s CPU and 33 MB transient per `Bash` call (one
      session's 218 calls, about 3.5 CPU-minutes, subagents' calls not counted), on a
      12-core, 16 GB machine.

      🔎 **On the prototype's trigger (stated so the record is exact, not to argue the
      point):** its plist carried `StartInterval 600` as well as `RunAtLoad`, and
      `launchctl print` showed 18 runs in its first three hours, so it was firing every 10
      minutes while he was logged in. What was wrong was the mechanism: a LaunchAgent is a
      login and background item macOS registers and warns about, which his rule forbids.

      **Owed.** Decide its home under the one-home, one-prefix rule (`450/*`): a `ccfleet`
      subcommand or its own `cc*` instrument; tests and a man page like the others; the
      relay's message wording generic and configurable; start and stop commands for the
      sleeping process; a cold review before it is used again.
