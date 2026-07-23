# Cold review — security-canon A/B/C/E edits (rule-4 pass)

**Subject (refs only):** delta `85157c3`, merged `73da10d` — the security-canon
gap closures A/B/C/E: SHA-pinned CI actions across `ci.yml` + child workflow
templates, root `SECURITY.md` + child template + REPO-STANDARD registration,
REVIEW.md lens-4 build-time threat pass + security-finding severity/recurrence
marks, PRINCIPLES §5 secure-by-default + §8 zero-dep-as-supply-chain-control,
tools/README "Supply chain" residual section.

**Spawn provenance:** this review was spawned by a non-author taker session that
the principal (Mike) opened and pointed at the review queue on 2026-07-23; the
work's author (an orchestrated queue run's instructed worker) neither started
nor instructed this review or this reviewer; the taker authored none of the
delta and gave the reviewer refs only.

**Status:** self-authored doctrine — REVIEW.md rules 3 and 4 apply. Findings
below are the principal's to decide; the reviewer recommends and applies
nothing.

## What the work is (as this reviewer establishes it from the delta and HEAD)

Ten files, 217 insertions. Two slices: (1) mechanical — five third-party GitHub
Action references converted from mutable tags to full-commit-SHA pins with
tag-as-comment, in `.github/workflows/ci.yml` and three
`docs/build/templates/workflows/` files; a root `SECURITY.md` (private
disclosure via GitHub Private Vulnerability Reporting, honest no-SLA/no-bounty
posture) plus a child template, registered in `docs/build/REPO-STANDARD.md` as a
publish-time artefact; (2) doctrine — REVIEW.md lens 4 gains a build-time
threat-enumeration obligation (gap A) and a security-finding
severity + recurrence-prevention specialisation (gap E); PRINCIPLES §5 gains a
secure-by-default bullet (gap B) and §8 a supply-chain bearing for the zero-dep
ethos (gap C, reframed per the commit to mutable-tag CI actions); tools/README
gains a "Supply chain" section naming the residuals (unpinned toolchain,
deferred SBOM). The commit claims the five tag→SHA resolutions were verified
live twice, and that the rule-4 review was queued, not self-spawned.

## Attack surface (the reviewer's own, committed before any deferred material)

1. **Are the pins real?** Re-resolve all five tag→SHA pairs live, independently
   (third resolution). A wrong SHA is a supply-chain control that points at the
   wrong code.
2. **Do the public-practice claims hold, checked not recalled?** SHA-pinning as
   the control for mutable tags (GitHub hardening guidance); the SSDF
   "respond to vulnerabilities" recurrence leg; GitHub Private Vulnerability
   Reporting as a real, *and actually enabled*, mechanism on this repo — a
   security policy whose reporting path is dead is worse than none.
3. **Is the encoding house doctrine or pasted canon?** Does each edit ground in
   existing frame (deny-by-default cases, stated-bridge grammar, EVIDENCE-style
   honesty about residuals), point rather than copy (DRY across
   REVIEW.md/PRINCIPLES/SECURITY.md/tools/README), and read in the repo's voice?
4. **Does it duplicate or contradict siblings?** SECRETS.md (its own
   "Grounding in public practice" + secure-defaults bullet), ACCESS.md,
   DATA-PROTECTION.md, SIGNING.md layer 2 (the SBOM/signing deferral the new
   section leans on), REVIEW.md's existing lens 4, floor.yml's own supply-chain
   posture (scanners deliberately floating `atelier@main`).
5. **Does any new rule weaken an existing protection, over-promise, or leak
   person-local detail into a public repo?** (Lens 4 at design altitude — this
   delta is itself security doctrine.)
6. **Re-run every live proof in scope:** the scanners as the hook/CI invoke
   them, both test suites, the pin resolutions.

Non-goals: none. Nothing is fenced off; the deferred material (the gap map §3
and the 2026-07-22-1210 queue-run close entry) is sequenced below the findings,
not out of scope.

