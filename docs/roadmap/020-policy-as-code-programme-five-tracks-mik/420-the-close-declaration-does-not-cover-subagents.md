- [x] **BUILT 2026-10-18** (wt: atelier-qr-020-420)
      🔎 **The close declaration does not cover subagents: nothing checks that
      every agent a session launched has finished before "ready to close", and
      closing the tab kills a running agent silently** Filed 2026-10-16 (UTC)
      from a session with no repo, after the principal asked whether the
      sessions he had closed in the previous day had left agents mid-flight.
      He had been closing tabs on the agent's "ready to close" signal alone,
      trusting that it covered subagents. It did not, by construction: neither
      the doctrine nor `ccclose` reads them.
      **Evidence, from a fresh read of every session transcript touched in the
      24 hours to 2026-10-16 23:30 UTC (30 sessions, 21 closed, 240 subagents
      launched by the closed ones).** Every "ready to close" claim in a closed
      session (about 35) was made with no agent still working, so no harm this
      time. But 11 agents across four sessions were cut mid tool-call by the
      host crash of 2026-10-16 07:35 UTC, and the only reason their work was
      not lost is that each session happened to be *resumed*: on resume the
      harness posts *"N background agents didn't finish before the previous
      session ended"*, and the orchestrators then resumed them by message or
      rebuilt them. A tab that is closed and never reopened never shows that
      notice. The signal exists only after the fact, and only on a path the
      principal may never take. One more case: an orchestrator stopped a
      duplicate agent on purpose (`TaskStop`); the close message named it,
      which is the right shape, and shows the check needs "stopped on purpose"
      as a passing state.
      **What is owed — three things, one item because they share the gap:**
      1. **`ccclose` check 12, "Subagents finished".** Reads, for the session
         checked, `~/.claude/projects/<project>/<session-id>/subagents/`.
         Each agent has `agent-<id>.jsonl` and `agent-<id>.meta.json`
         (`description`, `toolUseId`, `requestShape` background|foreground,
         `model`). An agent is *finished* when its last `assistant` record has
         `stop_reason: "end_turn"`; one whose last assistant record is a
         `tool_use` with no result after it was cut mid-flight. The parent
         transcript records the agent's end as a `<task-notification>` with
         `<task-id>` and `<status>completed|killed|stopped</status>`, carried
         in an `attachment` record of type `queued_command`, a
         `queue-operation` enqueue, or a plain `user` record (all three shapes
         occur). A foreground agent's end is its `tool_result` on the launch's
         `toolUseId`. A `SendMessage` resume appends to the same agent file.
         Proposed states: ❌ an agent launched in the window with no finished
         final turn and no completed or killed notification · ⚠️ finished by
         its own transcript but no notification in the parent (the result was
         never consumed) · ✅ otherwise · ➖ no `subagents/` directory. Design
         note and man page updated with it; the fixture suite gains a
         synthetic `subagents/` tree. Read-only, like the rest.
      2. **`RECORD.md` § *Finish the sequence, then declare the close*.** The
         evidence list the all-clear carries (session entry, records, pushes,
         worktrees, PRs, review) gains the agents: every agent the session
         launched is named with its end (reported, or stopped on purpose),
         read from the agent list at that moment, never from memory. A
         declaration with an agent still running is not a declaration.
      3. **`CONCURRENCY.md` § the close-out measurement.** The list of what
         "nothing of mine is outstanding" is measured by (`git status`,
         `git worktree list`, a claim grep) gains the live agent list.
      **Why the tool and not the principal's memory:** this is the same class
      `020/180` was built for. The principal should never be the one who has to
      remember to open the agent list before closing a tab.
      **Not in scope:** making the harness refuse to close a tab with agents
      running; that is not ours to build. Doctrine for children follows by
      the usual propagation once atelier's text lands.

  **Closed 2026-10-18** by a Mike-opened Opus 5.5 queue run; all three parts.
  (1) `ccclose` check 12, *Subagents finished* (commit `a738f85`), built by a
  Sonnet worker to this item's spec and read by the orchestrator before the
  merge. It reads the three notification carriers and the foreground
  `tool_result`. A killed or stopped agent passes and is named. Problems are
  listed first, so the cap cannot hide one. Instruments suite 458/458 at the
  rebased head, man page lint-clean. Run live against the orchestrating
  session while its two workers ran, it reported both as ❌ cut mid-flight,
  which is the right answer for a live agent. One judgement noted: the
  `finished` field some real `.meta.json` files carry is ignored, because this
  item defines "finished" from the agent's own transcript. (2) `RECORD.md` and
  (3) `CONCURRENCY.md`, commit `089fcdc`. Cold pass queued at `160/920`.
  `ccclose` is still not on the machine's path; installing it there is the
  principal's.
