- [x] **High-entropy hits in a tracked data export** — ruled and executed
      2026-07-28. A business-system export committed to a repo, carrying
      token-shaped values. Three things generalise, and none of them were
      visible before the triage actually ran:
      **(a) Read what the values ARE, not just that they are high-entropy.**
      Here every hit sat on one field, and that field held customer-facing
      capability links — URLs whose unguessability *is* the access control.
      That is neither an API key nor a false positive, and the right action
      follows from the semantics, not the entropy score.
      **(b) A line-level allow-marker is not always available.** In a `.json`
      file it is impossible: JSON has no comment syntax, so the marker either
      breaks the file or is absorbed into a data value and falsifies it. Tested,
      not assumed. Where that holds, the accept branch collapses onto the
      file-scoped ignore — so the four branches are not always four.
      **(c) The scanner going green can be the failure mode.** Removing the file
      from the working tree clears the finding while changing the exposure not
      at all; the data stays one `git show` away. Deleting is still not one of
      the options — but *untracking* is the shape the mistake actually takes,
      and it looks like a fix on the board.
