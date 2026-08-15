# atelier — Claude session onramp

This repo *is* the operating model. When working here you are editing the rules
you work by everywhere else — so hold them especially tightly here.

**Repo facts:** `mike548141/atelier` · **Visibility: PUBLIC** (ADR 0005,
2026-07-10). A push *is* publication now — the no-personal-data boundary binds on
**every commit**, and the pre-commit scan hook is load-bearing, not a
private-repo nicety. Verify: `gh repo view mike548141/atelier --json visibility`.

## Read order at session start

1. Sync first: `git pull --rebase --autostash`, and **assume another session may
   be live** — a clean tree is not proof you're alone (this repo's own
   commit-small-push-fast hygiene means a disciplined parallel session leaves the
   tree clean between commits). Uncommitted changes you didn't make are positive
   proof another session is live: move to a worktree before touching anything.
   Absent that proof, still take a worktree by default for write-heavy or
   multi-commit work; reading needs no ceremony (`docs/method/CONCURRENCY.md`
   § The trigger).
2. `docs/method/00-APEX.md` — the frame everything sits inside.
3. `README.md` — what atelier is and its layers.
4. Tail of `docs/SESSIONS.md` — where the last session left off. A last commit
   then silence with **no closing entry** means the last session either died
   mid-flight **or is still live** — run the read-first recovery sweep
   (`docs/method/CONCURRENCY.md` § Surviving an interrupted session) before
   assuming either, and before starting new work.
5. `docs/ROADMAP.md` — what's open. It is the board's **generated index**
   (one file per item under `docs/roadmap/`; edit the item file, then
   `python3 tools/board.py rebuild` — never the index itself).

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
(`AUTONOMY.md`). The repo is **public, `mike548141/atelier`** (ADR 0005) — routine
pushes are granted, and a push is now publication, so the pre-commit scan hook
binds on every commit. The making-public floor is **spent** (ADR 0005 was the
confirmation). The live floor is the next deliberate *widening* — a public
announcement, a published package, a plugin/skills bundle — which stays Mike's
call, never the agent's initiative. And because the repo is public, the
no-personal-data boundary is load-bearing continuously, not just at publish.

## Layout

- `docs/method/` — how we work (shareable doctrine)
- `docs/build/` — how we build (repo-craft standard + templates)
- `docs/decisions/` — ADRs · `docs/reviews/` — peer-review briefs

## Conventions

- Conventions — currency, date/time format, encoding, language, timezone — are
  declared in [`docs/method/CONVENTIONS.md`](docs/method/CONVENTIONS.md), the
  canonical default-frame doc: NZ English with macrons on te reo Māori; UTC
  timestamps at rest, local on presentation; ISO 8601 dates; UTF-8; NZD.
- Git identity `Mike Clements <mike@cxi.nz>`; commit messages  <!-- leakscan:allow:email,local-term: author's own attribution; named worked example (ADR 0005), adopters substitute their own identity -->
  `area: imperative subject`, why-dense body, Co-Authored-By trailer.
- Before finishing a session, append a `docs/SESSIONS.md` entry.
