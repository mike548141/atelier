# 2026-07-11 · session 39 — the whole fleet adopted (Opus)

Mike: "atelier is in a good place to adopt all the other repos I use Claude on —
let's do that." Settled the vocabulary from `PROPAGATION.md` (**child repos** in
**the fleet**; the act is **adopting** = stamping the doctrine block + pin), then
inventoried and adopted every one of his repos.

## Outcome — `tools/pins.py`: all 11 children current at `1588fda`

**Newly adopted (7)** — doctrine block + pin + `floor.yml` + fail-closed hook,
each proven blocking a planted key:
- `rpi`, `nova` — already close to standard; block prepended, additive.
- `Baby Brain`, `FoodTracker` — early iOS/Swift apps; light honest scaffold
  (purpose one-liner flagged TODO, not fabricated).
- `ec2_builder`, `homenetwork`, `hitchbots_guide` — the ones carrying
  secrets/client content (below).

**Pin-bumped current (4)**: `faves`, `ros`, `numen`, `docker-heap`
(`d45a431`/`5db645e` → `1588fda`). Caught real block-wording drift — the
canonical had been de-instanced (`record Mike's decision` → `record the
principal's decision`); faves & ros still had the old text, so the bump carried
the wording, not just the SHA (exactly PROPAGATION's rule).

**Excluded (not a choice — doctrine):** `python-metaname` is under the
`metaname` org, not Mike's — the create-repo "don't touch a third-party repo"
rule, and its named example.

## Security debt surfaced (the scan pre-check earned its keep)

Adopting isn't just stamping — the scan floor *found things*. Handled per the
docker-heap policy Mike set (scaffold safely, ignore captured snapshots, owner
rotates/purges; never silently allow-mark a real secret):

- **`ec2_builder` — the urgent one.** Its own ROADMAP P0 (dated 2026-07-05) is
  **still open**: a **live Google-Authenticator TOTP seed** + TLS private keys,
  and the repo *was public*, so those hit public git history. Verified before
  alarming that the scary "OpenAI key" finding was a **false positive** (an SSH
  FIDO security-key algorithm name in a commented `HostKeyAlgorithms` line, not an
  API key). `data/web_server/` (captured EFS snapshot) + the sshd recipe scan-ignored;
  real keys are the tracked P0. **Recommendation: rotate the TOTP seed now if it's
  still in use; purge history.**
- **`homenetwork`** — real WireGuard/RouterOS keys in a stale `_archive/2024-09-23/`
  capture; scan-ignored as tracked debt (purge candidate). Network repo →
  leakscan `ipv4,ipv6,mac-address` disabled (CI + hook), the docker-heap pattern.
- **`hitchbots_guide`** — **no real secrets**; every finding a false positive on
  ingested published standards (NZISM 3.9, gov frameworks) + source URLs. Scoped
  ignores keep `clients/` scanned. Noted: the machine-local leakscan term list
  legitimately flags client names here (this *is* the client library) — hook-only,
  documented.

## Per-repo scan scoping learned
Infra/network repos need `--disable ipv4,ipv6,mac-address` (docker-heap,
homenetwork). Reference libraries need the ingested-standards dirs ignored
(hitchbots_guide). Captured runtime snapshots (`data/web_server/`, `_archive/`)
get `.secretscanignore` + `.leakscanignore` — they're data, not source, and their
real secrets are tracked debt, not a per-commit gate. floor.yml CI is green on all
adopted repos except where a real secret is knowingly tracked (docker-heap,
ec2_builder — red by design until the owner rotates).

## Owed to the owner
Rotations/purges (ec2_builder TOTP + keys, homenetwork archive keys, docker-heap
inline secrets); the app purpose one-liners for Baby Brain/FoodTracker; and — the
standing floor item — registering an SSH signing key to activate the signing
doctrine fleet-wide.
