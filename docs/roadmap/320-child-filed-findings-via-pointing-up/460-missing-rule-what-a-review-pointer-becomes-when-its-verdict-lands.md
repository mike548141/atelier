- [x] 🔎 **MISSING HOUSE RULE — what a `⏳` review pointer becomes when its
      verdict lands** `[S][doctrine]` — handed up by a private child
      2026-09-27 via `PROPAGATION.md` § *Pointing up*. Class-only: no child
      name, no child paths.

      ## The gap

      The board legend (`docs/roadmap/README.md`) and `REVIEW.md` define the
      `⏳` pointer's shape, who may take it and on what tier — and stop at the
      take. Neither says what the pointer **becomes** once the verdict lands
      and findings are owed a ruling. A child's cold pass graded the gap
      minor: each taker invents a transition, and a `⏳` left in place reads
      to `pointerscan` as still current.

      ## What the house actually does — measured, not asserted

      Read at `c600f62`, across the `rule-4-cold-pass-queued-*` and
      `rule-4-review-queued-*` item files: a landed pointer is **rewritten in
      its own file**, never closed and re-opened elsewhere. It stays `[ ]`
      and its lead swaps `⏳` for 🎯 (cycle closed, rulings owed) or 🛑
      (cycle open on a MAJOR), and flips to `[x]` once nothing is owed. One
      mixed instance (`[x] 🎯`) exists. The child had followed a different
      precedent of its own — close the pointer `[x]`, open a separate 🎯
      rulings item — until its principal ruled on 2026-09-27: *follow what
      atelier says.* Atelier **does** one thing and **says** nothing, so the
      child is now following an unwritten practice.

      ## Proposed

      One sentence in the board legend beside the `⏳` definition, stating
      the in-place transition above as the rule, with the `[x] 🎯` shape
      either named or retired. Consideration and remediation are atelier's;
      the reporting child stops at this report.

      ✅ **Answered 2026-10-05 by `130/020`.** The board legend now says what a
      `⏳` pointer becomes when its verdict lands: the glyph comes off in the
      landing commit, and the work-owed tri-state takes over, led by 🎯 while
      Mike's ruling is owed. An `[x]` line that still carries 🎯 reads as done.
      The reporting child hears the answer through the pointing-up route at
      its next pin bump.
