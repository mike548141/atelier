- [ ] **REPORT — `CONCURRENCY.md`'s session-start bookend tells every session to
      run `--autostash` on a checkout the same document says a peer may have
      uncommitted work in, and the stash stack it writes to is shared**
      `[S][method]` — filed from a private child, 2026-09-06, via § *Pointing
      up*. Evidence: a live near-miss, recorded below.

      ## The contradiction, inside one file

      **`CONCURRENCY.md` § *Integration hygiene*** instructs, unconditionally:

      > *"**Sync bookends** shrink the collision window the substrate can't
      > cover … `git pull --rebase --autostash` at session start"*

      **The same document, sixty lines earlier**, establishes the premise that
      makes that dangerous:

      > *"a path staged before you opened, or left behind when a peer landed by
      > `update-ref`, is still sitting there to be committed under your
      > message"* … *"a clean status seconds ago is not a clean status now.
      > With several sessions live the window is minutes"*

      `--autostash` stashes **whatever is dirty in the working tree**, not
      whatever is yours. On a shared checkout with a live peer that is the
      peer's uncommitted work — and **the stash stack is shared across the
      primary checkout and every worktree**, so the entry lands somewhere a
      second session may pop. The doctrine's own stashing guidance elsewhere
      forbids bare `stash`/`stash pop` for exactly that reason; the bookend
      reaches the same stack by a different door and carries no such warning.

      🔎 **The file already knows the hazard and confines it to the wrong
      case.** § *Repository state is shared, and unprotected* says to *"back any
      autostash out to a file before aborting"* — but only about a rebase found
      already in progress. The session-start bookend, which is where a session
      will actually meet it, says nothing.

      ## The incident (2026-09-06, private child)

      A session ran the bookend verbatim at the point it claimed a board item.
      A peer session was live in the same checkout with **five uncommitted
      board-item files staged**. The pull failed for an unrelated reason before
      the autostash executed, and `git stash list` was empty afterwards — so
      nothing was lost. **It was luck, not care**, and the same command on a
      repository where the pull succeeds would have moved a peer's work to a
      shared stack mid-edit.

      ## 🚩 And a second condition the rule does not test for

      That child repository **has no git remote at all** — deliberately, and its
      own onramp says so twice. So the bookend is a guaranteed no-op that still
      carries the autostash hazard: all cost, no benefit, on every session start
      forever. The rule reads as unconditional, so a session following it
      literally does the wrong thing in a repository the house otherwise
      supports.

      ## The shape of a fix (sketch, not a design)

      Three things the bookend could say and does not:

      1. **Gate it on a remote existing.** No upstream, no bookend.
      2. **Gate it on the working tree being yours.** Read `git status` first —
         if anything dirty is not yours, the bookend is a stop, not a step. That
         is the same *read-then-act* discipline the document already requires
         of the destructive cases.
      3. **Name the stash stack as shared where the bookend is stated**, not
         only where a mid-rebase abort is discussed, and point at the
         tagged-push / apply-by-SHA discipline the house already documents.

      ⚠️ **Not proposed: dropping the bookend.** The collision window it exists
      to shrink is real. What is wrong is that its safest-looking flag is the
      one that reaches another session's work.

      Consideration and remediation are atelier's; the reporting child stops at
      this report.
