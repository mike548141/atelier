- [x] **Build a generic mechanism keeping any hand-maintained index true to
      the directory it maps — option C, chosen over the counselled
      single-index build.** Grounding: the decisions index drifted twice in
      three weeks (five records unlisted; then a retro-distilled entry
      naming a wrong path, caught only because pathscan landed the same
      day). Counsel recorded with the ruling: C is built on one bitten
      instance, so the over-engineering risk is real and owned. **Design
      constraint binding the pickup: census first** — enumerate every
      hand-maintained index across the estate (decisions, any child-repo
      equivalents, instrument/tool catalogues) before designing; if the
      census finds the class is one member, that finding returns to Mike
      before any generic machinery is built. Likely per-directory
      instantiation for decisions: self-describing records (each new record
      carries its own one-line summary; the index is generated and
      match-checked; frozen records blameless with their hand lines kept —
      the reviewscan precedent). Self-authored mechanism when it lands ⇒
      rule-4 ⏳ at landing.
      ---
      📊 **CENSUS DONE 2026-10-03 (queue run, read-only). The class has MANY
      members, so the one-member fallback is off the table and the build
      stands as ruled.** All 31 git repos in the estate were swept. Repo
      identities are withheld here, which leaves classes and counts only.
      - **22 hand-maintained indexes, of 7 firm kinds, in 14 repos.** By
        kind: decisions index (14 repos, 11 with content), session-log index
        (4), tool or instrument catalogue (3), method/docs index, research
        index, reviews index, and one routing manifest. Root-README layout
        sections are a borderline 8th kind and were not counted.
      - **Drift today, measured by name-match:** 4 firm. In atelier, the
        decisions index was missing 1 ADR and the tools catalogue was
        missing 4 scripts. One private repo's tool catalogue is missing 6,
        and an archived repo has 1 dangling link. 3 more are probable but
        unverified: two session indexes, with 7 and 102 entries unlisted by
        name, where early entries may cite files differently, and the
        manifest.
      - **Guarded: none, against unlisted files.** Link resolution
        (`linkscan`/`pathscan`) catches only the listed-but-missing
        direction. That is the same half-guard `320/430` found for the
        session-log index.
      - **What drifts is catalogues and session indexes, not decisions
        indexes.** The decisions indexes are mostly clean now. That bears
        on the design: the likely per-directory instantiation above was
        written for decisions, and the census says it has to handle
        catalogues first.
      🧹 **atelier's own drift was fixed in the same sitting.** The board-
      store ADR is now indexed, and `signscan`, `signfleet` and `floorfleet`
      have catalogue entries. `filewalk.py` is deliberately left
      unindexed, because its documentation gap is FW2, a finding in the
      ruling round.
      **Next is the design and build.** It is self-authored machinery, so a
      rule-4 `⏳` is owed at landing. It is not started, so the item stays
      `[ ]`.

      ✅ **Built and merged 2026-10-05: `tools/indexscan.py`** (queue run, an
      Opus 5.5 worker; `8d10487`). An index opts in with one declaration near
      its head, `<!-- indexscan:maps dir=<path> match=<glob> [exclude=…]
      [before=YYYY-MM-DD] -->`. The guard then reports every entry in that
      directory that the index never names, as a link or a code span.
      `before=` keeps frozen records blameless, and `indexscan:allow: <entry>
      <reason>` exempts one entry with a reason. A marker that no longer
      exempts anything is reported as stale. Listed-but-missing stays with
      `linkscan` and `pathscan`, which already catch it; a test pins that.
      **No declaration, no check**, so no child is affected until it declares
      an index. It is registered **warn-only** on both planes and declares
      that it makes the failure cheap and forbids nothing.

      **Adopted in atelier on four indexes:** decisions, tools, instruments
      and sessions. Decisions and instruments were clean. Tools had two
      unlisted helpers whose catalogue entries are already owed by open review
      findings (FW2, AM5), so those carry allow-markers that go stale when the
      entries land. The session index had **ten unlisted detail files**. The
      orchestrator read each one: all ten are records-only captures or
      annexes, each reached from another record, so each carries a reasoned
      allow-marker rather than a back-dated index line. Evidence: 29 new
      tests, 194 across the affected modules, Node 406/406, CI plane exit 0,
      and about 2.8 s on atelier's tree. The code pass is queued at `160/700`.
      The unlisted-file half of `320/430` is now mechanised, noted there.

      **Stated limits:** any link or code-span mention counts as listing an
      entry. An index line whose date or slug disagrees with its file is not
      checked; that is `320/430`'s second gap. Non-Markdown indexes are out of
      scope.
