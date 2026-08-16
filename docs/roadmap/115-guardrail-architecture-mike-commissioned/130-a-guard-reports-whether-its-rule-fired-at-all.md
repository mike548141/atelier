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
      **The base rate, from the field that named the problem.** A hardware
      verification group measured it across first runs on new designs:
      **roughly 20% of properties passed vacuously, and a vacuous pass always
      pointed to a real problem** — in the design, the specification, or the
      environment. Not a warning that sometimes mattered; a defect indicator
      every time. If even a fraction of that rate holds here, the cheapest
      check on this board is also one of the highest-yield.
      **The same field's framing answers the harder question too.** Vacuity and
      coverage are one technique pointed two ways: vacuity mutates the
      *specification* and re-runs, coverage mutates the *system*. That maps
      cleanly onto this section — the grounding replay in item `120` perturbs
      the guard's inputs, while this item perturbs nothing and asks only
      whether the rule engaged. Both are needed and neither substitutes.
      **The class is wider than a scanner's output — it reaches the label,
      and there the victim is the auditor.** Added 2026-08-16 from a child
      session's neighbouring instance: a continuous-integration job named for
      one invariant while four of its five steps check entirely different
      ones. The job works perfectly; the **name** misdescribes its cover, and
      a session auditing coverage nearly reported a working guard as ungated.
      Nothing is wrong with the check and nothing would ever fire.
      **This estate has already fixed one instance of that and never
      generalised it.** The floor board used to render a warn-only scanner
      with the same tick a blocking one earns — *identical output for
      materially different cover* — and the fix was the three-state render
      now on the board. That was treated as a rendering bug. It was an
      instance of this class, and the class has now appeared on a second
      surface, in a second repo, on a plane with no scanner in it at all.
      **So the requirement generalises**: a guard, a job, or a board must not
      name a property it does not cover. Coverage reporting answers it for a
      scanner's output; the label plane needs the same question asked of it,
      and no existing check looks there.
      **Small, and it composes with the item above.** A guard that reports its
      own coverage makes the grounding replay checkable at a glance: a replay
      that fires on zero of its incidents is the same signal as a scan that
      opened zero files. Both currently render as success.
      **A worked caution from the measurement.** The same scanner run two
      defensible ways differed threefold — through the floor wrapper, and
      invoked directly, where it walked a nested worktree and counted the tree
      twice. Coverage reporting would have made that visible in the output
      rather than in a footnote.
