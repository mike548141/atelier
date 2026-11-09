# Held back — do not open before your findings are durably written

Sibling of `docs/reviews/2026-11-09-0126-ccclose-loop-worktrees-cold.md` (`REVIEW.md` rule 1).
Written 2026-11-09 UTC by session `84e3aa7f`, the brief-writer, which authored none of the delta.
Open this only after act 1 is committed. Everything here is a floor, never a fence, and none of it
is a finding.

## The brief-writer's own questions

1. `LOOP_CLOSE` and `LOOP_OPEN` are text patterns over the whole command: what do `git commit -m
"all done"`, `echo for you`, a heredoc body or a quoted word do to the depth count? Which direction
is the error: a false listing or a false drop?
2. A command that adds one worktree per word and fails on one of them: `resolvePending` works from
the whole command's result. Is an add that failed listed as made?
3. `break`, `continue` or an `if` guard in the loop body: is the add listed once per word although
the real loop did not run it for every word?
4. Nested literal loops multiply: is there a bound on the product, and what does a long word list
cost?
5. `dropped` counts a site once though several of its expansions may be dropped. What unit is "N
worktree adds", and does it match what the sentence tells the reader?
6. `site.includes(wtPath)` silently de-duplicates. Is that right when two words resolve to one path?
7. The operator precedence of `br === null && branch !== null` inside the `||` chain, and the case
of a positional commit-ish holding an unknown variable.

## What the brief-writer ran, and what it got

- `ccclose`: Node 24: 105 tests, 105 pass, 0 fail, 284 s under load.
