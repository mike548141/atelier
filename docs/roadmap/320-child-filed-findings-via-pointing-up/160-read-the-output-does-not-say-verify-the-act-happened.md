- [ ] **REPORT — the read-the-output rule covers an unread check and not an act
      that silently did not happen; two sessions in one repository hit the
      second in the same hour** `[S][method]` — filed from a private child,
      2026-09-06, via § *Pointing up*. Evidence: two independent incidents,
      recorded below.

      ## 🛑 The sentence worth putting at the top

      **Absence of an error is not evidence that the act happened.**

      ## The gap

      The child's principal widened its local guard rule the same day, to: *run
      the check as its own command, read the output, then act — any act, not
      only a destructive one.* Three costumes were recorded with it, and **all
      three are about the check being unread**:

      | Costume | What goes wrong |
      |---|---|
      | `&&`-chained | the check printed and the act ran before anyone read it |
      | a masking pipe | `cmd \| tail` reports the pipe's exit code, so red reads green |
      | a persisting `cd` | the act lands somewhere nobody checked |

      **The fourth is the mirror image and no rule covers it: the check WAS
      read, and the act silently did not happen.** A command that produces no
      output on failure, or whose failure a session filters out, leaves the
      operator believing a state change occurred when nothing did.

      ## The evidence — two sessions, one hour, same shape

      **Session A.** Ran a full gate over its working tree: green. The commit
      that would have put that tree on the integration branch **failed on an
      `index.lock` collision** with a peer. Its own check for a blocking marker
      matched nothing, and it read that absence as success. **The branch stayed
      red for several minutes and a peer's commit landed on top of the red
      base** — so a correct gate, correctly run and correctly read, certified a
      tree that never became the branch.

      **Session B**, the peer, twice in the same hour. One commit failed on
      A's lock. A second failed because **`git commit <pathspec>` refuses a
      path that is not yet tracked** — an untracked file needs `git add` first —
      and again the grep for a failure marker matched nothing and the absence
      read as success. Two blocked commits, no error noticed, while A was
      blocked behind B.

      🚩 **Neither session was careless and neither broke the rule as written.**
      Both ran the check as its own command. Both read its output. The rule has
      nothing to say about the step after.

      ## 🛑 The close-out case, and it is the expensive one

      Added after filing, because a **third** session hit it in the same
      evening and in the worst possible place.

      A session running its close-out checks asked *is anything of mine
      uncommitted?* and answered **no** — from what it believed it had
      committed, not from `git status` at that moment. A completed piece of
      work, with its full record written, was sitting uncommitted in the shared
      checkout. It was caught only because a **peer** read the tree and said
      so.

      **This is the same failure and the most costly version of it**, for three
      reasons:

      1. **Nobody is left to notice.** Every other instance is caught by the
         next command; a close-out failure is caught by nobody, because the
         session ends.
      2. **It strands the shared record.** The generated board index and the
         item store disagree from that moment on, so the floor reds on whoever
         commits next — a peer pays for it.
      3. **It is silent in both directions.** The session reports a clean
         close-out and means it. The report is what a principal reads.

      🚩 **The third session's own count for one evening: an empty-message
      commit that passed the entire gate and then aborted; two commits that
      failed on an `index.lock`; and this.** Four instances, three sessions, one
      repository, one evening. Every one is *absence of an error read as
      evidence the act happened.*

      🎯 **So the clause has a second half.** A close-out claim of *nothing
      outstanding* must be **measured at that moment** — `git status`,
      `git worktree list`, `git branch --no-merged`, and a claim grep — never
      recalled from what the session believes it did. The child already has a
      local rule that a lane's completion report is not evidence and only the
      integration branch is; **that rule does not currently point at the
      session's report about itself.**

      ## Why it matters more on a shared checkout

      A green gate is a statement about **a tree**. A tree only becomes the
      integration branch if the commit actually lands. With one session those
      are nearly the same thing; with two in one checkout they come apart
      routinely, because `index.lock` contention is the normal case rather than
      the exception — the two sessions above collided on it repeatedly in one
      evening.

      ⚠️ **And the harness makes it easier to miss, not harder.** A backgrounded
      command reports the exit code of the *wrapper* — a session that writes
      `make check > file; echo "EXIT=$?"` gets the `echo`'s status, so a failed
      gate is notified as success. One of the two sessions did exactly that and
      found the failure only by reading the output file.

      ## The shape of a fix (sketch, not a design)

      One clause, wherever the read-the-output rule is stated: **verify the act
      completed, by its own effect and not by the absence of an error.** For a
      commit that is `git log --oneline -1`; for a push, the remote ref; for a
      write, the file. It is one command and there is no argument against the
      cost.

      🔎 Worth stating beside it that **filtering a command's output for known
      failure markers is not reading it** — a grep that matches nothing is
      indistinguishable from a command that produced nothing at all, which is
      precisely the case here.

      Consideration and remediation are atelier's; the reporting child stops at
      this report. The finding is the peer session's; it is filed by the other
      because that session was closing and had the branch conventions loaded.
