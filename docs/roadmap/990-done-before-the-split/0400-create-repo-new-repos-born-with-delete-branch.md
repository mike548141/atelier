- [x] **create-repo: new repos born with delete-branch-on-merge** — DONE
      2026-07-11: the skill's create-remote step now follows `gh repo create`
      with `gh repo edit --delete-branch-on-merge` (stated as standard, not
      option), and REPO-STANDARD's new-repo process gained step 6 saying the
      same — the landed half of CONCURRENCY's put-away rule automatic at birth.
