# Concurrency — running several lines of work at once, safely

The goal: build, test, document and ship more than one thing at a time without
the parallel lines corrupting each other or stepping on the live world. This is
the bulkhead principle (a failure in one partition can't cascade) applied to
*time* instead of to devices.

## The substrate: one worktree per line of work

Never run parallel work in a single working tree — two sessions editing the same
files race the git index and stomp each other's changes and test runs. Instead,
each independent line of work gets its **own git worktree**: its own checkout,
its own branch, off the same repo.

```sh
git worktree add ~/worktrees/<repo>-<feature> -b <feature>
```

- Worktrees live **outside iCloud** (`~/worktrees/…`) to avoid sync churn; the
  external venv is shared across them, which is what you want.
- Each parallel session = one worktree = one branch = one session-log entry that
  names its worktree and branch.
- They reconcile on `main` via PR/merge. `main` is the integration point; the
  worktrees are where divergence is allowed to happen.

## Two kinds of parallelism — use the right one

- **Parallel *sessions* (worktrees)** — for independent, long-lived lines of
  work you want to *steer* (feature A here, feature B there). Human-in-the-loop
  on each.
- **Background *agents* (fan-out)** — for breadth *within one task* that you then
  synthesise: multi-file reviews, research sweeps, "check these 20 things". The
  agents return results into one context you drive; they are not long-lived
  independent developers.

Rule of thumb: **agents for breadth-within-a-task; worktrees for
parallel-tasks.**

## The safety rail: serialise real-world side-effects

Builds may run fully in parallel. **Actions that touch the live world must
not.** Anything that changes a device, deploys, publishes, or spends is
**serialised and announced**, even when the builds that produced them ran
concurrently.

- Two worktrees may both *prepare* a change to the same live device; only one
  *applies* at a time, and it says so.
- This is the apex + the AUTONOMY floor holding across concurrency: parallelism
  is a build-time convenience, never a licence to double up on irreversible or
  outward actions.

*Bearing:* tiki already applies serially per device (parallel across devices,
serial within one); this doctrine generalises that discipline to every outward
action across every parallel session.

## Integration hygiene

- Rebase/merge small and often; a worktree that diverges for days is a merge
  hazard.
- Delete a worktree when its branch lands (`git worktree remove`); stale
  worktrees are the concurrency equivalent of a leaked file handle.
- If two lines of work both need the same live resource, that's a signal to
  sequence them, not to build a locking scheme — KISS over cleverness.
