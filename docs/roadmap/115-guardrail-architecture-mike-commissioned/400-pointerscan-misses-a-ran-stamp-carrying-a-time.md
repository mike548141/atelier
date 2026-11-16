- [x] 🔎 **`pointerscan` misses a RAN stamp that carries a time, so four
      landed pointers read as a lost queue entry.** Found 2026-11-16 UTC by
      queue run 78ca9153 at its first commit: the hook's `pointerscan` printed
      four `[state]` findings (`160/994`, `160/1080`, `160/1250`, `160/1420`),
      each saying its title claims a queued review and "nothing records the
      pass as run". Each item does record it: "PASS RAN 2026-11-15T20:40Z",
      "PASS RAN 2026-11-16T06:01Z" and the like, the stamp the 2026-11-15/16
      drain wrote. The `_LANDED` pattern ends its date with `\b`, and between
      a date's last digit and ISO 8601's `T` there is no word boundary, so a
      dated-and-timed stamp never matches. Warn-only today, but the finding is
      false and teaches readers to skip the check.
      **Owed:** end the date with a not-a-digit lookahead so a time may
      follow, with a test for the timed stamp.
      🔒 CLAIMED 2026-11-16T11:12Z (claimed 2026-11-16-1112, wt: none) by
      queue-run session 78ca9153 (Opus 5.5, principal-opened).
      ✅ FIXED 2026-11-16 UTC: `_LANDED` ends the date on `(?!\d)`; a
      test pins the timed stamp; the tree-wide run is clean (the four findings
      are gone). Warn-only scanner, so no cold pass queued.
