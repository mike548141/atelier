- [x] **A re-check of fixes is owed on what the fixed findings were, not only on whether
      🔒 Claimed by session 9c5fa72c (`atelier-fa`, Opus 5.5), principal-opened by
      `/atelier:work run`.
      (claimed 2026-11-27-0915, wt: atelier-qr-9c5f-reviewbar)
      one was a MAJOR** `[S][doctrine]`. The principal's typed words, 2026-11-27 ~01:55 UTC
      (session 4ce066ba, `atelier-c1`, AskUserQuestion, in place of the options), on
      releasing `160/1870`, verbatim: *"Release it as per your recommended option - but to
      clarify we now have a better definition than just "are there any major findings""*.
      **The gap.** `REVIEW.md` § *When a finding is fixed before use, and when fixes earn a
      re-check* defines an issue (failure shown happening) against a risk, and five kinds
      of risk fixed before use (`460/050`). Its re-check sentence still keys off severity
      alone: *"A re-check of fixes is owed only when the pass being fixed returned a
      MAJOR"*, and the chain stops "at the first pass that returns no MAJOR". The session
      that asked him put the question in those terms, and he corrected the framing.
      **Owed:** rewrite the re-check trigger and the chain's stop in terms of the issue and
      risk definition (for instance: owed when a fix closed an issue, or one of the five
      kinds of risk fixed before use; not owed for fixes of plain risks), keeping the
      2026-07-13 stop he applied to code (*"Apply to code too (Recommended)"*). The exact
      wording is the building session's; where it goes beyond his words, put the reading
      to him as options. Doctrine, so its review folds into `160/1880` (open, unbriefed,
      same section).
      ✅ **Done 2026-11-27 (session 9c5fa72c, `atelier-fa`, an Opus worker).** `REVIEW.md`
      § *When a finding is fixed before use, and when fixes earn a re-check*: a re-check is
      owed only when the pass being fixed returned a MAJOR that the section fixes before use
      (an issue, or one of the five kinds of risk), as the step-4 decision classes it; the
      chain stops at the first pass with no such MAJOR, and a count that is not falling
      means stop and ask him. His words above are quoted there. The 2026-07-13 stop is kept
      (a pass with no MAJOR still closes); *Applying decisions to doctrine* counts the same
      MAJORs, and `CHANGELOG.md` replaces the 2026-11-26 line.
      **Beyond his words, for him to confirm (asked at the run's close):** keeping MAJOR
      beside the class (the text marks it the repo's reading). The other reading, any fixed
      issue or five-kind risk earning a re-check whatever its severity, would have owed
      `160/1870`, which he released: `DP` returned issues shown by probe (`DP1`) but no MAJOR.
      - Commitment: whether every chain of fixes gets another cold pass, and when it stops.
      - Worst failure: a fixed issue that needed a second look closes unseen, or chains of
        re-checks on plain risks resume.
      - Why the floor misses it: no test reads what doctrine means; a stop set wrong shows
        only as passes run or skipped.
      **Review:** folds into `160/1880` (open, unbriefed, same section); its delta is widened
      to this commit.
