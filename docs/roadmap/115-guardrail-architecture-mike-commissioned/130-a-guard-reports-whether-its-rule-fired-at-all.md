- [ ] **A guard reports whether its rule fired at all, and over what — so
      "clean" and "scanned nothing" stop looking identical.** The cheapest
      finding of the whole commission, and it is imported rather than invented:
      assertion verification calls this vacuity, and treats a property that
      passes without ever exercising the behaviour it guards as a defect in its
      own right, on the stated ground that trivially-valid properties give a
      false sense of safety. The standard remedy is to require evidence the
      antecedent fired.
      **The estate has already shipped the bug this catches.** A scanner given
      an absolute path matched no repo-relative entry, emptied its own file
      set, scanned nothing and exited 0 — indistinguishable from a clean run. A
      second instance: a check whose skip-list silently excluded whole archive
      stores while printing an affirmative clean claim over files it never
      opened. Both were found by a person, later, not by the tool.
      **Doctrine already demands the sibling of this and stops one step short.**
      `GUARDS.md` requires a count of what was suppressed and by which
      mechanism, never a bare tick — that is *allowance* accounting. Nothing
      requires *coverage* accounting: how many files were opened, how many
      lines the rule evaluated, whether any rule matched at all. The reasoning
      for the first applies unchanged to the second.
      **Small, and it composes with the item above.** A guard that reports its
      own coverage makes the grounding replay checkable at a glance: a replay
      that fires on zero of its incidents is the same signal as a scan that
      opened zero files. Both currently render as success.
      **A worked caution from the measurement.** The same scanner run two
      defensible ways differed threefold — through the floor wrapper, and
      invoked directly, where it walked a nested worktree and counted the tree
      twice. Coverage reporting would have made that visible in the output
      rather than in a footnote.
