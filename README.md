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

## If you're adopting this

atelier is a **named worked example**, not an abstract framework. It's written to
one principal — Mike — grounding real decisions in a real estate (`ros`, `tiki`),
because a principle reads truer anchored to a real call than floated free of one.
To adopt it, **you become the principal**: read Mike's instance to learn the
*shape*, then instantiate it as yourself — your `~/.claude/` context, your estate,
your decisions. The doctrine in `docs/method/` is the general part meant to
travel; the person-and-estate specifics are the worked example you replace.

`ros` and `tiki` are named throughout as **provenance** — the private repo this
doctrine was extracted from, cited so each principle shows its real origin. They
stay private; you can't open them and you don't need to. The citation means
"here's where this was earned", not a link to follow.

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
| `docs/reviews/` | peer-review briefs (work earns trust through independent review — see `method/REVIEW.md`) |
| `tools/` | the mechanical controls that *enforce* the doctrine — e.g. `leakscan.py`, the pre-commit boundary keeping personal/estate data out of a shareable repo |

### `docs/method/` — the operating model

- **`00-APEX.md`** — honesty is absolute, then the AI-adapted Three Laws. Above
  everything else.
- **`AUTONOMY.md`** — when the agent proceeds vs stops to ask; broad standing
  grant (commit/push/PR), with a fixed floor and per-repo narrowing.
- **`STORAGE.md`** — GitHub = master, iCloud = backup/offline, laptop =
  disposable; keep churn out of iCloud.
- **`CONCURRENCY.md`** — one worktree per line of work; serialise real-world
  side-effects.
- **`PRINCIPLES.md`** — the design principles, precedence ladder, and situation
  tests, with generalised cases. **Canonical here** (extracted 2026-07-10);
  child repos keep their bearings + case-law and point up.
- **`MODEL-ECONOMICS.md`** — match the model to the job (plan model builds,
  usage-billed model reviews), the which-pool self-check, tiered authority, and
  session hygiene. **Canonical here** (extracted 2026-07-10); the estate-specific
  numbers stay person-local.

## Status

Early. The `method/` layer is standing up first; the `build/` layer (the
`create-repo` standard) and the heavier extractions from `ros` follow. See
`docs/ROADMAP.md`.

## Sharing

**Public** since 2026-07-10 (see `docs/decisions/0005-going-public.md`),
Apache-2.0. No personal, health, family, or financial context ever enters this
repo — that stays in the operator's private person-level context by design,
which is exactly what makes atelier safe to publish. Because the repo is public,
that boundary is load-bearing on **every commit**: the `tools/` scan hook
(leakscan · secretscan) is the mechanical gate, not a pre-publish afterthought.
Widening further — an announcement, a packaged plugin/skills bundle — is the next
deliberate step, not this one.
