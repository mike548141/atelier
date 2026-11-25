---
action: plan
description: Show the review queue before anything runs — every owed review, briefed or not, ranked, routed to the cheapest budget that still matches a local pass, with its estimated cost; runs, seals and claims nothing. review run and review brief start from it.
argument-hint: "[the principal's words for the next run, if any]"
---

# Review — plan

Show the principal the review queue before anything runs: what is owed, in
what order, by which route, at what cost, and what would not fit. Run nothing.

His words, 2026-11-24, verbatim, commissioning it (board `180/210`): *"consider
a plan mode … to prep for a drain but not run the reviews i.e. it finds them,
prioritises them, shows me a queue of work, estimated budget/API spend, what
reviews will route to local vs Batch API vs Agent SDK etc"*. And on where the
logic lives, verbatim: *"I would put all the logic in /atelier:review-plan and
then have /atelier:review-drain call review-plan when it starts a drain.
Similarly I would look at any other commands that require similar logic like
ccfleet drain --dry-run and consolidate the logic into one. Essentially the
logic is a module of code that can be re-used and not repeated."* (He then
ruled the space form, `/atelier:review plan` and `/atelier:review run`,
board `450/020`.) And, verbatim: *"Also I think /atelier:review brief should
use /atelier:review plan to find the work that requires a brief to be
written"*.

## One finder, three callers

This file is the one home of the method. Nothing else ranks, routes or finds
owed reviews; a second copy is a defect to fold back in here.

| Caller | What it takes from the plan |
|---|---|
| `/atelier:review run` | the briefed rows, in rank order; it seals them with the principal's words for its run, then drains |
| `/atelier:review brief` (no subject named) | the owed-but-unbriefed list; it writes those briefs |
| `ccfleet drain --dry-run` | `ccfleet plan`'s reading, printed before the rehearsed launches |

**Where each half lives** (the build's design call, made once, 2026-11-24):

- **The code half reads; it never judges.** `ccfleet plan` (`ccfleet --doc`)
  calls the adopter's queue read-only (`queue.evidence`, and `queue.owed`
  when the adopter has one) and reads ccfleet's own past pass logs for
  measured cost. It prints the evidence, the routes each review fits, and the
  cost history. It never calls `seal`, `take`, `ranked` or `next`, so a
  rehearsal cannot touch the real run.
- **The judgement half is this file.** An agent (you) reads that evidence and
  ranks and routes it, by the rules below. The adopter's queue holds the
  seal: `review run` hands it the ranking this plan made.
- An adopter with no ccfleet config (one repo, no estate) reads the same
  evidence by hand: the board items whose own text says a review is owed, and
  `docs/reviews/` for each one's brief and its `.deferred.md` sibling.

## The steps

Read-only from start to finish: no claim, no worktree, no session started, no
commit, no seal. A plan is never a seal.

1. **Read every owed review, briefed or not**, in every repo: `ccfleet plan
   --json` where a config exists (add `--fetch` to read each repo's remote
   first). For each, what the judge needs: the item, its age, the principal's
   words on it, dates ahead, what it guards, what waits on its verdict, and
   what each route can and cannot do for it. A review is **owed** when its
   item carries a review pointer (REVIEW.md rule 4: a `⏳` that names the
   delta to review and its intent record is the queue entry, and any spawner
   passing the criterion may take it and brief it), or when its item's own
   text, or the principal's words on it, says one is required. A `⏳` that
   names no delta (a wait on something other than a review), REVIEW.md's
   triggers met by work nobody has pointed, and a writer's view that something
   deserves a review do not make one owed: those are **review candidates**,
   which go to the principal as a list (step 5), never into a brief. An owed
   review with no brief goes on the unbriefed list (step 5), never into the
   ranking. Where the adopter's `queue.owed` finds the owed reviews, it applies
   this definition; a difference between the two is a defect to report, and
   this file governs until it is fixed.
2. **Rank the briefed ones by judgement.** The principal's direction first
   (his words for the next run, if given after the command, then standing
   words on an item); then importance, urgency (a real date first), the risk
   the review mitigates (credentials, public exposure, live or irreversible
   paths, money) and the value of the work it unlocks; a pass whose core needs
   a live write last; a standing repo order breaks ties only.
3. **Route each one**, among the routes the principal has opened, only to a
   route that reaches local quality. When a budget's lapse is near, the route
   drawing the budget that lapses soonest goes first. When no lapse is near,
   the cheapest capable route goes first (a batch route where the review fits,
   then a credit route, then the included budget). Cost per review breaks any
   remaining tie. This file fixes no threshold for "near": the plan says, per
   budget, whether its lapse counts as near and why. "Near" is judged per run,
   so a route shown here is a forecast for a run started now: the run that
   drains them re-plans, and its own plan says where each review goes. A
   review needing probes
   or re-run lines does not fit a single-request batch route; one needing
   tools only the local session has fits only local. **Unsure means the local
   route**: quality is never traded for price or for a lapse.
4. **Estimate each one's cost** from measured past passes on that route,
   never invented: `ccfleet plan`'s history (or the adopter's own lane
   records). It gives the median and maximum per completed pass, all its
   sessions summed with the reviewer subagent included, pooled, per repo and
   per model. It has no measure of a review's size, so the estimate is the
   route's figure, or the repo's, and says which; a review you judge larger
   than most is said so in words beside it, never priced up. The figure is
   the CLI's list price: on a subscription plan it is notional, not money
   spent, so a column that mixes a plan route with a paid one says which is
   which. With no measurement for a route, the row says "no measurement"
   rather than a guess.
5. **Show it**, as a table in the reply (the principal's pick, 2026-11-24,
   verbatim: *"a table in the reply"*):

   | # | The review | Why it ranks here | Route, and why not a cheaper one | Est. cost |
   |---|---|---|---|---|

   "The review" is plain words: what it checks and what it guards, never a
   bare item id. Then, per budget: the total routed to it, what it has left,
   when it lapses, and what would not fit. Then the **owed, not yet briefed**
   list: what each guards and why it is owed. Then the **review candidates**
   from step 1: what each is, why it might deserve a review, and that it waits
   on the principal's word before anyone briefs it (or "none").

What the principal changes in the plan (a reorder, a hold, a forced route) is
his words for the next run. `review run` quotes them into its seal; the run
still re-ranks afresh, because a seal lasts one run.

## Where the ranking rules come from

The principal, 2026-11-20, verbatim, in part: *"… it should first look at all
the reviews in all the repos to priortise the highest priority ones based on
either my direction or the reviews importance, urgency, and the risks it
mitigates or value of work it unlocks. Make sure that is built into them so it
happens everytime I run it"*.

Steps 2 and 3 beyond those words are this file's paraphrase of his later
words, not his words and not a ruling; an adopter's own principal's words,
kept in the rulings file, govern their estate. Each review goes to the
cheapest route that still produces a review of the same standard as a local
pass. "Cheapest" weighs the whole spend, not one job: a budget or credit lost
at a set time is spent first when that time is near, and no budget is free (a
subscription pays for the included ones).
