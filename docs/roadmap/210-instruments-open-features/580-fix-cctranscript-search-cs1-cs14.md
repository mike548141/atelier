- [x] 🔧 **Fix `cctranscript --search`: all fourteen findings CS1–CS14, as
      the reviewer advised.** His pick, 2026-11-24 (session edf25bd3,
      AskUserQuestion; quoted in full on `160/010`): *"Fix all as advised
      (Recommended)"*. The findings and their advice are in
      [`reviews/2026-08-15-1032-cctranscript-search-cold.md`](../../reviews/2026-08-15-1032-cctranscript-search-cold.md).
      The three MODERATEs lead: CS1, the `--regex` gate and the probe read
      different texts, so a pattern with a quote, a backslash, a newline
      class or an anchor never hits (and the manual's workaround fails);
      CS2, a trailing `--search` with no term renders a transcript at exit 0
      where the manual says exit 2; CS3, no threat step and no caution in the
      man page, README or help that its excerpts of a private corpus must not
      be reproduced in shared records.
      **First,** the findings are 100 days old: re-check each against the
      tool at HEAD and record any already gone, with the commit that removed
      it, rather than fixing it twice. CS13 (the design was never reviewed
      before it was built to) is answered by this item's own cold pass.
      *Tier:* build tier (Opus or Sonnet); no review tier. *After:* a rule-4
      cold pass queued as a `160/` item, run in a later drain on his
      approval.
      ✅ **Done 2026-11-25 (session f8dd3843, `atelier-31`, queue run; an Opus worker built
      it).** Re-checked first: CS8 was never present (the timer has started before the
      pool is built since the landing commit `0eb03ed`; a comment and a man-page note now
      say `elapsedMs` includes pool building); half of CS11 was gone (the `--list` crash,
      `c11c5371`, `160/680`). Fixed: CS1 (a `--regex` is gated on the raw log only when a
      token check proves the raw text cannot hide a match, otherwise every swept log is
      parsed and `meta.gateBypassed` says so; `^`/`$` bind per line), and beside it a
      literal term with a space missing a slash command (now gated on its longest
      whitespace-free part); CS2 and CS10 (exit 2 with the reason); CS3 (a PRIVACY section,
      README sentence, `--help` line, `meta.privacy`, a threat step in the design); CS4,
      CS5, CS6, CS7, the other half of CS11, CS9, CS12, CS14. CS13 is answered by the cold
      pass queued as `160/1840`. Tests: 126 in `instruments/cctranscript.test.js` (113
      before), 15 of them failing against the old tool. The same collapsed figure also sits in
      the frozen archive (`990-done-before-the-split/README.md`); that is a record, kept as
      written.
