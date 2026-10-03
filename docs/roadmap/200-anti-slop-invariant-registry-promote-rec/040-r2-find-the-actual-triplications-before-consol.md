- [x] **R2 — find the actual triplications before consolidating any of them.**
      Mike's premise is that points are stated three times over; this session
      wrote the *rule* for handling that but did **not** survey the corpus, and
      guessing which passages are redundant is how a consolidation drops two of
      three real facets. The work: a duplication pass over `docs/method/` +
      `docs/build/` + the stamped copies in `skills/` and `templates/`, keyed on
      claims rather than phrases, producing a ranked list of *independent*
      restatements (the defect) separated from *stamped* copies (the mechanism
      working). Pairs with D2 — `stampscan` exists to watch the second class and
      is shelved, so the stamp discipline is currently convention watched by
      nothing.
      ---
      ✅ **SURVEYED 2026-10-03 (queue run, read-only, keyed on claims).**
      Scope: all of `docs/method/` (SIGNING grepped only), `docs/build/`
      and its templates, the four skills, `commands/` and `session-open/`.
      **68 multi-stated claims: 7 stamped, 20 pointer, and 41 independent
      restatements**, which is the defect. Only the floor block is
      *mechanically* stamped. Three artefacts carry a "stamped copy" header
      that nothing watches (`skills/review-brief`, `skills/queue-run` and the
      template reviews README). So D2's "stamp discipline is convention
      watched by nothing" is measured, not just feared.
      **Eleven copies already disagree**, and those are filed as defects in
      `100` with file:line evidence. The rest of the top 25, ranked by drift,
      then load, then copy count:
      1. sync bookend: status first, then stop and move (contradicts, `100`
         C1);
      2. always-confirm floor membership: five lists, three memberships (C7);
      3. what earns review: six copies, drifted (C9);
      4. naming a private repo in a public record: five docs in tension;
      5. remote-creation authority (C2);
      6. harvest as a close step (C3);
      7. when to write an ADR: one test against two prongs;
      8. hard-coded tiers in templates (C8);
      9. scope of "no personal data" (C11);
      10. the scanner roster: "four" against 15 in `floor --list`.

      Ranks 11–25 currently agree in substance:
      rule-4 cold spawn and tier (7+ copies) · cheapest-model / state your
      tier (9+) · a ruling is challengeable on its briefing · capacity never
      picks the tier · claim before work · per-item close · the allowlist is
      not committed · push to public is publication · burned secret: rotate
      now · a standing credential is tracked debt · advisory is debt with a
      review-by · record identifiers · one fact, one home (the most copies,
      and mostly pointers) · hand up noisily · encode the policy.
      **Limits:** `docs/decisions/`, `docs/reviews/`, tool docstrings and
      man pages were not covered. Agreement for ranks 11–25 is by facet,
      not a sentence diff. The pointer and stamped sets are the least
      verified. No history was mined, which is R1's job. Consolidation is
      the next step and is not started. The item asked for the survey
      *before* any consolidation, so this closes it.
