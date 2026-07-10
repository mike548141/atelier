# Changelog

All notable changes to atelier. Format: [Keep a Changelog](https://keepachangelog.com/);
newest first. Everything stays under _Unreleased_ until there's a reason to tag.

## [Unreleased]

### Added
- `tools/worktree.py` — one command for `CONCURRENCY.md`'s "one worktree per
  line of work": `start`/`list`/`land`/`remove`. Bakes the doctrine's guards into
  the tool — refuses an iCloud base (sync corrupts a live `.git` index), branches
  off the integration branch so a line never inherits a half-done branch, flags
  stale/dirty worktrees (merge hazards + leaked file handles), and refuses to
  delete uncommitted/unmerged work without `--force`. Zero-dep, `--json`,
  `--selftest`, fail-safe exit codes; 12 stdlib tests over real throwaway repos.
  Makes the parallel-work doctrine a tool, not just prose (Mike, 2026-07-10).
- `tools/leakscan.py` — the mechanical leak-scan (first executable control):
  shareable structural patterns + a machine-local literal-term list, run as a
  pre-commit hook and in CI to keep personal/estate data out of a shareable
  repo. Zero-dep, `--json`, self-tested; caught real address/coordinate leaks in
  its own fixtures on first run. `--disable <rules>` + `--staged <subtree>` scope
  it to a networking repo's shareable subtree (proven on ros `tiki/`).
- Initial scaffold: the `method/` layer stands up first.
- `docs/method/00-APEX.md` — honesty is absolute, then the AI-adapted Three
  Laws (extracted from ros `docs/PRINCIPLES.md` §0, generalised estate-wide).
- `docs/method/AUTONOMY.md` — per-repo autonomy framework; reconciles the
  ros (commit-only) vs faves (commit + push, deploy-on-push) grants.
- `docs/method/STORAGE.md` — GitHub master / iCloud backup / Time Machine→NAS
  whole-machine / laptop disposable; keep churn (venvs, caches, worktrees) out
  of iCloud.
- `docs/method/CONCURRENCY.md` — one worktree per line of work; serialise
  real-world side-effects.
- `docs/method/TOOLBOX.md` — keep a tool manifest; approved-but-missing may be
  installed; the personal inventory stays machine-local, not in this repo.
- `docs/method/PROPAGATION.md` — the propagation mechanism: thin-anchor /
  fat-pointer (inlined safety floor + SHA pin + session-start drift check), the
  standard child doctrine block, the layer-override rule, and the enforcement
  clause (read ≠ complied). Versioning decided: the commit SHA is the version;
  CHANGELOG is the human-readable index; tags reserved for milestones.
- `docs/method/EVIDENCE.md` — the machinery behind the apex's honesty (harvest
  A1): authority tiers, acquisition-method error risk, absolute dating,
  store-the-rule-not-the-value, one-fact-one-home, trigger-based refresh,
  invest-where-the-model-is-weak, enforce-by-machine. Generalised from a private
  reference-library `STANDARDS.md`.
- `docs/method/REVIEW.md` — the enforcement half (harvest A2): independent
  review by a more capable model; three lenses; brief-on-top/verdict-below
  lifecycle; inline-vs-batched triggering.
- `docs/method/RECORD.md` — session + doc-as-code discipline (harvest A3):
  lockstep doc change, append-only session log with detail-on-demand, ADRs for
  re-litigable decisions, absolute dating; the record is what makes a session
  resumable cold.

### Changed
- **Review reframed: independence, not superiority (2026-07-10 method-layer
  review, R1).** `REVIEW.md` no longer claims a "*more capable* model" reviews —
  the mechanism is an **independent capable review**: fresh context, a different
  model's blind spots, an adversarial brief, capability as a floor. Same phrase
  aligned in `PROPAGATION.md`'s enforcement clause, README, `RECORD.md`.
- **Standard child doctrine block regains two floor cases** dropped in the
  ~15-line squeeze (method-layer review P1/P2): *new trust surfaces* (deploy
  keys, webhooks, CI secrets, OAuth grants) and the *deploy-on-push new-content*
  qualifier on the routine-push grant. Children re-stamp at next pin bump.
- `PROPAGATION.md` enforcement clause names its honest window (routine sessions
  that skip the drift check are caught only at the next reviewed slice);
  `EVIDENCE.md` §1/§4/§12 scoped honestly (two-register provenance,
  primary-read corroboration, no validator for in-conversation claims);
  `RECORD.md` lockstep scoped to the shared branch (WIP may trail on its own
  branch); `PRINCIPLES.md` mitigation-under-uncertainty + special-case tests
  regain generalised precedent lines. All from the 2026-07-10 method-layer
  review (`docs/reviews/2026-07-10-method-layer.md`).
- `docs/method/PRINCIPLES.md` — extracted from stub to the canonical general
  spine (§1–7 + precedence ladder + situation tests, generalised off tiki with
  the cases kept). ros `docs/PRINCIPLES.md` is now the *bearings + case-law*
  child that points up; trimming its transitional general-prose duplication is a
  tracked ROADMAP follow-up.
- README, CLAUDE onramp, LICENSE (Apache-2.0), house `.gitignore` +
  `.claude/settings.json`.

### Pending (see ROADMAP)
- `MODEL-ECONOMICS.md` extraction from ros.
- The `build/` layer: the `create-repo` standard + templates.
- `create-repo` rewired to inherit from atelier instead of copying empty
  templates.
