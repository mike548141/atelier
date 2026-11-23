- [x] 🔎 **`licenscan` cannot read a CC0-1.0 licence file, so a child that
      declares it fails the floor.** Reported 2026-11-20 by a private child's
      adoption run (started by session 19378351), class only. Declaring
      `"licence": "CC0-1.0"` in `.atelier-floor.json` fails with an
      expect-mismatch, because the scanner does not recognise the CC0 text in
      `LICENSE`. The child left the licence undeclared, which skips
      `licenscan` entirely: harmless while the repo is private, a gap the day
      it is published. **Owed:** recognise CC0-1.0 (and check the other
      public-domain dedications), with a test.
      ✅ **Done 2026-11-23** (queue run c7a1e36e, inline): `licenscan` reads
      a CC0-1.0 body (its "CC0 1.0 Universal" title line), the id and its
      short spellings, and PyPI's CC0 classifier, which sits outside "OSI
      Approved"; CC0-1.0 is in the permissive family. Checking the other
      dedications found two more gaps: a **0BSD body read as ISC** (both open
      with the same grant sentence; ISC is now told apart by its
      notice-retention clause), and **Zlib had no text signature at all**.
      The Unlicense was already read. Tests in `tools/test_licenscan.py`,
      nine new assertions that fail on the old scanner; the test's ISC
      fixture was a truncation that stopped before the clause, and now holds
      the real opening paragraph. Cold pass queued as `160/1730`.
