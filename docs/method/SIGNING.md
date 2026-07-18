# Signing — provenance for a record worth trusting

*Commits are the record, and the record is load-bearing: children pin atelier
by SHA (ADR 0002), reviews cite commits as evidence, and the repo is public —
a push is publication. But a git identity is an **assertion, not an
authentication**: anyone can commit as anyone with two `git config` lines.
Signing closes that gap mechanically (EVIDENCE §12 — enforce by machine, not
by good intention). Standard decided 2026-07-11 (ADR 0007); **activated
2026-07-12** — steps 1–3 of the ladder are live (a dedicated key registered,
the machine wired, atelier's adoption boundary set at a commit that verifies
on both planes), fleet retrofit + CI verification (steps 4–5) still pending.
Written before activation deliberately, so the wiring landed against a stated
standard rather than ad-hoc choices.*

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
  their git config at it; child CI resolves it **at the child's existing
  atelier pin (ADR 0002), never floating `main`** — a floated trust list
  would let anyone with write access to atelier's main mint trust for every
  child silently, exactly the auth-plane compromise the dedicated key exists
  to survive. (A new key therefore fails child CI until a visible, reviewed
  pin bump — correct behaviour for a trust root. Stated residual: no
  signature CI defends against full write compromise of the repo holding the
  trust list — the attacker self-attests in one push; branch protection is
  the compensating control.) Entries carry the committer email as principal
  by convention and `valid-after` (plus `valid-before` on retirement),
  subject to **two traps that both silently fail an entry's verification**:
  - **Quote the values** (`valid-after="20260711Z"`): the man page's unquoted
    form fails to parse on the estate's own OpenSSH ("missing start quote").
  - **Suffix the timestamp with `Z` (UTC), and set `valid-after` before the
    earliest signed commit's committer time *in UTC*.** Bare `20260712` is read
    in the *verifier's local timezone*, so a list that passes on a UTC+12
    machine fails in a UTC CI runner with "key is not yet valid" — a commit made
    at 02:13 NZST is 14:13 the previous UTC day, which falls before a
    local-midnight `valid-after`. Anchoring the window in UTC makes the local
    hook and CI agree. (Both traps were caught live — the quote trap in the
    2026-07-12 review, the timezone trap by atelier's own CI dogfood the same
    day, before any child was retrofitted.)

  Because a parse or timezone failure is silent, the CI/hook step carries a
  known-signed-fixture selftest whose quoted, `Z`-suffixed `valid-after` turns
  either regression red. The file is **append-only** — a retired key is bounded, never deleted,
  so old signatures stay verifiable forever (proven live 2026-07-12: git
  passes the commit's committer timestamp as the verify-time, so a bounded
  key keeps verifying its own era).
- **GitHub's "Verified" badge is the convenience plane, not the durable one.**
  It requires the public key uploaded to the account as a *signing* key and
  the committer email verified on the account. GitHub's verification record
  is **persistent**: it does not re-verify or retroactively adjust old
  commits when a key's state changes — removing a key leaves its history
  marked Verified (and SSH signing keys carry no revocation semantics there
  at all). The `allowed_signers` file + `git verify-commit` is the durable
  plane not because the badge decays but because the badge is
  GitHub-controlled and unauditable, while the file is self-hosted,
  versioned, and reviewed.

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
enforces nothing. And verification is **two-plane by necessity, not choice**
(2026-07-12 review, G1): the house PR flow itself mints commits committed by
GitHub — merge/squash commits signed by GitHub's web-flow **GPG** key, never
by any machine key; two already sit in atelier's own `main` (`a0ef731`,
`4b2cf6f`) — and `git verify-commit` on those needs a GPG keyring this estate
doesn't run. A verify step that swept every commit against `allowed_signers`
would red-flag its own repo on first activation.

- **Machine-key commits** (everything not committed by
  `GitHub <noreply@github.com>`): `git log --show-signature` / <!-- leakscan:allow: GitHub's public web-flow committer address, not personal data -->
  `git verify-commit <ref>`, resolved against the canonical
  `allowed_signers`.
