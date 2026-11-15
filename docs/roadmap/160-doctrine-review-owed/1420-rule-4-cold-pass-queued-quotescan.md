- [ ] 🎯 **Rule-4 cold pass queued: `quotescan`, a quote of the principal on commits touching his prompt, warn-first (`160/900` QK1, `320/810`), and `leakscan --messages` (`320/550`).** The authoring session (a
      principal-opened Opus 5.5 queue run, session d0ca5d24, 2026-11-09 UTC,
      which dispatched the worker that wrote it) queues this and does not
      take it.
      *Tier:* Fable, the principal-named review tier, checked at selection;
      the pass waits for his explicit permission for Fable work.
      *Pass type:* code cold pass, per `method/REVIEW.md` rule 4.
      *Delta, scoped to paths:* `tools/quotescan.py`, `tools/test_quotescan.py`, its registry entry in `tools/floor.py`, the `--messages` mode in `tools/leakscan.py` and its test — the commits that add them, on `main`.
      *Questions worth the pass's time:* whether any quotation marks at all satisfy it; whether `--messages` reports only its own findings and stays read-only.
      *Intent record:* `160/900`, `320/810`, `320/550`.
      📝 BRIEF WRITTEN 2026-11-14 by session 5b3a35e9 (Opus 5.5), a headless
      brief-writer started by an estate health sweep, orchestrator session
      58027096: `docs/reviews/2026-11-14-0322-quotescan-and-leakscan-messages-cold.md`,
      with its `.deferred.md` sibling. Neither session may run the pass. Review NOT
      run. The pass waits for a criterion-passing cold Fable session and the
      principal's explicit permission for Fable work.
      🔒 CLAIMED 2026-11-15T19:22Z UTC for the cold pass, in Mike's weekly Fable drain
      (his `/fable-drain` order, 2026-11-16 06:53 NZDT; approval lapses at the
      reset, 2026-11-15 23:00 UTC). Orchestrator: a headless Opus 5.5 session
      started by drain session 21a271a5, a rule-4 off-tier orchestrator that
      holds the context partition, forms no finding and writes no severity.
      Reviewer: Fable 5.1, tier checked at selection, spawned by that
      orchestrator. Neither is a barred session (5b3a35e9, 58027096,
      d0ca5d24). The sibling is held out of the worktree until act 1 is
      committed. The item's "waits for his explicit permission for Fable
      work" is met by that drain order.
      ✅ PASS RAN 2026-11-15T19:52Z UTC (acts 1 and 2 by the Fable 5.1 reviewer; the
      sibling folded below the verdict by the off-tier orchestrator, which
      formed no finding): `docs/reviews/2026-11-14-0322-quotescan-and-leakscan-messages-cold.md`.
      *Verdict:* PASS-WITH-FINDINGS, 1 MAJOR, 4 MODERATE, 7 minor, 2 notes
      (QT1–QT14; QT13 and QT14 formed at reconcile).
      *Standing MAJOR:* QT1, quotescan reads the shape of a quotation, not
      his say-so (a quoted file name passes, a wrapped real quotation
      fails), and on 2027-05-31 that shape starts blocking commits; the
      verdict says the flip should not happen as built unless he rules
      otherwise.
      🎯 *His to rule (rule 3: guard code guarding his own text, so the
      author applies nothing):* every finding, MAJOR first. Asked plainly:
      on 2027-05-31 a check that only looks for quotation marks starts
      refusing commits to his session-open prompt. Options: (a) keep it
      warn-only with no date until a check can read a real reference to
      his words; (b) change it to require a reference (a tracked record
      path, or an item id plus a date, holding his words); (c) let it flip
      as built. Reviewer's counsel, recommended here: (a) now, (b) as the
      follow-up. Then, bulk: QT2–QT5 (MODERATE: committed messages lose
      `#` and scissors lines to cleaning; the trailer skip drops any
      trailer-shaped line; an option-shaped spec makes `git log` write a
      file and still reads clean; the CI plane misses a merge's own change
      and treats a read failure as silence), QT6–QT10 and QT13–QT14
      (minor), QT11–QT12 (notes): apply as the verdict's follow-up
      checklist counsels.
      *Routing:* the fixes are atelier work on `tools/quotescan.py`,
      `tools/leakscan.py` and `tools/commitmsg.py`, queued after his
      rulings; the changed tools earn their own cold pass.
