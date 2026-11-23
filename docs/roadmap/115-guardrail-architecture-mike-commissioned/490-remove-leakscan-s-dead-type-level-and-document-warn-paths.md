- [x] **Remove `leakscan`'s now-dead type-level and document warn-only
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
      ✅ **Done 2026-11-23** (queue run c7a1e36e; a Sonnet worker, read by
      the run before landing). Removed from `tools/leakscan.py`:
      `in_type_level_grace`, `in_document_grace`, `render_type_level`,
      `render_documents`, `_grace_remedy`, `DOCUMENT_UNTIL`,
      `DOCUMENT_FORMATS`, `TYPE_LEVEL_RULE`, the two warning tallies and
      their summary counts, and the `binary_type_level` and
      `binary_documents` blocks in `--json` (a read-only grep of the estate
      found no reader outside this repo). `TYPE_LEVEL_UNTIL` stays: the
      post-date refusal names it. The `--binary-entries` note that still
      said "accepted with a warning until" now says the line has not kept
      the set since then. Tests: the pre-date tests removed, the post-date
      blocking tests kept, a JSON test pins both blocks absent; 464
      `test_leakscan` and 110 `test_report` pass. Findings over this tree
      are identical before and after, text and JSON. Behaviour-preserving
      removal, so no pass is queued, as `010/190` did.
