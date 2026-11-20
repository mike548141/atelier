- [ ] **Remove `leakscan`'s now-dead type-level and document warn-only
      paths.** Since 2026-11-20 both cut-offs have passed (`115/480`, the
      principal's answer *"Move both to blocking from today"*), so
      `in_type_level_grace`, `in_document_grace`, their callers, the
      `binary_type_level` and `binary_documents` warning blocks in `--json`,
      the two summary-line counts and the tests of the pre-date behaviour are
      dead code a reader must still reason about. Remove them as `010/190`
      removed the last graces: keep the post-date behaviour exactly, grep every
      reader of the removed `--json` keys across the estate first (read-only),
      and run `test_leakscan` plus the shared-contract modules. Filed
      2026-11-20 UTC by queue run 08cd3b95.
