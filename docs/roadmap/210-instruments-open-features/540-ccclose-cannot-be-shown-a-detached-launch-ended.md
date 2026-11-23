- [x] **`ccclose` check 15 gives no way to show a detached launch ended,
      when its PID was never printed.** A hand-up from a private child,
      2026-11-23. A drain session started a detached driver
      (`python3 -c 'os.setsid(); os.execvp("nohup", …)' … &`) and three
      detached launchers the same way. All four finished: the driver's own
      log reads "driver down", each launcher wrote its exit code (0) to a
      file, and a later `ps -p <pid>` read every PID gone, with the PIDs
      found from `pgrep -fl` output earlier in the transcript. Check 15
      still prints both launch commands as ❌ "nothing shows it finished;
      stop it by its pid or show it ended", so the close reads "not ready"
      with nothing left running. The leg-3 rule ("its PID read gone, or its
      own result recorded") has no form the session can produce for a
      launch whose PID the launching command did not print, and the tool
      does not say what evidence it accepts.
      **Read in the code (2026-11-23):** `judgeLaunched` takes PIDs only
      from the launching command's own result, through `pidsOf`: an `$!`
      echo, `pid=N`, or a `[1] N` job line. The driver's launch result did
      print its PID, as `pgrep -fl` output (`71599 zsh drain-driver.sh`),
      which none of the three patterns matches; and no later tool result
      is consulted, so "show it ended" has no form after the fact.
      **Do:** say in the ❌ line and the man page what counts as "shown
      ended" for a detached launch; accept at least (a) a `ps -p`/`kill -0`
      read gone for a PID that appears in a later tool result whose command
      matches the launch, and (b) a stated result file the launch wrote
      (exit code or END line) read after it; or offer a flag that records
      the evidence. Keep it fail-closed: unmatched evidence still blocks.
      A launch form that prints its PID (`… & echo $!`) is the cheap
      prevention; the skill or doctrine that launches detached work could
      say so.
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
