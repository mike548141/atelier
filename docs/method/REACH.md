# Reach — getting past a block, and the line you won't cross to do it

When the clean path to a resource is blocked — a `403`, an anti-bot wall, a
login the agent doesn't hold — there is a *further* path, and there is a
**limit** on how far the agent may go to take it. This doc is both halves:
**escalate cheapest-first** (the ladder), and **never mint access from the
principal's saved credentials** without an explicit grant (the boundary). It is
the doctrine behind the
`instruments/` layer's third verb — `tools/` **enforce**, the observer
instruments **observe**, and **capability** instruments **extend what the
teammate can *do*** (ADR 0006 addendum); getting through a wall is the kind of
capability this doc governs, not the whole verb. The worked instance is
`instruments/browser-fetch/`; the rules here are generalised from that one
worked instance — engine-agnostic by construction, untested beyond it.

## Escalate cheapest-first — the ladder

Reaching the internet (or any walled resource) is a **ladder of methods,
cheapest at the top**. Rungs 1–2 cost the same and typically clear the same
walls — pick between them by **request shape** (a processed page vs raw bytes,
an API, exact headers), not by strength. From rung 3 down, every step costs
more of something — time, tokens, or the operator's attention — so descent is
**block-gated**: step down only when the current rung is actually blocked, and
never open at a lower rung because it's more likely to work; the cost you'd
skip is the cost that keeps the high rungs the default. **Blocked** means the
rung cannot return the resource in usable form — a hard error, a challenge
page, or demonstrably degraded or empty content (anti-bot walls usually fail
*soft*: a 200 with a JS shell counts, "might work better lower" does not).

The general shape, from cheapest:

1. **Built-in, processed** — the cleaned, known-URL fetch or the search that
   finds one. No process of your own, no operator.