The four lenses (approach & assumptions; correctness & quality;
completeness/harvest; security & privacy) organise the run; they do not bound
it.

---

# Verdict — PASS-WITH-FINDINGS

**Counts:** 1 MAJOR · 1 minor · 3 LOW · 1 nit. No finding overturns the
delta's direction; the MAJOR is an operational gap the delta shipped around
(a disclosure policy whose reporting switch is off), not a wrong rule.

**Spawn provenance (repeated per rule 4):** this review was spawned by a
non-author taker session that the principal (Mike) opened and pointed at the
review queue on 2026-07-23; the work's author (an orchestrated queue run's
instructed worker) neither started nor instructed this review or this reviewer;
the taker authored none of the delta and gave the reviewer refs only.

**Re-run, with results (2026-07-23, ~0230 UTC, worktree `queue-reviews` at
`3107ea4`):**

- **Five tag→SHA resolutions, third independent run** (`gh api
  repos/actions/<repo>/git/ref/tags/<tag>`): checkout@v5 → `fbc6f39…`,
  checkout@v4 → `11d5960…`, setup-python@v6 → `ece7cb0…`, setup-python@v5 →
  `a26af69…`, setup-node@v4 → `49933ea…` — **all five match the committed
  pins**, and all five refs are lightweight (type `commit`), so the recipe's
  output was a commit SHA here (see SC3 for the general case).
- **Scanners as the hook/CI invoke them** — `secretscan`, `leakscan`,
  `linkscan`, `reviewscan` (`--root . .`) all clean, exit 0; `sizescan --check`
  exit 0 (ROADMAP size-advisory only, never a gate).
- **Tests** — `node --test instruments/*.test.js`: 150/150 pass;
  `python3 -m unittest discover -s tools`: pass, exit 0.
- **Public-practice claims, checked not recalled** — GitHub's security-hardening
  guidance confirms full-length-SHA pinning as "currently the only way to use an
  action as an immutable release" and names the moved-tag risk the comments
  describe; NIST SSDF (SP 800-218) RV group includes addressing "root causes of
  vulnerabilities to prevent recurrences", corroborating the severity +
  recurrence-prevention encoding; GitHub Private Vulnerability Reporting is a
  real per-repo mechanism — **and is not enabled on this repo** (SC1).
- **`/security-review` scanner** — discharged with grounds, one line per
  REVIEW.md: this is a landed-delta review with a clean tree (nothing pending to
  aim it at), and the delta's files are markdown doctrine plus workflow YAML —
  the markdown class sits inside the scanner's own exclusions, so a clean pass
  would be definitionally empty and is weighed as nothing.

**Lens-4 design-altitude discharge (explicit, no scanner can reach it):** the
delta *strengthens* the posture everywhere it touches — pins narrow trust, the
secure-by-default bullet generalises existing deny-by-default cases without
displacing them, the threat-pass obligation is right-sized against its own
STRIDE-ceremony warning, and SECURITY.md deliberately under-promises (no SLA,
no bounty) in the apex's voice. No new rule weakens an existing protection. No
personal or person-local detail enters: SECURITY.md's "one-person project" is
already-public fact, templates carry placeholders only. The one design-altitude
defect found is SC1 — the policy's operative mechanism was never switched on —
and the one honesty gap in the residual accounting is SC5.

## Findings

### SC1 — MAJOR (security) · SECURITY.md's only reporting channel is not enabled

- **Claim:** the shipped root `SECURITY.md` (`SECURITY.md:36-40`) directs
  reporters to "the 'Report a vulnerability' button under this repository's
  *Security* tab (GitHub Private Vulnerability Reporting)" and forbids public
  issues — but PVR is a per-repo opt-in and is **off** for `mike548141/atelier`:
  `gh api repos/mike548141/atelier/private-vulnerability-reporting` →
  `{"enabled":false}` (live, 2026-07-23). As deployed, the button does not
  exist; a reporter has no working private path and is told not to use the
  public one. The policy's confidentiality claim ("keeps the report confidential
  until a fix exists") is currently false in practice.
