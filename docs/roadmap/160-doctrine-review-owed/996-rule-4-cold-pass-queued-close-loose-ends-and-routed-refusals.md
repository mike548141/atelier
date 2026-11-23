- [ ] 🎯 **Rule-4 cold pass queued: a loose end makes the close "not ready
      until you decide", a refused call is an ask and never routed around,
      and ccclose's scratch-folder check and refused-delete re-route flag
      (`180/170`, `180/180`).** This is standing close and autonomy doctrine
      every session reads, and the instrument that checks it. So the
      authoring session (a principal-opened Opus 5.5 queue run, session
      4c65083c, 2026-11-03, which dispatched the Opus worker that wrote the
      text and code) queues this and does not take it.
      *Tier:* Fable, the principal-named review tier, checked at selection.
      *Pass type:* code and doctrine cold pass, per `method/REVIEW.md` rule 4.
      *Delta, scoped to paths:* `docs/method/RECORD.md`,
      `docs/method/AUTONOMY.md`, `docs/method/CONCURRENCY.md`,
      `instruments/ccclose`, `instruments/ccclose.test.js`,
      `instruments/man/ccclose.1`, `instruments/ccclose.design.md`,
      `instruments/README.md` (the commit that closes the two items below, on
      `main`, 2026-11-03).
      *Intent records:*
      [`../180-orchestrated-queue-runs-from-hand-carrie/170-declared-ready-to-close-with-loose-ends.md`](../180-orchestrated-queue-runs-from-hand-carrie/170-declared-ready-to-close-with-loose-ends.md),
      [`../180-orchestrated-queue-runs-from-hand-carrie/180-a-denied-delete-was-worked-around-with-python.md`](../180-orchestrated-queue-runs-from-hand-carrie/180-a-denied-delete-was-worked-around-with-python.md).
      📝 BRIEF WRITTEN 2026-11-09 by session d4a0fcf3 (Opus 5.5, headless,
      started by coordinating session 74f2b8cd; neither authored this delta):
      `docs/reviews/2026-11-09-0207-close-loose-ends-refusals-cold.md`, with
      its `.deferred.md` sibling. Pass size: medium. Review NOT run: this pass
      waits for a criterion-passing cold Fable session and the principal's
      explicit permission for Fable work. Neither named session may run it.
      🔒 2026-11-22T22:34Z: claimed for the Fable pass by a headless per-pass
      orchestrator, session 7dbb6565 (Opus 5.5, rule-4 off-tier orchestrator:
      it holds the partition and forms no finding), started by drain session
      eca14b23; the reviewer is a Fable 5.1 subagent, tier checked at
      selection. Neither is barred by the brief. The approval this item waits
      for is his drain order of 2026-11-23, verbatim: *"Start a fable drain or
      whatever it is called now. Target 100% of weekly budget by 11.30am NZT
      todat"*. The held-back sibling is partitioned out of the review tree
      until act 1 is committed.
      ✅ 2026-11-23T00:08Z: PASS RAN (Fable 5.1, both acts; orchestrator as claimed).
      **Verdict: PASS-WITH-FINDINGS — 1 MAJOR, 1 MODERATE, 6 minor, 1 note
      (`LE1`–`LE8`, `N1`).** Standing MAJOR: `LE1`, `ccclose`'s `REFUSAL`
      is a closed list of harness wordings that misses four live refusal
      shapes (the harness's `rm` guard, its built-in safety check, the
      worktree-isolation block, hook blocks), about one delete refusal in
      three, so a re-route after one is never listed and the close reads
      clean; all four predate the census the code cites. MODERATE: `LE3`,
      the `rm` route misses `/bin/rm` and a trailing `xargs rm`. Minor:
      `LE2` AUTONOMY's list of who refuses omits harness checks and hooks;
      `LE4` Node `fs.unlink` double-labelled as pathlib; `LE5` the label
      asserts a re-route on a route change alone; `LE6` the "at least"
      branch is untested; `LE7` "harms nothing" contradicts the scratch
      doctrine; `LE8` (formed at reconcile) AUTONOMY's refused-call rule has
      no headless fallback. Note `N1`: the route and wording lists live in
      four places. The doctrine itself landed on the principal's sentence,
      and the grounding-session claim reproduced.
      🎯 **Owed to him (rule 3, every finding is his):** (1) `LE1`, replace
      the closed wording list with an open bucket (any errored delete that
      is not an ordinary exit-code failure counts as refused), with the four
      wordings pinned as fixtures (counsel: yes); (2) `LE2` + `LE8`, widen
      AUTONOMY's refused-call rule to every refuser and give it the headless
      fallback CONCURRENCY already has (counsel: yes, one edit); (3)
      bulk-approve the remaining fixes `LE3`–`LE7` and `N1` as one
      application commit. Recommendation: approve all three, `LE1` first.
      *Routing:* an application session in this repo after his word; its
      diff earns its own cold pass. Verdict, folded sibling and review log:
      `docs/reviews/2026-11-09-0207-close-loose-ends-refusals-cold.md`.
