- [x] 🔎 **conflictscan's open-conflict state runs across staged hunks**
      `[S][tools]`. Found 2026-10-16 by the `300` worker, not reproduced and
      not fixed there, because it is old behaviour outside that item. On the
      staged plane conflictscan walks a file's added lines in order and
      carries its "inside an open conflict" state from one hunk to the next,
      as if the added lines were consecutive. So an opener added in one hunk
      can make a bare `=======` added in a distant hunk read as a separator.
      That state gates the separator and base rules, which exist to avoid
      flagging a bare `=======` that is ordinary text (the module
      docstring's section on the ambiguity). **The work:** reproduce it
      first. If it holds, reset the state at a hunk boundary, which
      `report.staged_added`'s line numbers make visible as a gap, and add a
      test. A finding that blocks wrongly here costs an allow-marker on a
      correct line.

      ✅ **Closed 2026-10-16: reproduced, and the fix rejected on evidence**
      (1501 UTC queue run). A Sonnet worker reproduced it: an opener staged
      at line 3 and a bare `=======` at line 26, unchanged lines between,
      reported a separator at 26. Its fix (`d79492b`, not merged) reset the
      state at any gap in the added lines' line numbers. The orchestrator
      tested that fix against the commonest real case before merging, and
      it loses a true finding. In a bad merge staged against `HEAD`, the
      "ours" lines between the opener and the separator are unchanged, so
      they show as context, a gap. Old code reports opener, separator and
      closer. The fix reports opener and closer only. Both still block. The
      original defect costs less: its false separator can only appear
      beside a genuine opener that already blocks the commit, and it goes
      away once that opener is resolved. So it never reaches a correct
      line on its own. Nothing changed in code. If it is ever worth more,
      the fix is a separator reported with its hunk, not a state reset.
