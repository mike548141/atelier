- [ ] 🎯 **Hand-up: where a queued brief's held sibling lives is read two
      ways, and one reading hides the brief from the queue.** Reported
      2026-11-25 by a private child's queue run (met 2026-11-23, session
      95797e59), class only.
      `/atelier:review brief` says deferred material lives in its own file,
      `<slug>.deferred.md`, and the house convention puts that file beside
      the brief in `docs/reviews/`, which is what the review queue reads.
      `CONCURRENCY.md` § *Orchestrated queue runs* says material an
      orchestrator holds back from a cold reviewer *"lives in a user-local
      directory the orchestrator creates outside the repo"*. A dispatch that
      followed the second rule literally for a brief being *queued* (not a
      pass being run) put the sibling outside the repo, and the queue then
      did not see the brief as complete.
      **Evidence:** the child run's first brief-writer dispatch did exactly
      that; the orchestrator moved the sibling back beside the brief.
      Unevidenced beyond that one instance.
      **Asked:** one line saying the held-material rule governs the pass
      (while a cold reviewer is running), not the queued brief at rest, or
      the reverse if the house means the sibling never to sit in the repo.
      🎯 **Read 2026-11-25 by session f8dd3843 (`atelier-31`, queue run); his call, because it
      sets how much a later reviewer can see.** The two texts are less opposed than they look:
      `REVIEW.md` rule 1 names the sibling's path in the repo
      (`docs/reviews/<date>-<HHMM>-<slug>.deferred.md`) and keeps the bytes with the
      orchestrator only while a pass runs; `CONCURRENCY.md`'s held-material sentence drops
      that *while*. Practice is split: eight `.deferred.md` siblings sit committed in
      `docs/reviews/`, while the 2026-11-25 DV and PK passes held theirs user-local from the
      moment the briefs were written. **Recommendation:** the held-material rule governs the
      pass; at rest a queued brief's sibling sits beside it, where the queue reads it, and the
      orchestrator moves it out when it starts the pass. The cost to weigh: a committed sibling
      is in a public repo's history, readable by any later session; the alternative (never in
      the repo) needs the queue taught to find a user-local sibling, and a brief whose writer's
      machine is gone loses its seeded questions.
