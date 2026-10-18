# ccclose — a close-out checker a session runs before it declares the close

Status: **built** (2026-10-16; design pass the same day, committed on its own
first). Written before the build because the tool is first-of-kind: nothing in
`instruments/` or `tools/` has checked a whole session's close before. Three
changes landed with the build: §6 first named `encodePath` as reused, and the
build took `friendlyModel` and `humanDelta` instead; §4 gained the live
session's window running to now; and §8 gained `--no-optional-locks`. The last
two are marked where they sit.

## 1. What it is, in one line

A read-only CLI the session runs at close. It prints the standard outputs (the
session ID, its transcript, its time window) and checks, **from a fresh read of
the repo, the host and the transcript, never from the session's memory**,
whether the close left anything owing. It ends with a one-line verdict.

## 2. Why it exists

`RECORD.md` § *Finish the sequence, then declare the close* already says what a
close owes, and that "nothing is owed" is a claim that must carry its evidence.
`CONCURRENCY.md` says every branch ends put away and no phantom `[~]` claim is
left. What nobody had was something that *runs* that checklist. A session
narrated its compliance from memory. The memory is exactly what drifts in a
long session, so the check has to be a fresh read. Mike's acceptance shape
(2026-09-12), verbatim:

> *"maybe we make some code that every session uses when I ask it to close out
> the session. Giving me standard outputs like transcript ID etc. but also check
> for what I mean by leaving things clean and tidy e.g. worktrees closed up;
> branches and PR's merged; docs updated like session log, roadmap etc; no work
> arounds when issues come up like contention on commits;
> defects/learnings/evidence/assumptions recorded"*

He added that he often gives close-out checks in a turn or mid-turn prompt, and a
tool should be reading for them rather than relying on him to repeat them.

## 3. Home, language, name

**`instruments/ccclose`, Node, zero dependencies.** Not `tools/`. ADR 0006
draws the line: `tools/` *enforces* (Python checks that gate a commit, run in
place, wired into hooks and CI); `instruments/` serve the teammateship itself
and are user-invoked. ccclose is invoked by a session at a moment of its
choosing, never by a hook, and its central input is a Claude Code transcript.
That is an instrument by the ADR's purpose rule. Node also lets it reuse
`cctranscript`'s transcript classifiers directly (§6), not re-implement them.

The name stays `ccclose`. It fits the `cc*` family and it names the moment it
serves.

## 4. Session identity and the window

- **Which session.** `$CLAUDE_CODE_SESSION_ID` by default (the harness sets it
  in every session's shell). `--session <id|path>` chooses another, or points at
  a `.jsonl` file directly. The id resolves to
  `~/.claude/projects/*/<id>.jsonl`. Every project folder is looked in, because
  a session that moved into a worktree still logs under the folder it started
  in. With no id and no flag, the session is *unknown* and every check that
  needs it says so.
- **The window** is the first and last timestamp in the transcript. "This
  session's" commits, branches, worktrees, claims and PRs are the ones dated
  inside the window on this repo. **That is a heuristic, and the output says so
  every run**: two sessions working the same repo at the same time can each be
  credited with the other's work. One attribution is stronger: a `[~]` claim
  line that names the session's 8-character id prefix (the queue-run claim
  form) is this session's whatever its date.
