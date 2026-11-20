- [x] 🎯 **D2 — `stampscan`: fix at the parser, or shelve it.**
      (claimed 2026-08-05-1243, wt: queue-batch-0806) Built, tested,
      and **not wireable as built** — re-verified 2026-07-27, the live tree
      exits 2 today. Three MAJOR: marker recognition is context-blind, so any
      document that *describes* the syntax reds the scan as a config error that
      `--warn` cannot suppress; a narrowing declaration accepts narrowing to
      nothing, so one word vacates the whole check while it reports clean; and
      the template ships markers whose source cannot resolve in any scaffolded
      child, which would red future scaffolds estate-wide once registry-wired.
      Reviewer's counsel is explicit — **do not wire, not even advisory** —
      until the parser strips fenced and inline code, an ignore file ships, and
      the narrow-to-nothing hole is closed or explicitly accepted. Verdict:
      [stampscan S4 cold pass](../../reviews/2026-07-26-2215-stampscan-s4-cold.md).
      **RULED 2026-08-04 (Mike): FUND THE FIXES NOW** — chosen over the
      counselled shelve. All three preconditions built (code-span-aware
      parsing, the ignore file, narrow-to-nothing closed), then wire
      advisory per the reviewer's bar. Work owed: one build item.
