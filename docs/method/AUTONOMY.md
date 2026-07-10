# Autonomy — when the agent proceeds, when it stops to ask

Mike carries high cognitive load across several entities. Stopping to ask "may
I run this?" for work he would only ever say yes to is itself a cost — it spends
his attention on a decision he doesn't need to make. The point of this doctrine
is to **maximise the work the agent can do unsupervised without ever crossing
the lines that actually matter**.

## The one rule

> **Proceed on anything recoverable. Stop and confirm only for the genuinely
> hard-to-undo: making private things public, secrets, spend, and anything
> touching people or safety.**

Git is recoverable (revert/reset/restore a branch), so committing, pushing, and
managing pull requests are *inside* the recoverable line, not outside it —
Mike granted this as a standing rule for all work (2026-07-10: *"you should be
free to commit and push as you see fit, and manage pull requests as needed —
you have better context than I"*). The rest of this doc is where the line falls.

## Always proceed (no prompt)

- Read anything in the repo; search, list, inspect.
- Write/edit files in the repo; create scratch files.
- Run the dev loop: tests, linters, type-checkers, builds, formatters.
- **Commit, push, and manage pull requests** at discretion across all work —
  commit at natural checkpoints, push, open/merge/close PRs, branch as needed.
  Deploy-on-push (e.g. Cloudflare Pages from `main`) is accepted under this
  grant.
- All local git: branch, stage, diff, stash, merge, `git worktree add`.
- Install an **approved** tool that's merely missing (see TOOLBOX).

## Always confirm

The floor. These hold everywhere, standing grants notwithstanding, because they
are hard or impossible to undo:

- **Making a private thing public** — changing repo/artifact visibility to
  public, or sending to an external audience. Publishing is not undoable: it may
  be cached or indexed even after deletion. (Routine *push to Mike's own
  remotes* is not this — that's granted above; this is the private→public
  boundary and external distribution.)
- **Truly destructive / irreversible** — deleting data the agent didn't create,
  `rm -rf` of real work, force-push or history rewrite on a shared branch,
  dropping a database, wiping a device.
- **Secrets** — reading, writing, moving, or regenerating credentials/keys.
- **Spend** — anything that costs money or metered usage beyond the plan
  (e.g. a billed model review — see MODEL-ECONOMICS).
- **People and safety** — any action touching a person's safety, or the safety
  of physical resources.
- **Installing an *unapproved* tool** — a new capability is a new trust surface;
  that's the owner's call (see TOOLBOX).

When one of these is required, surface it plainly (the apex): say what the
action is, why, and what's irreversible about it. And a grant in one context is
not a grant for the next — "yes, publish this" is not "publish things like this
from now on".

## How the grant evolved (context, not gates)

Autonomy widened as trust was demonstrated. The waypoints:

| Date | Grant |
|---|---|
| 2026-07-06 | commit in `ros` at discretion (push confirmed) |
| 2026-07-10 | `faves`: commit **+ push** at discretion (push = deploy) |
| 2026-07-10 | **all work: commit + push + manage PRs at discretion** |

The floor above never moved through any of these. A repo may still record a
*narrower* posture in its `CLAUDE.md` when its live blast-radius warrants extra
care (e.g. a repo that pushes straight to live network infrastructure might keep
a human beat before an apply) — but the default is now broad.

## Before you destroy or overwrite

Before deleting or overwriting something the agent didn't create, look at it
first — if what's there contradicts how it was described, surface that instead
of proceeding.
