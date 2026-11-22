- [ ] 🎯 **Rule-4 cold pass queued: `ccclose` names a `failed` agent as its own state (`210/400`).** The authoring session (a
      principal-opened Opus 5.5 queue run, session d0ca5d24, 2026-11-09 UTC,
      which dispatched the worker that wrote it) queues this and does not
      take it.
      *Tier:* Fable, the principal-named review tier, checked at selection;
      the pass waits for his explicit permission for Fable work.
      *Pass type:* code cold pass, per `method/REVIEW.md` rule 4.
      *Delta, scoped to paths:* `instruments/ccclose`, `instruments/ccclose.test.js`, `instruments/ccclose.design.md`, `instruments/man/ccclose.1` — the commit that closes `210/400`, on `main`.
      *Questions worth the pass's time:* whether a failed foreground agent is judged correctly before its tool result; whether the count of *failed* can mix agents with background commands.
      *Intent record:* `210/400`.
      📝 BRIEF WRITTEN 2026-11-14 by a headless Opus 5.5 brief-writer (session 6321275c,
      started by an estate health sweep, orchestrator session 58027096; neither authored this
      delta): `docs/reviews/2026-11-14-0242-ccclose-failed-state-cold.md`, with its
      `.deferred.md` sibling. The delta is one commit, `50547442`. Pass size: small. Review NOT
      run: it waits for a criterion-passing cold Fable session and the principal's explicit
      permission for Fable work. Neither named session may run it.
      🔒 2026-11-22T22:21Z: claimed for the Fable pass by a headless per-pass
      orchestrator, session 98afb222 (Opus 5.5, rule-4 off-tier orchestrator:
      it holds the partition and forms no finding), started by drain session
      eca14b23; the reviewer is a Fable 5.1 subagent, tier checked at
      selection. Neither is barred by the brief. The approval this item waits
      for is his drain order of 2026-11-23, verbatim: *"Start a fable drain or
      whatever it is called now. Target 100% of weekly budget by 11.30am NZT
      todat"*. The held-back sibling is partitioned out of the review tree
      until act 1 is committed.
      ✅ 2026-11-22T23:00Z: PASS RAN (Fable 5.1, both acts; orchestrator as claimed).
      **Verdict: FAIL — 1 MAJOR, 2 MODERATE, 5 minor, 2 notes (`FA1`–`FA10`;
      `FA10` formed at reconcile).** Standing MAJOR: `FA1`, a `failed`
      notification is read as the agent's end even when the agent was resumed
      after it, so a working agent reads `failed` (the brief's worst failure, a
      live agent called dead); the store holds 48 agents resumed after a
      `failed`, and no test pins the case. MODERATE: `FA2`, "none ending on
      `end_turn`" is measured only over agents whose latest notification is
      `failed` (47 resumed ones end on it); `FA10`, a foreground agent whose
      launch `tool_result` is an error, with no notification, reads
      `reported`, a pass (`is_error` is never read; one real case in the
      store). Minor: `FA3` two design-note rows omit `failed`; `FA4` changelog
      says "fifth" state, it is the sixth; `FA5` the census has four homes, its
      total stale; `FA6` the `failed` line names no contrary evidence; `FA7`
      a plain user record can set `failed` (no threat line). Notes: `FA8` why a
      `failed` agent blocks a close is unstated; `FA9` check 15 passes a
      `failed` launch that check 12 fails. Suite 153/153, manual lint clean,
      census figures reproduced (50 and 0; total now 3,915), live proof read.
      🎯 **Owed to him (rule 3, every finding is his):** (1) `FA1`, give the
      `failed` branch the `completed` branch's resume test, with tests both
      ways (reviewer's counsel: yes); (2) `FA10`, an error launch result with
      no notification becomes at most a warn, or `failed` (counsel: yes, one
      of the two); (3) `FA8`, is a `failed` agent a close blocker or a warning
      (counsel: his call; lost work matches `cut`); (4) bulk-approve `FA2`–`FA7`
      as one application commit, `FA9` for awareness. Recommendation: approve
      (1), (2) and (4), `FA1` first, and rule (3). *Routing:* an application
      session in this repo after his word; its diff earns its own cold pass.
      Verdict, folded sibling and review log:
      `docs/reviews/2026-11-14-0242-ccclose-failed-state-cold.md`.
