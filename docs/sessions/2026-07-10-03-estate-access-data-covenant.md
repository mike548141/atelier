**2026-07-10 — estate-access + data covenant.** Also this session: Mike stated
the **data covenant** ("always protect data, mine and others; I hate losing
data") → new `method/DATA-PROTECTION.md` (read-before-write; verified way-back
before any destructive op; data plane is the slow lane even under broad grants;
reproducibility as insurance; enforce the plane-split with the credential not
discipline; protect others' data). Also-added doctrine: model-capability
"who-acts" axis in AUTONOMY; know-your-repo-visibility + secret-exposure
mitigation; parallel-work-tooling item. Estate-access expansion agreed
(least-privilege, read-first, widen-in-rings — NOT blanket tenancy admin):
Google Workspace MCP confirmed live (read); Cloudflare read-token + TrueNAS
observe await Mike provisioning. nas02: full-write-with-snapshot-gate, via **two
separate credentials** (data vs config) so the plane split is token-enforced.
Estate specifics live in ros memory (instance), not this repo. Permissions fixed
so atelier edits stop prompting (ros settings.local.json). **Next session — two
tracks:** (A) build atelier per ROADMAP, start with the propagation anchor;
(B) wire the estate first-ring (Cloudflare + TrueNAS creds; nas02 two-credential
+ snapshot gate).
