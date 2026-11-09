# Secrets — designed to be cheaply burned

The counterpart to the two scans (`tools/leakscan.py`, `tools/secretscan.py`).
The scans are the *detect* half; this is the *make-rotation-cheap* half. Together
they turn an exposed secret from a disaster into a **rotate-immediately** event:
*detect → rotate → the burn cost is minutes*. `AUTONOMY.md`'s push floor rests on
this doctrine holding — it is why a secret near a commit is a bounded event and
not a catastrophe.

The design goal is not "never risk a secret". It is **"a burned secret costs
minutes"** — because the alternative, a hand-kept irreplaceable token, fails
closed the moment it leaks: you cannot rotate what you cannot re-mint. This is
the rotation case of the posture principle — engineer for the failure being
cheap, not impossible — whose canonical statement is
[`PRINCIPLES.md`](PRINCIPLES.md) §10; this doc carries the case, not the rule.

## Reproducible / re-mintable — the enabling property

No *operational* secret in the estate is a hand-kept, irreplaceable artefact
(the honest boundary below names the two edges of that claim). Every secret can
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

Replaceability is **absolute, and hesitation is the tell** (Mike, 2026-07-22):
there must never be a credential whose roll anyone fears might break a service
or the network. The moment someone hesitates to rotate — "what depends on
this?" — the credential has silently become irreplaceable debt. Fix the
coupling that causes the fear; never accommodate the fear by not rolling.

**The honest boundary (2026-07-10, review B12).** Two edges of the claim, named
so a clean-sounding doctrine doesn't over-promise:

- **The store's own master key** (the age/KMS-class key that unlocks the store)
  is re-mintable for *exposure* — regenerate and re-encrypt, minutes, like any
  internal secret — but its *loss* is a different failure: you cannot re-mint
  your way back into a store you can no longer read. Loss is guarded by
  **redundancy** (an out-of-band backup of the key, or a second resolution
  plane holding the same values), and that backup is a named obligation, not an
  optional nicety. One hand-kept artefact class survives the doctrine, and this
  is it — kept survivable by copies, not by minting.
