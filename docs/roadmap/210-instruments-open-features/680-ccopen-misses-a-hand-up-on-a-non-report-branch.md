- [~] 🔎 **`ccopen`'s hand-up read is narrower than the doctrine it reports on: it counts
      🔒 Claimed by session a2097e54 (`atelier-b2`, Opus 5.5), principal-opened by
      `/atelier:work run`.
      (claimed 2026-11-27-1226, wt: atelier-qr-a209-handup)
      a PR as a hand-up only by its head ref, so a child's filing on any other branch
      reads as "other open"** `[S][tool]`. Found 2026-11-27 by session 9c5fa72c
      (`atelier-fa`). `PROPAGATION.md` § *Report without harming the parent* names a
      hand-up by "a `report-` head ref or a hand-up title"; `instruments/ccopen`
      (`HANDUP_HEAD`) matches `report-` or `handup/` on the head only, and reads no
      title. A child's filing of `210/670` came in on `handup-limit-watch-instrument`
      (a hyphen, not a slash) with an ordinary `board …` title, so `ccopen` reported
      "0 hand-up PRs open · 1 other open" and said ready to start; the orchestrator
      found it only by reading `gh pr list` by hand. Two halves, both owed:
      1. `ccopen` also counts a PR whose body or title says it was filed from a child
         (the doctrine's "hand-up title"), or else lists every other open PR by title
         so a reader can judge, rather than a bare count.
      2. The child-side route (the filing skill or text) names the branch form, so a
         filer does not invent `handup-`.
      **Not fixed in passing:** filed under `CLAUDE.md`'s rule that a doctrine or tool
      defect is reported first.
