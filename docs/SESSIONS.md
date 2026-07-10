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

---

**2026-07-10 — mechanism, then the harvest extraction (Opus, "keep going until
economics say stop").** Followed the ROADMAP sequencing (mechanism before more
content) end to end. **Propagation mechanism** built and proven — new
`method/PROPAGATION.md` (thin anchor / fat pointer: inlined safety floor that
binds even unread + SHA pin + session-start drift check; layer-override rule;
enforcement clause; versioning = commit SHA). Retrofitted `ros` + `faves`
CLAUDE.md with the standard doctrine block; behavioural test passed (drift check
clean at HEAD, surfaces the moved commit from a stale pin). Then the three owed
harvest docs, all grounded not invented: **`EVIDENCE.md`** (A1 — the machinery
behind the apex's honesty: authority tiers, acquisition-method error risk,
absolute dating, store-the-rule, one-fact-one-home, trigger refresh, enforce-by-
machine; generalised from a private reference-library STANDARDS.md), **`REVIEW.md`**
(A2 — the enforcement half the PROPAGATION clause forward-referenced: more-capable-
model review, three lenses, brief-on-top/verdict-below lifecycle) and
**`RECORD.md`** (A3 — docs-as-code lockstep, append-only session log, ADRs,
absolute dating). Finally the **keystone**: extracted `PRINCIPLES.md` from stub to
the canonical general spine (§1–7 + precedence ladder + situation tests,
generalised off tiki with the cases KEPT). Canonicality: atelier now canonical
for the general statement; ros keeps bearings + case-law and points up — the
transitional DRY breach (ros §1–7 prose still mirrors the spine) is flagged loudly
at the top of ros/docs/PRINCIPLES.md and tracked as a ROADMAP trim follow-up
(deferred to a focused ros session). Children's pins bumped c3676ee→dde4170 as the
deliberate adoption act. Six commits across atelier, four across ros/faves; all
pushed. **Economics call: stopping here** — a large coherent slice is done and
context is full; the keystone PRINCIPLES doc + the whole method/ layer deserve
their own Fable review with fresh context. **Next session:** (1) brief + run the
Fable review of the new method/ docs (approach/quality/completeness + leak-check —
the review practice REVIEW.md just codified, applied to itself); (2) then either
the ros PRINCIPLES trim, MODEL-ECONOMICS full extraction + A6/A7, or the build/
layer + create-repo rewire (the delivery vehicle for the propagation block).

---

**2026-07-10 — review brief, then the first mechanical control (Opus, "keep
going until economics say stop").** Session-start drift check fired as designed:
`957fa08` surfaced past the `dde4170` pin — inspected, found session-log-only (no
`method/` change), bumped ros's pin `dde4170→957fa08` deliberately. Then two
deliverables. **(1) The owed review is briefed:** `docs/reviews/2026-07-10-
method-layer.md` scopes the Fable review of the whole `method/` layer (PROPAGATION,
EVIDENCE, REVIEW, RECORD, PRINCIPLES) against the three lenses, with a load-bearing
assumption to attack per doc — sharpest being REVIEW.md's "a *more capable* model
reviews" vs the actual Opus-builds/Fable-reviews split (Fable is the cheaper review
tier, not uniformly more capable; the real value may be independence + fresh
context). ROADMAP grew a "review gate" section so the brief blocks further
extraction. Applies REVIEW.md's own lifecycle to the layer that codified it.
**Running the review is Fable's job, not this Opus session's** — so, staying on the
independent side of that gate, built **(2) the mechanical leak-scan** — atelier's
first executable tool (`tools/leakscan.py` + README, `pre-commit.sample`, term-list
template, unittest). Two layers, split so the scanner leaks nothing: shareable
STRUCTURAL shape-patterns that always run, + a machine-local LITERAL term list
(`~/.claude/leakscan-terms.txt`, never in a repo); absent ⇒ structural-only with a
loud warning (graceful degradation + legibility). Fail-safe exit codes, `--staged`
hot path, `--json`, `.leakscanignore` + `leakscan:allow` escape hatches; zero-dep
stdlib. **It bit on first run** — caught real leaks in its own draft fixtures (a
real address, real coordinates, a family name), now fictionalised: the tool earning
its keep against its own author is the honest proof. ROADMAP safety item ticked;
README/CHANGELOG in lockstep; pyc litter caught + gitignored (amend). **Economics
call: a clean stopping point.** The remaining queue is gated — most extraction
waits on the method/ review (Fable), secret-scan needs a tool install (floor/
confirm), and the ros PRINCIPLES trim depends on the review trusting the spine.
**Next session:** (1) run the briefed Fable review; (2) seed the real
`~/.claude/leakscan-terms.txt` so the scan runs full-cover (turns the control from
partial to real); (3) wire the hook + CI per shareable repo; then the gated
extraction once the review clears.

