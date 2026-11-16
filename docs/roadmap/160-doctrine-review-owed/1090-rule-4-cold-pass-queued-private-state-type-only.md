- [ ] 🎯 **Rule-4 cold pass queued: a private repo's state goes by type in public records (`260/080`, posture C).** The authoring session (a
      principal-opened Opus 5.5 queue run, session 722ac2e2, 2026-11-09, in
      its ruling round, which dispatched the Sonnet worker that wrote it)
      queues this and does not take it.
      *Tier:* Fable, the principal-named review tier, checked at selection;
      the pass waits for his explicit permission for Fable work.
      *Pass type:* doctrine cold pass, per `method/REVIEW.md` rule 4.
      *Delta, scoped to paths:* `docs/decisions/2026-08-05-1233-estate-internal-context-in-public-records.md` (Decision, Rejected, Consequences), `docs/method/RECORD.md` § *The record is public*, `docs/decisions/README.md`, `CHANGELOG.md` — the commit that closes `260/080`, on `main`, 2026-11-09.
      *Questions worth the pass's time:* whether the condition/act line is drawable by a session at write time; whether the drafter's two readings follow from the posture.
      *Intent record:* [`../260-sharing-public-since-2026-07-10-adr-0005/080-p6-rpi-f5-estate-internal-context-accumulating.md`](../260-sharing-public-since-2026-07-10-adr-0005/080-p6-rpi-f5-estate-internal-context-accumulating.md).
      📝 BRIEF WRITTEN 2026-11-09 by session 84e3aa7f (Opus 5.5), a headless
      brief-writer started by coordinating session 74f2b8cd:
      `docs/reviews/2026-11-09-0126-private-state-type-only-cold.md`, with its
      `.deferred.md` sibling. Neither session may run the pass. Review NOT
      run. The pass waits for a criterion-passing cold Fable session and the
      principal's explicit permission for Fable work.
      🔒 CLAIMED 2026-11-15T22:09Z UTC for the cold pass, in Mike's weekly Fable drain (his
      `/fable-drain` order, 2026-11-16 06:53 NZDT; approval lapses at the reset,
      2026-11-15 23:00 UTC). Orchestrator: headless Opus 5.5 session 6dd1e8d3,
      started by drain session 21a271a5, a rule-4 off-tier orchestrator that holds
      the context partition, forms no finding and writes no severity. Reviewer:
      Fable 5.1, tier checked at selection, spawned by that orchestrator. Neither
      is a barred session (722ac2e2 and what it started, 84e3aa7f, 74f2b8cd). The
      sibling is held out of the worktree until act 1 is committed. The item's
      "waits for the principal's explicit permission for Fable work" is met by
      that drain order.
      ✅ PASS RAN 2026-11-15 UTC (act 1 `f082493f`, act 2 `e6896167`; act 2 was cut
      by the weekly usage limit and finished by the same Fable 5.1 reviewer after the
      reset, on the principal's resume order). Verdict **PASS-WITH-FINDINGS — 0 MAJOR ·
      2 MODERATE · 6 minor · 2 note** (TY3 lowered to minor and TY10 added at
      reconcile). No standing MAJOR, so applying the rulings closes without a further
      pass. Verdict, folded sibling and the reviewer's work log:
      `docs/reviews/2026-11-09-0126-private-state-type-only-cold.md`.
      🎯 Owed to the principal (rule 3), all ten, recommendation in each finding's
      counsel: **TY1** MODERATE, `RECORD.md`'s closing-entry block still says a private
      repo is "named generically" (the old posture), contradicting the new rule at its
      point of use; **TY2** MODERATE, the rule works per sentence, so an allowed act
      sentence plus a type-only condition sentence in one entry rejoins the name to the
      condition. Minor: **TY3** `namescan` and two skill prompts apply a stricter
      posture than the ADR's "naming stays allowed", unnamed by either text; **TY4** the
      ADR's scanner-item reference points at the wrong board section; **TY5** the rule
      is not at its points of use (closing-entry spec, review-brief skill, fleet-pins
      command), a silent cut from the draft; **TY6** the ADR's review line names no
      brief or pointer; **TY7** part (b)'s answer is an unmarked drafter's reading;
      **TY10** "the work in flight inside it" (type-only) conflicts with the allowed
      "Session ran in X to land item X". Notes: **TY8** a type only one repo fits needs
      a worked example; **TY9** the 2026-11-09 correction sits in the Decision, not a
      dated Addendum.
      Routing: the fixes are doctrine edits in this repo (`RECORD.md`, the ADR, the
      review-brief skill, the fleet-pins command, item `030/070`), Sonnet-tier once
      ruled; the reviewer's counsel suggests the reworded clauses.
