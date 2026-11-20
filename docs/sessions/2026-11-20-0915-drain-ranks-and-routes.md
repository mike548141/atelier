# 2026-11-20 · 0915 UTC — A drain ranks and routes the whole queue first

**Session:** `64f984ac`, Claude Opus 5.5, principal-opened in the VS Code extension.
No review-tier model used; no review run. Peers live at open: queue run `08cd3b95` on
this repo's primary checkout (its uncommitted `leakscan` work left untouched; this
session worked in its own worktree).

## What was asked

The principal, verbatim (the first message; the second, on routing to the cheapest
route that reaches local quality, is summarised in the skill because it carries
account detail): *"when I run fable drain or its equivalent, and similar
code/skills/whatever that get fable reviews completed like using Agent SDK or Batch API
it should first look at all the reviews in all the repos to priortise the highest
priority ones based on either my direction or the reviews importance, urgency, and the
risks it mitigates or value of work it unlocks. Make sure that is built into them so it
happens everytime I run it"*.

## What changed here

- `instruments/ccfleet`: `drain` requires `queue.ranked` and calls it before the first
  pick; nonzero starts nothing. Two tests; suite 42 OK. Man page and example config.
- `skills/review-drain/SKILL.md`: § *Rank and route the whole queue first*, generic.
- The ranking itself (evidence, seal, routes, lanes) is the adopter's queue's, built in
  the private estate root's queue tool the same session; nothing of it is named here.

## Owed

- `160/1660`: the rule-4 cold pass over this delta. Needs a brief; Fable-gated.
