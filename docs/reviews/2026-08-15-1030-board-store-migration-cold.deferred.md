# Deferred — the board store migration cold pass

*Sibling of `2026-08-15-1030-board-store-migration-cold.md`. Open only after
the reviewer's own findings are durably written (REVIEW.md rule 1). Fold in
below the verdict and delete this file when the verdict lands.*

## References withheld from the brief

- **Intent record:** `docs/sessions/2026-08-15-0610-board-store-migration.md`
  (and its one-line entry in `docs/SESSIONS.md`).
- **The queue pointer:**
  `docs/roadmap/010-board-store-migration-per-item-files-mik/050-rule-4-cold-pass-queued.md`.
- **Related open items in the same section** (the author's own follow-ups —
  read as the author's account, not as settled scope): `020-board-check-staged-plane-seam.md`,
  `030-fleet-rollout-of-the-split-board.md`, `040-monolith-era-wording-sweep.md`.
- **Prior verdicts on neighbouring surfaces** — reconcile only, never anchor:
  `docs/reviews/2026-07-29-1306-b4-harvestscan-cold.md` (harvestscan),
  `docs/reviews/2026-08-05-1238-pointer-grammar-b4-wiring-cold.md`
  (pointerscan), `docs/reviews/2026-07-19-0407-review-trigger-sizescan-combined-cold.md`
  (sizescan's harvest gate, which the split retires in part).

## The brief-writer's seeded questions

Written by a non-author cold session from the delta alone. A floor, never a
fence — the reviewer's own findings come first.

1. **Index flags are derived from the raw first line, code spans included.**
   `board.py`'s `index_line` collects any glyph in `FLAGS` that appears in the
   item's first line. Item `130-…/010-…` opens with a `⏳` inside backticks
   and renders in the index as `⏳🔎` — a non-pointer item wearing the queue
   glyph in the file a taker greps first. `pointerscan` strips code spans for
   exactly this reason. Is this a defect in the projection, and does it
   recreate the stale-pointer trap the 130 item itself describes?
2. **Migration fidelity.** The claim is 4,063 lines → 27 sections / 118 items.
   Diff the pre-migration `docs/ROADMAP.md` (parent of `a9abc26`) against the
   concatenated store: is any line, allow-marker, or nested sub-bullet lost,
   re-parented, or de-indented? Nested sub-bullets under a pointer (the shape
   `160-…/080` and `090` carry) are the likeliest casualty.
3. **`--check` reads the worktree, not the staged plane.** The author records
   this as a stated residual and a follow-up item. Can a commit land with a
   stale index through the hook plane, and does the ci plane catch it? Probe
   it, do not read it.
4. **The GENERATED marker as a skip key.** Scanners skip any file carrying the
   marker line. Could an item file, or any other prose file, carry that line
   and thereby escape `pointerscan`? Is the marker matched on line 1 only?
5. **Doctrine drift left behind.** RECORD.md and CONCURRENCY.md moved with the
   mechanism; the author's own follow-up names a monolith-era wording sweep
   still owed. Which surfaces still tell a session to edit `ROADMAP.md`
   directly (REVIEW.md rule 4's pointer wording, skills, templates, children's
   floor blocks), and does any of them now instruct a breach of the `board`
   check?
6. **The harvest step retired.** With `[x]` flipped in place and no harvest,
   what now stops a section from accreting closed items and their narrative
   forever? Does `sizescan`'s cold-content gate still fire on a `[x]` inside
   an item file, or only on the (now never-`[x]`) index?
7. **Children.** The check reports not-in-scope where `docs/roadmap/` is
   absent. Is that honest for a child that adopts the split half-way — a
   `docs/roadmap/` directory present but a hand-kept `ROADMAP.md`?
