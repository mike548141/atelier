# Held back — do not open before your findings are durably written

Sibling of `docs/reviews/2026-11-09-0126-ccclose-board-order-cold.md` (`REVIEW.md` rule 1). Written
2026-11-09 UTC by session `84e3aa7f`, the brief-writer, which authored none of the delta. Open this
only after act 1 is committed. Everything here is a floor, never a fence, and none of it is a
finding.

## The brief-writer's own questions

1. Does `localeCompare` with `numeric: true` agree with `board.py`'s key on leading zeros (`010/200`
against `10/200`) and on ties? Run both on the same list.
2. Is `sorted` the only place the board lists are ordered? Look for another text sort of ids in
`ccclose` and its siblings.
3. The new test calls the comparator directly. Does anything pin the order through the printed
block?

## What the brief-writer ran, and what it got

- `ccclose`: Node 24: 105 tests, 105 pass, 0 fail, 284 s under load.
