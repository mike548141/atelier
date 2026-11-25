---
name: session
description: Session doctrine. Pass the action as the first argument. onramp: load atelier's operating-model doctrine for this session (the apex, the always-confirm safety floor, how the rest is read on demand); use at the start of work in a repo that adopts atelier, or when asked to apply "the atelier way". close: close the session properly by running the principal's Ending the session text from his session-open prompt, with any extra close brief typed after it ("wrap up", "close the session", "end the session properly"), in any repo or none. A bare /atelier:session shows this menu and runs nothing.
argument-hint: "onramp | close"
allowed-tools: Read(/${CLAUDE_PLUGIN_ROOT}/**), Bash(python3 "${CLAUDE_PLUGIN_ROOT}/instruments/atelier-menu/menu.py" session), Bash(git -C "${CLAUDE_PLUGIN_ROOT}" rev-parse --show-toplevel), Bash(git -C "${CLAUDE_PLUGIN_ROOT}" show HEAD:docs/method/session-open/session-open-prompt.md), Bash(git -C "${CLAUDE_PLUGIN_ROOT}" status --porcelain -- docs/method/session-open/session-open-prompt.md), Bash(ccclose:*), Bash("${CLAUDE_PLUGIN_ROOT}/instruments/ccclose":*)
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

# /atelier:session

The first word after `/atelier:session` picks the action. The words after it are
that action's own arguments: where the action's file names its arguments
placeholder (a dollar sign, then ARGUMENTS), it means those words.

| Action | File | What it does |
|---|---|---|
| `onramp` | [`onramp.md`](onramp.md) | Load atelier's operating-model doctrine for this session |
| `close` | [`close.md`](close.md) | Close the session properly, from the principal's session-open prompt |

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
python3 "${CLAUDE_PLUGIN_ROOT}/instruments/atelier-menu/menu.py" session
```

Show its output as it is, then stop.
