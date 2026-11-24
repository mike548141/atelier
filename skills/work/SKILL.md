---
name: work
description: Work sessions on the board's queue. Pass the action as the first argument. run: run a work session from the principal's session-open prompt, draining the shared roadmap queue as an orchestrator, with any brief typed after it ("progress any work you can", "drain the queue", "keep the plan busy"). plan: show what a work run would do (the opening checks, what is buildable and in what order, what it would ask) and claim or change nothing ("what would a run do", "plan the work"). A bare /atelier:work shows this menu and runs nothing.
argument-hint: "run | plan"
allowed-tools: Bash(python3:*), Bash(git:*)
---

<!--
  A SUBJECT, NOT A COMMAND: every /atelier: command is subject, space,
  action, and a bare subject shows its menu (board 450/020; the principal,
  2026-11-24, verbatim: "So something like /atelier:review by itself would be
  a help screen, not run a command by default"). This file only routes: each
  action's text lives in its own file beside it, so a use loads only its own.
  tools/test_subject_skills.py keeps the table below, the action files and
  the description in step.
-->

# /atelier:work

The first word after `/atelier:work` picks the action. The words after it are
that action's own arguments: wherever the action's file says `$ARGUMENTS`, it
means those words.

| Action | File | What it does |
|---|---|---|
| `run` | [`run.md`](run.md) | Run a work session |
| `plan` | [`plan.md`](plan.md) | Show what a work run would do |

**A known action:** read only that action's file, from this skill's base
directory, and follow it as written. Where it says `${CLAUDE_PLUGIN_ROOT}`,
use the plugin's root: the folder two levels above this skill's base directory.

**No action, or a word not in the table:** show this subject's menu and do
nothing else, however clear the rest of the request looks; a dropped or
misread word must never start work. The menu is:

```
python3 "<this skill's base directory>/../../instruments/atelier-menu/menu.py" work
```

Show its output as it is, then stop.
