- [~] (claimed 2026-10-16-1556 UTC by queue run abe96d8d, a worker) 🔎 **conflictscan's open-conflict state runs across staged hunks**
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
