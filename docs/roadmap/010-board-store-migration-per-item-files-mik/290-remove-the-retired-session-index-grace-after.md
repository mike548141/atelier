- [ ] **Remove the retired-session-index grace once 2026-12-04 has passed.**
      Filed 2026-11-20 with `010/270`, which retired the one-file session
      index: the session log is `docs/sessions/`, one file per session, and
      the folder is the index. Children run atelier's tools from `main`, and
      most still keep a `docs/SESSIONS.md` until the health sweep retires it,
      so three things still accept the retired form. The 14-day span is the
      building run's pick, aligned with `010/250`'s date, not a ruling.
      1. `instruments/ccclose`, `RETIRED_INDEX_ACCEPTED_UNTIL = '2026-12-04'`
         (the first day it is refused): until then a commit to a kept index
         counts toward *Session record written*; from that day only a session
         file does. The code switches by itself; what is owed is removing the
         grace branch, the `todayUtc`/`CCCLOSE_TODAY` hook, the grace test and
         the man page and design-doc sentences that describe it.
      2. `tools/pathscan.py` `RECORDS_GLOBS`, `tools/coldsweep.py` `BARRED`
         and `tools/sizescan.py` `HOT_PATH_FILES` still name
         `docs/SESSIONS.md` (or `SESSIONS.md`), so a kept index stays a
         record, stays barred to a cold reviewer, and has a header hatch
         named. Remove each once no repo keeps one, not on the date: barring
         a file nobody has costs nothing, and lifting the bar early would let
         a cold reviewer read an unswept repo's log.
      **Owed, in order:** before the date, run `archivecut.py --plan`
      (read-only) in every child checkout and list which still keep
      `docs/SESSIONS.md` and whether each would pass its proof; that list
      goes to the principal before the cut-off, so a child whose closes start
      failing on the date is expected. Then remove (1), and (2) once the list
      is empty.
