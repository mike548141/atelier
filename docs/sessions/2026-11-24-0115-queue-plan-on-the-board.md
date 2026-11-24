# 2026-11-24 01:15 UTC — A plan mode for drains, put on the board

**Session:** `edf25bd3` (messaging name `atelier-75`), Claude Opus 5.5,
principal-opened in the VS Code extension. Primary checkout, clean, one
commit; no workers.

## What was asked

The principal, verbatim: *"consider a plan mode for /atelier:queue-run to
prep for a drain but not run the reviews i.e. it finds them, prioritises
them, shows me a queue of work, estimated budget/API spend, what reviews
will route to local vs Batch API vs Agent SDK etc"* · *"It could be
atelier:queue-plan as a command"*, then mid-turn: *"Put it on the board"*,
and after the filing: *"Sorry I quoted the wrong command name there I was
thinking of /atelier:review-drain not queue-run"*. The item was amended to
say so. Then, verbatim: *"So it would be /atelier:review-plan as a new
command. Tell me if theres a better idea or way"*. Recommended: keep the
name, as a thin command over a new plan mode in `review-drain`, and have
a real drain print the same table at its start. Then he turned it around, verbatim (in part): *"I would put all the logic
in /atelier:review-plan and then have /atelier:review-drain call
review-plan when it starts a drain"*, and consolidate copies such as
`ccfleet drain --dry-run` into one reusable module. Recorded in the item,
with the four places the logic lives today, found by grep. Last, verbatim:
*"We should consider renaming /atelier:review-drain to /atelier:review-run
as well to get some consistency across the commands"*. Recommended yes, in
the same build; sized and recorded in the item. Then he offered a space
instead of a hyphen; asked in the device (hyphen recommended), he ruled,
verbatim: *"I think a space and for the default it could have a menu or
help screen a little like what /atelier does by itself. We should make all
the atelier command like this so its consistent"*. Filed as board
`450/020`; `180/210` points to it.

## What was done

Read `review-drain` § *Rank and route the whole queue first* and `ccfleet`'s
`--dry-run`: the ranking exists only inside a real drain, and the dry run
skips it. Filed board `180/210` with that gap and a shape to consider (reuse
the drain's rank-and-route steps unchanged, stop before the seal, one table
with route and estimated cost per review, estimates from measured passes
only, his edits carried as words for the next run). Nothing built.

## Left open

`180/210` itself, with questions for the build session to settle
with him: none left (page form, his answer: *"a table in the reply"*); and
`450/020`, whose mapping of today's commands
waits for his confirmation before anything moves. Asked whether retiring
the user-level drain command is on the board: it is, `450/010` row 2
(cleared by him 2026-11-18, waiting on a clean `160/1450` re-check); both
items now cross-link to the new target.
On the four single-action commands, his pick: *"Group them
(Recommended)"* (`repo scan`, `repo hook`, `repo create`, `session
onramp`); recorded in `450/020`. He agreed the word "drain" stays in the
description, asked what "second copy" meant (it was the wrong word: a
forwarder holds no copy), and on old names picked *"Nothing"* over a
forwarder or the signpost recommended. Recorded in both items. Later he restated
his reason for the space form, thinking the first telling was lost; it had
arrived as his typed answer in the question dialog. The restatement is
added to `450/020` verbatim. At the close, verbatim: *"Also I want you to carry on with design and build in a fresh session, not wait until the fable review is done"*. Recorded on `180/210` and `450/010`. Then, verbatim: *"Also I think /atelier:review brief should use
/atelier:review plan to find the work that requires a brief to be
written"*; recorded on `180/210`. At the close he asked which Fable passes he had
already approved in this area (three: atelier `160/1450` re-check, and two
in a private repo); asked what the `160/1450` one should review, his pick: *"Wait, review the new build (Recommended)"*. Recorded on `210/470`, `180/210`, `450/010`.
