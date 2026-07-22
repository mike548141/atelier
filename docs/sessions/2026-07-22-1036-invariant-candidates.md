# Anti-slop invariant candidates — mined from atelier's own review corpus

*Records-only capture (2026-07-22, wt `atelier-antislop-mine`). This is the
**mining half** of the ROADMAP "Anti-slop invariant registry — promotion rule"
item. It produces **CANDIDATES for Mike's per-item approval** — no doctrine
edits, no scanners built, no `docs/method/` changes. The PROPOSED-then-ratify
pattern: decisions are Mike's. Everything below is grounded in real finding IDs;
where a cluster cannot reach three concrete findings it is named below-threshold,
never rounded up.*

## What was mined

The full review corpus — every `docs/reviews/*.md` (brief + verdict, 47 files),
the finding inventories inside `docs/sessions/*.md`, and `docs/ROADMAP-DONE.md`'s
review-cycle summaries — was read in full by five parallel miners and
transcribed to a per-finding inventory (ID, severity, disposition, defect class).

| Source | Findings | Series covered |
|---|---|---|
| `docs/reviews/` 2026-07-10 → 07-11 (10 files) | 113 | A, B, C, E, H, L, N, P, PR, Q, R, V + numbered |
| `docs/reviews/` 2026-07-12 → 07-13 (11 files) | 75 | A, C, F, G, H, I, R + numbered |
| `docs/reviews/` 2026-07-14 → 07-17 (12 files) | 69 | F |
| `docs/reviews/` 2026-07-19 → 07-22 (14 files) | 73 | F, G, N, CF, DD, SR, RS, SL, AC, IR, HI-F, HA, SA |
| **Review corpus (primary)** | **330** | across 47 files |
| `docs/sessions/*.md` + `ROADMAP-DONE.md` sweep | ~0 net-new | HI, HA, SL, AC, IR, N4, plus disposition rows |

**Dedup ruling: review files are primary.** The sessions/ROADMAP-DONE sweep
confirmed almost every finding double-homes — the review file carries the defect
text, the session/ROADMAP row carries the *disposition*. The only clearly
session-primary finding-detail is the **N4 child-CI trigger follow-ups**
(`2026-07-11-31`, deliberately un-reviewed as self-verifying) and the instruments
code-review (whose brief was recovered into a review file). So the deduped unique
count is **≈330 findings across 47 review files**; the sweep is corroboration of
disposition, not additional findings.

Almost every file is PASS-WITH-FINDINGS — there are essentially **no clean
verdicts** in the corpus. That is itself a signal: the review practice bites.

## Clusters (by defect class, not by file)

Counts are cited finding IDs; the promotion rule is **> 2 occurrences (≥ 3)**.
Full ID citations per cluster are in the appendix.

| Cluster (defect class) | Occurrences | Promotable? | Natural seam |
|---|---:|---|---|
| Overclaim vs evidence (claim > evidence, n=1 generalised) | ~30 | ✅ | verifier (= lens 2) |
| Internal contradiction / cross-doc unreconciled | ~18 | ✅ | verifier/checklist |
| Stale-ref / pointer drift / structure-as-documented missing | ~20 | ✅ | scanner (partial) |
| Fail-open scanner / silent-success gate | ~15 | ✅ | scanner selftests |
| Doctrine-change incomplete propagation / unswept mirror sites | ~10 | ✅ | scanner + verifier |
| Missing definition / specification / underdefined scope | ~10 | ✅ | verifier |
| Unverified "live-proven" claim (false at recording commit) | ~9 | ✅ | verifier (= re-run rule) |
| Second-source duplication / one-fact-one-home | ~9 | ✅ | checklist |
| Scope narrowing / silent floor-narrowing on restatement | ~9 | ✅ | scanner + checklist |
| Missing security/privacy lens | ~8 | ✅ | verifier (= lens 4) |
| Detector edge-case / scanner parsing false pos-neg | ~8 | ✅ | scanner selftests |
| Line-wrap / >80-col hygiene in prose docs | 3–4 | ✅ | scanner |
| Missing/mis-attributed provenance | ~3 | ✅ | checklist |
| Record dating: relative / undated / non-UTC | 3 | ✅ | scanner |
| Personal-estate-data leak / instance-in-shareable-layer | ~6 | ✅ | scanner (leakscan) |
| Unguarded crash / code robustness | 3 | ⚠️ single-source | repo checklist |
| US spelling (NZ-English breach) | 2 + 1 bundled | ⚠️ borderline | scanner |

## The candidates — for per-item 🎯 approval

Grouped by proposed **enforcement seam**. Each carries: the declarative rule, the
cited occurrences, the seam (with one line of why), and the proposed home
(atelier-shared floor vs repo-specific catalog). Honest headline up front: **the
two largest clusters are judgement classes that atelier already enforces as
REVIEW lenses** — codifying them is validation of the mechanism (an always-loaded
verifier checklist), not new machine-checks. The genuinely *new* machine-checks
are the four small, sharp scanner candidates.

