- [~] **The board miscounted the review queue — make its markers unambiguous to
      the sessions that read them (Mike, 2026-10-03).** (claimed 2026-10-05-1128, wt: atelier-qr-130-020) Mike's instruction,
      verbatim, after a session summarised the failure for him:

      > good, now record that on the board as something to improve i.e. more
      > work for you to do later

      The summary he was answering: *"the other session miscounted the review
      queue because the board's markers were ambiguous. That's a correctness
      problem for Claude sessions to fix among themselves, and I should never
      have turned it into a question for you."* Earlier the same day: *"only you
      read these files, I will never read the board because it exists solely
      for you to track the work you need to do … it is written by claude for
      claude to read later."*

      **What happened.** On 2026-10-03 a session reported "20 queued reviews"
      to Mike from the index, when all twenty had run on 2026-09-25/26: each
      close had recorded the outcome in a sub-bullet and left the item's
      top-line `⏳`, which the index projects. A second session found the truth
      only by opening every item file. The closing session then swapped the
      markers on 27 proven-reviewed items to `- [ ] 🎯` or `- [ ] 🛑` (commit
      `1d96efa`) — markers the legend does not define — and asked Mike to choose
      between them. Both moves were wrong: the first left a marker that misstates
      state, the second invented one and put a Claude-side question to him.

      **The work.** Decide, among Claude sessions, one unambiguous way a review
      pointer's state reads once its verdict lands, using only what the board
      legend defines (the work-owed tri-state, ruled 2026-07-23, plus the `⏳`
      pointer marker); write it into the legend; make `board.py` and
      `pointerscan` enforce it so a session counting the index cannot be misled;
      then bring the 27 items marked in `1d96efa` (and any later close) into
      that form. Two items already record the defect and should be closed by
      the same work: `130/010` and `320/460`. If the legend genuinely needs a
      new state, that is a doctrine change and goes to Mike as a plain-language
      recommendation with its use case — never as a choice between markers.

      **Also owed, from the same incident:** every session that closes a review
      must update the pointer's own state line in the closing commit, and a
      session reporting a queue count must count from item state, not glyphs.
