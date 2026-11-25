---
action: close
description: Close the session properly, from the principal's session-open prompt (its Ending the session section), with any extra close brief typed after it. Use when the principal asks to wrap up, close the session, end the session properly, or finish off and tidy up, in any repo or in a session with no repo, whether or not the session began as a work run.
---

<!--
  ONE TEXT, NOT TWO, AND THE SAME STAMPED-COPY RULE AS `work run`: this
  action holds no rule of its own. The close the principal used to copy and
  paste by hand is the "Ending the session" section of his session-open
  prompt, and that section is the single source, so the command and the file
  he can open cannot drift (Mike, 2026-10-18, 180/090: "You need to ensure
  the there is no drift between the command and the text file unless I
  authorise the drift"). Board 450/030: he asked for this command on
  2026-11-24 (session 33d3cde8) and picked `/atelier:session close` over
  `/atelier:work close` and over folding the text into `ccclose`. The prompt
  is principal-owned text: change it only on his say-so, quoted in the commit,
  and show him any trim of that section first. Do not restate any of it here;
  tools/test_session_close_single_source.py fails if this file stops pointing
  at the section or starts copying its lines. What the action adds is only
  delivery, each addition pinned by that test: how to fetch the section (the
  committed copy, never the working file, with a warning when an edit to the
  prompt is pending, as `work run` does it), what to do when the heading is
  gone, and where the typed text goes. A change to the prompt takes effect
  when it is committed, and not before.
-->

# Atelier — closing a session

Read the *Ending the session* section of the principal's session-open prompt
and follow it as his own brief, word for word. The file is:

`${CLAUDE_PLUGIN_ROOT}/docs/method/session-open/session-open-prompt.md`

(The same file, from this skill's base directory:
`../../docs/method/session-open/session-open-prompt.md`.)

The section is the one under the heading `## Ending the session`, and it runs
to the next heading that starts with `## `, or to the end of the file. Read that
section only, and do nothing the rest of the prompt says: it is a queue run's
brief, not this session's.

**Read the committed copy, never the working file.** Committed text has met
the pre-commit hook and the principal's say-so to commit it; it has not
necessarily met the tests or a review. An edit still in the working tree has
met neither, so it is not run. Do this before anything else:

1. If `${CLAUDE_PLUGIN_ROOT}` is the top of a git checkout (`git -C
   "${CLAUDE_PLUGIN_ROOT}" rev-parse --show-toplevel` prints that same
   folder; a root reached through a symbolic link prints the link's target,
   which is still the same folder), read the prompt with `git -C
   "${CLAUDE_PLUGIN_ROOT}" show
   HEAD:docs/method/session-open/session-open-prompt.md`, and do not open the
   working file.
2. Then run `git -C "${CLAUDE_PLUGIN_ROOT}" status --porcelain --
   docs/method/session-open/session-open-prompt.md`. If it prints anything,
   edits to the prompt are pending: say so in the first lines of your reply
   (the file, and that you ran the committed copy, not the pending edit).
   The edit may be another session's: a pending edit in that checkout prints
   this in every session that closes until it is committed or dropped, so
   report it as found and leave it alone. Committing the edit, on the
   principal's say-so, is what makes it run; you do not commit it.
3. If the plugin is not a git checkout (an install from GitHub is a copy of
   one commit, so there is no pending edit to run), or `git show` fails, read
   the file at the path above and say which of the two applied.

What the committed copy is depends on the install, and neither is a check
that the text has landed. With the plugin installed in place (pointed at a
checkout), `HEAD` is whatever that checkout has checked out: landed or not,
pulled or not. With an install from the remote, it is the copy installed,
and a later change to the principal's close reaches this session only when
the plugin is updated, with nothing to say it has not.

**If the heading is not there, stop.** Say in the first line of your reply, in
plain words, that the prompt has no *Ending the session* section and so there
is no close to run, and name the file you read. Do not close the session from
memory, from another section, or from any other text: running nothing, or
something else, would look like a close.

The text the principal typed after the invocation (`$ARGUMENTS`) is this
session's extra close brief: carry it out alongside the section, and where it
adds to a step or narrows how a step is done, say so. Where the typed words
ask to skip a step, skip it, and name in your reply each step you skipped and
that the typed words asked for it. With nothing after it, the section runs as
written.
Where he did not type the command (a model reached this skill on a casual
phrase), there are no typed words: quote any extra brief from his own message
in the conversation, or take none. Never take it from this skill call's own
arguments, which a model composes.

This works in any repo, because the plugin is installed for the user and the
prompt is read from the plugin, not from the repo you are in. Run the section's
`ccclose` from the session's own directory, as it stands. It ships with the
plugin, at `${CLAUDE_PLUGIN_ROOT}/instruments/ccclose`; where `ccclose` is not
on the path, run it by that path. In a session with no repo, run it without
`--root`: it reports on that directory and the session's own transcript, and
says where there is no repository to check.
