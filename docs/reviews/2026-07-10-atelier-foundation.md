# Fable review — atelier foundation & approach

**Status:** brief (ask on top). Verdict appended below the divider after the
review runs. Mike flagged this as the highest-value work in flight and
authorised generous Fable spend, so review deep, not fast.

## What atelier is (context for the reviewer)

atelier is the extracted, shareable *operating model* for how Mike and Claude
work — the doctrine that made `ros`/`tiki` good to build in, lifted above any
single repo so every project inherits it and peers can adopt it. Two layers:
`docs/method/` (how we work — shareable) and `docs/build/` (how we build — repo
craft). Born 2026-07-10; `method/` first slice is written, `build/` +
extractions are pending. Read the repo (`README.md`, `docs/method/*`,
`docs/ROADMAP.md`) before reviewing.

## Scope — three lenses, review all three

1. **Approach & assumptions** (the most important lens — is this the right
   problem, solved the right way?).
2. **Doctrine quality & honesty** (are the written docs sound, consistent, and
   free of overclaim — is a stub honestly a stub?).
3. **Completeness / harvest** (what doctrine already lives in the repos that
   atelier has NOT captured?).

## Load-bearing assumptions to challenge

Attack these; if any is false, atelier is mis-built:

1. **The good stuff is extractable.** That the thing which makes ros good is
   *writable doctrine* that transfers by being read — not tacit skill that a
   document can't carry. If most of the value is tacit, atelier is theatre.
2. **Layered inheritance is the right model** for *working method*
   (machine→house→project→session), the same shape tiki uses for config. Or is
   working-method the wrong thing to model as config-inheritance?
3. **A separate repo is the right home** — vs keeping doctrine in ros, or in
   `~/.claude`. Does extraction create a second source of truth that will
   diverge (the exact DRY sin the principles forbid)?
4. **Propagation is solvable simply.** The hard open problem (see below). Is
   there a KISS mechanism, or does "keep every repo current with the house
   doctrine" inherently require heavyweight machinery?
5. **The shareable/personal split is cleanly separable** — that no piece of
   genuinely useful doctrine is so entangled with personal/estate context that
   it can't be shared without leaking. Test the boundary.
6. **Broad autonomy is safe.** commit+push+PR granted for all work, with the
   stated floor (private→public, destructive, secrets, spend, people/safety,
   unapproved-tool install). Is the floor complete? Any recoverable-looking
   action that is actually catastrophic and slips through?

## The propagation problem (design critique wanted)

Mike: *"How do we learn this lesson once — keep all repos/sessions up to date as
the house doctrine changes? Child repos like faves need to feed off the house
doctrine repo."* Weigh the candidate shapes and recommend one (or a better
one):

