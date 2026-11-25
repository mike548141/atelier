- [~] 🔧 **`publishscan` keeps its own ignore-file loader, outside the
      🔒 CLAIMED 2026-11-25T13:25Z (claimed 2026-11-25-1325, wt: atelier-qr-f8dd-pa) by session f8dd3843
      (`atelier-31`, Opus 5.5, principal-opened by `/atelier:work run`): folding the loader into allowmarker.
      A worker subagent builds it in the worktree; this session lands it.
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
