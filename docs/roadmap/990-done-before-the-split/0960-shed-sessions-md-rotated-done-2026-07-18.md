- [x] **shed: SESSIONS.md rotated — DONE 2026-07-18**, 318→204 (older entries
      verbatim → new `SESSIONS-ARCHIVE.md`; all 14 verified present once).
      Also fixed en route: shed's `hooks.atelierTools` was *relative*
      (`../atelier/tools`), resolving only from the main checkout, so the
      fail-closed pre-commit scanner blocked every worktree commit — set
      absolute. **Worth checking on other children.**
