# Session — C1: `advisory` takes a reason and an expiry (phase 1)

- **Date**: 2026-07-28 02:44 UTC
- **Worktree**: `ta-findings-application`, branch `worktree-c1-advisory-schema`
- **Subject**: Track C's C1, ruled by Mike 2026-07-28, plus A1 option (b) which
  had been deferred into C1 and was ruled alongside it.

## The rulings

| Question | Ruled |
|---|---|
| How strict is the new schema? | **Both `why` and `review-by` hard-required** |
| How does it reach the children? | **Transition window, then tighten** |
| What happens when the date passes? | **Board goes red, nothing blocks** |
| A1(b): must a narrowed boundary scope state why? | **Yes; reason only, no expiry** |

## Measured before costing

| Measure | Roadmap said | Measured |
|---|---|---|
| Advisory declarations | 11 | **17** |
| Children carrying them | 8 | **10** |
| Carrying a reason | 0 | 0 (no slot existed) |
| Oldest declaration | — | **2026-07-26**, two days |
| A1(b) reach | — | **1** (`ros` → `leakscan`) |

The migration is ~55% larger than the roadmap stated. That is the **fourth**
blast-radius figure this programme has had wrong, and the first that understated
the work rather than overstating it — the previous three all made a strong fix
look more expensive than it was. Worth noting as a pattern that runs in both
directions: the roadmap's numbers are not a reliable input to a ruling, and
measuring is cheap.

The counterweight: nothing has decayed yet. Every config was written
2026-07-26, so this lands in a clean window — C1 is preventive, not a cleanup.

## What the fix does

- `advisory` becomes `{name: {why, review-by}}`. Both required. The date is
  validated as a real ISO 8601 date at parse, which is what lets the ageing
  comparison downstream be a plain string compare. Unknown keys refused (the
  LS4 call). A bare reason with no date is refused with a message naming the
  missing half.
- An expired advisory renders 🔴 on the floor and on the board, with **how many
  days** it has been standing, and exits 0. Nothing blocks on a date.
- `scope` gains an object form `{paths, why}`. The `why` is required only for
  the five checks with no advisory form (A1(b)). No `review-by`: a narrowed
  scope is a permanent structural fact, not dated debt.
- `Config.__post_init__` normalises the shorthand shapes so every internal
  stage sees `Advisory`/`Scope` and never a union. The JSON loaders stay the
  strict door — a config file is a claim, a keyword argument is a shorthand.

## The transition, and why it exists

Children fetch `atelier@main` at CI run time. A hard error on the old spelling
would therefore break all 10 children's CI the afternoon it landed — a flag
day, not a rollout. The bare list still parses, marks itself `legacy`, and
renders 🟡 *"pre-C1 declaration, migrate it"* on every run and every board row.
**Phase 2 removes the spelling once the board is clean.** A transition, not a
dialect: if the legacy form is still parsing in a month, C1 has recreated the
decay it was written to end, one level up.

## Verification

- 747 Python tests (720 → 733 → 747 across the day's work), green.
- Six-case live probe of the advisory schema: legacy parses 🟡 rc=0; live date
  ⚠️ rc=0; expired 🔴 **rc=0**; reason-without-date, date-without-reason and
  malformed date each rc=1 with the specific remedy named.
- Five-case live probe of A1(b): boundary scanner without `why` rc=1; with
  `why` rc=0; legacy list rc=0; softenable scanner without `why` rc=0; unknown
  key rc=1.
- Board run against the real estate: all 17 declarations render 🟡 unmigrated,
  which is the intended transition state.

## Owed — the part not done here

**The 17 declarations are not migrated.** Writing them needs a `review-by`
date, and a date is a commitment about when the backlog gets cleared — that is
the principal's to set, not the applier's to invent, and inventing one across
ten of his repos would be fitting a number to make a board go green. The
migration also writes to ten repos outside atelier, several private, which is a
wider action than this session was pointed at.

Queued for Mike as one decision (the horizon), after which the migration is
mechanical. **Phase 2 — deleting the legacy spelling — is blocked on that
migration**, and the roadmap says so rather than implying C1 is finished.

Rule 4: this is self-authored doctrine and enforcement code, so a `⏳` is queued
in the landing commit. Not spawned by this session.
