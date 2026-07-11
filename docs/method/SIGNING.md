# Signing — provenance for a record worth trusting

*Commits are the record, and the record is load-bearing: children pin atelier
by SHA (ADR 0002), reviews cite commits as evidence, and the repo is public —
a push is publication. But a git identity is an **assertion, not an
authentication**: anyone can commit as anyone with two `git config` lines.
Signing closes that gap mechanically (EVIDENCE §12 — enforce by machine, not
by good intention). Standard decided 2026-07-11 (ADR 0007); **not yet active**
— see the activation ladder below. Written before activation deliberately, so
the wiring lands against a stated standard rather than ad-hoc choices.*

## What a signature honestly claims (read this first)

A signed commit proves: **made with custody of this private key, on a machine
holding it**. It does not prove the principal personally typed the change —
in this house most commits are agent-authored under the owner's git identity,
and the same machine key signs them. That is not a loophole; it is the claim.
Authorship nuance is already carried honestly by the `Co-Authored-By` trailer
(RECORD); the signature adds *custody and tamper-evidence*: this commit came
from a trusted machine and has not been altered since. Stating the claim at
its true strength is the apex applied to cryptography — a signature sold as
"the human wrote this" would be an over-claim.

## Two layers, deliberately split by cost

### Layer 1 — commit/tag signing (the standard: adopt fleet-wide)

Git signs with **SSH keys natively** (`gpg.format ssh`, git ≥ 2.34). No GPG
keyring, no external tooling, nothing breaching the tool-install floor — the
zero-dep house ethos answer. The shape:

- **A dedicated ed25519 signing key**, distinct from the auth key.
  Least-privilege (SECRETS' triad): auth and signing then burn independently —
  a compromised auth key doesn't invalidate the signature trust plane, and
  either can be revoked without touching the other. (GitHub permits reusing
  one key for both; the coupling of blast radii is why we don't.)
- **Machine-level config is the mechanism** — signing is a property of the
  machine + key, not of any one repo:

  ```
  git config --global gpg.format ssh
  git config --global user.signingkey <path-to-signing-key>.pub
  git config --global commit.gpgsign true
  git config --global tag.gpgsign true
  git config --global gpg.ssh.allowedSignersFile <path-to-allowed_signers>
  ```

  `create-repo` additionally bakes `commit.gpgsign=true` repo-locally —
  belt-and-braces so a new repo signs even where global config has drifted.
- **One canonical `allowed_signers` file, tracked in atelier** (repo root).
  Public keys are public — safe in a public repo — and one-fact-one-home
  (EVIDENCE §9) says the trust list has exactly one source: machines point
  their git config at it; child CI fetches it alongside atelier's tools.
  Entries carry `valid-after` (and `valid-before` on retirement); the file is
  **append-only** — a retired key is bounded, never deleted, so old
  signatures stay verifiable forever.
- **GitHub's "Verified" badge is the convenience plane, not the durable one.**
  It requires the public key uploaded to the account as a *signing* key, and
  it lasts only while the key stays registered — remove the key and history
  shows unverified again. The `allowed_signers` file + `git verify-commit`
  is the verification that survives; the badge is UI sugar on top.

### Layer 2 — release-artifact signing + SBOM (deferred, stated trigger)

Signing *built artifacts* and emitting an SBOM needs external tooling
(cosign/syft-class), which hits the tool-install floor and breaks the
zero-dep house-tool pattern — a deliberate design call, not an oversight.
**Trigger to revisit:** the first real *release* — a published package or
binary that someone else installs. Lightest route if triggered: GitHub's
native artifact attestations (no local tooling). Until an artifact exists,
there is nothing to sign, and standing up the machinery would be ceremony.

## Verification — signing without checking is ceremony

The same read-≠-complied logic as PROPAGATION: a signature nobody verifies
enforces nothing. Two verification planes:

- **Local:** `git log --show-signature` / `git verify-commit <ref>`, resolved
  against the canonical `allowed_signers`.
- **CI:** a `floor.yml` / `ci.yml` step verifies signatures the same way the
  scanners verify content — over commits **after the adoption boundary** (see
  below), pointing `gpg.ssh.allowedSignersFile` at the tracked file.

## The adoption boundary — unsigned history is a fact, not a defect

History is **never rewritten to sign it**: atelier's `main` is append-only,
and a force-push would orphan every child's pin (ADR 0002). Each repo's
boundary is simply its first signed commit; verification gates from there
forward. Pre-boundary unsigned history is stated plainly and left alone —
retro-signing would trade the whole propagation mechanism for a badge.

## Key handling — where SECRETS' boundary falls

The signing key is **identity-layer, person-level**: per SECRETS' scope
boundary it lives in the operator's personal vault and custody, outside the
estate's cheap-burn store. Its failure modes are both mild — the reason this
layer is cheap to run:

- **Exposure** — remove the key from GitHub, mint a replacement, append the
  new entry to `allowed_signers` and bound the old with `valid-before`.
  Pre-revocation signatures stay verifiable; the badge plane heals on upload.
- **Loss** — mint and register a new key; nothing becomes unreadable, and
  local verification of old commits is untouched (`allowed_signers` still
  holds the retired public key). Unlike the store master key, a lost signing
  key costs minutes, not access.

## Activation ladder (status: step 1 pending — the standard is dormant until it moves)

1. **Principal registers a signing key** — generate the dedicated key, upload
   to GitHub as a signing key, name it to the agent. A new trust surface on
   his identity infra: **his act, never the agent's initiative** (AUTONOMY
   floor). Optional at this step: GitHub vigilant mode (flags unsigned
   commits "Unverified" — including his own pre-boundary history; his call).
2. Agent wires the machine: global git config + the canonical
   `allowed_signers` in atelier.
3. `create-repo` bakes the repo-local `commit.gpgsign=true` into its
   git-config step.
4. Retrofit the fleet's existing repos; record each boundary.
5. Add the CI verification step to the floor workflows.

Steps 2–5 are agent-executable the day step 1 lands.

## What lives elsewhere

The key itself, its passphrase, and its vault location — personal, never in
any repo (SECRETS). The per-repo wiring mechanics land in
`build/REPO-STANDARD.md` when steps 3–5 execute; this doc stays the *why* and
the standard's shape.
