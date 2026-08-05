# build/ — how we build

The repo-craft layer: the standard shape every project repo takes, and the
templates that seed it. Where `method/` is estate-wide and mostly non-code,
`build/` is specifically about **software project repos**.

This layer owns repo *shape*. It points up to `method/` for the cross-cutting
doctrine (evidence, records, review, propagation, autonomy) rather than copying
it — a second copy drifts.

## Contents

- **`REPO-BOUNDARY.md`** — the decision *before* the standard: whether a piece of
  work is its own repo, a component (folder in an existing repo), or a monorepo
  folder — by independent-lifecycle discriminators (visibility, cadence,
  ownership, reuse, blast radius). Advise proactively; when ambiguous, prefer the
  reversible direction.
- **`REPO-STANDARD.md`** — the standard: product-in-a-subfolder, sizing to the
  repo type, the standard file set (with pointers up to `method/` for the
  doctrine-heavy docs), honest-CI, repo-craft conventions, and the two processes
  (new repo / standardise an existing one). The readable, forkable source.
- **`templates/`** — the seed files the standard describes: README, CLAUDE.md
  (carrying the stamped doctrine block), CONTRIBUTING, CHANGELOG, LICENSE
  (Apache-2.0, the house default — verbatim text; the holder goes in the
  appendix line + NOTICE), NOTICE,
  gitignore, the `.claude/` allowlist, the `docs/` set (ARCHITECTURE, ROADMAP,
  SESSIONS, ECONOMICS, decisions/, reviews/), both CI workflows, and
  `tools/linkscan.py`. One source, shared by the `create-repo` skill and the
  published methodology — moved here from the skill's private copy 2026-07-10 and
  scrubbed of instance residue (a hardcoded holder, a project name, a stale
  ros-is-canonical pointer).

## Still owed (ROADMAP)

1. **Supply-chain / release standard** — committed deterministic SBOM + keyless
   signing. Its own doc when written; currently deferred (external tooling hits
   the tool-install floor — see ROADMAP). The licence-consistency pre-publish
   gate landed 2026-07-10 as `tools/licenscan.py` (review B11 swept this line —
   it still listed the gate as unwritten after the tool shipped).
