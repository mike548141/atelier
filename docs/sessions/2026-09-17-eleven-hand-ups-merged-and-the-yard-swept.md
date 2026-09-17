# 2026-09-17 · Eleven hand-ups merged, and the yard swept

**Session:** Sonnet 5 (VS Code) · integration worktree `at-pr-tidy`, merged to
`main` · 11 PRs landed, 4 worktrees + 6 branches removed, nothing built.

## The ask

Mike: *"I believe there are open PR's to merge, maybe branches or worktrees
to tidy up. Use the right model for the job to best protect the data and
the work to tidy all this up."* The 2026-09-16 entry had already flagged
four unmerged report-branch worktrees and left them untouched — this
sitting picked that up plus everything that had queued behind it.

## What was actually open

11 open PRs (#67–75, #79, #80), all child hand-ups under § *Pointing up*
filing `docs/roadmap/320-child-filed-findings-via-pointing-up/` items; 4 of
them backed by the pre-existing worktrees. `gh pr view` showed 8 of the 11
`CONFLICTING` against `main` — every one on `docs/ROADMAP.md`, the
generated index, never on the item files themselves (each hand-up adds a
brand-new file). A closer read found the real hazard `board.py`'s own
`number_collisions()` check exists to catch: **six item-number collisions**
across the batch — 320/140 and 320/150 each claimed a second time by PR #67
(stale, opened 2026-08-26, before the numbers it copied were taken by later
trunk work), 320/150 claimed a third time by PR #71 and a fourth by PR #75,
320/160 claimed twice (PR #69, PR #72), 320/220 claimed twice (PR #72's
post-renumber slot and PR #74), and 320/240 claimed twice (PR #79, PR #80).
None of this shows up in GitHub's mergeable-state check, which only sees
file-level text conflict — two new files with different names never
conflict there even when their leading numbers collide, which is exactly
the gap `number_collisions()`'s docstring names as "the one surviving
counter."

A local ref `pr76`, unreachable from any branch, carried two further commits
past what PR #76 had merged. Checked before assuming it stranded — `diff`
against the corresponding item on current `main` was **empty**: the content
had already landed by some other route and the ref was just leftover
pointer, not lost work. Deleted, no action needed.

## The merge

One integration worktree (`at-pr-tidy`, off `origin/main`), 11 sequential
`git merge --no-ff` calls in PR-number order, never touching a reporter's
own branch (`CONCURRENCY.md`'s § *Report without harming the parent*: land,
never rebase the reporter). `docs/ROADMAP.md` conflicts resolved the
standing way — regenerate via `board.py rebuild`, never hand-merge. Six
collisions caught by `board.py check` after each merge, each resolved by
moving the **later-landing** item to the section's next free number (none
had inbound references yet, so PRINCIPLES.md §10's tie-break was moot) —
320/210, 220, 240→260, 270, 280, 290 assigned this way, all recorded in
their own commit messages. Full CI-plane floor (`floor.py --plane ci`)
green, 261/261 node tests, Python `unittest discover` green, before any
push. Pushed as a fast-forward (`origin/main` was an ancestor throughout —
no one else moved trunk during the sitting); GitHub auto-closed all 11 PRs
on the push and deleted their remote branches. **Confirmed on the pushed
floor, not the local one** — `gh run watch` on the resulting Actions run,
green, per `ENV-GATED-TEST-FAILURES`'s rule that the local scan is never the
all-clear.

## The sweep

4 worktrees removed (`at-handup-320-140`, `at-handup-actcompleted`,
`at-handup-autostash`, `at-handup-conflictscan`) once their branches were
merged; local branches for all 11 PRs plus the stale `pr76` ref plus
`feat/ccmail-delegation` (already merged as PR #78, remote long gone)
deleted. Primary checkout fast-forwarded to the new `main`. Zero open PRs,
zero stray worktrees, zero stray branches at close.

## Model choice

Ran as one careful sequential pass in the primary session (Sonnet 5) rather
than fanning the eight conflicting PRs out to parallel agents — they all
write the same generated index and the same section's number space, so
parallel workers would have recreated the exact collision class this
sitting exists to catch, or clashed with each other resolving it. The
judgement-heavy step — deciding a renumber is safe and where it lands — ran
inline against `board.py`'s own check after every single merge, never
batched, so the collision that would have shipped silently on a bulk apply
was structurally impossible here.
