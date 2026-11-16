- [ ] 🎯 **Rule-4 cold pass queued: `/atelier:queue-run` reads the committed
      prompt and warns on a pending edit, and the teardown rule's three legs
      (`160/900`, QK1 and its counsel applied).** The command every queue run
      starts from now runs only committed text. The authoring session (a
      principal-opened Opus 5.5 queue run, session 722ac2e2, 2026-11-09, in
      its ruling round, which dispatched the Sonnet worker that wrote it)
      queues this and does not take it.
      *Tier:* Fable, the principal-named review tier, checked at selection;
      the pass waits for his explicit permission for Fable work.
      *Pass type:* code and doctrine cold pass, per `method/REVIEW.md` rule 4.
      *Delta, scoped to paths:* `skills/queue-run/SKILL.md`,
      `tools/test_queue_run_single_source.py`, `docs/method/CONCURRENCY.md`
      (§ *Orchestrated queue runs*: teardown, doctrine source, identifiers,
      ask cadence), `docs/method/RECORD.md`, `docs/method/README.md`,
      `docs/method/session-open/README.md`, `README.md`, `CHANGELOG.md` — the
      commit that applies `160/900`'s QK1, on `main`, 2026-11-09.
      *Questions worth the pass's time:* whether an agent following the
      skill can still end up running uncommitted prompt text (a checkout
      that is not the plugin root, a detached head, a stale clone); whether
      the three-leg teardown rule is followable by a separate-session worker.
      *Intent record:*
      [`900-rule-4-cold-pass-queued-queue-run-carries-the-brief.md`](900-rule-4-cold-pass-queued-queue-run-carries-the-brief.md).
      📝 BRIEF WRITTEN 2026-11-09 by session 84e3aa7f (Opus 5.5), a headless
      brief-writer started by coordinating session 74f2b8cd:
      `docs/reviews/2026-11-09-0126-queue-run-committed-prompt-cold.md`, with
      its `.deferred.md` sibling. Neither session may run the pass. Review NOT
      run. The pass waits for a criterion-passing cold Fable session and the
      principal's explicit permission for Fable work.
      🔒 CLAIMED 2026-11-15T22:16Z UTC for the cold pass, in Mike's weekly Fable drain (his
      `/fable-drain` order, 2026-11-16 06:53 NZDT; approval lapses at the reset,
      2026-11-15 23:00 UTC). Orchestrator: headless Opus 5.5 session 9cdae066,
      started by drain session 21a271a5, a rule-4 off-tier orchestrator that holds
      the context partition, forms no finding and writes no severity. Reviewer:
      Fable 5.1, tier checked at selection, spawned by that orchestrator. Neither
      is a barred session (722ac2e2 and what it started, 84e3aa7f, 74f2b8cd). The
      sibling is held out of the worktree until act 1 is committed. The item's
      "waits for the principal's explicit permission for Fable work" is met by
      that drain order.
      ⚠️ PASS RAN 2026-11-16 UTC (Fable 5.1 reviewer, act 1 committed before the sibling opened, act 2
      folded with the sibling; the weekly usage limit cut act 1 and the same reviewer resumed on
      the principal's resume order): **PASS-WITH-FINDINGS — 0 MAJOR, 3 MODERATE, 3 minor,
      4 notes** (`QC1`–`QC10`, verdict in the brief). No standing MAJOR.
      🎯 **The principal's to rule (rule 3; recorded, nothing applied):** MODERATE first. `QC1`
      the "nothing but delivery" test pins five substrings per block, so most planted rule
      insertions pass green while the changelog and skill claim every added paragraph fails;
      `QC2` the skill says committed text "has met the pre-commit hook, the tests and review",
      which overclaims and contradicts its own README; `QC3` the threat note's controls do not
      reach a local install, where what the committed read buys is a trace, not a check (counsel:
      fail closed when `git show` fails on a checkout). Then minor `QC4` (the "answer, not a
      ruling" relabel reached 1 of 4 surfaces), `QC5` ("closing paragraph" misplaces the away
      sentence), `QC9` (the session-open README still says the say-so check is not built); notes
      `QC6` (the principal's own prompt still says the command "cannot differ" from the file; his
      text, his call), `QC7` (a symlinked or nested plugin root fits neither named shape), `QC8`
      (leg 3 is evidence for session workers only), `QC10` (the opening report does not say which
      commit's prompt ran). Each carries counsel in the verdict. With no MAJOR, `REVIEW.md`'s
      close rule applies: the rulings go to the backlog with no further queued pass.
      *Recommendation, for one bulk ask:* approve the counselled fixes as a list, `QC1`–`QC3`
      first. *Routing:* fixes land in atelier (`skills/queue-run/SKILL.md`,
      `tools/test_queue_run_single_source.py`, `docs/method/session-open/README.md`,
      `CHANGELOG.md`).