- **A live session's window runs to now.** When the session checked is the one
  running ccclose (its id is `$CLAUDE_CODE_SESSION_ID`), the log's last line
  can predate a commit made just before the check, so the window's end is now.
  *(Added in the build: the throwaway-repo dogfood missed a branch committed
  after the fixture log's last line.)*
- **Times print in UTC**, labelled. The output is close-out evidence that gets
  pasted into records, and records are UTC at rest (`CONVENTIONS.md`).

## 5. The surface

```
ccclose [--session <id|path>] [--root <dir>] [--json]
ccclose -h | --help
```

Three selectors and nothing else. `--session` and `--root` name *what is
checked* (the house convention: a flag is named for what it selects, as
`--from-archive` is). `--root` defaults to the current directory and is resolved to
its git top level. No `--fix`: the tool is read-only by contract (§8), so it has
no operation a fixing flag could name.

## 6. Reuse of cctranscript

`cctranscript` exports its classifiers when required, with its CLI guarded by
`require.main === module`. ccclose takes five of them: `extractText` (a
message body as text, whatever its block shape), `classifyUserRecord` (whether a
`type:"user"` record is the principal's prompt or harness text),
`isHumanQueuedCommand` (which
mid-turn records are the principal's own typing: not every `queued_command` is),
`friendlyModel` (the models line) and `humanDelta` (the window's span), plus the
wrapper lists `stripElements` works from. It does **not** take `readTurns`, which reads the whole log
into memory. ccclose streams the log line by line instead, so a long session
costs one line of memory at a time. The prompt numbering matches
`cctranscript`'s refs exactly (turn `N`, mid-turn `N+K`), so a ref ccclose
prints opens the same exchange in `cctranscript`.

Whether a `type:"user"` record is the principal's is cctranscript's call, made
once in `classifyUserRecord`: a record marked `isMeta`, or text that is wholly a
harness wrapper (`<task-notification>`, `<local-command-stdout>`,
`<system-reminder>`, `<browser_instruction>` and kin), is harness text, and
cctranscript shows it with its own role. Harness text still takes an exchange
number there (the model answers it, and renumbering would move quoted refs), so
ccclose numbers it the same way and only declines to treat it as an ask. One
filter remains ccclose's own, for the asks list only: the slash-command wrappers
(`<command-name>` and kin) are stripped from a prompt's text, because they hold
none of the principal's sentences, though cctranscript still shows the record as theirs.

## 7. The checks

Fixed set, fixed order, every run. Each ends in one of four states:
✅ pass · ❌ fail · ⚠️ partial or unknown · ➖ not applicable (its input is
absent; the line says why). A check never reports a pass it could not read for,
and an absent input never crashes the run.

| # | Check | Reads | ❌ when | ➖ when |
|---|---|---|---|---|
| 1 | Worktrees put away | `git worktree list`, each admin dir's creation time | a linked worktree created inside the window still exists | not a git repo |
| 2 | Branches put away | local branches, tip commit time | a non-default branch whose tip is inside the window still exists (merged-but-not-deleted counts: CONCURRENCY § *Every branch ends put away*) | not a git repo |
| 3 | Commits pushed | commits in the window that no remote-tracking ref contains | any | no remote |
| 4 | PRs merged | `gh pr list --state open` | an open PR created in the window, or headed by one of this session's branches | no GitHub remote |
| 5 | Session record | commits in the window touching the session log and its detail store | no index line written in the window, or written but not committed | no session log in the repo |
| 6 | Board rebuilt | the board's own check (`board.py --check`) | the generated index is stale | no generated board |
| 7 | No live claim | `[~]` lines in the board's item files | a `[~]` naming this session's id prefix, or dated inside the window | no board |
| 8 | Floor at the pushed head | `gh run list --commit <full sha>` | a failed run, or a **cancelled** one (not a pass: RECORD § the floor at head) | nothing from the window reached the default branch; no workflows |
| 9 | Reviews queued | doctrine/tool paths changed in the window, and `⏳` lines added to the board in the window | never; a miss is ⚠️ | no board; no doctrine/tool paths in the repo |
| 10 | Workaround-shaped commands | the transcript's shell commands | never; any hit is ⚠️ | no transcript |
| 11 | Working tree clean | `git status` | never; dirty is ⚠️ | not a git repo |
| 12 | Subagents finished | the session's `subagents/` directory beside its transcript, and the parent transcript's `<task-notification>`s and `tool_result`s | an agent with no finished final turn and no completed, killed or stopped notification | no transcript; no `subagents/` directory |

Why three checks can never fail:

- **Reviews (9).** Whether work earns a review is a judgement (`REVIEW.md`
  § *calibrate to risk*): self-verifying work over reviewed machinery does not.
  A changed tool path with no `⏳` is a question the session must answer, not a
  defect the tool can prove.
- **Workarounds (10).** Mike named "no work arounds when issues come up like
  contention on commits". The tool lists the commands shaped like one
  (`--no-verify`, signing switched off, force pushes, `reset --hard`, bare
  `git stash`, `git add -A`, removing an `index.lock`, `gh pr merge --admin`,
  hooks redirected). Some are legitimate. It lists them; the session answers.
- **Working tree (11).** Uncommitted changes the session did not make are proof
  another session is live (`CONCURRENCY.md`), so a dirty tree cannot be
  attributed from here.

**Subagents finished (12), precisely.** *(Added 2026-10-18, board item
020/420.)* Closing a tab on "ready to close" kills a running agent silently, so
the declaration has to cover them. The agents sit beside the transcript, at
`<project>/<session-id>/subagents/agent-<id>.jsonl`, each with an
`agent-<id>.meta.json` (`description`, `toolUseId`, `requestShape` background
or foreground, `model`). The directory is derived from the transcript's own
path, so a fixture transcript carries its own agents and no test reads the real
store. Every agent in that directory belongs to the session; "launched in the
window" holds by construction, since the window is the transcript's own span.

An agent is **finished** when its last `assistant` record has
`stop_reason: "end_turn"` (the streamed partials before it carry `null`). A
`SendMessage` resume appends to the same file, so the last record is the final
turn. One whose last assistant record is a `tool_use` with no result after it
was **cut mid-flight**. The parent records an agent's end three ways, and the
tool reads all of them: a `<task-notification>` with the agent's `<task-id>` and
a `<status>` (`completed`, `killed` or `stopped`), carried in an `attachment`
record of type `queued_command`, in a `queue-operation` enqueue, or in a plain
`user` record. The same notification usually arrives in more than one shape;
the latest per agent governs. A text counts only when it opens with the tag, so
a record that merely quotes one is not a notification. A **foreground** agent's
end is instead the `tool_result` on its launch's `toolUseId`; for a background
agent that same `tool_result` is only "launched", and does not count.

| State | When |
|---|---|
| ✅ reported | finished, and a `completed` notification (or, foreground, the `tool_result`) |
| ✅ stopped on purpose | a `killed` or `stopped` notification, whatever the transcript says. Named, never hidden: an orchestrator that stops a duplicate is doing right. |
| ⚠️ unconsumed | finished by its own transcript, but the parent has no notification: the result was never read. Also a `completed` notification over a transcript that stops short of `end_turn`, and a status the tool does not know. |
| ❌ cut mid-flight | no finished final turn and no completed, killed or stopped notification. Also an agent resumed after its `completed` notification (records later than the notification) and cut again. |
| ➖ | no transcript, or no `subagents/` directory ("not applicable", never a pass) |

The check is ❌ when any agent is cut, else ⚠️ when any is unconsumed, else ✅.
Its line prints every count, zeros included (`N agent(s) · R reported · S
stopped on purpose · U finished, result never consumed · C cut mid-flight`),
then one line per agent (short id, description, end), problems first so the
cap never hides one. An empty directory is a known zero and passes. If the
transcript exists but cannot be read, the line is ⚠️ unknown, because no
notification can be matched. `--json` adds `counts` and the capped `agents`
list to this check. Like the rest it is read-only. The session running the
check is live, so its own still-running agents (a worker, a reviewer) show ❌
until they end: that is the intended answer to "ready to close?".

**Pass and fail on the floor (8), precisely.** The sha checked is the newest
commit from the window that the default branch's remote-tracking ref contains,
not the ref's head: a later push by another session evidences a different tree.
Per workflow, the latest run counts. Any `failure`, `timed_out`,
`startup_failure` or `cancelled` is ❌. A run still queued or in progress is ⚠️
("pending"), which is the honest form RECORD allows. No run at all is ⚠️. `gh`
missing or not authenticated is ⚠️ unknown, never a pass.

**Detected, not hard-coded.** Atelier's conventions are the first adapter, and
each is found by looking:

- the session log is `docs/SESSIONS.md` or `SESSIONS.md`, with a `sessions/`
  detail store beside it if one exists;
- a *generated* board is a `ROADMAP.md` carrying board.py's generated banner
  beside a `roadmap/` item store; a hand-kept `ROADMAP.md` has claims but
  nothing to rebuild;
- `board.py` is the repo's own `tools/board.py` if it has one, else the copy
  beside ccclose in atelier (children call atelier's tools, ADR 0008);
- the doctrine/tool paths are whichever of `docs/method/`, `docs/build/`,
  `docs/decisions/`, `tools/`, `instruments/`, `skills/`, `commands/` exist.

## 8. Read-only and network

ccclose never commits, pushes, fetches, removes a worktree or edits a file.
Every git call runs with `--no-optional-locks`, because a plain `git status`
refreshes the index under `index.lock`, and on a shared checkout that write can
collide with a peer's commit. *(Added in the build.)* It does not `git fetch`, so "pushed" means "contained in a remote-tracking ref as
of the last fetch", and the output says so. The only network is `gh`, only when
`gh` is on `PATH` and `gh auth status` succeeds; otherwise checks 4 and 8 are
⚠️ unknown. `board.py --check` is the one subprocess outside git and gh, and it
only reads.

## 9. Asked of this close — answer each

After the checks, the principal's prompts (turn and mid-turn, §6's rules) that
contain a close-out-shaped instruction are listed as short quotes, each with
its UTC time, its channel and its cctranscript ref, under the heading
**"Asked of this close — answer each"**. The tool lists; it does not judge
whether each was met. The session answers each in its close message.

The match is a **keyword heuristic**, stated in the output. A sentence is
listed when it has a strong close phrase ("close out", "ready to close",
"before you finish", "tidy up", "wrap up", "leave … clean"), or when it has
both a cue ("make sure", "remember to", "check that", "record", "update") and
an object ("session log", "roadmap", "board", "changelog", "worktree",
"branch", "PR", "push", "learnings", "defects", "evidence", "assumptions",
"decisions", "questions"). It errs towards listing. A missed ask is the costly
error, and a listed non-ask costs one line of answer.

## 10. Output

A header block of standard outputs, the twelve check lines, the asks, then one
verdict line, for example `❌ not ready to close: 2 fail · 1 unknown · 6 pass ·
2 not applicable · 3 asks to answer`. The field set is stable: every check
prints every run, zeros print, and a figure the tool could not read prints
`unknown`, never `0`. Listed items are capped (25 per check, 25 asks), with the
number not shown. `--json` carries the same content, uncapped counts beside the
capped lists. Exit `0` when no check fails, `1` when any fails, `2` on a usage
error.

## 11. Not mechanised, and said so

- **"defects/learnings/evidence/assumptions recorded".** Whether a session's
  findings reached the record is a reading of meaning. The tool proves a
  session record was written in the window (check 5). Whether it holds the
  learnings is for the asks list and the session's own answer.
- **Attribution under overlap** (§4). The window heuristic is the best a fresh
  read can do without a session id in every commit. It is printed, not hidden.

## 12. Testing

`instruments/ccclose.test.js`, node:test, zero dependencies. Every test builds
throwaway git repos and a fake `HOME` in a temporary directory, with synthetic
transcripts, and for check 12 a synthetic `subagents/` tree beside them. No test reads the real `~/.claude` or a real repo. `gh` is
replaced through `CCCLOSE_GH` (a path to a stub script), the same seam shape as
ccarchive's `CCARCHIVE_SIMULATE_DATALESS`. The usual drift guards apply:
`--help` fits a screen and points at the man page, and every flag it prints is
in the page.

## 13. Out of scope

- **The model router** from the same 2026-09-12 message stays idea-only. Mike
  said nothing to start it, and nothing here designs it.
- **Fixing anything.** A close-out tool that removed worktrees or reverted
  claims would act on the heuristic attribution of §4, which can be wrong. The
  remedy stays the session's.
- **Archive mode.** A session being closed is live, so its log is in the live
  store. `--session <path>` covers any other file.

## 14. Review posture

First-of-kind and doctrine-adjacent (it encodes RECORD's close declaration as
code), so a rule-4 cold review is owed on the build. The building session does
not spawn it. The orchestrating session queues the `⏳`.