- **Evidence:** `SECURITY.md:36-40`; live API check above; neither
  `docs/build/REPO-STANDARD.md:78-88` nor `docs/build/templates/SECURITY.md`
  names enabling the setting as part of seeding the file, so every child that
  copies the template inherits the same failure class.
- **Severity:** MAJOR — a shipped, public-facing security control that does not
  function; the whole document routes through it.
- **Recurrence-prevention step (the class, not the instance):** make "enable
  PVR" part of the seeding act — one line in REPO-STANDARD's SECURITY.md bullet
  and in the template's comment block: *enable Private Vulnerability Reporting
  in the repo's settings and verify with
  `gh api repos/<owner>/<repo>/private-vulnerability-reporting`* — so the
  policy and its switch land as one act. (A CI assertion is possible but likely
  over-ceremony for a one-time publish-time act; the reviewer does not
  recommend it.)
- **Reviewer counsel (decision Mike's):** enable PVR on `mike548141/atelier`
  (repo Settings → Advanced Security, or
  `gh api -X PUT repos/mike548141/atelier/private-vulnerability-reporting`),
  then land the two doc lines. The instance fix is one switch; the class fix is
  two sentences.

### SC2 — minor · The new supply-chain section re-asserts a "deferred" call the repo already made

- **Claim:** `tools/README.md:103-104` (new in this delta) states "**Scanner
  distribution to children** stays the other deferred supply-chain call
  (vendor / fetch / publish) — see the leakscan **CI** wiring note below." But
  `docs/build/templates/workflows/floor.yml` (landed `bafeaa3`, 2026-07-10) *is*
  the fetch resolution: a child's CI checks atelier out beside the repo and runs
  its scanners ("ONE SOURCE, NO VENDORED COPY", floor.yml:8-13). The leakscan CI
  note the new bullet points at (`tools/README.md:208-212` — "A child repo
  cannot do this yet… a child's only scan gate is the per-clone hook") predates
  floor.yml (`bbdeece` is an ancestor of `bafeaa3`) and is stale; the same stale
  claim also lives in `tools/pre-commit.sample:44-46`. The delta's new section
  endorsed the stale note instead of sweeping it — the exact PRINCIPLES §6
  "sweep the stale claims" defect, in a section whose stated purpose is naming
  residuals honestly.
- **Evidence:** `tools/README.md:103-104` vs `floor.yml:8-13,106-115`; commit
  order `bbdeece` → `bafeaa3` (both 2026-07-10); `tools/pre-commit.sample:44-46`.
- **Reviewer counsel (decision Mike's):** reconcile one way. If the call is
  decided (fetch-at-CI via floor.yml — the shipped reality), sweep the three
  stale notes (new bullet, leakscan CI note, pre-commit.sample) to say a child's
  CI floor fetches atelier's scanners and the hook covers the local clone. If
  the call is genuinely still open, floor.yml's header overclaims and should say
  so instead. The reviewer reads the evidence as *decided*.

### SC3 — LOW · The pin-bump recipe silently mis-resolves annotated tags

- **Claim:** `tools/README.md:87` ships
  `gh api repos/<owner>/<repo>/git/ref/tags/<tag>` as the re-resolution recipe.
  For a **lightweight** tag this returns the commit SHA (all five `actions/*`
  tags are lightweight — verified live). For an **annotated** tag it returns a
  *tag object* SHA; pinned into `uses:`, that SHA is not a commit and the
  checkout fails — or worse, a copy-paste lands a SHA that never matches the
  code reviewed. Children applying the recipe to arbitrary third-party actions
  will meet annotated tags.
- **Evidence:** `tools/README.md:85-88`; GitHub git-refs API semantics
  (`.object.type` is `commit` or `tag`); live resolutions above returned type
  `commit` for all five.
- **Reviewer counsel (decision Mike's):** one clause in the bullet — check
  `.object.type` and dereference a `tag` object
  (`gh api repos/<o>/<r>/git/tags/<sha> --jq .object.sha`), or use
  `git ls-remote --tags <url> '<tag>^{}'`.

### SC4 — LOW · SECURITY.md's fix-uptake sentence is imprecise about how fixes reach children

- **Claim:** `SECURITY.md:55-57` — "children pin atelier by commit SHA,
  adopters pick it up by bumping their pin." Half-true: the CLAUDE.md doctrine
  pin works that way, but **scanner** fixes — the likeliest security-fix class
  this policy covers — reach children with *no* pin bump, because floor.yml
  deliberately floats the scanner checkout at `atelier@main` ("newest is
  safest", floor.yml:15-21). The sentence understates the good news and
  misstates the mechanism.
- **Evidence:** `SECURITY.md:55-57`; `floor.yml:15-21`;
  `docs/build/templates/CLAUDE.md` pin line.
- **Reviewer counsel (decision Mike's):** split the sentence — scanner fixes
  flow to child CI automatically (floating floor); doctrine/template fixes
  arrive on the deliberate pin bump.

### SC5 — LOW · The residual list omits the largest unpinned code path a child consumes

- **Claim:** the new "Supply chain" section promises the residual is "named
  here rather than pretended away" (`tools/README.md:75-77`), and names the
  actions, the toolchain, and the deferred SBOM — but not the fact that a
  child's CI **executes atelier's scanners fetched at floating `main`**: for a
  child, that is a whole repo of code consumed unpinned, a strictly larger
  trust surface than the tag-pinned actions the section dwells on. The trade is
  deliberate and well-argued — but in floor.yml's header, not in the section
  that claims to be the residuals' one home (and note the *trust list* is
  deliberately read at the pin, not main — floor.yml:178-184 — so the design
  already distinguishes the two; the README section just doesn't say so).
- **Evidence:** `tools/README.md:67-104` vs `floor.yml:15-21,178-184`.
- **Reviewer counsel (decision Mike's):** one bullet in the residual list:
  child CI trusts atelier@main for scanner code by design (rationale pointer to
  floor.yml), while the signing trust root is pinned — the asymmetry is the
  point and deserves naming where the residuals live. Composes with SC2's
  sweep.

### SC6 — nit · US spellings landed against CONVENTIONS, already swept

- **Claim:** the delta introduced "artifact" (4× `tools/README.md`, 1×
  `docs/build/REPO-STANDARD.md`) against CONVENTIONS' NZ-English default.
  Already corrected repo-wide by the SA9 sweep (`f8350ee`, 2026-07-23) —
  nothing left to fix; recorded because the pattern (new text landing
  US-spelled, caught by a *different* cycle's sweep) is worth a worker-prompt
  nudge, not doctrine.
- **Evidence:** `git show 85157c3:tools/README.md` lines 97-100 vs HEAD;
  `f8350ee` SA9.
- **Reviewer counsel:** none beyond the note.

## Lens summaries (what was checked and found sound)

- **Lens 1 (approach):** the encoding is house doctrine, not pasted canon —
  secure-by-default is built as a generalisation of the repo's own scattered
  deny-by-default cases with the §7 stated-bridge grammar; the threat pass is
  explicitly right-sized against STRIDE ceremony; SECURITY.md's no-SLA/no-bounty
  posture is the apex's no-claim-stronger-than-evidence applied. Sound.
- **Lens 2 (correctness):** all five pins correct at a third independent
  resolution; tag-comments match; all `uses:` across `.github/workflows/` and
  the templates are pinned — none missed. The commit's "verified live twice"
  claim reproduces. Suites and scanners green at HEAD.
- **Lens 3 (completeness/duplication):** no contradiction with SECRETS.md
  (whose grounding section explicitly deferred this sweep to the ROADMAP —
  this delta is that item landing), ACCESS.md, DATA-PROTECTION.md, or
  SIGNING.md (the SBOM/signing deferral correctly points at layer 2's stated
  trigger). Severity/recurrence lives once in REVIEW.md with SECURITY.md and
  REPO-STANDARD pointing at it — DRY held. The one harvest miss is SC2's stale
  trio.
- **Lens 4 (security/privacy):** discharged above; SC1 is the confirmed
  security finding and carries its severity and recurrence-prevention step per
  the delta's own new rule — the rule works; the switch it presumed was on
  was not.

---

## Reconciliation — deferred material (opened only after the findings above were durably written)

*Read after findings SC1–SC6 were committed to this file: the gap map
`docs/sessions/2026-07-22-1025-security-canon-gap-map.md` (§3 especially) and
the close entry of `docs/sessions/2026-07-22-1210-queue-run-3-standing-items.md`.*

**Do the built edits match the mapped gaps?** Yes, on all four, with the map's
own preferences honoured:

- **Gap A** — map proposed the REVIEW.md seam ("prefer REVIEW — the seam
  already lives there") plus a §5 pointer; the delta built exactly that
  (REVIEW.md lens-4 build-time enumeration; PRINCIPLES §5 pointer to it, DRY
  held).
- **Gap B** — map proposed one PRINCIPLES §5 bullet generalising the existing
  deny-by-default fragments using the stated-bridge grammar; built verbatim to
  that shape.
- **Gap C** — **the reframe landed as mapped**: the map's verdict was "name
  zero-dep as the control, enumerate the small residual, don't import an SCA
  pipeline", with the mutable-tag CI actions as the concrete residual item.
  The delta names zero-dep as the control (tools/README + §8 bearing), pins
  the actions, states the toolchain trust, and cross-links the SBOM deferral —
  the map's most substantive finding, executed in its own terms.
- **Gap E** — both moves built: the severity + recurrence-prevention marks
  (seam chosen as REVIEW.md, where the finding lifecycle lives) and the root
  SECURITY.md, extended to a child template + REPO-STANDARD registration.
- **Gap D** — dismissed by the map, untouched by the delta. Correct.

**The queue-run close entry (1240)** lists six worker divergences; all six are
real in the delta as described (pins widened to every template including
commented example lines; E's seam in REVIEW.md not RECORD.md; the child
template + registration; the C bearing in §8 not §2; best-effort window with
no fabricated number; why-comments at each pin). Its verification claims
reproduce: "five tag→SHA resolutions re-run independently (matched)" — my
third resolution corroborates all five; "zero bare `@vN` `uses:` lines left
anywhere" — corroborated by grep at HEAD; floor green — corroborated by the
re-runs above.

**How the deferred material bears on the findings:**

- **SC1** is not touched by either record: the map proposed "a repo-root
  SECURITY.md disclosure policy" and the worker shipped the document, but
  neither the map, the close entry, nor the delta names *enabling* Private
  Vulnerability Reporting as part of the act. The finding stands, and the
  class-fix (make the switch part of the seeding step) gains support: the gap
  was invisible at every stage because no step owned it.
- **SC2's root cause is upstream in the map**: gap C's residual item 3 cites
  tools/README's "the deferred supply-chain call" note as an already-tracked
  residual — trusting that the note was *current*, when floor.yml had resolved
  the call (fetch-at-CI) back on 2026-07-10. The map's own discipline
  ("verified by reading the cited doc") verified the note *exists*, not that
  it was still true; the worker then encoded the inherited stale claim into
  the new section. Finding and counsel unchanged; the provenance sharpens the
  lesson — a cited residual is a live-proven claim like any other.
- **SC3–SC6** are untouched by the deferred material; no overlap, no
  anchor-adjustment needed.

Nothing in the deferred records overturns a finding or reveals a mapped
requirement the delta silently dropped.

---

*Reviewed 2026-07-23 0231 UTC · cold rule-4 pass, read-only, one file written
(this one). Findings SC1–SC6 above are the principal's to decide (REVIEW.md
rules 3–4); the reviewer applied nothing.*
