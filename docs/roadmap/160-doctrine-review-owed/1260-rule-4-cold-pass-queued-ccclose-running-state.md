- [ ] 🎯 **Rule-4 cold pass queued: ccclose's fourth agent state, still running (`210/380`).** The authoring session (a
      principal-opened Opus 5.5 queue run, session d0ca5d24, 2026-11-09 UTC,
      which dispatched the worker that wrote it) queues this and does not
      take it.
      *Tier:* Fable, the principal-named review tier, checked at selection;
      the pass waits for his explicit permission for Fable work.
      *Pass type:* code cold pass, per `method/REVIEW.md` rule 4.
      *Delta, scoped to paths:* `instruments/ccclose`, `instruments/ccclose.test.js`, `instruments/man/ccclose.1`, `instruments/ccclose.design.md` — the commit that closes `210/380`, on `main`.
      *Questions worth the pass's time:* whether the two freshness tests can read a dead agent as running past the stated bound; whether a run of the check under live workers stays honest.
      *Intent record:* `210/380`.
      📝 BRIEF WRITTEN 2026-11-14 by a headless Opus 5.5 brief-writer (session 947ac694,
      started by an estate health sweep, orchestrator session 58027096; neither authored this
      delta): `docs/reviews/2026-11-14-0154-ccclose-running-state-cold.md`, with its
      `.deferred.md` sibling. The delta is one commit, `1bc89816`; `50547442` has since changed
      the same function and stays `160/1350`'s subject. Pass size: small. Review NOT run: it
      waits for a criterion-passing cold Fable session and the principal's explicit permission
      for Fable work. Neither named session may run it.
      🔒 2026-11-22T22:16Z: claimed for the Fable pass by a headless per-pass
      orchestrator, session 1e1c5269 (Opus 5.5, rule-4 off-tier orchestrator:
      it holds the partition and forms no finding), started by drain session
      eca14b23; the reviewer is a Fable 5.1 subagent, tier checked at
      selection. Neither is barred by the brief. The approval this item waits
      for is his drain order of 2026-11-23, verbatim: *"Start a fable drain or
      whatever it is called now. Target 100% of weekly budget by 11.30am NZT
      todat"*. The held-back sibling is partitioned out of the review tree
      until act 1 is committed.
      ✅ 2026-11-22T22:42Z: PASS RAN (Fable 5.1, both acts; orchestrator as claimed).
      **Verdict: PASS-WITH-FINDINGS — 0 MAJOR, 2 MODERATE, 2 minor, 1 note
      (`LV1`–`LV5`).** No standing MAJOR. MODERATE: `LV1`, the parent-clock
      test in `runningVerdict` never decides a verdict (0 differences over
      4.4 M probe cases), yet the code comment, design note, manual and
      `CHANGELOG.md` call it a second signal, and its one test uses a parent
      record stamped in the future; `LV2`, the bound's error is stated one way
      only: the census's own 0.1 % tail past 600 s, and the harness moving an
      over-cap command to the background, make a working agent read as cut,
      while the design note says it "never calls a live agent dead". Minor:
      `LV3` the census has no dated home (five copies); `LV4` two cosmetic
      branches unpinned. Note `LV5`, a past `--session` read is judged by the
      wall clock. No finding formed at reconcile; sibling question 5 (does the
      harness write to a dead agent's file) stays open, unprobed. Suite 153/153,
      manual lint clean, live proof matched the design note.
      🎯 **Owed to him (rule 3, every finding is his):** (1) `LV2`, should
      the running/cut lines state both error directions and drop "never calls
      a live agent dead", with either a margin above the harness cap or a cut
      line that prints the silence length (counsel: yes, the line that prints
      the silence length); (2) `LV1`, remove the parent-clock test and its
      four statements, or make it a signal that can occur (counsel: remove);
      (3) bulk-approve `LV3`–`LV4` as one application commit, `LV5` for
      awareness. Recommendation: approve all three, `LV2` first. *Routing:* an
      application session in this repo after his word; its diff earns its
      own cold pass. Verdict, folded sibling and review log:
      `docs/reviews/2026-11-14-0154-ccclose-running-state-cold.md`.
