- [ ] ⏳ **Rule-4 cold pass queued: the orchestrator writes the review
      pointer at the landing, and the worker writes none (`180/190`).**
      Doctrine every orchestrated run follows, so the authoring session (a
      principal-opened Opus 5.5 queue run, session deeac927, 2026-11-03,
      which wrote it inline) queues this and does not take it.
      *Tier:* Fable, the principal-named review tier, checked at selection.
      *Pass type:* doctrine cold pass, per `method/REVIEW.md` rule 4.
      *Delta, scoped to paths:* `docs/method/CONCURRENCY.md` (§ *Orchestrated
      queue runs*, the paragraph headed "The orchestrator writes the review
      pointer"), `docs/method/session-open/dispatch-brief.md` (the commit
      that closes `180/190`, on `main`, 2026-11-03).
      *Intent record:*
      [`../180-orchestrated-queue-runs-from-hand-carrie/190-worker-pointers-cite-a-branch-the-merge-deletes.md`](../180-orchestrated-queue-runs-from-hand-carrie/190-worker-pointers-cite-a-branch-the-merge-deletes.md).
      📝 BRIEF WRITTEN 2026-11-09 by session d4a0fcf3 (Opus 5.5, headless,
      started by coordinating session 74f2b8cd; neither authored this delta):
      `docs/reviews/2026-11-09-0207-orchestrator-writes-the-pointer-cold.md`,
      with its `.deferred.md` sibling. Pass size: small. Review NOT run: this
      pass waits for a criterion-passing cold Fable session and the
      principal's explicit permission for Fable work. Neither named session
      may run it.
