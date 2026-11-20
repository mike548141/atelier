- [x] **A4 — LS1–LS5, the repo-local seam's edges.** LS1 Actions log-command
  injection through a child-authored `why`, encoded at the point of
  interpolation. LS2 an executable non-Python script with no shebang crashed
  the floor with a traceback — now a clean BLOCK with the summary preserved.
  LS3 a committed symlink executed out-of-tree code; realpath containment now
  enforced, and the old test exercised lexical strings only, so it overstated
  the guard. LS4 unknown keys in a local declaration read past in silence — not
  cosmetic, since a `planes` typo runs a hook-only check on CI. LS5 a disabled
  local check lost its `local` marking.
