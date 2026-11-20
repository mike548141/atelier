- [ ] 🎯 **The index lists every finished item, so finished work is read at
      every session start.** Filed 2026-11-20 by session 19378351. The
      generated `ROADMAP.md` carries one line per item whatever its state,
      and nothing in `tools/board.py` collapses a finished section. Measured
      here the same day: 814 lines, 46 sections, 17 of them with no open
      item; a dropped-done index would be about 400 lines, and the five
      largest boards in the estate fall by a quarter to five-sixths each.
      **Agreed** (Mike, 2026-11-20, to "Should finished themes drop out of
      what sessions read?"): *"yes I agree"*. That approves the collapse of
      an all-done section to one line; item files stay untouched.
      **🎯 Shape still being discussed** (his words, same message):
      *"I am considering if ROADMAP.md should be a synopsis and state of only
      the themes of work (the folders basically). And then in each folder the
      README.md or some other dedciated file that runs the board for that
      theme of work, in the same way ROADMAP.md runs the baord for each theme.
      The detail still sits in individual work item files"*. The weighing put
      to him: about ten tools across the estate read the index's state lines
      (`pointerscan`, `harvestscan`, `coldsweep`, `cclive`, `ccclose`, a
      review-queue reader and others), and sections are uneven (one board
      holds 290 open items in six sections), so a sections-only index does
      not bound what a session reads there. Build waits for his pick.
