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
