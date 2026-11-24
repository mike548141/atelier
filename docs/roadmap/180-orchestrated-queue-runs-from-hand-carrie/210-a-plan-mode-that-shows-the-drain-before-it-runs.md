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
      **Name, his words, 2026-11-24, verbatim:** *"So it would be
      /atelier:review-plan as a new command. Tell me if theres a better idea
      or way"*. Recommended to him the same turn: a thin `review-plan`
      command over a new plan mode inside `review-drain`. **He turned it
      around, verbatim:** *"I agree but I would turn it around. I would put
      all the logic in /atelier:review-plan and then have
      /atelier:review-drain call review-plan when it starts a drain.
      Similarly I would look at any other commands that require similar
      logic like ccfleet drain --dry-run and consolidate the logic into one.
      Essentially the logic is a module of code that can be re-used and not
      repeated."* That is the build shape:
      - **`/atelier:review-plan` owns the logic:** read every briefed review,
        rank, route, estimate, show the table. It seals nothing and starts
        nothing.
      - **`review-drain` calls it** at the start of every drain, then seals
        that plan with his words for the run and runs it. Its § *Rank and
        route the whole queue first* shrinks to a pointer. The drain prints
        the plan as its record of what it is about to do, with no question
        to him (drains are not to stop for answers).
      - **Every other copy is found and folded in.** Found 2026-11-24 by
        grep, by class only (the adopter's copies are private): (a)
        `review-drain` § *Rank and route*, the method in prose; (b) a
        user-local drain skill outside the plugin with its own *Rank and
        route* section and the concrete commands (also 450/010's one
        command outside the prefix); (c) the adopter's private queue tool,
        whose `evidence`, `seal` and `ranked` are the method's code half;
        (d) `ccfleet drain --dry-run`, which calls no ranking at all
        (`instruments/ccfleet` `drain()`, by design so a rehearsal cannot
        touch the seal). Shape to consider for (d): a `ccfleet plan` that
        calls the queue's plan hook read-only, used by the command, by
        `drain` before it seals, and by `drain --dry-run`, so a rehearsal
        shows the real plan without touching the seal. Where the judgement
        half (an agent reading the evidence) and the code half (route
        fit, cost history, the table) each live is the build's first
        design call, made once and written down.
      **Rename, his words, 2026-11-24, verbatim:** *"We should consider
      renaming /atelier:review-drain to /atelier:review-run as well to get
      some consistency across the commands"*. Recommended to him: yes, in
      the same build, so the pair lands together and the naming reads
      `<subject>-plan` (look, change nothing) and `<subject>-run` (do it),
      which `queue-run` already fits. Keep the word "drain" in the skill's
      description so "drain the reviews" still finds it; his answer, verbatim:
      *"yes makes sense, I'm likely to still use the word drain when I think
      about running it"*. Old names: first written here as "no alias, a stub
      would be a second copy", which was wrong (a forwarder holds no copy of
      the logic). Put to him properly (forwarder, signpost recommended, or
      nothing), his pick: *"Nothing"*. The old name simply stops existing. Sized 2026-11-24 by `git grep`: 26 live
      files here, 16 records (left as written; history is kept), and nine
      files in two private child repos, which their own sessions sweep
      (`fleet-sweep`), never this repo's.
      **Superseded on form the same day:** he ruled a space, not a hyphen,
      for every `/atelier:` command, so these are `/atelier:review plan` and
      `/atelier:review run`, with a bare `/atelier:review` showing a menu
      (450/020). Read the names above in that form.
      **Page form, his answer 2026-11-24, verbatim:** *"a table in the
      reply"*. Nothing is open for the build to ask him.
