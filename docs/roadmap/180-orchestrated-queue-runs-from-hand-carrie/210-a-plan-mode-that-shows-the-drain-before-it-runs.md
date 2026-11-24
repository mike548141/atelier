- [ ] 💡 **A plan mode, `/atelier:queue-plan`: show the principal the drain
      before it runs, and run nothing.** Commissioned 2026-11-24 ~01:15Z, his
      words, verbatim: *"consider a plan mode for /atelier:queue-run to prep
      for a drain but not run the reviews i.e. it finds them, prioritises them,
      shows me a queue of work, estimated budget/API spend, what reviews will
      route to local vs Batch API vs Agent SDK etc"* · *"It could be
      atelier:queue-plan as a command"* · *"Put it on the board"*. Then,
      verbatim: *"Sorry I quoted the wrong command name there I was thinking
      of /atelier:review-drain not queue-run"*. So it is a plan mode for
      `review-drain`; reviews only.
      **What exists, and the gap.** `review-drain` § *Rank and route the whole
      queue first* already reads every briefed review, ranks it, routes it and
      seals the result, but only as step 1 of a real drain: the ranking is
      made, sealed and spent inside the run, and the principal sees it only
      afterwards. `ccfleet drain --dry-run` prints launches but does not call
      `queue.ranked` (the skill says so), so it shows neither the ranking nor
      the routes nor any cost. Nothing gives him the queue, the routes and the
      spend ahead of time, when he decides whether to order a drain, how big,
      and whether to release the month's credit.
      **Shape to consider.**
      1. Run the drain's own rank-and-route steps 1–3 unchanged (one method,
         never a second ranking that drifts from the real one), and stop
         before the seal: a plan is never a seal, and seals nothing.
      2. Show one table, in rank order: the review in plain words (what it
         is and what it guards, no bare ids), why it ranks where it does, the
         route (local plan budget · Batch API · Agent SDK on credit) and why
         not a cheaper one, and its estimated cost. Then a total per budget
         against what each has left and when it lapses, and what would not
         fit.
      3. Estimates come from measured past passes per route and review size,
         never invented (`ground numeric limits`); with no history for a
         route it says "no measurement" rather than guess.
      4. The principal's changes to the plan (reorder, hold, force a route)
         are his words for the next run and the drain's seal records them;
         the drain still re-ranks afresh, as a seal lasts one run.
      5. Lives under the plugin's prefix as a command over `review-drain`
         (450/010's one-home rule). Read-only: no claims, no worktrees, no
         sessions started.
      **Open, for the build session to settle with him, not here:** the
      command's name (his `queue-plan` was said of `queue-run`; something
      like `review-plan`, or a `plan` mode of `review-drain`, may now fit
      better) and the page form (reply table or a page in his browser).
