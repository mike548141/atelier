---
name: review
description: Cold reviews of work before it is trusted. Pass the action as the first argument. plan: find every owed review across the estate, briefed or not, rank it, route it to the cheapest budget that still matches a local pass, estimate the spend, and show it as a table, running nothing ("what would a drain do", "plan the reviews"). run: drain the briefed reviews on the review tier, several at once under a load gate, until an approved budget is used up, or resume passes a usage limit cut off ("drain the reviews", "use up the budget", "resume" after a reset). brief: write a peer-review brief and run an independent review when work earns one (a design others build to, a decision that forecloses alternatives, a diff that ships; "review this properly", "draft the brief"). A bare /atelier:review shows this menu and runs nothing.
argument-hint: "plan | run | brief"
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

# /atelier:review

The first word after `/atelier:review` picks the action. The words after it are
that action's own arguments: wherever the action's file says `$ARGUMENTS`, it
means those words.

| Action | File | What it does |
|---|---|---|
| `plan` | [`plan.md`](plan.md) | Find every owed review across the estate, briefed or not, rank it, route it to the cheapest budget that still matches a local pass, estimate the spend, and show it as a table |
| `run` | [`run.md`](run.md) | Run briefed cold review passes across an estate on the principal-named review tier, several at once under a load gate, back to back, until an approved budget is used up |
| `brief` | [`brief.md`](brief.md) | Write a peer-review brief and run an independent review of work before it is trusted |

**A known action:** read only that action's file, from this skill's base
directory, and follow it as written. Where it says `${CLAUDE_PLUGIN_ROOT}`,
use the plugin's root: the folder two levels above this skill's base directory.

**No action, or a word not in the table:** show this subject's menu and do
nothing else, however clear the rest of the request looks; a dropped or
misread word must never start work. The menu is:

```
python3 "<this skill's base directory>/../../instruments/atelier-menu/menu.py" review
```

Show its output as it is, then stop.
