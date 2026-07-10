# atelier — Claude session onramp

This repo *is* the operating model. When working here you are editing the rules
you work by everywhere else — so hold them especially tightly here.

**Repo facts:** `mike548141/atelier` · **Visibility: PRIVATE** (so a push is not
publication — but *making it public* is a floor action; confirm). Verify:
`gh repo view mike548141/atelier --json visibility`.

## Read order at session start

1. `docs/method/00-APEX.md` — the frame everything sits inside.
2. `README.md` — what atelier is and its layers.
3. Tail of `docs/SESSIONS.md` — where the last session left off.
4. `docs/ROADMAP.md` — what's open.

Read the rest of `docs/method/` on demand when a change touches it.

## Hard constraints

- **No personal data, ever.** No health, family, financial, or personal-estate
  context enters this repo. atelier is built to be shareable; that boundary is
  the whole reason it's safe to share. Mike's personal context stays in
  `~/.claude/` and never travels here. (This is stricter than most repos — here
  it's the point, not a precaution.)
- **Live the doctrine you're writing.** The apex (`00-APEX.md`) applies to the
  agent editing this repo: honest about what's done vs stubbed, no rounding a
  half-extraction into "extracted".
- **Ground everything.** Doctrine here is extracted from real, decided practice
  (mostly `ros`) — never invented to fill a heading. If it can't be grounded
  yet, stub it and say so, per `create-repo`'s stub-don't-fabricate rule.

## Autonomy in this repo

Full standing grant applies: commit + push + manage PRs at discretion
(`AUTONOMY.md`). The repo exists — **private, `mike548141/atelier`** — so routine
pushes are granted. The one thing that still stops to ask is the floor item it
sits nearest: **making it public** (or widening its audience) is a deliberate
private→public act — confirm, cite the floor, never flip visibility on your own
initiative. This is private-first until Mike decides otherwise.

## Layout

- `docs/method/` — how we work (shareable doctrine)
- `docs/build/` — how we build (repo-craft standard + templates)
- `docs/decisions/` — ADRs · `docs/reviews/` — peer-review briefs

## Conventions

- NZ English; macrons on te reo Māori.
- Git identity `Mike Clements <mike@cxi.nz>`; commit messages
  `area: imperative subject`, why-dense body, Co-Authored-By trailer.
- Before finishing a session, append a `docs/SESSIONS.md` entry.
