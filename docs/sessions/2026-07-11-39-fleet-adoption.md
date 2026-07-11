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
- `ec2_builder`, `homenetwork`, `hitchbots_guide` — same scaffold; per-repo
  scan scoping applied (the shareable pattern below).

**Pin-bumped current (4)**: `faves`, `ros`, `numen`, `docker-heap`
(`d45a431`/`5db645e` → `1588fda`). Caught real block-wording drift — the
canonical had been de-instanced (`record Mike's decision` → `record the
principal's decision`); faves & ros still had the old text, so the bump carried
the wording, not just the SHA (exactly PROPAGATION's rule).

**Excluded (not a choice — doctrine):** `python-metaname` is under the
`metaname` org, not Mike's — the create-repo "don't touch a third-party repo"
rule, and its named example.

## Security debt surfaced (the scan pre-check earned its keep)

Adopting isn't just stamping — the scan floor *found things*. **The estate
specifics (which private repo carries what) deliberately do NOT live here** —
atelier is public, and the no-personal-estate-data rule covers *posture prose*,
not just secret values. Each finding is tracked in its own private repo's
records. The shareable lesson only:

- Some repos carried **real committed credentials** already tracked in their own
  roadmaps; handled per the policy the principal set in session 38 — scaffold
  safely, treat the secrets as the owner's tracked debt to rotate/purge, **never
  silently allow-mark a real secret**.
- One scary-looking finding was **verified a false positive before it was
  reported** (an SSH FIDO security-key algorithm name mistaken for an `sk-` API
  key) — the "verify before you alarm" discipline.
- Reference/knowledge repos threw **only false positives** on ingested published
  standards; scoped ignores kept the genuinely-scannable content scanned.

## Per-repo scan scoping learned (the shareable pattern)
Infra/network repos need `--disable ipv4,ipv6,mac-address` (IPs/hostnames/MACs
are legitimate config). Reference libraries need their ingested-standards dirs
ignored. Captured runtime snapshots get `.secretscanignore` + `.leakscanignore` —
they're data, not source, and any real secrets in them are the owner's tracked
debt, not a per-commit gate. floor.yml CI is green on every adopted repo except
where a real secret is knowingly tracked (red by design until the owner rotates).

## Owed to the owner
Rotations/purges in the repos that carry tracked secret debt (details in those
private repos); the app purpose one-liners for the two early apps; and — the
standing floor item — registering an SSH signing key to activate the signing
doctrine fleet-wide.
