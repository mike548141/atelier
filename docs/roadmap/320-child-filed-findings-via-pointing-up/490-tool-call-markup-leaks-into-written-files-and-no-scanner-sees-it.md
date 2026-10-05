- [ ] 🔎 **Hand-up: tool-call markup leaks into files an agent writes, and
      no floor scanner sees it** `[S][tooling]`. Filed by a private child on
      2026-10-02 via § *Pointing up*, by direct write into the parent's tree,
      with the PR opened before stopping. The child is not named, and the
      branch carries no repo token.

      **What was found.** Files written with the harness's file-write tool
      sometimes end in two literal lines, `</content>` then `</invoke>`. That
      is the tool call's own closing markup, saved into the file body. The
      floor passed every one of them.

      **Evidence.**
      - In this repo, two committed session records end that way:
        `docs/sessions/2026-07-22-0245-interruption-resilience-doctrine.md`
        (lines 100–101) and
        `docs/sessions/2026-07-22-1036-invariant-candidates.md` (lines
        291–292). Run `git grep -n -E '^</(content|invoke)>'` to see them.
      - In the child: five committed docs from 2026-10-01 and 2026-10-02, and
        two agent memory files, one of them this repo's own project memory.
        All were cleaned there.
      - **The child reproduced it on its very next write** in the same
        session. So this is a live failure, not a fossil.

      **Why it matters.** It is small but silent. It corrupts the content of
      records, docs and memories, it reads as noise, and nothing flags it. A
      memory file that ends in markup is loaded into every later session.

      **Proposed check, for atelier to weigh.** A floor rule, perhaps in
      `conflictscan` (the same "leftover markers" class), that flags a line
      that is exactly `</content>`, `</invoke>`, or starts with
      `<invoke name=` or `<parameter name=`, in staged text files. Keep an
      allow-marker for docs that quote the markup on purpose. The child is
      using a manual `tail -n 3` after each write until something structural
      exists.

      **Not done here:** the two session records above are left untouched.
      Fixing atelier's records is atelier's call.

      📎 **2026-10-05: a third atelier instance**, found by a queue-run worker:
      `docs/sessions/2026-07-22-1036-invariant-candidates.md` (the `200`
      mining record) also ends in committed tool-call markup. It is filed
      with that record's other stale statements as `200/110`.
