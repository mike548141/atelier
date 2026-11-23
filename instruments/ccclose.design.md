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
  inside the window on this repo, a commit being dated by its committer date
(when the session made it; an author date set back by a history import plays no
part, `210/320`). **That is a heuristic, and the output says so
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
ccclose [--session <id|path>] [--root <dir>] [--json] [--identifiers]
ccclose -h | --help
```

Two selectors and two output forms: `--json` and `--identifiers` (§15). `--session`
and `--root` name *what is checked* (the house convention: a flag is named for what it selects, as
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
ccclose numbers it the same way and only declines to treat it as an ask. Two
filters remain ccclose's own, for the asks list only (`stripWrappers`):

- **The slash-command wrappers split.** `<command-name>` and `<command-message>`
  are stripped from a prompt's text, because they name the command and hold none
  of the principal's sentences. `<command-args>` is **unwrapped, not stripped**:
  it holds exactly what the principal typed after the command, so an ask typed
  as a command's argument is read. (Until 2026-11-09 all three were stripped on
  the ground that none held a sentence of the principal's; that was false for
  `<command-args>`, and an ask typed that way was dropped: 160/880, HC1.) A
  command with empty arguments is still wrapper-only, so it is no prompt.
  cctranscript shows such a record as `/name args`.
- **Every harness wrapper is stripped from a prompt's text, wherever it sits.**
  cctranscript keeps all but `<browser_instruction>` in a prompt's text, because
  a prompt that quotes a wrapper is the principal's own writing. So the two
  tools agree on whose a record is and on its exchange number, and **differ on
  its text** when a prompt quotes a wrapper (cctranscript shows the quote,
  ccclose does not read it as the principal's sentence), and the header's
  `N you` differs from ccclose's `N turn` by the commands with empty
  arguments. A census of the local store (2026-11-09) found no harness element
  injected onto a prompt other than `<browser_instruction>`, so cctranscript's
  narrower rule is the right one for the render (160/880, HC2, HC3).

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
| 5 | Session record | commits in the window touching the session folder (`docs/sessions/`); the retired one-file index still counts until 2026-12-04 | no session file written in the window, or written but not committed | no session log in the repo |
| 6 | Board rebuilt | the board's own check (`board.py --check`) | the generated index is stale | no generated board |
| 7 | No live claim | `[~]` lines in the board's item files | a `[~]` naming this session's id prefix, or dated inside the window | no board |
| 8 | Floor at the pushed head | `gh run list --commit <full sha>` | a failed run, or a **cancelled** one (not a pass: RECORD § the floor at head) | nothing from the window reached the default branch; no workflows |
| 9 | Reviews queued | doctrine/tool paths changed in the window, and `⏳` lines added to the board in the window | never; a miss is ⚠️ | no board; no doctrine/tool paths in the repo |
| 10 | Workaround-shaped commands | the transcript's shell commands | never; any hit is ⚠️ | no transcript |
| 11 | Working tree clean | `git status` | never; dirty is ⚠️ | not a git repo |
| 12 | Subagents finished | the session's `subagents/` directory beside its transcript, and the parent transcript's `<task-notification>`s and `tool_result`s | an agent with no finished final turn and no completed, killed or stopped notification | no transcript; no `subagents/` directory |
| 13 | Scratch folder empty | the scratch folder the transcript's environment attachment records | never; anything left is ⚠️ | no transcript; no environment record |
| 14 | Atelier pin and floor copy current | atelier's `tools/pins.py --json --child <repo>` (fetches origin in the atelier checkout) | the floor copy differs from the floor at the pin, the pin is behind **and** the floor has changed since it, or the pin is ahead, diverged or unknown (`020/470`) | not a child: atelier itself, or no pin or floor stamp in `CLAUDE.md` |
| 15 | Launched work finished | the process table (`ps -Eww`), and the transcript's Bash calls and harness-tool calls | a live process of the session, a background command no terminal notification ended, a detached launch nothing shows finished, or a harness-started item not ended; **fails closed** | no session id and no transcript |

Why four checks can never fail (check 15 can fail; its schedules and its
unreadable-table state only warn, as set out under it):

- **Reviews (9).** Whether work earns a review is a judgement (`REVIEW.md`
  § *calibrate to risk*): self-verifying work over reviewed machinery does not.
  A changed tool path with no `⏳` is a question the session must answer, not a
  defect the tool can prove.
- **Workarounds (10).** Mike named "no work arounds when issues come up like
  contention on commits". The tool lists the commands shaped like one
  (`--no-verify`, signing switched off, force pushes, `reset --hard`, bare
  `git stash`, `git add -A`, removing an `index.lock`, `gh pr merge --admin`,
  hooks redirected). Some are legitimate. It lists them; the session answers.
  One shape spans two calls: a **refused delete re-routed** *(added
  2026-11-03, board item 180/180)*. A session whose `rm` was refused by a deny
  rule then deleted the same files with a Python `shutil.rmtree`. A Bash
  call's delete routes are read from its command (`rm`, `rmdir`, `unlink`,
  `find -delete`, Python's `rmtree`, `os.remove`/`os.unlink`/`os.rmdir`, a
  pathlib `.unlink()`/`.rmdir()`, Node's `fs.rm`/`fs.unlink`/`fs.rmdir` and
  their `Sync` forms). When its `tool_result` is a refusal, its routes are
  marked refused. The refusal is read from the result's wording with
  `is_error` set: a deny rule ("Permission to use … has been denied"), the
  auto-mode classifier, the principal's rejection, a block for safety, or a
  compound command whose parts "require approval" (a census of the live store,
  2026-11-03). A later delete is listed when every route it uses is unrefused;
  one that also retries a refused route is a retry, since a rule narrowed on
  the principal's word lets the same command through. A call issued before the
  refusal's result landed is not read against it. On the grounding session
  the form lists the two Python deletes and not the later `rm`; across the
  store's 1119 transcripts, 73 hold a refused delete and 9 are listed. It
  misses a delete inside a script file, any other route, a subagent's own
  transcript, and refused effects other than deletes, and the flag never
  expires, since the transcript does not record a rule change.
- **Working tree (11).** Uncommitted changes the session did not make are proof
  another session is live (`CONCURRENCY.md`), so a dirty tree cannot be
  attributed from here.
- **Scratch folder (13).** *(Added 2026-11-03, board item 180/170.)* A close
  once declared "the scratch folder is clean" over about 98 files its agents
  had left. The folder is read from the transcript's `environment`
  attachment (`snapshot.scratchpadDirectory`, the latest governing), never
  derived: the harness allocates it, and a renamed project folder already
  breaks the derivation from the project path. Every entry is the session's
  own, since a queue run's workers write into the orchestrator's folder. It
  warns rather than fails because a file left there harms nothing and the
  remedy may be the principal's (a refused delete): the session clears it or
  names each as a loose end. The walk stops at 10000 entries, a bound on run
  time rather than a measured size, and then says "at least".

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
a `<status>` (`completed`, `killed`, `stopped` or `failed`), carried in an `attachment`
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
| ❌ failed | a `failed` notification, whatever the agent's own transcript or launch `tool_result` says: the parent's own word that it died. A census of 3,587 agents found 50 so recorded, none ending on `end_turn`. Its own count, never folded into cut or unknown (210/400). |
| ❌ still running | no finished final turn and no notification, but the agent's own transcript is still growing: its last record is at most 10 minutes old by the clock (`FRESH_MS`), and the parent has recorded nothing more than 10 minutes after it. Also an agent resumed after its `completed` notification that is growing again. |
| ❌ cut mid-flight | no finished final turn and no completed, killed or stopped notification. Also an agent resumed after its `completed` notification (records later than the notification) and cut again. |
| ➖ | no transcript, or no `subagents/` directory ("not applicable", never a pass) |

Ten minutes is a bound from a census of 3,587 real agent logs (881,904 gaps
between consecutive records): 99% of gaps are 83 s or less, 99.9% are 600 s or
less, and 600 s is the longest one foreground command may run. A dead agent
therefore reads as running for up to that long, and its line says how long
ago it last wrote. Running fails the check like cut, because a close under a
working agent is the hazard, but never calls a live agent dead (210/380).

The check is ❌ when any agent is cut, running or failed, else ⚠️ when any is unconsumed, else ✅.
Its line prints every count, zeros included (`N agent(s) · R reported · S
stopped on purpose · U finished, result never consumed · W still running ·
C cut mid-flight · F failed`),
then one line per agent (short id, description, end), problems first so the
cap never hides one. An empty directory is a known zero and passes. If the
transcript exists but cannot be read, the line is ⚠️ unknown, because no
notification can be matched. `--json` adds `counts` and the capped `agents`
list to this check. Like the rest it is read-only. The session running the
check is live, so its own still-running agents (a worker, a reviewer) show ❌
(running) until they end: that is the intended answer to "ready to close?".

**Launched work finished (15), precisely.** *(Added 2026-11-22, board item
210/460.)* The principal's ruling, verbatim: *"Any work started by a session
including sub agents, background tasks, sessions spawned or whatever must be
checked for by ccclose and it must report that as a blocker to the session
closing."* A session once declared itself ready to close while a detached
headless run it had started was still working; check 12 had counted only the
session's own agents, all reported. That run left no agent log: nothing in
check 12's reads could see it.

*New check, not a widening of 12.* The two read different things and fail
differently. Check 12 reads files beside the transcript and judges each agent
into six states (210/380, 210/400); this reads the host's process table and the
transcript's own commands, and its rule is "what cannot be proven finished
blocks". Folding it in would have changed 12's counts, which records already
quote, and its numbering; it is appended as check 15, so the numbers 13 and 14
(scratch, pin) that other documents cite stay put. The identifiers block's
Agents field gains a sub-line for it rather than a new field (§15), so the
seven-field set holds.

The measurement behind it (2026-11-22, macOS, Darwin 25.6, Claude Code 2.1.330):
the harness puts `CLAUDE_CODE_SESSION_ID` and `CLAUDE_PID` into the environment
of every process a session's shell starts, and a detached child keeps both
after it reparents to launchd. `ps -Eww` shows them for the user's own
binaries. Two limits, both measured: Apple platform binaries (`/bin/sleep`,
`/bin/sh`) show no environment to `ps -E`, so a bare `nohup sh -c …` is
invisible to leg 1; and the harness's own MCP servers carry the same id.

Four legs, each fail-closed:

1. **Live processes.** Every process whose environment carries this session's
   id, less the harness: the process whose pid is the `CLAUDE_PID` (read from
   the carrier's environment, and from `ccclose`'s own), a direct child of it
   that started before the session's first prompt (start = now − `etime`, ten
   seconds of slack for etime's whole seconds), or a direct child whose command
   names MCP (`mcp`, `modelcontextprotocol`, `mcp-server`); and `ccclose`'s own
   chain: its pid, its ancestors up the table, and its children (the `ps` that
   read the table), and the rest of its own command: everything under its
   parent shell, so the `grep` in `ccclose | grep` is not launched work
   (`210/510`), unless that parent is the harness. A `&` inside the same
   command is still read by leg 3. Each blocker prints its pid, its age and the first three
   words of its argv, the program as a basename and any `name=value` word as
   `name=…`. The argv is never printed whole: a command line can hold a secret.
   The id is read from `ps` for any session `--session` names, so a past
   session's orphans are found too.
2. **Background shell commands.** A Bash call with `run_in_background: true`.
   Its task id is in the launch's result (`toolUseResult.backgroundTaskId`, or
   "Command running in background with ID: …"). It is ended by a terminal
   `<task-notification>` for that id (`completed`, `killed`, `stopped`,
   `failed`: all four mean the work is over), a successful `TaskStop` or
   `KillShell` naming it, or a terminal status in its own result. A launch whose
   call errored started nothing and is not listed. No recorded result, or no
   task id in it, is a blocker: the end cannot be matched. *"Unless its process
   is provably gone"* is read as "provably ended by the transcript": the shell
   wrapper is an Apple binary, so the process table cannot prove a background
   command gone by environment, and no pid is recorded for it.
3. **Launch forms in the commands.** The command is read with its quoted text,
   comments and heredoc bodies blanked (a word in a string, a `grep` pattern or
   a comment is no launch), and `sh -c '…'` / `bash -c "…"` text is read too.
   The forms: a control-operator `&` (not `&&`, `>&`, `&>`, `|&`, or an
   unquoted URL's `&y=`), `nohup`, `setsid`, `disown`, `screen` and `tmux`
   starting a session or window, `launchctl load|bootstrap|kickstart|submit|
   start|enable`, `crontab` installing, and `at <time>`; `claude -p` is
   named when one of those detaches it, and is no launch in the foreground,
   where it ended with its own result (that is how its tool_result came back).
   A launch is **shown finished** when its own command also ran `wait`; when a
   later successful command undid it (`launchctl unload|remove|bootout`,
   `crontab -r`, `atrm`, `tmux kill-session`, `screen -X quit`); or when a pid
   it printed is gone from the table. A pid is read only where the command
   asked for one (`echo $!`) or the output labels it (`pid: N`, `[1] N`, or a
   `pgrep -l`/`-fl` line `PID argv` whose argv is the launch's own): a
   bare number is otherwise a count, and mistaking a count for a pid could read
   a live launch as gone. A pid still in the table is a blocker whatever its
   environment shows, which is how a platform binary's pid is caught. A launch
   one of leg 1's processes already accounts for (its program or script is a
   word of the command) is counted once, in leg 1. Anything else is a blocker
   named by its command, cut to 70 characters, with "the command let go of it
   and nothing shows it finished; stop it by its pid, or show it ended: a later
   ps -p/kill -0 read of its pid gone, a pgrep -f of its command line that
   found nothing, or its result file read showing an exit or END line".

   **Shown ended after the fact (210/540, 210/550).** A launch whose pid its
   command never printed used to have no way to clear: the ❌ said "show it
   ended" and no later act counted. Three forms now do, read from the
   transcript's own later calls. All are fail-closed: evidence that does not
   match is no evidence, and the ❌ stays.
   *Which calls count.* Only a call made after the launch's *result* came back
   (calls and results are numbered in the order the log holds them, so a read
   sent in the same message as the launch does not count), and only a read of
   one simple command: no `;`, `&&`, `||`, `|`, `$(`, backtick or redirect
   other than to `/dev/null`, so nothing else on the line can print the answer.
   The last 2000 such reads are held (`ps`, `kill`, `pgrep`, and `cat`, `tail`,
   `head`, `grep`, `sed`, `awk`, `less`, `more`, `bat`, `rg`).
   (a) *A pid read gone.* The pids are those in the launch's own result in any
   form above, or in a later `pgrep`/`ps` read whose `PID argv` line is the
   launch's own (every word of the argv that is not a shell or interpreter is a
   word of the launch command, and one of them is a name of 8+ characters).
   Each is gone when the process table, read now, lacks it, or a later `ps -p
   <pid>` printed nothing but a header, or `kill -0 <pid>` failed with "no such
   process" (not "not permitted"). All of a launch's pids must be shown gone;
   one still in the table is ❌ whatever an earlier read said.
   (b) *Gone, by command line.* A later `pgrep -f` (flags from `f l a i q`
   only, one pattern) that exited 1 and printed nothing, where the pattern is
   two or more words, 8+ characters, has no regex syntax, and is a plain
   substring of the launch command. It is ✅, worded "gone, by command line ...
   (weaker than a pid)": it shows no process matched, not which one the launch
   was. A pattern that is one word, or not in the command, or any `pgrep` that
   printed a match, is not accepted.
   (c) *Its result file.* A redirect target of the launch itself (`> f`, `>> f`,
   `2> f`, `&> f`, quoted or inside `sh -c`; never `/dev/null`) named by a later
   `cat`, `tail`, `head`, `grep`, `sed`, `awk`, `less`, `more`, `bat` or `rg`
   whose successful output has a line that is an exit code (`exit=0`, `exit
   code: 1`, `exited with code 0`, `rc=0`, `EXIT=3`) or `END`, `DONE`,
   `FINISHED` or `COMPLETED` alone. "Done with step 3" is a progress line, not
   an end.
   (b) and (c), and a pid found by a later read, are taken only for a launch
   that let go of one thing (one `&`, or one `nohup`/`setsid`): with two in the
   command, a pattern, a file or a later pid cannot say which one it shows.
   Not accepted, so a session does not hunt for them: a `ps -p` with `||
   echo gone` after it (the read must be bare); a file that was not the
   launch's own redirect target; `nohup sh -c '…'` (its inner redirects are not
   read); and the `driver down` kind of log line, which is prose. A stale
   result file from an earlier run reads as finished: write a fresh path per
   launch. **Cheap prevention:** a launch should print its pid, `… & echo $!`,
   which leg 3 reads at once and which needs none of the above.
4. **Harness tools that start work elsewhere.** `Workflow` and `Monitor` are
   judged like a background command (a task id, a terminal notification, a
   `TaskStop`; a Monitor also ends at its own time limit, `timeoutMs` past its
   call, when it is not persistent). `RemoteTrigger` is listed for every action
   but the read-only ones (`list`, `get`, `list_runs`); a `run` blocks, since
   its end is not in the transcript, and a create or update is a schedule. A
   **schedule** (`CronCreate`, `ScheduleWakeup`, a RemoteTrigger create) is
   ⚠️, never ❌: the item says a schedule the principal asked for is reported,
   not blocked, and *whether he asked for it is not in the transcript*, so
   ccclose cannot tell and treats every schedule as a question, "left on
   purpose?". A `CronDelete` of its id ends it; a wakeup whose `scheduledFor`
   has passed has fired. Tools whose names say they start a session or agent
   (`mcp__…session…` or `…agent…` with start, spawn, launch, create, new or
   run in the name) are listed and block like a background command. A census
   of 600 recent transcripts found none by that name; the list is a net and is
   the weakest leg.

States: ✅ every leg empty or every item ended, stopped, or never started;
⚠️ a schedule is pending, or the process table could not be read (leg 1 is then
unknown, and "no process" is never claimed), or there is no transcript (legs 2
to 4 unread); ❌ any blocker in any leg; ➖ no session id and no transcript. An
unreadable process table is ⚠️ and not ❌: a failed `ps` is not a finding that
something runs, and the four-state rule is that nothing unread passes; it
keeps the verdict out of "ready to close" either way. The line prints every
count, zeros included: `N live process(es) · B background command(s) not
ended · L detached launch(es) not shown finished · H harness-started item(s)
not ended · S schedule(s) pending · E ended or stopped · X harness/own
process(es) excluded`, then one line per item, problems first, under the
25-line cap. `--json` adds `counts` and `legs` (`processes`, `background`,
`launches`, `harness`, each the capped list). The process read is `ps -Eww
-axo pid=,ppid=,etime=,command=`, through `$CCCLOSE_PS` when it is set (a path
to a stub, the seam the tests use, mirroring `CCCLOSE_GH`); a run in which the
session's own harness is live does not flag the harness itself. Read-only, as
the rest.

**Pass and fail on the floor (8), precisely.** The sha checked is the newest
commit from the window that the default branch's remote-tracking ref contains,
not the ref's head: a later push by another session evidences a different tree.
Per workflow, the latest run counts. Any `failure`, `timed_out`,
`startup_failure` or `cancelled` is ❌. A run still queued or in progress is ⚠️
("pending"), which is the honest form RECORD allows. No run at all is ⚠️. `gh`
missing or not authenticated is ⚠️ unknown, never a pass.

**The pin check (14), precisely** (`020/470`; the principal: "build it into
ccclose as a post tidy up"). It runs atelier's own `pins.py` for the one repo
rather than comparing anything itself, so `pins.py` stays the one judge. It is
the exception to "read-only": `pins.py` fetches `origin` in the atelier checkout
(remote-tracking refs only), because a comparison against a stale ref would read
as current. Fail noisy on the safety rules, which are the floor and not the
pin: a drifted copy, or a pin behind while the floor text has changed since it
(`pins.py`'s `floor_moved`), is ❌ and exits 1. A pin merely behind, floor
unchanged, is ⚠️ with the commits listed: atelier moves dozens of commits a day,
and a peer moving on is a signal to read the delta and decide, not to bump by
reflex. Ahead, diverged and unknown pins stay ❌ (integrity). Any
failure to get an answer (no checkout, a failed fetch, a 20 s timeout, output
that does not parse) is ⚠️ "no result" with the reason, never "current". The
other attachment point he named, a `SessionStart` hook, is not built here: it
changes every session on his machine and is his call.

**Detected, not hard-coded.** Atelier's conventions are the first adapter, and
each is found by looking:

- the session log is the folder `docs/sessions/` or `sessions/`, one file
  per session (board `010/270` retired the one-file index on 2026-11-20; a
  repo that still keeps `docs/SESSIONS.md` or `SESSIONS.md` is named, and its
  commits count until 2026-12-04);
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

## 9. What the prompt asks in words: four listings

*(Rebuilt 2026-11-22, board item 210/480; the principal: "I want you to look at
everything in the lastest version of the prompt in session-open-prompt.md and
look at what would be more effectively built into ccclose rather than being in
the prompt".)* After the checks, four listings carry what the session-open
prompt used to ask the session to do from memory. Each is a **listing**: the
tool lists, the session answers. They are not check numbers (the fifteen stay
fixed). Only two things reach the verdict, and neither can be a mere listing:
a repo check that fails in another repo is ❌ like at home, and an unanswered
question, a live peer or a warning elsewhere is ⚠️.

### 9.1 Asked in this session — answer each: done / queued (item) / not done

Every principal prompt, turn and mid-turn (§6's rules: the same
`classifyUserRecord` and `isHumanQueuedCommand`, the same exchange numbers, so
each cctranscript ref opens the same exchange), with its UTC time, its channel,
its ref and a quote cut to 200 characters. Harness text, meta records and an
`AskUserQuestion` result are not prompts (the answer to his own question is not
a fresh ask). The session answers each: *done*, *queued* with its board item, or
*not done*.

A **`[close]`** tag marks each prompt the old close-keyword heuristic would have
listed, so that signal is not lost. A sentence is tagged when it has a strong
close phrase ("close out", "ready to close", "before you finish", "tidy up",
"wrap up", "leave … clean"), or both a cue ("make sure", "remember to", "check
that", "record", "update") and an object ("session log", "roadmap", "board",
"changelog", "worktree", "branch", "PR", "push", "learnings", "defects",
"evidence", "assumptions", "decisions", "questions"). It errs towards tagging. The
JSON `asked` field is that old list, unchanged; `askedAll` is the new one
(`total`, `closeShaped`, `items`).

The list is capped at 40 (a bound on the page, not on the count: the whole
count prints, and "cctranscript lists every one"). It is higher than the 25 of a
check's list because the point of the list is that none is missed. The
verdict's `asks` field keeps its meaning (the close-shaped count); the line
reads `N prompt(s) to answer (K close-shaped)`, and the JSON verdict gains
`prompts`.

### 9.2 Questions put to the principal

Every `AskUserQuestion` call in the transcript, one line per question: its
header and text (cut to 110) and its answer. The answer is the
`toolUseResult.answers` entry for that question (the text form,
`"question"="label"`, is the fallback). A question is **not answered** when its
result is an error (the call was interrupted because the session ended, or he
declined), when no result was recorded, or when a multi-question call has no
answer for it. ✅ answered (listed so the session acts on it), ⚠️ not answered,
with the reason: "open question: record it on the board". It is never ❌.

Beneath it, **call-out lines**: assistant text lines that carry 🎯 (a decision or
action that is his) or ⏳ (time-sensitive, waiting on him), cut to 200, each
distinct line once. These are the session's own side of the conversation, which
nothing read before; a call-out is "an open ask: answered or queued?", not a
warning on its own (every session has some). The JSON is `questions` (`total`,
`open`, `items`, `callouts`).

### 9.3 Other repos touched

The session-open prompt asks to deal with "everything you've touched"; the
identifiers block printed "fill in by hand". The repos are now read from the
transcript: each Bash record's `cwd`, each `cd <dir>` and `git -C <dir>` in a
command (a relative one against the cwd), the folder of a file the session
wrote or edited (Write, Edit, NotebookEdit), and the worktree paths it created
(the same list the identifiers block reads). Each directory goes to its nearest
**existing** ancestor, then to its git top level and common dir. A repo sharing
the checked repo's common dir is the home repo (its own worktrees included) and
is not "other". The scratch folder, a temp folder and `~/.claude` are never
counted. A directory that is in no repo any more (a put-away worktree of another
repo, a plain folder) is **unresolved**: counted, never guessed. Up to 12 repos
are read; the rest are counted as not read.

For each repo the checks that make sense are run, all local git reads, over the
**same window**: worktrees put away, branches put away, commits pushed, session
record, no live claim, working tree clean. Not PRs or the floor (network), not
the board rebuild or the pin (subprocesses, and the pin fetches). They run on the
repo's main checkout where it exists (a repo's branches, pushes and claims are
repo-wide), else the top level the session used. **One refinement:** the session
record is judged only in a repo where the session committed in the window. A repo
it only read owes no record, and a ❌ there would be a false one; it reads ➖
"no commit from the window in this repo". A failing check in another repo is ❌
like at home: it counts in the verdict's `fail` and the exit code is 1. The
attribution heuristic of §4 applies, and the output says so (the heuristic line).

Printed as a compact block per repo: the repo's status, its path, its window
commit count, one line of the six statuses, then the summary and up to three
items of each failing or warning check. The identifiers block's **Other repos**
field now carries the repo names with their commits and how many paths were
unresolved ("fill in by hand" stays for those), and a note that a private repo is
named generically in a public record (`RECORD.md` § *The record is public*):
the block is pasted into records, and ccclose cannot tell which repos are
private. `--json` keeps the `otherRepos` string of the identifiers form (now the
names) and adds `touched`; the default form's JSON gains `otherRepos`.

### 9.4 Other live sessions

The other live sessions in the same repos (the checked repo and those touched),
by cclive's own reads, required and not copied (`collectTranscripts`,
`tailInfo`): a transcript or an agent log written in the last 10 minutes
(check 12's bound, `FRESH_MS`) whose last recorded working directory sits in one
of those repos (same git common dir). The session checked, and the session
running ccclose, are not "other". It is ⚠️ with "answer: do they have what they
need from you?", each with its short id, repo, working directory, branch, how
long ago it wrote and its title, and **never ❌**; ➖ when there are none. cclive
is required at call time, not at load: cclive requires ccclose for `FRESH_MS`,
so a top-level require would be a cycle. `module.exports` is set before `main()`
runs for the same reason. A transcript folder that cannot be read is ⚠️
unknown, not "none". Limits are cclive's: a quiet transcript may be a slow
agent, a session open and waiting writes nothing, and another machine's
sessions are invisible.

### 9.5 The identifiers block in the default run

The default output ends with the `## Identifiers` block after the verdict, so the
close is one command (this was built earlier, board 210/300, and is kept);
`--identifiers` alone prints only the block; `--json` keeps the checks and the
listings above, and the block's own JSON is `--identifiers --json`.

## 10. Output

A header block of standard outputs, the fifteen check lines, the four listings
of §9 (every ask, the questions put to the principal, the other repos touched,
the other live sessions), then one verdict line, for example `❌ not ready to
close · 2 fail · 1 unknown or partial · 6 pass · 9 not applicable · 12
prompt(s) to answer (3 close-shaped) · 1 unanswered question(s) · 2 other live
session(s) · 3 other repo(s) touched`, then the identifiers block (§15). The
field set is stable: every check prints every run, zeros print, and a figure the
tool could not read prints `unknown`, never `0`. Listed items are capped (25 per
check, 40 prompts), with the number not shown. `--json` carries the same
content, uncapped counts beside the capped lists, and only ever gains fields:
the new counts are `verdict.prompts`, `openQuestions`, `liveSessions`,
`otherRepos`, `otherRepoFail` and `otherRepoWarn`, and the new top-level keys
`askedAll`, `questions`, `otherRepos` and `liveSessions`. The verdict's `fail`
now includes a failing check in another repo. Exit `0` when no check fails
(here or in another repo), `1` when any fails, `2` on a usage error.

## 11. Not mechanised, and said so

- **"defects/learnings/evidence/assumptions recorded".** Whether a session's
  findings reached the record is a reading of meaning. The tool proves a
  session record was written in the window (check 5). Whether it holds the
  learnings is for the asks list and the session's own answer.
- **Launched work it cannot see (check 15).** An Apple platform binary shows no
  environment to `ps -E`, so leg 1 cannot see a bare `nohup sh -c …`; leg 3
  covers it from the command, and a launch no pid, wait, undo or later read
  (pid gone, `pgrep -f` empty, result file with an exit line) shows finished
  is a blocker. A launch hidden inside a script file, a Python `Popen`, an
  `ssh`, or any form not in leg 3's list is missed, not guessed. A background
  command is proven ended only by the transcript (a notification, a stop, its
  own result), never by the process table. Whether a schedule was asked for is
  unknowable from the transcript, so each is ⚠️. A process that was reparented
  under another session's id is not this session's. A dead process whose pid
  was recycled reads as alive: it fails closed.
- **What the listings cannot judge (§9).** Whether each prompt was done, whether
  a question put to him is the one a board item names, whether a call-out is
  still open, and whether a live peer has what it needs: all are the session's
  answer, which is why they are listings. A prompt typed in a form the harness
  does not record as the principal's, or a question asked in prose rather than
  through the device, is not read. Other repos are read from directories the
  transcript names: a repo the session worked in through a script, an `ssh` or a
  path built by a command is missed, and a put-away worktree of another repo is
  counted unresolved, not placed. A repo touched only by a read can show a
  warning (an old dirty tree) the session did not make.
- **Attribution under overlap** (§4). The window heuristic is the best a fresh
  read can do without a session id in every commit. It is printed, not hidden.

## 12. Testing

`instruments/ccclose.test.js`, node:test, zero dependencies. Every test builds
throwaway git repos and a fake `HOME` in a temporary directory, with synthetic
transcripts, and for check 12 a synthetic `subagents/` tree beside them. No test reads the real `~/.claude` or a real repo. `gh` is
replaced through `CCCLOSE_GH` (a path to a stub script), the same seam shape as
ccarchive's `CCARCHIVE_SIMULATE_DATALESS`, and the process table through
`CCCLOSE_PS` (a stub that prints a fixture file; every `world()` installs an
empty one, so no test reads the real table). Check 15 has a fixture per leg.
Each §9 listing has its own: every ask (the close tag, the cap, results and harness text excluded), the questions (answered,
interrupted, declined, absent, multi-question, call-outs), other repos (a
failing one, a visited one, the home repo's worktrees and the scratch folder
excluded, the unresolved count), and live sessions (live, stale, elsewhere, none)
over a fake `HOME` whose `projects/` folder holds the peers' transcripts.
The usual drift guards apply:
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

## 15. The identifiers form

`ccclose --identifiers` prints the block `RECORD.md` asks every detail record and
closing message to end with ("read fresh at close, never recalled"; asked for by
Mike, 2026-10-18, board item `210/280`). It prints only a `## Identifiers`
heading and seven fields in `RECORD.md`'s order, and runs none of the fifteen
checks: it shares their reads (`gather()`: session, transcript, window, repo,
board, `gh`, branches) but not their verdicts, so it never waits on
`board.py --check` or a floor run. It exits `0`, since it is a record and not a
verdict. `--json` gives the same fields as JSON, as there was nothing to design.

The field set is stable (§10): an empty field prints `none`, a field the tool
cannot derive prints `by hand — <why>` and never a guess. `Other repos` printed
the by-hand line until 210/480 (§9.3), because nothing here could see another
repo; it now names the repos read from the transcript, and prints by hand only
for the paths it could not place, or when there is no transcript.

- **Commits.** Three tiers, because the window alone credits a concurrent
  session's work as the session's own (§15.1). *Credited*, oldest first, as
  short shas: a commit that a `git commit` command of the session, or of one of
  its subagents, made, matched by subject, repo, result and time (§15.1), or the
  squash merge of a PR the session ran `gh pr merge` on. The range shows only when each credited commit's
  one parent is the credited commit before it, and is written `first^..last`
  because a git range excludes its left end; a peer's commit between two of
  them breaks it, which is the honest answer. *Unconfirmed, dated in the window
  only*: the rest of the window's commits, listed on their own line with "check
  before pasting as fact"; one whose subject matches a command that does not fit
  says so on a line of its own. *Left out*: squash merges of PRs the session ran
  no numbered merge for (a heuristic, and printed as one). Both sub-lines print
  on every run (`none` when empty).
- **Pull requests.** The repo alone cannot name a merged PR, so the union of
  three sources: `gh pr create` results (the PR URL in the output),
  `gh pr merge <n>` commands, and the open PRs check 4 already credits. Each
  carries what the session did (`opened`, `merge run`) and its state now from
  `gh pr view`. A command whose result is an error counts for nothing, a
  merge with no number or `--repo` is skipped, and a created PR whose URL names
  another repo is counted and left to hand.
- **Board.** From one `git log -p -U0` over the item store, reduced once per
  commit tier: an added item file is *created*; a first line that becomes
  `- [x]` is *completed*; one that becomes `- [~]` is *claimed*, listed only if
  it is still claimed at the end (a claim released inside the window is not
  owed); a state line that gains `⏳` marks a *review item created*. Ids come
  from the path's two numeric prefixes. The four lines follow the credited
  commits only (a claim counts as still open only if nothing in the window moved
  the item since, so a confirmed claim an unconfirmed commit closed or released
  has its own line); a further line lists what the unconfirmed commits add on
  top, and a last one what only a left-out squash merge carries, because the
  branch commits it repeats may be on no ref (IE14). A hand-kept board has no
  item store and prints by hand.
- **Worktrees and branches.** A worktree put away and its deleted branch leave
  no trace in git, so the creations are read from the transcript: `git worktree
  add` commands (path, and `-b` or the path's name for the branch) and
  `EnterWorktree` results saying "Created worktree at ...". A `$VAR` in the path
  is expanded from a literal assignment earlier in the command or the
  transcript (the same reading as message files); a path that cannot be resolved
  is dropped, not guessed (`210/330`). An add inside a `for VAR in w1 w2; do ...
done` loop whose word list is plain words (no glob, brace, `$` or backtick) is
expanded once per word, nested loops multiplying; a loop over anything else
leaves its variable unknown. Every add still dropped is counted, and the block
prints one line, "N worktree adds not resolved", so a short list says so
(`210/360`). Each is then
  checked now: directory present or put away, branch deleted or kept (merged
  or not). Worktrees born in the window and branches with a tip in it are
  added, since those still exist and the repo can show them.
- **Agents.** Check 12's per-agent reads, uncapped, because an identifier list
  that stops at 25 stops being a record. A sub-line beneath it, *other launched
  work*, carries check 15's counts (zeros included) and every item, uncapped
  (210/460): the field set stays seven, and `--identifiers --json` gains a
  `launched` key beside `agents`. `RECORD.md`'s Agents line says it covers
  anything the session launched.
- **Other repos.** *(210/480.)* The repos §9.3 found, one line each (name, the
  commits from the window, and the status of its checks when not clean), the
  count of unresolved paths with "fill in by hand", and the note on naming a
  private repo generically.

The shell parsing is deliberately small (the first segment of a command, the
common option forms). A form it cannot read is missed, not guessed, and the
block's last line says in italics how commits and board movement were
attributed (§15.1).

Not done: the commits of workers' other repos, a PR opened from a checkout of
another repo (counted, listed by hand), and a `gh pr merge` that names no
number.

### 15.1 Attribution of commits and board movement (210/290)

The first real block listed 115 commits where the session's own were 88: a
concurrent session's branch commits and the squash merge of a PR the session
never merged were dated inside the window, so the window credited them. The same
block credited that session's board item as created, and listed an item as a
review item only because its close note mentioned `⏳`. The block is pasted into
records as fact, so the window is no longer enough for it. (Checks 1 to 12 keep
the window; they report owing, where over-crediting errs towards a look, not
towards a false claim.)

Options weighed:

- *First-parent commits on the integration branch only.* Rejected as the rule.
  It drops the work of a session that committed on a branch or worktree (a
  worker, this very item) and of one whose branch was merged `--no-ff`, and it
  does not remove a peer's direct commits to the integration branch, which are
  first-parent too. It survives in one place: a squash merge is recognised by
  sitting on the integration branch's first-parent line (local and
  remote-tracking), so a branch commit whose subject merely ends `(#N)` is not
  mistaken for one.
- *Leave out squash merges of PRs the session did not run `gh pr merge` on.*
  Taken, as a heuristic that the block prints as one. The merge is read from the
  session's and its subagents' commands, a failed command counting for nothing
  (the subagents' results are checked as the parent's are, IE5), and run in
  this repo. Cost: a `gh pr merge` with no number (current branch), a web-UI or
  `--auto` merge, or a direct commit whose subject names an issue `(#N)` on the
  first-parent line, is listed as left out, visibly, and not silently lost. A
  squash whose title, less the `(#N)`, equals a subject the session gave a
  commit command is not left out: it may be the session's own branch work, merged
  by a peer, so it is unconfirmed, with the reason on a line of its own.
- *Positive evidence of authorship.* Taken as the main rule, and bound to the
  command (160/960, after the cold pass found the first binding, subject
  equality alone, crediting a concurrent session's same-subject commit as fact).
  This house commits with `git commit -q`, so a SHA never reaches the
  transcript, but the message does, in `-m` or in a heredoc (`-m "$(cat
  <<'EOF'` or `-F - <<'EOF'`), and so do the command's own times and result. A
  window commit is credited only where one `git commit` or `git merge` command of
  the session, or of one of its subagents (the same directory check 12 reads),
  fits it on all four: the subject (whitespace-collapsed; a message's first
  paragraph, its lines joined, as git reads %s); the repo (the record's cwd, a
  preceding `cd` and each `-C` resolve into the repo, a linked worktree of it, or
  a worktree the session added, or into a directory sharing its git common dir);
  the result (the tool_result is not an error: a command that fails for any
  reason, `&& git push` included, counts for nothing, which errs towards
  unconfirmed); and the time (the commit's committer second falls inside the
  span from the command's tool_use record to its tool_result, a second of slack
  each side). Each command confirms at most one commit. A git word counts only
  in command position, so a commit command quoted in a heredoc body, a grep
  pattern, an echo or an `sh -c` string runs nothing and is no evidence. A
  rebase, a `pull --rebase` or an amend with no message re-commits the session's
  own commits; a copy made inside such a command's span confirms only if its
  subject is one the session already gave a commit command. A commit whose
  subject matches a command that does not fit (failed, another repo, another
  time) stays unconfirmed and says so. A message in a variable is unreadable and
  its commit lands as unconfirmed, never as credited. A message in a file (`-F path`, `--file=path`, 210/310) is
  read from the same transcript's own evidence of writing that file: the
  Write tool's `file_path` and the first non-empty line of its `content`, or a
  heredoc in a Bash command (`cat > path <<'EOF'`, `cat <<EOF > path`,
  `tee path <<EOF`; appends are skipped, since the file's first line is then
  unknown). The path must match exactly after resolving it against the
  command's cwd (and a `git -C dir`), never by basename. The latest write
  before the commit, in the same transcript, wins; where the writer is a
  different transcript of the session (parent or subagent), the two cannot be
  ordered and a subject from any write to that path is accepted. A file the
  session did not write, such as a peer's, matches nothing.
- *Time window only.* Kept as the fallback, but never as fact: what only the
  window supports is printed as *unconfirmed* with an instruction to check it.
  Over-listing an unconfirmed commit costs a glance; crediting a peer's work
  costs a false record.

Board movement is reduced once from the same log per tier, so a board line
cannot credit what the commit line does not. The `⏳` marker follows board.py's
grammar: the file's first line, after the `- [ ]`, `- [~]`, `- [x]` or bare
`- ⏳` form, outside backtick code spans, and *gained* by the commit.

A path with a shell variable (`$S/m.txt`, `${DIR}/m.txt`) resolves only when
the same command, or an earlier one in the transcript, assigned the variable a
literal (`S=/abs/path`, or a literal relative to the cwd). A variable set from
a command (`S=$(mktemp -d)`), from another variable, or never in the
transcript leaves the commit unconfirmed. Every run says so, in the
attribution line: a message read from a file is matched only when the session
wrote that file at a path that resolves. The JSON gained fields with 160/960
(`commits.evidenceUnreadable`, an optional `note` on an unconfirmed item,
`board.claimedMoved` and `board.viaSquash`); existing fields keep their meaning,
the credited lists being the stricter ones.

Worker sessions (IE8): a worker dispatched as its own headless session has its
own transcript, which this form does not read. Its commits print as unconfirmed,
which is expected, not a fault, for an orchestrator's block under the queue-run
pattern; the orchestrator confirms them by hand (its own claim commit, the
worker's report) or says so. Subagents of the session, whose transcripts sit in
its `subagents/` directory, are read. An unreadable subagent transcript is
counted on the Commits line ("evidence incomplete"), since its commits then
print as unconfirmed.

Board state line (IE13): the board reduce reads each item file's first line,
where `board.py` reads the first non-blank, non-comment line. An item whose
state line follows a leading comment reads here as having no state. No item in
this repo has that shape.

Not solved: a message file written some other way (`echo`, `printf`, an
editor, a script, `sed -i` on an existing file) or at a path built by a
command is unreadable, and so is a message in a variable; a session that
commits only that way gets an empty credited list and everything unconfirmed,
which is honest but unhelpful. A Write whose result was an error still counts
as a write. Symlinked paths (`/tmp` against `/private/tmp`) are compared as
written, not by realpath. A commit made by a tool on the session's behalf (a
script that commits) is unconfirmed too. Under-credit forms, each erring towards
unconfirmed (IE10): a cherry-pick, a revert and a default-message merge (no
subject in the command); `git --git-dir=...`, an alias, `-qmfoo`, `--file=-`,
a `$'...'`-quoted message, and a commit command wrapped in `sh -c`, `ssh` or a
script; a message file edited with an editor or the Edit tool after its Write; a
commit made in a worktree since removed that the session's own `worktree add`
commands do not name; and, where a branch's pre-rebase copy survives on a ref,
both copies are credited (every one is the session's, so the count doubles but
no peer's commit is credited).
