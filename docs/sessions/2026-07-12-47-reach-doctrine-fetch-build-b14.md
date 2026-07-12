# 2026-07-12 · 47 — REACH doctrine, the fetch build, signing gate, B14 (Opus)

"Any work to do on atelier?" → a survey → Mike: **"proceed on all 4"** (fetch
→ doctrine, fetch → build, signing warn→block flip, B14 ros estate-access map),
"up to you on this session or separate ones." Orchestrated as parallel streams:
doctrine + signing assessment in the main line, three background agents (cold
review, worktree build, ros-scoped B14).

## Red main, fixed first (the session-46 regression)

`gh run list` at the top showed **atelier's own floor RED** on the session-46
commit — the doctrine repo failing its own gate. Cause: session 46 added the
**Concurrency** bullet to PROPAGATION.md's canonical child block but not the
stamped copy in `docs/build/templates/CLAUDE.md`; `test_stamped_block_matches_
canonical` caught the drift exactly as designed. Synced the template (canonical
wins) → green. Committed on its own before stacking anything (`templates:` —
green-before-content). The drift test earned its keep: a copy that drifts is a
second source, and this is precisely the class it exists to catch.

## Fetch ladder → doctrine: `method/REACH.md`

Elevated the two rules living operationally in `instruments/browser-fetch/
README.md` into portable doctrine. **Named REACH** for the instruments' third
verb — `tools/` enforce, observers observe, browser-fetch **extends reach**
(ADR 0006) — and the one-word capability-noun pattern of its neighbours
(SECRETS/ACCESS/STORAGE). Indexed after ACCESS in the SECRETS/ACCESS family.

Both halves in one doc, grounded not invented:
- **The escalation ladder** — engine-agnostic, cheapest-first (built-in → raw
  client → real-engine-disposable → operator-started-isolated → operator's
  live session → ask). The rungs climb isolation-traded-for-reach, crossing
  needing-the-operator at rung 4. The *built* Chrome instance stays in the
  instrument; the doctrine is the principle.
- **The credential boundary as a purpose-of-storage test** — provisioned
  stores (why-stored = for agent use) are the intended path; personal
  convenience stores (browser logins, the principal's password manager) off by
  default; ride a session, never mint from saved credentials; the principal
  grants across the line (floor-class, moves the credential into the
  provisioned machinery). Drawn as the reciprocal of SECRETS' own scope
  boundary — same personal vault, from the agent's side.

**Cold review** (background fresh-context agent, session-40/44 lifecycle,
barred from the person layer): **PASS-WITH-FINDINGS**, verdict in
`reviews/2026-07-12-reach.md`. All four sharp questions green — grounded ladder
(no invented rungs), the two-halves join *argued* on a real mechanism (same
event at rungs 4–5), the purpose test covers the estate's cases without
outlawing provisioned use, no person-level leak. **R1–R5 all [fixed] same day**,
one theme (adopter-clarity + one genuine seam): R1 definite "estate registry"/
"keychain" → indefinite; R2 the operator=principal identity the join leans on
now stated; R3 the seam between the purpose test and the categorical browser
rule closed (a browser store is never itself the provisioned path — ride, don't
mint, whichever profile); R4 the rung-4/5 one-mechanism caveat pulled up beside
the ladder; R5 the grant exception signalled at first statement.

## Fetch ladder → build: multi-engine + explicit 4/5 split

Background worktree agent built both open sub-items; taken as **files, not
merged** (its base predated this session's REACH review round, so a naive merge
would have reverted R1–R5 and deleted the review file — the diff-stat caught it).

- **Rung 3 multi-engine** — `browser_fetch` gains `engine` (chromium default /
  firefox / webkit), Playwright-bundled. **Firefox + WebKit live-verified this
  session**: each fetched example.com end-to-end through the actual
  `_launch_engine`/`_load_and_extract` path (200 + correct title/body) after
  `playwright install firefox webkit` (engine download, not a dep change). The
  live gate the agent honestly couldn't run — driven in the main line.
- **Explicit rung 4/5 split** — `rung` param (4 dedicated / 5 everyday) mapping
  to distinct ports (`:9222` / `:9223`) the operator binds per profile, with
  rung-specific unreachable errors. **Honest limit, not faked:** rungs 4/5 stay
  **Chrome-only by protocol** — CDP is Chrome's, `connect_over_cdp` speaks only
  it; Firefox/WebKit have no connect-to-running equivalent. Rung-4 proven on
  adoption (change is port-param, unit-covered); **rung-5 live fetch is
  owed-to-operator** by nature (needs the operator's everyday Chrome on `:9223`).

11 unit tests, floor 216 green, scanners clean. Agent worktree + branch put
away per CONCURRENCY (unique commit, but content incorporated — a kept branch
still taxes).

## Signing warn→block flip: assessed, HELD

Gate **not met, and the blocker is not main-line-agent-clearable** — recorded
rather than flipped (enforce-mode over a knowingly-red fleet would be
enforcement-theatre, against the apex). The three red repos fail for **three
different reasons, none a signing failure** (so the flip wouldn't newly-red
them): **homenetwork** — secretscan 25 findings (real secret debt, Mike's
rotation, session 39's owed list); **docker-heap** — secretscan full-cover
(same class); **rpi** — ruff (2) + a Windows test error in its **bespoke** CI,
**not the scanner floor and not signing** — session 41 mis-filed this as
"scanner debt"; it's ordinary code debt, agent-actionable, separate cleanup.
On docker-heap/homenetwork signscan never runs (secretscan fails first). The
"every active machine signs" half is also unverified. **Owed to Mike:** the two
secret rotations, and a yes/no on taking the rpi ruff/test cleanup.

## B14: ros consolidated estate access map

Background agent scoped **inside the private ros repo**; structure reported
back, sensitive topology never crossed into public atelier. Created
`docs/ACCESS-MAP.md` — a row per domain across ACCESS.md's four axes
(credential+store · plane split · rings walked · status/debt), seeded from ros's
own scattered facts (SPECS, inventory, secrets README), honest per-domain status
(one LIVE/mature, one STAGED, one PLANNED — nothing rounded to "onboarded").
Committed **signed** on isolated worktree branch `access/estate-access-map`
(`c3bc612`), **not pushed** — a concurrent session is live on ros's main (the
agent's worktree isolated it correctly). Merge + push is the follow-up once that
session settles; ACCESS.md's honest "not yet consolidated" status flips then.

## Net

Two of four fully closed (doctrine reviewed + shipped; build shipped +
live-verified), one created-pending-merge (B14, blocked only by a live ros
session), one assessed-and-held (signing, blocked on Mike). Plus a red main
fixed. Owed to Mike: the homenetwork/docker-heap secret rotations, the rpi
cleanup nod, the rung-5 operator live check, and the ros map's merge.
