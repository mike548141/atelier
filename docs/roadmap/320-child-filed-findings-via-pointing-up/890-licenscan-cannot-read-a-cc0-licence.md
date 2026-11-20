- [ ] 🔎 **`licenscan` cannot read a CC0-1.0 licence file, so a child that
      declares it fails the floor.** Reported 2026-11-20 by a private child's
      adoption run (started by session 19378351), class only. Declaring
      `"licence": "CC0-1.0"` in `.atelier-floor.json` fails with an
      expect-mismatch, because the scanner does not recognise the CC0 text in
      `LICENSE`. The child left the licence undeclared, which skips
      `licenscan` entirely: harmless while the repo is private, a gap the day
      it is published. **Owed:** recognise CC0-1.0 (and check the other
      public-domain dedications), with a test.
