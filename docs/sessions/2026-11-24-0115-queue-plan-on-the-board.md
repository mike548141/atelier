# 2026-11-24 01:15 UTC — A plan mode for drains, put on the board

**Session:** `edf25bd3` (messaging name `atelier-75`), Claude Opus 5.5,
principal-opened in the VS Code extension. Primary checkout, clean, one
commit; no workers.

## What was asked

The principal, verbatim: *"consider a plan mode for /atelier:queue-run to
prep for a drain but not run the reviews i.e. it finds them, prioritises
them, shows me a queue of work, estimated budget/API spend, what reviews
will route to local vs Batch API vs Agent SDK etc"* · *"It could be
atelier:queue-plan as a command"*, then mid-turn: *"Put it on the board"*.

## What was done

Read `review-drain` § *Rank and route the whole queue first* and `ccfleet`'s
`--dry-run`: the ranking exists only inside a real drain, and the dry run
skips it. Filed board `180/210` with that gap and a shape to consider (reuse
the drain's rank-and-route steps unchanged, stop before the seal, one table
with route and estimated cost per review, estimates from measured passes
only, his edits carried as words for the next run). Nothing built.

## Left open

`180/210` itself, including two questions for the build session to settle
with him: whether the plan also lists non-review queue items, and its page
form.