*Continued (same session):* Mike chose "seed, then wire hooks". **Term list
SEEDED** at `~/.claude/leakscan-terms.txt` (estate specifics from `~/.claude/
CLAUDE.md`; full names, not bare "Mike" which doctrine uses deliberately). Full-
cover validation: atelier **clean**; a scan of ros `tiki/` returned 738 raw hits
but exposed a design truth — structural IP/MAC rules are pure noise on a
networking codebase (722 of them). Added **`--disable <rules>`** (skip named
structural rules, local terms always run) + **positional-path filtering in
`--staged`** (scope to a subtree). With network shapes off, tiki/ narrowed to 16,
all verified fictional/intended — the lone real residue being the OSS author name
in `tiki/pyproject.toml` (allow-marked as intentional attribution; Mike's call
whether to use a handle). This **live-validated the earlier tiki scrub**. Hooks
**installed + proven**: atelier whole-repo; ros `tiki/`-scoped (a real term in
`tiki/` blocks; the same term in the private `docs/` passes). Hooks are local
(`.git/hooks`, uncommitted); tool + docs committed. **Still owed:** CI wiring;
term-list portability to Mike's other devices. **Flagged for Mike:** the
`pyproject.toml` author-identity decision.

---

**2026-07-10 — the method/ layer review (Fable 5, usage-billed; the gated
review both prior sessions stopped for).** Ran the brief at
`docs/reviews/2026-07-10-method-layer.md` deep-not-fast: all five in-scope docs
+ APEX/AUTONOMY/MODEL-ECONOMICS, README/ROADMAP/SESSIONS, the foundation
review, ros `docs/PRINCIPLES.md`, and both stamped child blocks; mechanical
leak-scan over the five docs (clean). **Live datum before the review began:**
the session accidentally started on Opus; the "state your model + pool" rule
surfaced it in line one and Mike swapped to Fable before spend — the doctrine
bit. **Verdict: PASS-WITH-FINDINGS** — 14 findings, 11 [fixed] in-session, 3
[backlog]. Headline (the brief's sharpest ask, confirmed): REVIEW.md's "more
capable model" framing was false against the house's own economics — Fable is
the *cheaper review tier*, and MODEL-ECONOMICS already said the true mechanism
(a *separate, usage-billed* model reviews). Reframed to **independent capable
review** (independence + different blind spots + adversarial brief; capability
a floor, not the definition) across REVIEW/PROPAGATION/README/RECORD, reframe
recorded in-place. Second-order: the child doctrine block's ~15-line squeeze
had **dropped two floor cases** (new trust surfaces; deploy-on-push
new-content qualifier) — restored; children re-stamp at next pin bump.
Honest-gap sentences landed (PROPAGATION's enforcement window; EVIDENCE §12's
no-validator-for-conversation case; EVIDENCE §1 two-register provenance; §4
primary-read scoping); RECORD lockstep scoped to the shared branch; two
PRINCIPLES situation tests regained precedent lines; README's stale
PRINCIPLES-canonicality line + four unlisted method docs fixed (a lockstep
miss). Real-world checks passed: drift check fired-as-written n=2; foundation
review properly dispositioned; ladder adjudicated a fresh live collision (the
leakscan gate-sizing call). [backlog]: fleet-level drift view (P4), SESSIONS
index/detail split (V2), ros-trim guardrail (PR2) — all on the ROADMAP
follow-ups item. Review gate ticked; extraction is unblocked. Committed on
`atelier-method-review`, PR to main (expect ROADMAP/SESSIONS merge conflicts
with the parallel Opus session — keep both sides).
