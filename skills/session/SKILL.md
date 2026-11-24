---
name: session
description: Session doctrine. Pass the action as the first argument. onramp: load atelier's operating-model doctrine for this session (the apex, the always-confirm safety floor, how the rest is read on demand); use at the start of work in a repo that adopts atelier, or when asked to apply "the atelier way". A bare /atelier:session shows this menu and runs nothing.
argument-hint: "onramp"
allowed-tools: Bash(python3:*)
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

# /atelier:session

The first word after `/atelier:session` picks the action. The words after it are
that action's own arguments: wherever the action's file says `$ARGUMENTS`, it
means those words.

| Action | File | What it does |
|---|---|---|
| `onramp` | [`onramp.md`](onramp.md) | Load atelier's operating-model doctrine for this session |

**A known action:** read only that action's file, from this skill's base
directory, and follow it as written. Where it says `${CLAUDE_PLUGIN_ROOT}`,
use the plugin's root: the folder two levels above this skill's base directory.

**No action, or a word not in the table:** show this subject's menu and do
nothing else, however clear the rest of the request looks; a dropped or
misread word must never start work. The menu is:

```
python3 "<this skill's base directory>/../../instruments/atelier-menu/menu.py" session
```

Show its output as it is, then stop.
