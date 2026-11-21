# 2026-11-20 · 0915 UTC — A drain ranks and routes the whole queue first

**From the retired session log**, word for word; only its link paths were re-pointed for this folder:

<!-- archivecut:log-entry docs/SESSIONS.md 370+1 -->
- [2026-11-20 · 0915 UTC · A drain ranks and routes the whole queue first (Opus 5.5, principal-opened)](2026-11-20-0915-drain-ranks-and-routes.md) — `ccfleet drain` requires `queue.ranked`; review-drain skill section; cold pass queued as `160/1660`, no brief


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

## 2026-11-21: "cheapest" means the budget that lapses first

- The principal clarified the routing: a budget or credit lost at a set time
  goes first when that time is near; the aim is the most benefit from the whole
  spend, and no budget is free. His words stay private (the figures in them
  are financial); the skill carries a paraphrase.
- `skills/review-drain/SKILL.md` § *Rank and route*: routes order by lapse time,
  cost breaking a tie; the seal needs each open budget's lapse; the local route
  never takes from a budget lapsing sooner. The adopter's queue tool got the
  same change in the private estate root.
- `160/1450` carries a delta note (its brief-writer, queue run 08cd3b95, told);
  `160/1660` still folds into it.
