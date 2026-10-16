# Deferred sibling — one unambiguous review-pointer state

**Held under rule 1's split** (`docs/method/REVIEW.md`). Open only after your
phase-1 findings are committed to the brief
`docs/reviews/2026-10-16-1550-queued-glyph-state-cold.md`. At verdict, fold this
file in below your reconcile and delete it.

Written 2026-10-16 UTC by the Opus brief-writer named in the brief, which authored
none of the delta and forms no finding: the questions below are seeds, a floor
and never a fence.

## Intent record

- `docs/sessions/2026-10-05-1120-queue-run-closes-and-builds.md` — **not opened
  by the brief-writer**.

## Prior verdicts on the same surfaces (named, not opened)

Path greps over `docs/reviews/` for `tools/pointerscan` and `tools/board.py` name
these; none was opened by the brief-writer:

- `docs/reviews/2026-08-05-1238-pointer-grammar-b4-wiring-cold.md`
- `docs/reviews/2026-08-15-1030-board-store-migration-cold.md`
- `docs/reviews/2026-08-17-0730-board-generator-child-truth-cold.md`
- `docs/reviews/2026-08-17-1321-bs1-wording-cold.md`
- `docs/reviews/2026-08-21-0820-pointing-up-cold.md`
- `docs/reviews/2026-09-25-0715-0918-registry-code-cold.md`
- `docs/reviews/2026-09-25-0715-bw-rulings-applied-cold.md`
- `docs/reviews/2026-09-25-0715-linked-worktree-skip-cold.md`
- `docs/reviews/2026-09-25-0715-staged-plane-check-cold.md`
- `docs/reviews/2026-09-25-0715-tier-ruling-cold.md`

Plus, for the phase-2 state-line check, the verdict of each of the sixteen items
`b02c56d` rewrote (found from each item's own links).

## The pointer's own lens hints

None. The pointer is refs-only (delta, intent record, tier, pass type).

## Seeded questions

1. **Two shapes, one count.** The legend says the queue is "the count of `⏳`
   state lines — the index's `- ⏳` lines". At HEAD the generated index carries
   queued pointers in two shapes: `- ⏳ [` (the glyph as the marker) and
   `- [ ] ⏳ [` (an open box with the glyph as a flag). This pass's own pointer
   and 160/680's wear the second shape. A brief-writer's grep on 2026-10-16 found
   12 of the first and 17 of the second. Does a session following the legend's
   words count only the first, and miss most of the queue — the very miscount the
   delta set out to end?
2. `board.py` maps `⏳` as a marker and also lifts it as a flag; `pointerscan`'s
   `queued_state` accepts it as the marker or in the state prefix. Do the
   generator, the scanner and the legend agree on what a queued pointer is?
3. `_LANDED` keys on an upper-case `RAN` and a few cycle phrasings. The house's
   own close stamps vary. How many real landed pointers in history would it miss,
   and is the "exactly 27, no other" measurement evidence of precision, or a
   pattern fitted to the one incident it was built from?
4. The detector is warn-only, while its subject is an obligation (an owed review)
   whose miss the legend says it exists to prevent. Is warn-only the right tier,
   given `board` itself is enforced?
5. The commit says the index change makes one child's enforced board check
   "read stale until that child rebuilds its index" — a red in a child the
   author did not touch. Was that red held for the principal, as the fleet
   blast-radius practice asks, or shipped?
6. 🛑 became 🎯 on thirteen items "whose record says the findings are the
   principal's to decide". Is a decision mark on an open review the same as an
   owed ruling, and does the legend's "eye-flags are never state" leave a session
   any way to find the ruling queue?
