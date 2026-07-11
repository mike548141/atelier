# 2026-07-11 · atelier packaged as an installable Claude Code plugin (Opus)

Mike picked the plugin/skills-bundle packaging as the next widening — "makes the
doctrine travel." Built the v1 bundle and handed it back as **PR #3** on branch
`plugin-bundle`; the marketplace only resolves from the default branch, so **the
merge is the go-live act** — the widening floor stays the principal's call, not
the agent's. Nothing is installable-from-GitHub until Mike merges.

## Format grounded, not remembered

Launched a `claude-code-guide` agent to fetch the *current* plugin +
marketplace schema from the official docs (not memory): `.claude-plugin/
plugin.json` + `.claude-plugin/marketplace.json`, components at root
(`commands/`, `skills/`, `agents/`, `hooks/hooks.json`), `${CLAUDE_PLUGIN_ROOT}`
for plugin-relative paths, a repo can be its own marketplace (`source: "./"`),
public-repo required, and — load-bearing — a Claude Code "hook" is an *event*
hook, so the git pre-commit hook can't auto-install (must be a command/manual step).

## Two design calls made without asking (obvious + reversible-enough)

- **Root-as-plugin (`source: "./"`), not a subfolder.** Looks like it breaks
  REPO-STANDARD's product-in-subfolder rule, but it's *forced by one-source*: a
  `git-subdir` install sparse-clones only the subdir, so a `plugin/` folder could
  not reach `tools/`+`docs/` without copying them — the exact second source
  atelier exists to prevent. Root keeps `${CLAUDE_PLUGIN_ROOT}` = the repo;
  scanners + docs referenced in place. Documented exception (the subfolder rule
  was already scoped to deployable-artifact repos, B8).
- **`version: "0.1.0"`, bumped deliberately — not omitted.** Omitting makes every
  commit (incl. a records commit) a version consumers auto-pull; a real version
  matches ADR 0002 (SHA-as-version) at the consumer edge.

## Scope — Mike took the recommendation (Middle tier)

- **`/atelier:scan`** — the four publish-safety scanners over any repo.
- **`/atelier:install-hook`** — the fail-closed git pre-commit hook; resolves
  `${CLAUDE_PLUGIN_ROOT}/tools` to an *absolute path at install time* (git has no
  such env var at commit time — the one non-obvious correctness point).
- **`session-onramp`** skill — inlines the apex + always-confirm floor, points at
  the bundled doctrine (read on demand).
- **`review-brief`** skill — the REVIEW.md peer-review lifecycle.
- The whole `docs/method` + `docs/build` doctrine as bundled reference.
- Deferred to v2: de-instanced `create-repo` (general → `${CLAUDE_PLUGIN_ROOT}`,
  gh-account/identity/holder → adopter-filled placeholders that stay
  machine-local), plus `worktree`/`fleet-pins` commands.

## Verified end-to-end — exercised, not "looks right"

JSON valid; scan triad + linkscan clean over the new files; suite **205 OK**.
Then the real proof: added atelier as a **local marketplace** (the real parser
accepted `marketplace.json`), **installed to user scope**, and `plugin details`
reported **all 4 components discovered** (`scan`, `install-hook`,
`session-onramp`, `review-brief`; ~320 tok always-on) — then **uninstalled +
marketplace removed** to leave config clean (verified: no plugins installed, no
atelier marketplace; the two empty `{}` settings keys the CLI left are inert).

## The boundary biting its own author again

leakscan blocked the commit on the author's own name in the two manifests'
attribution fields (three hits). This is the approved named-worked-example
identity (ADR 0005) — the same case the CLAUDE.md convention line handles with an
inline `leakscan:allow` — but JSON can't hold that marker, so a **file-scoped
`.leakscanignore` exemption** (tight: two small structured manifests; secretscan
still covers them) is the only mechanism. Then leakscan flagged the *reason
comment* I wrote (it quoted the name) — reworded to not quote it. The boundary
working exactly as designed, twice.

## Left open (deliberately)

- **Go-live: Mike merges PR #3.** Held at the merge line by design.
- **Cold peer review owed** — net-new, first-of-kind, public-facing tooling earns
  a fresh-context review before it's leaned on (ceremony-to-risk). Don't-stack:
  the builder doesn't review its own bundle; a `review-brief` pass is the
  follow-up. Suggest briefing the range on this branch.
- **v2**: de-instanced `create-repo`, `worktree`/`fleet-pins` commands.
- After merge, `create-repo`/REPO-STANDARD could mention the plugin as an install
  path; not stacked here.
