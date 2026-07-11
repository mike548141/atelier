# 2026-07-11 · 36 — parallel builds + three cold reviews cleared (Fable)

Mike stepped out with "do all the build work on atelier that you can" — the
session ran the open ROADMAP items in parallel: three cold reviews + a
feasibility scoping as fresh-context background agents (the "cold, fresh
session" the review items ask for), with the instruments builds done in the
main line meanwhile. One interruption: a session limit killed the
plugin-bundle reviewer mid-verification; Mike resumed the session and the
reviewer was resumed with its context intact (its half-done secretscan plant
question answered properly on resume — the plants were malformed, not a
scanner miss).

## Reviews (all PASS-WITH-FINDINGS, all findings dispositioned same day)

- **PRINCIPLES §8 "Leverage"** — `reviews/2026-07-11-principles-8-leverage.md`.
  Placement verified against pre-change text; ties hold; the gold-plate
  discipline genuinely bounds it. 3 findings [fixed]: the intro's "§1–7"
  swept to "§1–8" (the reviewer's sharpest observation: §6's own
  stale-claim-sweep rule, violated two sections above §6), §7's "Numbered
  last" opener made position-independent, and the optional
  observed-vs-predicted recurrence evidence bar taken.
- **CONCURRENCY "Every branch ends put away"** —
  `reviews/2026-07-11-concurrency-put-away.md`. Fork exhaustive for lines of
  work; no RECORD/REVIEW conflict. 3 findings [fixed]: bearing's
  "multiple sessions" grounded to the two reconstructible events (and
  *sharpened* — the branch was kept deliberately and still generated the
  re-derivation tax); scoping clause for integration/permanent branches;
  `archive/<date>-<name>` per RECORD's absolute dating.
- **Plugin bundle (PR #3)** — `reviews/2026-07-11-plugin-bundle.md`. The big
  one: driven live in an isolated worktree — validate/install/uninstall at
  user scope (config verified clean after), `/atelier:scan` honest in a
  foreign repo, install-hook block/pass/fail-closed re-proven, and
  **merge-is-go-live proven directly** (marketplace add from GitHub fails
  today; the README's install instructions only become true with the merge).
  **Nothing blocks the merge.** Findings 1–3 [fixed] on the branch
  (`030f185`, pushed — PR #3 updated): the version-pinned-scanner-path
  update trap documented in install-hook's tell-the-user list + README; both
  skills' `${CLAUDE_PLUGIN_ROOT}` doctrine refs made location-relative
  (expansion in skill context was the one thing the reviewer couldn't
  verify — the rephrase removes the dependence); "two companion behaviours"
  → three. Go-live stays Mike's call. Reviewer's worktree/branch put away
  per the (just-reviewed) rule: zero unique commits, straight delete.

## Builds

- **ccrepo full ccusage breakdown** — Cache Create/Read columns + a derived
  Cache Hit ratio (reads ÷ prompt-side tokens) in table, children, and
  `--json`; footnote defines it. Fixtures corrected to ccusage's real shape
  (totalTokens includes cache). Driven live: repo hit rates read 95–98%,
  exactly the point-don't-paste signal MODEL-ECONOMICS wants observable.
  (Caught + fixed my own test theatre mid-build: an assertion I'd written
  with `|| true` was a no-op — rewritten as a real assertion.)
- **cctranscript `N.M` reply IDs** — both roadmap decisions taken and stated:
  replies = text replies only (the citable unit; think/tool stay unnumbered
  under `--full`), and `--json` carries `ref` per turn. Pre-prompt replies
  number under exchange 0. `numberTurns()` pure, unit + contract tested;
  driven live.
- **create-repo delete-branch-on-merge** — the skill's create-remote step and
  REPO-STANDARD's new-repo process both gain the `gh repo edit
  --delete-branch-on-merge` step (standard, not option).
- **ccrepo actuals-vs-estimate — config designed, code held** (the item's own
  design-before-code rule): `instruments/README.md` § "ccrepo billing model".
  Machine-local `~/.claude/ccrepo-billing.json` (spend data never in a repo;
  absent ⇒ unchanged behaviour), plan = sunk monthly cost + `covers[]`
  families at $0 marginal, uncovered models keep API-rate as actual;
  limits/overage out of scope v1, stated. Build once Mike confirms the shape.
- **VS Code UI — scoped, not built** (as the item required). Grounded
  findings: the official extension exposes no third-party hooks; the
  statusline can carry per-repo cost but renders only in terminal surfaces.
  Recommended: a tiny sideloaded companion extension (status bar +
  tooltip off `ccrepo --json`, local `.vsix`), ~4–6 h, with a ~1 h spike as
  the feasibility proof. Full report condensed into the ROADMAP item.

## Floor

Full floor run before commit: tools suite **205 OK**, all four scanner
selftests OK, scan triad + linkscan clean over the whole tree, Node
instrument tests **22/22** (was 20; +numberTurns unit, +cacheHitRate unit).
CI watched on GitHub after push.
