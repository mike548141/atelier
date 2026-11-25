---
name: repo
description: This repo against the house standard. Pass the action as the first argument. create: scaffold a new repo or standardise an existing one to the atelier repo standard, stamped with your identity from an instance profile ("create a repo", "start a project", "standardise this repo"). scan: run four of the floor's scanners (secret, leak, licence, link) by hand and report. hook: install atelier's fail-closed pre-commit scan hook. A bare /atelier:repo shows this menu and runs nothing.
argument-hint: "create | scan | hook"
allowed-tools: Read(/${CLAUDE_PLUGIN_ROOT}/**), Bash(python3 "${CLAUDE_PLUGIN_ROOT}/instruments/atelier-menu/menu.py" repo)
---

<!--
  A SUBJECT, NOT A COMMAND: every /atelier: command is subject, space,
  action, and a bare subject shows its menu (board 450/020; the principal,
  2026-11-24, verbatim: "So something like /atelier:review by itself would be
  a help screen, not run a command by default"). This file only routes: each
  action's text lives in its own file beside it, so a use loads only its own.
  tools/test_subject_skills.py keeps the table below, the action files and
  the description in step.

  THE GRANT (allowed-tools) is the narrowest that lets the router work, and
  the test pins it line for line. Reading the plugin's own files: an
  action's text is a read of a path outside the session's directory, which a
  session with no read grant of its own is refused (review 2026-11-24 RK1;
  the double slash makes the path absolute). The menu, by its exact command.
  Under session and work only, the read-only git commands that fetch the
  principal's committed prompt, and under session the close's read-only
  report. Nothing wider: a router's grant pre-approves its commands for
  every action under it while it is the active skill, so any python or any
  git here would let a run push or reset unasked (RK29). An action's own
  file carries no allowed-tools: it is read, not loaded as a skill, so the
  harness never applies one there.
-->

# /atelier:repo

The first word after `/atelier:repo` picks the action. The words after it are
that action's own arguments: where the action's file names its arguments
placeholder (a dollar sign, then ARGUMENTS), it means those words.

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
directory, and follow it as written. The plugin's root, filled in as this
file loaded, is:

`${CLAUDE_PLUGIN_ROOT}`

Where the action's file names the plugin-root placeholder (a dollar sign and
braces around CLAUDE_PLUGIN_ROOT), it means that path. This skill pre-approves
reading the plugin's own files, so the action's file and the doctrine it points
at load without a grant of your own.

**No action, or a first word not in the table:** show this subject's menu
and do nothing else, however clear the rest of the request looks (a dropped or
misread word must never start work, and that includes reads toward one). Then
say which words were typed, and that the first of them is not an action here
(a later word that names an action does not make it one: only the first word
picks). The menu is:

```
python3 "${CLAUDE_PLUGIN_ROOT}/instruments/atelier-menu/menu.py" repo
```

Show its output as it is, then stop.
