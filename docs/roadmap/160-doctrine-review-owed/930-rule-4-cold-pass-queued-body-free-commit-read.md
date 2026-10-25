- [ ] 🎯 **Rule-4 cold pass queued: the body-free commit read (`130/030`).**
      (claimed 2026-10-25-2233, wt: atelier-cold-160-930; cold pass: a Fable 5.1
      reviewer under an Opus 5.5 orchestrator, session 52e11d15, which holds
      the context partition, forms no finding and writes no severity)
      ✅ **PASS RAN 2026-10-25 (UTC)**, acts 1 and 2, by a Fable 5.1 reviewer
      under that orchestrator, which held the deferred sibling out of the tree
      until act 1 was saved, then folded it below the verdict.
      [`reviews/2026-10-18-0508-body-free-commit-read-cold.md`](../../reviews/2026-10-18-0508-body-free-commit-read-cold.md).
      **PASS-WITH-FINDINGS — 1 MAJOR / 4 MODERATE / 5 minor / 5 notes
      (BF1–BF15).** The cycle stays OPEN while BF1 stands: with no `--path`,
      `coldsweep --commit` prints the intent record's hunk and the queue
      pointer under a clean "message body not read" line.
      🎯 **Mike to rule (rule 3):** all fifteen; BF5 together with `160/910`,
      whose paragraph its fix overlaps. Nothing applied.
      The `review-brief` skill's text is doctrine by function, and `coldsweep`
      is a guard whose clean output is read as "nothing barred was seen". So
      the authoring session (a Mike-opened Opus 5.5 queue run, 2026-10-18, wt
      atelier-qr-130-030, which dispatched the Sonnet worker that wrote the
      code) queues this and does not take it.
      *Tier:* Fable, the principal-named review tier, checked at selection.
      *Pass type:* code and doctrine cold pass, per `method/REVIEW.md` rule 4.
      *Delta, scoped to paths:* `tools/coldsweep.py`, `tools/test_coldsweep.py`
      (commit `8132805`) and `skills/review-brief/SKILL.md` (commit
      `30aa8dc`, which also queued this item), both on `main`, 2026-10-18.
      *Intent record:*
      [`../130-a-closed-cycle-can-keep-its-and-pointers/030-the-brief-bars-the-commit-body-but-names-no-command-that-avoids-it.md`](../130-a-closed-cycle-can-keep-its-and-pointers/030-the-brief-bars-the-commit-body-but-names-no-command-that-avoids-it.md).
      **Brief WRITTEN 2026-10-18, review NOT run** —
      `docs/reviews/2026-10-18-0508-body-free-commit-read-cold.md` with a
      `.deferred.md` sibling. Written by an Opus brief-writer that authored
      none of the delta (dispatched by the Mike-opened Opus 5.5 queue run, wt
      atelier-qr-briefs-1018); its exposure is disclosed in the brief. The
      pass stays queued for a criterion-passing cold Fable session.
