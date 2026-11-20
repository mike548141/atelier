# <name> roadmap — the board

**One file per item.** Each item lives in `<NNN>-<section>/<NNN>-<slug>.md`:
its checkbox line first, detail beneath, its own `git log` as provenance (which
commit flipped its state, and what work that commit carried). Each section's
narrative lives in that section's `README.md`. [`../ROADMAP.md`](../ROADMAP.md)
is the **generated index** and is never hand-edited: it is what a session reads
at open, so keep the item lines lean and the detail in the item file.

**After any state change or new item, regenerate the index in the same commit:**

```sh
python3 "${ATELIER_TOOLS:-$(git config hooks.atelierTools)}"/board.py --rebuild
```

The `board` floor check blocks a commit whose index is stale. After a merge
conflict on the index, rebuilding *is* the resolution.

**The index shows what is owed, not what is done.** It opens with a summary
table, one row per section, counting open `[ ]`, claimed `[~]`, `🎯` (waiting
on the principal) and `⏳` (review queued) items. Beneath it, each section that
still owes work lists only its unfinished items; a section with nothing owed
keeps its table row, marked `✅`, and nothing else. A finished item stays in its
own file, one click from its section's narrative. There is no archive file to
move it to.

## Checkbox states

A **work-owed tri-state**, never a disposition:

- `[ ]` work still owed.
- `[~]` **claimed** by a live parallel session: `(claimed <date>-<HHMM>, wt:
  <branch>)`. Do not start a `[~]` item; take the next open one.
- `[x]` **no more work owed**: delivered, superseded or declined, with the
  disposition said in the item's own dated note, never a fourth bracket.
- `⏳` **review queued** for a non-author to take. It means one thing: a review
  is queued and its pass has not returned a verdict. The commit that lands the
  verdict takes the `⏳` off, in the item's own file.
- `🎯` on a state line marks a decision that is the principal's to make. It is
  an eye-flag, never state: the bracket alone is the state.

A `[x]` flips **in the item's own file, in the commit that finishes the work**.
An inline claim (`wt: none`) closes in the commit that lands its work.

## Adding work

- A new item is a new file in the right section folder, numbered
  coordination-free (the next free number in that folder; the `board` check
  reports a collision). A new section is a new `<NNN>-<slug>/` folder with its
  own `README.md`, whose first heading is the section's title in the index.
- An item that records **design or direction** (a chosen approach, a scoped
  feature, a decision that forecloses alternatives) carries a review line:
  `review: queued (docs/reviews/<file>)` or `review: not warranted — <grounds>`.
  Plain work items don't.

The full legend, the review-pointer rules and the claim protocol are atelier's:
its `docs/roadmap/README.md` and `docs/method/RECORD.md` § *The roadmap*.
