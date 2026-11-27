- [~] 🔎 **In git mode, `secretscan`, `leakscan` and `conflictscan` skip untracked,
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
      **Built (session 4ce066ba queue run).** Reproduced first in a
      throwaway git repo: an untracked file in `.vscode/` and the same bytes in `ctl/`; all
      three scanners named only `ctl/`, and the tally read "not counted (git walk)"
      (`conflictscan` printed no pruned part at all). Fixed the cheap way: `filewalk`'s git
      walk now counts the listed paths the skip names drop (`tools/filewalk.py`), the files
      read are unchanged, and `conflictscan` takes the counter. The staged plane never walks,
      so skip names do not apply to it. Cold pass: not yet queued.
      🔒 Claimed by session 4ce066ba (`atelier-c1`, Opus 5.5), principal-opened by
      `/atelier:work run`.
      (claimed 2026-11-27-0045, wt: atelier-qr-4ce0-gitskip)
