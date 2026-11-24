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
that action's own arguments: where the action's file names its arguments
placeholder (a dollar sign, then ARGUMENTS), it means those words.

| Action | File | What it does |
|---|---|---|
| `plan` | [`plan.md`](plan.md) | Show the review queue before anything runs |
| `run` | [`run.md`](run.md) | Drain the briefed cold reviews across an estate on the principal-named review tier |
| `brief` | [`brief.md`](brief.md) | Write a peer-review brief and run an independent review of work before it is trusted |

**Check the first word before anything else.** It must be exactly one of the
words in the table's first column, nothing else counts: not a synonym (for
example `drain` for `run`), not a word later in the sentence, not your reading
of what was meant. Read no action file and run nothing until this check passes.

**A known action:** read only that action's file, from this skill's base
directory, and follow it as written. Where it names the plugin-root
placeholder (a dollar sign and braces around CLAUDE_PLUGIN_ROOT), use the
plugin's root: the folder two levels above this skill's base directory.

**No action, or a first word not in the table:** show this subject's menu
and do nothing else, however clear the rest of the request looks (a dropped or
misread word must never start work, and that includes reads toward one). Then
say which words were typed and that none of them is an action here. The menu
is:

```
python3 "<this skill's base directory>/../../instruments/atelier-menu/menu.py" review
```

Show its output as it is, then stop.
