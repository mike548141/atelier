# Review brief — AW1–AW9 rulings application (rule-4 cold pass)

- **Date**: 2026-07-23 03:22 UTC (brief written; verdict stamped below)
- **Subject**: commit `e8d707c` — the application of the AW1–AW9 rulings onto
  the apex-widening doctrine. Files in the delta: `docs/method/00-APEX.md`,
  `docs/method/GLOSSARY.md`, `docs/method/README.md`, `docs/ROADMAP.md`.
  Reviewed as applied text at HEAD `9df3510`; applied-text provenance
  established below.
- **Review class**: application review under REVIEW.md § *Applying decisions
  to doctrine*. The prior pass (0222 apex-widening cold) carried 1 MAJOR, so
  this application inherits rule-4 status. Rule 3 binds: findings are the
  principal's to decide; this reviewer recommends and applies nothing.
- **Spawn provenance** (stated verbatim, repeated in the verdict): this review
  was spawned by a non-author taker session that the principal (Mike) opened
  and pointed at the review queue on 2026-07-23; neither the doctrine's
  author, any prior verdict's author, nor the applier session (or its
  subagents) started or instructed this review or this reviewer; the taker
  authored none of the chain and gave the reviewer refs only.

## Applied-text provenance (which HEAD text is the applied text)

- `00-APEX.md`, `GLOSSARY.md` — untouched between `e8d707c` and HEAD; HEAD
  text is the applied text verbatim.
- `docs/method/README.md` — later touched only by `86f8530` (economics cycle,
  the ECONOMICS entry hunk, lines ~48–51); the AW9 hunk (GLOSSARY→REVIEW
  spacing) is disjoint. Survival verified below.
- `docs/ROADMAP.md` — later rewritten by `bbaec81`, `9990fc9`, `9df3510`
  (cycle closures + the taker's claim commit). The AW6 preamble sentence and
  the AW2/AW8 propagation item must be verified surviving at HEAD; the AW-item
  pointer itself was legitimately rewritten into the application-review claim.

## Sequencing note (rule 2 residual — named, not denied)

Deferred until findings are durably written in this file: the prior verdict
`docs/reviews/2026-07-23-0222-apex-widening-cold.md`, everything in
`docs/sessions/`, `docs/SESSIONS.md`, `docs/ROADMAP-DONE.md`, all other
`docs/reviews/` files. Unavoidable exposure, named not denied: (a) the
subject commit's own message carries a per-ruling digest (AW1–AW9, one line
each, including AW1's MAJOR framing) — read via `git show`, unavoidable when
establishing the subject; (b) the ROADMAP pointer names the chain (pass
counts, "accept-all as counselled", cycle statuses). Both are the applier's
framing; both are treated as claims to test, not settled scope. The
reconcile section (ruling-by-ruling faithfulness table) is written only after
findings are committed.

## Attack surface (named by the reviewer as its first act)

1. **Fidelity vs invention** — an "accept-all as counselled" application
   should reproduce the rulings, not extend them. Attack: does any applied
   hunk carry new doctrine the ruling digest doesn't cover (the glossary
   cold-review rewrite and the AW7 "admitted on concept-spread" note are the
   likeliest places for applier judgement to have produced *new* wording with
   doctrinal force)?
