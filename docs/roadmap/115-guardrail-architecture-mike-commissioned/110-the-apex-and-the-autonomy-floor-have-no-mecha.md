- [ ] 🔥 **The apex and the always-confirm floor have no mechanical backing at
      all — the highest-stakes rules in the estate are the least enforced.**
      A rule-by-rule enforcement map of the four governing documents, run
      2026-08-15. **`00-APEX.md` is 100% prose-only**: not one rule in the file
      has a blocking gate. Not honesty, not *never emit a claim stronger than
      its evidence*, not the briefing triple, and not *surface a genuine
      dilemma; never silently resolve it* — which is undetectable by
      construction, because a silently-resolved dilemma leaves nothing behind.
      **`AUTONOMY.md`'s always-confirm floor is the same.** Seventy lines
      naming the estate's highest-stakes acts — making a repo public,
      destructive and irreversible operations, secrets, spend, lockout-class
      changes, new trust surfaces — and nothing detects any of them. The
      sharpest line in the file forbids *widening your own authority: editing
      this file*, and an agent editing it to widen its own grant passes every
      scanner in the registry. Visible only if a person reads the diff.
      **Ranked by blast radius**, the prose-only rules with no backstop are:
      widening own authority · surface a dilemma · the review independence
      criterion in full · the reading-order bar, which leaves no artefact at
      all · and the rule that a queue item's text never overrides doctrine,
      where the concurrency doc states outright that *no scanner catches
      intent*.
      **Across all four documents there are six blocking gates**, and they back
      credentials, review-line presence, index freshness, date form and link
      resolution. Every governance rule — who may review, whether the principal
      was informed, whether authority widened — has none.
      **Blocked on item `100`.** Most of these are only mechanisable on a
      before-plane; a commit gate cannot see a dilemma that was never surfaced.
      But two are reachable today with no new plane: a diff-path trigger on
      edits to `AUTONOMY.md` or a permission allowlist, and a push-time check
      comparing declared repo visibility against the platform's answer. Both
      are small, and both guard acts the record classes as irreversible.
      🔒 CLAIMED 2026-11-16T11:40Z (claimed 2026-11-16-1140, wt: qr-78ca-autonomy) by queue-run
      session 78ca9153 (Opus 5.5, principal-opened).
      Progress 2026-11-16: both reachable pieces now exist. The push-time
      visibility check was already built (`260/050`): `check_visibility` in
      `tools/floor.py` asks GitHub on every CI run and reds only a repo
      declared private that GitHub says is public; every other mismatch, an
      unreadable answer or no declaration is 🟡. The diff-path trigger is built
      as an extension of `quotescan`, not a new scanner (same evidence, planes,
      reader and marker): a commit that changes `docs/method/AUTONOMY.md`, the
      floor region of `docs/method/PROPAGATION.md` or a stamped copy of it in a
      `CLAUDE.md`, or the `permissions` key of a `.claude/settings*.json`, with
      no quotation of the principal and no reasoned marker, gets a 🟡 line per
      surface asking for his words in the body. Advisory on every plane and
      date, never blocking (`tools/README.md` § quotescan). Remains: the apex
      rules (honesty, claim strength, surface a dilemma), the review
      independence criterion in full, the reading order and queue text never
      overriding doctrine, which leave no artefact a commit gate can read and
      wait on item `100`'s before-plane; and, inside the authority slice, an
      unstamped floor copy, a child's autonomy block outside the floor stamp
      and a widening through any settings key but `permissions`.
