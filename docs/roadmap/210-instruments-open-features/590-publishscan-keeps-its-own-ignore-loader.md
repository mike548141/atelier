- [x] 🔧 **`publishscan` keeps its own ignore-file loader, outside the
      shared `tools/allowmarker.py`.** The GA1 finding (`160/060`) was
      single-sourced on 2026-10-03 (`643cf809`), but `publishscan.py`'s
      `load_ignores` and `_ignored` were left as their own copy. They are
      stricter on purpose: the reason must sit on the glob's own line, and a
      `#` glued to the glob is refused (PA3, ruled 2026-08-03), with control
      characters stripped at ingest (C1F3/PA4). His pick on GA1, 2026-11-24:
      *"Make it one module (Recommended)"*. **Do:** fold the loader into
      `allowmarker` with its strictness as parameters (the module's own rule:
      every difference is a parameter, never a default), keeping every
      current refusal and message byte-identical under the existing tests;
      or, if a parameter cannot carry it, record in `allowmarker`'s
      docstring why this copy stays. *Tier:* build tier. *After:* add it to
      the next scanner cold pass queued under `160/`.
      ✅ **Done 2026-11-25 (session f8dd3843, `atelier-31`, queue run; a Sonnet worker
      built it).** `allowmarker.load_ignore_globs` takes `same_line_reason`,
      `refuse_glued_hash`, `strip_controls` and `file_only`, and `allowmarker.ignored`
      takes `case_sensitive` and `directories`, every one defaulting to the reading the
      other scanners already had. `publishscan`'s loader and matcher are now thin calls
      with its strict values; `BadIgnoreFile` is an alias of
      `allowmarker.StrictIgnoreFileError`, whose messages are the old ones byte for byte.
      Nothing of the strictness stayed behind. The existing `test_publishscan` assertions
      are untouched and pass; about 14 new tests in `test_allowmarker.py` pin each
      parameter. Its cold pass is queued as `160/1850`.