- **Reference** — each child `CLAUDE.md` points at atelier ("doctrine lives
  there, read it"). One source, but requires the child session to actually go
  read it, and offline/other-device access matters (see north-star).
- **Vendored copy + drift-check** — child carries a copy; a check flags when it
  lags atelier. No divergence-by-neglect, but two copies.
- **Session-start pull/hook** — a hook refreshes doctrine at session start.
  Events-over-polling? Fail-safe if atelier is unreachable?

Judge against the principles (DRY, one source of truth, legibility/observable
staleness, graceful degradation when atelier is unreachable, KISS).

## New threads to risk-check

- **Portable personal context** — Mike wants `~/.claude` personal context to
  travel with *him* across devices (iPhone/Mac/successors), while never entering
  a shared repo. Where should that store live? Security/privacy of syncing
  personal+health+financial context across devices.
- **Session archive** — archive every session (chat/cowork/CLI/VS Code) as
  detail-on-demand. Worth the storage + privacy handling, or is the SESSIONS.md
  index enough? Retention/scrub concerns.
- **Repo-boundary guidance** — the rule for standalone repo vs component of an
  existing one (e.g. rich EPL client work). What's the decision framework?

## Real-world check (the honest test)

The true proof is behavioural, not textual: (a) would a *new* repo scaffolded to
inherit atelier actually behave per the doctrine in a fresh session, and (b)
could `faves` genuinely "feed off" atelier today? If the answer needs machinery
that doesn't exist yet, say so plainly — don't grade the docs as if they were
the mechanism.

---

## Verdicts (2026-07-10) — synthesis of three reviewers

Two Fable reviewers (approach/propagation; quality/honesty/leak-check) + one
plan-pool harvest agent. Faithful synthesis; finding IDs preserved so nothing is
lost. Disposition tagged: **[fixed]** this session · **[backlog]** a named
ROADMAP slice.

### Overall: PASS-WITH-FINDINGS ×2 + clean leak-check
Right problem, right home, honest stubs, **no personal-data leak**. Conditional
on: canonicality decided before extraction; the autonomy floor's gaps closed;
extraction that keeps the case-law; instance-detail split out of the shareable
layer at (or before) public release.

### Approach & assumptions (Reviewer 1)
- **A1 extractable — partial.** ros doctrine works because it's *case law*
  (every principle has a bearing, every precedence rule a decided case).
  Extracting the "spine" while deleting the cases = theatre. **Extract WITH
  generalised cases.** [backlog: PRINCIPLES extraction]
- **A2 layered inheritance — partial.** Great *placement* rule, not a *merge*
  mechanism (no engine — an LLM reads several docs). Needs an explicit override
  rule: *a child may narrow or append, never silently contradict; a contradiction
  is a defect to surface.* [backlog: method/ override rule]
- **A3 separate repo — holds, condition breached NOW.** `00-APEX.md` and ros
  `PRINCIPLES.md §0` are two verbatim copies. Canonicality is a *precondition*
  of extraction, not a deferred question. **Decision taken:** atelier canonical
  for the general statement; ros keeps bearings + case-law and points up;
  children point up, the parent never points down for truth. [fixed]
- **A4 propagation — holds.** See recommendation. [backlog: build the anchor]
- **A5 shareable/personal split — partial.** AUTONOMY (cognitive-load profile +
  grant ledger) and STORAGE (Apple/iCloud/NAS specifics) carry the *instance* in
  the shareable layer. Restructure on the TOOLBOX practice/instance pattern.
  [fixed: tagged as worked-examples · backlog: full restructure]
- **A6 broad autonomy — partial, two leaks** (see Reviewer 2 Q1, merged).

**Propagation recommendation — "thin anchor, fat pointer" (dependency+lockfile
for doctrine).** Reject bare-reference (silent staleness — the failure §6
exists to kill), vendoring (rebuilds the N-copy problem), pull-hook (machinery
to distribute machinery). Build: (1) atelier tags itself on each doctrine change
(CHANGELOG already there); (2) every child CLAUDE.md carries a standard block =
inlined ~8-line safety floor (apex + always-confirm, binds even if atelier is
never read — fail-safe) + pointer + version pin; (3) a one-line drift check rides
the existing session-start CLAUDE.md read (`git -C ../atelier log --oneline
PIN..HEAD`); (4) bumping the pin is a deliberate per-repo act; (5) create-repo
stamps the block; (6) sessions need nothing extra — the CLAUDE.md read *is* the
propagation event. Honest caveat: the pin makes staleness *observable*, not
*enforced* — enforcement is the review practice. [backlog: mechanism slice —
do BEFORE further extraction]

**Category error to write down:** read ≠ complied. Enforcement was always the
review loop, not the document. [backlog: review-practice doc]

### Quality / honesty / leak-check (Reviewer 2)
- **Q1 autonomy floor — three gaps (do first; atelier becomes every repo's
  inherited posture):** (a) **self-widening** — nothing stops the agent editing
  AUTONOMY/allowlists to widen its own grant; add *grants change only on Mike's
  explicit dated words; the agent records, never originates.* (b) **lockout-class**
  — deploy/merge can sever the agent's own access path (router/tunnel/auth/
  firewall); looks recoverable, isn't; confirm or have a tested out-of-band
  rollback. (c) **GitHub settings surface** — add-collaborator (audience),
  deploy-keys/webhooks/app-installs (trust surface), repo-delete, remote-branch
  delete with unmerged work. [fixed]
