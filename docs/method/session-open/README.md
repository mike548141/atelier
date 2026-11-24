# The session-open prompt and its history

The principal opens most working sessions with a prompt of his own: a standing
brief that points the session at the repo's doctrine and says how he wants it
to work, close and report. This directory keeps that prompt, and beside it the
house's own dispatch brief, the bounds an orchestrator opens each worker with.

- [`session-open-prompt.md`](session-open-prompt.md) is the prompt, and it is
  exactly what `/atelier:work-run <this run's brief>` runs: the skill loads
  this file and adds no rule of its own (only how to fetch it, the bundled
  path of the doctrine and where the typed text goes), so the command and the
  copy pasted by hand are one text (`180/090`;
  `tools/test_work_run_single_source.py` guards it). It is the principal's
  text: an agent changes it only on his say-so, quoted in the commit.
  **Its history is its git history, and nothing else.** There is no copy of
  an old version anywhere in the tree. Every version since the first opener
  of 2026-07-08 is a commit on this one path:

  ```
  git log --author-date-order -p -- docs/method/session-open/session-open-prompt.md
  ```

  Three lines of descent meet in it, each a real commit series with its
  author date set to when the text was first used:

  - **The mined template, versions 1 to 50** (2026-07-08 to 2026-10-17),
    subjects `session-open template: version N of 50`. Mined from the
    transcripts on 2026-10-18 (method below), first kept as a separate file,
    `template-history.md`, and folded onto this path on 2026-11-22, when that
    copy was retired. Each message counts the sessions its version opened.
  - **The hand reconstruction, V1 to V9** (2026-07-13 to 2026-09-16), folded
    in by subtree merge on 2026-09-16. Each is a whole prompt as pasted, not
    only its reused part, so it and the mined series differ in what they
    keep; neither is wrong.
  - **The live file**, every edit since 2026-09-16, made in this repo.

  Where the two reconstructions overlap in time, the log shows both. Each
  commit's diff is against its own parent, so each series reads cleanly on
  its own: add `--first-parent` for the live file alone.
- [`dispatch-brief.md`](dispatch-brief.md) is the **dispatch brief**: the
  fixed bounds an orchestrator copies into every worker's opening prompt
  (`180/120`). Unlike the prompt it is house text, not the
  principal's, and it holds no rule of its own: each line points at the
  `CONCURRENCY.md` rule that grounds it.

## What the command runs, and who can change it (`160/900`, QK1)

A plugin installed from a local clone loads the clone's files in place, so
the working file and the committed file can differ. The command runs only the
**committed** copy (`git show HEAD:` on the file) and says so in its opening
report when an edit to the file is pending in the working tree (Mike,
2026-11-08: *"Keep edit; read committed only"*). An edit takes effect when it
is committed, which is when the pre-commit hook, the tests and review can see
it.

This file is an instruction channel, so the threat is stated here:

- **Who can change what runs.** Anyone who can land a commit on `main` (the
  repo is public); and, on a machine with a local-path install, any process
  running as the user, which can edit the working file but cannot make the
  command run it unless it also commits.
- **What catches a hostile commit.** The pre-commit scanners (they judge
  shape, not intent), the four phrase pins in `tools/test_templates.py`
  (an edit that keeps those phrases passes), and a human reading the diff.
  `tools/quotescan.py` reads whether a commit to this file carries the
  principal's say-so (`160/900` QK1 counsel): a message with no quotation
  of two or more words is reported, warn-only until 2027-05-31 and blocking
  from that date. It reads the form of a quotation, never whose words they
  are.
- **What the command does not guard.** The committed copy is what was
  committed, not what was reviewed: a commit that never met review still runs.

## How the mined template series was built (2026-10-18, `180/060`)

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
verbatim. While the series sat in its own file, a spellscan exemption covered
it; the scanners read the tree, not history, so the exemption went with the
file on 2026-11-22.

## What the mined series does not show (cold pass, `160/940`)

A cold pass found no private detail and no single session's work in any of the
50 versions. It also found these limits in how the series describes itself.

- **The first four times have no seconds.** The retired copy committed
  versions 1 to 4 with a `+12:00` offset on a time that is UTC; the 2026-11-22
  replay onto this path carries the same digits as UTC, as each message
  always said, and says so in the message. The seconds were zeroed at mining
  and cannot be recovered.
- **The session counts do not quite reconcile.** The messages of versions 5 to
  50 count 226 family sessions (142 first runs and 84 re-pastes), and versions
  1 to 4 add 25 precursor sessions. The family figure above is 228, so two
  family sessions are in no commit. A likely reason is that they opened with
  the newest text, which is held back until it has opened two sessions. That
  is unconfirmed.
- **Version 31 is unconfirmed as a recurring unit.** One of its paragraphs is
  seen whole in one session on the live store. Its message credits the version
  with three sessions, but whether the paragraph itself came back has not been
  re-driven from the archive. The version stands as published history.
- **Removals leave no mark.** Of the nine units taken out, only the one
  replaced by `[estate-root repo]` shows. A bullet that ends at a colon with
  nothing after it, as in versions 17 and 18, is where a run's task list was.
- **A version can be a single use.** A version is an ordered assembly of units
  that each recurred, so a version can have opened one session: 17 of the 50
  messages report one session and no re-paste. The history cannot tell the
  sessions the principal opened from those a run opened, because the store
  lists sessions and not who typed the first prompt. Counts of re-pastes
  therefore mean "this text ran this often", not "he typed it this often".
