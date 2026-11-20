- [x] **`remove` compares against local `main`, which a direct push leaves
      stale.** After `git push <branch>:main`, `remove` refused — *"branch … is
      not merged into main"* — because local `main` had not moved.
      `git merge-base --is-ancestor HEAD origin/main` said otherwise, correctly.
      The guard is right to exist; its referent should be the remote integration
      branch, or it teaches `--force` as the routine escape from a safety check.
