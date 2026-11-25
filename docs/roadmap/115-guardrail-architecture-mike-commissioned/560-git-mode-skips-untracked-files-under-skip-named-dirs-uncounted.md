- [ ] 🔎 **In git mode, `secretscan`, `leakscan` and `conflictscan` skip untracked,
      not-ignored files under skip-named directories, and nothing counts them.** Found
      2026-11-25 by the worker that built `320/900` (session f8dd3843's queue run), not yet
      reproduced by a second session. `320/900` made the plain-tree (`os.walk`) fallback count
      what it prunes; git mode was kept unchanged by that item's brief, and there the skip names
      act on the paths git lists, so an untracked file under, say, `.vscode/` that no ignore
      rule covers is dropped unread and the tally reads "not counted (git walk)". It is the same
      class as `320/900`: a scan that can read green with files unread. **Owed:** reproduce it
      in a throwaway git repo, then decide whether git mode counts those paths (cheap: git has
      already listed them) or reads them; the pre-commit plane reads staged files, so say which
      planes it reaches. *Tier:* build tier.