### CI-scanner candidates (machine-checkable — the new mechanical floor)

> 🎯 **S1 — Line-wrap / column hygiene in prose docs.**
> *Rule:* Markdown under `docs/**` (and templates) wraps prose at the house
> width (~80 cols; ambient tolerance 81–85). A prose line materially over that
> reds. **Exempt:** fenced code, tables, headings, and lines whose overflow is a
> single unbreakable token (URL, path, long identifier).
> *Occurrences (3, an explicit repeat-regression):* `SL7` (2026-07-21-2158),
> `AC1` (2026-07-22-0244, a 122-col line re-shipping SL7's class), `IR3`
> (2026-07-22-0257, "third shipping of the wrap class in three cycles") — plus
> adjacent `conventions-utc-applied F4` (ragged wraps).
> *Seam:* **CI scanner** — trivially machine-checkable, and the corpus shows it
> shipped three cycles running *because* nothing mechanical caught it.
> *Home:* **atelier-shared floor** (all `method/` docs, fleet-wide).

> 🎯 **S2 — Structure-as-documented: a named path/dir/file must resolve.**
> *Rule:* A doc that names a repo path — a directory, a file, a template dir —
> must have that path exist, whether the reference is a markdown link *or bare
> prose*. **Exempt:** inline-code'd examples, deliberately-stubbed future paths
> marked as stubs.
> *Occurrences (≥3):* `foundation H2` (README lists `docs/decisions/`, absent),
> `post-method B14` (MAJOR — ACCESS points at an estate map ros doesn't hold),
> `post-method B11` ("seed from `templates/`" — none existed); related
> `foundation H3` (fabricated quotation attributed to AUTONOMY).
> *Seam:* **CI scanner**, extending linkscan — which already resolves markdown
> *links* (see already-enforced) — to bare prose paths. The fabricated-quote
> subset stays review-only (not mechanisable).
> *Home:* **atelier-shared floor.**

> 🎯 **S3 — Absolute-UTC dating discipline in records.**
> *Rule:* Dated records state ISO-8601 absolute dates stamped from `date -u`; no
> relative-time words ("today", "yesterday", "last week"); a dated maintenance
> edit carries its date. **Exempt:** quoted external text, prose *about* relative
> time.
> *Occurrences (3):* `communication C3` (worked example an undated copy, breaks
> the doc's own dating rule), `concurrency-put-away 3` (tag convention omits the
> absolute date RECORD mandates), `conventions-utc-applied F2` (a default
> re-declared without dating it). Adjacent, same UTC root, different surface:
> `instruments 1` (MAJOR — a timezone-fragile test straddling local midnight).
> *Seam:* **CI scanner** — a relative-time-word denylist + ISO/UTC check over
> `docs/**` is cheap and precise. (Corroborated by the standing at-rest-dating
> correction that cost a 5-file sweep.)
> *Home:* **atelier-shared floor.**

> 🎯 **S4 — Inlined-floor / child-template restatement must match its canonical
> parent (stamp-drift).**
> *Rule:* Where a child repo or template inlines a floor/pull-quote of canonical
> doctrine, the inlined block must equal the parent's canonical text (or
> legitimately *narrow* it — never silently drop or contradict an item). A drift
> reds.
> *Occurrences (≥3):* `create-repo C3` (nothing keeps the stamped block equal to
> PROPAGATION's canonical text), `method-layer P1` (inlined floor drops "new
> trust surfaces" — silent narrowing), `foundation Q2` (pull-quote lists 4 of 6
> floor items), plus `CF4`/`IR2`/`SL1`/`HI-F4` (child templates and skills left
> behind by a doctrine change).
> *Seam:* **CI scanner** — a genuinely new mechanism: hash/compare the stamped
> block against the pinned parent text. This is the mechanical half of the
> propagation-sweep discipline (V3).
> *Home:* **atelier-shared floor** (the stamping is a create-repo/PROPAGATION
> concern).

> 🎯 **S5 — NZ-English spelling (borderline; cheapest scanner).**
> *Rule:* `docs/**` uses NZ-English spelling (artefact, organise, licence,
> synthesise, colour…). **Exempt:** quoted external text, third-party proper
> nouns, identifiers/APIs (`artifact` in a tool name).
> *Occurrences:* **2 dedicated findings** — `foundation Q6` ("synthesize"),
> `SA9` ("artifact") — **plus 1 bundled** mention (`model-economics F6`, "old
> spelling" in a child template). **Honest count: borderline 3.** It sits below a
> clean promotion, *but* a spot-check found "artifact" 15+ times across `method/`
> docs (RECORD, SECRETS, SIGNING, PRINCIPLES…) despite the NZ-English rule — so
> the class is **under-detected, not rare**, which is exactly what a scanner
> surfaces. Promote on ROI, not on finding-recurrence, and only if Mike agrees
> the finding count is thin.
> *Seam:* **CI scanner** (wordlist). *Home:* **atelier-shared floor.**

### Agent-verifier / review-checklist candidates (judgement — the always-loaded catalog)

These are the ROADMAP's "two-layer acceptance criteria" idea: per-change criteria
plus a catalog the verifier loads unasked. Most are **already REVIEW/​APEX
doctrine** — the candidate is to *codify them as an explicit always-run checklist*
so no reviewer has to remember them, not to invent a new rule.

> 🎯 **V1 — No claim stronger than its evidence** (the single largest cluster,
> ~30). Occurrences incl. `method-layer PR1`, `post-method B7`, `child-ci N4`,
> `signing G5`/`G8`, `principles-s2-four-bullets F1`, `cli-docs-standard F4`,
> `CF1`, `IR1`, `HA2`/`HA4`. *Seam:* **agent-verifier criterion** — this is APEX
> honesty + REVIEW lens 2; not mechanisable, highest value as an always-loaded
> check. *Home:* **atelier-shared floor.**

> 🎯 **V2 — Re-run every recorded "live-proven"/"verified" claim in scope**
> (~9). `post-method B1`, `signing G1`/`G2`/`G3`, `create-repo C2`,
> `principles-s2-four-bullets F2`, `cli-docs-standard F7`, `F1` (0407). *Seam:*
> **agent-verifier criterion** — already REVIEW "Re-run every live-proven claim";
> codify as a catalog line. *Home:* **atelier-shared floor.**

> 🎯 **V3 — Doctrine-change propagation sweep** — an edit to a canonical rule
> sweeps every mirror site (child templates, skills, sibling docs, READMEs)
> (~10). `conventions-utc F1` (MAJOR), `conventions-utc-applied F1`,
> `review-rule4-cold F3`, `F3` (0407), `CF4`, `SL1`, `SL3`, `IR2`, `HI-F4`,
> `HA3`. *Seam:* **verifier criterion + S4 scanner** for the template subset.
> *Home:* **atelier-shared floor.**

> 🎯 **V4 — One fact, one home** (no second-source duplication) (~9). `foundation
> A3`, `create-repo C3`/`C8`, `instruments 8`/`9`, `review-rule4-cold F4`,
> `informed-principal F7`, `N1` (0629), `SA7`. *Seam:* **review-time checklist**
> — duplicated normative prose is judgement, not a regex. *Home:*
> **atelier-shared floor.**

> 🎯 **V5 — Internal-contradiction / cross-doc reconciliation** (~18). e.g.
> `reach-rereview A4`/`A6`, `review-independence I4`/`I7`, `independence-batch
> G2`/`G5`, `reach-batch H3`/`H7`, `review-doctrine F2`/`F5`, `CF2`, `SL5`.
> *Seam:* **review-time checklist**. *Home:* **atelier-shared floor.**

> 🎯 **V6 — Security & privacy lens on every review** (~8). `create-repo C9`,
> `reach-rereview A2`, `signing G7`/`G10`, `reach-batch H2`/`H4`,
> `principles-s2-four-bullets F4`, `SA1`. *Seam:* **agent-verifier criterion** —
> already REVIEW lens 4 (Mike's 2026-07-21 ruling) + `/security-review` where
> reachable; codify as a mandatory catalog line. *Home:* **atelier-shared floor.**

> 🎯 **V7 — Rule-4 spawn-provenance present** on self-authored-doctrine reviews
> (3). `review-rule4-cold F5` (no provenance hook), `F9` (0407, missing
> provenance), `F4` (0407, mis-attributed provenance). *Seam:* **review-time
> checklist** (partly mechanical — a verdict-file field, reviewscan-adjacent).
> *Home:* **atelier-shared floor.**

## Already effectively enforced (validation of the mechanism, not new work)

Four clusters are already held by an existing scanner — the promotion rule is
*validating* these mechanisms, not proposing new ones:

- **Personal-estate-data leak** (~6: `foundation L1`/`L2`, `method-layer L1`
  "13 devices", `record-private R2`/`R3`) → **`leakscan`** (structural + literal
  denylist). Residual the scanner *cannot* hold, by its own premise: the
  name-to-posture *join* (`record-private R2`/`R3`) — review-time only, exactly
  as RECORD.md states.
- **Broken internal links** → **`linkscan`** (the `linkscan L1–L10` findings were
  the scanner's own hardening; the *class* is now mechanically held). S2 proposes
  extending it to bare prose paths.
- **Decision record missing a `review:` line** → **`reviewscan`** (closing
  2026-07-19 F6; `RS1–RS4` hardened it). Note the deliberate non-cover: roadmap
  headings are *not* linted (the 0820 ruling), so V-side review lines there stay
  conventional.
- **Cold content on the hot path / botched harvest** → **`sizescan`** (`--check`
  gates completed `[x]` items and live markers in archive stores;
  `size-rebalance`/`harvest-integrity` findings hardened it).

⚠️ **Fail-open / detector-edge is a caution, not a clean win.** The
fail-open-scanner and detector-edge clusters (~23 combined) *are* partly held by
the `tools/test_*.py` selftests and `floor.yml`'s selftest step — yet the class
**kept recurring even with tests present** (`RS1`, `SL2`, `HI-F1`, `G1` at 0544
all post-date the selftest discipline). Honest reading: the mechanism exists but
is under-covered; the remedy is stronger selftest/fuzz coverage in `tools/`
(repo-specific), not a new fleet invariant.

## Below-threshold — named honestly, not promoted

- **US spelling** — 2 dedicated findings (+1 bundled). Carried in S5 as an
  ROI-justified exception with the count stated plainly; below the finding-
  recurrence bar on its own.
- **Unguarded crash / code robustness** — 3 findings (`instruments 4`/`5`/`6`)
  but **all from one review of one codebase in one session**. Meets the number,
  fails the spirit ("recurring across the corpus"): it is a single incident.
  Belongs in a **repo-specific (instruments) code-review checklist**, not fleet
  doctrine.
- **False mechanism** (2: `claiming-work 2`, `concurrency-claiming 6`),
  **fabricated quote** (1: `foundation H3`), **adopter-applicability cliff** /
  **terminology conflation** (adopter-facing judgement, scattered) — all real,
  none reaches a clean 3 as a distinct promotable class.

## How the registry would be checked — PROPOSALS (the ROADMAP's open questions)

Answering the ROADMAP's *enforcement-seam* and *where-does-it-live* questions, as
proposals only:

1. **Seam decision rule (code-checkable vs judgement).** A candidate is a
   **scanner** only if a clean "does it match / does it exist / is it over N
   cols / is the word on the list" decides it with no judgement — S1–S5. Anything
   needing "is this claim honest / does this contradict that / did the sweep
   reach every site" is a **verifier/checklist** — V1–V7. This is the existing
   spectrum (leakscan-class ↔ review-time ↔ human), applied per candidate.
2. **Registry home — both layers, mirroring doctrine.** An **atelier-shared
   floor** (the fleet-wide invariants — S1–S5, V1–V7, same layer as the current
   scanners and REVIEW lenses) plus **repo-specific catalogs** appended locally
   (a child's own conventions; the instruments code-robustness checklist above is
   the first). Same shape as PROPAGATION's thin-anchor/fat-pointer: shared floor,
   local append, child may narrow-not-contradict. Ties REPO-STANDARD.
3. **One verification pass.** The scanner candidates run in the pre-commit hook +
   CI alongside the existing four (`secretscan`/`leakscan`/`linkscan` + the
   pre-publish `licenscan`), fail-closed like them. The verifier candidates load
   as a standing checklist the reviewer runs unasked — the article's "the catalog
   enforces the org rule without the author remembering it" — assembled with the
   per-review brief's task-specific questions into one pass.
4. **Governance.** Each promoted invariant is self-authored doctrine by function
   (it governs future agent behaviour), so promotion from candidate → live
   invariant is **Mike's ruling**, and the doctrine edit that lands it earns a
   rule-4 `⏳` cold pass — exactly the ADR-style path this capture defers to.

*review: this capture is records-only (no doctrine edited) — a review is
**WARRANTED** on any candidate Mike promotes to a doctrine edit or a built
scanner, per the item above, not on the capture itself.*

## Surprises in the corpus

- 🔎 **The biggest recurring defect class is the one atelier already enforces
  best.** Overclaim-vs-evidence (~30) and the live-proven-claim family (~9) are
  APEX honesty + REVIEW lens 2 / the re-run rule. The mining validates the
  doctrine rather than exposing a gap — the highest-frequency findings are caught
  *because* the practice looks for them.
- 🔎 **The same wrap defect shipped three cycles running** (`SL7`→`AC1`→`IR3`),
  each fix re-introducing the next — the clearest case in the corpus for a cheap
  mechanical gate replacing a judgement the reviewer kept having to re-make.
- 🔎 **"artifact" is pervasive despite the NZ-English rule** — 15+ times in
  `method/`, only twice caught as a finding. The invariant idea's whole premise
  (a scanner catches the convention the eye skips) is visible in one word.
- 🔎 **Fail-open kept recurring after the selftest floor existed** — a caution
  that a mechanism's *presence* is not its *coverage*; the honest disposition is
  "harden the existing tests", not "declare it solved".
</content>
</invoke>
