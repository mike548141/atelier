- [x] 🔎 **`ccopen`'s hand-up read is narrower than the doctrine it reports on: it counts
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

      **Done 2026-11-27** (worker of session a2097e54, branch `qr-a209-handup`):
      1. `instruments/ccopen`: a PR reads as a hand-up by head (`report-`,
         `handup-` or `handup/`), title (*hand-up*) or the start of its body's
         first line (*hand-up*, *filed finding*, *a private child*; the body is
         now fetched), and every other open PR is listed (`other open: #n title
         (head)`, five shown, the rest counted) and carried in `--json` as
         `data.other` beside `data.list`, which now says which place matched
         (`by`). Field set stable: `handups`, `otherOpen`, `list`, `other` are
         all present in every case, empty when none. Shape chosen because the
         doctrine names three places a filer says it (branch, first line, PR
         body) and a net of three can still miss, so the listing lets a reader
         judge what the net lets by; a body read past the first line was
         rejected on evidence (atelier's own PRs say "lands the hand-up PRs").
         Tests beside `ccopen.test.js` (two new, the 210/670 shape and the
         listing and stable-fields case); `ccopen.design.md` and
         `instruments/man/ccopen.1` updated.
      2. Canonical form, by evidence: `report-<subject>-<HHMM>`, no repo token
         (`PROPAGATION.md` § *Report without harming the parent* rule 1; the
         census row PRO33; `namescan`'s own fixtures). `handup/` was the tool's
         own, never in doctrine; `handup-` is what a child invented when the
         child-side text said only "name the branch for the report". The child
         block (`PROPAGATION.md`'s standard block and
         `docs/build/templates/CLAUDE.md`) now names the form and says never
         `handup-`; rule 1 says use that spelling and no other. Children's
         stamped copies of the block pick it up at their next pin bump.
      Commitment: a read-only, advisory open-time read and the wording of a
      branch name; nothing blocks on either.
      review: not warranted — a fix to an already-reviewed read-only instrument
      whose tests cover it (a wrong read here is a loud ❌ in atelier or a ⚠️
      elsewhere and a listed PR, never a silent grant), plus a wording
      correction that names an existing rule's form and adds or changes no rule
      (`REVIEW.md` § *Whether work earns a review at all*, the never list).
