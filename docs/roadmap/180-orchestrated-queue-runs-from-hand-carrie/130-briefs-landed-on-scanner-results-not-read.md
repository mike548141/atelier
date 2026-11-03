- [x] **DONE 2026-11-03** (wt: atelier-qr-4c65-dispatch) 🔎 **Three of five review briefs were landed on scanner results, not
      read.** Session `8e498ef1` (2026-10-18, `180/110`) said so itself: it
      read the privacy brief and one authorship section, and landed the other
      three "on the writers' clean scanner reports, without reading them in
      full". `CONCURRENCY.md` has the orchestrator read the work it endorses
      before the merge lands. A brief is what the cold reviewer is held to,
      so an unread brief can steer a pass with no one having checked it.
      The disclosure was honest. The rule was still broken, and nothing in
      the text says whether a brief counts as "work it endorses". **Shapes:**
      say that it does, with a read of every brief before it lands; or name a
      lighter, stated check for brief-only landings.
      ✅ **Landed 2026-11-03** (the first shape).
      `CONCURRENCY.md` § *Orchestrated queue runs*, the orchestrator/worker
      paragraph: a review brief is work the orchestrator endorses and is
      read in full before it lands; a writer's clean scanner report is not
      that read.
      Review owed: `160/995`.
