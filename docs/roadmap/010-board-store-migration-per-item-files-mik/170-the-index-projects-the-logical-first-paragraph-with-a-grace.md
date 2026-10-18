- [~] **Project an item's logical first paragraph into the index, with a
      (claimed 2026-10-18-0710, wt: atelier-qr-010-170)
      grace period for children** — part 1 of `320/450`, split out to build.
      `board.py` reads only an item's first physical line, so a title or
      `(claimed …)` fragment wrapped onto line two never reaches the index.
      A queue run's own claims hit it on 2026-10-18. The fix joins the
      indented continuation lines of the first paragraph before `TITLE_RE`
      and `CLAIM_RE` run. But `board` blocks in every child's CI from
      `floor.yml@main` and has no advisory form, so a changed projection
      would make each child's committed `ROADMAP.md` read stale at its next
      run. The queue run recommended: *"build it with a one-release grace
      period, where the check accepts both the old and the new index, and
      tell the children"*. Mike, 2026-10-18, answering that recommendation:
      *"I agree"*. Owed: the new projection; `--check` accepting the old
      one until a stated end, saying so when it does; a test for each; and
      the notice children read at their pin bump.
