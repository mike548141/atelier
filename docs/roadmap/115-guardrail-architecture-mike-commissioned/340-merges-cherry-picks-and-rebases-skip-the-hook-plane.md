- [ ] 🔎 **Merges, cherry-picks and rebases make commits the hook plane
      never sees** `[S][tools]`. Hand-up filed 2026-10-16 by a private
      child, found by a cold review there and measured again before filing.
      Not fixed in the child's place: the floor hook is the house's.
      **What happens.** The floor's hook plane runs from `pre-commit`
      (atelier ships `.githooks/pre-commit` only). Git does not run
      `pre-commit` for a merge commit made by `git merge --no-ff`, nor for
      the commits `git cherry-pick` and `git rebase` write. Measured on git
      2.50.1 with a throwaway repo whose `pre-commit` prints and exits 1:
      `merge --no-ff`, `cherry-pick` and `rebase` all exit 0 and the hook
      never runs. Only a merge that stops on a conflict and is finished
      with `git commit` goes through `pre-commit`.
      **Why it matters.** The orchestrated queue run lands every worker's
      branch with `merge --no-ff` (`CONCURRENCY.md`), and the worker's own
      commit ran the hook on the worker's base, not on the merge result.
      Two clean branches can combine into a tree no hook plane ever
      checked: a staged-plane guard that would have refused the combined
      tree is silent, and CI is the first and only plane to see it. On a
      check that runs only at the hook (for example a local, credentialed
      tripwire that CI cannot run), nothing sees it at all.
      **The work.**
      1. Ship a `pre-merge-commit` hook beside `pre-commit` that runs the
         same hook plane over the merge's staged tree (git invokes it for
         an automatic merge commit, and `--no-verify` skips it just as it
         skips `pre-commit`).
      2. Say plainly in `GUARDS.md` (or wherever the hook plane is
         described) that cherry-pick and rebase have no client-side hook
         that covers them, so the commits they write are checked by CI
         only. A `post-rewrite` hook can warn after a rebase but cannot
         refuse.
      3. Consider whether `floorfleet.py` should report a child that
         installs `pre-commit` but not `pre-merge-commit`.
      review: warranted, light — a guard-coverage change on every repo's
      hook plane.
      🔎 **Verified at HEAD 2026-10-16** (1501 UTC queue run, a read-only
        Sonnet worker): CONFIRMED on git 2.50.1: with a failing pre-commit,
        merge --no-ff, cherry-pick and rebase exit 0 and never run it; a
        conflicted merge finished by git commit does. A pre-merge-commit hook
        does fire on a clean merge. Atelier ships pre-commit only; GUARDS.md
        is silent. Adjacent: 320/480.
