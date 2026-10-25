- [ ] 🎯 **Rule-4 cold pass queued: the queue-run skill carries the whole
      run brief (`180/010`, `180/030`), and worker teardown (`180/020`).**
      (claimed 2026-10-25-2016, wt: atelier-cold-160-900; cold pass: a Fable 5.1
      reviewer under an Opus 5.5 orchestrator, session 52e11d15, which holds
      the context partition, forms no finding and writes no severity)
      ✅ **PASS RAN 2026-10-25 (UTC)**, acts 1 and 2, by a Fable 5.1 reviewer
      under that orchestrator, which held the deferred sibling out of the tree
      until act 1 was saved, then folded it below the verdict.
      [`reviews/2026-10-18-0517-queue-run-carries-the-brief-cold.md`](../../reviews/2026-10-18-0517-queue-run-carries-the-brief-cold.md).
      **PASS-WITH-FINDINGS — 1 MAJOR / 6 MODERATE / 4 minor / 3 notes
      (QK1–QK14).** The cycle stays OPEN while QK1 stands: the command runs
      the local clone's working tree, so uncommitted prompt text executes
      with no commit, hook, test or review having seen it.
      🎯 **Mike to rule (rule 3, doctrine):** all fourteen; the brief's
      *Follow-up checklist* lists them. Nothing applied.
      Doctrine text, so the authoring session (a Mike-opened Opus 5.5 queue
      run, 2026-10-18, wt atelier-qr-180-plugin) queues this and does not
      take it.
      *Tier:* Fable, the principal-named review tier, checked at selection.
      *Pass type:* doctrine cold pass, per `method/REVIEW.md` rule 4.
      *Delta, scoped to paths:* `docs/method/CONCURRENCY.md` (§ *Orchestrated
      queue runs*: *Where the doctrine is read from*, the three selection
      rules, what the report carries, the value reading of a spend directive,
      the ask cadence), `skills/queue-run/SKILL.md`, `README.md` (local-path
      install) and `docs/method/session-open/session-open-prompt.md`, all in
      commit `998c35f` on `main`, 2026-10-18; and, widened by the same
      session (AW6), the *teardown* rule (`CONCURRENCY.md` § *Orchestrated
      queue runs* and the worktree bullet in § *Integration hygiene*, plus
      one sentence in `skills/queue-run/SKILL.md`), commit `1487e9c` on
      `main`, 2026-10-18, which closes `180/020`; and commit `140a190`
      (`180/040`, `180/050`: the restored prompt lines in the prompt,
      `CONCURRENCY.md` and the skill; the version field dropped from both
      plugin manifests; README); and commit `1adf398` (`180/070`, `180/080`:
      the session id first, the identifiers block in `RECORD.md` § *The
      session log*, and the prompt, `CONCURRENCY.md` and skill pointers),
      with its two same-day `RECORD.md` sharpenings, commit `46320f8` and the
      one after it (PRs, worktrees created, board items completed and
      created); and commit `12e6d9b` (`180/090`: the skill now loads the
      prompt file and adds nothing, with
      `tools/test_queue_run_single_source.py`).
      *Intent record:*
      [`../180-orchestrated-queue-runs-from-hand-carrie/010-the-plugin-was-never-installed-so-the-hand-carried-prompt-never-stopped.md`](../180-orchestrated-queue-runs-from-hand-carrie/010-the-plugin-was-never-installed-so-the-hand-carried-prompt-never-stopped.md)
      ,
      [`../180-orchestrated-queue-runs-from-hand-carrie/020-teardown-inferred-from-git-is-not-the-same-as-stopped.md`](../180-orchestrated-queue-runs-from-hand-carrie/020-teardown-inferred-from-git-is-not-the-same-as-stopped.md)
      and
      [`../180-orchestrated-queue-runs-from-hand-carrie/030-the-canonical-session-open-prompt-is-not-the-one-in-use.md`](../180-orchestrated-queue-runs-from-hand-carrie/030-the-canonical-session-open-prompt-is-not-the-one-in-use.md).
      **Brief WRITTEN 2026-10-18, review NOT run** —
      `docs/reviews/2026-10-18-0517-queue-run-carries-the-brief-cold.md` with
      a `.deferred.md` sibling. Written by an Opus brief-writer that authored
      none of the delta (dispatched by the Mike-opened Opus 5.5 queue run, wt
      atelier-qr-briefs-1018); its exposure is disclosed in the brief. The
      pass stays queued for a criterion-passing cold Fable session.
