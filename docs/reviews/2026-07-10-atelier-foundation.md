# Fable review — atelier foundation & approach

**Status:** brief (ask on top). Verdict appended below the divider after the
review runs. Mike flagged this as the highest-value work in flight and
authorised generous Fable spend, so review deep, not fast.

## What atelier is (context for the reviewer)

atelier is the extracted, shareable *operating model* for how Mike and Claude
work — the doctrine that made `ros`/`tiki` good to build in, lifted above any
single repo so every project inherits it and peers can adopt it. Two layers:
`docs/method/` (how we work — shareable) and `docs/build/` (how we build — repo
craft). Born 2026-07-10; `method/` first slice is written, `build/` +
extractions are pending. Read the repo (`README.md`, `docs/method/*`,
`docs/ROADMAP.md`) before reviewing.

## Scope — three lenses, review all three

1. **Approach & assumptions** (the most important lens — is this the right
   problem, solved the right way?).
2. **Doctrine quality & honesty** (are the written docs sound, consistent, and
   free of overclaim — is a stub honestly a stub?).
3. **Completeness / harvest** (what doctrine already lives in the repos that
   atelier has NOT captured?).

## Load-bearing assumptions to challenge

Attack these; if any is false, atelier is mis-built:

1. **The good stuff is extractable.** That the thing which makes ros good is
   *writable doctrine* that transfers by being read — not tacit skill that a
   document can't carry. If most of the value is tacit, atelier is theatre.
2. **Layered inheritance is the right model** for *working method*
   (machine→house→project→session), the same shape tiki uses for config. Or is
   working-method the wrong thing to model as config-inheritance?
3. **A separate repo is the right home** — vs keeping doctrine in ros, or in
   `~/.claude`. Does extraction create a second source of truth that will
   diverge (the exact DRY sin the principles forbid)?
4. **Propagation is solvable simply.** The hard open problem (see below). Is
   there a KISS mechanism, or does "keep every repo current with the house
   doctrine" inherently require heavyweight machinery?
5. **The shareable/personal split is cleanly separable** — that no piece of
   genuinely useful doctrine is so entangled with personal/estate context that
   it can't be shared without leaking. Test the boundary.
6. **Broad autonomy is safe.** commit+push+PR granted for all work, with the
   stated floor (private→public, destructive, secrets, spend, people/safety,
   unapproved-tool install). Is the floor complete? Any recoverable-looking
   action that is actually catastrophic and slips through?

## The propagation problem (design critique wanted)

Mike: *"How do we learn this lesson once — keep all repos/sessions up to date as
the house doctrine changes? Child repos like faves need to feed off the house
doctrine repo."* Weigh the candidate shapes and recommend one (or a better
one):

- **Reference** — each child `CLAUDE.md` points at atelier ("doctrine lives
  there, read it"). One source, but requires the child session to actually go
  read it, and offline/other-device access matters (see north-star).
- **Vendored copy + drift-check** — child carries a copy; a check flags when it
  lags atelier. No divergence-by-neglect, but two copies.
- **Session-start pull/hook** — a hook refreshes doctrine at session start.
  Events-over-polling? Fail-safe if atelier is unreachable?

Judge against the principles (DRY, one source of truth, legibility/observable
staleness, graceful degradation when atelier is unreachable, KISS).

## New threads to risk-check

- **Portable personal context** — Mike wants `~/.claude` personal context to
  travel with *him* across devices (iPhone/Mac/successors), while never entering
  a shared repo. Where should that store live? Security/privacy of syncing
  personal+health+financial context across devices.
- **Session archive** — archive every session (chat/cowork/CLI/VS Code) as
  detail-on-demand. Worth the storage + privacy handling, or is the SESSIONS.md
  index enough? Retention/scrub concerns.
- **Repo-boundary guidance** — the rule for standalone repo vs component of an
  existing one (e.g. rich EPL client work). What's the decision framework?

## Real-world check (the honest test)

The true proof is behavioural, not textual: (a) would a *new* repo scaffolded to
inherit atelier actually behave per the doctrine in a fresh session, and (b)
could `faves` genuinely "feed off" atelier today? If the answer needs machinery
that doesn't exist yet, say so plainly — don't grade the docs as if they were
the mechanism.

---

<!-- Fable verdict appended below this line -->
