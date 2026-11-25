- [ ] 🔎 **Hand-up: where a queued brief's held sibling lives is read two
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
