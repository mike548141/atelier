- [x] **`linkscan` prints the replacement path** where it is computable
  (`b89a306`) — `↳ did you mean: ../../tools/x.py` beneath the finding. Turns a
  17-item chore into 17 obvious edits.
  - **Two tiers, both requiring a *unique* answer**, because a confident wrong
    suggestion costs more than none: (1) the path resolves from the **repository
    root** — the commonest break by a wide margin, a root-relative path written
    inside a file two levels down; (2) exactly **one** file in the tree carries
    that basename, the moved-or-renamed case. Two candidates and it stays
    silent. Dot-directories are skipped: a match under `.github` is not
    something a reader can follow.
  - **Advisory only, and pinned as such** — a suggestion never changes a verdict
    or an exit code, and nothing is rewritten. A test asserts the suggested path
    *actually resolves*, so the tool cannot confidently mis-advise.
  - 668 python tests (was 661).

  Original item: **`linkscan` could name the fix for its commonest class.** *(claimed 2026-07-26-0845, wt: none — inline on main)* One repo carried 17 broken links of a single shape: a repo-root-relative path written inside a `docs/` file two levels down, so it resolves to `docs/<dir>/<path>` and 404s. The correct target is computable from the finding. Idea: print the suggested relative path alongside the error. Turns a 17-item chore into 17 obvious edits, and this shape will recur wherever records cite source files.
