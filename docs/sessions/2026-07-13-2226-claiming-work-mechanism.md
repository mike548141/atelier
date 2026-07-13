# 2026-07-13 · 22:26 — claiming work: making selection collide like naming does (Opus)

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