- **GitHub server-side commits:** assert
  `gh api repos/<owner>/<repo>/commits/<sha> --jq .commit.verification.verified`
  is `true`. The committer string alone exempts nothing — anyone can set it;
  the API check is what closes the spoof (live-proven on `a0ef731`:
  `verified: true, reason: valid`). `gh` is already the house tool, so
  zero-dep survives.
- **CI:** a `floor.yml` / `ci.yml` step runs both planes over commits **after
  the adoption boundary** (see below). Two execution facts the step must
  encode when it lands: the checkout needs `fetch-depth: 0` (the floor
  template's default depth-1 sees no history), and the sweep is
  `git rev-list <boundary>..HEAD`.

What verification asserts, honestly: git checks the signing key is a *member*
of `allowed_signers` — it does **not** bind key to committer identity (any
listed key verifies any committer; proven live). The assurance is
machine-level custody unless CI additionally compares the reported principal
to the committer email — not wired; decide when step 5 lands.

## The adoption boundary — unsigned history is a fact, not a defect

History is **never rewritten to sign it**: atelier's `main` is append-only,
and a force-push would orphan every child's pin (ADR 0002). Each repo's
boundary is simply its first signed commit; verification gates from there
forward. Pre-boundary unsigned history is stated plainly and left alone —
retro-signing would trade the whole propagation mechanism for a badge.

## Key handling — where SECRETS' boundary falls

The signing key is **identity-layer, person-level**: per SECRETS' scope
boundary the *durable* copy lives in the operator's personal vault, outside
the estate's cheap-burn store. Custody stated at true strength (2026-07-12
review, G5): signing runs on every commit, so every committing machine holds
a working copy (or an agent session) readable by the agent process — a
standing machine credential, tracked as such per SECRETS, passphrase-in-agent
as the mitigation. The failure modes stay mild — the reason this layer is
cheap to run:

- **Exposure** — remove the key from GitHub (this stops *future* badge
  minting only: existing badges persist, including any the attacker minted
  before removal — the local plane is the only recourse for those), mint a
  replacement, append the new entry to `allowed_signers` and bound the old
  with `valid-before`. Honest limit: bounding is **retirement hygiene, not
  revocation** — the verify-time is the commit's own committer timestamp,
  which a signer controls, so a holder of the retired key can backdate into
  its window and verify locally; GitHub's plane (key registration checked at
  push time) is the complement, and the two cover each other.
- **Loss** — mint and register a new key; nothing becomes unreadable, and
  local verification of old commits is untouched (`allowed_signers` still
  holds the retired public key). Unlike the store master key, a lost signing
  key costs minutes, not access.

## Activation ladder (status: fully active 2026-07-12 — warn-first, faves/ros deferred)

