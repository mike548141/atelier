- [~] 💡 **A plan mode for `/atelier:work-run`, as `/atelier:work-plan`:
      show the run before it runs, and run nothing.** An idea to consider,
      his words, 2026-11-24, session b95c0d98, verbatim: *"We could also
      consider having /atelier:work-plan in the same way a parallel session is
      working on /atelier:review-plan vs /atelier:review-drain"*. Idea only:
      it stays queued until he says to start it.
      **Sibling:** `180/210`, the plan mode for `review-drain`. A work plan
      would run a work run's opening reads and triage (`ccopen`, the waiting
      and parked items, what is buildable without him, the run-gating
      questions) and stop before claiming anything, showing what the run
      would do, in what order, and what it would ask him. Build it on the same
      shape as `180/210` once that lands, so the two plan modes read alike.
      **Moved into `450/020`'s build, his words, 2026-11-24, verbatim:** *"You
      can do the work plan, but that should be done at the same time as the
      other /atelier work I've described in the parallel session in this
      repo. Its just one of the commands being changed"*. Built there as
      `/atelier:work plan`, not here.
      (claimed 2026-11-24-0938, wt: atelier-e8-subject-action)
