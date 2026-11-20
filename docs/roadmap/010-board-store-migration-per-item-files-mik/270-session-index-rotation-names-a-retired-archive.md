- [x] **The session-index rotation rule names a store the archive cut
      retires.** Filed 2026-11-20 by session 19378351. RECORD.md § *The
      session log* lets the index rotate: older index lines move verbatim to a
      `SESSIONS-ARCHIVE.md` growth store. On 2026-11-20 the principal picked
      *"Split, fall back to move (Recommended)"* for the existing frozen
      archives, `SESSIONS-ARCHIVE.md` included, so they are cut into
      `docs/sessions/` and leave `docs/`. A later rotation would recreate the
      file. **Owed, his to answer:** where a rotated index tail goes now
      (one choice: a dated index file inside `docs/sessions/`, so nothing
      returns to `docs/`). No repo has rotated since the split, so nothing is
      blocked meanwhile.
      **His reply, 2026-11-20 UTC** (typed in answer to the three offered
      routes, so an answer, not a ruling): *"This does not sound like
      doctrine, they should not be in one big sessions file in the first
      place"*. So no route that keeps a growing session file stands: neither
      an archive file nor, read plainly, the hand-appended index itself. The
      reading and its shape are being put back to him before any build.
      **Answered 2026-11-20 UTC** (his pick from offered options, an answer):
      *"Retire SESSIONS.md"*: no index file at all; the date-named
      `docs/sessions/` folder is the index, and a session starts by reading
      the newest few files. The rotation rule goes with it. **Owed:** each
      index line moves word for word into its session file (proved by
      script), `SESSIONS.md` is removed, and every rule, tool, template and
      skill that reads or appends to it changes; atelier first, then the
      health sweep carries it to the children.
      **DONE in atelier, 2026-11-20 UTC** (a worker of session 19378351,
      Opus 5.5). A dating note first: the two lines above first said
      "2026-11-21", the New Zealand date; the answer came at about 20:25 UTC
      on 2026-11-20 (`5d82e25a`), and they are corrected to it. `b68cf410`:
      `tools/archivecut.py` retires the index, and any frozen session
      archive, into `docs/sessions/`, files only. Each entry goes word for
      word into the session file it links, right after that file's `# `
      heading (so the title stays first and the line reads as the file's
      summary), under "From the retired session log" and a comment carrying
      its line numbers; an entry linking no session file gets a new file
      named for its date, with a day counter where it states no time. The
      rest goes fenced into `docs/sessions/README.md`. The proof (multiset,
      every link mapping back, a byte-for-byte rebuild from the outputs as
      written) must pass or nothing is written, and the archive route no
      longer writes index lines. RECORD.md, CONCURRENCY.md's recovery
      sweep, CLAUDE.md, REPO-STANDARD, the template, `create-repo`,
      `fleet-sweep` and `ccclose` moved to the folder; `ccclose` accepts a
      kept index until 2026-12-04 (`010/290` removes the grace).
      `e5f9f245`: atelier's own run, 340 entries (295 placed, 45 new
      files), proof and `--verify` passing. A read-only dry run on fourteen
      children found every session log would pass its proof. Cold pass
      queued: `160/1700`. Each child's own run rides on the health sweep
      (`010/230`, healthy item 6 now names it).
