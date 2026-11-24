---
name: atelier
description: Show the menu of every /atelier: command. Use when the user types a bare /atelier or /atelier:, or asks what atelier commands there are.
allowed-tools: Bash(python3:*)
---

# The /atelier menu

Run this and show its output to the user as it is, with nothing added before
the table except one line naming what it is:

```
python3 ~/.claude/skills/atelier/menu.py
```

If the user named a command after `/atelier` (for example `/atelier work-run`),
show the menu, then tell them the exact command to type (`/atelier:work-run`).
Do not run that command for them: the menu only points.
