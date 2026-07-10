# atelier — session log

Append-only, newest last. Tail-read at session start; append an entry before
finishing. One short paragraph per session; unpack detail in the repo it
describes.

---

**2026-07-10 — repo born.** Split out of a wider conversation about how Mike and
Claude work together. atelier is the extracted operating model: the doctrine
that made `ros`/`tiki` good to build in, lifted above any single repo so every
project inherits it and peers can adopt it. Decided (Mike): start with the
doctrine repo; name `atelier`; private-to-CEL first. Two layers — `method/` (how
we work, shareable) and `build/` (how we build, repo craft). Stood up the
`method/` layer: `00-APEX` (honesty absolute + AI-adapted Three Laws, extracted
from ros §0 committed the same day and generalised estate-wide), `AUTONOMY`
(per-repo grants; reconciles ros commit-only vs faves commit+push-deploys),
`STORAGE` (GitHub master / iCloud backup / Time Machine-to-NAS whole-machine /
laptop disposable), `CONCURRENCY` (worktree-per-line + serialise real-world
side-effects), `TOOLBOX` (keep a manifest; approved-but-missing may be
installed; keep the personal inventory machine-local). `PRINCIPLES` and
`MODEL-ECONOMICS` left as honest stubs pointing at ros pending extraction.
Local commit only — GitHub owner/visibility deferred to Mike. Next: the
extractions and rewiring `create-repo` to inherit from here.

---

**2026-07-10 — pushed, reviewed, corrected.** Repo created private
`mike548141/atelier` and pushed. Global autonomy grant landed (commit+push+PR
all work; floor holds). Ran the foundation review: 2 Fable reviewers
(approach/propagation; quality/honesty/leak-check) + 1 plan-pool harvest
(scanned all repos for uncaptured doctrine). Both Fable PASS-WITH-FINDINGS, leak
check clean. Verdicts synthesised into
`docs/reviews/2026-07-10-atelier-foundation.md`. Applied all corrections to
already-pushed doctrine: closed 3 autonomy-floor gaps (self-widening, lockout,
GitHub-surface) + deploy carve-out + recoverability-ends-at-push; decided
canonicality and fixed the active APEX↔ros §0 DRY breach (ros §0 shrunk to
inlined floor + pointer — first instance of the "thin anchor, fat pointer"
propagation pattern the review recommended); honesty nits (fabricated quote,
absent decisions/ dir, stale per-repo summaries, renumbering, NZ spelling);
tagged instance-detail as worked-examples. Folded in Mike's live threads:
all-models-one-doctrine (APEX "who it binds"), review-trigger policy
(inline-background vs batched) + tiered authority (MODEL-ECONOMICS), and the
**two-tier person-context portability** north star (crown-jewels E2E-only vs
lighter instance layer; iPhone leg has no filesystem mechanism). ROADMAP
rewritten as the prioritised backlog — **mechanism (propagation anchor +
create-repo rewire) before further extraction**. Net-new build (EVIDENCE,
peer-review, session-discipline, PRINCIPLES/MODEL-ECONOMICS extraction,
supply-chain, build/ standard, leak-scan tooling) deferred to fresh session(s)
for context economics. Next: build the propagation anchor mechanism.

---

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

---

**2026-07-10 — propagation mechanism built + children stamped.** Built the
load-bearing "thin anchor, fat pointer" architecture the foundation review put
ahead of all further extraction. New `method/PROPAGATION.md`: the mechanism (5
parts — SHA-as-version, standard child block, inlined floor that binds unread,
drift check riding the session-start read, human-in-the-loop pin bump), the
canonical child-block text, the **layer-override rule** (a child may
narrow/append, never silently contradict; a contradiction is a defect to
surface, and the stricter reading wins pending resolution up), and the
**enforcement clause** (read ≠ complied — the review-with-a-more-capable-model
practice is the enforcement, not the document). Versioning decided: commit SHA
*is* the version, CHANGELOG is the human index, tags reserved for milestones.
Wired into method/README + CHANGELOG; ROADMAP propagation block fully ticked.
Committed atelier at **c3676ee** (the pin). Retrofitted both children with the
stamped block: `ros` (PRIVATE, secrets+topology → publish needs scrub;
declares its `docs/PRINCIPLES.md` bearings as narrow/append) and `faves`
(PRIVATE-for-now but publication-bound). Behavioural test passed — the drift
check runs clean at HEAD and surfaces exactly the moved commit from a stale pin.
Next per ROADMAP: extraction can now begin (PRINCIPLES spine + cases, EVIDENCE
harvest A1), or rewire `create-repo` to stamp this block on new repos (the
delivery vehicle for the mechanism just built).
