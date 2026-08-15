# 2026-08-15 · 0610 UTC · The board store migration — research, ruling, and the split (Opus research → Fable build, wt: board-per-item-0815)

Mike's ask, verbatim: *"I want you to look at the issues we have been having
with (a) multiple sessions updating core files like sessions, roadmap etc
concurrently, (b) the size of the files causing concern, (c) work being moved
to the roadmap-done file when the work is not completed and/or marked as
completed in roadmap file. Should we migrate these files to a sqlite database
or something else that better addresses our needs."* Then, after the research:
*"Review this session and challenge everything from both myself and the opus
model to get the best outcome."* Then: *"I accept your recommendation.
Proceed."*

## The research, and the adversarial re-test that reshaped it

First pass (Opus): fleet-wide measurement — record-file sizes across all 24
repos, atelier's git history (968 commits), a transcript sweep (566 sessions).
Verdict: not SQLite; split the grain — the monolithic board was at once the
unit of contention, of reading (~67k tokens at every session open), and of
truth for 100+ independent items.

Second pass (Fable, at Mike's direction): challenge everything. Three evidence
claims **fell**: transcript-hit and commit-density figures read as contention
were mostly measuring the designed hygiene working (the worst "collision hour"
was one orchestrated session's claim/close waves), and the read-cost figure
emerged as the strongest surviving fact. Two design flaws in the first pass's
own recommendation were caught **before build**: a generated *committed* index
recreates the conflict it exists to remove unless conflicts resolve by
regeneration, and `closed_by: <sha>` cannot survive the landing-equals-
bookkeeping rule (a commit cannot cite its own SHA) — provenance moved to the
item file's own `git log` instead. The re-test also surfaced the larger
non-storage bottleneck: ~67 items awaiting Mike's ruling, answered by a weekly
ruling sitting (Mike's process; accepted in the same ruling).

## What landed

- **`8ce1bb7`** — the toolchain: `tools/board.py` (index generator +
  item-file validator, `--selftest`, 14 unit tests), registered as the
  enforced `board` floor check on both planes; `harvestscan` watches the
  board directory (stores may be directories, expanded at the OLD revision so
  a deleted item file is enumerated, not skipped; +3 tests); `pointerscan`
  reads item files by directory and skips the generated index.
- **`a9abc26`** — the migration: all 4,063 lines of `ROADMAP.md` moved — 27
  sections to `docs/roadmap/` directories (narrative verbatim in per-section
  READMEs), 118 items to their own files (checkbox grammar unchanged),
  relative links re-based; `ROADMAP.md` regenerated at 253 lines;
  `ROADMAP-DONE.md` frozen as the pre-split archive.
- **`15d3de2`** — doctrine moved with the mechanism: RECORD.md board section,
  CONCURRENCY.md claiming-on-a-split-board (index conflicts resolve by
  regenerating, the dirty-tree tell moves to the item file), CLAUDE.md read
  order, the board README legend, the ADR
  (`docs/decisions/2026-08-15-0610-board-store-per-item-files.md`) with
  Mike's ruling verbatim and the rejected stores costed.

## Two live defects the build found in its own design, both pinned by tests

1. **One text cannot have correct relative links at two depths.** The first
   index inlined the board preamble; its links were right at
   `docs/roadmap/README.md` and broken at `docs/ROADMAP.md`. The index now
   links the preamble instead of inlining it.
2. **A projection must inherit its source's exemptions.** The generated index
   reproduced a verbatim non-ISO date whose item line carried a scoped
   `datescan:allow` — and the hook's datescan correctly blocked the commit.
   Allow-markers on a state line now travel to the generated line.

## Verification (run, not asserted)

linkscan clean tree-wide after the move; harvestscan clean against HEAD
(every pre-split item survives — the survivor check that exists for exactly
this kind of bulk move); sizescan's long-standing ROADMAP size advisory gone
(SESSIONS +6 advisory pre-dates this work and remains); datescan clean; the
full tool suite green including the floor's 132; every commit passed the full
hook plane including the new `board` check.

## Follow-ups queued (own items, section 010)

The staged-plane seam in `board --check` (HV4's class, stated at birth); the
fleet rollout 🎯 (gated on this cycle's review; order and timing Mike's);
a monolith-era wording sweep. The rule-4 cold pass is queued refs-only in
`050-rule-4-cold-pass-queued.md`; per REVIEW rule 4 this session queues and
stops — it does not spawn its own review.
