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

## Recorded against itself

- Twice a commit was refused by the hook while the output was filtered
  through `grep`, so the refusal showed only as a missing commit: the
  wrapscan and board refusals on the first claims. Caught each time by
  `git log`, which is `CONCURRENCY.md`'s own rule ("filtering output is not
  reading it"). The test-count grep failed the same way once. After that,
  output went to a file and the exit code was checked.
- `pathscan` (warn-only) now flags the prompt file's `../atelier/...` path,
  which is relative to a child repo by design. Left unsuppressed.
