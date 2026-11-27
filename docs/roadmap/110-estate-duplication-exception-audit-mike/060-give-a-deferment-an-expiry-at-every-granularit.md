- [~] **Give a deferment an expiry at every granularity, not just `advisory`.**
      🔒 Claimed by session a2097e54 (`atelier-b2`, Opus 5.5), principal-opened by
      `/atelier:work run` (part 4, line-marker granularity, warn-only).
      (claimed 2026-11-27-1226, wt: atelier-qr-a209-linemarker)
      Raised by the ruling above. Today `review-by` is a floor-config field, so
      the only declarable deferment is a whole check. The two cases just dated
      are path-level, and a line marker has the same hole — `<guard>:allow:` is
      pure acceptance by construction, which is fine until someone writes one
      for a thing they mean to fix. Cheapest shape that keeps the ignore-file
      format: an optional `review-by: YYYY-MM-DD` recognised in the comment
      block attached to a glob, reported on the floor line and the fleet board
      exactly as an advisory's expiry is, red when lapsed. Deliberately not
      built here: it is a scanner-loader change across ten ignore-file readers
      plus board rendering, and it wants its own session. Until it exists,
      a path-level deferment's date is a promise, not a gate — which is
      precisely the thing `GUARDS.md` says a deferment must not be.
      **Slice 1 built 2026-11-16 (queue run 78ca): the shared parser and one
      adopter.** `allowmarker.ignore_deferments` reads `review-by: YYYY-MM-DD`
      from a glob's attached comment (stanza or trailing reason) with the
      loader's own grammar, marks a date lapsed when strictly before the UTC
      date given, and reports an unreadable value as malformed rather than
      dropping it. `wrapscan` is the first adopter: a `deferments:` line after
      its `suppressed:` line, 🟡 per lapsed or malformed date, `deferments` in
      `--json`. **Warn-only**: no exit status changes, because children run
      the floor at `@main`. Syntax documented in `tools/README.md`
      § *Allow markers and ignore files*. **Remaining:** (1) adopt the reader
      in the other ignore-file scanners, `leakscan` (and `.leakscanbinaries`),
      `secretscan`, `conflictscan`, `datescan`, `licenscan`, `linkscan`,
      `indexscan`, `pathscan`, `sizescan`, `spellscan`, `stampscan`;
      (2) render it on the floor line and the fleet board (`floor.py`,
      `floorfleet.py`) as an advisory's expiry is; (3) the announced switch
      from 🟡 to red when lapsed; (4) the line-marker granularity the item
      names, which this glob reader does not cover. The cold pass is owed at
      (3), the slice that makes a lapsed date block: that is where the syntax
      becomes a commitment children build to (orchestrator 78ca9153's call,
      2026-11-16; this slice is additive and warn-only).
      🔒 CLAIMED 2026-11-16T11:55Z (claimed 2026-11-16-1155, wt: qr-78ca-expiry) by queue-run
      session 78ca9153 (Opus 5.5, principal-opened). Ended: that run closed;
      kept as history.
      **Slice 2 built 2026-11-23 (queue run 608d8123, a Sonnet worker, read
      by the run before landing): part (1).** All eleven other ignore-file
      scanners read `review-by` (`leakscan` over both `.leakscanignore` and
      `.leakscanbinaries`, `secretscan`, `conflictscan`, `datescan`,
      `licenscan`, `linkscan`, `indexscan`, `pathscan`, `sizescan`,
      `spellscan`, `stampscan`), each printing the `deferments:` line
      `wrapscan` prints and carrying `deferments` in `--json`; one helper,
      `allowmarker.deferment_report`, serves all twelve (`wrapscan`'s output
      unchanged). Warn-only: tests in `tools/test_ignore_deferments.py`
      compare exit status with and without dates on a tree each scanner
      blocks. **Remaining:** (2) the floor line and fleet board, (3) red
      when lapsed, where the cold pass is owed, (4) line-marker granularity.
      **Slice 3 built 2026-11-23 (same run, a Sonnet worker, read by the
      run before landing): part (2).** The floor line shows a lapsed or
      unreadable date as a 🟡 note on the check's line and a live one as
      `[n deferment(s), next review by …]`, mirroring an advisory's expiry;
      `floorfleet` gives each check with a dated deferment one row under the
      repo; both carry `deferments` in `--json`. The floor reads each
      check's ignore file through the scanners' own parser
      (`allowmarker`'s check-to-file map, tested against each scanner's
      file name), so the three surfaces cannot disagree. A repo with no
      dates prints exactly what it did. Deliberately not mirrored: an
      expired advisory's 🔴; a lapsed deferment stays 🟡. 422 floor tests
      pass. **Remaining:** (3) red when lapsed, where the cold pass is
      owed, and (4) line-marker granularity.
      **Slice 4 built 2026-11-27 (queue run a2097e54, an Opus 5.5 worker,
      branch `qr-a209-linemarker`): part (4), warn-only.** A `review-by:
      YYYY-MM-DD` in a line marker's reason now dates it.
      `allowmarker.marker_review_by` reads it with the glob form's own token
      reader (`_read_review_by`), and only from a marker the scanner's reader
      has already counted (`_read` for a scoped pattern, the blanked search
      for an unscoped one). So the marker grammar is unchanged, and a reason
      that already held the words `review-by:` exempts exactly what it did;
      the most it gains is a 🟡 line. The reason runs to the line's end, cut
      at the next `<word>:allow` head and at a `-->` or `*/` closer; a date in
      a code span is a mention. `record_marker_deferment` keeps one
      `Deferment` per file and line (the tuple gains `path`, "" for a glob).
      `deferment_lines` and `deferments_dict` render a marker by its file,
      line and marker word (`file`, `line`, `marker` in `--json`) on the same
      one `deferments:` count line as the ignore-file dates. Eight scanners
      adopt it at their reader's call site: `wrapscan`, `datescan`,
      `linkscan`, `pathscan`, `spellscan`, `secretscan`, `leakscan`,
      `conflictscan`. Syntax in `tools/README.md` § *Allow markers and
      ignore files*. Tests: `test_ignore_deferments.py`
      `LineMarkerAdopters` (each of the eight: lapsed and unreadable dates
      reported, future and undated quiet, the same exit status and the same
      `suppressed:` line with and without a date on a passing and a blocked
      tree, the JSON entry, one count line shared with globs) and
      `MarkerReviewByReader` (the shared reader's cuts and edge cases).
      **Remaining:** (3) red when lapsed, where the cold pass is owed;
      line-marker dates in `indexscan` (its marker reads an entry name
      before the reason, so the shared reader's reason span does not fit
      it), `licenscan`, `sizescan`, `stampscan` (no tally at the marker
      read) and the six scanners with no ignore file (`blockscan`,
      `attribscan`, `quotescan`, `namescan`, `pointerscan`, `reviewscan`);
      and the floor line and fleet board, which read ignore files without
      running a scanner and so do not show marker dates. **Review:** this
      slice is additive and warn-only, so it folds into the cold pass
      already owed at (3); that pass reads the line-marker syntax with the
      rest, since (3) is where a lapsed marker date would start to block.
