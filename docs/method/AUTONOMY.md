# Autonomy — when the agent proceeds, when it stops to ask

Mike carries high cognitive load across several entities. Stopping to ask "may
I run this?" for work he would only ever say yes to is itself a cost — it spends
his attention on a decision he doesn't need to make. The point of this doctrine
is to **maximise the work the agent can do unsupervised without ever crossing
the lines that actually matter**.

This is not a fixed permission list. It is the *framework* every repo's
permission list is generated from.

## The one rule

> **Proceed on anything reversible and local. Stop and confirm only for actions
> that are hard to undo or reach outside the machine.**

Everything else is detail on where that line falls.

## Always proceed (no prompt)

Reversible, local, and inside the repo or a scratch area:

- Read anything in the repo; search, list, inspect.
- Write/edit files in the repo; create scratch files.
- Run the dev loop: tests, linters, type-checkers, builds, formatters.
- **Commit** at natural checkpoints (a completed, verified unit of work).
- Local git that doesn't rewrite shared history: branch locally, stage, diff,
  stash, `git worktree add`.

## Always confirm (regardless of repo, unless a specific standing grant covers it)

The floor. These hold even where broad autonomy has been granted:

- **Destructive / irreversible** — deleting data the agent didn't create,
  `rm -rf`, force-push, history rewrite, dropping a database, wiping a device.
- **Outward-facing / publishing** — sending anything to an external service or
  audience; making a private thing public. (Publishing is not undoable: it may
  be cached or indexed even after deletion.)
- **Secrets** — reading, writing, moving, or regenerating credentials/keys.
- **Spend** — anything that costs money or metered usage beyond the plan
  (e.g. a billed model review — see MODEL-ECONOMICS).
- **People and safety** — any action touching a person's safety, or the safety
  of physical resources.

When one of these is required, surface it plainly (the apex): say what the
action is, why, and what's irreversible about it.

## The middle: push, deploy, and per-repo grants

Push is the interesting case, because whether it's "local" or "outward" depends
entirely on what the remote *does*:

- **Push to a repo that only stores** → still outward (it leaves the machine and
  is shareable) but low-consequence; grantable as standing autonomy per repo.
- **Push to a repo that deploys** → push *is* a deploy, a real outward action;
  confirm unless the owner has explicitly granted standing authorisation for
  that repo.

So autonomy is **granted per repo, by context**, and each repo records its own
level in its `CLAUDE.md`. The two live examples that ground this doctrine:

| Repo | Standing grant | Why | Still asks |
|---|---|---|---|
| **ros** | commit at discretion; push confirms | no remote today; changes touch live network infra | push, outward actions |
| **faves** | **commit *and* push** at discretion | push to `main` deploys via Cloudflare Pages — Mike wanted the deploy loop unblocked | branching off `main` |

Same agent, same floor, different granted middle — decided by what a push
actually does in each place. A new repo inherits the *framework* here and then
records the specific grant Mike gives it.

## Notes

- A grant in one context does not extend to the next. "Yes, publish this" is not
  "yes, publish things like this from now on".
- Before deleting or overwriting something the agent didn't create, look at it
  first — if what's there contradicts how it was described, surface that instead
  of proceeding.
- This doctrine generalises two earlier per-domain grants: commit authority
  (ros) and device-change authority (the MikroTik fleet). Both are instances of
  "the owner sets the autonomy level for a domain; the floor never moves".
