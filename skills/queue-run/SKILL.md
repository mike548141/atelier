---
name: queue-run
description: Orchestrate a queue run — drain the shared roadmap queue as an orchestrator, executing items yourself or via worker sessions in worktrees, closing records per item so a session cap loses at most the item in flight. Use when the principal points a session at the queue ("progress any work you can", "drain the queue", "keep the plan busy"), or asks to run atelier's orchestrated-queue-run pattern, optionally with this run's brief after the invocation.
---

<!--
  ONE TEXT, NOT TWO. This skill runs the principal's session-open prompt and
  adds nothing of its own: the prompt file below is the single source, so the
  command and the copy he pastes by hand cannot drift (Mike, 2026-10-18,
  180/090: "You need to ensure the there is no drift between the command and
  the text file unless I authorise the drift"). The prompt is principal-owned
  text: change it only on his say-so, quoted in the commit. Do not restate any
  of it here; tools/test_queue_run_single_source.py fails if this file stops
  pointing at the prompt or starts copying its lines. The doctrine the prompt
  anchors to is docs/method/CONCURRENCY.md § Orchestrated queue runs and its
  siblings, bundled with this plugin.
-->

# Atelier — orchestrating a queue run

Read the principal's session-open prompt and follow it as his own brief, word
for word:

`${CLAUDE_PLUGIN_ROOT}/docs/method/session-open/session-open-prompt.md`

(The same file, from this skill's base directory:
`../../docs/method/session-open/session-open-prompt.md`.)

The text the principal typed after the invocation is that prompt's *This run*
section. With nothing after it, the run takes the prompt's default order.
