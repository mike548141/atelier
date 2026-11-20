- [ ] 🎯 **The session-index rotation rule names a store the archive cut
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
      **His reply, 2026-11-21 UTC** (typed in answer to the three offered
      routes, so an answer, not a ruling): *"This does not sound like
      doctrine, they should not be in one big sessions file in the first
      place"*. So no route that keeps a growing session file stands: neither
      an archive file nor, read plainly, the hand-appended index itself. The
      reading and its shape are being put back to him before any build.
