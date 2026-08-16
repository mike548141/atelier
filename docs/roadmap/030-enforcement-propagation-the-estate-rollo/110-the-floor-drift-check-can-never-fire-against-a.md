- [ ] **The floor drift check can never fire against a stale checkout — the
      canonical `<SHA>..HEAD` range is the defect.** `PROPAGATION.md`'s floor
      region tells every child to run
      `git -C "<atelier-path>" log --oneline <SHA>..HEAD`. That reads the
      child's *local* atelier checkout, and nothing keeps that checkout
      current. Measured at faves on 2026-08-16: the checkout sat 16 commits
      behind its own `origin/main`, so a pin moved to the true tip made the
      range run backwards and report **nothing** — `0107000..HEAD` returned
      0 commits on a tree whose doctrine had moved 38. This is the mirror of
      the failure the same bullet exists to describe. A check that always
      fires is a check nobody reads; a check that can never fire is one
      nobody *can* read, and it fails silently, which is worse. Suggested
      fix, matching what faves applied to its own copy in `2df2564`:
      `git -C "<atelier-path>" fetch -q &&`
      `git -C "<atelier-path>" log --oneline <SHA>..origin/main`.
      That copy therefore **diverges from the canonical region**, and a
      `stampscan` retrofit would red it until the canonical text catches up —
      so the fix is owed here, in `PROPAGATION.md`, not at the child. Paired
      with the fleet sweep in the item below. Raised by Mike, 2026-08-16,
      from a faves session's pin bump.
