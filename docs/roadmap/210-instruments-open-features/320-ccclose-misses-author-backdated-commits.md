- [ ] 🔎 **`ccclose --identifiers` misses a session's commits whose author
      date predates its window.** Seen 2026-10-18 by the session that landed
      the opening prompt's template history (`180/060`). That history is 50
      commits whose author dates are set to each version's first use, in
      July to October, and committed inside the window. After `210/290`'s
      evidence-based attribution landed, the block credited that session with
      52 commits. Its own count on `main` is 102, and the gap is the
      backdated history. Shape to weigh: judge membership by committer date,
      or accept either date when the commit carries other evidence. Filed,
      not started; the attribution code is a peer session's fresh work.