- **Scope: system and infrastructure credentials.** Person-level credentials —
  account recovery keys, identity seeds, the master key's own backup — are
  deliberately *outside* this doctrine, in the operator's personal vault, and
  some are genuinely not re-mintable from code. The doctrine doesn't pretend to
  cover them; it keeps the estate's *operational* secrets cheap to burn so the
  irreplaceable set stays as small as the identity layer itself
  (`DATA-PROTECTION.md`'s smallest-irreplaceable-set, applied to credentials).

## The credential triad — least, JIT, short-lived (the direction)

The target property of every credential, in priority order:

1. **Least-privilege** — scoped to exactly what it must do. The first and most
   achievable step; a scoped credential has a small blast radius when it burns.
2. **Just-in-time** — granted at the moment of use, not standing.
3. **Short-lived** — expires on its own, so an undetected exposure self-heals.

Most platforms don't offer JIT or short-lived grants, so **standing credentials
are the common honest reality** — and that's allowed, on one condition: a
standing credential is a **tracked debt to shorten, not a resting state**
(`PRINCIPLES.md` §5, *Honest pattern*, states the rule). It needs a stated
reason (usually "the platform offers no JIT grant"), and it stays on a list of
things to tighten. Silently treating a standing credential as the finished
state is the defect; naming it as a bridge is the discipline (`PRINCIPLES.md`
§7, "a hand-action is only a stated bridge").

**The next rung: no credential at rest.** Where the platform offers neither JIT
nor short-lived grants and the credential is used irregularly or rarely, a
tracked debt is not the only honest answer. In Mike's words, captured
2026-08-03: *"delete the credential entirely and make its rebuild cheap,
automated and tested"*. The credential is minted for the run and deleted after,
so between uses it does not exist. What stays durable is the procedure to mint,
which is the enabling property above taken to its end. The rung sits below the
triad, because a platform's JIT or short-lived grant is better where one is
offered, and above a standing credential, because the holder then achieves what
the vendor does not grant.

**This is a one-case claim.** One child repo's backup tool, on a platform whose
delegation grant is standing-only, deletes the credential after each run and
rebuilds it by a tested, automated path. The case grounds the shape; the limits
that follow are reasoned from it. An untested rebuild trades a
standing-credential risk for an outage risk, so *tested* is a condition of the
rung. The rebuild path itself authenticates with something: deleting the leaf
is progress, the minting credential still stands and stays a tracked debt, and
the rotation cadence below then bounds that credential, since a deleted one has
no exposure window left to bound. How often an idle rebuild must be rehearsed,
and how rare is rare enough before mint-per-use is simply JIT, are open until a
second instance.

## One credential, one entity, one system — the non-reuse rules

Non-reuse has two axes, and both are load-bearing (Mike's rulings, 2026-07-22):

- **Across systems: one system, one value.** The same account on two devices
  carries two different secrets — a service account present on every switch in
  a rack is minted a fresh password per switch. Reuse couples the fleet: a
  copied value opens every system it was copied to, so the blast radius of a
  burn is exactly one system only if the value lives on exactly one system.
  Where the platform supports central auth (the RADIUS/TACACS class), the
  stronger resolution is eliminating device-local secrets entirely — the
  secure-defaults ladder ("Grounding" below) applied to this rule (SA8,
  2026-07-23).
- **Across entities: one credential, one holder.** Two agents, tools, or people
  never present the same credential — not even to the same system. The reason
  is **revocation independence**: either holder can be cut off without touching
  the other, and an audit line attributes an action to one actor, not a pool.
  A shared credential is a shared fate.

The **identity/authenticator split** makes the first rule cheap to live with:
a *username* is identity, and sharing it across systems is a feature — the same
name lines audit trails up across the fleet. Only the *authenticator* (the
secret) must differ. Correlate by name, never by value.

Within one entity, the split runs the other way: **one holder may carry several
credentials, separated by privilege**, where two genuinely distinct use cases
exist — a read-only credential for routine observation and a read-write one
taken up only for the change (the `sudo` shape: stand low, elevate
deliberately). The test is the use-case boundary, not tidiness — don't multiply
credentials that would only ever be used together. This is the triad's
least-privilege leg applied *within* an entity, and it composes with the
plane-split-in-the-credential rule (`ACCESS.md` step 2).

## Asymmetric keys — stronger, so graded; not exempt

The per-system rule above is calibrated to symmetric secrets, where every
system that *verifies* the value also *holds* it — each copy is a place it can
leak. A keypair breaks that symmetry: the target holds only the public half,
and nothing it *stores* can be replayed against another system — at rest, a
compromised target gains nothing toward the fleet. So the
rule grades rather than transfers: **one key across many systems is
acceptable** (Mike, 2026-07-22) — the leaky-verifier case that forces
per-system passwords doesn't exist here. The live *session* is a different
channel (SA1, 2026-07-23): a delegated-credential mechanism like SSH agent
forwarding lets a compromised middle host authenticate onward to everything
the key opens without ever holding it — so **no delegated use of the key
through systems you don't control** (no agent forwarding through untrusted
hosts), and take presence-confirmation (touch-to-sign) where hardware
backing offers it.

Acceptable is not ideal. The private key is now a single point whose exposure
is a fleet-wide blast radius, so the residual duties concentrate on it: keep it
where it can't travel (hardware-backed, or at least passphrase-wrapped at
rest), split keys per security realm where that's cheap — and above all keep
the roll cheap. Replaceability binds keys exactly as it binds passwords, and a
key so widely deployed that rolling it is frightening has silently become the
irreplaceable artefact this doctrine exists to prevent.

## Minting — a leaked value must teach nothing

Secrets are **machine-minted at the maximum entropy the technology accepts** —
never hand-composed, never derived from a house scheme. The bar is Kerckhoffs'
principle applied to credential *shape*: only the secret is secret, so the
minting format must be publishable at zero cost. A leaked example teaches an
attacker nothing about the next value — no prefix convention, no
word-digit-symbol template, no *chosen* length. The bar is **entropy, not
length-worship** (SA3, 2026-07-23): take the platform's maximum up to entropy
sufficiency — past ~128 bits of randomness, added length buys no security —
and where a verifier silently truncates (the bcrypt-class 72-byte cutoff),
the *effective* length is the verifier's cap and is recorded as such beside
that platform's mint procedure, so the store never misstates what actually
authenticates.
(Public practice agrees: NIST SP 800-63B rejects composition rules in favour of
length and randomness — see "Grounding" below.)

