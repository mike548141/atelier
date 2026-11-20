- [x] **`secretscan`/`leakscan` now refuse an absolute positional path in
      `--staged` mode** (exit 2, naming the working form). git lists staged paths
      repo-relative, so an absolute one matched no prefix: the filter emptied the
      staged set and the scan exited 0 — a boundary check that covered nothing,
      indistinguishable from one that found nothing wrong. The silent-success
      class (linkscan L1) these tools already close for a *missing* path, reached
      through a different door.

      Found for real, not theorised: `tools/floor.py`'s first draft rendered
      absolute paths on the staged plane and every boundary check across the
      estate passed green; only the planted-secret commit tests caught it.
      `floor.py` was corrected at the time so the estate was never exposed, but
      the footgun stayed loaded for anyone calling the scanners directly.

      Fixed at the class, not the instance: those two are the *only* scanners
      with a staged mode, so there is no third waiting to be rediscovered.
      Verified live — absolute refused (rc 2), a relative subtree still blocks on
      a real finding (rc 1), whole-diff cover still blocks (rc 1). Pinned in both
      test suites. Commit `6998c2a`.
