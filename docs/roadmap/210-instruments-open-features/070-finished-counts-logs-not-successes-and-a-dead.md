- [x] **`finished` counts logs, not successes — and a dead agent still leaves a
      log.** Measured on the session that shipped the feature: it started six
      subagents, **three of which died** on infrastructure faults (two watchdog
      stalls, one connection closed mid-response), and the header still read
      `6 agents started · 6 finished`. All six had written a `subagents/*.jsonl`;
      the three casualties are visible only as unusually short ones (4, 27 and 32
      lines against 73–173). So the started/finished gap catches a spawn that
      **never began** — skipped, refused, stopped before launch — and is blind to
      one that began and **fell over**, which in practice is the failure an
      orchestrator most wants to see. The man page's "one log per agent that
      actually ran" is *accurate* (an agent that crashed did run), so this is a
      gap in what the pair can tell you, not a defect in what it says.
      **Not yet a build item** — what a third figure would even key on is the
      open question. Candidates worth measuring before choosing: whether a
      terminated agent's log lacks a final assistant/result record that a
      completed one always has; whether length alone is too crude to be honest
      (it plainly is, on its own); and whether the `.meta.json` sidecar records
      an outcome. If none of those separates the cases cleanly, say so and leave
      the pair as it stands rather than shipping a third number that guesses —
      the same call the started-vs-finished split already made once.
      **One of the three candidates is now closed (measured 2026-07-28): the
      `.meta.json` sidecar records no outcome.** A census of all 425 live
      sidecars finds `agentType`, `description`, `toolUseId`, `spawnDepth`,
      `model`, `worktreePath`/`worktreeBranch` and `parentAgentId` — and **no
      key matching status / outcome / result / error / exit / completion at
      all**. The sidecar is written at *spawn* and describes the intent, not the
      ending. So the third figure, if it ever exists, must come from the agent
      log's own tail; the remaining candidate is the first one. Recorded here so
      the measurement isn't repeated.
      - **CLOSED, declined 2026-11-09** (queue run d0ca5d24). The remaining
        candidate, a terminated agent lacking a final `end_turn`, was measured
        on every agent log under the transcript store (counts only): 3,587
        agents. By last assistant `stop_reason` against what the parent
        recorded of the agent's end: `end_turn` 3,077 completed, 135
        foreground result, 121 no notice, 1 killed; no `end_turn` 253, which
        is 130 completed, 50 failed, 35 killed, 3 stopped, 26 no notice and 9
        foreground result. So a "no `end_turn`" figure catches all 50 agents
        the parent marked failed, and also 130 that completed (4.1% of the
        3,207 notified complete): about one flagged agent in four is a real
        failure, which is a figure that guesses. It separates no better on
        the final reason alone: `stop_sequence` ends 45 of the 50 failed and
        10 others. Length was already ruled out above, and the sidecar
        records no outcome. A third figure in `cctranscript` would also have
        to open every agent log, which `finishedAgents` deliberately never
        does (names only, so an evicted or archived store is not read). The
        pair stands as it is.
        **One finding from the same census, filed as `210/400`:** the
        parent's own `<task-notification>` carries a `failed` status (50 of
        3,587 agents), a clean signal this item never listed.
