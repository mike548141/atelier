- [x] **DONE 2026-11-03** (wt: atelier-qr-4c65-ccclose) 🔎 **`ccclose --identifiers` misses a session's commits whose author
      date predates its window.** Seen 2026-10-18 by the session that landed
      the opening prompt's template history (`180/060`). That history is 50
      commits whose author dates are set to each version's first use, in
      July to October, and committed inside the window. After `210/290`'s
      evidence-based attribution landed, the block credited that session with
      52 commits. Its own count on `main` is 102, and the gap is the
      backdated history. Shape to weigh: judge membership by committer date,
      or accept either date when the commit carries other evidence. Filed,
      not started; the attribution code is a peer session's fresh work.
      ✅ **Closed 2026-11-03, no behaviour change needed.** The premise did
      not hold: `windowCommits` has judged a commit by `%ct`, the committer
      date, since the tool was built (`4eda680`), and `git log --since` filters on the committer
      date too, so a commit with a backdated author date and a committer date
      in the window is already in the window. A fixture now proves it (author
      date 90 days back, committer date inside; credited when a command of
      the session names it). The 50 history commits were most likely made by
      a script, so no `git commit` command names them: they print on the
      "unconfirmed" line, dated by committer date, which the same test pins.
      That is `210/290`'s evidence tier working as designed, not a window
      miss. The code comment, man page and design note now say committer date.
