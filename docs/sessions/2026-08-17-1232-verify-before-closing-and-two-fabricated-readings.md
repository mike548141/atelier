# Verify before closing — and two fabricated readings from a wandering cwd (2026-08-17, 1232 UTC)

**From the retired session log**, word for word; only its link paths were re-pointed for this folder:

<!-- archivecut:log-entry docs/SESSIONS.md 285+1 -->
- [2026-08-17 · 1232 UTC · Verify before closing — and two fabricated readings from a wandering cwd (Opus 5, main)](2026-08-17-1232-verify-before-closing-and-two-fabricated-readings.md) — Mike asked for the full list of open work, then commissioned a deep proof that the stale flake item `120` was truly done before it was closed: *"Look at from every angle you can to ensure we are not mistakenly closing an item that still requires work"*. The commission paid. The fix in `b879b02` is real, and the verification **falsified two claims in the item's own evidence** — reproducing the defect first (a shared state file makes every third call for a session id give up instead of blocking: a fixed 1-in-3 cycle, not a random flake), then running the pre-fix code as a control in a throwaway tree with an isolated `HOME`, which failed on runs 3 and 6 of 6. That control killed the record's *"the module alone passes 47/47 every time"*: the pre-fix module fails alone at the same rate, so the full-suite-versus-alone asymmetry never existed — and it was the observation that sent the original finder after a fixture race. One residual now named and nothing else: **nothing guards the fix**, which is one line of test `setUp`, and CI structurally cannot see its removal because every run gets a fresh `HOME`. Item left OPEN; the guard question is Mike's. **The part worth more than the verification: two readings this session invented.** A probe script `cd`-ed out of the repo, the shell did not come back where assumed, and `git` was read through it — so the answer to Mike's opening question described a checkout a week behind (3,990-line index and "124 open items", against the real 332-line index over 175 item files: 153 open, 15 closed, 1 claimed), and a "parallel session is live" claim was built on commits that were **ancestors dated a week earlier** plus a worktree that does not exist. Both were put to Mike with real evidence attached that described another tree. Second recorded instance of the class, and recorded again for where it landed: **it happened while verifying `110`, a defect whose whole subject is cwd-versus-root confusion producing a confident false clean** — the same failure one level up from the tools. The discriminator that resolved it was **ancestry, not timestamps**; intuition failed twice, and the same check later proved a genuine five-commit move real when the temptation was to dismiss it as another false alarm. **A peer withdrew a claim mid-session and the withdrawal did not land:** `ros` retracted "`--root` is silently ignored", but its conclusion "there is no tool defect" is falsified by probe — its two re-runs never pass a relative path with a foreign root. Nothing needed removing (the receiving session had never adopted the claim), but the withdrawal **does** cost `110` its grounding story, since `ros` now attributes its lost readings to a stuck `cd` with `--root .`, which is not a mixed root. Queued as Mike's ruling. Closed nothing, changed no severity, edited no doctrine; the full list of work Mike asked for is still owed and must be rebuilt from the store.


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
