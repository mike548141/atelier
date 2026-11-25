- [x] 🔎 **Hand-up: the dispatch skeleton's test bound and the review-brief
      skill's re-run duty contradict each other for a worker that writes a
      brief.** Reported 2026-11-25 by a private child's queue run (met
      2026-11-23, session 95797e59), class only.
      `docs/method/session-open/dispatch-brief.md` tells every worker *"Run
      only the test modules for what you changed … Never the full suite"*.
      `REVIEW.md` (the paragraph after the re-run rule) and
      `/atelier:review brief` tell the brief-writer that it *"runs every
      re-run line once, from where the brief says to run it, before writing
      it down"*. A brief's re-run lines routinely include the full suite or
      modules the worker did not change, so a worker dispatched to write a
      brief cannot honour both.
      **Evidence:** two brief-writer workers in one run met it; one obeyed
      each rule, and the orchestrator ran the missing re-run lines itself
      before landing the briefs. Both rules read as quoted at atelier
      `origin/main` on 2026-11-25. Related, not the same: `180/200` (the
      bound's origin).
      **Asked:** say which wins for a brief-writing worker, e.g. a line in the
      skeleton exempting the brief's own re-run lines (run once, under
      `nice`, one after another), or a line in the brief skill handing the
      re-run to the orchestrator.
      ✅ **Done 2026-11-25 (session f8dd3843, `atelier-31`, queue run): the test bound
      wins for the full suite only.** A brief-writing worker runs each of its brief's
      re-run lines once, under `nice`, one after another; a full-suite line it names in its
      report and the orchestrator runs before landing the brief, as at any landing. Why
      that split: the bound exists for machine load (`180/200`, load 310), and the full
      suite is already the orchestrator's at the landing; every other re-run line stays
      the writer's, so a line that fails from the place it names is still caught before
      the reviewer meets it (PF10). Written in `method/CONCURRENCY.md` § *Orchestrated
      queue runs* (the worker test-bound paragraph), the skeleton line in
      `method/session-open/dispatch-brief.md` and its grounding row, `method/REVIEW.md`
      (after the brief-writer's duty) and `skills/review/brief.md` item 5. Its cold
      pass is queued as `160/1830`.
