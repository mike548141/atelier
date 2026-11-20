- [ ] 🎯 **Every repo keeps the house board, and the health sweep enforces
      it.** Filed 2026-11-20 by session 19378351. Mike's words, 2026-11-20:
      *"I want all repos to use the doctrine way of managing work on its
      board. If the repo is archived or a fork of someone elses repo then it
      is an exception and its left as is"* · *"the estate health check skill
      needs to find things like this and fix them when a repo does not meet
      doctribe rule like this"*.
      **Gap in the skill, measured:** `skills/fleet-sweep/SKILL.md` healthy
      item 6 already requires the per-item board, and its survey exempts
      archived repos only; it names no fork exemption, and it treats a repo
      with no pin as a question rather than work. Its check also reads
      the form of a board that exists, so a repo with **no board at all**
      passes unseen: two adopted children have none today, and one
      unarchived, unforked repo was never adopted.
      **Owed:** the skill's survey gains the fork exemption and a no-board
      check; a repo without a board gets the empty store (`docs/roadmap/`
      with its `README.md`, the generated index); the archive work of
      `010/220` and the index shape of `010/210` join the sweep once
      settled. Worker runs wait until he closes the board discussion (his
      words: *"first lets finish discussing how we manage the board and then
      also look at all other similar use cases like the SESSIONS file"*).
