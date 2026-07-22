# 2026-07-22 · 1005 UTC · Access-management doctrine — SECRETS.md expansion, review queued ⏳ (Fable, wt: secrets-access-mgmt)

## Trigger

Mike opened with "let's talk security, in particular access management — we
need to improve the doctrine to address all of this", followed by a set of
explicit rulings on credential etiquette, then three mid-turn widenings:
build in publicly available good practice (OWASP named), a pasted
secure-SDLC checklist, and the NCSC developers-collection link.

## Mike's rulings, now doctrine (delta `caa85fe`)

All decided in-conversation, 2026-07-22; grounded citations carry the date:

1. **Non-reuse across systems** — the same account on two devices carries two
   different secrets; per-system minting bounds a burn to one system. The
   *username* staying the same is a feature (audit correlation): identity is
   shared, the authenticator never — the identity/authenticator split.
2. **Non-reuse across entities** — two agents/tools/people never present the
   same credential; revocation independence (cut one off without touching the
   other) and clean attribution. "A shared credential is a shared fate."
3. **Privilege-split within one entity** — read-only + read-write credentials
   for the same holder where two genuinely distinct use cases exist (the
   `sudo` shape); the test is the use-case boundary, not tidiness.
4. **Asymmetric keys graded, not exempt** — one key across many systems is
   acceptable (the verifier holds only the public half; nothing it sees
   replays elsewhere) but not ideal: private-key exposure is fleet-wide blast
   radius, so hardware/passphrase backing, per-realm splits where cheap, and
   replaceability binding in full.
5. **Replaceability is absolute** — hesitation to roll is the tell that a
   credential has become irreplaceable debt; fix the coupling, never
   accommodate the fear.
6. **Minting** — machine-mint at the platform's maximum entropy; Kerckhoffs
   applied to credential *shape* (only the secret is secret — the format must
   be publishable at zero cost; a leaked example teaches nothing).
   Technology-imposed caps are the only allowed pattern, recorded as stated
   bridges beside the instance mint procedure.
7. **Exposure** — watch (standing duty: the scans, breached-credential
   screening, the store's own access trail) → roll on confidence, not proof
   (cheap burn makes the economics one-sided) → the roll automated and
   rehearsed, with cadence rotation doubling as the live rehearsal of the
   incident runbook.
8. **Never scrub history** — a rolled credential in an immutable store is
   dead text; rewriting published history costs integrity and buys nothing.
   The durable residue of a leak is *shape*, and ruling 6 prices shape at
   zero **by design rather than by luck**.

`ACCESS.md` step 2 gains one line: the onboarding credential is minted fresh
for the domain — never reused — because onboarding is exactly where reuse
tempts.

## Public-practice grounding (Mike's mid-turn widening)

Verified before citing: **NIST SP 800-63B rev 4 went final 2025-07-31** —
length-over-composition, breached-credential screening, and
change-on-evidence all corroborate the rulings above. **One divergence
owned in the doctrine text**: NIST drops *scheduled* expiry for
human-memorised passwords (forced rotation degrades what humans choose
next); that mechanism doesn't exist for machine-minted store-held secrets,
so the cadence stays for this doctrine's scope while NIST's rationale is
accepted for the class it addresses. The **OWASP Secrets Management Cheat
Sheet** corroborated store/rotation/least-privilege and contributed one
genuinely new leg: the tamper-resistant **audit trail on the store itself**,
absorbed as the watch leg's third surface.

The **NCSC developers collection** (8 principles) is SDLC-wide; its
credential-relevant principle (protect the code repository) is already
standing practice (ADR 0007 signing + the scanner floor). It and Mike's
pasted secure-SDLC checklist were **deliberately not crammed into this
delta** — captured on the ROADMAP as a doctrine-wide gap analysis with
already-held items named as corroboration and candidate gaps listed
(threat modelling, secure defaults beyond credentials, supply-chain vuln
screening, secure-coding floor, vulnerability tracking).

## Proofs

- Pre-commit scans green on the delta commit (secretscan, leakscan,
  linkscan); `sizescan --check` exit 0.
- No estate specifics entered the public doctrine — examples genericised
  (switches in a rack, agents/tools), per the no-personal-data boundary.

## Review

Self-authored doctrine ⇒ **rule 4: the review is queued `⏳` on the ROADMAP
for a non-author to take; this session spawned nothing.** The pointer names
the delta (`caa85fe`) and this record only — no evaluative account beyond
it.
