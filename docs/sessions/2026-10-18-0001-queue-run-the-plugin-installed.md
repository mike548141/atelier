# 2026-10-18 · 0001 UTC — Queue run: the plugin installed, and the prompt it replaces carried

**Tier:** Opus 5.5 orchestrating; three cheaper agents for search and research
(one Sonnet clause-mapper, a docs guide twice), two Sonnet workers for the two
code builds. Worktrees `atelier-qr-180-plugin`, `atelier-qr-020-420` and
`atelier-qr-130-030`. Machine load was 29 on 12 cores at open, before this
session started any agent; never more than two agents ran at once.

**The brief.** Mike opened with his hand-carried queue-run prompt and named
the theme: atelier's `queue-run` plugin *"has never been installed. That's
[the estate-root repo's] board item 950. I want you to focus on this work"*,
and *"The current version of the prompt I like to use is this
"~/.pets/session-open-prompt-prior-version-2026-09-14.txt" which we should
update into atelier too"*. He was away for hours: *"Try not to stop and ask me
questions until you have done all the work"*.

## What was done

- **Plugin installed (`180/010`, closed).** First installed from GitHub. Then
  found, from the plugin docs and the install record, that a GitHub install
  is a copy frozen at `plugin.json`'s `version` (0.2.0, unchanged since
  2026-07-21), and third-party marketplaces do not auto-update. Re-installed
  from a **local-path marketplace** on the primary checkout, which the docs
  say loads in place. Measured: a fresh headless session lists all eight
  `atelier:` skills, and loading `atelier:session-onramp` reports the
  checkout's own `skills/session-onramp` as its base directory. The vestigial
  cache copy under the plugin cache is unused.
- **The skill now carries the whole prompt.** A clause-by-clause map of
  Mike's prompt against the skill and doctrine found six clauses carried
  nowhere and five only partly. `CONCURRENCY.md` § *Orchestrated queue runs*
  gains: where the doctrine is read from (and the minimum viable and no-repo
  runs), three selection rules (mid-run hand-overs become items, idea-only
  items wait, big items are split), what the report carries (session id, one
  decision at a time, a re-read of every ask), a value reading of the spend
  directive (follow-on 2 of `180/010`), and a per-run ask cadence. The skill
  points at each. README says how to install in place.
- **The canonical prompt is the text in use (`180/030`, filed and closed).**
  His text, with two lines reconciled to later rulings. 🔎 Both lines had
  been fixed in that file and were undone on 2026-10-17 by `6a0ac93`, a
  "restore current content" commit that wrote an older text back as current.
- **Worker teardown (`180/020`, closed, option 3).** Remove a worker's
  worktree only after the harness's finished notice; ask every worker for a
  terminal marker. This run's two workers were briefed that way, and both
  worktrees came down only after both signals.
- **Hand-up PR #120 landed** (`320/720`), then **fixed**: `REVIEW.md` rule 1's
  *side doors* — records a reviewer reads before the brief name deferred
  material by file and count only. `RECORD.md` points at it.
- **`020/420` built**: `ccclose` check 12, *Subagents finished* (Sonnet
  worker, read before merge; 458/458 instrument tests at the rebased head),
  and the agent list in `RECORD.md`'s all-clear and `CONCURRENCY.md`'s
  close-out measurement.
- **`130/030` fixed**: `coldsweep --commit <sha> [--path <p>]`, the body-free
  read of a landing commit (Sonnet worker; tools suite 1930, all passing),
  and the `review-brief` skill naming it.
- **The estate-root repo's item 950 closed** there, with the one loose
  prompt copy left in place as Mike's paste fallback.
- **Cold passes queued, none taken** (this run authored every delta):
  `160/900` (queue-run and teardown), `160/910` (side doors), `160/920`
  (subagents at close), `160/930` (body-free commit read).

## Not done, and why

- **The practical proof of `/atelier:queue-run`** is the first real run
  opened with it. This session could not run it: a run never starts its own
  successor.
- **The 2026-09-16 prompt additions** Mike's text drops (date at open,
  checklist reports, verify-don't-infer, bullet-list board answers, the
  fuller close confirmation) stay in git history. Whether any comes back is
  his call, put to him at the close.
- **Stopped** because the theme Mike named is done, along with every loose
  end next to it that needed no ruling. Most of the rest of the board needs
  a ruling or a Fable reviewer.

## After the first close

- The session hit the plan's five-hour limit right after the close commit
  and was resumed. Before the cut it had landed hand-up PR #121 (`115/340`
  addendum, opened by a peer during the window). On resume it acted on that
  addendum's own lesson and re-ran both suites on merged `main`: instruments
  458/458, tools 1930 OK. The floor at `5bdc71f` is green. The intermediate
  `main` runs (`7b4b466`, `d2ca04c`) were cancelled by cancel-in-progress,
  which is exactly the gap #121 records.
- `020/420`'s close first said `ccclose` was not on the path. It is, as a
  link into the checkout, so check 12 is live. Corrected on the item.

## Mike's close-out answers, enacted

Asked at the close, one decision at a time, through the decision device:

