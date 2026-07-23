# 0007 — commit signing via SSH keys, fleet-wide; artifact signing deferred

**Status**: accepted (activation pending — see consequences) • **Date**: 2026-07-11

## Context

Mike asked (2026-07-11): "how do we sign all the code in the various repos".
The record is load-bearing — children pin atelier by SHA (ADR 0002), reviews
cite commits as evidence, and the repo is public (ADR 0005), so a push is
publication — yet a git identity is an assertion, not an authentication:
anyone can commit under any name with two config lines. The house constraints
that shaped the answer: the zero-dep tool ethos, the tool-install floor
(AUTONOMY), and enforce-by-machine (EVIDENCE §12).

## Decision

**Sign commits and tags fleet-wide with SSH keys natively** (`gpg.format ssh`,
git ≥ 2.34): a dedicated ed25519 signing key (distinct from the auth key),
machine-global config plus a `create-repo`-baked repo-local
`commit.gpgsign=true`, one canonical append-only `allowed_signers` file
tracked in atelier, and CI verification from each repo's adoption boundary
forward. History is never rewritten to sign it. **Release-artifact signing +
SBOM is deferred** with a stated trigger: the first real published artifact;
lightest route then is GitHub's native attestations. Doctrine:
`docs/method/SIGNING.md`.

## Rejected

- **GPG signing:** a keyring, a tool install, and key-management ceremony,
  for no capability SSH signing lacks in this estate. Breaches the zero-dep
  ethos for zero gain.
- **Sigstore/gitsign (keyless):** external tooling plus an OIDC dance on
  every commit; hits the tool-install floor; verification also needs the
  tooling, so children and CI inherit the dependency.
- **No signing:** leaves authorship spoofable in a public repo whose SHAs
  other repos pin as truth — the record's trust would rest on nothing but
  convention.
- **Artifact signing/SBOM now (the old A5):** nothing published exists to <!-- spellscan:allow: software-supply-chain term of art (cosign/syft artifact), not the general "produced thing" sense -->

  sign; standing up cosign/syft-class machinery ahead of a release is
  ceremony that breaks zero-dep for an empty benefit.

## Consequences

GitHub "Verified" on new commits; a floor step can verify signatures the way
the scanners verify content; the durable verification plane is the tracked
`allowed_signers`, not the badge (removing a key from GitHub un-verifies its
history there — the file keeps it verifiable locally forever). Costs,
accepted: pre-boundary history stays unsigned (append-only main, ADR 0002);
the badge plane depends on the key staying registered; key custody is
person-level and sits outside the cheap-burn store (SECRETS' honest
boundary). **Activation is gated on Mike registering a signing key — a new
trust surface on his identity infra, his act (AUTONOMY floor). The standard
is decided but dormant until then**; the doctrine's activation ladder names
the agent-executable steps that follow.

---

## Addendum (2026-07-12) — pre-activation review corrections, decision unchanged

The cold review (`docs/reviews/2026-07-12-signing-doctrine.md`,
PASS-WITH-FINDINGS) live-proved the core design and corrected two statements
above; recorded as an addendum per the decisions README no-edit rule:

- **Badge persistence inverted (G2).** "Removing a key from GitHub
  un-verifies its history there" is the reverse of current GitHub behaviour:
  verification is persistent and non-retroactive — removed keys leave their
  history marked Verified. The durable-plane conclusion stands on its real
  grounds: `allowed_signers` is self-hosted, versioned, and reviewed; the
  badge is GitHub-controlled and unauditable.
- **GPG rejection over-stated (G8).** "No capability SSH signing lacks in
  this estate" — the estate's own `main` already holds GitHub web-flow merge
  commits whose signatures *are* GPG, and GPG has revocation semantics SSH
  signing lacks. True strength: GPG offers no capability we need for signing
  *our own* commits; server-side commits are verified via GitHub's API plane
  (SIGNING.md's two-plane verification), not by adopting GPG.

Decision unchanged: SSH-native commit/tag signing fleet-wide; activation
still gated on the principal registering a key.
