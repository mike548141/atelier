- [ ] 🎯 **PROPOSAL for the floor + `GUARDS.md` — where siblings exist, require a
      path-scoped commit or an explicit whole-index marker** `[M][tools][docs]`
      — filed from `cbom` 2026-08-19 via § *Pointing up* (its board `120/070`,
      `b60590b`), by a session reporting itself as the **offender** in a fresh
      staged-sweep instance. The fix is proposed here because the floor is
      atelier's and the child calls it without a shim. Mike's ruling: it is a
      *forbids the act* guard declaration, and the guard programme is his
      commission.
      **The finding that makes it worth more than another instance: the floor
      already printed the sweep, and the correct number was scenery.** The filer
      read `git diff --cached --stat` before staging — four paths, all its own —
      and the floor's own line on that same commit said
      `✓ publishscan clean — 5 staged path(s)…`. A peer had staged into the
      shared index in the window between the read and the commit. 🛑 **So "print
      the path list, not just the count" is the WRONG fix** — a correct number
      was already on screen, and the floor prints roughly a hundred lines across
      fifteen scanners. More text into that wall makes an instance findable in
      hindsight, not preventable at the time. The filer notes it would have
      argued for that fix itself before watching it fail on it.
      *Recorded as reported:* the five-versus-four reading is the child's
      measurement of its own commit and was not reproduced here. *Verified
      here:* `publishscan --staged` does build its set from
      `git diff --cached --name-only --diff-filter=ACMR`
      (`tools/publishscan.py:256` at atelier HEAD — the filer cited `:247`, a
      few lines out), which is exactly the set `--stat` shows, so the comparison
      is between like and like.
      **The mechanism, re-run at this end rather than taken on report** (a
      throwaway repo, a `core.hooksPath` hook printing what it sees):

      | commit form | `GIT_INDEX_FILE` the hook sees | staged set the hook sees |
      |---|---|---|
      | `git add a b; git commit` | `.git/index` | 2 — `a b` |
      | `git add c d; git commit -- c` | `.git/next-index-<pid>.lock` | 1 — `c` |

      `d` remained staged after the second commit. Two consequences, both
      confirmed: **detecting a path-scoped commit is free** — the temporary
      index gives it away — and the hook's `--staged` view is **already narrowed
      to what the commit will actually carry**, which is what makes the guard
      enforceable at the hook rather than after the fact.
      **The proposal.** Where `git worktree list` reports more than one worktree,
      the floor requires the commit to be path-scoped, or to carry an explicit
      marker declaring the whole index is intended.
      **Three limits, filed with it so it is not oversold.** (a) It does not make
      the index safe — it makes *your commit* not carry foreign paths, and
      `CONCURRENCY.md`'s precondition still travels: `git commit -- <paths>` is
      safe when you can *identify* whose the other paths are, which a session
      working alone cannot do. (b) It cannot stop a deliberate foreign
      path-scope; it stops the **accidental** sweep — 7 of 7 of the child's
      instances that day. (c) `git worktree list` is a **proxy** for concurrency,
      not a measurement: a stale worktree nobody is using still charges the tax,
      and two sessions in one checkout with no worktree still slip through.
      **The cost, and it lands hardest here.** You name your paths on every
      commit in a multi-worktree repo. The child reports six worktrees live as it
      wrote. **atelier is structurally multi-worktree** — the harness nests
      worktrees inside the repo, and `git worktree list` in this very session
      returns 3 — so the tax would bind on essentially every atelier commit, not
      occasionally. That is the number a ruling should weigh, and it is the
      argument both ways: the exposure is continuous here, and so is the cost.
      **Related and unresolved:** limit (c) is the same proxy-versus-measurement
      shape as `310/020` (nothing enumerates what the estate owes the house), and
      the accidental-sweep class is `050` above from the writer-versus-reader
      angle. Whether they are one guard or three is part of the ruling.
