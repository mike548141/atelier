# Deferred reading for `2026-11-09-0153-exception-register-redraft-cold.md`

Open only after your act-1 findings are committed (`docs/method/REVIEW.md` rule 1). Fold into the
brief below the reconcile, then delete this file. A floor, never a fence.

## The queue pointer's questions (the author's framing, verbatim)

> whether the both-forms transition really keeps every child green; whether the provenance record
can be forged cheaply; whether XR1–XR16 are each closed as claimed.

## The brief-writer's questions

1. Reworking to the central shape after a redraft: did any answer to a prior finding depend on the
in-place shape the rework dropped?
2. Union merge on an append-only file: what happens to two grants that conflict, and to a removal?
3. Where does a child's existing marker read differently under the register than under today's
reader during the both-forms period?

## What the brief-writer held back

- The pointer said the pass was best run after the four questions were answered. They now are
  (`160/650`; ADR § *Open questions for Mike*), so that condition is met.
- The rework went against the option recommended to the principal on Q1; the design's reasoning and
  the costs in § 8 were written after that choice.

## Re-run results (2026-11-09 UTC, at `457615cc`)

`floorfleet --json`: exit 0; 23 rows, 1 parent, 21 wired children, 1 absent. `floor.py --plane ci`:
exit 0. **Not run by the brief-writer:** re-deriving the figures in the ADR's § *What exists,
measured*.