- **Q2** pull-quote lists 4 of 6 floor items — omits *truly destructive* +
  unapproved-install. [fixed]
- **Q3** stale "per-repo grants" summaries (README, method/README) lag the global
  grant. [fixed]
- **H2** README lists `docs/decisions/` which doesn't exist (structure-as-present
  = apex defect). [fixed: stub added]
- **H3** TOOLBOX quotes AUTONOMY saying "reversible and local" — phrase not in
  AUTONOMY (fabricated quotation — apex defect). [fixed]
- **Q4** STORAGE "Three locations" heading over a 4-row table; secrets "fourth"
  (would be fifth). [fixed]
- **Q5** atelier CLAUDE.md narrowing should cite the private→public floor, not
  silent blast-radius. [fixed]
- **Q6** NZ English: "synthesize" → "synthesise" (CONCURRENCY). [fixed]
- **Q7** APEX Law 2 "human beings" reads as *any* colleague in shared use; scope
  to "its principal". [fixed]
- **H1 / Q8 positive:** stubs honestly labelled; docs concrete + actionable.

**New-threads risk:**
- **N1 portable context:** E2E-encrypted sync ONLY (iCloud ADP or sops/age);
  **never GitHub, even private**; the repo boundary must be enforced
  **mechanically** (pre-commit/CI leak-scan denylist) — intent isn't a control;
  tier the store (crown-jewels encrypted at rest locally); device floor
  (FileVault/passcode). Honest gap: the **iPhone leg has no mechanism** — the
  Claude app doesn't read `~/.claude`. [backlog: north-star, with these as
  mandatory controls]
- **N2 session archive:** worth it as **encrypted cold storage** — NAS,
  local-only (never iCloud-broad, never a repo), ~12-month rolling retention, **no
  search index initially** (searchability = exfil surface); NZ Privacy Act
  retention applies (third-party PII in transcripts). Start with Claude Code
  `.jsonl`; "every session incl. chat/cowork" needs export machinery that doesn't
  exist — say so. [backlog]

**Leak-check — clean.** Residuals: **L1** EPL named → add "client names" to the
public-release scrub list. **L2** operator-instance detail (iCloud path/NAS in
STORAGE; ros/faves in AUTONOMY table) — tag as worked examples. **L3**
`settings.local.json` (gitignored, verified) grants unscoped Bash — makes the
committed allowlist decorative on this machine; personal choice, noted.

### Harvest (plan-pool) — doctrine NOT yet in atelier, ranked
A1 **evidentiary/provenance standard** (hitchbots `STANDARDS.md`: authority
tiers, absolute-dating, store-the-rule-not-the-value, trigger-refresh) — biggest
un-captured seam; mechanically hardens the apex → new `method/EVIDENCE.md`.
A2 **peer-review lifecycle** + brief format. A3 **session + doc-as-code
discipline**. A4 **model-capability authority** (ros ADR 0006 — a *who-acts*
axis distinct from AUTONOMY's *what-action*; "policy in memory protects
nothing — encode it"). A5 **supply-chain/release provenance** (SBOM +
keyless signing; recurs faves+rpi → house standard). A6 source-acquisition
escalation ladder. A7 honest-instrument doctrine. A8 **manifest-as-router /
multi-surface consumption** (hitchbots — a working precedent for propagation +
resume-from-any-device). A9 3-tier model allocation. A10 repo-craft cluster
(product-in-subfolder, standardise-existing process, honest-CI, lockstep-change,
TODO/comment conventions). A11 licence-consistency pre-publish gate. **Flag:**
`docker-heap` is unstandardised (stub README, no CLAUDE.md) — candidate for the
standardise-existing pass. [all backlog: build slices]

---
<!-- End verdicts. Follow-up tracked in docs/ROADMAP.md. -->

