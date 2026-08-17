# Verify before closing — and two fabricated readings from a wandering cwd (2026-08-17, 1232 UTC)

**The ask.** Mike, opening: *"Give me a full list of work to do in this repo"*.
Then, after the first answer: *"Lets walk through the questions and rulings
required to progress"*, with a commission attached — *"As you are not the
session that did the work for the stale item I want you to dig in deep to fully
prove that it is truly done to the full intent of whats in the roadmap before
marking it completed. Look at from every angle you can to ensure we are not
mistakenly closing an item that still requires work"*.

**The commission was the right instinct and it paid.** The item in question —
`120`, the `test_plainscan.StopHook` flake — was fixed a week earlier by another
session. A shallow check would have closed it. The deep check confirmed the fix,
**falsified two claims in the item's own recorded evidence**, and surfaced one
residual nobody had named. Detail is on the item; the shape of the method is
what belongs here: **reproduce the defect before believing the fix**, then run
the pre-fix code as a control.

- Reproduced deterministically: firing the reply hook at one shared state file,
  the third call for a session id gives up instead of blocking, because the
  give-up path clears the counter. A fixed 1-in-3 cycle, not a random flake.
- Control on `b879b02^` in a throwaway tree with an isolated `HOME`: failed on
  runs 3 and 6 of 6, matching the recorded failure pair exactly.
- That control is what falsified the record. The item said *"the module alone
  passes 47/47 every time"*; the pre-fix module fails **alone** at the same
  rate. The full-suite-versus-alone asymmetry never existed — and it was the
  observation that sent the original finder after a fixture race.
- Residual, now the only open question on the item: **nothing guards the fix.**
  The isolation is one line of test `setUp`. Delete it and the flake returns at
  one-in-three, invisible to CI, because every CI run gets a fresh `HOME`.

## The part worth more than the verification: two readings this session invented

**The first answer to Mike's question was wrong, and so was a liveness claim
built on top of it.** Both came from one cause: a probe script `cd`-ed out of
the repo, the shell's working directory did not come back where assumed, and
`git` was then read *through* it. The reading came from a checkout a week
behind, and nothing in the output said so.

| Claimed | Actual |
|---|---|
| `ROADMAP.md` is 3,990 lines; **124 open items**, grouped in ~40 sections | The index is **332 lines**; the store is **175 item files** — 153 open, 15 closed, 1 claimed |
| "A parallel session is live" — two commits landed mid-session, worktree `plainscan-rescope-0810` holds a claim | Those commits are **ancestors dated a week earlier**; that worktree does not exist. HEAD had not moved at all |

**Both were stated to Mike with confidence and evidence attached.** The evidence
was real; it described another tree. This is the second recorded instance of the
class — the estate's own guidance already says a shell's cwd can silently revert
and that liveness conclusions have been fabricated from it before. Recording it
again because a *second* instance is the argument for mechanising, and because
of where it happened:

🔑 **It happened while verifying a defect whose entire subject is cwd-versus-root
confusion.** Item `110` says a scanner given `--root X` and a relative path
reads the cwd's file under X's rules, and that the danger is a confident false
clean. This session produced a confident false clean *about the repository
itself*, by the same mechanism, one level up from the tools. The rule that
would have caught it is the one `110` already argues for: never let a relative
reading stand when an absolute one is available. Every later measurement here
used `git -C <abs>` and absolute tool paths.

**The discriminator that resolved it**, worth keeping because intuition failed
twice: not recency of timestamps, but **ancestry**. `a2ab913` looked like new
work and was an ancestor of HEAD. Later in the session HEAD *did* genuinely move
five commits, and the temptation was to dismiss that as another false alarm —
the same ancestry check is what proved it real.

## A peer withdrew a claim mid-session; the withdrawal did not land

The `ros` session sent a correction over the channel, unprompted: it withdrew
"`pathscan`/`wrapscan` accept `--root` and silently ignore it", saying it had
never tested it and that a persisted `cd` explained its readings.

- **Nothing needed removing.** The receiving atelier session never adopted the
  claim — it re-derived the mechanism and corrected the framing in the item body
  *and* its source footer.
- **The withdrawal's conclusion is falsified.** "There is no tool defect" does
  not follow from its two re-runs, because neither passes a relative path with a
  foreign root. Confirmed by probe: two trees carrying the same `docs/bad.md`,
  one 199 columns and one clean, `--root` at the clean tree — the finding names
  the cwd tree's line, and adding an ignore file to the root tree makes the same
  run report clean with `1 file(s) suppressed`. Both halves in one command.
- **It does cost the item its grounding story**, which is the real disposition:
  `ros` now says its lost round came from a stuck `cd` with `--root .`, which is
  not a mixed root. `ros` is the only witness to its own invocation, so that
  account outranks the inference. Queued on `110` as Mike's ruling.
- The clause it offered to ground — label measurement separately from diagnosis
  — is already grounded generically at `CONCURRENCY.md:441`. The offer adds a
  *named* instance, and this exchange supplies two: the original claim was wrong
  in one direction, the withdrawal wrong in the other, one turn apart.

Of its two smaller offers, the claimed-marker drift is already carried by the
rollout item. The wrapped-title finding — 38 of 194 titles rendering as
fragments in a repo wrapped at 80 columns — has no trace on the board and is
Mike's to queue.

## What this session did NOT do, deliberately

- **Closed nothing.** `120` stays open pending Mike's ruling on the guard.
- **Changed no severity and no doctrine.** `110` keeps 🔥; retiring its grounding
  and adopting the named instance are both put to Mike, not taken.
- **Rebuilt no board list.** The full list of work Mike originally asked for is
  still owed, and must be built from the 175 item files rather than the index.

## Owed to Mike

1. `120` — guard then close, close and queue the guard, or close bare.
   Recommended: the first.
2. `110` — retire the grounding sentence; hold 🔥 on the eleven-tool proof, or
   step it down.
3. Take the named grounding instance into `CONCURRENCY.md`? Doctrine edit, owes
   a cold review.
4. Queue the wrapped-title finding against the rollout item?
5. The original ask, unmet: the full list of open work, rebuilt from the store.
