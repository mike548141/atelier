- [x] **Rule-4 cold pass queued: `board.py` sorts item and section
      numbers as numbers (`010/200`).** `board.py` generates every child's
      index, so the authoring session (a principal-opened Opus 5.5 queue
      run, session deeac927, 2026-11-03, which wrote it inline) queues this
      and does not take it.
      *Tier:* Fable, the principal-named review tier, checked at selection.
      *Pass type:* code cold pass, per `method/REVIEW.md` rule 4.
      *Delta, scoped to paths:* `tools/board.py`, `tools/test_board.py`,
      `CHANGELOG.md` (the commit that closes `010/200`, on `main`,
      2026-11-03).
      *Intent record:*
      [`../010-board-store-migration-per-item-files-mik/200-a-four-digit-item-number-sorts-out-of-order.md`](../010-board-store-migration-per-item-files-mik/200-a-four-digit-item-number-sorts-out-of-order.md).
      📝 BRIEF WRITTEN 2026-11-09 by session d4a0fcf3 (Opus 5.5, headless,
      started by coordinating session 74f2b8cd; neither authored this delta):
      `docs/reviews/2026-11-09-0207-board-sorts-numbers-cold.md`, with its
      `.deferred.md` sibling. Pass size: small. Review NOT run: this pass
      waits for a criterion-passing cold Fable session and the principal's
      explicit permission for Fable work. Neither named session may run it.
      **Dequeued 2026-11-27 ~01:55 UTC (board `460/040`; session 4ce066ba, `atelier-c1`,
      AskUserQuestion; an answer to options Claude wrote, not a ruling), not run.** His pick,
      verbatim: *"Drop 8, merge 6 (Recommended)"* (option text: *"31 reviews stay in Monday's
      drain. Takes back your earlier picks on 4 of them. Saves roughly 8 Fable passes of
      budget; the 6 merged ones still get reviewed, just together."*). Under the bar in
      `method/REVIEW.md` § *Whether work earns a review at all*, this is a loud fix to a
      reviewed, tested tool: a sort, which the `board` check reds on when the index and the
      store disagree, and `tools/test_board.py` covers; the recorded grounds give reach, which
      the bar does not count. The brief stays as record, marked retired:
      `docs/reviews/2026-11-09-0207-board-sorts-numbers-cold.md`.
      review: not warranted — a sort fix to `board.py`, a reviewed tool its tests cover