1. **[done 2026-07-12]** **Principal registers a signing key** — generate the
   dedicated key, upload to GitHub as a signing key, name it to the agent. The
   badge additionally needs the committer email verified on the account (it
   already is here; stated for adopters). A new trust surface on his identity
   infra: **his act, never the agent's initiative** (AUTONOMY floor). Optional
   at this step: GitHub vigilant mode (flags unsigned commits "Unverified" —
   including his own pre-boundary history; his call — **left off for now** so
   the pre-retrofit fleet doesn't read red).
2. **[done 2026-07-12]** Agent wires the machine: global git config + the
   canonical `allowed_signers` in atelier (quoted-timestamp entries — see
   above). Adoption boundary is atelier `958b1ea`; proven on both planes
   (`git verify-commit` → good, `gh api …verification.verified` → true). The
   passphrase-protected key is loaded via `ssh-add --apple-use-keychain` so
   signing runs unattended (passphrase-in-agent, per Key handling above).
3. **[done 2026-07-12]** `create-repo` bakes the repo-local
   `commit.gpgsign=true` into its git-config step (and REPO-STANDARD's new-repo
   process states the same).
4. **[done 2026-07-12]** Retrofit the fleet's existing repos; record each
   boundary. The boundary's home resolved as designed: **`SIGN_BOUNDARY` in the
   child's own `floor.yml`**, read by `git rev-list <boundary>..HEAD`. All **10
   children carrying the house floor** retrofit (pin bumped to a signing-aware
   atelier SHA + the floor signing steps + their pre-signing HEAD as boundary);
   7 verified green, 3 (docker-heap, rpi, homenetwork) red on **pre-existing
   scanner debt that predates signing** — they fail at the scanner stage before
   the signing steps run, owner's debt to clear. **Deferred: faves and ros** run
   bespoke `ci.yml`, not the house floor — signing-CI for them waits on a
   separate floor-adoption pass (they still *sign* every commit; only their CI
   *verification* is deferred).
5. **[done 2026-07-12]** CI verification in the floor workflows — both planes
   (machine-key via `tools/signscan.py` + GitHub API), `fetch-depth: 0`, trust
   list at the child's pin (`git show <pin>:allowed_signers`), the
   known-signed-fixture selftest. **Warn-first** (Mike's steer): reports, does
   not block, until the fleet settles; flip instructions live in both workflows.

Vigilant mode stays off until the fleet is fully green (else pre-boundary
history reads "Unverified"); flipping CI from warn to block is the remaining
deliberate step, Mike's call once the pre-existing scanner debt is cleared.

### Answering "would the flip pass?" — `tools/signfleet.py`

Warn-first has a blind spot that cost this estate a wrong belief for six days.
Because `signscan` runs `--warn` everywhere, **no child's floor can fail on
signing** — so a green floor is not evidence that a child signs, only that the
step cannot fail. And on a child whose earlier scanners fail, the signature steps
never execute at all: the job skips the rest. Greens and reds were both mute.

On 2026-07-12 that produced a recorded claim that flipping "wouldn't newly-red"
any child, reasoning from the fact that none of the *scanner-red* children failed
on signing. The reasoning could not carry the claim, and re-probing on 2026-07-19
found **two children that would newly-red — both of them green at the time**.

`signfleet` closes the gap: it runs `signscan` in **blocking** mode against every
discovered child, each resolved the way that child's own CI resolves it — trust
list from atelier's `allowed_signers` **at the child's pin** (never floating
main, per ADR 0002), boundary from the child's own `SIGN_BOUNDARY`. It is
read-only and answers exactly one question: *would the flip pass, today?*

```sh
python3 tools/signfleet.py            # fleet report
python3 tools/signfleet.py --check    # exit 1 if any child would fail
python3 tools/signfleet.py --json     # machine-readable
```

It is a **local** tool, like `pins` — it reads sibling repos on this machine, so
it cannot run in CI, and its test suite is where it is proven. Two honest limits
carried in its docstring: it verifies the **machine plane only** (server-minted
merge/squash commits are reported `deferred`, exactly as `signscan` reports them,
and need the `gh api` plane), and a pass means *today, at this HEAD* — the next
unsigned commit changes the answer. **Run it before the flip, not after.**

## Operational notes (known issues)

- **"couldn't load key" / "incorrect passphrase" on commit.** The signing key is
  passphrase-protected; if it isn't loaded in the ssh-agent, `git commit` fails
  to sign with that cryptic error and writes no commit. **Fix — load it once per
  login:** `ssh-add --apple-use-keychain ~/.ssh/id_ed25519_signing` (drop the
  `--apple-use-keychain` flag off macOS). The flag caches the passphrase in the
  OS keychain so it survives reboots; you should rarely need to re-run it. The
  pre-commit hook now runs a silent test-sign and prints this same remedy the
  moment signing looks unready, so the failure is caught before the scanners'
  work is wasted, not after.

## What lives elsewhere

The key itself, its passphrase, and its vault location — personal, never in
any repo (SECRETS). The per-repo wiring mechanics land in
`build/REPO-STANDARD.md` when steps 3–5 execute; this doc stays the *why* and
the standard's shape.
