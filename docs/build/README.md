# build/ — how we build

The repo-craft layer: the standard shape every project repo takes, and the
templates that seed it. Where `method/` is estate-wide and mostly non-code,
`build/` is specifically about **software project repos**.

## Status: pointer, not yet extracted

The working version of this standard currently lives as the **`create-repo`
skill** (`~/.claude/skills/create-repo/`), which encodes:

- **Product in a subfolder** (`site/`, `src/`, …); the root holds only meta.
- The **standard file set** — README, CLAUDE onramp, CONTRIBUTING, CHANGELOG,
  LICENSE (Apache-2.0), `.gitignore`, committed `.claude/settings.json`, real
  CI sized to the repo.
- **docs/** — ARCHITECTURE, ROADMAP (+ ROADMAP-DONE when it grows), append-only
  SESSIONS, MODEL-ECONOMICS, numbered ADRs in `decisions/`, peer-review briefs
  in `reviews/`.
- Sizing the standard to the repo *type* (static/web, Python package, infra,
  docs) — not every element fits every repo.

## What's owed here (ROADMAP)

1. Extract the standard into this layer as the readable, forkable source.
2. **Rewire `create-repo` to inherit from atelier** — reference this doctrine
   and seed new repos from it, instead of copying empty templates that are born
   wisdom-empty. That closes the original gap: new projects should inherit the
   reasoning, not just the shape.
3. Move the templates (`templates/`) alongside the standard so the skill and the
   published methodology share one source.
