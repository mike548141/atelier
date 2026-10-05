- [x] **`--think` is a flag that no longer does anything.** The harness stopped
      writing thinking text to the log — blocks carry a `signature` and no
      content, so `readTurns`' `(b.thinking || '').trim()` gate finds nothing to
      render. Confirmed behaviourally as well as by census (9 text-bearing blocks
      in 24,856, none after 2026-07-04). A flag that silently does nothing is the
      defect; the fix is not obvious and is a judgement call about how loud to
      be — a `NOTES` line in the man page, or a one-line notice when `--think` is
      passed against a log with no thinking text. Grounding →
      [`cctranscript.search.design.md`](../../../instruments/cctranscript.search.design.md) §5.

      ✅ **Closed 2026-10-05 — delivered by the item's own first option**
      (queue run, Opus 5.5). The man page's `--think` entry now says plainly
      that the flag renders no thinking turns on a current session, with the
      measurement behind it (31,800 blocks, 9 with text, none after
      2026-07-04), and that `--search` offers no thinking layer for the same
      reason. That is the "`NOTES` line in the man page" this item named. The
      runtime notice was the alternative, not a second requirement.
