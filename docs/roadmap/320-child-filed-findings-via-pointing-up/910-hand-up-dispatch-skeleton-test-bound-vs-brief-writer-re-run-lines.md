- [~] 🔎 **Hand-up: the dispatch skeleton's test bound and the review-brief
      🔒 CLAIMED 2026-11-25T13:27Z (claimed 2026-11-25-1327, wt: atelier-qr-f8dd-tb) by session f8dd3843
      (`atelier-31`, Opus 5.5, principal-opened by `/atelier:work run`), inline.
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
