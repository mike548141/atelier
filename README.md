# atelier

**The operating model for working with Claude as a teammate.**

`atelier` is the extracted, versioned home of *how* Mike and Claude work —
the doctrine that made the `ros`/`tiki` project good to build in, lifted out of
that one repo so every project can inherit it and so it can be shared with
peers. An atelier is a workshop where craft is practised; this is the workshop's
standing rules.

It exists because the good stuff — design principles, model economics, the
autonomy posture, session discipline, doc-as-code — used to live *inside one
repo*. New projects were born shape-complete but wisdom-empty, and the reasoning
had to be re-taught each time. atelier is the missing middle layer: general
doctrine that sits above any single project.

## The layers

The same general→specific inheritance the estate's own tools use, applied to how
we work:

| Level | Where | What |
|---|---|---|
| You / machine | `~/.claude/` | personal context, model default, global permission floor — never travels into a repo |
| **House doctrine** | **this repo** | principles, model economics, autonomy, storage, concurrency, session + doc-as-code discipline, the repo-build standard |
| Project | each repo's `CLAUDE.md` + `docs/` | that product's truth, and which principles bind hardest here |
| Session | one worktree, one branch | a unit of work |

## Structure

| Path | Holds |
|---|---|
| `docs/method/` | **how we work** — the shareable crown jewels. Read `00-APEX.md` first. |
| `docs/build/` | **how we build** — the repo-build standard and templates (repo craft) |
| `docs/decisions/` | ADRs — decisions that rejected a real alternative |
| `docs/reviews/` | peer-review briefs (work is reviewed by a more capable model before it's trusted) |

### `docs/method/` — the operating model

- **`00-APEX.md`** — honesty is absolute, then the AI-adapted Three Laws. Above
  everything else.
- **`AUTONOMY.md`** — when the agent proceeds vs stops to ask; per-repo grants.
- **`STORAGE.md`** — GitHub = master, iCloud = backup/offline, laptop =
  disposable; keep churn out of iCloud.
- **`CONCURRENCY.md`** — one worktree per line of work; serialise real-world
  side-effects.
- **`PRINCIPLES.md`**, **`MODEL-ECONOMICS.md`** — *(extraction in progress — see
  ROADMAP; the canonical source is currently ros `docs/`.)*

## Status

Early. The `method/` layer is standing up first; the `build/` layer (the
`create-repo` standard) and the heavier extractions from `ros` follow. See
`docs/ROADMAP.md`.

## Sharing

Private-first: shared with Competitive Edge / EPL peers to harden in real use
before any public release. No personal, health, family, or financial context
ever enters this repo — that stays machine-local by design, which is what makes
atelier safe to hand to a colleague. Licensed Apache-2.0.
