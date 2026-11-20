- [x] 🎯 **Doctrine candidate — bulk deletion from a record store is a
      show-first action, regardless of who created the mess.**
      (claimed 2026-08-05-1243, wt: queue-batch-0806) Grounded in a
      worked example: a session created 185 lines of duplicate roadmap
      sections, then removed them having compared **heading names only**, and
      asserted "duplicates" in the commit message without diffing a single
      body. Mike challenged it. The diff took thirty seconds and showed three
      sections byte-identical, one correctly superseded — and **one a genuine
      loss**, a completed item whose only roadmap trace went with it. Two
      things made it feel safe and neither holds: *"it's my own mess"* (the
      sections encoded **Mike's** rulings, not the agent's drafts) and *"git
      remembers"* (git remembers the text, not that the work was supposed to
      happen).
      **RULED 2026-08-04 (Mike): ADOPT.** The rule becomes doctrine — before
      removing a block from a record store, diff it and show what goes, or
      ask; `harvestscan`'s bulk-deletion warn is the mechanical net beneath
      it and this rule covers what the net cannot see. DELIVERED 2026-08-05:
      `RECORD.md` carries the rule and its grounding; `AUTONOMY.md`
      § *Before you destroy or overwrite* carries the cross-link and names
      the grant boundary. (Moved from ROADMAP.md 2026-08-05.)
