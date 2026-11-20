# <name> roadmap

Tick items as work lands. Keep this file honest — it's the cross-session
memory of what's actually left — and lean: it's read at every session
start. Once the board splits to one file per item (`tools/board.py`),
a done item stays in its own file as `[x]`; there is no archive file
to move it to.

Checkbox states are a **work-owed tri-state**: `[ ]` work still owed ·
`[~]` claimed/underway · `[x]` no more work owed — delivered, superseded,
or declined, with the disposition in the item's own dated note (the
harvest-integrity gate holds archive stores to finished-state items only —
a live `[ ]`/`[~]`/`⏳` item there reds the floor).

An entry that records **design or direction** (a chosen approach, a scoped
feature, a decision that forecloses alternatives) carries a review line —
`review: queued (docs/reviews/<file>)` or `review: not warranted — <grounds>`
(atelier `method/REVIEW.md`: omission is the bug). Plain work items don't.

## Now / next

- [ ] <the next real thing>

## Backlog

- [ ] <later>
