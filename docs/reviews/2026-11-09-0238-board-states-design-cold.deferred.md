# Held back — the board-states design

Opened only once the reviewer's own findings are durably written (`REVIEW.md` rule 1). A floor,
never a fence. Written by the brief-writer, session `9bb1b984`, which did not author the delta.

## The pointer's own questions

1. Does the migration keep every child green?
2. Do the measurements support the model?

## The brief-writer's questions

3. "Additive" rests on children reading atelier's tools at `floor.yml@main`. What about the local
   hook's copy, a child with an older checkout of atelier, or a `[-]` written while a sibling
   session's tools predate step 1? `board --check` exits 1 on an unknown box: is there a window in
   which a new box reds a run?
4. Step 1 says "nothing renders differently". The rendering table gives `[/]`, `[-]` and a waiting
   field new index text. Which step actually changes the index, and does that stale a committed
   index in a child that takes a tool update and no item change?
5. A longer index-line prefix (`- [ ] ⏸️ him`, a roll-up count): does it still fit `wrapscan`'s
   width, and `sizescan`'s hot-path rules?
6. The design says the table's samples are "not extrapolated". Problem 3 says "about half … is not
   takeable", and the outcome rests on it. Is that extrapolation?
7. Problem 2 is a house-wide claim on `[~]`. The table says 35 of the 36 non-claim `[~]` sit in one
   child. Is that a state vocabulary problem or one child's habit?
8. The census shows `⏳` as a first-line state 8 times and on 162 open items' state lines. Reconcile
   the two counts: what is the 162 counting that the 8 is not?
9. 1,245 + 1,189 + 52 + 8 = 2,494 and 1,189 − 45 = 1,144. Those two add up. Do the other figures
   survive a fresh census at a fresh date, and how much have the boards moved?
10. The design departs from his two-tier words on "mixed", and says so "plainly". It is not among the
    three questions put to him. Should it be? Are the three questions the ones that are really his?
11. "Who may set what": `[-] not-required` is "Mike only" on "work Mike commissioned". How does a
    session or a check know which work that is, across 2,494 items that do not record it?
12. A parent is "declared and checked". What stops a parent simply not declaring its children? Does
    the check catch the absence, or only a contradiction in a declaration that exists?
13. `(waiting: <repo>)`, `[-] moved to X` and the roll-up put a repo name on a public index line.
    What does `RECORD.md` § *The record is public* say about a private repo's name beside its
    state, and does the design's grammar invite exactly that join in a public tree?
14. Phase 2's grace is tied to `010/190` and 2026-11-18. Is that date realistic given this draft is
    not ruled, and what happens to two graces if it slips?
15. Rejected shape C cites a 2026-08-15 store decision. Does `(waiting: …)` plus `children:` plus the
    tier-2 word amount to the second state vocabulary that decision refused, on the item's first line
    rather than in frontmatter?

## Facts held back

- **Re-run lines, 2026-11-09 UTC, run from the worktree root (the `cd tools` line from `tools/`).**
  `python3` was 3.14.6. `board.py --check --root .` exit 0; `test_board` exit 0.
- The brief-writer confirmed `STATE_RE` is in `tools/board.py`, `_MARKER` in `tools/pointerscan.py`,
  `ITEM_RE` in `tools/harvestscan.py`, `_COLD_ITEM` and `_LIVE_ITEM` in `tools/sizescan.py`, and
  `ITEM_STATE`/`STATE_LINE`/`CLAIM_LINE` names in `instruments/ccclose`. It did not test what each
  does. It re-ran no census and no transcript search.
