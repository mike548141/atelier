- [x] **A1 — a `scope` path resolving to nothing silently disabled the check.**
  Now a hard config error for any scanner with no advisory form; the skip
  survives for the softenable docs-scoped checks, which is the case it was
  written for. **Extended past the finding as written:** the review described a
  scope resolving to *nothing*, but the class is *any* declared path that does
  not resolve — one of two paths going missing halves a boundary check's cover
  the same way, so partial drift blocks too. `floorfleet` now reads `scope`,
  `flags` and a non-default `docs` on the board and in `--json`.