- **Prompt lines**: he picked all four of the dropped 2026-09-16 lines (the
  fuller close check, the date with checklist updates, verify-don't-infer,
  board answers as bullets). Restored, and carried in `CONCURRENCY.md` and
  the skill (`180/040`). Four smaller phrases were not offered to him and
  stay out; they are named on the item.
- **Plugin version**: *"Track every commit"*. The version field was dropped
  from both manifests (`180/050`). His install is unaffected because it
  loads in place.
- **Loose prompt copy**: keep it as a fallback. Left in place.

## Mike's mid-run asks after the resume

- **The template history (`180/060`).** *"I would like that to be recorded
  in my git history so I can see how my opening prompt changes over time"*,
  in public atelier, with only text reused in two or more sessions, and no
  private detail or session-specific work. A Sonnet worker mined 946
  sessions. The orchestrator read every flagged unit and dropped nine (one
  run's themed work, five of them also naming private repos, tools or
  devices), and redacted one repo name. Re-pastes were collapsed, leaving 50
  versions, 2026-07-08 to 2026-10-17. They are committed oldest first to
  `docs/method/session-open/template-history.md`, each with its first-use
  date as author date; the directory README gives the method. Nothing before
  2026-07-08 survives in the store. A privacy cold pass is queued at
  `160/940`.
- **Session id first, no date line (`180/070`).** The harness now stamps
  each turn, so the date line goes. That is Mike's observation, not tested
  on other surfaces.
- **The identifiers block (`180/080`).** `RECORD.md` asks for it at the
  tail of every detail record and closing message. Mike named the session
  id and commits, then PR ids and worktrees created, then board items
  completed and created. The rest of the set is the agent's recommendation.
  `ccclose --identifiers` prints it (`210/280`, Sonnet worker, home paths
  shown as `~/`). Its first real run over-credited a parallel session's work
  (`210/290`, filed), so the block below is corrected by hand where marked.

## Recorded against itself

- Twice a commit was refused by the hook while the output was filtered
  through `grep`, so the refusal showed only as a missing commit: the
  wrapscan and board refusals on the first claims. Caught each time by
  `git log`, which is `CONCURRENCY.md`'s own rule ("filtering output is not
  reading it"). The test-count grep failed the same way once. After that,
  output went to a file and the exit code was checked.
- `pathscan` (warn-only) now flags the prompt file's `../atelier/...` path,
  which is relative to a child repo by design. Left unsuppressed.

## Identifiers
- **Session**: e1d4097c-51e0-4103-8dc4-2c361166237b · Opus 5.5 · 2026-10-17 23:59 to 2026-10-18 04:14 UTC
- **Commits** (88 on `main`, this session's own; hand-corrected from the tool's 115, `210/290`): `b12c76d` to `ec37c6b` on the first-parent line, excluding `b6be263` (PR #119, a parallel cloud session's). 50 of them are the template history, author-dated to each version's first use.
- **Pull requests** (2):
  - #120 merge run — now merged
  - #121 merge run — now merged
- **Board**:
  - completed: 020/420, 130/030, 180/010, 180/020, 180/030, 180/040, 180/050, 180/060, 180/070, 180/080, 210/280, 320/720
  - created: 160/900, 160/910, 160/920, 160/930, 160/940, 180/030, 180/040, 180/050, 180/060, 180/070, 180/080, 210/280, 210/290, 320/720 (320/720 arrived as PR #120, landed here)
  - claimed (still open): none
  - ⏳ review items created: 160/900, 160/910, 160/920, 160/930, 160/940
- **Worktrees and branches** (7):
  - ~/worktrees/atelier-qr-180-plugin (branch qr-180-plugin) — worktree put away; branch deleted
  - ~/worktrees/atelier-qr-020-420 (branch qr-020-420) — worktree put away; branch deleted
  - ~/worktrees/atelier-qr-130-030 (branch qr-130-030) — worktree put away; branch deleted
  - ~/worktrees/atelier-qr-180-followups (branch qr-180-followups) — worktree put away; branch deleted
  - ~/worktrees/atelier-qr-180-070 (branch qr-180-070) — worktree put away; branch deleted
  - ~/worktrees/atelier-qr-210-280 (branch qr-210-280) — worktree put away; branch deleted
  - ~/worktrees/atelier-qr-180-060 (branch qr-180-060) — worktree put away; branch deleted
- **Agents**: 6 · 6 reported · 0 stopped on purpose · 0 result never consumed · 0 cut mid-flight
  - a61c42c Build ccclose --identifiers — reported (completed notification)
  - a6ede35 Mine opening-prompt template versions — reported (completed notification)
  - aa97dfb Build ccclose check 12 — reported (completed notification)
  - aab4048 Map prompt clauses to doctrine — reported (completed notification)
  - ab1989e Build coldsweep --commit — reported (completed notification)
  - ac4bc87 Plugin update semantics — reported (completed notification)
- **Other repos**: the private estate-root repo, two commits (claim and close of its item 950). User-level, outside any repo: the plugin install in Claude Code's user settings, and two memory notes.

*Generated by `ccclose --identifiers`; Commits, the Board lines and Other repos corrected by hand as marked.*