The one pattern allowed is the one the technology imposes: a platform that caps
passwords at 30 characters makes "all its passwords fit in 30 characters" a
visible pattern, but an *imposed* one — take the maximum the platform permits
and record the constraint beside that platform's mint procedure
(instance-local, "what lives elsewhere"). An imposed cap is a stated bridge
(`PRINCIPLES.md` §7, "a hand-action is only a stated bridge"), never a licence
for schemes below the cap.

**The break-glass class** (SA4, 2026-07-23). Credentials a human must
transcribe by hand during an outage, when the store itself may be unreachable
— the out-of-band console login, the serial-line password mid-incident, the
hypervisor root while the store's host is down — are a use-imposed constraint
the paragraph above doesn't cover: a max-length random string is hostile to
the recovery path exactly when it matters. The class stays machine-minted and
schemeless, but may be minted **transcription-optimised** (a generated
word-sequence passphrase): the constraint is recorded as a stated bridge
(`PRINCIPLES.md` §7) beside that platform's mint procedure, instance-local,
like any imposed cap.
What it never licenses is a human "memorable" scheme — the temptation this
class exists to name is the one the minting bar exists to kill.

**What these permanent bridges rest on** (`160/570` BR2). The imposed cap and
the break-glass class are not the shapes `PRINCIPLES.md` §7 licenses (a bridge
*temporary pending codification*, or permanent because codifying is *unsafe*):
nothing awaits codification and nothing is unsafe to codify; they last until the
platform changes. What holds them is the credential rule in `PRINCIPLES.md` §5
(*Honest pattern*, and Zero Trust's *name the gap*): a stated reason, on a list,
kept tightening, weighed again at technology choice. §7 supplies the grammar's
name, "stated bridge", and no more.

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

## The boundary's posture — over-flag, because detection enables everything

The two scans answer to one stated intent (Mike, 2026-07-28): **find every
secret, credential, private key and piece of personal data, so none of it
reaches a public or insecure place.** That is the bar they are judged against —
not a low false-positive count, and not a quiet log.

**Over-flagging is the fail-safe direction.** A false positive costs an
allow-marker carrying a written reason; a false negative costs a leak. The two
costs are not comparable, so where a tuning call is genuinely uncertain, the
scan flags. This was already `leakscan`'s posture, stated in its own source; it
is now **both** scans' posture by decision. The decision was needed because the
two had drifted into opposite tunings with nothing recording the difference —
the personal-data scan tuned to over-flag, the credential scan tuned for
precision with no posture stated at all. That is backwards on risk, and nobody
chose it; it accumulated. It is written here as found-and-decided so the next
hand inherits a posture rather than a docstring.

**Rotation presupposes detection.** Every duty below — watch, roll on
confidence, rotate on cadence — is dischargeable only against what the boundary
actually catches. *Detect → rotate → the burn cost is minutes* has no first
term if the detector was tuned to stay quiet, and the cadence leg bounds the
undetected window only for exposures something is capable of noticing.
Detection is the enabling half of this doctrine, which is why its posture is
stated here and not left to the tools. This, and not any
credential-versus-personal-data risk ranking, is what the posture rests on: the
ranking is contestable — a credential re-mints, a published address never does
— and the posture holds whichever way that argument lands.

**Narrowing coverage is the principal's decision.** Keeping detection
deliberately narrower than the stated intent changes what the boundary
promises, so it is the call of whoever owns the risk, recorded where they will
meet it — the roadmap or an ADR. Settling it at tool altitude, as a comment
beside the pattern that does the narrowing, is how a gap becomes invisible:
it happened here in the credential scan, and it took a review to find. Name the
narrowing and its cost in prose; never let the code comment be the record.

**The dial that makes the intent affordable — decided 2026-07-28, built
2026-08-07.** While a scan's only response is *block*, widening detection buys
coverage at the price of crying wolf, and that price is what drove the
narrowing above. The decided
direction (2026-07-28) is an advisory tier in the credential scan:
high-confidence hits block exactly as they do today — **the blocking set never
shrinks** — while context-free entropy hits report and exit clean, so coverage
can widen into the noisy path without weakening the gate. It was held until its
design named where advisory findings surface durably and whether they must be
acknowledged (2026-07-29): an advisory finding nobody reads is cover, not
coverage. It was built once that consumer was named (`dcb57fa`, 2026-08-07;
corrected here 2026-11-03, `115/370`, after this lead had still said "not yet
built" for three months). `leakscan` gains no advisory form for
anything that blocks, and that asymmetry is decided rather than incidental —
the fit being that a leak of personal data is the one exposure no rotation
undoes.

**One dated exception, decided 2026-10-18 (G3, `020/150`).** `leakscan` gates
tracked binary media (an image's metadata can name its owner and place), and
its four gate rules (`binary-unlisted`, `binary-changed`, `binary-metadata`,
`binary-stale-entry`) warn without blocking until `BINARY_GRACE_UNTIL`,
**2026-11-18**, and block from that day. Mike chose the option labelled
"Grace period (Recommended)" so no child went red on the day G3 landed; he made
the date firm for every child on 2026-11-08. It covers those four rules and
nothing else, and the code removes it after the date (`010/190`). So the
asymmetry above holds for every rule that blocks, with this one self-expiring
exception recorded here; the statements of it in `tools/README.md`, the
`leakscan.py` source comment and `CHANGELOG.md` are copies of this one.

**Narrowed 2026-10-16: in `leakscan`, rules that are off report without
blocking.** A rule withdrawn from the blocking set for noise, and a rule a repo
turns off with `--disable`, used to see nothing at all. Each now still runs:
its hits are listed and counted on every run, the floor board carries the
count, and none of them moves the exit code. Nothing that blocks stops
blocking, and a test pins that, so the blocking set cannot shrink. The
asymmetry above still holds for every rule that blocks; what changes is that a
rule that is off is no longer blind. This is Mike's answer of 2026-10-16
("Report-only for off rules"), given after he was re-briefed on the EI6
ruling of 2026-07-29 that it narrows, and it lifts that ruling for this case
only. The same question offered demoting noisy rules that block today, which
would shrink the blocking set, and he did not choose it.

Grounding: [`../ROADMAP.md`](../ROADMAP.md) § *Track E — E6*, ruled by Mike
2026-07-28, and the intent cold pass
[`../reviews/2026-07-29-1243-e6-intent-cold.md`](../reviews/2026-07-29-1243-e6-intent-cold.md)
(EI5, EI6), ruled 2026-07-29. The narrowing: roadmap `115/090`
([`../roadmap/115-guardrail-architecture-mike-commissioned/090-give-every-guard-a-second-dial-mike-s-2026-07.md`](../roadmap/115-guardrail-architecture-mike-commissioned/090-give-every-guard-a-second-dial-mike-s-2026-07.md)),
answered 2026-10-16, and its design note
[`../../tools/leakscan.off-rules.design.md`](../../tools/leakscan.off-rules.design.md).

## Rotation cadence bounds the undetected window

Rotation is not only an incident response. Because internal rotation is cheap
(mechanical convergence), rotate on a **cadence** as well — so that *any* silent
exposure, breach or not, has a bounded life. The cadence is the control that makes
"we never detected a leak" survivable: the undetected-exposure window is at most
one rotation period, by design rather than by luck.

The full loop's wording lives in **Exposure** below (watch → roll on
confidence → rehearsed roll — one home, so the two sections can't drift;
SA7, 2026-07-23); what this section adds is the independent third leg:
**rotate on cadence**, so undetected exposure expires on its own. Each leg
shrinks the window a different way.

## Exposure — watch, roll, never scrub

Three duties, in order (Mike's rulings, 2026-07-22):

- **Watch.** Exposure monitoring is a standing duty, not a commit-time event.
  The scans hold the paths we control (the push path, the machine-local tree);
  beyond them, watch the surfaces where a credential could surface without us
  publishing it — breached-credential screening where a platform offers it,
  provider breach notices, and the secret store's own access trail (who
  resolved which secret, when — OWASP's audit leg; a store that can't account
  for its reads can't tell you a secret was taken) **where the store can
  provide one** — a file-based store (the sops+age class, this doctrine's own
  exemplar) decrypts offline and has no read trail to offer, and that gap is
  a named limitation (`PRINCIPLES.md` §7, "a hand-action is only a stated
  bridge"; §5, *name the gap*) weighed when
  choosing store technology, never a duty silently skipped (SA2, 2026-07-23).
  Detection you don't do is
  rotation you never trigger.
- **Roll on confidence, not proof.** The trigger is *credible risk* of
  exposure, never confirmed exposure — the burn costs minutes by design, so
  the economics always favour rolling. Waiting for proof buys nothing and
  spends the window.
- **The roll is automated and rehearsed.** An exposure response that exists
  only as prose is a hope, not a process — the same shape as
  `DATA-PROTECTION.md`'s a-backup-isn't-a-backup-until-a-restore-is-verified,
  applied to rotation. Here the cadence earns a second keep: every scheduled
  roll is a live rehearsal of the exposure runbook, so the incident roll is a
  motion already proven routine, executed sooner.

And **never scrub history.** A rolled credential sitting in an immutable store
— git history, a transcript archive — is dead text: it opens nothing.
Rewriting published history to white-wash it costs real integrity (clones
diverge, signatures break, the record stops being trustworthy) and buys
nothing the roll didn't already buy. The one durable residue of a leak is
*shape* — what our secrets look like — and the minting bar above prices that
at zero by design rather than by luck. Roll it, and leave the corpse where it
lies. Two scope lines, so the absolute isn't quoted past its own body (SA6,
2026-07-23): the rule binds **published** history of **rolled credentials** —
amending a secret out of a not-yet-pushed local commit costs nothing and is
routine hygiene, not a scrub; and residue no roll can kill (personal data; a
key whose captured past traffic lacks forward secrecy) is not "dead text" —
that class is `DATA-PROTECTION.md`'s problem, handled there.

**On the output side, a field allowlist is only as strong as the kept values'
types.** A session reading a provider API that allowlists the fields it keeps
before printing treats any non-scalar value under a kept field as
un-allowlisted: drop it, or recurse the allowlist into it, and never print it
whole. A kept field holding an object is an unfiltered surface wearing an
allowlisted name. Grounding: a child's read of a certificate listing kept a
field whose value had always been a scalar label; for objects signed by the
provider's own internal CA, that field carried the whole issuing-CA object,
private key included, and the allowlist passed it into the session transcript
(handed up 2026-08-22, `320/090`).

## Grounding in public practice

The rules above are Mike's decided practice, but they are also deliberately
checked against published doctrine — corroboration named, divergence owned:

- **[NIST SP 800-63B rev 4](https://pages.nist.gov/800-63-4/)** (final
  2025-07-31): length-and-randomness over composition rules corroborates the
  minting bar; its screen-against-breached-lists duty is the watch leg's
  mechanism *at mint time* (NIST mandates the check when a secret is set —
  the *standing* screening the watch leg names is platform practice, not an
  800-63B mandate; SA5, 2026-07-23); and
  *change on evidence of compromise, not on a calendar* corroborates
  roll-on-confidence. **One owned divergence:** NIST drops *scheduled*
  expiry for human-memorised passwords because forced rotation degrades what
  humans choose next. That mechanism doesn't exist for machine-minted,
  store-held secrets — no human memorises them, so rotation costs nothing and
  degrades nothing — which is why the cadence stays for this doctrine's scope
  (system and infrastructure credentials) while the NIST rationale is accepted
  in full for the human-password class it addresses.
- **[OWASP Secrets Management Cheat
  Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html)**:
  a centralised store holding values with everything else holding references,
  automated rotation, and fine-grained least privilege corroborate the store
  rule, the cheap-burn goal, and the triad. Its **tamper-resistant audit
  trail** (who requested/used a secret, when, and whether expired ones were
  re-tried) is absorbed above as the watch leg's third surface.
- **Secure defaults** (CIS-class guidance): where a platform offers a stronger
  authenticator class — MFA on a human account, keys over passwords, scoped
  tokens over account passwords — take it by default; deny-by-default on
  access. The weaker class needs the stated reason, not the stronger one.

Public practice wider than credentials — threat modelling, supply-chain
checks, secure-coding floors — belongs to a doctrine-wide gap analysis, not
this file (tracked in `ROADMAP.md`).

## What lives elsewhere

This is the shareable doctrine. The concrete mechanism is instance-local:

- **The store technology and layout** (e.g. sops+age, per-org files, the
  `!secret` reference syntax), the specific standing credentials and their
  shortening-debts, the mint procedures for each external secret, and each
  platform's imposed constraints (length caps and the like, per the minting
  rule) — all stay in the instance repo's secrets doc and its `secrets/` tree,
  never here.
- **The estate credential map** (which credential guards what) is instance-local
  and, being sensitive topology, is itself protected under `DATA-PROTECTION.md`.
