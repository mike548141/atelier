- [ ] ⏳ **Rule-4 cold pass queued: the bar before a pass is queued, and when a finding is
      fixed before use and when fixes earn a re-check (`460/020`).** The authoring session
      (4ccec293, `atelier-56`, Opus 5.5, principal-opened by `/atelier:work run` with
      `460/020` as its brief) wrote the change inline and queues this; it neither briefs
      nor takes it.
      *Tier:* Fable, the principal-named review tier, checked at selection; it runs only on
      his approval (the general Fable hold). He ordered a pass of its own for this change
      (his brief to the authoring session, 2026-11-26: *"Doctrine, so its own Fable review
      is queued for my approval, not run."*), so it is not folded into `160/1830`, the
      open, unbriefed pass on the same four files; a drain may run the two together.
      *Pass type:* doctrine, per `method/REVIEW.md` rule 4: a change to rule 4 itself and to
      when a pass is owed.
      *Delta, scoped to paths:* `docs/method/REVIEW.md`, `docs/method/ECONOMICS.md`,
      `docs/method/CONCURRENCY.md`, `docs/method/session-open/dispatch-brief.md`,
      `skills/review/brief.md`, `CHANGELOG.md`: every commit on `main` after `b459dd7e` up to
      and including the commit that closes `460/060` (folding in `460/050`, his widened
      list of risks fixed before use, and `460/060`, his default that every owed review
      waits for the next drain; one open pass per subject). Widened 2026-11-27 by
      `460/030` step 1, which its item folds here: `tools/pointerscan.py`,
      `tools/test_pointerscan.py`, `tools/README.md` and the same `REVIEW.md` and
      `CHANGELOG.md`, every commit after `3693786f` up to and including the commit that
      lands `460/030` step 1. Intent record for that part:
      [`../460-the-bar-before-a-fable-review-is-ordered-mike-comm/030-gate-pointers-that-lack-the-grounds.md`](../460-the-bar-before-a-fable-review-is-ordered-mike-comm/030-gate-pointers-that-lack-the-grounds.md).
      Widened 2026-11-27 by folding `160/1830` here (board `460/040`, one open pass per
      subject; his pick *"Drop 8, merge 6 (Recommended)"*), so the two now run as one
      pass: `docs/method/CONCURRENCY.md`, `docs/method/REVIEW.md`,
      `docs/method/session-open/dispatch-brief.md`, `skills/review/brief.md`: also commit
      `f239dc3b`, the commit that lands `160/1830`'s pointer, on `main`. Intent record for
      that part:
      [`../320-child-filed-findings-via-pointing-up/910-hand-up-dispatch-skeleton-test-bound-vs-brief-writer-re-run-lines.md`](../320-child-filed-findings-via-pointing-up/910-hand-up-dispatch-skeleton-test-bound-vs-brief-writer-re-run-lines.md).
      The folded item's own notes stay in `160/1830`.
      *Intent record:*
      [`../460-the-bar-before-a-fable-review-is-ordered-mike-comm/020-write-the-bar-into-the-review-rules.md`](../460-the-bar-before-a-fable-review-is-ordered-mike-comm/020-write-the-bar-into-the-review-rules.md).
      💬 **When it runs, his pick 2026-11-26 ~22:00 UTC (session 4ccec293, `atelier-56`,
      AskUserQuestion; an answer, not a ruling):** *"Monday's drain (Recommended)"* (option
      text: *"Runs in the weekly drain that starts Mon 30 Nov, using budget that would
      otherwise lapse."*). So it runs in the drain that starts 2026-11-29 23:00 UTC, by a
      session that wrote none of it; it gates nothing. Barred from briefing or running it:
      4ccec293.
