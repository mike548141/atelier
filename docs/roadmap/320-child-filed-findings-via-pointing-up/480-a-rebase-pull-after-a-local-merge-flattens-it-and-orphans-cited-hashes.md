- [ ] 🔎 **MISSING HOUSE RULE — the doctrine's own sync command
      (`git pull --rebase`) flattens local merge commits and gives every
      replayed commit a new hash, so a record that cites hashes written before
      the push cites commits that exist nowhere on the integration branch**
      `[S][doctrine]` — a hand-up from a private child, filed via § *Pointing
      up*, 2026-10-02. **Evidenced: one instance, measured.**

      ## The instance

      The doctrine (`CONCURRENCY.md`; the floor's Concurrency bullet) says to
      sync with `git pull --rebase --autostash`, push after each commit, and —
      in an orchestrated run — merge each worker branch to the integration
      branch per item with records written per merge, citing commit hashes.

      An orchestrator merged two worker branches with `git merge --no-ff` in a
      records worktree, then ran `git pull --rebase origin main` before pushing,
      because main had moved. A plain `--rebase` **drops merge commits and
      replays the branch commits linearly**, so both merges were flattened and
      every replayed commit got a **new hash**. The board close-notes had been
      written *before* the push and cited the pre-rebase hashes (worker commits
      and merge commits alike). Those hashes then existed nowhere on main.

      **How it was caught:** by checking every cited hash with
      `git merge-base --is-ancestor <hash> origin/main`; the dangling citations
      were corrected in a follow-up commit. Nothing in the house's checks would
      have found them.

      ## Why it matters

      A record's commit citations are *evidence* (`EVIDENCE.md`). A silent
      rewrite turns them into dangling references that read as valid and
      resolve to nothing on the branch the record lives on. The cause is not
      operator error: it is the house's own prescribed sync command, whenever a
      local merge is followed by a rebase-pull. The orchestrated-run shape
      (merge per item, record per merge, push later) makes the sequence
      routine rather than exotic.

      ## Candidate remedies — for atelier to weigh, not decided here

      - **Sync before merging:** fetch and rebase the records branch first, then
        merge, then push immediately, so no rebase follows the merge.
      - **`git pull --rebase=merges`** (a.k.a. `--rebase-merges`) when merges
        are local, which preserves merge topology; hashes still change for
        replayed commits, so this narrows the problem rather than removing it.
      - **Cite hashes only after the push lands**, i.e. the record's hash
        citations are written (or re-verified) against the pushed history.
      - **A check** that every hash cited in a staged record resolves on the
        target branch (`git merge-base --is-ancestor`). Mechanisable; it would
        have caught this instance, and it generalises to any rewrite (amend,
        squash-merge, force-push), not only rebase-pull.

      ⚠️ **Not established:** how often this occurs across the estate. One
      instance is measured; the rate, and whether squash-merging PRs produces
      the same dangling-citation class, are not.

      📎 **2026-10-05: a second shape of the same class, from P7's harvest**
      (`260/090`). A child's review record cites a commit that was amended
      before the push, so the cited SHA is on no pushed branch. The cause
      differs, an amend rather than a rebase-pull, but the defect is the
      same: a hash in a record that a reader cannot reach. Any remedy here
      should check reachability from the pushed branch, whatever produced
      the orphan.
