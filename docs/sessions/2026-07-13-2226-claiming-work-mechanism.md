# 2026-07-13 · 22:26 — claiming work: making selection collide like naming does (Opus)

**From the retired session log**, word for word; only its link paths were re-pointed for this folder:

<!-- archivecut:log-entry docs/SESSIONS.md 84+1 -->
- [2026-07-13 · claiming work — making selection collide like naming does (Opus)](2026-07-13-2226-claiming-work-mechanism.md) — Mike's fourth concurrency snag, hit repeatedly across parallel evening sessions: several sessions each told only "the next thing in the queue" self-selected the **same** roadmap item and duplicated the work, silently — nothing in tree or record ever conflicted to warn them. Selection was the one coordination point CONCURRENCY named a substrate for (worktrees) and a trigger for (say-so / dirty-tree) but never a *claim* on. Fix generalises the record-ID bearing the doc already carries: **force the collision onto one shared line.** A session claims an item by editing *its own roadmap line in place* (`[~]` + `(claimed <date>-<HHMM>, wt: <branch>)`) and pushing **before** working — same-item double-claim lands as a trivial same-line rebase conflict, first-to-push wins, loser takes the next open item; different items touch different lines and both proceed. Worktree-mode only (zero cost to the solo default); grain is the leaf item not the theme (a themed instruction fans out); release = branch put-away; **orphan claims** judged like stale branches (timestamp bounds staleness, no lease/lock — the unhappy path Mike singled out). Landed `method/CONCURRENCY.md` new section + ROADMAP `[~]` legend + review-owed item + CHANGELOG. **Owed:** cold un-briefed review (no seeded brief authored per REVIEW.md independence; self-authored doctrine → Mike decides); children inherit by pointer, `[~]` legend rides the next pin bump.
<!-- archivecut:log-entry docs/SESSIONS.md 85+1 -->
- [2026-07-13 · addendum: the claiming section reviewed + all seven applied (Opus)](2026-07-13-2226-claiming-work-mechanism.md) — the cold un-briefed pass earned its keep: **PASS-WITH-FINDINGS, 1 MAJOR · 4 MEDIUM · 2 LOW**, and the MAJOR was a real hole — claiming was gated to worktree-mode, whose only reliable trigger is the principal's say-so, i.e. exactly the condition the grounding incident broke, so the mechanism wouldn't have fired in the case it was built for. Mike ruled **all seven [fixed]**; applied same day. The reframe (option A, decouple): claiming now keys on **selection from the shared queue** — solo or parallel — and the claim commit lands on `main` *before* branching (a feature-branch claim is invisible; separate branches' pushes never collide). MEDIUMs folded in: bundled/themed lines are claimed as a unit and *serialise* (fan-out needs per-leaf lines); **adjacent** one-line claims raise a trivial keep-both rebase conflict (reviewer live-verified — "silent everywhere else" was false), so `[~]` goes on the checkbox line and the guarantee is softened; put-away's abandonment gained the `[~]`→`[ ]` reversion; tracker-based adopters pointed at the assignee/in-progress primitive. LOW: timestamp demoted to a staleness tiebreak behind branch-existence. Decisions stamped in the verdict file. **Applied-batch cold pass owed** per the cycle rule (first pass carried a MAJOR).
<!-- archivecut:log-entry docs/SESSIONS.md 86+1 -->
- [2026-07-13 · addendum: applied-batch cold pass — cycle closed, two residuals fixed, shed spillover (Opus)](2026-07-13-2226-claiming-work-mechanism.md) — the cycle rule's owed applied-batch pass RAN un-briefed: **PASS-WITH-FINDINGS, no MAJOR → cycle closes**, all seven confirmed in-text and live-reproduced. Two residuals, Mike ruled **both [fixed]**: a **MEDIUM** the fix-2 reframe opened one layer beneath — "claim on `main`" is right, but git checks `main` out in exactly one place, so a parallel session makes the claim *from the primary checkout before `git worktree add`* (named as the sync-bookend integration landing, with a trigger-section back-reference; separate-clone adopters skip it) — and a **LOW** inherited imprecision (the "three-line diff context" parenthetical was wrong; adjacency = no unchanged line between, a one-line gap rebases clean). Cycle was already closed so no further pass owed. **Shed spillover, same session:** a shed session hit its `validate.py` token-shape guard tripping on a 46-char coordination-free ADR id; diagnosed as **shed's to fix** (its own tool), verified **atelier's own secretscan/leakscan pass these ids clean** (low entropy), and — Mike's call — added a RECORD.md note that ids are long/hyphenated by design so downstream validators/scanners must allow the shape. Claiming-work doctrine now fully reviewed, applied, and closed.


Mike raised a fourth concurrency snag, hit repeatedly across parallel evening
sessions: multiple sessions, each told only "the next thing in the queue",
self-selected the **same** roadmap item and duplicated the work — wasted model
time, and nothing in the tree or the record ever conflicted to flag it. He asked
for a way a session can *claim* a piece of work, open to any efficient method.

## The diagnosis

CONCURRENCY already had a substrate for parallel work (worktrees) and a *trigger*
for knowing you're the second session (say-so / dirty-tree backstop) — but
**selection** was an unguarded coordination point. The failure is the exact
silent-collision class the doc had already beaten *once*, for record identifiers:
a next-N counter let two sessions allocate the same number as two differently
named files, so no git conflict fired. Work-selection was the same shape one rung
up — two sessions, one item, no shared mutation, silent duplication.

## The mechanism (landed, review-owed)

Generalise the fix the record-ID bearing already uses: **force the collision onto
one shared line.** A session claims a roadmap item by editing *that item's own
line, in place* (`[~]` + `(claimed <date>-<HHMM>, wt: <branch>)`), committing and
pushing the claim **before** any work. Same-item double-claim → both edited one
line → trivial same-line rebase conflict → first-to-push wins, loser takes the
next open item. Different items → different lines → no conflict, both proceed.
Resolves exactly at the contested grain, silent elsewhere.

Design points that make it fit rather than bolt on:

- **In-place mutation, never an append-tail claims list** — an appended "who's on
  what" would let two same-item claims land as two lines and go silent, the
  counter mistake reincarnated. Mutating the contested line *is* the design.
- **Worktree-mode only** — fires under the same trigger as the worktree; the solo
  trunk-based default pays nothing.
- **Grain = leaf item, not theme** — two sessions both told "do the reviews" each
  claim a different item and coexist; a themed instruction fans out.
- **Release = put-away** — a claim's life is its branch's life; done → `[x]`,
  abandoned → the existing salvage → tag → delete → record, reverting to `[ ]`.
- **Orphan claims (the unhappy path Mike liked)** — a dead session leaves a `[~]`
  with no live branch: a stale branch wearing a marker, judged the same
  mechanical way, timestamp bounding staleness. No lease timer, no lock server —
  reclaiming is evidence-based judgement, inside the doc's no-locking-machinery
  line.

## Landed

- **`method/CONCURRENCY.md`** — new section *Claiming work — make selection
  collide like naming does*, placed between the coordination-free record-ID
  principle it generalises and *Every branch ends put away* (its release path).
- **`ROADMAP.md`** — `[~]` checkbox legend at the top; review-owed item added.
- **`CHANGELOG.md`** — one Added line under _Unreleased_.

## Owed

- **Cold, un-briefed review** — per REVIEW.md independence, no seeded brief
  authored (the author doesn't set the reviewer's attack surface); self-authored
  doctrine, so findings are Mike's to decide. Tracked under *Doctrine —
  review-owed*.
- Children inherit `method/` by pointer — no propagation edit; the mechanism is
  generic and rides the next pin bump for any child that wants the `[~]` legend
  in its own ROADMAP.
