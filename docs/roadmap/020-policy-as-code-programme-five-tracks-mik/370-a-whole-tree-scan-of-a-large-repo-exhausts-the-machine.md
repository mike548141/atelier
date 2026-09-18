- [ ] 🔥 **A whole-tree `secretscan` / `leakscan` run over a large repo grows
      to ~9 GB and thrashed the principal's machine** — found 2026-09-18 by the
      queue run that caused it, reported by a peer session in another repo.
      **What happened.** An estate probe (old vs new scanner, every sibling
      repo) ran the scanners over each repo's working tree. One sibling holds
      several GB, mostly untracked data plus a very large tracked CSV. A single
      `secretscan` process over it reached ~9 GB resident after ~56 minutes. A
      second, unrelated session's run over the same repo sat at the same size.
      Together with the probe's `leakscan` they pushed a 16 GB machine ~21 GB
      into swap at load 54. A peer session traced the processes and asked for
      them to be stopped; they were killed, and the rerun scanned only
      HEAD-tracked content (`git archive HEAD`, which is what CI sees). That
      was still slow on the same repo.
      🔎 **Class, not instance:** the scanners keep per-file state in memory
      in proportion to the tree, with no size cap per file and no streaming.
      So their cost grows with the largest repo anyone points them at. The
      estate has one repo that size today, and any repo that vendors data
      becomes the next.
      **Owed:** measure where the memory goes (whole-file reads of huge
      files, findings lists, the advisory tier keeping ~43,000 findings);
      then decide between a per-file size cap that reports what it skipped
      (never silently), streaming line reads, and capping the advisory list.
      Adjacent: `020/160` (scanners walk gitignored nested worktrees).
      **Standing practice until then:** an estate-wide probe scans tracked
      content only, one process at a time, and leaves the largest repo out or
      runs it alone.
