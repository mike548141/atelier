# atelier — Claude session onramp

This repo *is* the operating model. When working here you are editing the rules
you work by everywhere else — so hold them especially tightly here.

**Repo facts:** `mike548141/atelier` · **Visibility: PUBLIC** (ADR 0005,
2026-07-10). A push *is* publication now — the closed personal-data list binds on
**every commit**, and the pre-commit scan hook is load-bearing, not a
private-repo nicety. Verify: `gh repo view mike548141/atelier --json visibility`.

## Read order at session start

1. Sync first — `git status` before `git pull --rebase --autostash`, because
   autostash shelves dirty work that may be a peer's and returns it unstaged
   (`CONCURRENCY.md` § Integration hygiene). Dirty work you didn't make is
   positive proof another session is live: **stop and move to a worktree before
   touching anything, never autostash it**. Dirty work that is yours (a
   predecessor cut mid-flight): commit it or back it out first; the pull runs
   on a clean tree only. And **assume another session may be live** — a clean
   tree is not proof you're alone (this repo's own commit-small-push-fast
   hygiene means a disciplined parallel session leaves the tree clean between
   commits). Absent that proof, still take a worktree by default for
   write-heavy or multi-commit work; reading needs no ceremony
   (`docs/method/CONCURRENCY.md` § The trigger). Run `cclive` too: every live
   session, claim and worktree on this machine, in about two seconds.
2. `docs/method/00-APEX.md` — the frame everything sits inside.
3. `README.md` — what atelier is and its layers.
4. Tail of `docs/SESSIONS.md` — where the last session left off. A last commit
   then silence with **no closing entry** means the last session either died
   mid-flight **or is still live** — run the read-first recovery sweep
   (`docs/method/CONCURRENCY.md` § Surviving an interrupted session) before
   assuming either, and before starting new work. **A cold reviewer skips this
   step:** the log is on the review rules' barred list
   (`docs/method/REVIEW.md` rule 2).
5. `docs/ROADMAP.md` — what's open. It is the board's **generated index**
   (one file per item under `docs/roadmap/`; edit the item file, then
   `python3 tools/board.py --rebuild` — never the index itself).
6. Open hand-up PRs — `gh pr list --state open --json
   number,title,headRefName,createdAt`, read for a `report-` head ref or a
   hand-up title. A child's filed finding has no owner until atelier lands it;
   landing one is the first act of a session that finds one
   (`docs/method/PROPAGATION.md` § *Report without harming the parent*).

Read the rest of `docs/method/` on demand when a change touches it.

## Hard constraints

- **No personal data beyond the closed list in `docs/PERSONAL-DATA.md`.**
  No health, family, financial or personal-estate context enters this repo, and
  neither does any other person's name, contact detail or address. The list is
  the one place that says what personal data atelier holds (the published
  author identity and account name), why, and in which files; a test keeps it
  matching the tree. It is **closed**: in a public repo only Mike grants an
  exception, in his own words, so a session that thinks it needs one stops and
  asks him. An allow-marker on a line is not a grant. Mike's personal context
  stays in `~/.claude/`. The purpose rule and his words are in
  `docs/build/REPO-STANDARD.md` § *Repo-craft conventions*.
- **Live the doctrine you're writing.** The apex (`00-APEX.md`) applies to the
  agent editing this repo: honest about what's done vs stubbed, no rounding a
  half-extraction into "extracted".
- **Ground everything.** Doctrine here is extracted from real, decided practice
  (mostly `ros`) — never invented to fill a heading. If it can't be grounded
  yet, stub it and say so, per `create-repo`'s stub-don't-fabricate rule.
- **Report your problems with the doctrine — atelier is not exempt from its own
  rule.** If a house rule is wrong, unworkable, ambiguous, contradictory, stale,
  missing or unfindable, it goes on the board as an item with its evidence, the
  same way a child's finding arrives (`PROPAGATION.md` § *Pointing up*). Fixing
  the wording in passing is the thing this forbids: a defect quietly patched
  leaves no trace of what was wrong, so the class can't be counted and
  § *When a rule keeps breaking* has nothing to read. Being the home of the
  doctrine makes the report shorter, not optional. A report from a private
  repo is described by its class only: atelier is public and a push cannot be
  retracted, so the reporter never names itself or its contents (hosts,
  clients, secrets) on any surface the filing creates (branch, PR title,
  commit subject, PR body, item) — `PROPAGATION.md` § *The route*, rule 2.

## Autonomy in this repo

Full standing grant applies: commit + push + manage PRs at discretion
(`AUTONOMY.md`). The repo is **public, `mike548141/atelier`** (ADR 0005) — routine
pushes are granted, and a push is now publication, so the pre-commit scan hook
binds on every commit. The making-public floor is **spent** (ADR 0005 was the
confirmation). The live floor is the next deliberate *widening* — a public
announcement, a published package, a plugin/skills bundle — which stays Mike's
call, never the agent's initiative. And because the repo is public, the
closed personal-data list is load-bearing continuously, not just at publish.

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
