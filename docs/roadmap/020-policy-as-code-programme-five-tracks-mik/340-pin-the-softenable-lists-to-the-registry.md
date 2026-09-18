- [x] **Pin the three softenable-set prose lists to `Scanner.advisory`
      (AP2, ruled 2026-08-23).** floor.py's docstring, ADR 0008 Decision 2
      (as amended 2026-08-23) and CONTRIBUTING's never-softened list each
      describe which scanners carry advisory forms; none is test-pinned to
      the registry, which is how the docstring and the ADR drifted wrong
      while CONTRIBUTING stayed right. One test: parse each prose list,
      assert it matches `advisory is None` over SCANNERS, so the next
      registry change reds the stale sentence instead of leaving it.
      review: not warranted — a queued test item recording an accepted
      ruling; the test earns review with its code.

      ✅ **FIXED 2026-09-18** (`64a47cb`, merged from `board-flags-0918`):
      `tools/test_floor.py::SoftenableListsPinnedToRegistry` parses the
      editable prose lists and asserts each equals the registry's
      `advisory is None` set. It caught live drift on first run —
      `docs/build/templates/CONTRIBUTING.md` was missing `board` — fixed in the
      same commit. ADR 0008's restatement is excluded with a comment: ADRs are
      frozen records, and a test must not be failable by text the repo has
      committed never to edit. 🔎 Noticed, not fixed: `tools/test_board.py`'s
      own docstring restates the set short of `board` and `licenscan`; it is
      not one of the named lists.