2. **Raw client** — raw bytes when you need exact headers, an API, a file, or
   when the processing in rung 1 gets in the way. In the worked instance it
   shares rung 1's anti-bot profile (both a bare HTTP client), so it
   typically clears no new *walls* — it's a different *shape* of request,
   not a stronger one. (Where rung 1 is a provider-hosted fetch, the two
   profiles can differ in both directions — test, don't assume.)
3. **A real engine, disposable** — a standalone, fully isolated browser the
   agent drives itself. Beats a bare client at anti-bot walls because it *is* a
   real engine; shares nothing with the operator's browsing, so it can't be
   clicked away or break anything.
4. **A real engine the operator started, isolated** — non-headless (some walls
   key on headless specifically) but still a dedicated, everyday-browsing-free
   profile. Costs the operator an action to start it.
5. **The operator's own live session** — their real history and logged-in
   tabs, "just another tab as if they'd opened it". Only when the operator
   *deliberately* exposes it, and only when nothing weaker gets through.
6. **Ask the operator** — full manual fallback, when even their browser hits a
   wall only a human clears.

Across the engine rungs (3–5) the ladder trades one axis away — **isolation
for reach**: a disposable engine shares nothing with the operator, their live
session shares everything. Rungs 1–2 sit above that trade (typically equal
wall-clearing power, different request shape — no isolation given up). A
second axis crosses at rung 4: **needing the operator**. Rungs 1–3 the agent
walks alone; 4–6 cost the operator progressively more, which is the real
reason to exhaust the cheap rungs first. The escalation principle is general;
the *engines and tools* that fill the rungs are instance-local (see "What
lives elsewhere") — a
given instance may even serve rungs 4 and 5 with one mechanism, split only by
which profile the operator exposes, though the rungs stay distinct in principle.

Sibling ladder, opposite-sounding maxim, no conflict: `EVIDENCE.md` §13's
acquisition ladder says *climb* — spend more — as the stakes demand. The two
govern different choices: **reach picks the pipe** to a source, **evidence
picks the strength** of what must come back — and stakes can compel a fetch
that reach-economics alone would not.

Residual, named not solved: some walls are the **resource owner** saying no —
a paywall, a terms-of-service line, a rate limit. Whether to defeat a
deliberate wall *at all* is its own judgement with its own floor
(`AUTONOMY.md`'s people-safety and legality concerns, the target's terms);
the ladder governs **how** to escalate, never **whether** the target is fair
to take.

## The credential boundary — a purpose-of-storage test

Descending the ladder eventually rides the operator's real browser (rungs 4–5),
where saved logins live. The boundary that governs it generalises past
browsers: **which credential stores may the agent draw on at all?** The test is
*why the credential was stored*, not where it sits or how easy it is to reach.

- **Provisioned stores are the intended path.** Credentials saved *so that* a
  repo, tool, or agent can use them — a provisioning registry's entries,
  per-consumer minted API tokens, the whole `SECRETS.md` / `ACCESS.md`
  machinery. Agent use is the thing they exist for — in scope by design **for
  the use they were provisioned for, through the resolving machinery** (the
  tooling resolves references to values; the agent handling values directly is
  what `SECRETS.md`'s right-plane rule exists to avoid). The provisioning
  grant is the confirm *for that use*; directly reading, exporting, or
  repurposing a stored value stays on `AUTONOMY.md`'s always-confirm secrets
  floor.

- **Personal convenience stores are off-limits by default.** A browser
  profile's saved logins, the principal's password manager — saved over years
  to ease the *principal's own* use, never provisioned for the agent, and far
  broader than any task needs. The agent may **ride a session the principal
  has already authenticated** — existing cookies, a logged-in tab — **in
  place, driven through the ridden session**; reading or exporting session
  state (a cookie store, a token) is touching the store, on the secrets
  floor — a cookie *is* a minted bearer credential, and copying it out buys
  rung-5 reach with rung-3 isolation and no operator present. It
  may **never reach for the stored credentials that would mint a session**,
  nor the credentials themselves. **Riding an open session is fine; touching
  the credentials behind it is the line.** And riding licenses
  **retrieval** — the reach this doc exists for. Any state-changing act taken
  *through* a ridden session (sending, buying, deleting, granting) is its own
  action under the `AUTONOMY.md` floor, and a rung-5 ride is scoped to the
  exposure the operator deliberately made — never a standing grant: standing
  reach goes through the provisioned path (the grant below moves the
  credential there), never through a standing ride. A browser's
  saved-credential store is never itself the provisioned path — the two
  tests govern different things: *purpose* governs which **stores** the
  agent may draw on; *mint-vs-ride* governs which **acts** it may take
  through them, and a saved-login autofill is a mint whatever the store's
  purpose. Provisioned *browser* access means the operator authenticates and
  the agent rides the session, so ride-not-mint holds whichever profile it
  is — even a dedicated one stood up for the agent's use.

- **The principal can grant across the line** — per credential, temporary or
  permanent, as an explicit act. A grant is the principal's alone to make
  (`AUTONOMY.md`: the agent records a grant, never originates one; crossing this
  line is a trust-surface widening, floor-class). A **standing** grant *moves*
  the credential into the intended path: it enrols in the provisioned
  machinery (`SECRETS.md`'s store, `ACCESS.md`'s runbook). A **temporary**
  grant ("use this once") expires with the task — a one-shot credential never
  enrols and never persists; what is recorded is the *grant itself*, dated and
  scoped, never the value (`EVIDENCE.md`: store the rule, not a loose
  recollection of it).

The line runs where `SECRETS.md`'s own scope boundary runs — its person-level
credentials sit in the operator's personal vault, *outside* the estate's
operational doctrine. This test is the reciprocal from the agent's side: the
same personal vault the estate doctrine declines to cover is the store the agent
declines to draw on. Both halves keep the irreplaceable, personal credential set
untouched by the operational machine.

## Why the two halves are one doc

The ladder is how far the agent reaches; the boundary is the line reach must not
cross. They meet at rungs 4–5, where extending reach *is* riding the principal's
authenticated session — in the worked instance the operator running the browser
is the principal whose vault the boundary guards, so the guardrail and the
escalation are the same event seen twice. The two terms are distinct, and the
solo case is an assumption, not a rule: the **principal** is the deciding human
the agent serves (`00-APEX.md`); the **operator** is whoever runs the browser
being ridden. Where they differ — a team adoption, a colleague's rung-4/5
browser — the exposed session and vault are the *operator's own*: the ride is
scoped to what that operator deliberately exposed, and a grant across the line
belongs to **whoever owns the store**, never to the agent's principal by
default. A reader who has the ladder without the boundary would
descend it
into the saved-credential store; a reader who has the boundary without the
ladder would never learn there's a disciplined, cheapest-first way down at all.

## What lives elsewhere

This is the shareable doctrine. The concrete mechanism is instance-local:

- **The built ladder** — which engines and tools fill rungs 1–6, the exact
  tool names and their `status`/isolation behaviour, and the honest gaps —
  lives in `instruments/browser-fetch/README.md` and the ROADMAP, never here.
  The doctrine is engine-agnostic; the instance's coverage and its gaps are
  stated there, where they can change without falsifying a doctrine sentence.
- **The estate's provisioned stores and the grants across the line** — which
  keychain items and tokens exist, and which personal credentials the principal
  has moved into the intended path — are the `SECRETS.md` / `ACCESS.md`
  instance-local machinery (sensitive topology under `DATA-PROTECTION.md`),
  never here.
