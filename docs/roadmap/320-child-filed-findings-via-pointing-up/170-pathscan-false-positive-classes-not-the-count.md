- [ ] **REPORT — four verified `pathscan` false-positive classes from a second
      child, and a correction to the child's own headline figure: "20 of 20
      false" is stale and must not be carried** `[M][tools]` — filed from a
      private child, 2026-09-06, via § *Pointing up*. The classes were read
      line by line in the child; each was then re-probed here against
      `tools/pathscan.py` at `35912e3`, and **two of the child's four asks did
      not survive that probe unchanged**.

      ## The count, corrected before anything else

      The child's own item still reads *"20 findings, all twenty false
      positives"*, measured 2026-08-26. **That is not a current fact.**
      Re-measured 2026-09-06 over the same repo: **32 findings**, and they are
      not all false.

      - **7 of the 32 are genuine stale paths.** A tracked directory was
        renamed on 2026-09-04; the files exist under the new name and seven
        records still cite the old one. `pathscan` is right about all seven.
      - **2 of the 32 exist only because the scan ran from a worktree** — the
        sibling-repo pair, which is item
        [`180`](180-sibling-path-convention-breaks-in-a-worktree.md).
      - **The remaining 23 were not re-classified one by one at this count.**
        The four classes below rest on the child's 2026-08-26 line-by-line read
        and on the probe here; the tally does not, and is not offered as one.

      🔑 **The classes are the report; the count is not.** Any argument that
      leans on a 0% true-positive rate — the shape
      [`320/010`](010-pathscan-reds-on-three-shapes-that-are-never-real.md)
      builds for a different child — cannot be built on this child's figures
      any more.

      ⚖️ **And the seven genuine findings carry their own question.** The rename
      updated every live reference and deliberately left the records citing the
      old name; the commit message states the reasoning, that a record edited
      to match the present stops being evidence. So those seven are
      mechanically real and were deliberately created. Whether a checker should
      print them forever is the open question at the end of this item, not a
      defect in the classification.

      ## The probe, and its control

      A throwaway repo, one file, and the **same nonexistent token** placed in
      three positions, plus two home-path spellings. Controls held throughout:
      a genuinely present path stayed clean, a genuinely absent bare path
      stayed flagged. The five spellings probed — shown inside a fence, since
      quoting them in prose would itself add findings to this repo:

      ```text
      A  fenced       ./nosuch/same.sh run      (inside a shell code fence)
      B  inline       ./nosuch/same.sh run      (inside a backtick code span)
      C  bare         ./nosuch/same.sh          (plain prose)
      D  tilde-user   ~claude/nosuch/same.sh    (inside a backtick code span)
      E  tilde-slash  ~/nosuch/same.sh          (inside a backtick code span)
      ```

      | Spelling | Verdict |
      | --- | --- |
      | A, inside a fenced shell block | **clean** |
      | B, inside an inline code span | flagged |
      | C, bare in prose | flagged |
      | D, tilde-then-username home path | flagged, and the tilde is stripped |
      | E, tilde-then-slash home path | **clean** |

      ## The four classes, and what the probe did to each ask

      Listed in the child's stated order of value, with the correction against
      each.

      - ❌ **"Do not scan inside fenced code blocks" is ALREADY IMPLEMENTED.**
        Spellings A and B are the same token and differ only in their
        wrapper: A is clean, B is flagged. The child's evidence line for this
        class is an **inline code span** carrying a shell invocation, not a
        fenced block — its item says "fenced" and the content at 2026-09-06
        says otherwise. **The live ask is the inline code span**: a backticked
        relative script invocation is a command run in the host's working
        directory, not a link. Filed as a correction rather than folded away,
        because the ask as the child wrote it would have been actioned against
        a behaviour that already exists.
      - ⚠️ **A leading tilde is half-handled.** Spelling E, the tilde-slash
        home path, is already clean; spelling D, tilde-then-username, is not,
        and the tilde is **stripped rather than the token skipped** — so the
        remainder is reported as a repo-relative path that does not exist. The
        ask narrows to: treat a tilde-then-username prefix the way
        tilde-slash is already treated, and skip rather than strip.
      - ✅ **A path whose own line marks it as external is still flagged.** Two
        shapes verified in the child and reproduced in the probe: a line ending
        `(private repo)`, and a line naming a sibling estate repo before the
        path. **The disambiguating context is on the flagged line and unread.**
      - ✅ **`../<sibling>` resolves or not depending on which checkout the scan
        runs from.** Reproduced in a clean probe with a valid control — see
        item [`180`](180-sibling-path-convention-breaks-in-a-worktree.md),
        filed separately because it is a property of the sibling-path
        convention rather than of this scanner, and
        `git rev-parse --git-common-dir` would fix it for every tool at once
        rather than one tool at a time.

      ## The open question the child asked, and did not answer

      **Should a path checker run over records at all?** The tool's own
      docstring says *records never come clean*, and it already excludes five
      record files by name. If that is true — and this child's evidence says it
      is, in both directions, since all seven of its genuine findings sit in
      board items and the index generated from them, prose about the estate
      rather than configuration, which the rename deliberately did not rewrite
      — then the exclusion should probably be the record **class**, not a
      hand-maintained list of five files.

      ## Why the child cannot fix it locally

      Every child-side hatch is worse than the defect, and the child says so:
      a blanket `.pathscanignore` over its records would hide a genuinely stale
      path as well as the noise — which is what its seven real findings prove
      would happen — and a per-line marker on every hit taxes every future
      author. The tool is atelier's.

      Consideration and remediation are atelier's; the reporting child stops at
      this report.
