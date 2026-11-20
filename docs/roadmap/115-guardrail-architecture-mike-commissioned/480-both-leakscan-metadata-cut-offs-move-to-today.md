- [x] **Both leakscan metadata cut-offs move to blocking from 2026-11-20, on
      the principal's answer.** Two dates were the authoring runs' choices,
      never his: `TYPE_LEVEL_UNTIL` (2026-12-18, whole-set image-metadata
      lines, `020/450`, the `160/990` pass's GF1) and `DOCUMENT_UNTIL`
      (2027-01-18, the document reader, `115/390`). Put to him through the
      device at queue run 08cd3b95's close, 2026-11-20 UTC, with the measured
      reach (no child carried a whole-set line; 48 document findings in three
      siblings would block). Options offered: confirm both, warn only until he
      rules, or confirm one. His answer, verbatim, typed in place of the
      options: *"Move both to blocking from today"*. An answer to an ask, not
      a ruling in his own words.
      **Owed:** both constants set to 2026-11-20 and labelled as his; the
      README, source comments and CHANGELOG say whose date it is; the tests
      that pinned the old dates follow. Then the warn-only paths are dead code,
      removed later as `010/190` removed the last graces.
      🔒 CLAIMED 2026-11-20T08:45Z (claimed 2026-11-20-0845, wt: inline, no
      worktree) by queue-run session 08cd3b95 (Opus 5.5, principal-opened).
      ✅ **Done 2026-11-20 UTC, same session.** Both constants are 2026-11-20,
      labelled with his words in `tools/leakscan.py`, `tools/README.md` and
      `CHANGELOG.md`; the two tests that pinned the old dates now pin his
      (`test_leakscan`: 471 OK). Measured the same hour with the new dates:
      the three siblings that track Office or PDF files hold 22, 25 and 1
      metadata findings, 48 in all, now blocking there; atelier's own tree is
      clean. Each of the three gets an item on its own board. Still owed and
      unclaimed: remove the now-dead warn-only paths (`in_type_level_grace`,
      `in_document_grace` and their callers), as `010/190` removed the last
      graces.
