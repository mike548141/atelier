# The session-open prompt and its history

The principal opens most working sessions with a prompt of his own: a standing
brief that points the session at the repo's doctrine and says how he wants it
to work, close and report. This directory keeps that prompt and the history
of how it changed.

- [`session-open-prompt.md`](session-open-prompt.md) is the **current** text,
  and it is exactly what `/atelier:queue-run <this run's brief>` runs: the
  skill loads this file and adds nothing, so the command and the copy pasted
  by hand are one text (`180/090`; `tools/test_queue_run_single_source.py`
  guards it). It is the principal's text: an agent changes it only on his
  say-so, quoted in the commit. Its own git history runs back to a first
  reconstruction made on 2026-09-16 (V1 to V9, folded in by subtree merge).
- [`template-history.md`](template-history.md) is the **template history**:
  one commit per version of the reusable part of the prompt, in the order the
  versions were first used. Read it with
  `git log --follow -p docs/method/session-open/template-history.md`. Each
  commit's author date is when that version was first used, and its message
  says how many sessions used it.

## How the template history was built (2026-10-18, `180/060`)

The principal's rule, in his words: *"All the parts of the session opening
prompt(s) that were re-used across more than one session transcript. By
definition if it were only used in one session then its not part of the
"template"."* And it must not include *"any private or personal information"*
or *"the specific work I asked of that session"*.

- **Sources.** Every Claude Code session transcript on the principal's
  machine and in its transcript archive: 946 sessions, 934 of which open with
  a typed prompt. The opening prompt is the first record the human typed;
  harness text is skipped.
- **The family.** Sessions whose opening prompt shares a paragraph or bullet,
  word for word after whitespace is normalised, with a known version of this
  prompt: 228 sessions, 2026-07-13 to 2026-10-17. Four shorter openers from
  2026-07-08 to 2026-07-10 share no wording with it but were each pasted into
  two to ten sessions to do the same job, so they lead the history as its
  precursors.
- **The rule.** A paragraph or bullet is template only if it appears in the
  opening prompt of at least two sessions. A session's version is its
  template units in order. Consecutive sessions with the same version count as
  one version. A later re-paste of an older version is not committed again,
  but each commit message counts how often its version came back.
- **What was taken out.** Nine units that recurred but named one session's
  work (a run's themed task list, a named feature) or private detail (private
  repo and tool names, device names, a personal credential store). One unit
  keeps its frame with the private repo's name replaced by
  `[estate-root repo]`. Every other word is as typed, typos included; lines
  are rewrapped to the house width, which changes nothing in how the text
  renders.
- **What the rule leaves out on purpose.** One-off wording, including small
  edits used once. The review-session openers (*"Please do any review
  work"* and its successors), which are a different prompt for a different
  job. And the newest text in `session-open-prompt.md`, until it has opened
  two sessions.
- **What could not be recovered.** The principal remembers starting around
  June 2026. The store holds only one June session, and its opening is not
  this prompt, so the history starts on 2026-07-08.

The mining was done by a worker agent and checked by the orchestrating session
before landing: the excluded units were read one by one, and every landed
version passed the leak, secret, date and spelling scanners, with one
exception: `catalog` in one version is the principal's own spelling, kept
verbatim under his 2026-07-23 ruling that historical text is not
retro-spelled.
