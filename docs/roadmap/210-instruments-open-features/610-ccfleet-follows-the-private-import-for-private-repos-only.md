- [x] 🔧 **`ccfleet` hands a public repo's session only the shared part of the user-level
      instruction file: it follows the file's `@` import of the private part for private
      repos only.** Follows `RK10` (`210/600`), whose guard refuses a public repo's launch
      when the appended instruction file names a private name. The principal's answers,
      2026-11-25 UTC (session 0ee74059, AskUserQuestion; answers, not rulings): to keeping
      the refusal, *"Keep refusing as per your recommend option but what do we do to fix
      this?"*; to a separate public-safe file, *"Build it now as recommended but would it be
      better to have two instructions files? one with just hte private info in it and the
      other with everything else so that there cant be drift rather than needing a drift
      checker?"*. So: one shared file that imports one private file; no copy, so no drift.
      `ccfleet` inlines the imported files for a private repo and leaves the import line
      unfollowed for a public or unknown one, where the guard still reads what is appended.
      🔒 CLAIMED 2026-11-25T05:18Z (claimed 2026-11-25-0518, wt: atelier-c3-import) by
      session 0ee74059 (`atelier-c3`, Opus 5.5).
      ✅ **Landed 2026-11-25** (`f4360a79`, one Opus worker). `instructions_text` builds what
      each session is handed and the guard reads the same text: a private repo gets each
      import inlined (the harness's rules: relative to the importing file, `~` is home, four
      hops, none inside code); a public or unknown one gets the import line as text. `resume`
      now looks up visibility as a run does. Seven tests, each failing on the old code;
      `test_ccfleet` 136 OK. The operator's user-level file was split the same session, with
      a backup kept; checked on it: the public text names no private name and does not
      reach the imported part; the private text inlines it; a fresh session loads both.