2. **The AW1 scope sentence** — the one MAJOR. Attack: does the added scope
   sentence actually resolve the self-violation the MAJOR named (the
   proof-bar bullet binding the principal's dictated rulings), or does it
   merely gesture? Is it consistent with the surrounding bullet, with
   RECORD.md's actual machinery, and with the triad above it? Does the bullet
   still read coherently with two dated attributions ((Mike, 2026-07-23)
   inside a bullet closing (Mike, 2026-07-22))?
3. **The AW5 boundary clause** — the mandated-withholding carve-out is a
   *narrowing of the honesty absolute's transparency component*, the highest-
   blast-radius text in the repo. Attack: can the carve-out be read wider than
   intended (any "doctrine-barred value" as a withholding licence)? Does
   "declaring its existence and where it lives" hold against SECRETS-style
   practice?
4. **The AW2 propagation item's mechanical claim** — the ROADMAP now names
   specific surfaces with line numbers and asserts "all still two-element at
   HEAD". Line-number claims in prose rot fast and later commits already
   touched sibling files. Re-run every named surface at HEAD.
5. **The AW6 preamble rule** — "a later commit that touches a queued delta's
   doctrine surfaces widens the pointer's delta list in the same commit".
   Attack: did the repo itself comply between e8d707c and HEAD (later commits
   touched README.md and ROADMAP.md — both surfaces of this queued delta —
   did the pointer's delta list widen)? A rule broken by its own enacting
   window is the AW1 class of defect again.
6. **Glossary consistency** — the rewritten *Cold review* and *Doctrine*
   entries now make strong canonical claims ("single-sourced there",
   spawn-criterion restatement). Attack: do they match REVIEW.md's actual
   rule text, and do they stay inside GLOSSARY's thin-anchor admission rule
   (entries point to canon, not restate it)? Are they still marked
   SEED/PROPOSED where the ratify pass is owed?
7. **Survival at HEAD** — the delta landed mid-queue-run; three later commits
   rewrote ROADMAP.md wholesale. Verify each applied hunk survives.

## The four lenses

1. **Approach & assumptions** — is applying accept-all rulings via a neutral
   applier, with this exact wording, the right resolution of each ruling? The
   applier's wording choices are the reviewable judgement.
2. **Correctness & quality** — does each hunk do what the ruling decided;
   overclaim or silent scope-cut in the new text; internal consistency of the
   edited docs at HEAD.
3. **Completeness / harvest** — did the application miss a surface a ruling
   reached (stale restatements the AW2 list itself should have caught;
   sibling docs that restate the pre-AW5/AW1 text)?
4. **Security & privacy** — the AW5 clause is itself a security-adjacent
   doctrine change (what may be withheld and how declared); tree-mode
   scanners re-run as the mechanical floor; `/security-review` reach assessed
   for a landed markdown delta.

## Proofs to re-run (widest scope the work admits)

- `python3 -m unittest discover -s tools` (expect ~330)
- `node --test instruments/*.test.js`
- Five scanners, exit codes checked individually: secretscan, leakscan,
  linkscan, reviewscan, sizescan `--check`
- AW2 surface list: every named file:line checked two-element at HEAD
- AW6 vs the repo's own conduct in e8d707c..HEAD
- GLOSSARY PROPOSED/SEED markers; README AW9 spacing at HEAD; ROADMAP
  preamble sentence at HEAD

---

# Verdict

- **Date**: 2026-07-23 03:28 UTC (findings committed; reconcile section
  appended after, marked below)
- **Status**: **PASS-WITH-FINDINGS** — 0 MAJOR / 2 minor / 1 LOW / 1 nit
- **Cycle status**: **no MAJOR ⇒ the apex-widening cycle is terminal** per
  REVIEW.md's close rule — what remains decides into the backlog; this
  application does not spawn another full ceremony. Findings are the
  principal's to decide (rule 3); this reviewer applied nothing.
- **Spawn provenance** (repeated from the brief, verbatim): this review was
  spawned by a non-author taker session that the principal (Mike) opened and
  pointed at the review queue on 2026-07-23; neither the doctrine's author,
  any prior verdict's author, nor the applier session (or its subagents)
  started or instructed this review or this reviewer; the taker authored none
  of the chain and gave the reviewer refs only.

## Lens-4 mechanical floor — discharge stated

`/security-review` cannot be aimed at this work: the subject is a **landed
markdown delta** (nothing pending), the scanner reads pending changes — and
running it over the working tree would scan this review's own draft, the
exact SL2 hazard REVIEW.md records — and its file-class exclusions bar
markdown documentation, so even a contrived run would return a
definitionally-empty clean. Discharged on those grounds. The reachable
mechanical floor is the five tree-mode scanners, all re-run green (table
below). Lens 4 still ran substantively: the AW5 boundary clause is the
delta's one real security-adjacent surface — attacked below (finding-free);
the AW1 scope sentence is a governance boundary, no exposure; the
GLOSSARY/README/ROADMAP hunks are navigational.

## What held under attack (verified, not taken)

- **AW1 scope sentence resolves the MAJOR it answers.** The self-violation
  the prior pass named (the proof bar, read literally, binding the
  principal's own dictated rulings) is closed: proof duty attaches to the
  agent's proposals and the grounding/recording of rulings via `RECORD.md`,
  never as a bar against the principal. Coherent with 00-APEX § The
  principal's authority (the waiver structure) and REVIEW.md rule 3.
- **AW5 boundary clause survives widening attacks.** It cannot be read as a
  general withholding licence: the bar must exist *in doctrine* (SECRETS'
  references-never-values; the no-personal-data boundary), and the existence
  must be *declared* — the undeclared gap stays dishonesty. "Where it lives"
  discloses the store, never the value: no new exposure, consistent with
  SECRETS.md practice.
- **Glossary rewrites are faithful to canon.** The *Cold review* entry's
  spawn criterion, taker-writes-brief, and pointer-is-refs-only all match
  REVIEW.md rule 4's text; the cold-context-under-warm-spawn contrast matches
  rules 1–2. The *Doctrine* entry's "single-sourced there" reproduces rule
  4's own phrase for rule 3's definition. SEED/PROPOSED banner intact; the
  ratify item still queued in ROADMAP.
- **AW2's mechanical claim reproduces at HEAD.** All eight named locations
  verified genuinely still two-element / honesty-only (table below).
  `EVIDENCE.md`'s own header was probed as a candidate ninth surface and is
  *already* truth-bar-updated — correctly absent from the list.
- **AW7's term claim reproduces repo-wide.** "Testimony" appears in
  `00-APEX.md` only (plus the glossary entry itself) across README, CLAUDE.md,
  docs/method, docs/build, skills, templates.
- **AW9 spacing survives and is consistent** — the meta-section entries in
  `docs/method/README.md` are uniformly contiguous at HEAD; the later
  economics touch (`86f8530`) edited a disjoint hunk.
- **Every applied hunk survives at HEAD** — applied-text provenance per file
  in the brief; the AW6 preamble sentence and the AW2/AW8 propagation item
  both present verbatim at `9df3510`.

## Findings

### AWA1 (minor) — AW2's "mechanical sweep" list omits the child-template floor block

- **Claim**: the propagation item asserts its surface list makes the sweep
  mechanical, but `docs/build/templates/CLAUDE.md:24` carries a two-element
  apex floor block **byte-identical** to the `PROPAGATION.md` template block
  the list does name — and the build template is the surface that stamps new
  child repos, arguably the highest-impact restatement a propagation sweep
  can miss. A mechanical executor following the named list leaves the
  template stale, and per-child commits could then copy stale text back out.
- **Evidence**: repo-wide grep for apex restatements; `sed` comparison of
  `docs/build/templates/CLAUDE.md:20–32` against
  `docs/method/PROPAGATION.md:100–115` (identical block). The list names
  "`docs/method/PROPAGATION.md:40` + its inlined floor template block" —
  "its" scopes to PROPAGATION's own block, not the build template file.
- **Counsel**: add `docs/build/templates/CLAUDE.md` (floor block) to the
  item's surface list before the sweep runs, and note the two blocks must
  move in lockstep. One-line ROADMAP edit; backlog-safe.

### AWA2 (minor) — AW6's applied rule leaves the landing→queuing window open, and the window bit in its own enacting batch

- **Claim**: the applied preamble rule fires on later commits touching "a
  *queued* delta's" surfaces — but in this very batch the ⏳ pointer was
  created at `9990fc9`, four commits after the application landed at
  `e8d707c`. In between, `86f8530` (economics application) touched
  `docs/method/README.md`, a surface the pointer names. The rule's letter
  never fired (no pointer was queued yet), so at HEAD the pointer's delta
  list names only `e8d707c` while a named surface carries unattributed
  non-AW changes — the exact reviewer-meets-unexplained-text risk AW6 was
  ruled to close. This reviewer had to establish applied-text provenance
  manually (brief, above).
- **Evidence**: `git log --oneline e8d707c..9df3510 -- docs/method/README.md`
  → `86f8530`; `git show 9990fc9 -- docs/ROADMAP.md` → the `[~]`→`⏳` flip;
  ROADMAP at HEAD, delta list `e8d707c` only.
- **Counsel**: close the window either way — (a) queue the ⏳ pointer in the
  application commit itself, making landing = queuing (which `e8d707c`'s
  message already claimed — see AWA4), or (b) extend the preamble sentence to
  cover surfaces touched between an application's landing and its pointer's
  queuing. (a) is cheaper and also repairs AWA4's class.

### AWA3 (LOW) — AW1 bullet now closes a 2026-07-23 sentence with a 2026-07-22 attribution

- **Claim**: the inserted scope sentence (inline-dated "Mike's ruling,
  2026-07-23") is immediately followed by the bullet's original closing
  attribution "(Mike, 2026-07-22.)", which now visually dates the scope
  sentence to the earlier ruling. In a doctrine repo where dated grounding is
  load-bearing (worked cases, ruling provenance), attribution scope should be
  unambiguous; the inline date rescues it, but only for a careful reader.
- **Evidence**: `docs/method/00-APEX.md:139–143` at HEAD.
- **Counsel**: move "(Mike, 2026-07-22.)" to close the pre-existing text
  (before the Scope sentence), or reword to "(bullet: Mike, 2026-07-22;
  scope: Mike, 2026-07-23.)". Wording-sized; rides any next apex-touching
  commit.

### AWA4 (nit) — the application commit's message claims "⏳ queued at landing"; the tree queued it four commits later

- **Claim**: `e8d707c`'s message ends "⏳ queued at landing", but at that
  commit the ROADMAP still carried the old `[~]` AW1–AW9 item; the ⏳
  pointer appeared at `9990fc9`. The record ran ahead of the tree — the
  same claim-vs-evidence discipline the apex holds for prose applies to
  commit messages as records.
- **Evidence**: `git show e8d707c -- docs/ROADMAP.md` (no ⏳);
  `git show 9990fc9 -- docs/ROADMAP.md` (the flip).
- **Counsel**: fold into AWA2(a) — queue in the landing commit and the
  message becomes true by construction. No retro-action possible or needed;
  noted for the batch-application pattern.

## What I re-ran, with results

| Proof | Invocation | Result |
|---|---|---|
| tools test suite | `python3 -m unittest discover -s tools` | ✅ Ran **331**, OK, exit 0 |
| instruments tests | `node --test instruments/*.test.js` | ✅ **150 pass / 0 fail**, exit 0 |
| secretscan | `python3 tools/secretscan.py --root . .` | ✅ exit 0 |
| leakscan | `python3 tools/leakscan.py --root . .` | ✅ exit 0 |
| linkscan | `python3 tools/linkscan.py --root . .` | ✅ exit 0 |
| reviewscan | `python3 tools/reviewscan.py --root . .` | ✅ exit 0 |
| sizescan | `python3 tools/sizescan.py --check --root . .` | ✅ exit 0 |
| AW2 surfaces at HEAD | `sed`/`grep` per named location | ✅ all 8 stale as claimed: root `README.md:57`, `:93`; `PRINCIPLES.md:10`, `:316`; `PROPAGATION.md:40` + block (`:105`); `SKILL.md` description + §1; method `README.md:11` |
| AW2 candidate-miss probe | repo-wide apex-restatement grep | 🔎 one unlisted: `docs/build/templates/CLAUDE.md:24` → AWA1 |
| AW7 term claim | `grep -rn testimony` (method, build, skills, templates, root) | ✅ term in `00-APEX.md` only (+ the glossary entry) |
| AW9 spacing | method README meta section at HEAD | ✅ contiguous, uniform |
| AW6 preamble + propagation item survival | ROADMAP at HEAD | ✅ present verbatim |
| Applied-text provenance | `git log`/`diff e8d707c..9df3510` per delta file | ✅ apex+glossary untouched; README disjoint later hunk; ROADMAP named regions untouched |
| AW6 self-compliance window | `git show 9990fc9`, per-file logs | 🔎 landing→queuing gap → AWA2/AWA4 |
| EVIDENCE.md header probe | `sed -n 1,12p` | ✅ already truth-bar-updated; correctly absent from AW2 list |
| `/security-review` | reach assessment | ⚠️ discharged with grounds (see Lens-4 section) |

---

## Reconcile — deferred material opened after the findings above were committed

*(This section written after opening
`docs/reviews/2026-07-23-0222-apex-widening-cold.md`. Everything above it was
durably written first. No finding above is removed, reworded, or downgraded
here.)*

## Ruling-by-ruling faithfulness

| Ruling | Stamp | Reproduces at HEAD? | Notes |
|---|---|---|---|
| AW1 (MAJOR) | [fixed] | ✅ | The scope sentence Mike agreed verbatim is in the bullet verbatim-or-equivalent, citing `RECORD.md` as where a ruling becomes a decision of record — exactly as counselled and ruled. Residual: AWA3 (attribution placement), cosmetic only. |
| AW2 (minor) | [fixed→backlog split] | ✅ | The applied ROADMAP surface list reproduces the verdict's enumeration **exactly** — every location AW2 named is on the item, and each re-verified stale at HEAD by this pass. AWA1 is a residual of the *original enumeration* (which said "at least seven"), not application drift: the build-template floor block was never on AW2's list, so the applier faithfully reproduced an incomplete list while adding the "sweep is mechanical" claim that AWA1 attacks. |
| AW3 (minor) | [fixed] | ✅ | Cold-review entry matches the counselled shape point for point: spawn criterion, taker-writes-brief, pointer-refs-only, cold-context vs cold-spawn split. |
| AW4 (minor) | [fixed] | ✅ | Doctrine entry marked structural, pointer to `REVIEW.md` rule 3 as functional canon, "single-sourced there" — as counselled. |
| AW5 (minor) | [fixed] | ✅ | Boundary clause applied near-verbatim from the counsel, with a sound added preamble ("One boundary, so this clause never collides…"). Attacked pre-reconcile under lens 4; held. |
| AW6 (LOW) | [fixed] | ✅ | Preamble rule applied as counselled. Residual: AWA2 — the counselled wording's trigger ("a *queued* delta") left the landing→queuing window open, and this batch's own sequence exercised the gap. Faithful application of counsel whose first live window found its edge. |
| AW7 (LOW) | [fixed] | ✅ | (a) concept-spread admission stated in the entry — and re-proven repo-wide by this pass (term in apex only); (b) "may hold a worktree" applied. Both still PROPOSED under the intact SEED banner; ratify item queued. |
| AW8 (LOW) | [fixed] | ✅ | Precondition-clause constraint recorded on the propagation item verbatim-or-equivalent. |
| AW9 (nit) | [fixed] | ✅ | Spacing normalised; meta section uniform at HEAD. |

## Overlap and drift

- **No [fixed] stamp failed to reproduce.** All nine rulings are applied
  faithfully; nothing in the prior verdict is contradicted by this pass.
- **Zero finding overlap with the prior pass** in the strict sense: AWA1–AWA4
  are all new. AWA1 sits on AW2's residual surface (the enumeration's own
  "at least seven" hedge proved apt — this pass found the eighth); AWA2/AWA4
  sit on AW6's applied rule meeting its first live window; AWA3 is the one
  finding that is genuinely application-introduced (the insertion point of
  the scope sentence created the double attribution).
- **Prior-verdict proof drift, benign**: the 0222 pass recorded the tools
  suite at 330; this pass ran 331 — consistent with test growth from the
  since-closed sibling cycles, both OK.
- **The Decisions section's closing line** ("⏳ queued refs-only; the applier
  spawns nothing") is consistent with what the tree shows, with AWA4's
  caveat: the queueing landed at the batch-stamp commit `9990fc9`, not at
  `e8d707c` as that commit's own message claimed.

## Cycle close

This pass returns **no MAJOR**. Per REVIEW.md's close rule, **the
apex-widening cycle is terminal and closes on this verdict** — AWA1–AWA4 are
the principal's to decide into the backlog (rule 3); no further full ceremony
spawns from this application. The reviewer applied nothing.
