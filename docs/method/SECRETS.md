# Secrets — designed to be cheaply burned

The counterpart to the two scans (`tools/leakscan.py`, `tools/secretscan.py`).
The scans are the *detect* half; this is the *make-rotation-cheap* half. Together
they turn an exposed secret from a disaster into a **rotate-immediately** event:
*detect → rotate → the burn cost is minutes*. `AUTONOMY.md`'s push floor rests on
this doctrine holding — it is why a secret near a commit is a bounded event and
not a catastrophe.

The design goal is not "never risk a secret". It is **"a burned secret costs
minutes"** — because the alternative, a hand-kept irreplaceable token, fails
closed the moment it leaks: you cannot rotate what you cannot re-mint.

## Reproducible / re-mintable — the enabling property

No secret in the estate is a hand-kept, irreplaceable artifact. Every secret can
be regenerated from something you still hold:

- **Internal secrets** (ones both sides of which you control) rotate
  **mechanically, at will**: regenerate → push both sides → converge. Rotation is
  a routine convergence, not an incident response.
- **External secrets** (issued by a third party — an ISP, a cloud tenancy, an API
  vendor) **re-mint from code behind a single approval**: the mint procedure is
  written down and repeatable; the one human approval is the external-action floor
  (`AUTONOMY.md`), not a bottleneck you'd avoid.

This is `RECORD`/`EVIDENCE`'s **store-the-rule-not-the-value** applied to
credentials (EVIDENCE §8): what's durable is the *procedure to mint*, not a
frozen token. A store built this way is itself reproducible — it rebuilds from
code, so it is not an exception to infrastructure-is-code.

## The credential triad — least, JIT, short-lived (the direction)

The target property of every credential, in priority order:

1. **Least-privilege** — scoped to exactly what it must do. The first and most
   achievable step; a scoped credential has a small blast radius when it burns.
2. **Just-in-time** — granted at the moment of use, not standing.
3. **Short-lived** — expires on its own, so an undetected exposure self-heals.

Most platforms don't offer JIT or short-lived grants, so **standing credentials
are the common honest reality** — and that's allowed, on one condition: a standing
credential is a **tracked debt to shorten, not a resting state**. It needs a
stated reason (usually "the platform offers no JIT grant"), and it stays on a list
of things to tighten. Silently treating a standing credential as the finished
state is the defect; naming it as a bridge is the discipline (see
`DATA-PROTECTION.md`'s stated-bridge rule).

## Right plane, never the wrong one

A secret's *value* lives in exactly one place: the encrypted secret store.
Everywhere else holds a **reference**, never the value.

- **Never in the config/inventory tree, never on the device in plaintext, never
  in a shareable-bound repo.** Config holds a named reference the tooling
  resolves; the resolved value never lands where it would be committed or served.
- **Encrypted at rest** even in the store (age/sops-class), so the store file can
  ride an ordinary backup or private remote without becoming the exposure.
- The scans enforce this mechanically (EVIDENCE §12: enforce by machine, not by
  good intention) — `secretscan` on the push path, `leakscan` for the structural
  and machine-local terms. A reference (`!secret …`, `${VAR}`, a `<placeholder>`)
  is *safe by construction* and the scans skip it; a bare value is the thing they
  exist to catch.

## Rotation cadence bounds the undetected window

Rotation is not only an incident response. Because internal rotation is cheap
(mechanical convergence), rotate on a **cadence** as well — so that *any* silent
exposure, breach or not, has a bounded life. The cadence is the control that makes
"we never detected a leak" survivable: the undetected-exposure window is at most
one rotation period, by design rather than by luck.

The full loop, then: **detect** (the scans) → **rotate immediately** on any
suspicion → and independently, **rotate on cadence** so undetected exposure
expires on its own. Each leg shrinks the window a different way.

## What lives elsewhere

This is the shareable doctrine. The concrete mechanism is instance-local:

- **The store technology and layout** (e.g. sops+age, per-org files, the
  `!secret` reference syntax), the specific standing credentials and their
  shortening-debts, and the mint procedures for each external secret — all stay in
  the instance repo's secrets doc and its `secrets/` tree, never here.
- **The estate credential map** (which credential guards what) is instance-local
  and, being sensitive topology, is itself protected under `DATA-PROTECTION.md`.
