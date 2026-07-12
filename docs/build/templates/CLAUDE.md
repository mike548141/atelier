<!--
  CLAUDE.md — AI session onramp for a repo built to the house standard.

  The block below (## Doctrine — inherited from atelier) is the STANDARD
  DOCTRINE BLOCK. Its canonical text lives in atelier's
  docs/method/PROPAGATION.md — this is a stamped copy, not a second source.
  create-repo fills the four placeholders (<atelier-path>, <SHA>, <owner/repo>,
  <visibility fact>) at scaffold time. When atelier's apex or floor changes, a
  pin bump reviews this wording too (PROPAGATION § the standard child block).

  Everything below the block is repo-specific onramp — fill it with grounded
  content for THIS repo; delete the guidance comments as you go.
-->

## Doctrine — inherited from atelier (pinned `atelier@<SHA>`)

This repo works by the atelier operating model. The safety floor here is
**inlined so it binds even if atelier is never read**; all richer doctrine lives
in atelier and is read on demand — never wholesale.

- **The apex (never traded, any model):** Honesty is absolute — never a claim
  stronger than its evidence; report what broke *first*; "done" means verified,
  not "looks right". Then the Laws, in order: avoid harm → obey your principal →
  self-preserve. Surface a genuine dilemma; never silently resolve it.
- **Always stop and confirm (the floor):** making a private repo public or
  widening its audience; anything truly destructive or irreversible; secrets;
  spending money; anything touching people's safety; widening your own grant
  (record the principal's decision, never originate it); a lockout-class change
  that could sever your own access; installing an unapproved tool or adding a
  new trust surface (deploy keys, webhooks, OAuth/app grants). Everything
  recoverable — commit/push/PR included — just proceed.
- **Concurrency:** `git pull --rebase --autostash` at session start; push after
  each commit. Uncommitted changes this session didn't make ⇒ another session
  is live: move to a worktree — never work around or absorb them. Allocate
  record numbers (session NN, ADR NNNN) at landing, never at session open:
  fresh pull, commit, push at once — first landed wins, the loser renumbers.
- **Source & drift:** canonical doctrine is `<atelier-path>/docs/method/`. At
  session start run `git -C "<atelier-path>" log --oneline <SHA>..HEAD`; any
  output means the house doctrine moved — read it, then bump the pin above
  deliberately.
- **This repo's visibility:** <visibility fact>. Verify:
  `gh repo view <owner/repo> --json visibility`.

---

# <name> — session onramp

<!-- One line: what this repo is. The doctrine block above is the house frame;
     everything here is this repo's specifics. -->

## Read order at session start

1. `docs/ARCHITECTURE.md` — current truth: the stack and why.
2. `docs/ROADMAP.md` — what's open.
3. Tail of `docs/SESSIONS.md` — where the last session left off.

## Hard constraints

- **No personal / instance data.** No health, family, financial, or
  personal-estate context enters this repo. <!-- Tighten per repo: a public-bound
  repo forbids client names too; run the leak/secret scans as hooks. -->
- **Hooks don't travel.** The scan hook and its `hooks.atelierTools` config are
  per-clone — git transports neither, so a fresh clone commits **unscanned**
  until they're reinstalled. Before the first commit on any new clone or
  machine, rewire them (commands in CONTRIBUTING — Development setup).
- <!-- repo-specific invariants: the boundary a change must not cross. -->

## Layout

- `<subfolder>/` — the deployable artifact (never mixed with root scaffolding)
- `docs/` — architecture, roadmap, decisions, session log
- `tools/` — dev/CI helpers

## Dev loop

```sh
<!-- the one command to run it, and the one to run the checks -->
```

## Conventions

- NZ English; macrons on te reo Māori.
- Comments say *why*, not *what*; ADR the re-litigable decisions
  (`docs/decisions/`); append a `docs/SESSIONS.md` entry before finishing.
- Commit messages: `area: imperative subject`, why-dense body.
