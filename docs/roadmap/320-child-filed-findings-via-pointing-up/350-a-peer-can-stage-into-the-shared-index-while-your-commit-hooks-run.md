- [ ] 🔎 **Hand-up: a peer can stage into the shared index DURING your commit,
      so "read `git diff --cached` before every commit" cannot close the hole
      it is written to close — and the orchestrator seat is the one most
      exposed.** Filed from a private child 2026-09-20 via § *Pointing up*, by
      direct write into the parent's tree, PR opened before stopping. The child
      is not named; per § *The route* rule 2 that omission is deliberate, and
      the branch name carries no repo token either (`320/190` still unruled).

      **What the house says today.** `CONCURRENCY.md` § *The index is a shared
      surface too*: *"The check that sees it is `git diff --cached` immediately
      before every commit"*, plus staging by explicit path. Both are read-then-
      commit.

      **Why that is not sufficient — a measured sequence, not a hypothesis.**
      The check and the commit are not atomic, and the gap between them is not
      small: a floor-hook commit takes **over two minutes** in the child that
      filed this. In that window a parallel session staged four of its own
      files into the SAME index and the commit swept all five under a message
      describing one. The index belongs to the *checkout*, not the session, so
      explicit-path **staging** buys nothing once a peer can stage beside you.
      What actually works, and was used to recover: **`git commit -- <path>`**
      (pathspec commit, which takes only those paths and leaves a peer's
      staged files staged), and the real answer, **a worktree — the only thing
      that gives a session an index of its own.**

      **The second instance, two days later, is why this is filed rather than
      just fixed locally.** A session resuming work in the same child ran
      `git status` at open (the bookend rule) and found a **peer's session log
      staged in the shared index** by a run that was live at that moment. One
      ordinary `git commit` would have published it under the resuming
      session's message. Nothing but the status read stood between the two.

      **The seat that is most exposed is the one doctrine does not name.**
      § *Orchestrated queue runs* says a worker takes a worktree for a
      substantial slice and the orchestrator merges; it never says the
      **orchestrator** takes one. So the orchestrator is the session most
      likely to be making many small commits (claims, board edits, records)
      directly in the shared checkout, for the whole length of a run, beside
      live peers. Both recorded instances have the orchestrator on one side.

      **The proposed rule, for the house to weigh:** an orchestrator (or any
      session) doing multi-commit work in a repo where another session may be
      live **takes a worktree — full stop** — and where it must touch the
      shared checkout, **commits by pathspec**, not by staging then committing.
      The existing `git diff --cached` read stays: it catches the stale entry
      and the peer who staged *before* you looked. It simply cannot catch the
      peer who stages *after*.

      **Where it would live:** `CONCURRENCY.md` § *The index is a shared
      surface too* (the pathspec half) and § *Orchestrated queue runs*
      (the orchestrator-takes-a-worktree half).

      *Unevidenced beyond one child:* whether other repos see this. Both
      instances come from one private child running parallel sessions; the
      mechanism, though, is plain git and a slow pre-commit hook, neither of
      which is child-specific.
      *review: owed on whatever doctrine text the ruling produces (rule 4: a
      session that neither authored nor was instructed by the author).*
