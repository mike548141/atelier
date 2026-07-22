# Changelog

All notable changes to atelier. Format: [Keep a Changelog](https://keepachangelog.com/);
newest first. Everything stays under _Unreleased_ until there's a reason to tag.

## [Unreleased]

### Added (2026-07-22 — orchestrated queue run: ten items landed per-item)
- **The queue-run pattern is doctrine + a bundled skill** (`343def8`,
  `8111e9f`): CONCURRENCY § Orchestrated queue runs (role check, selection
  order, per-item close as the cap-safety property, four stop conditions,
  rule-4 synergy) + ECONOMICS § the orchestrated-run tier split +
  `skills/queue-run` (auto-discovered like review-brief). Mike's hand-carried
  run prompt is retired. Self-authored doctrine — rule-4 `⏳` queued; the
  authoring run may not take it. Built by the run *while running the
  pattern*, so its intent record is also the delta's second bearing.
- **ccarchive grew its missing half**: `--restore` full + delta off the
  audit buckets, content-first safety (`9ca1425`); iCloud dataless awareness
  — verify/audit skip evicted files, `--materialise` opts in, classifier
  proven on a real evicted file (`12794d6`); manifest signing — detached
  HMAC-SHA256, off-archive key, `--rekey`, five honest verify states, the
  rewrite-gz-and-manifest caveat closed and proven live (`2a85839`).
  Instruments suite 109→132.

### Changed (2026-07-22 — queue run, continued)
- **`MODEL-ECONOMICS.md` → `ECONOMICS.md`** (Mike's decision executed,
  `b639513`): `git mv` on canonical + child-template copies, 24 refs across
  16 live files, history untouched; children re-point at their next pin
  bump; ros keeps its private counterpart's name by its own recorded call.
- **ccrepo dedup keeps the richest record, not the last** (`75bba4c`): the
  logs re-emit messages with trailing zeroed usage lines; last-wins silently
  dropped tokens. Sonnet-5 drift → 0.00% (exact ccusage match on frozen
  data); `server_tool_use` measured all-zero, its pricing hypothesis
  retracted; per-model reconcile scoped to matched sessions.

### Reviewed / recorded (2026-07-22 — queue run, continued)
- **SECRETS/ACCESS `⏳` cold pass taken and closed** (rule-4 provenance on
  the record): PASS-WITH-FINDINGS 0M/4m/4L/1n, terminal; 🎯 SA1–SA8 to Mike
  (`reviews/2026-07-22-1021-secrets-access-cold-pass.md`).
- **Security canon mapped against `method/`**
  (`sessions/2026-07-22-1025-security-canon-gap-map.md`): gaps A/B/E
  confirmed narrow, C reframed (zero-dep is the control; residual =
  mutable-tag CI actions), D dismissed; doctrine-edit follow-up queued.
- **Anti-slop invariant candidates mined from the whole review corpus**
  (330 findings, 47 files —
  `sessions/2026-07-22-1036-invariant-candidates.md`): 5 scanner + 7
  verifier candidates for Mike's per-item approval; the wrap class shipped
  three cycles running; fail-open recurrence flagged as only-partly-held.
- **Both cc-instruments open questions answered with measurement**
  (`sessions/2026-07-22-1050-cc-instruments-questions.md`): tool-result
  sidecars are a real capture hole (~7% of volume, CAPTURE recommended);
  cctranscript/ccarchive merge counselled against (~10 shared lines;
  schema-immunity must not couple to a schema-fragile parser).

### Changed (2026-07-22 — floor: sibling worktrees out of scanner reach)
- Mid-records-commit, linkscan redded on a **sibling session's** freshly
  created nested worktree (`.claude/worktrees/…`, an in-flight dangling
  link) — another session's mid-flight tree must never gate this one's
  commits. `.linkscanignore` + `.sizescanignore` now exclude
  `.claude/worktrees/**`, the same nested-worktree class `.gitignore`
  already fences for `git add -A`; the sibling's files untouched
  (CONCURRENCY's never-work-around-a-stranger rule).

### Changed (2026-07-22 — HA1–HA5 ruled and applied: skip classes split, fence recount whole-file)
- **Mike accepted all five terminal-pass findings as counselled**; applied
  in `120b777`. `SKIP_DIR_NAMES` split into `NON_CONTENT_DIR_NAMES` (VCS
  internals, vendored code, venvs, caches — never scanned at all) and
  `STORE_DIR_NAMES` (metering bounded, integrity checked per HI-F1), so a
  vendored store-named file no longer reds the build. Unbalanced fence
  delimiters at EOF now recount the whole file with fences ignored — the
  true "as if no fence ever opened" semantic; the stray-delimiter window
  that silently hid a marker is closed and the comment claims exactly what
  the code does. Both CI surfaces name the harvest-integrity gate; the
  template legend reads finished-state-items-only; RECORD.md's trigger
  sentence re-anchors. Proof: suite 319→323; red leg reds exactly the four
  new tests; both live probes re-driven; selftest + live scan green.
  Residue [x]'d and harvested to DONE same session — queue empty.

### Reviewed (2026-07-22 — HI application cold pass: 0 MAJOR, cycle CLOSED)
- **The queued rule-4 pass on `30d350c` ran and closed the
  harvest-integrity cycle** (taker: a Mike-spawned "do any review work"
  session, author of none of the chain; verdict + reconcile:
  `reviews/2026-07-22-0943-hi-application-cold.md`). Every recorded proof
  re-ran green — suite 319, selftest, live scan, the red leg re-driven at
  `30d350c^` (exactly the four new HI tests go red) — and all six [fixed]
  stamps corroborated independently before the deferred material was
  opened. **PASS-WITH-FINDINGS 0M/2M/3L**, decided into the backlog for
  Mike (rule 3): HA1 — the HI-F1 bypass over-reaches its class (a
  store-named file under `node_modules/`/`.venv/` reds `--check`, probed
  live); HA2 — the unclosed-fence fix narrows its fail-open rather than
  closing it (a marker between a stray delimiter and a later fenced
  snippet is silently cleared; the comment's "never hide one" overclaims);
  HA3–HA5 — CI comments still cold-content-only, template-legend
  "exactly this grammar" overclaim, RECORD.md antecedent drift. Reconcile
  traced HA1 to the 0819 counsel itself (applied faithfully — the
  laundered-through-counsel class). Terminal per the close rule; no
  further ceremony. The stale interruption-resilience ROADMAP section
  (drafting long delivered) was harvested with the close.

### Changed (2026-07-22 — HI-F1–F6 ruled and applied: integrity checked wherever a store lives)
- **Mike accepted all six cold-pass findings as counselled**; applied in
  `30d350c`. The MAJOR's fix: archive-store basenames now bypass the
  growth-store directory skip — `SKIP_DIR_NAMES` bounds *metering*, never
  integrity, so a `*-DONE.md`/`*-ARCHIVE.md` under `sessions/`, `_archive/`,
  etc. gates like any other. An unclosed fence no longer swallows the rest
  of a file (the shared counter counts the tail, fail-safe, both grammars in
  parity). `RECORD.md` now names the harvest-integrity gate beside the
  cold-content gate; the child ROADMAP template teaches the tri-state
  pre-hoc; the blockquote skip and indented-code edge are documented as
  decisions. Proof: suite 314→319; both original fail-open repros re-driven
  red→green; live scan green. Application is a doctrine edit by the
  verdicts' author ⇒ its own cold pass queued `⏳` (rule 4).

### Reviewed (2026-07-22 — harvest-integrity gate cold pass: 1 MAJOR, cycle stays open)
- **The queued rule-4 cold pass on `0bdccf3` ran** (taker: a Mike-spawned
  "do any review work" session; verdict
  `reviews/2026-07-22-0819-harvest-integrity-gate-cold.md`). Every delta
  claim reproduced — suite 314, selftest, live scan, the four-situation
  taxonomy, tri-state coherence, hatch behaviour. **PASS-WITH-FINDINGS
  1M/3M/2 notes**: the MAJOR (HI-F1) is a latent fail-open — archive
  stores inside skipped dirs (`sessions/`, `_archive/`…) are invisible to
  the gate while the clean banner claims coverage; reproduced, no live
  incident (all five fleet repos keep stores at `docs/`). MINORs:
  unclosed-fence swallow (HI-F2), RECORD.md's account now incomplete
  (HI-F3), child template lacks the tri-state legend (HI-F4). 🎯
  HI-F1–F6 await Mike's ruling; the MAJOR keeps the cycle open
  (ruling → application → application's own `⏳`).

### Added (2026-07-22 — harvest-integrity gate: the archive must hold no live state)
- **sizescan now checks archive stores** (`*-DONE.md`, `*-ARCHIVE.md`) for
  live state markers — `[ ]`/`[~]`/`⏳` list items gate under `--check`,
  the same fail-safe contract as cold content (Mike's ratified design,
  embedded in CI for free via the floor's existing step). State coherence
  only — never `[x]`-delivery verification. On a hit the output prescribes
  investigate → recommend to the principal → never silently fix. The box
  grammar is ruled a **work-owed tri-state**: `[x]` = no more work owed
  (delivered / superseded / declined — disposition in the item's dated
  note). Suite 302→314; review queued `⏳` (rule 4).

### Decided (2026-07-22 — MODEL-ECONOMICS.md will become ECONOMICS.md)
- **Rename to `ECONOMICS.md`, do not split** (Mike's ruling, accepting the
  standing recommendation): the file spans both spend pools (model tokens
  and CI compute/runners) and its precedence/self-check doctrine is
  cross-cutting, so one unified spend doctrine keeps its point. `FinOps`
  was floated and ruled out — a branded cost-accounting practice term for
  what is spend *doctrine*, and jargon on a shelf of plain concept nouns.
  Execution (rename + PROPAGATION ref sweep) stays queued; nothing renamed
  yet. Roadmap item carries the DECIDED stamp and the FinOps reasoning.

### Changed (2026-07-22 — interruption-resilience doctrine reviewed; scope/lens-4 residue applied)
- **The interruption-resilience cycle closed same-day**: `9c11525`'s rule-4
  cold pass returned **PASS-WITH-FINDINGS 0M/3M/2L** — terminal per the
  close rule. Notable: the onramp tell was live-falsified during the review
  (a live sibling session matches the "died mid-flight" signature — IR1),
  and the authoring session's un-harvested `[x]` had the shared floor red
  on `main` for three pushes (IR5, fixed + re-proven green by the reviewing
  session). **IR1–IR4 ruled same day ("I take your recommendations") and
  applied**: the onramp tell now reads died-**or-still-live** (sweep before
  assuming either), the child template carries the firing pointer, wraps and
  legend fixed. A new **harvest-integrity invariant** was captured from the
  incident's follow-on question (no live checkbox in ROADMAP-DONE; counsel:
  extend sizescan) — its first manual run caught and corrected a `[ ]`
  parent whose children were both DONE.
  Verdict: `docs/reviews/2026-07-22-0257-interruption-resilience-cold.md`.
- **AC1–AC2 applied on the principal's accept-both**: the CONTRIBUTING
  template's 122-col line rewrapped; the review-brief skill's scanner
  clause now carries the exclusion-barred caution. Suite 302 green.

### Changed (2026-07-22 — reviewer scope mandated; security & privacy is lens 4)
- **Review scope is the whole commitment, and security & privacy is a must
  on every review** (Mike's rulings, 2026-07-21): `REVIEW.md` gained a scope
  mandate above the lenses (intent, decisions, assumptions, design, docs,
  code, tests, real-world behaviour — live where possible, with grounds when
  not; non-goals the only legitimate narrowing, and the narrowing itself
  reviewable) and **lens 4 — security & privacy** (design-altitude privacy
  weakness through code-altitude injection/XSS/authn/secret handling; likely
  vectors checked against OWASP Top 10/ASVS, not recalled; harness security
  scanners used reach-per-review-shape as the floor under the lens, never a
  discharge of it). The rule-4 cold pass on the delta (a fresh-context
  subagent, two-hop spawn) returned **PASS-WITH-FINDINGS 2M/3M/2L** — the
  MAJORs live-proven by the pass itself — and Mike's accept-all landed
  SL1–SL7: the review-brief skill now carries all four lenses with a
  **mechanical lens-roster parity floor** (LensRosterParityTest; suite
  298→302, red leg proven), the scanner clause states the
  never-scan-a-brief and exclusion-barred-class cautions, and the child
  templates are swept. Cycle **closed 2026-07-22**: the application's own
  rule-4 cold pass returned **PASS no MAJOR** — terminal per the close rule
  (suite 302 OK reproduced, red leg re-driven, scanner discharged with
  grounds under its own new reach-per-shape rule); two LOW residues
  (AC1 wrap line, AC2 skill compression loss) to the backlog for Mike.
  Verdict + decisions:
  `docs/reviews/2026-07-21-2158-review-scope-security-lens4-cold.md` and
  `docs/reviews/2026-07-22-0244-sl-application-cold.md`.

### Changed (2026-07-21 — REACH/AUTONOMY backlog closed: H1–H7 + R1 applied on Mike's accept-all)
- **`REACH.md` tightened on the seams its own 2026-07-13 no-MAJOR pass named**:
  riding a session is scoped to *in-place* use through the ridden session
  (exporting cookies/tokens is touching the store — H2); the two boundary
  tests scoped — purpose governs stores, mint-vs-ride governs acts, and a
  saved-login autofill is a mint whatever the store's purpose (H3);
  operator/principal defined with the team-adoption rule (H1); the
  resource-owner's "no" named as its own judgement with its own floor (H4);
  "blocked" defined incl. soft blocks (H5); rung-1/2 equivalence hedged to
  the worked instance (H6); standing reach joined to the provisioned path
  (H7). **`AUTONOMY.md`** secrets floor now catches machinery-mediated
  *unprovisioned use*, not only direct handling (R1). The browser-fetch
  README mirrors H2. Terminal application of a no-MAJOR pass ⇒ no further
  pointer; decisions stamped in the verdict's addendum.

### Changed (2026-07-21 — review-line cycle closed: RS1–RS6 accept-all applied)
- **The reviewscan cycle is closed terminal.** The rule-4 cold pass on the
  artefact delta returned **PASS — 0 MAJOR / 1 MEDIUM / 5 LOW**; Mike ruled
  accept-all and the counsel's author applied (no-MAJOR ⇒ terminal, no further
  pointer). reviewscan now scans an explicitly-named decisions dir or record
  file directly (RS1 — the silent-success hand-run closed, red legs proven),
  ignores `review:` lines quoted inside code fences (RS2), requires a
  non-empty value (RS3), accepts all-caps and states the backdate residual
  (RS4); REPO-STANDARD points at `tools/README.md` for the scanner roster
  instead of an inline list that had gone stale three scanners running (RS5);
  the 0820 record's spliced addendum is unwound with the restoration
  annotated (RS6). Suite **293→298**. Verdict + decisions:
  `docs/reviews/2026-07-21-0913-review-line-artefact-cold.md`.

### Added (2026-07-21 — the review-line artefact: templated field + reviewscan)
- **The `review:` line is now structural for decision records.** The ADR
  template and decisions README carry a **Review** field, the ROADMAP template
  states the convention for direction-setting entries, and the new
  `tools/reviewscan.py` (pre-commit + CI + child `floor.yml`) reds a decision
  record dated ≥ 2026-07-21 that omits the line — presence only, scoped to
  `docs/decisions/`, roadmap headings deliberately unlinted (the 0820 record's
  grounds). Closes 2026-07-19 cold-pass **F6**: `REVIEW.md`'s "enforcement is
  structural" claim is re-stated per surface — mechanical for decision
  records, honestly conventional for roadmap sections. Suite **284→293**.
  Deliberation: `docs/decisions/2026-07-21-0744-review-line-artefact.md`.
  Doctrine delta ⇒ ⏳ rule-4 cold pass queued.
- **Fleet re-stamp of the reviews template** (the unblocked ROADMAP item):
  nova, numen, shed — the three children carrying the drifted pre-trigger
  copy — re-stamped from the closed-cycle template, `<atelier-path>` filled,
  stamp grep + pointer resolution proven per child, pushed.

### Added (2026-07-21 — man pages for cctranscript + ccrepo; convention rollout closed)
- **`cctranscript` and `ccrepo` now ship a `man/<tool>.1` + trimmed `--help`**,
  closing the man-page convention rollout the CLI-docs standard opened (`ccarchive`
  was the reviewed worked example). Every CLI the installer publishes to `PATH`
  now documents itself in both registers: a full plain-language `man` page (the
  superset — what/why, every option, FILES/EXAMPLES/EXIT STATUS/NOTES, `mandoc
  -T lint` clean) and a concise `--help` digest pointing at it (cctranscript
  42→24 lines, ccrepo 67→35; rationale + worked examples relocated into the page
  so the two can't drift). EXIT STATUS is enumerated against every `process.exit()`
  path in each source (the drift a prior ccarchive review caught, designed out
  here). +6 doc-convention tests (92 instrument tests green). Installer needed no
  change — it already globs `man/*.1`.

### Changed (2026-07-20 — sizescan: line-count budget → cold-content gate)
- **`sizescan` now gates on relocatable cold content, not line count** (Mike's
  2026-07-20 ruling; reverses the 2026-07-19 budget gate). Cost is size ×
  read-frequency, so `--check` fails only on a completed `[x]` item on the hot
  path (a checkbox-worklog file — `ROADMAP.md`), whose fix is a lossless move to
  `ROADMAP-DONE.md`. Line count is demoted to a pure **advisory** — a class
  reference point that reports but never fails a build — so a file long purely
  from live current-truth is never penalised and the number can't induce
  line-golf. Prose-shaped cold content and thinness stay caught at review, not
  measured. The static `GATED` set is gone (gating is content-driven). Hatches:
  `sizescan:allow` exempts a file fully; `sizescan:budget=N` quiets the size
  advisory only, never the gate. Suite **267→282**; `ci.yml` + `floor.yml`
  retitled to the cold-content frame; `RECORD.md` module doc updated. `main`'s
  floor is green by harvesting 4 `[x]` items, not trimming lines.
- **`PROPAGATION.md` child-block size spec — structural rule, no line figure**
  (SR2 → SR2-C). The dead "~15 lines" figure was first replaced with "~50 lines",
  then **that number was dropped too** on review: it sat at measured-49+1,
  circular by the delta's own standard. The structural rule (one bullet per
  irreducible floor concern, seven today) is the whole spec; nothing gates on
  length here.
- **Cycle closed 2026-07-21.** The rework was queued for independent rule-4
  review (author did not self-review); it **RAN — PASS, 0 MAJOR / 2 MEDIUM /
  3 LOW** (`reviews/2026-07-20-2040-size-rebalance-cold.md`), Mike ruled
  accept-all, and the taker applied all five findings as a terminal application:
  SR1 (tools/README rewritten to the cold-content frame), SR2-C (figure dropped,
  above), SR3 (detector edges: code-fence false positive + `+`/ordered-bullet
  misses — suite **282→284**), SR5 (rule-4 refs-only pointer ceiling stated in
  the ROADMAP header at point of use), SR4 (accept-as-noted — immutable record,
  correction in the verdict).

### Changed (2026-07-20 — triple doctrine cycle closed terminal; DOCUMENTATION ratified)
- Three queued rule-4 cold passes ran in one taker session ("do any reviews
  waiting") and all returned **PASS, 0 MAJOR**; Mike ruled every counsel
  accepted ("1–3 I accept your recommendations") and the taker applied them
  as a terminal application (`87af9f9`) — no further pointer, per the close
  rule. Verdicts + decisions:
  `docs/reviews/2026-07-20-1355-{concurrency-flip,onramp-rhythm,documentation-draft}-cold.md`.
- **`method/DOCUMENTATION.md` is now ratified doctrine** (new, entry 15): the
  Diátaxis × consumer matrix, artefact inventory, five principles, the
  vendor-docs seam. Review fixes: developer column added to the
  great-per-cell table (DD1), centre-of-gravity qualifier on the mode↔audience
  mapping (DD2), tests/commit-messages/diagrams added to the inventory (DD3);
  the cold pass stands as the competing-draft counterweight (DD4 — none was
  ever opened). Every grounding claim re-verified at ros `806eb10`. tiki
  application half lives in ros.
- **`method/CONCURRENCY.md`** — the "assume you are not alone" flip refined:
  the solo default owns its trade (evidenced-alone pays nothing;
  alone-but-unevidenced buys near-zero-cost insurance; evidence is
  affirmative, never an absence — CF1/CF5); the cues are discovery-only,
  silence licenses nothing (CF2); new dirty-primary claiming rule (CF3); new
  § **Stay in your lane** — the standing "focus on given work" instruction
  finally has a home doc (SR1).
- **Child doctrine block** (`PROPAGATION.md` + `build/templates/CLAUDE.md`,
  parity re-proven, suite 20 OK): Concurrency bullet caught up to the flipped
  prior (CF4); Session-rhythm cue scoped to the shared queue (SR3), lane
  clause pointered, "final verdict" → "declare the work wrapped" (SR4). The
  dead "~15 lines" block spec replaced with the class-grounded lean rule;
  numeric re-grounding queued into the size-signal rebalance (SR2). Children
  adopt at pin bump.

### Changed (2026-07-19 — the review cycle closed terminal, no MAJOR)
- The queued cold review of the G1–G3 application ran: **PASS — 0 MAJOR ·
  0 MEDIUM · 0 LOW + 1 note**
  (`docs/reviews/2026-07-19-0629-g1g3-application-cold.md`), every recorded
  proof re-run independently (suite 275; G1's red/green legs on a full
  scaffold; G2's bite; G3's claims) and the reconcile clean. First no-MAJOR
  pass ⇒ terminal; Mike ruled the cycle **closed** and N1 accepted as named
  (create-repo's machine-local vocabulary copy — sync test rides with any
  future plugin-bundle shipping). The fleet re-stamp's hold is lifted;
  nothing applied, so no further pass queued.

### Changed (2026-07-19 — the applied-batch cold pass ruled and applied, G1–G3)
- The queued cold review of the F1–F9 application ran: **PASS-WITH-FINDINGS,
  1 MAJOR · 0 MEDIUM · 1 LOW + 1 note**
  (`docs/reviews/2026-07-19-0544-combined-applied-batch-cold.md`); Mike ruled
  all three as counselled. The application itself verified clean — all nine
  rulings applied exactly as ruled, the F2/F4 addenda independently
  fact-checked. Applied: **G1** the `floor.yml` template's pin slot reworded
  out of placeholder vocabulary — its `# ref: <SHA>` comment made the
  create-repo whole-tree prove-the-stamp grep unsatisfiable on every full
  scaffold, so the grep's green state now exists; re-proven both legs on a
  full scaffold. **G2** `test_templates.py` gains the set-wide
  placeholder-inventory pin (stamp tokens only where the stamp step fills
  them; suite 274→275, bite-proven). **G3** one-line addendum on the 0820
  record pointing at the F6 qualification.
- ⚠️ **One claim in the entry below is corrected** (G1 — dated addenda on the
  0407 verdict's F1 stamp and the 0407 session log; the originals stand): the
  F1 fix's "re-proven red and green in scratch" green leg held only on a
  partial tree without `floor.yml`; on the standard scaffold the grep could
  not go green until this entry's pin-slot reword. The F1 fix itself stands.

### Changed (2026-07-19 — the combined cold pass ruled and applied, F1–F9)
- The queued cold review of the two entries below (+ the sizescan doctrine
  deltas) ran: **PASS-WITH-FINDINGS, 3 MAJOR · 3 MEDIUM · 3 LOW**
  (`docs/reviews/2026-07-19-0407-review-trigger-sizescan-combined-cold.md`);
  Mike ruled all findings as counselled (F1–F8 fixed, F9 accepted). Applied:
  **create-repo** now fills `<atelier-path>` in every stamped file and its
  prove-the-stamp grep covers the whole tree, re-proven red and green in
  scratch (F1); **`skills/review-brief`** re-keyed to the commitment trigger
  with a stamped-copy header — the consolidation sweep had missed `skills/`
  (F3); the sizescan gate-class wording states its honest edge — an all-current
  file has nothing to move; ground a budget or accept a standing red (F5, in
  `tools/sizescan.py` + the `floor.yml` template); REVIEW.md's "enforcement is
  structural" qualified until the `review:`-field templates exist (F6);
  `test_templates.py` now pins the reviews template and the review-brief skill
  (F7; suite 267→274); `PRINCIPLES.md` header re-keyed off the build grammar
  (F8, as the pass ruled).
- ⚠️ **Two claims in the entry below are corrected** (F2, F4 — dated addenda in
  the 0111 session log and the 0100 intent record; the originals stand): the
  old reviews-template link was **not** "broken in every stamped child" — it
  resolved by construction (the template set ships the target) — and the
  stamped template was **not** one of the "three places" the `ros` session had,
  nor why the amendment "never reached the fleet" (that repo never carried the
  file). The fork→pointer conversion stands on the fork argument alone.

### Changed (2026-07-19 — the review trigger is commitment, not artefact)
- **`method/REVIEW.md` — the scope rule re-keyed at its source.** The heading
  loses *a change* (*"Whether **work** earns a review at all"*) and the trigger
  becomes **commitment, not artefact**: *what will come to rest on this once it
  is trusted* — a question that parses identically whether the reader holds a
  paragraph, a plan, or a patch. The 2026-07-18 entry below diagnosed this
  framing defect correctly but fixed it *downstream*, by explaining the trap in
  a later section; with the trigger corrected upstream, that explanation shrinks
  to hand the correction up and carry the transferable rule instead — **when a
  written rule keeps being broken, suspect its framing before its enforcement**
  (Mike, 2026-07-19).
- **`build/templates/docs/reviews/README.md` — converted from an unmarked fork
  to a stamped pointer.** This is the propagation fix, and the reason the
  2026-07-18 amendment never reached the fleet: the file `create-repo` stamps
  into every child — the one an agent actually reads when deciding whether to
  queue a review — pointed up for the *lifecycle* while silently restating the
  *trigger* and *brief format* as its own second source. It had drifted
  accordingly, still carrying a 3-for-3 diff-shaped trigger and still naming
  *"a doc line"* as not-review-worthy while the parent said otherwise —
  the N-copies shape `PROPAGATION.md` rejects, reproduced inside the doctrine
  that forbids it. It now carries the same *"stamped copy, not a second source"*
  header `templates/CLAUDE.md` uses, states the one commitment question as a
  thin floor, and defers calibration explicitly to the parent. Brief format made
  fillable by work that isn't built yet (`Build`→`Subject`; `Scope` points at a
  design record where no diff exists; `Real-world check`→`Grounding`). The
  carve-out keeps its point but loses *"a doc line"* and gains its opposite:
  prose is not routine by virtue of being prose.
- **`method/MODEL-ECONOMICS.md`, `build/templates/CONTRIBUTING.md`** — re-nouned
  where they co-own the trigger, and pointed at `REVIEW.md` for it rather than
  implying their own. Net diff is **+89/−47** — *larger*, not smaller; what
  shrank is the count of independent statements of the trigger rule, **four to
  one** plus three pointers.
- **Still owed** (stated, not silent): the structural remedy the 2026-07-18
  change promised — every durable design record carrying a `review:` line — has
  **no artefact**. No ADR template, decisions README or ROADMAP template carries
  the field, so the templates keep manufacturing the blank the rule declares to
  be the bug.

### Changed (2026-07-18 — review is an input to building, not only a gate)
- **`method/REVIEW.md` — new section "Review the design, not only the build —
  the earliest review is the cheapest"** (the principal's ruling, 2026-07-18).
  Answers *when in the lifecycle*, distinct from the existing risk-calibration
  (*whether*) and inline-vs-batched (*by what mechanism*) sections: a captured
  feature, ratified design or structural decision earns a review **in its own
  right** — reviewability is not conferred by containing code — and lens 1 has
  the most to bite on before the code exists, when changing the answer is free.
  Names the framing trap that let the existing rule fail: every prior
  formulation is phrased around *a change*, grammar that presupposes the work
  already exists, so an agent holding a design finds every sentence shaped for
  a diff. Enforcement is **structural, not more prose** — the scope rule was
  already present in three accessible places when it was broken (2026-07-15 and
  again 2026-07-18), so a fourth copy would be the category error
  `PROPAGATION.md` names: durable design records now carry a review line, either
  a queued pointer or an explicit `review: not warranted — <grounds>`, because
  **omission reads identically to nobody having considered it**. Calibration
  unchanged — this widens what is reviewable and when, never the ceremony.
  Intent record: `decisions/2026-07-18-0820-review-the-design-not-only-the-build.md`.
  ⏳ **Self-authored doctrine — cold review queued** (rule 4: the taker writes
  the brief; the author wrote none).

### Changed (2026-07-14 — `sizescan` reviewed, fixed, and wired into the gate)
- **Cold review of `sizescan` + the lean-files doctrine cleared** (PASS-WITH-
  FINDINGS, un-briefed; `reviews/2026-07-14-2048-lean-files-sizescan-cold.md`).
  All findings resolved:
  - **F1 (MAJOR, fail-open) fixed** — skip-dir names were matched against the
    *absolute* path, so a repo living under any ancestor named `archive`/
    `sessions`/`reviews`/… had every file skipped and reported "clean" (exit 0),
    the exact contract violation the tool forbids. Now matched relative to the
    scan base; **live-reproven** (a 400-line ROADMAP under `archive/` now flags).
  - **F2 (MEDIUM) fixed** — `sizescan:allow`/`sizescan:budget=N` matched anywhere
    in the file, so a budgeted file that merely *mentioned* a marker in prose
    silently exempted itself (the reviewer's own draft tripped it). Markers are
    now honoured only in the **header** (first 15 lines).
  - **F4 fixed** — overlapping positional paths no longer double-report.
  - **F3 (doctrine) decided by Mike — index rotation.** `RECORD.md` sharpened:
    "append-only" is a rule about **content** (entries never edited/reordered),
    **not a fixed home** — an index that outgrows its budget rotates its older
    entries verbatim to a `SESSIONS-ARCHIVE.md` growth store, the same
    current-truth/history split as `ROADMAP`→`ROADMAP-DONE`. Resolves the
    collision the review found (a budget with no sanctioned move for an
    already-split index).
- **`sizescan` wired into the gate in `--check` mode** — atelier's `ci.yml` and
  the child `docs/build/templates/workflows/floor.yml` now run it (with
  `--selftest`). A repo that adopts the floor while over-budget **reds** — the
  intended signal to harvest — with `sizescan:budget=N`/`allow` hatches for a
  legitimately long file. Existing children pick it up when they re-adopt the
  template. Pinned by new `test_sizescan.py` (F1/F2/F4) + `test_templates.py`
  tests; suite 240→247.

### Added (2026-07-14 — lean current-truth files: `sizescan` + the harvest trigger)
- **`tools/sizescan.py`** (seventh house scanner) — the missing *signal* behind
  the current-truth/history split. `method/RECORD.md` already prescribed the fix
  (open items stay in `ROADMAP.md`; completed detail moves to `ROADMAP-DONE.md`;
  a flat session log becomes an index + `docs/sessions/`), but nothing *triggered*
  it: the split got done once by hand and decayed silently — a sibling roadmap
  reached 3197 lines, atelier's own 1091, each finished item accreting a running
  log of how it got done. `sizescan` reports any current-truth file over its line
  budget (`ROADMAP` 300 · `SESSIONS` 250 · `README`/`ARCHITECTURE` 250 · `CLAUDE`
  200), and is narrow by design: it budgets **only** the files meant to stay lean
  (root `README`/`CLAUDE`, the singular `ROADMAP`/`SESSIONS`/`ARCHITECTURE`) and
  **ignores the append-only stores** (`ROADMAP-DONE`, `CHANGELOG`, `SPECS`,
  `sessions/`, `reviews/`, `decisions/`, archives) — flagging the *destination*
  would punish the fix. **Advisory by default** (reports, exits 0 — bloat is a
  recoverable hygiene threshold, not a defect); `--check` is the opt-in gate.
  Zero-dep, `--selftest`, `sizescan:budget=N`/`sizescan:allow`/`.sizescanignore`
  hatches; 24 tests. Proven across the fleet — sharp on the real offenders (ros
  3197, faves SESSIONS 1157), silent on the seven healthy repos.
- **`method/RECORD.md` § "The roadmap"** sharpened — names the growth dynamic (a
  finished item becomes a mini session-log; the case-law is *history* in a
  *current-truth* file), the fix (collapse to a one-line pointer, relocate
  verbatim, never delete), the generalisation (**current-truth files stay lean;
  history relocates to an on-demand store** — SESSIONS/ROADMAP/README all one
  shape), and the trigger (**harvest at session close**, backed by `sizescan`).
- **`docs/ROADMAP-DONE.md`** created — atelier dogfooding its own doctrine:
  `docs/ROADMAP.md` harvested 1091→lean (well under budget), ~800 lines of
  completed case-law moved **verbatim** to the new archive, every checkbox item
  accounted for (zero lost). `sizescan` + `linkscan` clean on the result.
- **Owed:** `sizescan` + this doctrine are net-new tooling → **cold review
  owed** before wiring into `ci.yml`/`floor.yml` (don't-stack). The ros ROADMAP
  harvest + faves SESSIONS split are logged as fleet backlog (their own sessions).

### Added (2026-07-13 — CONCURRENCY gains a work-claiming mechanism)
- **`method/CONCURRENCY.md` § "Claiming work — make selection collide like
  naming does"** — closes the last unguarded coordination point: two parallel
  sessions self-selecting the *same* roadmap item and duplicating the work,
  silently (nothing in tree or record conflicts). A session claims an item by
  editing that item's line **in place** (`[~]` + `(claimed <date>-<HHMM>, wt:
  <branch>)`) and pushing **before** working, so a same-item double-claim lands
  as a trivial same-line rebase conflict — the coordination-free record-ID
  bearing generalised from record *naming* to work *selection*. Worktree-mode
  only (zero cost to the solo default); grain is the leaf item not the theme (so
  a themed instruction fans out); release = branch put-away; orphan claims
  judged like stale branches (timestamp bounds staleness, no lease/lock). ROADMAP
  gains a `[~]` legend. **Reviewed same day** (cold, un-briefed):
  PASS-WITH-FINDINGS, 1 MAJOR · 4 MEDIUM · 2 LOW, Mike ruled **all seven [fixed]**
  and they were applied. The MAJOR reframed the mechanism — claiming now keys on
  **selection from the shared queue** (not worktree-mode, whose only trigger was
  the say-so the incident had already broken), and the claim commit lands on
  `main` *before* branching. Plus: fan-out needs per-leaf lines (bundled lines
  serialise); adjacent one-line claims raise a trivial keep-both conflict
  (live-verified); put-away carries the `[~]`→`[ ]` reversion; tracker-based
  adopters pointed at the assignee primitive; timestamp demoted to a staleness
  tiebreak. Verdict + decisions in
  `reviews/2026-07-13-concurrency-claiming-work.md`. **Applied-batch cold pass
  RAN same day** (owed because the first pass carried a MAJOR): PASS-WITH-FINDINGS,
  **no MAJOR — cycle closed**, all seven confirmed landed + live-reproduced. Two
  residuals, both **[fixed]**: the claim is made from the primary `main` checkout
  before `git worktree add` (git checks `main` out in one place — the MEDIUM the
  reframe opened beneath), and the adjacency parenthetical corrected (no unchanged
  line between, not a three-line context — LOW). Verdict in
  `reviews/2026-07-13-2256-claiming-work-applied.md`.
- **`method/RECORD.md`** — record ids are noted as long/lowercase/hyphenated by
  design (40+ chars), so a downstream tool that quotes one (registry validator,
  secret/token scanner) must allow that shape and reference the id in full.
  Bearing: a sibling repo's registry validator tripped its token-shape guard on a
  46-char id; atelier's own entropy-based scanners pass these ids clean.

### Changed (2026-07-13 — REACH re-review applied; four principal decisions land)
- **`method/REACH.md` + `method/AUTONOMY.md`** — the adversarial re-review's
  eight findings **A1–A8 all [fixed]** on Mike's decision (counsel had said
  A1–A5; he took the lot), applied by a neutral hand. The two majors close
  real credential-boundary gaps: **A1** REACH's "no further permission needed"
  reconciled with AUTONOMY's always-confirm secrets floor — provisioned
  credentials are in scope *for their provisioned use, through the resolving
  machinery*; direct value handling stays floor-stopped (AUTONOMY gains the
  matching carve-out so the two docs state one rule). **A2** riding an
  authenticated session now licenses *retrieval only*; state-changing acts
  through a ridden session are their own actions under the floor. Plus: stale
  instance-status parenthetical dropped (A3), descent rule split — shape picks
  rungs 1–2, block gates 3+ (A4), isolation axis restricted to rungs 3–5 (A5),
  temporary grants expire rather than enrol (A6), EVIDENCE §13 cross-reference
  (A7), generality honesty clause + ADR 0006 third-verb realignment (A8).
  **Cold pass RAN same day** per the cycle rule: PASS-WITH-FINDINGS, **no
  MAJOR — cycle closed**; fidelity 8/8, H1–H8 backlogged (verdict in
  `reviews/2026-07-13-reach-batch-applied.md`).
- **Session-38 name × debt join scrubbed** (Mike's decision) — the last
  surviving instance of a named child paired with its scan posture, reworded
  out of the session-38 detail file, its SESSIONS.md index line, and the
  ROADMAP bullet; each spot notes the scrub and that history keeps the old
  wording. The transferable lesson (read the repo's own roadmap before
  externalising a scan report) is kept.
- **Two decisions recorded:** the next deliberate widening is spent on a
  **v2 plugin** (de-instanced `create-repo`, `worktree`/`fleet-pins` commands
  — new ROADMAP item, scoping first); the estate credential-registry open
  question is **resolved** — it already lives in the dedicated private
  estate-root repo (unnamed here by RECORD's own rule).

### Changed (2026-07-13 — "disposition" renamed to "decision")
- **`method/REVIEW.md` + `method/CONCURRENCY.md` + `docs/ROADMAP.md`** — the
  review-lifecycle term **"disposition" is retired for "decision"**, Mike's
  call: the word was the agent's vocabulary, not his, and plain language wins
  (lifecycle step 4 is now **Decision**; findings are *decided*, decisions are
  stamped). Terminology only — no rule changes meaning. Dated records
  (`docs/reviews/`, `docs/sessions/`, past CHANGELOG entries) keep the word
  they were written with, per the leave-prior-records-standing practice.

### Changed (2026-07-12 — concurrency gets its trigger; sync bookends)
- **`method/CONCURRENCY.md`** — the worktree rule existed but nothing told a
  session it was the *second* one on a repo, so it never fired in practice;
  parallel sessions in shared checkouts stayed safe on short commit-to-push
  windows, not on the rule. Added: **the trigger** (say-so-at-open primary cue
  + dirty-tree backstop — uncommitted changes a session didn't make mean
  another session is live: move to a worktree, never work around or absorb
  them), **the solo default** (a lone session commits to the integration
  branch directly; branch-per-session is put-away ceremony with zero isolation
  gain), and **sync bookends** (`git pull --rebase --autostash` at start, push
  per commit; append-tail conflicts in session logs are expected-and-trivial).
- **`method/PROPAGATION.md`** — the standard child doctrine block gains a
  **Concurrency** line (bookends + dirty-tree backstop) so the trigger reaches
  the fleet on each repo's next pin bump; the narrowing-free-restatement note
  now names the line's source.
- **`CLAUDE.md`** — the session-start read order now begins with the sync
  bookend + dirty-tree check.

### Changed (2026-07-12 — COMMUNICATION.md cold-reviewed, findings fixed)
- **`method/COMMUNICATION.md` review-cleared** — the owed cold review RAN:
  **PASS-WITH-FINDINGS**, verdict in `docs/reviews/2026-07-12-communication.md`.
  The leak-by-implication fear cleared (the scrubbed example's join carries no
  content; the scrub note names only categories the boundary statement already
  publishes). Findings C1–C4 fixed in the doc: maintenance enforcement stated
  honestly (write-time discipline is the only control — the person layer is
  outside every mechanical floor and review sweep by design); the
  not-even-private rule's divergence from the portability north star surfaced
  and kept, with its why; the worked example dated as a 2026-07-12 snapshot
  and named as the one sanctioned exception to never-copied; the boundary
  sentence sharpened (*functions* without the personal context — the
  understanding stays person-local).

### Added (2026-07-12 — communication calibration doctrine)
- **`method/COMMUNICATION.md`** — calibrate replies to the person reading
  them. Each principal keeps a person-local "working with me" calibration
  (ordering, density, visual structure, cognitive-load stance, tone, locale,
  what personal context is for), maintained from dated evidence, pointed at
  and never copied into a repo. The TOOLBOX practice/instance split applied
  to communication; a scrubbed worked example included (ADR 0005
  named-worked-example framing). Declined 2026-07-12 as personal-only, then
  revisited the same day by Mike: the values stay in `~/.claude/`, the
  *pattern* is what a peer adopter needs. Review-owed (ROADMAP).

### Added (2026-07-12 — commit signing ACTIVATED; ladder steps 1–5)
- **Signing is live** (SIGNING.md, ADR 0007). Mike registered a dedicated
  ed25519 signing key to GitHub (step 1); the machine is wired (global
  `gpg.format=ssh` + `commit/tag.gpgsign` + canonical `allowed_signers` in the
  repo root); atelier's **adoption boundary is `958b1ea`**, proven on both
  planes (`git verify-commit` good, `gh api …verification.verified` → true).
- **`tools/signscan.py`** — verifies commit signatures over a range against a
  trust list, two-plane aware (machine-key commits locally via ssh-keygen;
  GitHub web-flow commits deferred to the `gh api` plane), with a `--selftest`
  carrying a known-signed fixture whose **quoted** `valid-after` turns a parse
  regression red. `--warn` for the warn-first rollout. Zero-dep; 12 tests.
- **CI verification wired** (step 5) into atelier's `ci.yml` and the child
  `floor.yml` template: `fetch-depth: 0`, both planes, trust list resolved at
  the child's atelier **pin** (never floating `main`), signscan selftest in the
  floor. **Warn-first** — reports unverified commits without failing the build
  until the fleet has settled. (Per-child retrofit — step 4 — rolls the updated
  floor to each child with a pin bump + recorded boundary.)
- **Fleet retrofit (step 4).** The 10 children carrying the house floor adopted
  signing verification — pin bumped to a signing-aware atelier SHA, floor
  signing steps rolled in, `SIGN_BOUNDARY` set to each repo's pre-signing HEAD.
  7 verified CI-green; 3 (docker-heap, rpi, homenetwork) red on **pre-existing
  scanner debt** that fails before the signing steps run (owner's debt, not
  signing). faves + ros run bespoke `ci.yml` (never adopted the house floor) —
  their signing-CI is deferred to a floor-adoption pass; they still sign.
- **Timezone trap fixed, caught by atelier's own CI dogfood.** The first CI run
  reported every signed commit `bad`: bare `valid-after="20260712"` is read in
  the verifier's local timezone, so the list passed on the UTC+12 author machine
  but failed in the UTC runner ("key is not yet valid" — a 02:13 NZST commit is
  14:13 the previous UTC day). Fixed by anchoring `valid-after` in UTC with a
  `Z` suffix (`"20260711Z"`), before the earliest commit's UTC time; SIGNING.md
  now mandates it and the signscan selftest fixture guards it. Dogfooding
  atelier before any child was retrofitted is exactly what surfaced it.
- **`create-repo` + REPO-STANDARD** bake repo-local `commit.gpgsign=true` so a
  scaffolded repo is born signing (step 3).
- **Signing pre-flight in the pre-commit hook.** When a repo signs with SSH, the
  hook runs a fast non-interactive test-sign; if the key isn't loaded it prints
  the `ssh-add --apple-use-keychain` remedy before git's cryptic failure, only
  after scanners pass, silent when ready, never blocking. Same remedy documented
  in SIGNING.md's new *Operational notes* section (the known-issue home).

### Changed (2026-07-12 — the two owed cold reviews ran; both doctrines corrected)
- **RECORD "keep private repos generic" redrafted** after its cold review
  (`docs/reviews/2026-07-12-record-private-repos-generic.md`,
  PASS-WITH-FINDINGS, R1–R7 all fixed): the regulated class is now the **join**
  — a private repo's *name* coupled to its *sensitive posture* (which secrets,
  where, exposure history, publication intent, client content) — not the name
  itself; name-only mentions are sanctioned behind a load-bearing-name test
  (e.g. ros, faves, numen). Enforcement stated honestly: no scanner can hold
  this rule — write-time discipline plus review sweeps, nothing stronger; and
  on a public repo a scrub of HEAD is not remediation. Four surviving
  name-to-posture joins the incident scrub missed were scrubbed at HEAD
  (SESSIONS index, two session detail files, ROADMAP).
- **SIGNING.md corrected pre-activation** after its cold review
  (`docs/reviews/2026-07-12-signing-doctrine.md`, PASS-WITH-FINDINGS, G1–G10
  all addressed; core design live-proven sound in a scratch drive):
  verification is now **two-plane** (machine-key commits via
  `git verify-commit`; GitHub's server-side merge/squash commits — GPG-signed
  by the web-flow key, two already on `main` — via the `gh api` verification
  check, spoof-safe); the badge-persistence claim was inverted vs current
  GitHub behaviour and is corrected (removing a key does **not** un-verify
  history) — ADR 0007 carries the correction as an addendum (no-edit rule);
  `allowed_signers` entries mandate **quoted** validity timestamps (unquoted
  man-page syntax fails to parse on the estate's ssh-keygen) and the trust
  list is resolved at the child's atelier **pin**, never floating `main`;
  custody, adoption-boundary stubs, and bounding-is-not-revocation stated at
  true strength. Decision unchanged; activation still gates on the principal
  registering a key.

### Added (2026-07-11 — RECORD: public records keep private repos generic)
- `docs/method/RECORD.md` new section **"The record is public — keep private repos
  generic"**: the no-personal-estate-data rule covers *prose describing* private
  secrets, not only literal values (a pattern scanner can't catch a sentence). A
  public record names a private sibling repo only when its name carries doctrinal
  weight as a worked example; it never records which private repo holds which
  secret, where, or its exposure history. Grounded in a same-day incident — session
  records had leaked secret-posture prose into public atelier; scrubbed from HEAD
  (history left, per the principal — no real values, only pointers). Review-owed.

### Added (2026-07-11 — signing doctrine: SSH commit signing fleet-wide, ADR 0007)
- `docs/method/SIGNING.md` — provenance doctrine for the record: SSH-native
  commit/tag signing (zero-install, `gpg.format ssh`), dedicated signing key,
  one canonical append-only `allowed_signers` tracked in atelier, verification
  in CI from each repo's adoption boundary, honest statement of what a
  signature claims (machine custody, not personal authorship). **Decided but
  dormant** — activation gated on the principal registering a signing key (a
  trust surface, his act); the doc carries the activation ladder.
- `docs/decisions/0007-ssh-commit-signing.md` — the ADR: SSH signing beats
  GPG (tool install for no gain), sigstore/gitsign (OIDC + tooling dependency),
  and no-signing (spoofable identity under load-bearing SHAs); artifact
  signing + SBOM stays deferred behind the first real release.

### Added (2026-07-11 — atelier packaged as an installable Claude Code plugin, v0.1.0)
- **atelier is now its own plugin *and* its own marketplace.** `.claude-plugin/
  plugin.json` (name `atelier`, `version 0.1.0`, Apache-2.0) + `.claude-plugin/
  marketplace.json` (`source: "./"`). Install:
  `/plugin marketplace add mike548141/atelier` → `/plugin install atelier@atelier`.
  The doctrine now travels as **behaviour**, not just readable docs.
- **Root-as-plugin, not a subfolder — a deliberate, documented exception to
  REPO-STANDARD's product-in-subfolder rule.** Forced by *one source*: a
  `git-subdir` install sparse-clones only the subdir, so a `plugin/` folder could
  not reach `tools/`+`docs/` without *copying* them — the exact second-source
  atelier exists to prevent. Root-as-plugin keeps `${CLAUDE_PLUGIN_ROOT}` = the
  repo, scanners and docs referenced in place.
- **`version: "0.1.0"`, bumped deliberately — not omitted.** Omitting makes every
  commit a new version consumers auto-pull, so a *records commit* would ship a
  "release". A real version bumped only on doctrine change matches atelier's
  deliberate-bump doctrine (ADR 0002 / SHA-as-version, applied to the consumer
  edge).
- **v1 (Middle tier) components:** `/atelier:scan` (the four publish-safety
  scanners over any repo), `/atelier:install-hook` (the fail-closed git
  pre-commit hook — resolves `${CLAUDE_PLUGIN_ROOT}/tools` to an absolute path at
  install time, since git has no such env var at commit time), the
  `session-onramp` skill (inlines the apex + always-confirm floor, points at the
  bundled doctrine) and the `review-brief` skill (the REVIEW.md lifecycle). The
  whole `docs/method/` + `docs/build/` doctrine ships as bundled reference.
- **Deferred to v2:** a de-instanced `create-repo` (general parts →
  `${CLAUDE_PLUGIN_ROOT}`, the gh-account / git-identity / copyright-holder
  specifics become adopter-filled placeholders that stay machine-local), plus
  `worktree` / `fleet-pins` commands.
- Delivered on a branch + PR: **the PR merge to `main` is the go-live act** (the
  marketplace only resolves from the default branch) — the widening floor stays
  the principal's deliberate call, not the agent's.

### Added (2026-07-11 — ccrepo actuals vs estimate)
- **ccrepo: an Actual column beside Est (API)**, driven by a machine-local
  `~/.claude/ccrepo-billing.json` (never in a repo — a plan and spend are
  personal data; absent ⇒ estimate-only with a byte-identical JSON contract;
  malformed ⇒ ignored-with-warning, never fatal). `plan.covers[]` matches model
  families by prefix after `claude-` is stripped, `perTokenModels` carves one
  back out; covered-model tokens cost **$0 marginal** and the sunk plan fee is
  apportioned per repo by covered-token share (falling back to total-token share
  if nothing covered ran in range), while uncovered models keep the API-rate
  figure. **Actual = apportioned plan share + uncovered per-token spend**, so the
  TOTAL Actual row equals `fee + all uncovered spend` — proven live: estate-wide
  Est US$2,305 vs Actual US$200 (the whole plan fee). Both columns convert
  together under `--fx`; `--no-billing` forces estimate-only. Multi-month outlay
  and overage thresholds are stated footnotes, out of scope v1. Closes the
  design-before-code roadmap item (the config was designed first, then the code
  once the shape was confirmed). 8 new pure tests (`loadBilling`,
  `coversPredicate`, `actualFor`, the covered/uncovered fold); Node suite 26→34.

### Fixed (2026-07-11 — the instruments test-floor code review's 10 findings)
- **All ten confirmed findings from the `8536971` code review fixed + pinned**
  (`docs/reviews/2026-07-11-instruments-test-floor-code-review.md`; suite
  20→26). The two that affected the floor itself: the **timezone-fragile
  `--by-day` test** (fixture timestamps moved to midday UTC — same local day in
  every real offset; proven under Halifax and Chatham) and the **`test_*.js` →
  `*.test.js` rename** — the documented command now works, and `ci.yml` runs the
  shell glob `node --test instruments/*.test.js` so a future test file can't
  silently skip CI. Correctness: help/validation argv parsing moved out of
  module load (requiring an instrument can no longer print help or kill the
  host off the host's argv — pinned by require-survival tests); `shortModel`
  total over drifted ccusage rows; `.session` envelope guard with a friendly
  message; dangling-symlink guard in ccrepo's projects walk; `main().catch`
  keeps failed runs loud. Cleanups: `pt`/`paint` painter deduped;
  one `sessionRecord()` constructor for walked + explicit-path sessions (real
  mtime, no more blank list timestamp); `buildIndex()` returns its maps instead
  of mutating module state.

### Added (2026-07-11 — instruments builds + three cold reviews cleared)
- **ccrepo: full ccusage breakdown** — the table, `--by-model`/`--by-day`
  children, and `--json` now carry **Cache Create · Cache Read · Cache Hit**
  (reads ÷ prompt-side tokens; definition footnoted in the output) alongside
  Input/Output/Total/Cost — the cache-economics lever MODEL-ECONOMICS names,
  made observable per repo. Fixtures corrected to mirror ccusage's real shape
  (totalTokens includes cache tokens); new `cacheHitRate` unit.
- **cctranscript: per-reply response IDs (`N.M`)** — each of Claude's text
  replies to prompt N is citable as `N.M` in the reply header
  (`◂ Claude 1.1 (Opus 4.8)`), M resetting per prompt; `--json` carries a
  `ref` on every turn (null on think/tool/result — the citable unit is what a
  human quotes). Completes the reference scheme the session-ID header and
  `▸ N` exchange rule started. `numberTurns()` pure + unit-tested; the
  contract test asserts the scheme.
- **ccrepo actuals-vs-estimate: billing-model config designed** (design-
  before-code, per the roadmap item) — `instruments/README.md` § "ccrepo
  billing model": machine-local `~/.claude/ccrepo-billing.json`, plan as sunk
  monthly cost with covered families at $0 marginal, uncovered models keep
  the API-rate figure; limits/overage explicitly out of scope v1. Code awaits
  Mike's confirmation of the config shape.
- **REPO-STANDARD: new repos born with delete-branch-on-merge** — new-repo
  process step 6 (+ the create-repo skill's create-remote step): `gh repo
  edit --delete-branch-on-merge` follows `gh repo create`, making the landed
  half of CONCURRENCY's put-away rule automatic at birth.

### Changed (2026-07-11 — three cold reviews, all PASS-WITH-FINDINGS, findings fixed)
- **PRINCIPLES §8 reviewed** (`docs/reviews/2026-07-11-principles-8-leverage.md`):
  intro's stale "§1–7" swept to "§1–8", §7's "Numbered last" opener made
  position-independent, observed-vs-predicted recurrence evidence bar added
  to the §8 discipline. Gate cleared.
- **CONCURRENCY put-away rule reviewed**
  (`docs/reviews/2026-07-11-concurrency-put-away.md`): the bearing's
  re-derivation count grounded explicitly (PR #1 close + session 34; a
  *considered* kept-branch still generated the tax), scoping clause added
  (integration/permanent branches are infrastructure, not open work),
  archive-tag convention date-prefixed per RECORD. Gate cleared.
- **Plugin bundle (PR #3) reviewed cold, install driven live**
  (`docs/reviews/2026-07-11-plugin-bundle.md`): PASS-WITH-FINDINGS, nothing
  blocks the merge; findings 1–3 fixed on the branch (update-invalidates-
  hooks warning, location-relative doctrine refs in skills, all three
  companions named). Go-live (the merge) stays Mike's call.

### Added (2026-07-11 — instruments/ test floor: ccrepo + cctranscript)
- **The `instruments/` layer gains its test floor** — shipped untested in session
  34 (stated, not silent); now floored. Runner decision, recorded because it's the
  first Node test surface and so sets the layer's convention: **Node's built-in
  `node:test` + `node:assert`, zero third-party dep** — mirrors `tools/`'s
  stdlib-only "no pytest" pattern. `instruments/test_cctranscript.js` carries a
  **`--json` output-contract test** over a checked-in synthetic fixture
  (`fixtures/session-sample.jsonl`) — role classification, model mapping,
  timestamp/text extraction, and `--think`/`--tools` gating — which is what catches
  a Claude Code `.jsonl` log-format change, plus pure-function units (friendlyModel,
  wrap, styleInline, humanDelta, fmtTime/dateOf, visLen/padLeftTo). `test_ccrepo.js`
  covers the pure functions and the aggregation fold over fixture ccusage rows.
  Testability refactor was minimal and behaviour-preserving: CLI entrypoints guarded
  by `require.main === module`, pure functions exported, three colour/tz-dependent
  functions given a defaulted param. **One stated fix** surfaced by a test: an
  explicit `.jsonl` path now recovers its repo label via `cwdFromLog` (every other
  route already did; the explicit-path branch had dropped it). Wired into `ci.yml`'s
  floor job (adds `setup-node`, stays zero-dep). Grounded in **EVIDENCE §14** — an
  honest instrument's "ok" is a claim the apex governs. **Residual:** ccrepo's
  `ccusage` shell-out / FX / render sit behind an untested seam (aggregation was
  factored to `aggregate()` and is covered; the `execFileSync` itself is not).

### Added (2026-07-11 — CONCURRENCY: every branch ends put away)
- **`docs/method/CONCURRENCY.md` gains "Every branch ends put away"** — "branch
  exists" had been allowed to mean two things: *open work*, and *closed work
  nobody finished putting away* — and every session that saw a half-closed branch
  paid to re-derive which it was. Now it means only the first. A branch ends
  **landed** (merged then deleted; delete-branch-on-merge flipped ON across the 8
  active repos makes that automatic) or **abandoned/superseded** via **salvage →
  tag → delete → record** — mechanical comparison, annotated `archive/<name>` tag
  stating what was salvaged where and what was consciously dropped, branch
  deleted, disposition in the session log. Grounded in the failure it closes:
  `atelier-method-review` was salvaged *and* archive-tagged properly, left
  standing, and re-derived by session after session. **Review-owed** (doctrine
  text; flagged in ROADMAP, not self-certified). create-repo birthing new repos
  with the merge setting on is backlogged.

### Added (2026-07-11 — the instruments/ layer: ccrepo + cctranscript, ADR 0006)
- **`instruments/` — a new top-level layer for teammate instruments**, split from
  `tools/` by purpose: `tools/` *enforces* the doctrine (Python checks that gate a
  commit), `instruments/` *observes* the collaboration itself. First residents:
  **`ccrepo`** (per-repo Claude Code token/cost totals — the DevFinOps view) and
  **`cctranscript`** (timestamped session transcript — the timestamps the chat UI
  hides), both zero-dep Node CLIs reading `~/.claude/projects/` read-only, plus an
  idempotent `instruments/install` (per-tool symlinks into `~/.local/bin`).
  Membership rule in **ADR 0006**: an instrument belongs only if its value *is*
  the Claude teammateship; estate utilities stay with the estate they serve.
  Moved in from `homenetwork/bin` (which is now removed); verified clean of
  personal data before entering the public repo. Tests backlogged in ROADMAP —
  shipped untested, stated not silent.

### Added (2026-07-11 — PRINCIPLES §8: leverage / "productive laziness")
- **`docs/method/PRINCIPLES.md` gains §8 "Leverage — invest now to stop paying
  later"** — Mike named the principle; strategic laziness is leverage: spend more
  now (a work-avoiding *design*, or a reliable *reusable tool*) to save repeated
  work later and get consistent, robust outputs. Two forms — **design out the
  work** (thin-anchor-fat-pointer, one-source) and **build the reliable tool once**
  (the scan triad; the codified verb that replaced recurring hand-surgery, a §7
  case now generalised; tied to EVIDENCE §14 — the tool is a source, so build it
  tested-and-honest). Plus **the discipline** (payback needs real recurrence, not
  gold-plating; never a shortcut through §0–§2) and a **"One-off or recurring?"**
  situation test. Appended, not renumbered (§5 is cross-referenced; external cites
  of `PRINCIPLES §N` must not shift). Grounded, not invented — the repo already
  instantiates it. **Review-owed** by the ceremony-calibration rule (doctrine text;
  flagged, not self-certified).

### Changed (2026-07-11 — the child-CI-floor review: the masking fix now covers the class)
- **secretscan + leakscan hardened by the child-CI-floor review** (Fable, cold
  session: `docs/reviews/2026-07-11-child-ci-floor.md`, PASS-WITH-FINDINGS,
  N1–N6 all fixed + re-driven; suite 196→205). The review's headline: the
  `d0870a4` linkscan masking fix had closed the *instance*, not the class —
  proven live at review HEAD, a planted `AKIA…` key in `docs/build/` scanned
  **green** whole-tree because both boundary scanners still hardcode-skipped
  `build`/`dist` (N1, now mirrored out); both also **phantom-succeeded on a
  nonexistent path** ("✓ clean", exit 0 — the linkscan L1 silent-success class;
  now exit 2, N2); and the ignore-file hatch was **dead whenever CWD ≠ root** —
  exactly floor.yml's invocation — because globs were matched against
  CWD-relative paths (N3, both sides now resolved, mirroring linkscan's
  reviewed `_rel`). `floor.yml` gains **every-push triggers** (a never-PR'd
  feature branch was scanned by nothing, while the header claimed "every push";
  N4), a **scanner-selftests step** before the scans (N5), and **in-file
  false-positive hatch docs** (N6) — all pinned by new `test_templates.py`
  tests. Floating `atelier@main` was attacked and held: the scanner fixes reach
  every child's next run with zero per-child bumps, which for a security floor
  is the safety property. Follow-up: numen re-copies floor.yml (workflow-file
  fixes don't float).

### Added (2026-07-10 — child CI scanner floor: the public scanners now gate child repos)
- **`docs/build/templates/workflows/floor.yml`** — the CI backstop to the
  pre-commit scan hook, for any repo that inherits house doctrine. The hook only
  guards the clone it's installed in (git transports neither hooks nor config);
  this workflow re-runs the publish/leak scans on every push + PR. It checks
  `mike548141/atelier` out **beside** the repo and runs its public
  secretscan/leakscan/linkscan against the repo's own tree — **one source, no
  vendored copy, no drift**, now possible because atelier is public (ADR 0005)
  and the scanners are zero-dep stdlib. Design calls are in the header:
  **`atelier@main`** floats (a security floor wants the newest scanner; and it
  avoids a second stamped-SHA drift surface — CLAUDE.md's pin stays the only
  doctrine-version truth); **leakscan structural-only** (its term list is
  machine-local — the same honest scope as atelier's own `ci.yml`);
  **licenscan commented** (no-LICENSE hard-fails it, so it's a *publish* gate,
  not an always-on floor for a private child). The scan is scoped to the repo's
  tree, not the whole workspace — atelier's own fake-secret fixtures would
  false-positive otherwise. Proven both ways (clean child 0/0/0; damaged child
  with a real key + broken link blocks) and pinned by 5 `test_templates.py`
  tests (suite 190→195). create-repo seeds it and REPO-STANDARD lists it; the
  skill's "CI scanning not wired yet" note is retired.

### Changed (2026-07-10 — the linkscan review: gate cleared, five assumptions repaired)
- **`tools/linkscan.py` hardened by its own review** (Fable, cold session:
  `docs/reviews/2026-07-10-linkscan.md`, PASS-WITH-FINDINGS, findings L1–L10).
  The brief's five load-bearing assumptions all took damage, proven live before
  fixing: a **typo'd path arg scanned nothing and exited 0** (now a usage error,
  exit 2 — the EVIDENCE §14 silent-success class in a gate-destined tool);
  **case-mismatched links** green on a case-insensitive disk but 404 on GitHub
  (now checked against on-disk casing, unicode-normalisation-safe); links
  **escaping the repo root** (new `outside-root` finding — GitHub serves nothing
  above the repository root); **anchor matching now exact** like GitHub's
  fragment matching, with the fix printed when only the casing is wrong — which
  required teaching the slugger that GitHub *keeps* literal underscores;
  **parenthesised filenames** (`a(1).md`) parse instead of false-positiving;
  **fence tracking** length- and info-string-aware (a ``` inside a ```` block
  stays code) via one shared tracker for links and headings; **setext headings**
  now mint anchors (they were false-positiving valid links, filed under the
  wrong failure class in the residual). Root-relative `/…` semantics verified
  against GitHub's docs (matches). Residual list updated: setext off;
  HTML-minted anchors and indented-code false positives on, the latter
  deliberately unfixed (the fix would cost real false negatives). Suite
  **171→187**, selftest +2 cases, whole tree rescanned clean under the stricter
  checks. **Gate cleared** — wiring into `ci.yml`/`pre-commit.sample` is
  unblocked but left to the next build session (a reviewer doesn't wire its own
  same-day fixes into the gate).

### Added (2026-07-10 — linkscan: the internal-link integrity check)
- **`tools/linkscan.py`** — the mechanical check that atelier's "thin anchor, fat
  pointer" graph (`method/PROPAGATION.md`) actually resolves. A relative link that
  404s — a renamed file, a moved doc, a typo'd `#anchor` — is a silent hole in the
  doctrine graph; this catches it before a reader (or adopter) does. Scope is
  deliberately narrow: **internal `[text](path)` links only** (external schemes and
  `//host` skipped — the network is a flakier tool's job). Two finding kinds:
  `missing-file` (path unresolved, relative to the linking file / repo root for
  `/…`) and `missing-anchor` (a `#fragment` into a Markdown target whose GitHub
  slug matches no heading; `#L42` line refs and non-Markdown anchors skipped).
  Fenced/inline code stripped so example links don't false-positive.
- Same house pattern as the scan triad: zero-dep stdlib, `--selftest`,
  `linkscan:allow` + `.linkscanignore` hatches, fail-safe exit codes (`0` clean /
  `1` break / `2` couldn't-complete — never a silent green). **`tools/test_linkscan.py`**
  adds 26 tests (suite 145→171). Proven live — selftest OK, whole tree clean (55
  Markdown files, 36 internal links), anchor pass/fail + a planted break verified
  against real files. Honest residual added to `tools/README.md`: reference-style
  links, HTML links, setext headings, a `](…)` split across two lines, and slugger
  divergence from full CommonMark are the known blind spots.
- **Review-gated before it becomes a gate** (`docs/reviews/2026-07-10-linkscan.md`,
  brief) — the false-negative surface is the sharpest lens. **Not yet wired into
  `ci.yml`/`pre-commit.sample`**; that wiring waits for the verdict
  (don't-stack-a-gate-on-unreviewed-tooling, third application after the method
  layer and the create-repo mechanism).

### Added (2026-07-10 — atelier's own CI: the floor, dogfooded)
- **`.github/workflows/ci.yml` (job `floor`)** — going public (ADR 0005)
  dissolved the blocker, so the floor every review had been asserting by hand now
  runs on every push and PR: the tool test suite (145 tests), the three scanner
  `--selftest`s, and the scan triad (`secretscan`/`leakscan`/`licenscan
  --expect Apache-2.0`) over the whole tree. Zero-dep stdlib → a runner needs
  only Python.
- **Honest CI scope, in the header not the fine print**: secretscan/licenscan run
  at full cover; **leakscan runs structural-only and deliberately WITHOUT
  `--require-terms`**, because its literal person/estate term list is
  machine-local by design (`~/.claude`, never in any repo) — CI can't hold it and
  must not. Full leakscan cover stays where the term list lives: the pre-commit
  hook on a real machine.
- Least-privilege (`contents: read`), concurrency-cancel for cost hygiene.
  **Live-proven twice on GitHub** — first run green (11s), then `checkout@v5` +
  `setup-python@v6` to clear the Node-20 deprecation annotation, re-run green (7s,
  11/11 steps, no annotation). Watched, not assumed (REVIEW's re-run-live-proven
  rule). The file doubles as the reference a child copies to run atelier's public
  `tools/` in its own CI (that half + a markdown link-check remain open).

### Fixed (2026-07-10 — the create-repo delivery-mechanism review: C1–C10, all fixed + re-driven)
- **The Fable sweep of the rewire ran cold and PASSED-WITH-FINDINGS** (verdict in
  `docs/reviews/2026-07-10-create-repo-rewire.md`); the gate is cleared — keeper
  repos may be scaffolded. Two findings proven live before fixing: **C1** a fresh
  clone of a scaffolded repo lost the hook + `hooks.atelierTools` silently
  (git transports neither) and committed a planted `AKIA…` key green — the
  fail-open class one hop later; now stated at the three places a new clone
  looks (template CLAUDE.md "Hooks don't travel" bullet, CONTRIBUTING
  once-per-clone install lines, the hook header). **C2** the stamped drift
  check broke run-verbatim — the block stamped the atelier path unquoted and
  the house path contains spaces; the canonical block (PROPAGATION) + template
  now quote it, and the skill stamps sibling-relative `../atelier` with a
  mechanical prove-the-stamp (grep unfilled placeholders; run the drift command
  verbatim, expect empty).
- **Template-block drift is now mechanically impossible to miss** (C3):
  `tools/test_templates.py` diffs the template's stamped doctrine block against
  PROPAGATION's canonical text character-for-character on every suite run, and
  pins the four-placeholder set (C4 — PROPAGATION's prose said "three" while
  its own block carried four). Suite 142→145 OK.
- **Honesty sweeps** (C6–C10): the hook's/README's "pair with CI" lines now
  state that child-repo CI scanning is *not wired yet* (the hook is a child's
  only scan gate — deferred scanner-distribution call); `templates/LICENSE`
  added (Apache-2.0 verbatim; was copied from faves — a second source with no
  target line for "set the holder"); the `ATELIER_TOOLS` trust surface stated
  in the hook header; skill step 7's `gh repo create` re-anchored to Mike's
  ask (not "push is recoverable"); the atelier-present precondition now checks
  the templates are *readable*, not just that the path exists (iCloud
  eviction).

### Fixed (2026-07-10 — create-repo scaffold exercised end-to-end; scan-hook fail-open defect closed)
- **The scaffolded scan hook silently protected nothing.** Exercising `create-repo`
  on a real local scaffold (the owed real-scaffold run) surfaced a defect the
  session-18 scratch dry-run couldn't: `tools/pre-commit.sample` hardcoded the
  scanners at `$repo_root/tools/` and **failed open** (`[ -f ] → skip`) when they
  were absent. A child repo has no scanners of its own — they live only in atelier
  — so its copied hook waved *every* commit through, secrets included (proven: a
  commit carrying a real `AKIA…` key went straight into history). The "costume,
  not doctrine" failure one layer down, and a textbook §14 silent-success defect.
- **Fix — resolve up + fail closed.** The sample now resolves atelier's tools dir
  (`ATELIER_TOOLS` env → `git config hooks.atelierTools` → in-repo fallback, so
  atelier itself still works) and **blocks the commit with an explanation** when a
  scanner it is configured to run is missing — a gate that can't scan must never
  pass silently. `create-repo` step 6 now bakes the path
  (`git config hooks.atelierTools "$PP/atelier/tools"`) and prove-it-once
  instructions. Re-exercised: fail-closed with no config, blocks a real secret
  with config, passes a clean commit, atelier's own path unaffected. Suite 137 OK.
- **The fix's contract pinned by tests** (same day, follow-on): the hook was the
  one scan artifact with *no* automated tests — exactly where the defect lived,
  and the live re-proof was one-time (the B1 lesson: a recorded proof can be
  stale by the time it's durable). `tools/test_precommit.py` added — 5 tests
  driving real `git commit`s in throwaway repos: fail-closed when unresolvable,
  config-resolution blocks a planted secret / passes clean, env-wins-over-config,
  in-repo fallback. **Known-failure proven**: the pre-fix sample re-run under the
  same scenario commits the secret with exit 0 — the tests catch the defect
  class, not just bless the fix. Suite 137→142 OK; tools/README wiring section
  now documents `hooks.atelierTools`/`ATELIER_TOOLS` + fail-closed.
- **Owed, surfaced not fixed:** CI templates carry *no* scanner step, so a
  scaffolded repo's only scan gate is the machine-local hook — the "pair it with CI"
  line in both the sample and step 6 is currently unbacked. Wiring scanners into CI
  needs the scanner-distribution decision (vendor / fetch atelier / publish) — the
  deferred supply-chain question; recorded in ROADMAP, not half-built here.

### Changed (2026-07-10 — create-repo rewired to inherit; templates moved into build/)
- **The core Q1 fix landed.** `create-repo` no longer re-encodes the standard from
  memory — it now **inherits from atelier** (the source) and **stamps the standard
  doctrine block + SHA pin** into every new repo's `CLAUDE.md`. The gap this
  closes: the skill had *no CLAUDE.md template at all*, so new repos were born
  with no inlined safety floor, no pointer up, no drift check — the whole
  `PROPAGATION.md` mechanism bypassed at birth. No delivery path now leaves a repo
  wisdom-empty.
- **Templates moved** from the skill's private copy into `docs/build/templates/`
  (18 files) — one source shared by the skill and the published methodology, per
  REPO-STANDARD's decided direction. Added the missing **`CLAUDE.md` template**
  carrying the stamped doctrine block (canonical text stays in PROPAGATION.md).
  Scrubbed of instance residue as they crossed into the shareable repo: `NOTICE`
  holder hardcoded to a company → `<copyright holder>`; `ci-static.yml` project
  name "Nova" → generic; `reviews/README.md` static-web-specific examples →
  type-neutral. Caught one **live drift** that grounds the whole one-source move:
  the `MODEL-ECONOMICS` template still named **ros** as canonical months after it
  was extracted to atelier — fixed to point up to atelier. Verified: residue grep
  clean, `leakscan` clean on the subtree.
- REPO-STANDARD + `build/README.md` updated from "owed" to done: templates now in
  `build/templates/`; the skill *inherits + stamps* rather than re-encodes; the
  seed→rename→fill→stamp→scan→push procedure documented. The skill is machine-local
  (delivery vehicle); it carries only instance specifics (exemplars, git identity,
  `gh` account, `$PP`, default holder, locale) and hard-depends on atelier being
  present — failing honestly if it is not. The stamp's mechanical core was
  dry-run-proven in a scratch scaffold (seed+renames, sizing, all four
  placeholders filled, the drift-check ran verbatim and read "current"); a
  real-repo run (`gh` create + hook install) and a Fable sweep remain owed.

### Changed (2026-07-10 — the post-method-review batch review, PASS-WITH-FINDINGS)
- The gated Fable sweep of `957fa08..f72031c` ran (verdict below the divider in
  `docs/reviews/2026-07-10-post-method-review-batch.md`): floor green (3
  selftests, 137 tests, live runs), 16 findings B1–B16 — every one carrying an
  in-repo fix applied and verified same session, plus two backlog strands (the
  ros access map from B14; a REVIEW.md lifecycle line). The two sharpest were honesty defects of the class the batch
  itself codified: **B1** — the licenscan "live-proven clean" claim was false at
  the commit that recorded it (the scan flagged its own unexempted test
  fixtures; fixed with `.licenscanignore`, re-proven exit 0); **B14** — ACCESS
  pointed at an estate access map ros doesn't hold (wording corrected to honest
  status; ros owes the map). Tool fixes: **B2** `-only`/`+` SPDX suffixes now
  normalise (a `GPL-2.0-only` header mis-tiered block→warn); **B4** `--staged`
  now uses `--diff-filter=ACMR` in both scanners — a renamed-and-edited file's
  added lines were invisible to the hook hot path (proven live both ways);
  **B5** leakscan `--require-terms` fails closed (exit 2) when the local list is
  absent, for hooks/CI expecting full cover; **B7** `tools/README.md` gains
  "What these scans cannot see" — the stated residual false-negative surface.
  Doctrine fixes: REPO-STANDARD's subfolder rule scoped to deployable-artifact
  repos (B8) + no-gate-must-be-stated (B9); RECORD gains the comments-say-*why*
  rule REPO-STANDARD already pointed at (B10); SECRETS gains the honest boundary
  (master-key loss is redundancy-guarded; person-level vault out of scope, B12);
  ACCESS owns its step-5 strengthening + states the one-broad-credential
  fallback (B13); EVIDENCE §13 gains the §11/§13 stakes-win tiebreak (B15);
  REPO-BOUNDARY gains split-*promptly* (B16). Suite 133→137. **The review gate
  is cleared; the create-repo rewire may stack.**

### Added (2026-07-10 — licence-consistency pre-publish gate)
- `tools/licenscan.py` (+ `tools/test_licenscan.py`, 35 tests) — the third
  pre-publish scan, completing the triad: leakscan (no personal data) · secretscan
  (no credentials) · **licenscan (no licence surprise)**. Three checks: LICENSE
  present and SPDX-recognised; every licence declaration (pyproject/package.json/
  Cargo/gemspec/setup.cfg/README badge) agrees with it; no incompatible
  `SPDX-License-Identifier` header (copyleft-into-permissive is a block — can't be
  relicensed on publish). Conservative + advisory (flags for a human, not legal
  advice), `--expect <SPDX>` assertion for CI, zero-dep stdlib, allow-marker +
  `.licenscanignore` escape hatches, `--selftest`. A pre-publish gate, not an
  every-commit hook (private repos carry licence mess harmlessly; it bites at the
  public boundary AUTONOMY already gates). ~~Live-proven clean on atelier itself
  (`--expect Apache-2.0`).~~ *(Correction, 2026-07-10 review B1: false at the
  commit that recorded it — the scan flagged its own unexempted test fixtures.
  Fixed and re-proven clean the same day; see the review entry above.)*
  tools/README documents it; suite 98→133. Reviewed 2026-07-10 (B1–B3).

### Added (2026-07-10 — access onboarding doctrine)
- `docs/method/ACCESS.md` — safe-access-onboarding: the ordered runbook for the
  moment access to a new domain (network/cloud/NAS/workspace/API) is granted.
  Invents no rule; **sequences** the existing ones — grant-recorded-not-originated
  (`AUTONOMY`), narrowest-credential + plane-split, credential-into-store-first
  (`SECRETS`), read-only first ring + reconcile-or-stop (`DATA-PROTECTION`),
  destructive gate encoded *before* destructive power, widen-in-rings each ring
  earned, Zero-Trust the new domain. The active onboarding counterpart to the
  DATA-PROTECTION/SECRETS/AUTONOMY posture; encodes the estate-access expansion as
  doctrine instead of memory. The concrete estate access map stays person-local in
  ros (sensitive topology, protected under DATA-PROTECTION). Slotted into
  method/README as #6 (after SECRETS); the rest renumbered. Reviewed 2026-07-10
  (batch review — B13 strengthening owned + fallback, B14 access-map claim
  corrected; see the review entry above).

### Added (2026-07-10 — the secrets doctrine)
- `docs/method/SECRETS.md` — the *make-rotation-cheap* half that the leak/secret
  scans' *detect* half depends on; extracted from ros §5 (credential triad) + §7
  (secret-store-not-exempt). Reproducible / re-mintable as the enabling property
  (internal secrets rotate mechanically, external re-mint from code behind one
  approval — no hand-kept irreplaceable token); the least → JIT → short-lived
  triad with standing credentials as a tracked debt, not a resting state;
  references-never-values in the right plane (config/device/shareable-repo hold a
  reference, the value lives only in the encrypted store, scans enforce it);
  rotation-on-cadence bounds the undetected-exposure window. Completes the
  *detect → rotate → burn-cost-is-minutes* arc and closes `AUTONOMY.md`'s
  forward-reference to "the secrets doctrine". Instance mechanism (sops+age,
  `!secret` syntax, the credential map) stays in ros. Slotted into method/README
  as #5 (after DATA-PROTECTION); the rest renumbered.

### Added (2026-07-10 — build/ layer: repo-boundary guidance)
- `docs/build/REPO-BOUNDARY.md` — the decision before the standard: whether a
  piece of work is its own repo, a component (folder in an existing repo), or a
  monorepo folder. Decided by independent-lifecycle discriminators (visibility,
  release cadence, ownership/access, reuse, blast radius) rather than size; a repo
  is a unit of independent lifecycle (loose-coupling from PRINCIPLES applied to the
  boundary). The rich client engagement is the worked monorepo case. Standing
  behaviour: advise proactively. When ambiguous, prefer the reversible direction —
  split later is cheap, merge is painful. Indexed in build/README; removed from
  its still-owed list.

### Added (2026-07-10 — build/ layer: the repo standard extracted (A10))
- `docs/build/REPO-STANDARD.md` — the repo-craft standard extracted from the
  `create-repo` skill into readable, forkable doctrine: product-in-a-subfolder
  (+ why), sizing the standard to the repo type, the standard file set,
  **honest-CI** (a green check that proves nothing is the phantom-success
  `method/` forbids an instrument), repo-craft conventions, and the two processes
  (new repo / standardise an existing one). It owns repo *shape* only and points
  up to `method/` for the cross-cutting doctrine (EVIDENCE for grounded-not-
  invented, RECORD for SESSIONS/ADRs/why-comments, REVIEW for the reviews/ briefs,
  PROPAGATION for the CLAUDE.md doctrine block, AUTONOMY for private-first) rather
  than copying it. Instance-local specifics (exemplar repos, git identity, `gh`
  account, workspace path, locale) stay in the delivery vehicle (the skill).
- `docs/build/README.md` rewritten from "pointer, not yet extracted" to the layer
  index; still-owed list now names templates-move, rewire-skill-to-inherit,
  supply-chain/release, and repo-boundary guidance.

### Changed (2026-07-10 — harvest extraction: A6 + A7, the last of the extraction section)
- `docs/method/EVIDENCE.md` gains **§13 source-acquisition escalation ladder**
  (harvest A6) and **§14 honest-instrument doctrine** (harvest A7). §13 is the
  active counterpart to §3: when a claim matters more than its current rung
  supports, climb the recall→snippet→fetch→tool-call→corroborate→reproduce
  ladder — the rung set by *the cost of being wrong, not the cost of climbing* —
  and state the gap when blocked rather than promoting a weak rung. §14 turns
  §1–§4 on the tools the agent *builds*: an instrument's own "ok"/"applied" is a
  claim the apex governs — success means verified not attempted, silent success
  is a defect (PRINCIPLES §6), "unknown" is a required output, and a known-failure
  test is the machine enforcement. Closes the extraction section's last line; the
  ros diagnose/apply phantom-success case-law is now named as §14's estate
  instance in the closing bearing.

### Changed (2026-07-10 — salvaged from the parallel review line)
- `docs/method/EVIDENCE.md` §1 gains the **two-register** provenance rule — a
  durable artifact carries provenance *written down*, an in-flight claim carries
  it *on demand* (answer-on-challenge + label-guesses-unprompted); ceremony
  scales with durability, discipline never drops. This was finding E3 in the
  worktree-branch draft of the method-layer review (`atelier-method-review`),
  which main's verdict had judged "§1 holds" and so never applied. Recovered
  during the worktree reconciliation before that branch was retired.

### Changed (2026-07-10 — harvest extraction)
- `docs/method/MODEL-ECONOMICS.md` promoted stub → **canonical**. Keeps the
  stub's match-the-model / which-pool self-check / tiered-authority /
  inline-batched review triggering, and adds the general session-hygiene
  mechanics + cache economics extracted from ros (per-model prompt cache, TTL
  churn, output>input, one-task-per-session, heavy-skills-are-episodic,
  point-don't-paste, keep-the-hot-path-lean). The estate-specific numbers
  (prices, model roster, measured session-overhead) stay person-local in ros; a
  foot-pointer names the split. README + `method/README` swept off "stub".

### Added (2026-07-10 — method-review backlog finding P2)
- `tools/pins.py` — the fleet view of "which children are stale" against atelier
  HEAD, closing the method-review's remaining backlog finding. The per-child
  drift check (PROPAGATION §4) is pull-based; this is the roll-up — stood in
  atelier it reads every child's pin and reports `current`/`behind N`/`ahead`/
  `diverged`/`unknown`/`no-pin`, with `--log` to show the drift a stale child
  would inspect. Deliberately **read-only**: bumping a pin stays the per-repo
  human-in-the-loop act (PROPAGATION §5), so the tool widens observability, not
  enforcement — the honest caveat in PROPAGATION is updated to say exactly that.
  Zero-dep, `--json`/`--check`/`--selftest`, fail-safe exit codes; 12 stdlib
  tests over real throwaway repos (behind/ahead/diverged/unknown/no-pin +
  discovery). Live-proven on the real fleet: faves 9 behind, ros current.

### Changed (2026-07-10 — method-review backlog finding P2)
- `docs/method/PROPAGATION.md` honest caveat acknowledges the fleet pin view
  (`tools/pins.py`) as the per-child → fleet observability widening, restating
  that it changes nothing about enforcement.

### Added (2026-07-10 — records, not doctrine: no method/ change)
- `docs/decisions/` ADRs 0001–0004 for the decided re-litigable questions
  (method-review finding V2): atelier-is-canonical, SHA-is-the-version,
  private-first, Apache-2.0. Deliberations recorded from the session/review
  record; 0004 is honest that the licence landed at scaffold via the house
  convention and records the reasoning that holds it.

### Changed (2026-07-10 — records, not doctrine: no method/ change)
- `docs/SESSIONS.md` split to index + `docs/sessions/<date>-NN-slug.md` detail
  files (method-review finding V3), entries preserved verbatim — the
  index/detail split RECORD.md prescribes, applied to atelier itself.
- ros `docs/PRINCIPLES.md` trimmed to bearings + case-law (the transitional
  DRY breach closed) — the change lives in ros (`73fd50b`); noted here because
  atelier's ROADMAP extraction item tracked it.

### Changed (2026-07-10 — method/-layer Fable review, PASS-WITH-FINDINGS)
- The gated review of the whole `method/` layer ran; verdict in
  `docs/reviews/2026-07-10-method-layer.md`. Ten findings fixed in the same
  commit: the child doctrine block's inlined floor now names **new trust
  surfaces** (deploy keys/webhooks/OAuth grants — was a silent narrowing of the
  AUTONOMY floor; children adopt at their next pin bump); the drift check says
  to bump even on a non-doctrine delta (alarm-fatigue guard); EVIDENCE §4
  scoped to *reported* facts (direct primary observation is its own
  corroboration), §12 names the ephemeral-claim boundary (no validator reaches
  an in-conversation claim), §8's real fleet figure swapped for an invented
  one; REVIEW reframed — independence + fresh context is the irreducible core
  of review, capability the multiplier not the precondition (cross-references
  swept in PROPAGATION + both READMEs), and the disposition set gained
  **[rejected: grounds]** so disagreement is recorded, never silent; RECORD's
  lockstep rule scoped to the integration boundary (a WIP branch may trail
  until it lands); PRINCIPLES §3/§4/§5/§7 got their generalised cases back
  (the preamble's every-principle-carries-a-case claim is now true); stale
  README/CHANGELOG statements about the PRINCIPLES extraction corrected.
  Backlog: fleet-level pin-staleness view; ADRs for atelier's own decided
  questions; SESSIONS.md index/detail split.

### Added
- `tools/secretscan.py` — the detection half of the secrets story: a zero-dep
  pre-commit/CI scan that blocks a plaintext CREDENTIAL from entering git
  history, in *every* repo (a burned secret is burned whatever the repo's
  visibility). Named vendor formats (AWS/GitHub/Slack/Google/Stripe/Anthropic/
  OpenAI/… tokens, private-key/PGP headers, JWTs) flag on shape; a secret-named
  assignment with a high-entropy value catches home-grown secrets. Skips the
  safe indirections (`!secret`, `${VAR}`, `<placeholder>`), code refs, public
  keys and URL paths — validated at **0 false positives** over real tiki source/
  inventory/docs while still catching the fixture-secret shapes. Report redacts
  to length+entropy, never the value. `--staged`/`--json`/`--disable`/
  `--selftest`, `.secretscanignore` + `secretscan:allow`; 47 stdlib tests. The
  shared pre-commit sample now runs both scanners. Pairs with the SECRETS
  doctrine: detect → rotate → the burn cost is minutes.
- `tools/worktree.py` — one command for `CONCURRENCY.md`'s "one worktree per
  line of work": `start`/`list`/`land`/`remove`. Bakes the doctrine's guards into
  the tool — refuses an iCloud base (sync corrupts a live `.git` index), branches
  off the integration branch so a line never inherits a half-done branch, flags
  stale/dirty worktrees (merge hazards + leaked file handles), and refuses to
  delete uncommitted/unmerged work without `--force`. Zero-dep, `--json`,
  `--selftest`, fail-safe exit codes; 12 stdlib tests over real throwaway repos.
  Makes the parallel-work doctrine a tool, not just prose (Mike, 2026-07-10).
- `tools/leakscan.py` — the mechanical leak-scan (first executable control):
  shareable structural patterns + a machine-local literal-term list, run as a
  pre-commit hook and in CI to keep personal/estate data out of a shareable
  repo. Zero-dep, `--json`, self-tested; caught real address/coordinate leaks in
  its own fixtures on first run. `--disable <rules>` + `--staged <subtree>` scope
  it to a networking repo's shareable subtree (proven on ros `tiki/`).
- Initial scaffold: the `method/` layer stands up first.
- `docs/method/00-APEX.md` — honesty is absolute, then the AI-adapted Three
  Laws (extracted from ros `docs/PRINCIPLES.md` §0, generalised estate-wide).
- `docs/method/AUTONOMY.md` — per-repo autonomy framework; reconciles the
  ros (commit-only) vs faves (commit + push, deploy-on-push) grants.
- `docs/method/STORAGE.md` — GitHub master / iCloud backup / Time Machine→NAS
  whole-machine / laptop disposable; keep churn (venvs, caches, worktrees) out
  of iCloud.
- `docs/method/CONCURRENCY.md` — one worktree per line of work; serialise
  real-world side-effects.
- `docs/method/TOOLBOX.md` — keep a tool manifest; approved-but-missing may be
  installed; the personal inventory stays machine-local, not in this repo.
- `docs/method/PROPAGATION.md` — the propagation mechanism: thin-anchor /
  fat-pointer (inlined safety floor + SHA pin + session-start drift check), the
  standard child doctrine block, the layer-override rule, and the enforcement
  clause (read ≠ complied). Versioning decided: the commit SHA is the version;
  CHANGELOG is the human-readable index; tags reserved for milestones.
- `docs/method/EVIDENCE.md` — the machinery behind the apex's honesty (harvest
  A1): authority tiers, acquisition-method error risk, absolute dating,
  store-the-rule-not-the-value, one-fact-one-home, trigger-based refresh,
  invest-where-the-model-is-weak, enforce-by-machine. Generalised from a private
  reference-library `STANDARDS.md`.
- `docs/method/REVIEW.md` — the enforcement half (harvest A2): independent
  review by a more capable model; three lenses; brief-on-top/verdict-below
  lifecycle; inline-vs-batched triggering.
- `docs/method/RECORD.md` — session + doc-as-code discipline (harvest A3):
  lockstep doc change, append-only session log with detail-on-demand, ADRs for
  re-litigable decisions, absolute dating; the record is what makes a session
  resumable cold.

### Changed
- `docs/method/PRINCIPLES.md` — extracted from stub to the canonical general
  spine (§1–7 + precedence ladder + situation tests, generalised off tiki with
  the cases kept). ros `docs/PRINCIPLES.md` is now the *bearings + case-law*
  child that points up; trimming its transitional general-prose duplication is a
  tracked ROADMAP follow-up.
- README, CLAUDE onramp, LICENSE (Apache-2.0), house `.gitignore` +
  `.claude/settings.json`.

### Pending (see ROADMAP)
- The `build/` layer: the `create-repo` standard + templates.
- `create-repo` rewired to inherit from atelier instead of copying empty
  templates.
