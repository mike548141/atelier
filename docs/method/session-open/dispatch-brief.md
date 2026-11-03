# The dispatch brief — what every worker prompt carries

An orchestrator that dispatches a worker writes it a prompt: the item, its
evidence, its bounds. The item part changes every time. The bounds below do
not, and before they were kept here they lived only in doctrine prose, so a
prompt written from memory dropped them (`180/120`). Start every dispatch
from this block, fill the `<…>` placeholders and keep every line.

This is house text, not the principal's: it changes like any other doctrine,
and it holds no rule of its own. Each line points at the rule in
[`../CONCURRENCY.md`](../CONCURRENCY.md) that grounds it (table below). It
carries bounds only, never a relaxation of standing doctrine.

```text
## Bounds (binding)
- Work only in <absolute worktree path> (branch <branch>), a worktree
  named <repo>-qr-<session id, first four>-<slug>. Absolute paths
  throughout; never edit the shared primary checkout.
- Scratch: <absolute scratch directory, unique to this worker>. Every
  temporary file goes there and nowhere else.
- A check that may run past the shell tool's foreground cap: redirect its
  output to a file in your scratch directory and append an exit-code line
  (exit=<code>). If the command is moved to the background, poll that file
  yourself; the completion notice will not reach you.
- Stage explicit paths only, never `git add -A`, and commit by pathspec
  (`git commit -- <paths>`).
- Do not push, merge or open pull requests. Commit in your worktree and
  hand back.
- Stop only processes you launched, by their PID or by your own worktree's
  cwd. Never kill by name pattern (`pkill -f`): it reaches other sessions.
- Write no review pointer: the orchestrator writes it when it lands your
  work. Where your item or report names your change, cite it by path and
  by the item it closes, never by branch name or commit hash.
- End your final reply with the line: WORKER DONE: <branch>@<final sha>
```

| Line | Grounding in `CONCURRENCY.md` |
| --- | --- |
| Worktree, its name, absolute paths | § *The substrate*; § *Orchestrated queue runs*: worktree names carry the session's short id (`180/160`); absolute on the cwd hazard, in the scratch rule |
| Scratch directory | § *Orchestrated queue runs*: the worktree is the isolation, the scratch space is not |
| Long-check poll | § *Orchestrated queue runs*: a long check is the worker's to poll (`320/680`) |
| Explicit staging, pathspec commit | § *The trigger*: the index is a shared surface too (`320/350`); § *Claiming work*: one worktree per worker, or forbid `git add -A` |
| No push or merge | § *Orchestrated queue runs*: what a worker inherits is bounded (QR3) |
| Kill scope | § *Orchestrated queue runs*: the machine is shared too (`320/700`) |
| No pointer; cite by path and item | § *Orchestrated queue runs*: the orchestrator writes the review pointer, at the landing (`180/190`) |
| Terminal marker | § *Orchestrated queue runs*: teardown waits for the worker to stop |

What the block leaves to each dispatch: the item and its evidence, the
reading the worker owes first, the checks the change must pass, the board
bookkeeping, and what the report back holds.
