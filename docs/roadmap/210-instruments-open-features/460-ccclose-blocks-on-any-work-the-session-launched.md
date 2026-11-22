- [~] 🔥 **`ccclose` must block a close while anything the session launched
      is still running, not only its subagents.** A hand-up from a private
      child, 2026-11-22. The principal's ruling, verbatim: *"Any work started
      by a session including sub agents, background tasks, sessions spawned or
      whatever must be checked for by ccclose and it must report that as a
      blocker to the session closing."* Check 12 sees only agents in the
      session's `subagents/` directory and their `<task-notification>`s. It
      does not see a background shell command (`run_in_background`) still
      running, nor a headless `claude -p` or loop started detached from a
      shell command (`nohup … &`, `setsid`, `disown`), which reparents to
      launchd and leaves no agent log. On 2026-11-21 a session declared itself
      ready to close while a detached headless run it had started was still
      working. `ccclose` had run in that session, and its check 12 counted
      only the session's own agents (all reported, 0 still running); the
      detached run is outside anything it reads. The principal had to stop
      the close himself.
      **Measured 2026-11-22 (macOS, Darwin 25.6, Claude Code 2.1.330):** the
      harness puts `CLAUDE_CODE_SESSION_ID` (and `CLAUDE_PID`) into the
      environment of every process a session's shell starts, and a detached
      child keeps it after reparenting. `ps -Eww -axo pid=,command=` shows it
      for the user's own binaries (a detached python.org Python showed it).
      Two limits, both measured: (1) Apple platform binaries (`/bin/sleep`,
      `/bin/sh`) show no environment to `ps -E`, so a bare `nohup sh -c …`
      is invisible to that read; (2) the harness's own MCP servers carry the
      same id, so they must be told apart (children of `CLAUDE_PID` started
      before the first prompt, or matched by command).
      **Shape (fail closed: what the tool cannot prove finished, it blocks
      on, and says why):**
      1. **Live processes:** every process carrying this session's id, other
         than the harness, its MCP servers and `ccclose`'s own chain, is a
         blocker, printed with PID, age and the first words of its command
         (argv cut, never printed whole: it can hold a secret).
      2. **Background shell commands:** every Bash call with
         `run_in_background` that has no terminal `<task-notification>` is a
         blocker, unless its process is provably gone.
      3. **Launch forms in the transcript:** a shell command that starts work
         and lets go of it (`&`, `nohup`, `setsid`, `disown`, `claude -p`,
         `screen`/`tmux` new sessions, `launchctl`, `crontab`, `at`), where
         neither (1) finds it nor the transcript shows it finished (its PID
         read gone, or its own result recorded), is a blocker named by its
         command. This is the leg that covers the platform-binary gap.
      4. **Harness tools that start work elsewhere:** `Workflow`,
         `CronCreate`, `ScheduleWakeup`, `RemoteTrigger`, `Monitor`, and
         messages that start a session in another project: listed, and a
         blocker unless finished, stopped or deliberately left scheduled
         (a schedule the principal asked for is reported, not blocked).
      Put it as its own check (or widen 12 and rename it "Launched work
      finished"), its own counts in `--json` and the identifiers block, the
      design doc's §7 table and §11, the man page, and tests with a fixture
      for each leg. Any doctrine sentence that says close waits for agents
      (`CONCURRENCY.md` § *Orchestrated queue runs*, `RECORD.md` close-out)
      widens to "anything the session launched".
      *(claimed 2026-11-22-0248 UTC, session 12a41aa2, wt: atelier-ccclose-460-480; the principal: "Build both now (Recommended)")*
