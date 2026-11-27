- [ ] 🔧 **Make a watcher, run outside every Claude session, that finds the sessions a
      usage-limit stop left idle and, once the budget is back, tells each to resume its
      planned work.** A child built a working prototype in the estate root on 2026-11-27 (shed
      `fleet/limit-watch/`: `limit-watch.py`, its README and a LaunchAgent plist; installed,
      tested, then unloaded on the principal's pick). Bring it home as an atelier instrument,
      generic and public, beside `ccfleet`; the prototype's private wording stays in the root.

      **His words, 2026-11-27 (a child queue run, `epl-estate-17`), verbatim:** *"can you set
      some kind of timer/watcher or something outside of the claude session that can check if
      the claude sessions have paused because they ran out of budget in about 3% remaining, and
      tell all the claude sessions what happended and to resume their work as planned"* ·
      *"But obviously the watcher cant be a claude session itself as they will all stop when we
      run out of budget"* · then, after it was built: *"Keep that code etc because we will have
      this situation again - but how about you push it to a suitable repo. I wonder if that is
      more the atelier repo than shed. And dont we already have code some what like this to
      resume sessions as a fable review drains the budget just before 12pm and then you pick up
      and finish the in-progress reviews after the budget resets at 12pm NZT"*.

      **What the prototype does (measured 2026-11-27).** Plain Python on a 10-minute launchd
      timer, so it runs while every session is blocked. (1) A top-level transcript whose last
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

      **Owed.** Decide its home under the one-home, one-prefix rule (`450/*`): a `ccfleet`
      subcommand or its own `cc*` instrument; tests and a man page like the others; the
      relay's message wording generic and configurable; install and remove commands, because a
      LaunchAgent is a background job the principal approves case by case; a cold review
      before anything installs it again.
