---
name: repo
description: This repo against the house standard. Pass the action as the first argument. create: scaffold a new repo or standardise an existing one to the atelier repo standard, stamped with your identity from an instance profile ("create a repo", "start a project", "standardise this repo"). scan: run four of the floor's scanners (secret, leak, licence, link) by hand and report. hook: install atelier's fail-closed pre-commit scan hook. A bare /atelier:repo shows this menu and runs nothing.
argument-hint: "create | scan | hook"
allowed-tools: Bash(python3:*), Bash(git:*), Bash(cp:*), Bash(chmod:*), Bash(cd:*)
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

# /atelier:repo

The first word after `/atelier:repo` picks the action. The words after it are
that action's own arguments: wherever the action's file says `$ARGUMENTS`, it
means those words.

| Action | File | What it does |
|---|---|---|
| `create` | [`create.md`](create.md) | Scaffold a new repo (or standardise an existing one) to your house conventions |
| `scan` | [`scan.md`](scan.md) | Run four of atelier's floor scanners (secret · leak · licence · link) by hand over this repo and report findings; the full floor is tools/floor.py. |
| `hook` | [`hook.md`](hook.md) | Install atelier's git pre-commit scan hook into this repository (secret · leak · link, fail-closed). |

**Check the first word before anything else.** It must be exactly one of the
words in the table's first column, nothing else counts: not a synonym (for
example `drain` for `run`), not a word later in the sentence, not your reading
of what was meant. Read no action file and run nothing until this check passes.

**A known action:** read only that action's file, from this skill's base
directory, and follow it as written. Where it says `${CLAUDE_PLUGIN_ROOT}`,
use the plugin's root: the folder two levels above this skill's base directory.

**No action, or a first word not in the table:** show this subject's menu
and do nothing else, however clear the rest of the request looks (a dropped or
misread word must never start work, and that includes reads toward one). Then
say which words were typed and that none of them is an action here. The menu
is:

```
python3 "<this skill's base directory>/../../instruments/atelier-menu/menu.py" repo
```

Show its output as it is, then stop.
