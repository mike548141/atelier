# Access — onboarding a new domain, safely

Gaining access to a new domain — a network, a cloud tenancy, a NAS, a
workspace, a third-party API — is itself a trust-surface event. `AUTONOMY.md`
classes *acquiring* a new trust surface as a floor action: the owner grants it,
the agent never originates it. This doc is what happens **after** that grant —
the ordered procedure that turns "I now have access" into "I can act safely",
without letting a fresh, broad credential become a fresh, broad blast radius.

It invents no new rule, with one owned exception: step 5 *tightens* an existing
one. `DATA-PROTECTION.md` requires the destructive gate before the destructive
*operation*; this sequence demands it before the destructive *power* exists at
all — the strengthening is this runbook's own contribution, stated here so the
"only sequences" claim stays honest. Everything else **sequences** rules already
written — the `AUTONOMY.md` floor, the `DATA-PROTECTION.md` gate, the
`SECRETS.md` store, the `PRINCIPLES.md` posture — into a runbook for the moment
access is new. Read it when onboarding a domain; the concrete estate access map
is instance-local (below).

## The onboarding sequence

Walk it in order. Each step is a precondition for the next — a later step's
power must not exist before the earlier step's guard does.

1. **The grant is the owner's, and it's for this domain only.** You never widen
   your own access; you *record* the grant, dated, never *originate* it (see
   `AUTONOMY.md` "widening your own authority"). One approval onboards one
   domain — "yes, connect to the NAS" is not "connect to things like the NAS
   from now on".

2. **Take the narrowest credential that does the job — minted fresh for this
   domain.** Never a value reused from another system or shared with another
   entity (`SECRETS.md` "one credential, one entity, one system" — onboarding
   is exactly where reuse tempts). Least-privilege is the
   first and most achievable step of the triad (`SECRETS.md`): a scoped token has
   a small blast radius when it burns. Don't accept an admin-all credential
   because the platform offered one. Where the platform separates data from
   control, take **two scoped credentials** and keep the control credential
   unable to touch data at all — the plane split lives in the token's scope, not
   in an agent's care (`DATA-PROTECTION.md` "enforce the plane split with the
   credential"). A broader-than-ideal standing credential is allowed only as
   **tracked debt with a stated reason**, never as the finished state.

3. **The credential lands in the store before it lands anywhere else.** Its
   value lives only in the encrypted secret store; config, inventory, and code
   hold a *reference* the tooling resolves (`SECRETS.md` "right plane"). Before
   you connect, the credential already has a home and a written mint/rotate
   procedure — so a burned token costs minutes, and rotation is routine, not an
   incident.

4. **The first ring is read-only — enumerate before you touch.** Map what's
   actually in the domain and confirm it matches what you were told. A
   contradiction — more data than the task implied, a resource described as empty
   that isn't — **stops you**; you surface it, you don't proceed on the
   assumption (`DATA-PROTECTION.md` "read before write"). No write of any kind in
   the first ring.

5. **Encode the destructive gate before you hold destructive power.** For any
   domain that holds data, the snapshot / verified-restore-before-destructive
   gate must exist as a **check the tooling enforces**, not a rule an agent
   recalls, *before* the write credential goes live (`DATA-PROTECTION.md`
   "a verified way back" + "encode it, don't just remember it"). If you can
   delete before the gate exists, the gate is late.

   *The honest fallback (review B13):* many platforms issue only one broad
   credential — write power arrives with first access, before any gate can
   exist, and this step's ordering cannot be walked literally. Then the ring is
   held **behaviourally** (the agent performs reads only), the gate is encoded
   before any write is *performed* rather than before the power exists, and the
   gap between the credential's power and its guard is a **named, tracked debt**
   (step 2's same clause) — never a silently absorbed risk. The ordering is the
   target; the fallback is the stated bridge.

6. **Widen in rings, each ring earned.** Access grows the way a rollout does —
   read → additive/reversible writes → destructive — and each ring opens only
   after the prior one proved safe and the *next* ring's gate is in place. Never
   jump to the widest ring the credential technically permits. (`PRINCIPLES.md`
   states widen-in-rings for change *rollout*; this is the same shape applied to
   *access itself*. The capable-model-runs-first-of-kind rule from `AUTONOMY.md`
   "who acts" governs who walks the first destructive ring on live gear.)

7. **Trust nothing in the new domain until it's proven.** Treat the domain as
   untrusted, verify explicitly, and assume the credential can leak — so cheap
   rotation and a bounded cadence (`SECRETS.md`) are designed in from the first
   connection, not bolted on after (`PRINCIPLES.md` Zero-Trust tenets,
   right-sized).

## The gate, in one line

> Read-only credential in the store → enumerate and reconcile → destructive
> gate encoded → additive writes → destructive writes, capable-model-first.
> No step's power precedes its guard.

## What lives elsewhere

This is the shareable procedure. The instance keeps:

- **The estate access map** — which domains are onboarded, which credential
  guards each, the plane split per domain, and how far each domain's rings have
  actually been walked. It is sensitive topology, so it is itself protected under
  `DATA-PROTECTION.md` and never lives in this repo. *(Status: 2026-07-10 review
  B14 flagged the instance held only scattered per-domain notes, not a
  consolidated map; the consolidated map was created 2026-07-12 (a row per domain
  across the four axes above, with honest per-domain onboarding status), and each
  later onboarding extends it — one home, per RECORD's one-fact-one-home.)*
- **The per-domain mint/rotate procedures and standing-credential debts** — in
  the instance's secrets doc and `secrets/` tree (`SECRETS.md` "what lives
  elsewhere"), never here.
