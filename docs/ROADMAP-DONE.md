# atelier ROADMAP — completed detail (archive)

The append-only companion to [`ROADMAP.md`](ROADMAP.md): the case-law of finished
work, moved here so the live roadmap stays lean (the current-truth/history split,
`method/RECORD.md`). **Entries are preserved verbatim** from ROADMAP.md; this
file is a destination that is *meant* to grow (`sizescan` never meters its size;
since 2026-07-22 it checks archive stores for **harvest integrity** — a live
`[ ]`/`[~]`/`⏳` list item here gates the floor: finished history only, `[x]`
with a disposition note where work was superseded or declined).
First harvested 2026-07-14 (ROADMAP.md had reached 1091 lines).

## Doctrine — completed review cycles
- [x] 🎯 **AWA1–AWA4 rulings (AW-application cold pass —
  [`verdict`](reviews/2026-07-23-0330-aw-application-cold.md))** — 0330
  rule-4 application pass, PASS-WITH-FINDINGS 0M/2m/1L/1n; all nine AW
  decision stamps reproduced at HEAD. Ruled 2026-07-23 accept-all,
  walked through one-by-one plain-language; applied by a non-author as the
  **terminal application** of the no-MAJOR pass — the child-template floor
  block joins the propagation sweep list (AWA1), landing = queuing closes
  the pointer window (AWA2, ROADMAP preamble + REVIEW.md rule 4), the
  00-APEX attribution split (AWA3), AWA4 folded into AWA2. Decisions
  stamped; **apex-widening cycle closed**, propagation sweep ungated.
  (Moved from ROADMAP.md 2026-07-23.)
- [x] 🎯 **SCA1–SCA3 rulings (SC-application cold pass —
  [`verdict`](reviews/2026-07-23-0330-sc-application-cold.md))** — 0330
  rule-4 application pass, PASS-WITH-FINDINGS 0M/1m/1L/1n; all six SC
  decision stamps reproduced (PVR re-verified live `enabled:true`). Ruled
  2026-07-23 accept-all; applied by a non-author as the **terminal
  application** — the atelier@main float named as a bounded standing grant
  (SCA1), scanner-fix uptake hedged to the default configuration (SCA2),
  the PVR verify command states its expected observation (SCA3). Decisions
  stamped; **security-canon cycle closed**. (Moved from ROADMAP.md
  2026-07-23.)
- [x] 🎯 **EB1–EB8 rulings (economics cold pass —
  [`verdict`](reviews/2026-07-23-0222-economics-billing-states-cold.md))** —
  0222 rule-4 taker's cold pass, PASS-WITH-FINDINGS 0M/4m/3L/1n; ruled
  2026-07-23 accept-all as counselled; applied `86f8530` by the taker
  session (authored neither doctrine nor verdict) as the **terminal
  application** of the no-MAJOR pass — both indexes + ECONOMICS.md swept off
  the two-pool frame, unknown-cap-distance guard, child template
  de-hardcoded to seats-by-risk; EB8 [backlog] rides AUTONOMY's next edit.
  Decisions stamped in the verdict; cycle closed. (Moved from ROADMAP.md
  2026-07-23.)
- [x] 🎯 **QA1–QA6 rulings (QR-application cold pass —
  [`verdict`](reviews/2026-07-23-0222-qr-application-cold.md))** — 0222
  rule-4 application pass, PASS-WITH-FINDINGS 0M/1m/3L/2n; all nine QR
  rulings verified faithfully applied, QR6's bite reproduced. Ruled
  2026-07-23 accept-all as counselled; applied `5891184` — the
  item-text-never-overrides guard mirrored into the skill and test-pinned on
  both surfaces, eviction extended to README, wording fixes. **Queue-run
  cycle terminal**; decisions stamped; cycle closed. (Moved from ROADMAP.md
  2026-07-23.)
- [x] 🎯 **VA1–VA4 rulings (v2-plugin application cold pass —
  [`verdict`](reviews/2026-07-23-0222-v2-plugin-application-cold.md))** —
  0222 rule-4 application pass, PASS-WITH-FINDINGS 0M/2m/1L/1n; all eight VP
  rulings byte-verified. Ruled 2026-07-23 accept-all as counselled; applied
  `bbaec81` — SIGNING.md + REPO-STANDARD swept to the profile-gated bake,
  VA2 [backlog] folded into the e2e exercise item, skill step-5 comment
  rule, eight facts restored. **v2-plugin cycle terminal**; decisions
  stamped; cycle closed. (Moved from ROADMAP.md 2026-07-23.)
- [x] 🎯 **SA1–SA8 rulings (secrets/access cold pass —
  [`verdict`](reviews/2026-07-22-1021-secrets-access-cold-pass.md))** — ruled
  2026-07-23, accept-all as counselled (SA4 = name the break-glass class,
  SA9 = repo-wide artefact sweep); applied `f8350ee` by a non-author as the
  **terminal application** of the no-MAJOR pass — decisions stamped in the
  verdict, cycle closed. (Moved from ROADMAP.md 2026-07-23; the item's
  original finding summary lives in the verdict.)
- [x] **HI application-pass residue — HA1–HA5, Mike's ruling** — five
  findings from the terminal pass
  ([`reviews/2026-07-22-0943-hi-application-cold.md`](reviews/2026-07-22-0943-hi-application-cold.md)),
  decided into the backlog per the close rule; rule 3 makes them Mike's.
  HA1 (M): the HI-F1 bypass conflates growth stores with non-content dirs —
  a vendored `ROADMAP-DONE.md` under `node_modules/` or `.venv/` reds
  `--check` (probed live); counsel: split `SKIP_DIR_NAMES` into store vs
  non-content sets, bypass only the former. HA2 (M): the unclosed-fence fix
  narrows its fail-open, doesn't close it (count=0 demo); counsel:
  delimiters unbalanced at EOF ⇒ recount the whole file with fences
  ignored. HA3 (L): CI surfaces cold-content-only. HA4 (L): template
  legend overclaim. HA5 (L): RECORD.md antecedent drift.
  *review: not warranted — the cycle's terminal pass reviewed the
  surrounding text; HA1/HA2 land with their own red-leg tests through the
  standing floor.*
  **RULED 2026-07-22 (Mike): "accept your recommendation on all of them" —
  HA1–HA5 [fixed]** as counselled, applied + re-proven same day (suite
  319→323 green, both probes re-driven, red leg reds exactly the four new
  tests); decision stamps in
  [`reviews/2026-07-22-0943-hi-application-cold.md`](reviews/2026-07-22-0943-hi-application-cold.md).
- [x] **HI application cold pass — terminal, cycle CLOSED** (2026-07-22,
  claimed 0943, run same session): the queued rule-4 pass on `30d350c` ran —
  taker a Mike-spawned "do any review work" session that authored neither the
  doctrine, the HI verdicts, nor the application. **PASS-WITH-FINDINGS
  0 MAJOR · 2 MEDIUM · 3 LOW**; every recorded proof re-ran green (suite 319,
  selftest, live scan, red leg re-driven at `30d350c^`); all six [fixed]
  stamps corroborated independently before the deferred material was opened.
  HA1–HA5 decided into the live backlog (🎯, rule 3). The stale
  "Interruption resilience" ROADMAP section (drafting delivered + harvested
  below) came off the hot path with this close. Verdict + reconcile:
  [`reviews/2026-07-22-0943-hi-application-cold.md`](reviews/2026-07-22-0943-hi-application-cold.md).
- [x] **Harvest-integrity gate cold pass — RUN, ruled, applied** (2026-07-22):
  PASS-WITH-FINDINGS 1M/3M/2n; Mike accepted all as counselled; **HI-F1–F6
  [fixed]** in `30d350c` (verdict + stamps:
  [`reviews/2026-07-22-0819-harvest-integrity-gate-cold.md`](reviews/2026-07-22-0819-harvest-integrity-gate-cold.md)).
  The application's own cold pass stays queued `⏳` on the live roadmap.
- [x] **Harvest-integrity invariant — no live checkbox in ROADMAP-DONE**
  **RATIFIED 2026-07-22 (Mike): "I like this idea of embedding it into the
  CI" — build as counselled (extend sizescan; CI embedding comes free via
  the floor's existing `sizescan --check`).** (claimed 2026-07-22-0634,
  wt: harvest-integrity-gate)
  (Mike, 2026-07-22; triggered by IR5 and confirmed real by its first manual
  run — see below). The invariant: `[ ]` / `[~]` / `⏳` state markers must
  never sit in `ROADMAP-DONE.md` — the archive records finished history, and
  a live marker there is either a botched harvest (open work silently
  buried) or an untrue state (done work never flipped). **Deliberately NOT
  delivery-verification of `[x]` items** (Mike's explicit bound — overhead
  too high); this checks *state coherence*, one grep's worth of cost.
  - **Counsel — extend `sizescan`, not a new tool**: it already owns the
    ROADMAP↔ROADMAP-DONE seam and reads both files; add a red on live
    markers in any `*-DONE` store, with a machine-readable escape for
    sanctioned non-delivery states. Legend gains one state for those:
    `[-]` **dropped** `— superseded / no longer required: <grounds>` — the
    only live-box-shaped thing the archive may hold.
  - **On hit, the finding is investigative, never auto-fixed**: the session
    that reds checks the evidence (children's states, sessions log, the
    codebase) for delivered-but-unmarked vs genuinely-open, then notifies
    Mike with the evidence and a recommendation — flip with a dated note,
    un-harvest back to ROADMAP, or mark `[-]` dropped. The scanner finds;
    the agent investigates; Mike decides.
  - **First manual run already caught one**: a `[ ]` parent
    ("Batch-review follow-ups") sat in ROADMAP-DONE with both children
    `[x]` DONE — delivered, never flipped; corrected with a dated note
    (this session). *review: WARRANTED when built — a CI gate is
    policy-as-code doctrine; brief owed at pickup.*
  **BUILT 2026-07-22, delta `0bdccf3`** (suite 302→314 green; live repo
  scan green). Two counsel points superseded by Mike's mid-build rulings,
  disposition noted: the `[-]` dropped state was replaced by the
  **work-owed tri-state** ([x] = no more work owed, disposition in the
  item's text); the "one grep" scope grew line-based parent/child
  coverage per Mike's four-situation taxonomy. Review queued ⏳ (rule 4).
- [x] **Interruption-resilience cycle — IR1–IR4 await Mike's ruling** —
  the rule-4 cold pass on `9c11525` returned **PASS-WITH-FINDINGS
  0 MAJOR · 3 MEDIUM · 2 LOW**, so the cycle is closed terminal (close
  rule); the findings are decided into this backlog item (rule 3 — Mike's).
  Verdict + counsel per finding:
  [`reviews/2026-07-22-0257-interruption-resilience-cold.md`](reviews/2026-07-22-0257-interruption-resilience-cold.md).
  IR1 (M): the CLAUDE.md onramp tell overclaims — "no closing entry means
  died mid-flight" also matches a live sibling (live-proven); counsel:
  one-line reword to "died or still live — sweep read-first before assuming
  either". IR2 (M, the author's flagged sub-question): the child CLAUDE.md
  template onramp carries no firing pointer; counsel: propagate one
  sentence via `<atelier-path>`, worded per IR1's correction, at next pin
  bump. IR3 (L): two lines over-wrap (~153-col aside, ~109-col table row).
  IR4 (L): the resume-breadcrumb grammar isn't in the ROADMAP legend.
  IR5 (M, records hygiene) is already **[fixed]** — the authoring session
  left an un-harvested `[x]` redding the shared floor on `main` for three
  pushes; harvested by the reviewing session (this commit), floor re-proven
  green. *review: not warranted — applying the rulings is line-level
  mechanical; the cold pass just reviewed the surrounding text.*
  **RULED 2026-07-22 (Mike): "I take your recommendations on these" —
  IR1–IR4 [fixed]** as counselled, applied + re-proven same day; decision
  stamps in `reviews/2026-07-22-0257-interruption-resilience-cold.md`.
- [x] **Scope/lens-4 cycle residue — AC1 + AC2, Mike's ruling** — two LOW
  findings from the terminal pass
  ([`reviews/2026-07-22-0244-sl-application-cold.md`](reviews/2026-07-22-0244-sl-application-cold.md)),
  decided into the backlog per the close rule; rule 3 makes them Mike's.
  AC1: `build/templates/CONTRIBUTING.md:44` is 122 cols (SL3's edit
  re-shipped the wrap class SL7 fixed) — counsel: one-line rewrap, no
  meaning touched. AC2: the review-brief skill's scanner clause omits the
  exclusion-barred caution (a clean pass over a barred file class is
  definitionally empty) — counsel: half a sentence at the next skill touch.
  *review: not warranted — applying two LOW rulings is mechanical; the
  cycle's terminal pass already reviewed the surrounding text.*
  **RULED 2026-07-22 (Mike): "agreed I accept both per your counsel" —
  both [fixed]**, applied + re-proven (suite 302 green) same day; decision
  stamps in `reviews/2026-07-22-0244-sl-application-cold.md`.
- [x] **Draft the three interruption-resilience gaps as one doctrine change**
      (landed `9c11525`, 2026-07-22) —
      - **Gap 1 (high): the resume-state carrier doesn't exist at the cut.**
        The session log is written at *close*; interruptions precede close, so
        a cut session leaves a clean tree but no *intent*. Fix: a durable
        in-flight breadcrumb (extend the claim line — `at: <step>, waiting on
        <X>`), updated as work moves. Overlaps the queue-run strand's per-item
        close (line ~122); reference, don't duplicate.
      - **Gap 2 (medium): decision-limbo.** A pending `🎯` question lives only
        in volatile chat; a dropped window loses it. Fix: write the open
        question into the record before blocking on it.
      - **Gap 3 (low): the recovery procedure isn't in method.** The cmd+Q
        sweep is twice-grounded (session 45, 2026-07-20) but lives in a session
        log. Fix: distil the checklist (tree/sync/stashes/orphan worktrees/
        reflog-after-close/respect sibling lanes) into CONCURRENCY, plus a
        resumer tell — did the last session close clean or die mid-flight?
      Cycle: cold pass PASS-WITH-FINDINGS 0M/3M/2L, closed terminal
      2026-07-22 (`reviews/2026-07-22-0257-interruption-resilience-cold.md`).
- [x] **Review-line artefact cycle — RS1–RS6, closed 2026-07-21** (delta
      `fa7a90f`; verdict + decisions in
      `reviews/2026-07-21-0913-review-line-artefact-cold.md`). The rule-4
      cold pass (taken from the `⏳` queue by a Mike-spawned non-author,
      claim-first, findings-before-deferred-material): **PASS — 0 MAJOR /
      1 MEDIUM / 5 LOW**, every recorded proof reproduced. Mike ruled
      **accept-all**; terminal application by the counsel's author
      (wt: review-line-rs-apply, `c06c0a4`): RS1 explicitly-named paths are
      scanned, never silently matched by nothing (dir/file-direct legs
      proven red); RS2 fenced `review:` is a quoted example, not a
      judgement; RS3 the field requires a non-empty value; RS4 backdate
      residual stated, all-caps accepted; RS5 REPO-STANDARD's scanner
      enumeration → non-staling pointer; RS6 the 0820 addendum splice
      unwound with the restoration annotated. Suite 293→298. No MAJOR ⇒
      cycle closed without a further pointer. The cycle's queue pointer was
      the first to honour rule 4's refs-only ceiling — the ROADMAP-header
      point-of-use fix proven on first exercise.
- [x] **REACH/AUTONOMY backlog — H1–H8 + residuals, closed 2026-07-21**
      (findings in `reviews/2026-07-13-reach-batch-applied.md`; counsel in the
      `2026-07-21-0736` session record). Agent-grade applied first (H8 the
      browser-fetch README alignment pass + two REACH.md rewraps); Mike then
      ruled **accept-all** on H1–H7 + the machinery-mediated-repurposing
      residual (R1) and the same session applied them
      (wt: worktree-reach-rulings-apply): H1 operator/principal defined +
      team-adoption clause; H2 riding scoped to in-place use (doctrine + the
      instance README); H3 purpose-governs-stores / mint-vs-ride-governs-acts,
      autofill is a mint; H4 resource-owner residual named; H5 "blocked"
      defined; H6 rung-1/2 equivalence hedged; H7 standing-reach join; R1
      AUTONOMY secrets bullet catches unprovisioned machinery-mediated use.
      Rulings of a no-MAJOR pass ⇒ **terminal application, no pointer**
      (decisions stamped in the verdict's 2026-07-21 addendum).
- [x] **Fleet re-stamp of the reviews template** — unblocked 2026-07-19 (cycle
      closed terminal on Mike's 0629 ruling; G1's blocker cleared — pin slot
      reworded, prove-the-stamp grep green re-proven on a full scaffold).
      **Done 2026-07-21** (wt: worktree-review-owed-triple): nova, numen, shed
      — the three children carrying the drifted pre-trigger copy — re-stamped
      from the closed-cycle template, `<atelier-path>` filled `../atelier`,
      no-placeholder grep + pointer resolution proven per child, committed and
      pushed (nova `13f6970`, numen `d271ae0`, shed `118fc69`). Other template
      deltas reach children at their own pin bumps, per the item's design.
- [x] **DOCUMENTATION doctrine — what great documentation is, per audience and
      consumer (Mike, 2026-07-20, raised in ros off the tiki CLI-UX review).**
      (**claimed 2026-07-20 1423 UTC** — Mike ruled "1–3 I accept your
      recommendations"; the taker applies DD1–DD4, wt: `atelier-rulings-apply`.)
      **Cold pass RAN 2026-07-20**
      (`reviews/2026-07-20-1355-documentation-draft-cold.md`): **PASS — 0 MAJOR
      · 2 MEDIUM · 2 LOW**; every grounding claim re-ran true at ros `806eb10`.
      🎯 **Mike's rulings owed:** DD1 (table drops the developer cell) · DD2
      ("map directly" overclaim) · DD3 (inventory misses tests / commit
      messages / diagrams) · DD4 (no competing draft exists — decide whether
      this cold pass discharges the reconcile intent). No-MAJOR ⇒ closes
      terminal on ruling. tiki application half still owed (ros's lane).
      Mike: *"be clear on what great documentation looks like, and its
      purpose"* — for **audiences** developer vs operator × newbie vs expert,
      and **consumers** human · AI · orchestrating software — covering
      *"everything from docstrings to the --help screen on a CLI app … to the
      man file and a wiki. And any other form of documentation you can think
      of."* Belongs HERE because it binds every child repo; **tiki (ros) is
      the named exemplar / real-world proving ground** (its ROADMAP carries
      the application half, same day). Scope for the method doc
      (`method/DOCUMENTATION.md` when authored): the audience×consumer
      matrix and what "great" means per cell · the artefact inventory
      (docstrings · CLI --help · man pages · README · canon docs
      (PURPOSE/ARCHITECTURE/GLOSSARY-class) · wiki/tutorials/examples ·
      error messages as documentation · the machine contract (--json
      schemas, exit codes) as documentation-for-software · changelogs ·
      session/decision records) · the single-source/pointer rule (a fact
      lives once; everything else points) · same-commit currency (docs
      change in the commit that changes the behaviour — the man-page rule
      generalised) · honesty in docs (claims carry their proving rung) · and
      the **third-party-docs seam**: a child's docs state its own intent +
      live-proven deltas/quirks, and POINT to vendor docs (RouterOS,
      VirtualBox, …) — never mirror them. Existing part-truths to absorb,
      not duplicate: RECORD.md (records), the CLI-docs standard cycle
      (ROADMAP-DONE), CONVENTIONS.md, ros PRINCIPLES §6 legibility.
      *review: WARRANTED — doctrine; author, Fable-review, THEN propagate
      (mechanism-before-content). The tiki application pass is the review's
      evidence base.*
      **Decisions to date (Mike, 2026-07-20):** (1) **anchor on Diátaxis**
      (tutorial · how-to · reference · explanation) and extend as needed —
      the least-invented path; (2) the **consumer axis** (human · AI ·
      orchestrating software) is the extension Diátaxis lacks; (3) fold the
      independently-surfaced deltas — the **developer** audience is a distinct
      cell Diátaxis's *explanation* mode serves, easy to conflate with
      expert-*user*; atelier's **record doctrine already IS the AI-reading
      standard** (resume-cold, one-fact-one-home, grounding, absolute dating —
      so that cell is *extraction*, not invention); **version-pin the vendor
      pointer** ("verified against RouterOS 7.x", not a bare link).
      **Draft authored 2026-07-20 (Opus) at `method/DOCUMENTATION.md`** —
      registered in `method/README.md` (15), grounded read-only against
      ros @ `806eb10` (tiki.1 MACHINE OUTPUT/CAVEATS/SEE ALSO, PRINCIPLES §6,
      EVIDENCE §9, RECORD). Mike commissioned this as **one candidate**, to be
      **cold-reviewed against any competing draft and reconciled** — so unlike
      the earlier note, a competing draft *is* deliberately open. *review
      state: `⏳` queued — a non-author session takes it (REVIEW.md rule 4),
      reconciles the drafts, and applies. Author does not self-review. tiki
      application (ros half) still owed and is the review's evidence base.*
      **CYCLE CLOSED 2026-07-20** — Mike ruled all counsel accepted; applied `87af9f9` (terminal, no-MAJOR). Verdict + decisions: `reviews/2026-07-20-1355-documentation-draft-cold.md`.


- [x] **CONCURRENCY posture flip — "assume you are not alone"** (Mike,
      2026-07-20).
      (**claimed 2026-07-20 1423 UTC** — Mike ruled "1–3 I accept your
      recommendations"; the taker applies CF1–CF7, wt: `atelier-rulings-apply`.)
      **Cold pass RAN 2026-07-20**
      (`reviews/2026-07-20-1355-concurrency-flip-cold.md`): **PASS — 0 MAJOR ·
      4 MEDIUM · 3 LOW**; flip judged sound and live-executed by the pass
      itself. 🎯 **Mike's rulings owed:** CF1 ("truly-alone pays nothing"
      overclaim) · CF2 (cue-relax sentence reads backwards) · CF3
      (dirty-primary claiming gap) · CF4 (child-block catch-up homeless —
      needs its own line) · CF5–CF7 (LOW wording). No-MAJOR ⇒ closes terminal
      on ruling. `CONCURRENCY.md` § The trigger now leads with a concurrent
      prior instead of a solo one: the dirty-tree backstop has a blind spot —
      the doctrine's own commit-small-push-fast hygiene leaves a *clean* tree
      between a disciplined parallel session's commits, so a clean tree is not
      evidence of solitude. Precaution scales with the write (read = none ·
      light single-commit = sync + claim · write-heavy/multi-commit = worktree
      by default). Solo default reframed: "solo" is a conclusion earned from
      evidence, not assumed from silence. `CLAUDE.md` onramp rule 1 restated to
      match. *review: WARRANTED — doctrine change (reverses the prior of a
      decided section); queued for an independent session per REVIEW.md rule 4 /
      review-brief-independence. Author (this session) does not self-review.
      Watch: whether the risk-scaled ladder over-taxes light sessions, and
      whether "positive evidence you are alone" is crisp enough to act on.*
      **CYCLE CLOSED 2026-07-20** — Mike ruled all counsel accepted; applied `87af9f9` (terminal, no-MAJOR). Verdict + decisions: `reviews/2026-07-20-1355-concurrency-flip-cold.md`.

- [x] **Session-onramp operating-rhythm — surface the working beat to every
      session** (Mike, 2026-07-20).
      (**claimed 2026-07-20 1423 UTC** — Mike ruled "1–3 I accept your
      recommendations"; the taker applies SR1–SR4, wt: `atelier-rulings-apply`.)
      **Cold pass RAN 2026-07-20**
      (`reviews/2026-07-20-1355-onramp-rhythm-cold.md`): **PASS — 0 MAJOR ·
      2 MEDIUM · 2 LOW**; reframe judged sound, cue parity re-proven (suite
      20 OK), sizescan red confirmed deliberate. 🎯 **Mike's rulings owed:**
      SR1 ("stay in your lane" has no home doc — author it or drop the
      clause) · SR2 (block 48 lines vs "~15" spec — re-ground or shrink) ·
      SR3–SR4 (LOW wording). No-MAJOR ⇒ closes terminal on ruling. Detail →
      [session](sessions/2026-07-20-1302-session-onramp-operating-rhythm.md).
      Finding: Mike's standing per-session instructions are already grounded
      doctrine in `method/*` but never *reach* a session — the only always-loaded
      surface (the child doctrine block, `PROPAGATION.md`) inlines the *safety
      floor* only. A reach gap, not a content gap. **Authored (applied):** (A)
      `CONCURRENCY.md` — a live `[~]` claim **outranks a standing instruction** to
      take that item; (B) `MODEL-ECONOMICS.md` item 7 — **surface the session
      boundary** + **stop safely under overload**; (C) `RECORD.md` — the close-out
      **all-clear carries its evidence**, not a bare "done". Dropped
      "think step-by-step" (ungrounded); folded "focus on given work" → "stay in
      your lane". **APPLIED — the child-block cue** (Mike ruled *yes* 2026-07-20, the
      block may carry an operating beat, not only the floor; decoupled from the
      concurrency-flip catch-up as standalone): a **Session rhythm** bullet now
      lives in `PROPAGATION.md`'s canonical block **and** `build/templates/
      CLAUDE.md` —

      > - **Session rhythm (points up for the full rule):** claim work before
      >   starting it, and let a live `[~]` claim override a standing instruction
      >   to take that item (`CONCURRENCY.md`); stay in the lane you were given;
      >   flag when economics favour a fresh session, and on overload stop at a
      >   safe point, record, and hand off (`MODEL-ECONOMICS.md`); before your
      >   final verdict, do the put-away unprompted and close with an
      >   evidence-based all-clear that nothing owed is left uncaptured
      >   (`RECORD.md`).

      *Still owed on the block, but NOT this item's:* the concurrency-flip
      (`295d94a`) catch-up — the block's Concurrency bullet still carries the
      pre-flip "dirty tree ⇒ another session live" wording; that propagation is
      the concurrency cycle's job. *review: WARRANTED — three method docs + the
      block cue; rule 4, independent, author does not self-review. Watch: whether
      the cue earns its lines in a block spec'd ~15 lines.*
      **CYCLE CLOSED 2026-07-20** — Mike ruled all counsel accepted; applied `87af9f9` (terminal, no-MAJOR). Verdict + decisions: `reviews/2026-07-20-1355-onramp-rhythm-cold.md`.
- [x] **CLI-docs standard — applied-batch cold pass reviewed, ruled, applied,
      CYCLE CLOSED 2026-07-17.** PASS-WITH-FINDINGS (0 MAJOR · 2 MEDIUM ·
      3 LOW), all seven prior rulings reconciled as faithfully implemented;
      Mike ruled F1–F5 [fixed] as counselled, applied + verified same day
      (man-page `EXIT STATUS` + layout-drift alarm; CI mandoc made real;
      unconditional man cleanup; "a closing line or two"; README manifest
      wording). Verdict + decisions:
      `reviews/2026-07-17-1157-cli-docs-applied-cold.md`. 0 MAJOR ⇒ the
      terminal application closes without a queued pointer (close rule).
- [x] **ADR 0006 addendum (ccarchive, the *preserve* verb) — reviewed, ruled,
      applied, CYCLE CLOSED 2026-07-17.** Cold pass PASS-WITH-FINDINGS
      (0 MAJOR · 1 MEDIUM · 3 LOW); Mike ruled F1–F4 [fixed] as counselled,
      applied + pinned same day (shrink guard `--force`, repo-dest guard
      `--allow-repo-dest`, layout-drift alarm, strict `--verify`; ccarchive
      tests 27→35). Verdict + decisions:
      `reviews/2026-07-17-1000-adr0006-ccarchive-preserve-cold.md`. 0 MAJOR ⇒
      the terminal application closes without a queued pointer (close rule).
- [x] **CONVENTIONS + UTC-at-rest ADR — applied-batch cold pass reviewed,
      ruled, applied, CYCLE CLOSED 2026-07-17.** PASS-WITH-FINDINGS (0 MAJOR ·
      1 MEDIUM · 5 LOW), the six prior rulings reconciled as implemented with
      one reconcile-stage drift caught (F6); Mike ruled F1–F6 [fixed] as
      counselled, applied + verified same day (seventh minting site UTC'd;
      row dated + foreign-formats line restored; ingestion clause scoped;
      reflows; CONCURRENCY→ADR-addendum pointer). Verdict + decisions:
      `reviews/2026-07-17-1157-conventions-utc-applied-cold.md`. 0 MAJOR ⇒ the
      terminal application closes without a queued pointer (close rule).
Closed doctrine review cycles (REVIEW rule 4, MODEL-ECONOMICS triple delta,
"informed principal" apex rule, PRINCIPLES §2 four bullets — all CYCLE CLOSED
2026-07-14/15) → [`ROADMAP-DONE.md`](ROADMAP-DONE.md) § Doctrine — completed
review cycles.
- [x] **REVIEW rule 4 — CYCLE CLOSED 2026-07-15.** Drafted from Mike's
      tiered ruling → cold pass (1 MAJOR — the spawner enumeration weaker
      than the ruled criterion) → F1–F8 ruled + applied → applied-batch cold
      pass **PASS-WITH-FINDINGS — 0 MAJOR · 2 MEDIUM · 5 LOW**, all eight
      rulings verified faithfully encoded, every claimed proof reproduced →
      Mike ruled F1–F7 as counselled, applied same day: the applier seam
      conditioned on an open cycle (terminal application queues no pointer);
      the `⏳` pointer spec now a ceiling as well as a floor (refs only, no
      evaluative account); MODEL-ECONOMICS §Sub-agents carries the full
      criterion; spawn provenance; the legend defines `⏳`; an application
      review tests the delta's author at minimum. Verdicts:
      `reviews/2026-07-15-1202-review-rule4-cold.md` +
      `reviews/2026-07-15-1244-review-rule4-applied-batch-cold.md`. 0 MAJOR
      ⇒ closed on the ruled application (close rule). Propagates on the next
      pin bump.
- [x] **MODEL-ECONOMICS triple delta — CYCLE CLOSED 2026-07-15.** Sub-agents
      (isolation-not-savings, when/when-not, lossiness), explicit tier
      selection (cheapest model that genuinely does the work — verifiability
      test, pool-anchored, price-the-job), hygiene item 4 (reset by record,
      not compaction; no numeric thresholds). Cold pass **PASS-WITH-FINDINGS —
      0 MAJOR · 3 MEDIUM · 3 LOW**; Mike ruled F1–F6 **[fixed]** same day
      (F1 re-ruled after a plain-language walk-through → the tiered rule now
      in REVIEW rule 4, item above) and supplied the price-the-job nuance,
      applied with the batch.
      Verdict + ruling: `reviews/2026-07-15-0910-model-economics-triple-delta.md`.
      0 MAJOR ⇒ closed on the ruled application (close rule). Propagates on
      the next pin bump; child template swept (F6).
- [x] **"Informed principal" apex rule — reviewed, applied, CYCLE CLOSED
      2026-07-14.** New `00-APEX.md` subsection *The principal's authority is
      conditioned on being informed* (now under *Honesty is absolute*). Cold
      pass by an independent reviewer (not the author): **PASS-WITH-FINDINGS —
      0 MAJOR · 4 MEDIUM · 3 LOW**, verdict in
      `reviews/2026-07-14-2235-informed-principal-apex-cold.md`. Mike ruled
      **F1–F5 [fixed]** (F1 apex list unified to cover governance rulings *and*
      floor stops so the child stamp stops out-scoping the parent; F2 teeth
      re-pointed at the agent's *withholding* + principal's right to *waive*
      once informed — Second-Law bind removed; F3 trigger runs both directions
      incl. principal-initiated overrule; F4 AUTONOMY + COMMUNICATION pointers
      added, asymmetry gone; F5 section demoted to a subsection under honesty),
      F6 folded into F5, F7 no-action. No MAJOR ⇒ cycle closed without a further
      ceremony (close rule). Floor green (247 tests · sizescan · linkscan).
      Propagates fleet-wide on the next pin bump.
- [x] **PRINCIPLES §2 four bullets — CYCLE CLOSED 2026-07-15 (escape valve;
      Mike ruled directly).** Applied-batch cold pass by an independent
      session (neither author nor applier): **PASS-WITH-FINDINGS — 1 MAJOR ·
      1 MEDIUM · 2 LOW**, four of five prior fixes verified clean at the
      primary sources; verdict + the principal's ruling in
      `reviews/2026-07-14-2333-principles-s2-applied-batch-cold.md`. MAJOR
      count flat across passes (1 → 1) ⇒ escape valve: Mike ruled F1–F4 in
      person, supplying the intent — **F1 [fixed] by re-scope**: API first
      binds *where we design the service* (contract first, logic behind the
      API, front end holds presentation only); consuming a third-party system
      is out of scope — tiki/RouterOS re-grounded as the consumption case
      stated honestly (REST for convergence, SSH/SFTP where REST doesn't
      serve — stated choices, not drift). F3 [fixed] subsumed (vendor-UI-seam
      clause gone); F2 [fixed] discriminator stated (a web fork adds no
      capability; a native app is a different medium riding the API
      contract); F4 [fixed] bullet rewritten in short sentences. The false
      source killed at origin: ros `rescue.py` stale "one non-REST step"
      comment fixed + pushed (ros `261fca2`). Every grounding claim
      re-verified at ros HEAD before writing; floor green (247 tests ·
      sizescan · linkscan). Propagates on the next pin bump.
- [x] **Applied-batch cold pass — CONCURRENCY "Claiming work" fixes — RAN
      2026-07-13, cycle CLOSED.** Un-briefed pass over the applied edits:
      **PASS-WITH-FINDINGS, no MAJOR** → cycle terminates per REVIEW.md. All
      seven fixes confirmed in-text and live-reproduced (same-item → conflict,
      adjacent → keep-both, spaced → clean). Two residuals, Mike ruled **both
      [fixed]**, applied same day (cycle already closed → no further pass): a
      MEDIUM the fix-2 reframe opened beneath — *how* a parallel session reaches
      `main` (git checks it out in one place; claim from the primary checkout
      before `git worktree add`) — and a LOW inherited imprecision (the
      three-line-context parenthetical was wrong; adjacency = no unchanged line
      between). Verdict + decisions in
      `reviews/2026-07-13-2256-claiming-work-applied.md`. Also spun out: a
      RECORD.md note that record ids are long/hyphenated by design so downstream
      validators/scanners must allow the shape (bearing: a sibling repo's
      validator tripped on a 46-char id; atelier's own scanners pass them clean).
- [x] **Cold review of CONCURRENCY "Claiming work"** — RAN 2026-07-13, un-briefed
      (reviewer chose its own attack surface): **PASS-WITH-FINDINGS**, verdict +
      decision in `reviews/2026-07-13-concurrency-claiming-work.md`. Core
      mechanism live-verified sound; **1 MAJOR · 4 MEDIUM · 2 LOW**. Mike ruled
      **all seven [fixed]**, applied same day. The MAJOR was real: the section
      gated claiming to worktree-mode, whose only reliable trigger is the
      principal's say-so — exactly the condition the grounding incident broke —
      so it wouldn't have fired in the case it was built for. Fix (option A,
      decouple): claiming now keys on **selection from the shared queue**, claim
      commit lands on `main` before branching. MEDIUMs: bundled lines serialise
      (fan-out needs per-leaf lines); adjacent one-line claims raise a trivial
      keep-both conflict (live-verified, "silent everywhere else" was false);
      put-away gained the `[~]`→`[ ]` reversion; tracker-based adopters pointed
      at the assignee primitive. LOW: timestamp demoted to a tiebreak.
      **Applied-batch cold pass owed** (above).
- [x] **Cold pass on the applied REACH batch — RAN 2026-07-13, same day:
      PASS-WITH-FINDINGS, no MAJOR — cycle CLOSED** per the stopping rule.
      Verdict verbatim in `reviews/2026-07-13-reach-batch-applied.md`.
      Fidelity 8/8 confirmed (two immaterial deviations, labelled, no drift
      label owed); the instance proof re-run 11/11. Eight findings H1–H8
      (four MEDIUM, four LOW) + two reconciliation residuals — none unseats
      an applied decision — consolidated onto the backlog item below, no
      further ceremony per the rule.
- [x] **REVIEW.md reviewer-independence rule — decided 2026-07-13, all
      fixed.** Two cold reviews ran: 2026-07-12 (scoped to the three independence
      edits, I1–I7, 3 MAJOR — `reviews/2026-07-12-review-independence.md`) and
      2026-07-13 (principal-commissioned, un-briefed, whole-doc, F1–F7 —
      `reviews/2026-07-13-review-doctrine-second-pass.md`). Mike ruled
      both batches **[fixed]**, choosing floor-not-fence on the seeded-questions
      fork and adding his own strengthening (questions influence by their very
      existence — the reviewer guards against their topic/tone steering its
      surface). Applied 2026-07-13 to REVIEW.md + PROPAGATION.md by a session
      that authored neither the doctrine nor either verdict; decisions
      stamped in both verdict files.
- [x] **Cold review of the applied independence batch — RAN 2026-07-13,
      decided same day: all nine [fixed], applied, cycle CLOSED.** Mike
      ruled the loop question directly: the cycle closes when a pass returns no
      MAJOR (this one did), and if MAJORs ever stop falling pass-to-pass, stop
      and ask him — both now encoded in REVIEW.md's application paragraph,
      alongside his endorsement of G1's structural fix (seeded questions defer
      below the brief's divider). This application spawns no further ceremony
      per the rule it encodes. **PASS-WITH-FINDINGS**, verdict verbatim in
      `reviews/2026-07-13-independence-batch-applied.md`. Fidelity confirmed:
      14/14 decisions faithfully applied (one deviation judged the right
      call — F2's pre-fork wording harmonised with the floor-not-fence
      decision). Nine findings G1–G9, five MEDIUM, none blocking: G1 the rule-1
      ordering instruction is behavioural where the house demands structural —
      exposure to seeded questions primes at read time, so defer them below the
      brief's divider (or name the ordering as mitigation-not-cure); G2 rule 3
      is wrongly conditioned on brief authorship (its true trigger is
      self-authored doctrine, however commissioned) and step 4 already says so;
      G3 the standing test's "passes clean" trigger keys on finding count — the
      metric F1 just evicted — and would not have fired on the REACH case
      itself; G4 the doctrine-review regress needs a stopping rule and the
      neutral-applier pattern deserves encoding; G5 application reviews can't
      honour rule 2 (the delta carries the decision stamps) — needs
      sequencing guidance. G6–G9 small wording/staleness. Applier's counsel,
      labelled (the applier authored the reviewed edits, so decides nothing):
      take all nine — G2/G6–G9 are mechanical; G1 suggests the deferred-
      questions brief shape (structural, matches rule 2); G3's re-key and G4's
      no-MAJOR stopping rule read sound; G5 pairs with G4's paragraph.
- [x] **REACH.md adversarial re-review — DECIDED 2026-07-13: all eight
      [fixed], applied same day** to `REACH.md` (A1–A8) + `AUTONOMY.md` (A1's
      matching secrets-floor carve-out, so the two docs state one rule) by a
      session that authored neither the doctrine nor the verdict; decisions
      stamped in the verdict file. **Cold pass on the applied batch owed**
      (REVIEW.md's cycle rule — tracked below). Original item follows:
      ~~DECISION OWED, Mike's, not the
      author's.** RAN 2026-07-12 (session 47's post-session self-review found
      the first review author-briefed — cold context, warm questions — so an
      un-briefed adversarial pass was commissioned; it chose its own attack
      questions and was barred from the prior review until its own verdict was
      drafted): **PASS-WITH-FINDINGS**, verdict in
      `reviews/2026-07-12-reach-rereview.md`. Eight findings A1–A8, **none
      overlapping the first review's five**; two MAJOR, both on the credential
      boundary reading more permissively than decided practice (A1 "no further
      permission needed" vs AUTONOMY's always-confirm secrets floor; A2
      ride-a-session unscoped beyond fetch-only). The reviewer's judgement of
      the first review: tier right, basis unsound — every pre-seeded question
      pointed where the author was already looking. Findings await **Mike's**
      decision; the doc's author applies nothing here on its own.~~
- [x] **Cold review of `method/REACH.md`** — RAN 2026-07-12 (cold
      fresh-context agent): **PASS-WITH-FINDINGS**, verdict in
      `reviews/2026-07-12-reach.md`. All four sharp questions cleared green — the
      ladder is a faithful abstraction with no invented rungs (generic 1–6 maps
      1:1 onto the Chrome-only instance, the partial-instance gap disclosed
      verbatim from this item); the two-halves join is *argued* on a real
      mechanism (same event at rungs 4–5), not asserted; the purpose-of-storage
      test covers the estate's cases without outlawing the one use the ladder
      exists for (riding the live session); no person-level leak (password
      manager named as a class, the ROADMAP's `Apple Passwords` instance
      correctly kept out). **5 findings R1–R5, all [fixed] same day** — none
      blocking, one theme (adopter-clarity + one genuine seam): R1 "the estate
      registry"/"keychain" definite references an outside adopter can't resolve →
      indefinite "a provisioning registry's entries"; R2 operator/principal
      identity the join leans on now *stated* where the halves meet; R3 the seam
      between the purpose test and the categorical browser rule closed (a
      browser's saved-credential store is never itself the provisioned path —
      ride, don't mint, whichever profile); R4 the rung-4/5 one-mechanism caveat
      pulled up beside the ladder; R5 the grant exception signalled at first
      statement ("without an explicit grant").
- [x] **Cold review of `method/COMMUNICATION.md`** — RAN 2026-07-12 (cold
      fresh-context agent, barred from the person-level layer by the brief so
      the leak question was judged as a genuine outside reader):
      **PASS-WITH-FINDINGS**, verdict in `reviews/2026-07-12-communication.md`.
      The sharpest question cleared: the scrubbed worked example does NOT leak
      the personal layer by implication — the join it creates is identity ×
      category-existence with zero specifics, and the categories named in the
      scrub note are the ones the repo's boundary statement already publishes.
      Axes grounded (unevenly evidenced, honestly so); decline-then-revisit
      read as append-only honesty, not relitigation. 4 findings C1–C4, all
      [fixed] same day — one theme: the doc held the boundary rigorously but
      was looser on itself (enforcement unstated → write-time-discipline-only
      now named; the not-even-private rule's divergence from the portability
      north star surfaced, kept strict with the reconciling why; the worked
      example dated as a snapshot per EVIDENCE §7/§9; the "works without the
      reader knowing it" overclaim sharpened to *functions* without it).
- [x] **Cold review of RECORD "keep private repos generic"** — RAN 2026-07-12
      (cold fresh-context agent): **PASS-WITH-FINDINGS**, verdict in
      `reviews/2026-07-12-record-private-repos-generic.md`. The central clause
      held; the naming clause was mis-drawn — the harmful class is the **join**
      (a private repo's name × its sensitive posture), not the name, and the
      rule as written outlawed the repo's own records while the actual join
      survived the original scrub in four places. 7 findings R1–R7, all
      [fixed] same day: section redrafted (the join is the regulated class;
      name-only mentions sanctioned behind a load-bearing-name test, e.g.
      ros/faves/numen; enforcement stated honestly — write-time discipline +
      review sweeps, no mechanical floor exists; scrub-of-HEAD-is-not-
      remediation now opens the section), and the surviving joins scrubbed at
      HEAD (the fleet-adoption three-repo join; the infra-child coarse joins
      in SESSIONS/detail/ROADMAP — resolved the strict way, so doctrine and
      record agree). Residual, stated: pre-scrub prose stays reachable in
      public history; the write-time rule is the only control that exists.
- [x] **Cold review of the signing doctrine (SIGNING.md + ADR 0007)** — RAN
      2026-07-12 (cold fresh-context agent; every mechanical claim live-driven
      in a scratch repo, GitHub claims grounded in current docs):
      **PASS-WITH-FINDINGS**, verdict in `reviews/2026-07-12-signing-doctrine.md`.
      The core design proved out live — config block verbatim-correct, and the
      crown-jewel claim (bounded retirement keeps old signatures verifiable)
      is true: git passes the committer timestamp as verify-time. 10 findings
      G1–G10, all addressed same day; pre-activation, so every fix was a text
      edit — exactly what review-before-activation was for. The three
      blocking: verification made **two-plane** (GitHub's own merge commits —
      two already on `main` — are GPG-signed by the web-flow key and would
      have red-flagged the repo on first activation; the `gh api` verification
      check closes it spoof-safe), the badge-persistence claim was **inverted**
      vs current GitHub behaviour (removing a key does NOT un-verify history —
      corrected in SIGNING.md + ADR 0007 addendum), and quoted
      `valid-after="…"` timestamps mandated (the man page's unquoted form
      fails to parse on the estate's own ssh-keygen). Plus: trust list
      resolved at the child's pin, never floating `main` (a floated trust
      root defeats the blast-radius argument); custody, boundary-stub, and
      backdating honesty. Decision unchanged; activation still gates on Mike
      registering a key.
- [x] **Cold review of PRINCIPLES §8 ("Leverage")** — RAN 2026-07-11 (Fable,
      cold session): **PASS-WITH-FINDINGS**, verdict in
      `reviews/2026-07-11-principles-8-leverage.md`. Placement verified against
      the pre-change text (appended-not-renumbered correct; §8 rightly off the
      precedence ladder); all ties hold; the gold-plate discipline genuinely
      bounds it. 3 findings, all [fixed] same day: intro's "§1–7" swept to
      "§1–8" (§6's own stale-claim class), §7's "Numbered last" opener made
      position-independent, and the optional observed-vs-predicted recurrence
      evidence bar taken. Gate cleared.
- [x] **Cold review of the plugin bundle (PR #3)** — RAN 2026-07-11 (Fable,
      cold session, isolated worktree): **PASS-WITH-FINDINGS, nothing blocks
      the merge** — verdict in `reviews/2026-07-11-plugin-bundle.md`. Proven
      live: install end-to-end (root-as-plugin delivers tools/+docs/ at the
      consumer end), `/atelier:scan` honest in a foreign repo, install-hook
      blocks/passes/fails-closed as documented, and merge-is-go-live proven
      directly (marketplace add from GitHub fails today — no manifest on
      main). 5 findings: 1–3 **[fixed] on the branch** (`030f185`, PR #3
      updated — update-invalidates-hooks warning, skills' plugin-root refs
      made location-relative, all three companions named); 4–5 notes, no
      action. User config verified clean after (install fully undone). **The
      merge (go-live) is Mike's call, now review-cleared.**
      **MERGED 2026-07-11 (Opus, session 38) — Mike authorised go-live.** PR #3
      merged to `main` (`a0ef731`) after resolving a CHANGELOG append-conflict
      with the intervening ccrepo work and re-running the floor green on the
      merged head (`6245986`: 34 Node + 205 Python + 4 scanners); CI green on
      the head SHA before merge. `main` now carries `.claude-plugin/plugin.json`
      + `marketplace.json`, so `/plugin marketplace add mike548141/atelier` →
      `/plugin install atelier@atelier` resolves — the doctrine now travels as
      behaviour. Branch deleted local+remote. **This is the first deliberate
      widening spent from the live-floor item below.**
- [x] **Cold review of CONCURRENCY "Every branch ends put away"** — RAN
      2026-07-11 (Fable, cold session): **PASS-WITH-FINDINGS**, verdict in
      `reviews/2026-07-11-concurrency-put-away.md`. Fork exhaustive for lines
      of work; no RECORD/REVIEW conflict (tag keeps history reachable;
      decision-in-session-log is RECORD's own discipline). 3 findings, all
      [fixed] same day: the bearing's "multiple sessions" count grounded
      explicitly (PR #1 close + session 34 — and sharpened: the branch was
      kept *deliberately* and still generated the re-derivation tax), a
      scoping clause added (integration/permanent branches are infrastructure,
      not open work), and the tag convention date-prefixed per RECORD. Gate
      cleared.
- [x] **create-repo: new repos born with delete-branch-on-merge** — DONE
      2026-07-11: the skill's create-remote step now follows `gh repo create`
      with `gh repo edit --delete-branch-on-merge` (stated as standard, not
      option), and REPO-STANDARD's new-repo process gained step 6 saying the
      same — the landed half of CONCURRENCY's put-away rule automatic at birth.

## Raised 2026-07-12 (logged, then resolved)

- [x] **Apply the REACH re-review findings A1–A8 on Mike's decision** — DONE
      2026-07-13: Mike ruled **all eight [fixed]** (the counsel had said A1–A5
      + judgement on the rest; he took the lot). Applied to `REACH.md` and
      `AUTONOMY.md` by a neutral hand (authored neither doctrine nor verdict);
      decisions stamped in `reviews/2026-07-12-reach-rereview.md`. The cold
      pass on the applied batch is the review-owed item at the top.
- [x] **Session-38 borderline join — SCRUBBED 2026-07-13, Mike's decision.**
      The name × debt join (a named child × "scan surfaced findings,
      owner-tracked, decided fix") was reworded out of all three public spots
      that carried it — the session-38 detail file, its SESSIONS.md index
      line, and the ROADMAP's standardisation bullet — keeping the
      transferable lesson (read the repo's own roadmap before externalising a
      scan report), each spot noting the scrub and that the old wording stays
      reachable in git history (a scrub of HEAD is not remediation).
- [x] **REVIEW.md — encode reviewer independence** — DONE 2026-07-12. The gap
      the REACH case proved: a *cold-context* review can still be
      *warm-questioned* — the REACH author wrote its brief's pre-seeded
      questions, all aimed where the author was already looking; the un-briefed
      re-run found eight findings, zero overlap, two MAJOR. Encoded as a new
      REVIEW.md section *Independence is more than fresh context* (three rules:
      reviewer chooses its own attack surface, barred from prior reviews until
      its verdict drafts, self-authored *doctrine* findings decided by the
      principal not the author) + two lifecycle carve-outs (step 1 author-brief
      exception, step 4 doctrine-decision carve-out). **Cold review owed**
      (tracked under *Doctrine — review-owed* at the top).

- Reply/reporting style — **reframed out of atelier scope 2026-07-12.** Mike
  clarified the purpose is *for the agent to understand him*, not rules the agent
  recites — so it's personal context (a specific person's communication
  preferences), which the no-personal-data boundary keeps in `~/.claude/`, not
  public atelier. Written into `~/.claude/CLAUDE.md`'s "Working with me" section
  (visual reader → iconography/tables; outcome-first-then-evidence; watch volume,
  let structure replace length). No atelier artifact — the clean call was *not*
  to build `method/REPORTING.md`.
  - **Revisited same day, by Mike — `method/COMMUNICATION.md` built
    (2026-07-12, session 43).** Not a reversal of the boundary: the *values*
    stay personal (`~/.claude/`), but Mike ruled the *pattern* shareable —
    peers adopting atelier work better with the agent if they keep their own
    calibration, and the doc is how they learn to. Same split as TOOLBOX
    (practice shareable / instance personal); Mike's calibration included
    scrubbed as the named worked example (ADR 0005 framing). The doc records
    this decline-then-revisit history honestly. **Review-owed** (below).
- [x] **Adopt browser-fetch as a teammate capability** — DONE 2026-07-12 (Opus,
      session 41). The first **capability** instrument: a Chrome-driving MCP
      server (fresh headless, or the operator's own Chrome over CDP for
      captcha/Cloudflare) for when `WebFetch`/curl are blocked. ADR 0006 got an
      addendum — `instruments/` widens to admit tools that **extend the
      teammate's reach**, not only observe; the zero-dep ethos flexes for a
      capability tool whose value needs deps (pinned `requirements`/`constraints`,
      a regenerable venv OUTSIDE the repo/iCloud, code versioned in-repo).
      `instruments/browser-fetch/` holds the **scrubbed** `server.py` (every
      "Mike" → operator, pre-SDK/machine history removed before this public repo),
      pinned deps, a reproducible `setup`, and a README. Proven end-to-end after
      setup (`browser_fetch` returned a rendered page; both tools register); MCP
      registration repointed to the atelier location. Not CI-unit-tested (a
      browser is disproportionate in CI); floor scanners cover `server.py`, live
      use verifies. **Confirmed + cleaned up 2026-07-12:** a fresh parallel
      session ran `browser_fetch` end-to-end against the re-registered server
      (example.com → 200; httpbin User-Agent showed `HeadlessChrome/149` — real
      Chrome), so the old `~/.claude/mcp-servers/browser-fetch` was deleted.
- [x] **Fetch escalation ladder — build the missing rungs + elevate to doctrine**
      — DONE 2026-07-12 (session 47): doctrine elevated (`method/REACH.md`,
      reviewed) and both build sub-items shipped (multi-engine rung 3,
      live-verified; explicit rung-4/5 port split). The full ladder is documented
      in `instruments/browser-fetch/README.md` (rungs 1 WebFetch/WebSearch ·
      2 curl · 3 `browser_fetch` standalone headless, now Chrome/Firefox/WebKit ·
      4 persistent dedicated profile `:9222` · 5 persistent everyday session
      `:9223` · 6 ask the operator). The **only residual is operator-gated**: a
      live rung-5 fetch needs the operator's everyday Chrome on `:9223`.
      Sub-items, for the record:
      - [x] **Other engines** — DONE 2026-07-12 (session 47). `browser_fetch`
            (rung 3) gains an `engine` param: `chromium` (default, real installed
            Chrome), `firefox` (Gecko), `webkit` (Safari's engine) — a second
            engine is a second way past anti-bot that keys on Chrome/headless
            specifically. Firefox + WebKit **live-verified** (each fetched
            example.com end-to-end through the server path). **Honest limit:**
            rungs 4/5 stay **Chrome-only by protocol** — CDP is Chrome's, and
            Playwright's `connect_over_cdp` speaks only CDP; Firefox/WebKit have
            no connect-to-running equivalent. Not a fillable stub — a real limit,
            documented in code + README.
      - [x] **Cleaner 4/5 split** — DONE 2026-07-12 (session 47). Made explicit
            two ways at once: `browser_fetch_persistent` gains a `rung` param
            (`4` dedicated / `5` everyday), each mapping to a **distinct port**
            (rung 4 → `:9222`, rung 5 → `:9223`) the operator binds to the
            matching profile — replacing the implicit "which profile is on
            `:9222`". Rung-specific not-reachable errors (rung 5's names the
            credential boundary and warns it's a deliberate escalation).
            Rung-4 live-proven on adoption (change is port-param, unit-covered);
            **rung-5 live fetch is owed-to-operator** by nature (needs the
            operator's everyday Chrome on `:9223` — can't be self-driven).
      - [x] **Elevate the credential boundary + ladder to `method/` doctrine**
            — DONE 2026-07-12 (session 47, Opus): `method/REACH.md` written,
            grounded in the browser-fetch README + this item. Both halves in one
            doc: the escalation ladder (engine-agnostic, cheapest-first) and the
            credential boundary as a purpose-of-storage test. Named for the
            instruments' third verb (*extend reach*, ADR 0006), indexed after
            ACCESS in the SECRETS/ACCESS family. **Review-owed** (cold
            fresh-context, session-40/44 pattern) — pre-seeded questions: does
            the ladder's generic shape stay honestly grounded without inventing
            rungs the instance doesn't have; is the two-halves-one-doc join
            argued or asserted; does the purpose-of-storage test cover the real
            estate cases without outlawing intended use. The rule as captured:
            - **Provisioned stores are the intended path** — credentials saved
              *so that* a repo/tool/agent can use them (keychain items the estate
              registry records, minted per-consumer API tokens, the SECRETS/
              ACCESS machinery). Agent use is what they exist for; in scope by
              design.
            - **Personal convenience stores are off-limits by default** — a
              browser profile's saved logins, the principal's password manager
              (here Apple Passwords; browsers hold little to nothing by his own
              practice): saved over years to ease the *principal's own* browsing,
              never provisioned for agent use, and far broader than any task
              needs. Riding an already-authenticated *session* is fine; the
              stored credentials that mint sessions are the line.
            - **The principal can grant across the line** — temporary or
              permanent, per credential, his explicit act; a grant moves that
              credential into the intended path (and belongs in the provisioned
              machinery, not ad-hoc).
            A shareable SECRETS/ACCESS-family boundary, currently stated only
            operationally in the browser-fetch README. The escalation principle
            (start cheapest, step down only when blocked) is likewise general.

## instruments/ layer (new 2026-07-11, ADR 0006)

- [x] **Both observers read the ccarchive archive (`--from-archive`) — DONE
      2026-07-23** (Mike's direct ask, in two steps; wts:
      cctranscript-archive-read then archive-sourcing-finish). **Closes the
      README's "sourcing seam" on the observe side.** Both `cctranscript` and
      `ccrepo` take `--from-archive` to read the compressed mirror instead of the
      live logs Claude Code prunes, sharing `--dest`/`$CCARCHIVE_DEST` resolution
      verbatim with ccarchive (so one vocabulary points every tool at the same
      mirror; `--dest` alone implies the flag) and one transparent-gunzip
      `readLogText` choke-point per tool (parsers stay byte-format-blind).
      - **cctranscript**: every view (list, render, `--json`, UUID/prefix, explicit
        `.jsonl.gz` path — the last needs no flag) renders a pruned session word
        for word. Eviction-aware because `--list` peeks inside every candidate for
        cwd/first-prompt: it never reads an iCloud-evicted (dataless) mirror
        (listed with an `evicted` marker; `--repo` still matches it by
        dash-encoded folder suffix, its label being lossy), while rendering one
        chosen session deliberately faults its bytes back. Suite 150→156.
      - **ccrepo**: totals reach back past the prune horizon. Because ccrepo reads
        *every* file to sum spend, an evicted mirror is skipped by default and
        counted as a stated gap (`⚠` footnote + `meta.evicted`); `--materialise`
        opts into reading (re-downloading) them. The ccusage cross-check is off in
        archive mode (ccusage reads the live store, which no longer holds the
        pruned sessions) with a footnote saying so; the actual-spend-vs-estimate
        reconciliation still runs. Suite 34→41.
      - ccarchive's SF_DATALESS check is ported into each tool with the same
        `CCARCHIVE_SIMULATE_DATALESS` seam; both man pages + `--help` updated under
        the flag drift guard. The flag is `--from-archive`, not `--archive`: the
        bare form read as an imperative ("archive the transcripts"), not a source
        selector (Mike's call). What remains of the seam is only the deferred
        rollup *precompute* ledger (`ccrepo.design.md` §8) — a speed layer, not a
        survival gap, since the raw logs are preserved (ROADMAP § ccrepo).

- [x] 🎯 **Fill the machine-local spend config — DONE 2026-07-23** (actual-
      spend mechanism BUILT 2026-07-22, `1711711`, merged `12613e0` — detail
      → [`ROADMAP-DONE.md`](ROADMAP-DONE.md)). On Mike's direction the
      config was populated from his real billing receipts (collected from
      his email by agent; **usage mode**, chosen because tiers changed
      mid-history), and the reconciliation footnote now renders against
      genuine billed figures. The receipts ledger and config live in
      `~/.claude` only — figures never enter this repo (the item's own
      boundary). Residual noted machine-locally: append each new invoice
      month to the config as receipts arrive. *(Harvested 2026-07-23 by the
      apex-widening session — the closing session pushed at 00:47 without
      the harvest, redding the cold-content gate.)*

- [x] **man-page convention rollout — cctranscript + ccrepo** (closed
      2026-07-21, wt: worktree-manpages). Closes the rollout the CLI-docs
      standard opened: the `--help`/`man` split (REPO-STANDARD § "An installed
      CLI ships both") was established with `ccarchive` as the reviewed worked
      example; this rolls it to the two remaining **installed** CLIs, so every
      tool the installer publishes to `PATH` now carries both registers. Each
      ships a full plain-language `instruments/man/<tool>.1` (NAME/SYNOPSIS/
      DESCRIPTION/OPTIONS/FILES/EXAMPLES/EXIT STATUS/NOTES/SEE ALSO, matching
      `ccarchive.1`'s roff style, `mandoc -T lint` clean) and a trimmed `--help`
      digest pointing at the manual (cctranscript 42→24 lines, ccrepo 67→35;
      rationale + worked examples relocated into the page — the page is the
      superset, so the two can't drift). **EXIT STATUS enumerated against every
      `process.exit()` path in each source** — the drift a prior ccarchive
      applied-batch review caught (`EXIT STATUS` predating the tool's non-zero
      paths), designed out here at authoring time. +6 doc-convention tests
      (digest-points-at-man, well-formed-roff, superset drift-guard), mirroring
      ccarchive's pattern; the installer already globs `man/*.1` so no install
      change. Verified: 92 instrument tests green, mandoc clean ×3, installer
      drive publishes all three pages into a throwaway MANPATH, leak/secret/
      link/size scans clean. Application of a reviewed convention, not new
      doctrine ⇒ no review cycle owed (REVIEW.md rule 4). Orchestrated: one Opus
      session + two parallel Opus agents (one per tool, disjoint files in the
      worktree), the orchestrator verifying and committing.

- [x] **ccrepo — cost fidelity, full breakdown, and reach** (Mike, 2026-07-11) —
      three strands to make the DevFinOps view truer and more accessible; all
      three now addressed (the VS Code *build* stays a separate decision):
      - [x] **Actuals vs estimate — show both.** DONE 2026-07-11 (Opus, session
            38): config confirmed (USD Max-20x, all Claude families covered) and
            the code built. `~/.claude/ccrepo-billing.json` (machine-local, never
            in a repo; absent ⇒ estimate-only, byte-identical JSON contract
            preserved; malformed ⇒ ignored-with-warning, never fatal) drives an
            **Actual** column beside **Est (API)**: `covers[]` matches model
            families by prefix (after `claude-` stripped), `perTokenModels` carves
            one back out; covered tokens cost $0 marginal, the sunk plan fee is
            apportioned per repo by covered-token share (falls back to total-token
            share if nothing covered ran in range), uncovered models keep the
            API-rate figure. **Actual = plan share + uncovered spend**, so TOTAL
            Actual = fee + all uncovered — proven live: estate-wide Est
            US$2,305 vs Actual US$200 (the whole plan fee), and `--by-model`
            children sum to their repo. Both columns convert together under
            `--fx`; `--no-billing` forces estimate-only. Multi-month outlay +
            overage thresholds out of scope v1, stated as footnotes. 8 new pure
            tests (`loadBilling`/`coversPredicate`/`actualFor`/covered-split
            fold); suite 26→34 Node.
      - [x] **Full ccusage breakdown** — DONE 2026-07-11: ccrepo now shows
            Cache Create · Cache Read · **Cache Hit** (reads ÷ prompt-side
            tokens, the point-don't-paste signal made observable) alongside
            Input/Output/Total/Cost, in the table, `--by-model`/`--by-day`
            children, and `--json` (`cacheCreationTokens`/`cacheReadTokens`/
            `cacheHitRate`); definition footnoted in the output. Tests updated
            + new `cacheHitRate` unit (fixtures now mirror ccusage's real
            shape: totalTokens includes cache); driven live — repo-level hit
            rates 95–98%.
      - [x] **VS Code UI — SCOPED 2026-07-11** (the item asked for scoping
            before building; grounded via current docs, not memory). Findings:
            the official Claude Code extension exposes **no** third-party hook
            points (no API, no contributed-view extension points; open feature
            requests confirm); Claude Code's **statusline** can carry per-repo
            cost (rich stdin JSON incl. `workspace` + live session cost;
            ~1.1 s ccrepo run needs a TTL cache) but renders **only in
            terminal surfaces**, never the graphical panel. Recommended route:
            a tiny **sideloaded companion extension** (status bar item +
            tooltip breakdown reading `ccrepo --json`; local `.vsix`, no
            marketplace; declare workspace-trust, resolve PATH explicitly),
            ~4–6 h, with a ~1 h spike (40-line extension showing the workspace
            total) as the feasibility proof. Statusline script is a free
            adjunct for terminal sessions. Build is a separate decision.
- [x] **cctranscript — per-reply response IDs (`N.M`)** — DONE 2026-07-11.
      Both open decisions taken and stated in the code: a "reply" is a **text
      reply only** (the unit a human cites; thinking/tool turns stay
      unnumbered even under `--full` — clutter loses), and `--json` carries a
      `ref` field on every turn (`"1"` on prompts, `"1.2"` on replies, null on
      think/tool/result) so citations are machine-addressable. Header shows
      `◂ Claude 1.1 (Opus 4.8)`; a reply before any prompt (resumed session)
      numbers under exchange 0, honestly marking its prompt isn't in the log.
      `numberTurns()` pure + unit-tested; `--json` contract test asserts the
      ref scheme; driven live.
- [x] **ccrepo + cctranscript ship untested** — DONE 2026-07-11 (session 35).
      They shipped with no tests (session 34), unlike the `tools/` scanners which
      each carry a unittest + `--selftest`; cctranscript had since grown real
      rendering logic (wrapping, markdown, model tags, right-align, exchange
      rules). Now floored with `node:test` + `node:assert` — **zero-dep, mirrors
      `tools/`'s stdlib-only pattern and sets the Node layer's test convention**
      (the first Node test surface; decision recorded in the session log). Minimal
      testability refactor only: each CLI entrypoint guarded by
      `require.main === module`, pure functions `module.exports`ed — no behaviour
      change, except one stated fix (an explicit `.jsonl` path now recovers its
      repo label via `cwdFromLog`, as every other route already did). Coverage:
      `instruments/cctranscript.test.js` — a `--json` output-contract test over a
      checked-in synthetic fixture (`fixtures/session-sample.jsonl`) asserting role
      classification, model mapping, timestamp/text extraction, and `--think`/
      `--tools` gating (this is what catches a Claude Code log-format change), plus
      pure-function units; `instruments/ccrepo.test.js` — pure functions and the
      aggregation fold over fixture ccusage rows. Wired into `ci.yml`'s floor job.
      Grounded in EVIDENCE §14 (an honest instrument's "ok" is a claim the apex
      governs). **Residual:** ccrepo's coverage is pure-functions + aggregation
      only — the `ccusage` `execFileSync` call, JSON parse, FX conversion, and
      table render sit behind an untested seam (aggregation was factored out to
      `aggregate()` to test the fold; the shell-out itself has no test double yet).

## Doctrine calibration — reviewed

- [x] **Review the "match the ceremony to the risk" doctrine change** — RAN
      2026-07-11 (Fable, fresh session, the light read the item asked for):
      **PASS, no findings.** Grounding verified by probe, not read: `don't-stack`
      appears nowhere in pre-change `docs/method/` (`git grep` at `cb37310^` —
      the "un-codified habit enforced as a rule" claim is true), and the
      original hygiene item 1's own rationale was always pivot-cost, so the
      sharpening is restoration, not revision. Consistency held everywhere
      checked: the narrowed don't-stack matches all five recorded applications
      (each was a gate on unreviewed tooling/doctrine); the self-verifying
      carve-out cannot be over-read to exempt scanner-class changes because the
      **silent-failure-mode bullet catches them** — and the same session's
      child-CI-floor review is the live demonstration of both halves (d0870a4
      earned its review and needed it: the class was still open in the sibling
      scanners; the records-only edits around it earned none). Recursive check
      honoured: flagged, not self-certified, merged by the principal.
      Follow-up DONE 2026-07-11 (Opus, session 31, `53b41db`): the condensed
      `build/templates/docs/MODEL-ECONOMICS.md` hygiene line shipped the exact
      "One task per session; start fresh" misread this change diagnosed —
      inherited by every scaffold. Rewritten to carry the sharpening (a coherent
      *line*, not a checkbox; break for a genuine reason, not a green item) plus
      the new ceremony-to-risk bearing. Judged self-verifying, not a fresh
      review: it applies an *already-reviewed* decision to its condensed mirror
      (the second-copy-drift class test_templates.py guards; no live pin on this
      file's body). Suite 205 OK, unchanged.

## Done (2026-07-10)

- [x] Scaffold + method/ first slice: `00-APEX`, `AUTONOMY`, `STORAGE`,
      `CONCURRENCY`, `TOOLBOX`.
- [x] Foundation review (2 Fable + 1 harvest) — `docs/reviews/2026-07-10-…`.
- [x] Autonomy floor closed (self-widening, lockout-class, GitHub-surface,
      deploy carve-out, recoverability-ends-at-push, pull-quote) + global
      commit/push/PR grant.
- [x] **Canonicality decided** (atelier canonical; children point up) and the
      active APEX↔ros §0 DRY breach fixed — ros §0 shrunk to inlined floor +
      pointer (first instance of the anchor pattern).
- [x] All-models-one-doctrine stated (APEX "who it binds"); review-trigger
      policy + tiered-authority in MODEL-ECONOMICS.

## Next — the propagation mechanism (do BEFORE further extraction)

The load-bearing architecture, review-endorsed shape: **"thin anchor, fat
pointer"** (dependency + lockfile for doctrine). Written up in
`docs/method/PROPAGATION.md` (2026-07-10).

- [x] **Version atelier** — decided: the **commit SHA is the version** (no tag
      ceremony); CHANGELOG is the human-readable index; tags reserved for
      milestones. One CHANGELOG line per doctrine change.
- [x] **Define the standard child CLAUDE.md doctrine block** — inlined safety
      floor (apex + always-confirm) + pointer + SHA pin + one-line drift check
      (`git -C <atelier-path> log --oneline PIN..HEAD`) riding the session-start
      read + a stated **repo-visibility fact** (verifiable via `gh repo view`).
      Canonical text lives in `PROPAGATION.md`.
- [x] **Retrofit `faves` and `ros`** with the block (stamped at the mechanism's
      commit SHA).
- [x] **Layer-override rule** into `method/`: a child may narrow or append,
      never silently contradict; a contradiction is a defect to surface.
      (`PROPAGATION.md` § layer-override rule.)
- [x] **Enforcement clause** (the category error, in writing): documents are the
      standard; the review-with-a-more-capable-model practice is the enforcement.
      (`PROPAGATION.md` § enforcement clause.)

## Review gate — before more content stacks on the method/ layer

The "mechanism/review before more content" rule: the keystone + the whole `method/`
layer earn a review with fresh context before extraction continues.

- [x] **Fable review of the `method/` layer** — RAN 2026-07-10:
      **PASS-WITH-FINDINGS**, verdict below the divider in
      `docs/reviews/2026-07-10-method-layer.md`. Architecture holds; 10
      findings [fixed] same session (trust-surface floor gap, drift-check
      alarm-fatigue guard, EVIDENCE §4 scope + §12 boundary, REVIEW reframe +
      [rejected] decision, RECORD integration-boundary lockstep, PRINCIPLES
      missing cases, stale README/CHANGELOG). **The gate is cleared —
      extraction may resume.** Notably: the sharpest ask's premise was
      corrected, not confirmed — Fable is the *more* capable tier (the reframe
      to independence-as-core still landed, for peer adopters without a
      superior tier).
- [x] **Method-review follow-ups ([backlog] findings)** — CLOSED. faves adopted
      the P1 trust-surface floor wording at its session-21 pin bump
      (dde4170→bbdeece); the 2026-07-11 session-31 fleet bump then carried all
      three children (faves/numen/ros) current to `d45a431` — `tools/pins.py`
      reads **all 3 current ✓**.
      - [x] P2 fleet pin view — DONE 2026-07-10 (Opus): `tools/pins.py`, the
            read-only roll-up of every child's pin vs atelier HEAD
            (`current`/`behind N`/`ahead`/`diverged`/`unknown`/`no-pin`, `--log`/
            `--json`/`--check`/`--selftest`); 12 stdlib tests; live-proven
            (faves 9 behind, ros current). PROPAGATION honest caveat updated to
            acknowledge it as observability-not-enforcement.
      - [x] V2 ADRs — DONE 2026-07-10 (Fable): `docs/decisions/0001–0004`
            (canonicality, SHA-as-version, private-first, Apache-2.0).
      - [x] V3 SESSIONS split — DONE 2026-07-10 (Fable): index +
            `docs/sessions/` detail files, entries preserved verbatim.

## Then — extraction (keep the case-law, don't strip it)

Generalise the *bearings/cases*, don't delete them (a de-cased principle is
theatre). Leave tiki-specific bearings + review case-law in ros.

- [x] **`PRINCIPLES.md`** spine + precedence ladder + situation tests, with
      generalised cases. Extracted 2026-07-10; canonical here.
- [x] **Trim ros `docs/PRINCIPLES.md`** — DONE 2026-07-10 (Fable, ros
      `73fd50b`) per the verdict's trim guidance (lens-1 answer 12): kept the
      §0 bearing, every Tiki-bearing/Already-holds line, the seven-tenet ZT
      estate mapping, and the whole precedent-annotated trade-offs section;
      dropped only the general prose the spine states. The transitional DRY
      breach is closed.
- [x] **`MODEL-ECONOMICS.md`** general shape — DONE 2026-07-10 (Opus): promoted
      stub → canonical. Match-the-model-to-job + which-pool self-check + tiered
      authority + inline/batched review triggering (already in the stub) plus the
      general session-hygiene mechanics + cache economics extracted from ros
      (per-model cache, TTL churn, point-don't-paste, one-task, heavy-skills).
      Person-local numbers (prices, model roster, 35k overhead) stay in ros; a
      foot-pointer names the split. README + method/README swept off "stub".
- [x] **`EVIDENCE.md`** (harvest A1 — highest-value net-new) — authority tiers,
      acquisition-method error risk, absolute-dating, store-the-rule-not-the-value,
      one-fact-one-home, trigger-based refresh, enforce-by-machine; mechanically
      hardens the apex. Generalised from a private reference-library `STANDARDS.md`.
- [x] **Peer-review lifecycle** doc (harvest A2 → `REVIEW.md`) +
      **session/doc-as-code discipline** doc (harvest A3 → `RECORD.md`) — both
      written 2026-07-10; close the enforcement-clause forward-references.
- [x] **Model-capability authority** section in AUTONOMY (harvest A4 — the
      *who-acts* axis; "policy in memory protects nothing — encode it").
      Ratified by Mike 2026-07-10; written into `method/AUTONOMY.md`.
- [x] **Source-acquisition ladder (A6) + honest-instrument (A7)** — DONE
      2026-07-10 (Opus): `EVIDENCE.md` §13 (climb the acquisition ladder to the
      *cost of being wrong*, state the gap when blocked) + §14 (an instrument the
      agent builds is a source; its "ok"/"applied" is a claim the apex governs —
      verified-not-attempted, silent-success-is-a-defect, "unknown"-is-required,
      known-failure-test enforces). Grounded in §3/§11 and PRINCIPLES §6; ros
      diagnose/apply phantom-success named as the estate instance. Closes the
      extraction section. Reviewed 2026-07-10 (batch review — holds; B15 §13/§11
      stakes-win tiebreak added).

## Review gate — the post-method-review batch (before more content stacks)

The same "mechanism/review before more content" rule that gated the `method/`
layer now gates everything built since it. Session 15 flagged this as the
standout debt; sessions 14–15 deliberately did not stack on it.

- [x] **Fable sweep of the `957fa08..f72031c` batch** — RAN 2026-07-10 (Fable,
      fresh session): **PASS-WITH-FINDINGS**, verdict below the divider in
      `docs/reviews/2026-07-10-post-method-review-batch.md`. Floor green (3
      selftests + 133→137 tests + live runs), doctrine grounded, ros cross-read
      done. 16 findings B1–B16, **every one carrying an in-repo fix, applied +
      verified same session**; two backlog strands remain below. The two
      sharpest: B1 a "live-proven clean" claim false at the commit that
      recorded it — licenscan flagged its own unexempted fixtures; B14 ACCESS
      pointing at an estate access map ros doesn't hold. Scan fixes re-run
      clean; B4 (renamed-file staged hole) proven live both scanners. **The
      gate is cleared — the create-repo rewire and further stacking may
      resume.**
- [x] **Batch-review follow-ups ([backlog] findings)** — the consolidated item
      *(box flipped `[ ]`→`[x]` 2026-07-22: both children below were already
      DONE at harvest and the parent was never flipped — found by the
      harvest-integrity check's first manual run; state corrected, text
      preserved verbatim)*:
      - [x] **ros: first consolidated estate access map** (B14) — DONE
            2026-07-12 (session 47; created by an agent scoped inside the private
            ros repo, then **landed on ros main** by the main line once ros's PR
            merged and it had no live session). `docs/ACCESS-MAP.md` in ros: a row
            per domain across ACCESS.md's four axes, seeded from ros's own
            scattered facts, honest per-domain onboarding status (nothing rounded
            up to "onboarded"). **Read before finalise caught a stale status** —
            a cell seeded while a ros work-stream was still in flight had gone
            stale by land time (the work had since merged, reviewed and
            live-proven), so it was corrected before push. Rebased onto the
            merged main (conflict-free, new file), signed, ff-merged + pushed
            (`82db55c`), worktree/branch put away. ACCESS.md's honest-status note
            flipped (map now exists). **Note:** ros's floor is red, but *not* on
            this map (it scans clean) — pre-existing scanner findings the owner
            judges false-positive-class, red since before the map landed;
            specifics in ros's own records. Separate from B14.
      - [x] **REVIEW.md addition** — DONE 2026-07-10 (Opus): new "Re-run every
            'live-proven' claim in scope" subsection — a recorded proof is a
            claim that can be stale by the commit that records it, so a review
            re-runs the work's asserted proofs, not just reads them. Grounded
            twice (B1 the scan's stale "live-proven clean"; C2 the stamped drift
            check that broke run-verbatim). Review-owed like any doctrine edit.

## build/ layer + inheritance delivery — completed
- [x] **Extract the `create-repo` standard into `docs/build/`** — DONE
      2026-07-10 (Opus): `docs/build/REPO-STANDARD.md` (product-in-subfolder + why,
      sizing-to-type, the standard file set, honest-CI, standardise-existing
      process, repo-craft conventions), pointing up to `method/` for the
      cross-cutting doctrine (EVIDENCE/RECORD/REVIEW/PROPAGATION/AUTONOMY) instead
      of copying it. build/README rewritten from pointer → layer index. Reviewed
      2026-07-10 (batch review — B8 subfolder rule scoped to deployable-artifact
      repos, B9 no-gate-must-be-stated, B10 RECORD gained the pointed-at
      comments rule, B11 templates/staleness swept). Instance specifics stay in
      the skill. Templates-move + rewire-to-inherit remain (below).
- [x] **Licence-consistency pre-publish gate** (A11) — DONE 2026-07-10 (Opus):
      `tools/licenscan.py`, the third pre-publish scan (leakscan · secretscan ·
      licenscan). Three checks — LICENSE present + SPDX-recognised, every
      declaration (pyproject/package.json/Cargo/gemspec/setup.cfg/README badge)
      agrees, no incompatible `SPDX-License-Identifier` header (copyleft-into-
      permissive blocks). Conservative + advisory, `--expect <SPDX>` for CI,
      zero-dep, allow-marker + `.licenscanignore` hatches, `--selftest`. 35 tests
      (suite 98→133). *Correction (2026-07-10 review, B1): the original
      "live-proven clean on atelier" claim here was **false at the commit that
      recorded it** — the scan flagged its own unexempted test fixtures at HEAD;
      any mid-build clean run didn't survive to the commit. Fixed (`.licenscanignore`,
      same reasoned exemption as the sibling scans) and re-proven:
      `--expect Apache-2.0` exit 0 at the review session's close.* Reviewed
      2026-07-10 (the batch review, B1–B3 fixed: `-only`/`+` SPDX suffixes,
      prose-header residual stated).

The completed children of the code-signing item (its open strands stay in ROADMAP.md):

      - [x] **Doctrine drafted — DONE 2026-07-11 (Fable):** `method/SIGNING.md`
            + ADR 0007. SSH-native commit/tag signing fleet-wide (dedicated
            ed25519 signing key, machine-global config + create-repo-baked
            repo-local `commit.gpgsign=true`, one canonical append-only
            `allowed_signers` tracked in atelier, CI verification from each
            repo's adoption boundary; history never rewritten to sign it; what
            a signature honestly claims — machine custody, not personal
            authorship — stated per the apex). Rejected: GPG, sigstore/gitsign,
            no-signing (see the ADR). **Reviewed 2026-07-12** — PASS-WITH-
            FINDINGS, all G1–G10 addressed pre-activation (see the review-owed
            section above; `reviews/2026-07-12-signing-doctrine.md`).
      - [x] **Activation (ladder in SIGNING.md) — FULLY ACTIVE 2026-07-12 (Opus,
            session 41), warn-first.** All five ladder steps done. Step 1: Mike
            registered a dedicated ed25519 signing key (his act). Step 2: machine
            wired, atelier boundary `958b1ea` proven on both planes
            (`git verify-commit` good + `gh api …verified` true). Step 3:
            `create-repo` + REPO-STANDARD bake repo-local `commit.gpgsign`. Step
            5: `tools/signscan.py` (two-plane, known-signed-fixture selftest) +
            CI verification in atelier `ci.yml` and the child `floor.yml`
            template, trust list at the child's pin, **warn-first**. Step 4: **10
            house-floor children retrofit** (pin bump + floor signing steps +
            `SIGN_BOUNDARY`), 7 CI-green, 3 red on **pre-existing scanner debt**
            that fails before the signing steps run — not signing, the owner's
            debt (which children, and what debt, lives in their own private
            records — the name × debt join stays out of public atelier per
            RECORD; joined here until the 2026-07-12 session-47 scrub). **Bug the dogfood caught:**
            bare `valid-after` is read in the verifier's local tz, so atelier's
            own first CI run flagged every signed commit "not yet valid" in the
            UTC runner — fixed by UTC-anchoring with a `Z` suffix; SIGNING.md now
            mandates it, the selftest guards it. Caught before any child was
            touched — the reason to dogfood atelier first.
            **Two follow-ups (below).**
      - [x] **faves + ros: adopt the house floor (then signing-CI).** Both run
            bespoke `ci.yml`, never adopted `floor.yml`, so the fleet retrofit
            skipped their signing *verification* (they still sign every commit).
            A separate standardisation pass: give them the house floor, or inject
            signing steps into their bespoke CI. The pre-existing gap this work
            surfaced.
            - [x] **DONE 2026-07-12 (Fable, session 42) — full adoption, both
                  floors green on first run.** Current template alongside each
                  repo's bespoke `ci.yml`; pins bumped to a trust-resolving SHA
                  (both old pins predated `allowed_signers`, so verification
                  would have silently skipped); boundaries at each repo's last
                  unsigned commit; two-plane verification *verified* (not
                  skipped) — faves 9/9, ros 2/2 good. Unlike the three
                  debt-red children, both went green by encoding each repo's
                  charter through the scanners' designed hatches: repo-type
                  `--disable` tuning (content shapes for a listings site,
                  network shapes for a network-inventory repo — the flag's own
                  documented example), reasoned ignore globs for chartered
                  content (each entry stating it does NOT survive the
                  publish-time scrub pass), inline allow-markers for the
                  handful of shape false positives. licenscan enabled in both
                  (settled Apache-2.0 — the template's stated trigger); four
                  real broken links fixed in passing. leakscan CI cover stays
                  honestly structural-only; full-term cover remains on the
                  pre-commit hook.

- [x] **Rewire `create-repo` to inherit from atelier** — DONE 2026-07-10 (Opus):
      the core Q1 fix. The skill now inherits from atelier (points up to
      REPO-STANDARD/REPO-BOUNDARY/PROPAGATION, seeds from `build/templates/`)
      instead of re-encoding the standard, and **stamps the doctrine block + SHA
      pin** into every new repo's CLAUDE.md — the skill had *no CLAUDE.md template
      at all*, so PROPAGATION was bypassed at birth. Templates moved skill→
      `build/templates/` (18 files, one source), the missing CLAUDE.md template
      added, three instance-residue scrubs + one live ros-is-canonical drift fix;
      leakscan clean. Skill stays machine-local (delivery vehicle), hard-depends
      on atelier, fails honestly if absent. Stamp core dry-run-proven in scratch
      (renames + all four placeholders + drift-check runs "current"); real-repo
      run (`gh` create + hook install) + Fable sweep owed. Review-owed.
  - [x] **Real-scaffold exercise — DONE 2026-07-10 (Opus):** scaffolded a real
        local git repo from the templates (seed → 3 renames → stamp → hook →
        commit) and drove the hook end-to-end. Surfaced + fixed a live
        **scan-hook fail-open defect** the scratch dry-run couldn't:
        `tools/pre-commit.sample` pointed at `$repo_root/tools/` and skipped
        silently when the scanners were absent — a child has none (they live in
        atelier), so its hook committed a real `AKIA…` secret. Fixed to resolve
        atelier's tools (`ATELIER_TOOLS` → `git config hooks.atelierTools` →
        in-repo fallback) and **fail closed**; step 6 bakes the path + a
        prove-it-once check. Re-proven: fail-closed / blocks-secret / passes-clean
        / atelier-unaffected, then pinned by `tools/test_precommit.py` (5 tests,
        known-failure proven against the pre-fix sample; suite 137→142 OK).
        **Still owed:** the single `gh repo
        create --push` step (not run — outward, unneeded for a throwaway); the
        Fable sweep (now briefed — gate below); and **CI scan wiring** — CI
        templates run no scanner, so the hook is a scaffolded repo's only scan
        gate (needs the scanner-distribution call: vendor / fetch atelier /
        publish — folds into the deferred supply-chain item).

## Review gate — the create-repo delivery mechanism
The same rule, third application: the mechanism that stamps doctrine into every
future repo must itself be reviewed before it's *used in anger*. Brief written
2026-07-10: `docs/reviews/2026-07-10-create-repo-rewire.md` — range
`f72031c..92c0112` **plus the machine-local skill** (outside the repo; no other
review will catch it). Nine load-bearing assumptions to attack; the sharpest:
clone-loses-hook-and-config (does protection evaporate on machine two?),
template-block drift vs PROPAGATION's canonical text, and prose-stamp-procedure
as model-memory reborn. **Run cold, fresh session.**

- [x] **Fable sweep of `f72031c..92c0112` + the skill** — RAN 2026-07-10
      (Fable, cold session): **PASS-WITH-FINDINGS**, verdict below the divider
      in `docs/reviews/2026-07-10-create-repo-rewire.md`. Floor green (142→145
      tests, 3 selftests, leakscan/licenscan clean); mechanism driven live
      twice. 10 findings C1–C10, **all [fixed] + re-driven same session**. The
      two sharpest, both proven live: C1 a fresh clone loses hook + config
      silently — machine two committed a planted `AKIA…` key green (fixed at
      the three places a new clone looks: CLAUDE.md bullet, CONTRIBUTING
      once-per-clone install, hook header); C2 the stamped drift check breaks
      run-verbatim — unquoted spacey path, and the skill's `$PP/atelier`
      contradicted the `../atelier` house practice (skill now stamps
      sibling-relative + block quotes the path + a mechanical prove-the-stamp
      in step 5). `tools/test_templates.py` pins template-block ≡ PROPAGATION
      canonical (C3). **Both owed items now closed 2026-07-10 (Opus):** the
      outward `gh repo create --push` step driven live for the first time —
      scaffolded **`numen`** (`mike548141/numen`, PRIVATE, verified
      `isPrivate: true`), the first keeper repo, born from this mechanism at
      `atelier@bbdeece`; hook proven live to block a planted `AKIA…` key +
      pass the real commit clean, drift check clean run-verbatim, no
      `settings.local.json` leaked. And ros (f72031c→bbdeece) + faves
      (dde4170→bbdeece, +the P1 trust-surface floor clause it lagged) pin bumps
      carried the reworded block down — fleet now all-current (`tools/pins.py`).

- [x] Until the verdict: create-repo may be used for throwaway/scratch
      exercising, but **don't scaffold a real keeper repo on the unreviewed
      mechanism** (the don't-stack-on-unreviewed rule, applied to delivery
      instead of doctrine). *Cleared 2026-07-10 by the sweep above — keeper
      repos may be scaffolded.*
- [x] **Repo-boundary guidance** — DONE 2026-07-10 (Opus): `docs/build/
      REPO-BOUNDARY.md`, the is-this-a-repo decision by independent-lifecycle
      discriminators (visibility/cadence/ownership/reuse/blast-radius) → standalone
      / component / monorepo-folder (rich client engagement as the monorepo case);
      advise proactively; when ambiguous prefer the reversible direction (split
      later is cheap, merge is painful). Reviewed 2026-07-10 (batch review —
      discriminators decide the three live cases; B16 split-promptly clause).
- [x] **Parallel-work tooling** (Mike 2026-07-10: make fork-and-merge a *tool*,
      not just doctrine) — built as `tools/worktree.py`
      (`start`/`list`/`land`/`remove`), the one-command delivery of CONCURRENCY's
      worktree-per-line: fork outside iCloud, hygiene view, push+PR back, guarded
      cleanup. Guards encode the doctrine — iCloud-base refusal, branch-off-main,
      stale/dirty flags, no-lose-work on remove. 12 stdlib tests + live-proven on
      atelier itself (start → list → remove round-trip, main tree left untouched).
      Built the same session Mike was handed the worktree recipe to run the
      method/ Fable review as a parallel line.

## Safety tooling (gates the person-context + archive threads)

- [x] **Mechanical leak-scan** — built 2026-07-10 as `tools/leakscan.py`
      (+ README, `pre-commit.sample`, `leakscan-terms.example.txt`, unittest).
      Shareable structural patterns (always run) + machine-local literal-term
      list (`~/.claude/leakscan-terms.txt`, never in a repo); graceful
      degradation to structural-only with a loud warning; `--staged` hot path,
      `--json`, fail-safe exit codes; `.leakscanignore` + `leakscan:allow`
      escape hatches; `--disable <rules>` + `--staged <subtree>` for networking
      repos / private-repo-with-shareable-subtree. Proven: caught real address/
      coordinate/name leaks in its own first-draft fixtures; **local term list
      SEEDED** in `~/.claude/`; **hooks INSTALLED** (atelier whole-repo; ros
      `tiki/`-scoped with network-shape rules off) and block/pass proven live.
      Full-cover scan validated the earlier tiki scrub — 1 residue (the intended
      OSS author name in `pyproject.toml`, allow-marked) out of 738 raw hits.
      **Owed:** CI wiring (a hook only guards the machine it's on); portability
      of the term list to Mike's other devices (north-star); extend patterns as
      gaps appear. Reviewed 2026-07-10 (batch review — B4 renamed-file staged
      hole fixed + proven live, B5 `--require-terms` fail-closed flag for
      hooks/CI, B7 residual false-negative surface now stated in tools/README).
- [x] **Secret-scan on push** — built 2026-07-10 as `tools/secretscan.py` (a
      zero-dep, self-written "equiv", not a gitleaks install — matches the house
      tool pattern + dodges the tool-install floor). Named vendor formats + a
      secret-named-assignment/entropy workhorse; skips the safe indirections
      (`!secret`/`${VAR}`/`<ph>`), code refs, public keys and URL paths.
      **Validated 0 FP over real tiki source/inventory/docs** (25→0 across three
      FP-class fixes) while still catching the fixture-secret shapes; report
      redacts to length+entropy. 47 tests; combined pre-commit sample runs it
      with leakscan; `.secretscanignore` + allow-marker escape hatches.
      Reviewed 2026-07-10 (batch review — pattern set + heuristic hold, skip-list
      verified against SECRETS.md's named forms; B4 renamed-file staged hole
      fixed + proven live, B6/B7 residuals stated). **Owed:** CI wiring (dead until atelier has a remote);
      hook portability to Mike's other repos. Closes the *detect* half of
      *detect → rotate → burn-cost-is-minutes*.
- [x] **`DATA-PROTECTION.md`** written (2026-07-10) — read-before-write; verified
      way-back before any destructive op; data plane is the slow lane even under
      broad grants; reproducibility as insurance; protect others' data.
- [x] **Safe-access-onboarding doctrine** — DONE 2026-07-10 (Opus):
      `method/ACCESS.md`, the ordered onboarding runbook (grant-recorded-not-
      originated → narrowest credential + plane-split → credential-into-store-first
      → read-only first ring + reconcile-or-stop → destructive gate encoded before
      destructive power → widen-in-rings → Zero-Trust the domain). Invents no rule;
      sequences AUTONOMY/DATA-PROTECTION/SECRETS/PRINCIPLES for the moment access is
      new. The concrete estate access map is instance-local (sensitive topology,
      protected under DATA-PROTECTION; ros owes its first consolidated map —
      B14 backlog). method/README #6. Reviewed 2026-07-10 (batch review — B13
      step-5 strengthening owned + one-credential fallback stated, B14 access-map
      claim corrected to honest status).
- [x] **`SECRETS.md`** doctrine — DONE 2026-07-10 (Opus): `method/SECRETS.md`,
      extracted from ros §5 (credential triad) + §7 (secret-store-not-exempt).
      Reproducible / re-mintable enabling property (internal rotate mechanically,
      external re-mint behind one approval); the least/JIT/short-lived triad with
      standing creds as tracked-debt-not-resting-state; references-never-values in
      the right plane; rotation-on-cadence bounds the undetected window. Closes
      AUTONOMY's forward-reference to "the secrets doctrine" and completes the
      *detect → rotate → burn-cost-is-minutes* arc with the two scans. Instance
      mechanism (sops+age, `!secret`, the credential map) stays in ros — ros
      cross-read confirmed it holds that content. Reviewed 2026-07-10 (batch
      review — B12 honest boundary added: master-key loss is redundancy-guarded,
      person-level vault out of scope by design).

## Sharing — completed
- [x] 🎯 **P1 — the command allowlist is untracked estate-wide. RULED
      2026-07-29 (Mike): option ⓑ — untrack everywhere, one uniform rule**,
      rather than public-only (ⓐ) or a trimmed-but-committed list (ⓒ).
      Grounds: a visibility-conditional rule silently becomes wrong the day a
      repo flips, and every private repo here is a candidate to flip. Raised by
      `rpi`'s post-flip cold pass (F1) — the child fixed it locally and thereby
      diverged from atelier doctrine, which mandated committing the file in
      four places; resolved upward here per `method/PROPAGATION.md`. Applied in
      atelier + all four doctrine surfaces (`build/REPO-STANDARD.md`,
      `method/TOOLBOX.md`, `templates/gitignore`, `skills/create-repo`);
      children follow at their next pin bump (standing guidance on the
      fleet-adoption item in ROADMAP.md). **Named cost, not hidden:** the
      allowlist stops being a shared reviewable record of what runs unprompted
      — it is machine-local per clone now, so a fresh clone re-prompts until
      seeded from `docs/build/templates/claude/settings.json`. **What this does
      not undo:** atelier's copy is already in published history and cannot be
      recalled. (Moved from ROADMAP.md 2026-07-29, same commit that landed it —
      the cold-content gate fired on the `[x]`.)

- [x] **P2 — `publishscan` built and registry-wired blocking, 2026-07-29.**
      The guard for the class P1 exposed: it reds when a repo *tracks* a file
      whose publication weakens it, judging the **path** rather than the
      contents. That is the one question no other scanner here asks, and it is
      why `secretscan` and `leakscan` both passed `rpi`'s allowlist correctly —
      the file holds no credential and no personal fact; the exposure was its
      presence. 14 tests; driven live red on the real defect (staging the
      allowlist back into the index) and green on the tree; full suite 820 OK.
      Patterns carry their provenance rather than blurring it: the
      `.claude/settings*.json` pair is grounded in F1, the rest (`.mcp.json`,
      `.env*`, `.envrc`, `.netrc`, `.npmrc`, `.pypirc`, editor-local config) is
      named as standard practice. It offers an **advisory** form — unusual for
      a boundary check, and for an adoption reason rather than a severity one:
      eleven children track the allowlist today, and a blocking check arriving
      by propagation would red their next commit for a file nobody has told
      them about. It deliberately **allows** the self-describing guard files
      (`.atelier-floor.json`, the `.<scanner>ignore` set) — they map where the
      defences are weak *and* must travel for the floor to run, so that
      exposure is accepted and mitigated by requiring a stated reason for every
      exemption, never by hiding the files. **Residuals, stated:** it is a
      denylist, so a novel defence-mapping file passes until someone teaches it
      (P2a); and it cannot unpublish — history already pushed stays pushed.
      One design error, caught by `floor.py`'s own test suite rather than by
      review: the first cut hard-failed on a tree with no git, which would have
      made it unrunnable in every child's fixtures. Corrected to a visible
      exit-0 skip — with no git there is no tracked set to miss, so the claim
      is true rather than unverified — while every *other* git failure stays
      exit 2. (Moved from ROADMAP.md 2026-07-29, same commit that landed it.)

- [x] **Public release (readable repo)** — DONE 2026-07-10 (ADR 0005), as a named
      worked example: no genericise-the-voice pass, no instance-restructure
      precondition; the audit showed the hard boundary already held. The flip
      was `gh repo edit --visibility public`, act-then-record.

- [x] **The next widening — plugin/skills bundle SPENT 2026-07-11** (Opus,
      session 38): the plugin bundle (PR #3) merged to `main` on Mike's explicit
      go-ahead — atelier is now an installable Claude Code plugin+marketplace,
      the doctrine travelling as behaviour (the higher-leverage option this item
      named). See the merged plugin-review item above for the go-live detail.
      **The live floor now advances to the *next* deliberate widening** — a
      public announcement, a v2 plugin (de-instanced `create-repo`, `worktree`/
      `fleet-pins` commands), or a published package. Still Mike's call, never the
      agent's initiative. For an announcement, reuse the ros `PUBLISHING.md`
      extract-scrub-fresh-export pattern; **scrub list must include client
      names**.

- [x] **atelier's own CI** — DONE 2026-07-10 (Opus): `.github/workflows/ci.yml`
      (job `floor`) dogfoods the floor every review asserted by hand — the tool
      test suite, three scanner `--selftest`s, and the scan triad over the whole
      tree. Zero-dep stdlib means a public runner needs only Python. Honest
      scope baked into the header: secretscan/licenscan at full cover; **leakscan
      structural-only, deliberately no `--require-terms`** (its term list is
      machine-local by design — CI can't hold it and must not). Least-privilege
      (`contents: read`), concurrency-cancel. **Live-proven twice on GitHub** (7s,
      11/11 steps, no deprecation annotation after the `checkout@v5`/
      `setup-python@v6` bump) — not assumed; watched green.
- [x] **Wire the public scanners into child CI** — DONE 2026-07-10 (Opus): the
      other half of the CI build, unblocked by the public flip (ADR 0005).
      `docs/build/templates/workflows/floor.yml` — a language-agnostic scanner
      floor any doctrine-inheriting child drops in beside its `ci.yml`. It checks
      `mike548141/atelier` out **as a sibling** and runs its public
      secretscan/leakscan/linkscan against the child's own tree (`repo/`) — no
      secret, no vendored copy, no drift. Design calls stated in the header, not
      buried: **floats `atelier@main`** (a scanner *floor* wants newest; also
      avoids a second stamped-SHA drift surface — the CLAUDE.md pin stays the sole
      doctrine-version truth; `ref:` commented for anyone wanting reproducible CI);
      **leakscan structural-only** (term list is machine-local — same honest scope
      as atelier's own `ci.yml`); **licenscan commented** (it hard-fails with no
      LICENSE, so it's a *publish* gate, wrong to default-on for a private child).
      Scan scoped to `repo/` because a whole-workspace scan would false-positive
      on atelier's own fake-secret fixtures (proven, load-bearing). Driven both
      ways before claimed: clean child passes 0/0/0, damaged child (real `AKIA…`
      key + broken link) blocks. Wired into create-repo (seed step 3, step 6 CI
      text), REPO-STANDARD file set, and pinned by 5 `test_templates.py` tests
      (one-source, repo-scoped, structural-only, licenscan-commented, least-priv;
      suite 190→195). The step-6 "not wired yet" text is retired.
  - [x] **Exercised on a real child (numen) — DONE 2026-07-11 (Opus).** Session
        27's owed real-child run: numen adopted `floor.yml`, closing its own
        stated no-CI-gate (unblocked by ADR 0005). Driving it caught two real link
        breaks in numen before push and exposed a **four-session linkscan false
        negative** — `SKIP_DIR_NAMES` held `build`, masking atelier's own
        `docs/build/` layer (14 files); fixed at `d0870a4` (drop `build`/`dist`;
        suite 195→196), which also caught the inherited template placeholder (now
        code-spanned). Proven on real GitHub Actions both ways: happy path green
        (`29092514962`), fail-closed red via a throwaway broken-link PR
        (`29092599385`, since cleaned up). Detail:
        `sessions/2026-07-11-28-child-ci-floor-exercised.md`.
  - [x] **Review the child-CI floor + the linkscan masking fix** — RAN
        2026-07-11 (Fable, cold session): **PASS-WITH-FINDINGS**, verdict below
        the divider in `docs/reviews/2026-07-11-child-ci-floor.md`. The brief's
        sharpest question answered decisively: the masking fix closed the
        *instance*, not the class — secretscan + leakscan still hardcode-skipped
        `build`/`dist` (a planted key in `docs/build/` scanned green, proven
        live), still phantom-succeeded on a nonexistent path (the linkscan L1
        class), and the child's ignore-file hatch was dead under exactly the
        floor.yml invocation (CWD-relative vs root-relative globs). Six findings
        N1–N6, all [fixed] + re-driven same session (suite 196→205): both
        scanners mirror the linkscan fixes; floor.yml gains every-push triggers
        (a never-PR'd branch was scanned by nothing), a selftests step, and
        in-file FP-hatch docs. Floating `atelier@main` attacked and **held**
        (N1–N3 reaching every child with zero bumps is the argument); the
        real-infra secret drive judged NOT owed (closed by composition).
        **Gate cleared — floor.yml may roll to further children.**
        - [x] Follow-ups — BOTH DONE 2026-07-11 (Opus), each proven on real
              infra. **atelier's own `ci.yml`** widened to every-push +
              `workflow_dispatch` (`2a4b2fd`); the gap-closure proven by pushing
              a throwaway `n4-trigger-proof` branch (never PR'd) and watching CI
              fire green on it — a run that would not have existed before — then
              torn down local+remote. **numen re-copied `floor.yml`** byte-for-
              byte from the post-review template (numen `f81f66f`), picking up the
              workflow-file fixes that don't float (N4 every-push, N5 selftests
              step, N6 hatch docs); numen's floor ran green with the new selftests
              step live in the job log. numen's tree re-scanned clean in the exact
              floor.yml shape first. numen's frozen pre-scaffold hook (no linkscan)
              stands as already flagged — its floor is the only linkscan gate.
- [x] **Markdown internal-link check** — BUILT 2026-07-10 (Opus), **REVIEWED
      2026-07-10 (Fable, cold session): PASS-WITH-FINDINGS, gate cleared** —
      verdict below the divider in `docs/reviews/2026-07-10-linkscan.md`.
      `tools/linkscan.py`, the mechanical check that atelier's "thin anchor, fat
      pointer" graph actually resolves. The review proved damage to **all five**
      of the brief's load-bearing assumptions and fixed it same session (suite
      171→187): L1 a typo'd path arg scanned nothing and exited 0 (the §14
      silent-success class — now exit 2); L2 case-mismatched links green on APFS
      but 404 on GitHub (now walked against on-disk casing, NFC/NFD-safe); L3
      links escaping the repo root (new `outside-root` kind — GitHub serves
      nothing above root); L4+L5 anchor matching now exact like GitHub's, after
      fixing the slugger's underscore-stripping divergence; L6 parenthesised
      filenames parse; L7 fence tracking length/info-string-aware (nested ````
      examples stay code); L9 setext headings now mint anchors. L8 root-relative
      `/…` semantics verified against GitHub docs; L10 indented-code FP stated
      as residual by design.
  - [x] **Wire linkscan into `ci.yml` + `pre-commit.sample`** — DONE 2026-07-10
        (Opus), the session after the verdict (don't-stack honoured). CI: a
        `--selftest` line + a whole-tree `linkscan --root . .` step, mirroring
        the triad. Hook: linkscan added as a **whole-tree integrity** check —
        *not* `--staged` like the two boundary scanners, because a link breaks
        when a *different* file is renamed/deleted (the stale file is usually
        not the one in your diff). `run_scan` generalised to drop the hardcoded
        `--staged` so each scanner declares its own mode; header documents the
        distinct contract; block-message + README updated. Contract pinned by
        three new `test_precommit.py` tests incl. the whole-tree crux (a rename
        breaking an *unstaged* link blocks — a staged-only scan would miss it);
        suite 187→190. Installed atelier hook refreshed so this very commit
        dogfoods it. **Residual, stated:** a scaffolded child inherits the
        stricter whole-tree contract (its whole doc tree must stay link-clean to
        commit, vs the diff-scoped boundary scanners) — cheap for a clean tree,
        `linkscan:allow`/`.linkscanignore`/`--no-verify` are the hatches.

## Open questions — resolved
- ~~`docker-heap` is unstandardised~~ — DONE 2026-07-11 (Opus, session 38):
  standardise-existing pass applied (doctrine block + pin `atelier@5db645e`,
  house README, `docs/` with ARCHITECTURE/ROADMAP/SESSIONS, CONTRIBUTING,
  `floor.yml` scoped for an infra repo, fail-closed hook, `.gitignore` fixed —
  it was self-ignoring + untracked). No stack config touched; what the scans
  reported is the owner's, in that repo's own private records *(reworded
  2026-07-13 on the principal's decision — the name × posture join; old wording
  in git history)*. Now `current` in `tools/pins.py`.
- ~~Where does estate-wide credential **governance** live?~~ — RESOLVED
  2026-07-13, the principal's designation: it lives in the **dedicated private
  estate-root repo**, which already exists and already holds the registry
  (metadata only — provider, scope, keychain item, expiry, roll story; never a
  value), the mint tooling, and the estate map, with its own ADR recording the
  root→child pattern. Which repo that is stays out of this public record —
  naming the registry's home is itself the pointer RECORD keeps out. The
  remaining half stands: the root→child *pattern* becomes a method/ candidate
  once a second provider confirms the shape.

## File-size hygiene — completed detail

- [x] **`sizescan` reviewed + wired into the gate** — DONE 2026-07-14. Cold pass
      cleared (PASS-WITH-FINDINGS); F1 (fail-open ancestor-dir MAJOR) fixed +
      live-reproven, F2 (prose-mention self-exempt) fixed (markers header-only),
      F4 dedup fixed; **F3 decided by Mike — index rotation** (`SESSIONS.md`
      tail + `SESSIONS-ARCHIVE.md` growth store; RECORD.md sharpened). Now runs
      `--check` in atelier's `ci.yml` and the child `floor.yml` template (a repo
      that adopts the floor while over-budget reds → the signal to harvest;
      `sizescan:budget=N`/`allow` hatches). Suite 240→247; pinned in
      `test_sizescan.py` + `test_templates.py`.

- [x] **atelier: sizescan + RECORD doctrine + this ROADMAP harvest** — DONE
      2026-07-14 (1091→lean; completed detail → `ROADMAP-DONE.md`). Dogfood of
      the doctrine here first.

- [x] **faves: SESSIONS/ROADMAP/ARCHITECTURE harvest — DONE 2026-07-18,
      `sizescan` clean.** `SESSIONS.md` 1157→234 (rotation → new
      `SESSIONS-ARCHIVE.md`), `ROADMAP.md` 766→299 (resolved → new
      `ROADMAP-DONE.md`, verbatim), `ARCHITECTURE.md` 276→250. `dba7658..ab6a12d`.

- [x] **shed: SESSIONS.md rotated — DONE 2026-07-18**, 318→204 (older entries
      verbatim → new `SESSIONS-ARCHIVE.md`; all 14 verified present once).
      Also fixed en route: shed's `hooks.atelierTools` was *relative*
      (`../atelier/tools`), resolving only from the main checkout, so the
      fail-closed pre-commit scanner blocked every worktree commit — set
      absolute. **Worth checking on other children.**

- [x] **ros: completed-detail harvest — DONE 2026-07-18** (`d92de7f..5ae6ee1`).
      `ROADMAP.md` **7123→4755** (116 done blocks → `ROADMAP-DONE.md` behind
      pointers; harvester took only `[x]`, >4 lines, **no nested open sub-item**;
      verified byte-identical, open census unchanged). Also `SESSIONS.md`
      269→174, `CLAUDE.md` 257→135 (legacy half → `docs/LEGACY-INIT.md`),
      `tiki/docs/ARCHITECTURE.md` 329→319. Stated scope complete.

- [x] **ros: both structural calls ruled by Mike + applied 2026-07-18.**
      *(a) SPECS migration* — ROADMAP **4756→982** (7123 at session start, 86%
      down) in three verified passes; each block byte-identical in `SPECS.md`,
      open census unchanged (101 `[ ]` + 24 `[~]`), 125 titles reachable. Stays
      **+682 over 300, signal left lit deliberately** — 125 open items is a
      structural floor, not bloat. *(b)* Purpose split to `tiki/docs/PURPOSE.md`;
      `ARCHITECTURE` 319→**218**, hatch withdrawn.

- [x] 🚩 **Budget hatches must be grounded — corrected 2026-07-18 (Mike caught
      it).** a declared `sizescan` budget of 320 had been declared on a 319-line file: derived
      from the file's own length, so circular — and the *"raise the budget"* move
      the 2026-07-14 review already ruled *"defers, doesn't resolve"*. The
      hatch's docs never said so; now fixed at the point of use in
      `tools/sizescan.py`.

- [x] **Lean-files doctrine + `sizescan` — reviewed 2026-07-14, all findings
      resolved, cycle closed.** Cold un-briefed pass **PASS-WITH-FINDINGS**
      (1 MAJOR · 2 MEDIUM · 1 LOW); verdict in
      `reviews/2026-07-14-2048-lean-files-sizescan-cold.md`. F1 (fail-open
      ancestor-dir) + F2 (body marker self-exempt) + F4 (dup paths) fixed +
      pinned + F1 live-reproven; **F3 decided by Mike — SESSIONS index rotation**
      (RECORD.md sharpened: append-only *content*, relocatable home →
      `SESSIONS-ARCHIVE.md`). `sizescan` now wired `--check` into the gate.

- [x] **Budgets are tripwires, not targets — Mike's ruling 2026-07-19, APPLIED
      2026-07-19; SUPERSEDED 2026-07-20 by the cold-content rebalance.** As
      applied: `--check` gated only the lossless-remedy files (`ROADMAP.md`,
      `SESSIONS.md` — a red demands a *move*, never rewording); judgement docs
      (`README`/`ARCHITECTURE`/`CLAUDE`) reported but never failed the build; the
      one-sided signal (no thinness floor) stated as deliberate in the module doc.
      **Superseded** 2026-07-20 (Mike's 2026-07-20 rebalance): the gate no longer
      keys on file class *or* line count at all, but on relocatable **cold
      content** — a `[x]` item on the hot path. The tripwire-not-target insight
      survives (its "always has a lossless fix" logic is exactly why the
      cold-content gate is fair); only its line-count *mechanism* was replaced.
      See the review-owed rebalance entry in `ROADMAP.md`.

- [x] **Size-signal rebalance to a cold-content gate — cycle CLOSED 2026-07-21.**
      Mike's 2026-07-20 ruling (reverses the 2026-07-19 line-count gate): **cost
      is size × read-frequency**, so the enemy is never fulsomeness but **cold
      content on the hot path**. `sizescan` now gates on relocatable cold content
      — a completed `[x]` item on a checkbox-worklog file, whose fix is a lossless
      move to `ROADMAP-DONE.md` — and **never on length** (demoted to a pure
      advisory that reports but never fails a build, so a wholly-open roadmap is no
      longer penalised and the number can't induce line-golf). Prose-shaped cold
      content + thinness stay caught at review, not measured. Applied 2026-07-20
      (Opus): `sizescan.py` reworked (static `GATED` set gone), `ci.yml`+`floor.yml`
      retitled, `RECORD.md` module doc; `main`'s floor green **the right way** —
      4 inline `[x]` items harvested, not lines trimmed.
      **Reviewed 2026-07-20 2047 UTC (rule-4 independent, Fable): PASS — 0 MAJOR /
      2 MEDIUM / 3 LOW** (`reviews/2026-07-20-2040-size-rebalance-cold.md`).
      **Mike ruled accept-all 2026-07-21; applied same day (Fable, terminal
      application):** SR1 `tools/README.md` § sizescan rewritten to the cold-content
      frame (was documenting the dead line-budget model at the commit that removed
      it); **SR2-C the child-block "~50 lines" figure dropped entirely** — it sat at
      measured-49+1, circular by the delta's own standard; the structural rule (one
      bullet per irreducible concern) already does the work and nothing gates on
      length; SR3 detector edges fixed (`[x]`-in-code-fence false positive; `+`/
      ordered-bullet misses) — suite 282→284; SR5 the rule-4 refs-only pointer
      ceiling stated in the ROADMAP header at point of use (breached two cycles
      running — a point-of-use framing gap, not a compliance one). SR4 ("moved
      verbatim" overclaim in the authoring record) resolved **accept-as-noted**:
      the record is immutable history, the correction stands in the review verdict.

- [x] **hooks.atelierTools worktree bug was fleet-wide — 2026-07-19.** 9 more
      children carried the relative path (every worktree commit blocked by the
      fail-closed hook); all 10 set absolute, and the **source fixed** —
      `create-repo` step 6 now absolutises the path it stamps. (Resolves the shed
      entry's "Worth checking on other children" above.)

## instruments/ccarchive — completed detail (moved 2026-07-19)

- [x] **Local-store audit vs the archive manifest — DONE 2026-07-17.**
      `ccarchive --audit` hashes every live `.jsonl` and buckets it against the
      manifest: **synced** · **grown** (archived bytes a strict prefix — a plain
      append, kept out of the drift signal so an active session isn't a false
      alarm) · **mutated** (rewritten/truncated) · **renamed** (content matched
      an archived path now gone from live) · **new** · **pruned**. Only mutated +
      renamed are drift (listed, non-zero exit); the rest are counted. Read-only
      over both trees (no write path ⇒ no git-worktree guard). Pure core
      (`auditCategorize` + `classifyDivergence`) unit-tested; +11 tests (35→46
      ccarchive, 86 instrument), man AUDIT section (mandoc clean), README +
      `--help`. Driven live: 435 archived · 432 synced · 3 grown · 19 new · 0
      drift → exit 0.

## Orchestrated queue run — completed detail (moved 2026-07-22)

The 2026-07-22-1018 run's ten landed items, harvested at the run's own close
(intent record: `sessions/2026-07-22-1018-orchestrated-queue-run.md`).

- [x] **SECRETS.md access-management expansion + ACCESS.md step-2 line** —
  rule-4 cold pass on `caa85fe` run 2026-07-22 by the wave-1 queue run
  (provenance in the brief; the run authored none of the delta):
  **PASS-WITH-FINDINGS 0 MAJOR · 4 MINOR · 4 LOW · 1 nit**, citations
  verified live, live-proven claims re-run clean, reconcile overturned
  nothing — terminal per the close rule, cycle closed. Verdict:
  `reviews/2026-07-22-1021-secrets-access-cold-pass.md`.
- [x] **Map the public canon against `method/` + the scanner floor** — done
  2026-07-22 (wave-1 queue run): mapping record
  `sessions/2026-07-22-1025-security-canon-gap-map.md`, every "already held"
  claim verified by reading the cited doc. Verdicts on the capture's
  candidates: **A** threat modelling CONFIRMED (narrow — reviewer-side held,
  the *builder* is never told to enumerate threats); **B** secure defaults
  CONFIRMED (narrow — fragments, not generalised); **C** supply chain
  CONFIRMED reframed (zero-dep *is* the control; the live residual is
  third-party CI actions pinned by mutable tag, not SHA); **D** secure-coding
  floor DISMISSED (instance-layer by design; one framing line owed); **E**
  vuln lifecycle CONFIRMED (partial — credential path fully held; missing
  severity/recurrence framing and a public-repo SECURITY.md disclosure
  posture). The mapping also corrected the section's "already held" list.
- [x] **`MODEL-ECONOMICS.md` renamed to `ECONOMICS.md`** — Mike's 2026-07-22
  decision executed 2026-07-22 (wave-1 queue run, `b639513`): `git mv` on
  the canonical file and the child-template copy, 24 pointer refs across
  16 live files; history append-only (113 old-name refs in records stand).
  Deliberation record: `sessions/2026-07-22-0435-economics-rename-decision.md`.
  Light review discharged mechanically per the item's own note: linkscan
  clean before/after, 323 tool tests green incl. the template block-sync
  test, orchestrator diff-verified at merge. Nothing dangles cross-repo —
  children resolve refs against their pins; each child updates its
  atelier-pointing refs (stamped block's session-rhythm pointer, floor.yml
  comments) **at its next pin bump**, and a child's own private
  `MODEL-ECONOMICS.md` counterpart keeps its name by that child's call
  (ros recorded exactly this, 2026-07-22).
- [x] **Queue-run: name the pattern in `method/`** — built 2026-07-22 by a
  fresh session per Mike's ratification ("build as counselled"), wave-2
  queue run, `343def8`: CONCURRENCY.md § Orchestrated queue runs (96 lines —
  run mechanics, role check at open, default selection order, per-item close
  as the cap-safety property, four named stop conditions + the 🎯-surfacing
  report, rule-4 synergy) + ECONOMICS.md § The orchestrated-run tier split
  (22 lines). Section-vs-new-file settled by the builder on actual size, as
  ratified. Every ratified element landed, incl. the deliberately-out items
  named at the point a reader would look. Grounded on both bearings
  (man-page rollout + the live 2026-07-22-1018 run).
- [x] **Queue-run: mechanise it as a skill** — built same delta, `8111e9f`:
  `skills/queue-run/SKILL.md`, plugin-bundled by auto-discovery exactly as
  review-brief travels (no manifest change needed — verified); stamped-copy
  header points up, narrowing-free.
- [x] **Anti-slop promotion rule — the mining half** — done 2026-07-22
  (wave-2 queue run, `84fb112`): 330 findings across all 47 review files
  clustered into 5 scanner candidates (S1 wrap-hygiene — the class that
  shipped three cycles running; S2 named-path-resolves; S3 UTC dating; S4
  template stamp-drift; S5 NZ spelling, carried on ROI) + 7
  verifier/checklist candidates (V1 overclaim-vs-evidence the largest
  cluster at ~30 — validating the doctrine, not exposing a gap),
  below-threshold classes named, already-enforced classes credited, and one
  ⚠️: fail-open/detector-edge (~23) kept recurring *after* the selftest
  floor — "harden tools/ tests", not "solved". Record:
  `sessions/2026-07-22-1036-invariant-candidates.md`.
- [x] **ccrepo: tighten the ccusage reconciliation drift** — done 2026-07-22
  (wave-2 queue run, `75bba4c`). Root cause found and fixed: the
  `(message.id, requestId)` dedup kept the **last** log line, and the logs
  re-emit messages with a trailing partial/zeroed usage line — last-wins
  silently dropped tokens. Now keeps the **richest** record (max-total),
  which matches ccusage **exactly** on a frozen matched-session set;
  sonnet-5 (the ~1.5% outlier) → 0.00%, total drift → ~0.00% with only
  in-flight current-session variance left, reported plainly.
  `server_tool_use` measured live: present on many messages but every
  counter zero — per-call pricing not built, the v1 "named contributor"
  hypothesis retracted in the design doc as measured-false. Per-model
  reconcile also scoped to matched sessions (one-sided window-edge sessions
  no longer smear into phantom per-model deltas). Suite 92→94 green (111
  instruments-wide, re-proven post-merge).
- [x] **ccarchive: restore from archive — full + delta** — built 2026-07-22
  (wave-1 queue run, `9ca1425`): `--restore` (full) + `--restore --delta`
  (audit's mutated/pruned/renamed buckets), `--dry-run`/`--force`/`--json`
  reused. Content-first safety: `grown` never a target (byte-prefix check,
  so even a full restore can't drop a live tail); diverged+newer live
  refuses unless `--force` (loud); zip-slip containment; additive only
  (renamed restores the OLD path, never deletes the live rename —
  documented choice). Suite 46→63 ccarchive / 109 instruments green,
  re-proven post-merge; live fixture run exercised every exit path. Man page
  + README updated per the CLI-docs standard.
- [x] **ccarchive: iCloud dataless-file awareness** — built 2026-07-22
  (wave-3 queue run, `12794d6`): `SF_DATALESS` read via BSD `stat -f %f`
  (Node exposes no `st_flags` — investigated incl. bigint stats),
  classifier **verified against a real evicted file** in the live archive,
  `stat` proven non-faulting. `--verify`/`--audit` skip evicted files into a
  distinct `evicted`/undetermined bucket (never a failure, never mis-read as
  missing/corrupt; success line says "every *checked* transcript"); opt-in
  `--materialise` reads them deliberately; `--restore` still faults content
  back by design (documented); manifest/backfill writes proven non-faulting.
  Honest residual: the end-to-end skip on a *live* eviction is
  seam-simulated, not exercised — nothing was evicted to test. Suite
  109→116 (118 instruments-wide post-merge). The `--json` audit contract
  gains the `evicted` array — consistent-awareness call endorsed at merge.
- [x] **ccarchive: sign the manifest (tamper-evidence)** — built 2026-07-22
  (wave-4 queue run, `2a85839`): detached HMAC-SHA256 sidecar
  (`manifest.json.sig`), key off-archive at `~/.claude` (file over Keychain
  — cron/launchd reads it promptless; the key guards tamper-evidence, not
  confidentiality), `--rekey` rotation re-signs the current manifest
  (SECRETS replaceability — a roll loses nothing), five verify states each
  honest and non-zero (tampered / key-mismatch / unsigned-legacy-migrates /
  no-key-unverifiable; verify never mints). The closed caveat proven live:
  forged `.gz` + recomputed manifest hash → signature MISMATCH, exit 1.
  Non-protections stated in the man page (key theft forges; no
  anti-rollback; evidence, not prevention). Suite 70→84 ccarchive / 132
  instruments-wide, re-proven post-merge. The two contestable defaults stay
  a live 🎯 on the ROADMAP.
- [x] **ccarchive: is there any metadata it misses?** — answered 2026-07-22
  (wave-3 queue run, `5ce9f00`): yes. The real hole is `tool-results/`
  sidecars — offloaded tool-output payloads the transcript only points at,
  so the archive can hold dangling references while advertising a complete
  record (≈7% of transcript volume; recommendation: CAPTURE, plus man-page
  honesty about what is excluded regardless). Full classification
  (capture / exclude-and-document / needs-Mike) in
  `sessions/2026-07-22-1050-cc-instruments-questions.md`. Rulings stay a
  live 🎯 on the ROADMAP.
- [x] **Should cctranscript and ccarchive be one?** — analysed 2026-07-22
  (wave-3 queue run, same record): **keep separate** counselled. Measured
  shared code is ~10 lines; merging would couple ccarchive's schema-immunity
  (the property guarding the sole durable copy) to cctranscript's
  schema-fragile parser, and blur ADR 0006's observe vs preserve verbs.
  Counter-case captured (natural pipeline pair → argues for a
  `--source <archive>` flag on the reader, not a merge); middle path (shared
  lib) only if shared code crosses ~40–50 lines. Mike's call whether to
  accept the recommendation; no work owed until then.

## Orchestrated queue run #2 — completed detail (moved 2026-07-22)

Run record: `sessions/2026-07-22-1210-orchestrated-queue-run.md`. Open residue
(🎯 VP1–VP8, 🎯 spend config, 🎯 D1–D5, the security-canon `⏳`) stays live in
ROADMAP.md; the finished detail is preserved here.

- [x] ⏳ **v2-plugin de-instance review — DELIVERED 2026-07-22 1221**
      (taken 1210 by the queue-run orchestrator, rule-4 provenance on the
      brief; two-hop fresh-context reviewer) →
      [`verdict`](reviews/2026-07-22-1215-v2-plugin-deinstance-cold.md).
      The 1018 run's "stray" worktree re-read on the evidence as a parked
      rule-4 handoff (complete recorded commit `1516ae1`, queued `⏳` inside
      its own delta), not a mid-flight death; merge stayed Mike's throughout.
- [x] **Doctrine edits for confirmed gaps A/B/C/E — BUILT 2026-07-22**
      (`85157c3`, merged `73da10d`): every third-party CI action SHA-pinned
      (ci.yml + all child workflow templates, five tag→SHA resolutions
      verified live twice); root `SECURITY.md` + child template, registered
      in REPO-STANDARD as publish-time; REVIEW.md gains the right-sized
      threat pass (A) + security-finding severity/recurrence-prevention (E);
      PRINCIPLES gains secure-by-default (B) + zero-dep-as-supply-chain-
      control with named residual (C). Worker divergences in the session
      record. Rule-4 `⏳` remains queued in ROADMAP.md.
- [x] **Actual spend (plan or usage) vs the API-usage estimate — BUILT
      2026-07-22** (`1711711`, merged `12613e0`): machine-local `spend`
      block (plan mode: months × fee + uncovered; usage mode: invoiced
      figures per month), reconciliation footnote with Δ $ and %, honest
      partial/unavailable degradation, JSON/CSV meta; 139 tests green;
      also fixed a pre-existing USD×rate² defect in the Actual footnote.
      Review: self-verifying class (instrument code under its test floor,
      no doctrine surface — ECONOMICS § Match the ceremony). Original item,
      for context — the money-side
      analog of the ccusage cross-check. ccrepo's cost is an API-list-price
      *estimate*; the billing model (`ccrepo-billing.json`) already apportions a
      flat plan fee into an Actual column, but Mike wants to compare **what he
      genuinely pays** — a subscription tier (e.g. Max 5x/20x) or metered usage —
      against what ccrepo computes from API usage, and see the delta. Needs a
      machine-local source of real spend (plan tier + period, or an exported
      usage/invoice figure) and a reconciliation footnote like the ccusage one but
      for dollars actually billed. Personal data ⇒ the spend source stays in
      `~/.claude`, never a repo (same boundary as `ccrepo-billing.json`).
      🎯 fill-the-config residue stays live in ROADMAP.md.

## v2 plugin shipped + the VP/D rulings (moved 2026-07-23)

- [x] **v2 plugin — CHOSEN 2026-07-13, SHIPPED 2026-07-23** (`0de6f52`).
      De-instanced `create-repo` travels in the bundle with `/atelier:worktree`
      + `/atelier:fleet-pins`; adopter-owned profile (eight instance facts incl.
      signing posture per VP2); canonical bundled-mode propagation block in
      PROPAGATION.md (VP1). History: built 2026-07-21 on branch
      `v2-plugin-deinstance` (`1516ae1`), found parked as the 1018 run's
      "stray", rule-4 cold pass 2026-07-22 (PASS-WITH-FINDINGS 2M/3M/1L/2n),
      **VP1–VP8 ruled per-finding by Mike 2026-07-23** — VP1–VP6+VP8 [fixed]
      as counselled, VP7 confirmed — applied `ff8a07f` on the branch rebased
      across ~155 commits (session-onramp resolution kept both queue-run wiring
      and the restructure), merged on Mike's merge-on-green ruling. Superseded
      baked-identity global skill retired (archived machine-locally). The
      application's own rule-4 `⏳` and the exercise-e2e residue stay live in
      ROADMAP.md.
- [x] **Portability D1–D5 ruled 2026-07-23** — decision stamps + grounds in
      `sessions/2026-07-22-1233-person-context-portability-design.md`
      §Decision stamps; headline: capsule rides the private estate repo;
      **full app-plane parity** (Mike's challenge upheld over the design's
      cautious counsel — no phone-unique risk); ADP available; key backup in
      the person-level credential home. Build items now live in ROADMAP.md.

## The 2026-07-23 decision sitting — standing backlog cleared (moved 2026-07-23)

Mike worked the whole standing 🎯 backlog in plain-language walk-throughs
(run record: the 1210 queue-run's addenda). Rulings and their closed items:

- [x] **ccarchive metadata classes + signing defaults** — sidecars, memory
      AND prompt history all captured (the last overturning the
      lean-exclude counsel); binary exits, new-machine-red, keep-separate
      all accepted. **Built same sitting** (`3c6394d`, merged `2df595e`):
      generalised walk + allowlist classifier, manifest/verify/signing
      untouched by design (they iterate manifest keys), restore redirects
      only tool-declared external rels, +11 tests (150 suite green).
- [x] **Invariant candidates S1–S5 / V1–V7 — all approved** (S5 explicitly
      on ROI over its borderline count); build items opened on the live
      ROADMAP.
- [x] **Checkbox grammar — keep the tri-state** (builder's counsel
      accepted; five states only if dispositions repeatedly need machine
      separation).
- [x] **Session archive — superseded by ccarchive under ADP-class E2E**;
      NAS second leg and retention clock consciously not taken (history
      kept indefinitely absent a retention ask). Original item text: NAS,
      local-only, ~12-month rolling, no search index (searchability = exfil
      surface); NZ Privacy Act retention noted for third-party PII.
- [x] **Floor-template duplicate trigger — trim `pull_request` on no-fork
      private children at pin bump; template stays two-trigger.** Preserved
      analysis: `push` scans the branch tip (what a public push publishes),
      `pull_request` scans the merge preview a tip-push can't see and
      covers fork PRs — not pure duplicates; the N4 review chose every-push
      for publish-safety, which holds for public repos; on private no-fork
      children the second metered run buys little (owner-only
      contributors) and costs half the minutes pool.
- [x] **Signing warn→block flip — hold re-confirmed** (rotation sitting
      offered, declined for now).

Still Mike's, deliberately untouched: the honesty/truth/transparency note
(being expanded via the apex-triad work), the Teams-chat note (prompted
verbatim, awaiting his expansion), the glossary ratify pass (his read).

## Orchestrated queue runs 0441 + 0618 — completed detail (moved 2026-07-23)

Two Opus-orchestrated queue runs' deliveries. The 0441 run left its four `[x]`
items un-harvested on the live ROADMAP; the 0618 run harvested both runs'
completed items at its close to restore the `sizescan --check` floor to green
— the worked case for the ROADMAP "close all-clear should carry the pushed
floor run's result" capture (the floor had been red on un-harvested `[x]`
across several sessions).

### Doctrine

- [x] **In-repo apex restatements swept to three-element — DONE 2026-07-23**
  (`a4740c4`, queue run, Opus worker). All named surfaces aligned to the widened
  apex (honesty → adaptation → the Laws): `README.md` (×2), `PRINCIPLES.md` (×2),
  `PROPAGATION.md` (description + inlined floor block), `build/templates/CLAUDE.md`
  floor block (kept **byte-identical** to PROPAGATION's — cmp + `test_templates`
  32/32 confirm the lockstep), `method/README.md` (EVIDENCE now behind honesty
  **and** adaptation), `session-onramp/SKILL.md` (description + a new
  Adaptation-is-continuous §1 bullet). AW8's honesty-precondition clause is
  verbatim on the child floor's adaptation line. Dated records / review files /
  EVIDENCE.md's accurate single-element honesty citation left untouched. This is
  the closed apex-widening cycle's scheduled application ⇒ no new review owed.
  (Its sibling `[ ]` "Propagate the widened apex floor to the fleet children"
  stays open on the live ROADMAP — the fleet half, pin-bump lane.)

### Anti-slop invariant scanners S1/S3/S5 + the S3 review

All three wired ADVISORY-ONLY (`--warn`, exit 0) in `ci.yml`; none in the
blocking pre-commit hook nor child `floor.yml` — each earns an independent
review before gating (don't-stack). Their `⏳` first-of-kind reviews (S1, S5)
and the datescan follow-ons (apply DSR1–DSR8; the advisory→blocking flip) stay
open on the live ROADMAP.

- [x] **S3 datescan BUILT 2026-07-23** (`6077972`, 0441 run, Sonnet worker).
  `tools/datescan.py` + 41 tests + `--selftest`. Relative-time-word denylist +
  non-ISO/invalid-ISO date check over `docs/**`, with
  fenced-code/blockquote/quoted-mention exemptions (limits documented honestly
  in-header; the "dated edit carries its date" clause stays review-only). Honest
  baseline left uncleaned as review evidence: **60 findings / 43 files**.
- [x] **S1 wrapscan BUILT 2026-07-23** (`72e8ecb`, 0618 run, Sonnet worker).
  `tools/wrapscan.py` + 40 tests (suite 412 green) + `--selftest`. Flags
  `docs/**` prose lines ≥86 cols; exemptions: fenced/indented code, table rows,
  ATX headings, ref-link defs, single-unbreakable-token overflow (each limit
  documented in-header; character-count not display-width is a stated Unicode
  caveat). Honest baseline: **286 findings / 19 files**. 🚩 worker flagged
  153/286 sit in `docs/SESSIONS.md` (a deliberate one-line-per-session log) and
  review-verdict files cluster heavily — whether those need a prose exemption /
  `.wrapscanignore` entry is a gate-readiness question for the ⏳ review.
- [x] **S5 spellscan BUILT 2026-07-23** (`760260473`, 0618 run, Sonnet worker).
  `tools/spellscan.py` + 60 tests (suite 432 green) + `--selftest`. NZ-English
  wordlist over `docs/**`: generative `-ize/-ise` + `-yze/-yse` stem families
  (irregular-noun stems excluded so it never invents a word) + hand-listed
  irregulars. Exemptions: fenced/inline code, blockquotes, quote-flanked MENTION,
  URL/path tokens, an `ALLOWLIST_PHRASES` for bare-prose API terms,
  ALL-CAPS-as-identifier. **license/practice deliberately EXCLUDED** — US/NZ
  noun-verb homographs untaggable without POS. Honest baseline: **68 findings /
  32 files** (`artifact` ×53, `catalog` ×10…) — confirms "under-detected, not
  rare".
- [x] **datescan (S3) review DONE 2026-07-23** (0618 run, Opus cold reviewer;
  brief+verdict `reviews/2026-07-23-0618-datescan-s3-cold.md`). Rule-4 clear:
  authored by the 0441 chain, taken by the independent Mike-started 0618 session.
  **Verdict PASS-WITH-FINDINGS, 0 MAJOR / 4 minor / 3 Low / 1 nit** — engine
  correct, honestly documented, correctly wired advisory; no active silent-miss
  producible. **But NOT gate-ready**: the 60-finding baseline is ~75% noise
  (currently-sense `today`, DSR3; numeric-triple FPs, DSR2; multi-word quoted
  mentions, DSR4). No MAJOR ⇒ review terminal; datescan stays advisory.

### instruments — cc-tools flag vocabulary (Mike, 2026-07-23)

- [x] **Audit + align the flag vocabulary across the cc-tools — DELIVERED
  2026-07-23** (`85b17dd`, 0441 run). End-to-end read of all three tools'
  `--help`, man pages and arg parsers confirmed **zero drift** — `--dest`,
  `--from-archive`, `--materialise`, `--json`, `--repo` all consistent where they
  overlap; no renames. Landed a **vocabulary table** in `instruments/README.md`
  as the standing reference, with the `--materialise` asymmetry documented as
  deliberate (cctranscript has no bulk-read op to name).
- [x] **Flag-vocabulary rule RATIFIED 2026-07-23 (Mike): flags-follow-operation**
  — uniform vocabulary whenever the operation is shared, but a flag is added to a
  tool only when that tool actually performs the operation it names (never bolted
  on for symmetry; the `--materialise`-on-cctranscript no-op is the rejected
  alternative). Blessed as adopted principle in `instruments/README.md`. cc-tools
  vocabulary strand closed.

### instruments — ccrepo rollup precompute ledger (Mike, 2026-07-17)

- [x] **ccrepo rollup precompute ledger — DELIVERED 2026-07-23** (`8a31b95`,
  0441 run, Opus worker; `ccrepo.design.md` §8). Machine-local ledger at
  `~/.claude/ccrepo-rollup.json` (mirrors the pricing/billing config convention;
  `CCREPO_ROLLUP` override), so a warm `--from-archive` run reads the ledger
  instead of re-gunzipping every file. **Live smoke: 3.1× faster warm, numbers
  byte-identical cold vs warm** (the rollup==recompute floor, proven in a fixture
  test AND on the real archive; invalidation tested; ccrepo 48/48, instruments
  167/167). **One endorsed design deviation:** keyed **per-file, not per-period**
  — a month can't be fingerprinted without first reading files for message
  timestamps (chicken-and-egg; file mtime ≠ message timestamp), so period-keying
  would misfile boundary-straddling sessions and break the floor. Per-file
  `(mtime,size)` is provably exact. Known tradeoff: ~46 MB ledger; compaction is
  a safe future optimisation. No review gate (design §9 self-verification).
- [x] **Rollup default CONFIRMED 2026-07-23 (Mike): transparent-by-default** (as
  shipped) — auto-used in `--from-archive` mode with a `--no-rollup` bypass; no
  code change. Mike aware of the ~46 MB machine-local ledger the first warm run
  writes under `~/.claude/` (recoverable). ccrepo rollup-ledger strand closed.
- [x] **ccrepo context-size column — DELIVERED 2026-07-26** (`c94f75e`, inline
  Opus; `ccrepo.design.md` § "Context size"). Mike asked for a reading of when
  window sizes get large and named the three candidate shapes himself (sum /
  average / max). **The answer was measured before it was chosen** — a throwaway
  probe over the live logs (419 sessions, 107,902 assistant messages) killed two
  of the three: **sum is meaningless** (every message carries the whole cached
  prefix, so it counts one window repeatedly — context is the only metric that
  must never go through `addTo`), **mean is skewed** by exactly the outliers the
  column exists to catch. Shipped as **one column, two numbers** (`110k/578k` —
  median beside max), which also answers the column-count concern. One repo
  settled it: median 108k, max 578k — scariest on the board by max, calmest by
  median. Grain is the **per-session peak**, not per-message (message-grain
  understates: 122k vs 168k across the set), matching what `cctranscript` already
  headlines. **A `% of window` column was designed and abandoned as unbuildable**
  — the logs carry no `[1m]` marker, so 200k and 1M variants are
  indistinguishable; the 934k observed peak proves 1M sessions exist but not
  which. Recorded so it isn't re-derived. `--json`/`--csv` deliberately go
  **wider than the table** (Mike's follow-on: a data file isn't width-bound) —
  full distribution incl. `p90`, plus the covered/uncovered split behind
  `Actual`; grand total in `meta.total` because peaks can't be re-aggregated from
  leaves. **`ROLLUP_SCHEMA` → /2 was load-bearing, not housekeeping:** the
  `(mtime,size)` fingerprint only proves the *source* unchanged, so v1-cached
  events lacking the new field would have reported a confident **zero** context
  on every warm archive run forever — caught at design time, with a test that
  rewinds a ledger and proves it's re-read. 180/180 tests, floor 9/9.
- [x] **ccrepo `opus-5` price gap — FOUND + CLOSED 2026-07-26** (`ba40c62`, same
  session). No `opus-5` entry meant 1,314 messages in one live drive counted at
  **$0**. Added at **$5/$25 per MTok** from Anthropic's published list (same as
  `opus-4-8`). **Verified, not assumed:** the ccusage cross-check moved to
  **Δ +$0.00 (+0.00%) across all 420 sessions** — the oracle agreeing to the cent
  with a number read from the list rather than fitted to the logs. Notable for
  *how* it closed: it was first handed to Mike as needing a published price
  (citing the ban on fitting numbers to one's own measurement) when the price was
  one lookup away. Mike's correction — *"you got the prices for the other models.
  Isn't there an API or web page you can reference?"* — became the `EVIDENCE.md`
  §13 doctrine delta (⏳ queued). Same lookup surfaced `sonnet-5` sitting at its
  **introductory** `$2` rate, which reverts to `$3` on **2026-09-01**; left at
  `$2` as correct through 2026-08-31 and queued as a dated edit, not a decision.

- [x] **CI floor restored to green — DELIVERED 2026-07-26** (`eac5581` +
  `908de1d`, inline Opus, found during a close-out check). The pushed floor had
  been **red since `6749202` (2026-07-25 13:16)** — ~19 hours, 20+ consecutive
  failing runs, across several sessions — while every session's *local* scan
  reported 9/9 green. Two stacked failures, the first masking the second.
  **(1)** `floor.py --json` violated its own documented contract (`run()`:
  *"stdout carries nothing but the JSON document"*) by printing Actions
  `::group::`/`::error::` markers to stdout unconditionally, so a caller parsing
  `--json` from inside a workflow hit `JSONDecodeError` on line 1 — that caller
  being our own `test_missing_records_tree_skips_visibly`. **The failure was
  environment-gated, not logic-gated:** `GITHUB_ACTIONS` is never set on a dev
  machine, so the suite was green locally and red only in CI, the one place
  nobody re-runs by hand. Fixed by routing the markers to `child_stdout` (stderr
  under `--json`, stdout otherwise); both workflows invoke floor.py *without*
  `--json`, so grouping still renders where it is consumed. New
  `test_json_stdout_stays_pure_inside_actions` pins `GITHUB_ACTIONS=true` for the
  subprocess so the contract is tested where it breaks; suite 660 → 661, green
  under both conditions. **(2)** With the pipeline unblocked, a never-reached
  step ran and failed: `mandoc -T lint` on an 81-byte line in `ccrepo.1`, from
  the same session's context-column work — verified locally with `man -P cat`
  (which *renders*) rather than `mandoc -T lint` (which *checks*, and isn't
  installed locally). Rewrapped. Floor at head green. **Standing gap flagged:**
  no local equivalent of the mandoc gate exists on this machine.

## Queue run 0707 — datescan DSR-apply + S1/S5 first-of-kind reviews (moved 2026-07-23)

Verbatim from ROADMAP.md; the live follow-ons (apply-findings + Mike's-call
flips/rulings) stay open in ROADMAP.md. Session record:
[`sessions/2026-07-23-0707-orchestrated-queue-run.md`](sessions/2026-07-23-0707-orchestrated-queue-run.md).

- [x] **Apply datescan review findings DSR1–DSR8 + re-baseline** — DONE
      2026-07-23 (queue run 0707, Sonnet worker, merged `b7b292c`→ merge commit).
      All eight applied; baseline **60→0** (5 genuine hits fixed: ISO rewrite
      where re-derivable, `datescan:allow` with honest reasons where not). Three
      extra real bugs caught mid-work (whole-line ISO cue leak, `YYYY-MM-DD-HHMM`
      false-fire, empty `-->` reason). 58 datescan + 489 tools-suite green; DSR3
      `today`-narrowing silent-miss trade declared in-header. Orchestrator (Opus)
      verified before merge.
- [x] **wrapscan (S1) first-of-kind review — DONE 2026-07-23** (queue run 0707,
      cold Opus reviewer; taker rule-4 cleared). Verdict **PASS-WITH-FINDINGS —
      1 MAJOR / 3 minor / 2 Low**, NOT gate-ready. Tool is correct, honestly
      documented, correctly wired advisory; 40 tests + selftest green (orchestrator
      re-verified). The MAJOR (WS1) is a **gate-scope** finding, not a detection
      bug: default `docs/**` buries the real signal (~15% doctrine-prose
      over-wraps) under 154 deliberate single-line SESSIONS index rows (54% of the
      287 baseline). Brief:
      [`reviews/2026-07-23-0707-wrapscan-s1-cold.md`](reviews/2026-07-23-0707-wrapscan-s1-cold.md).
- [x] **spellscan (S5) first-of-kind review — DONE 2026-07-23** (queue run 0707,
      cold Opus reviewer; taker rule-4 cleared). Verdict **PASS-WITH-FINDINGS —
      0 MAJOR / 2 minor / 1 Low / 1 nit**, NOT gate-ready. The core spelling-tool
      safety property is *proven*: no confident wrong correction, no both-correct
      word flagged (z→s engine verified across all 46 noun forms). 60 tests +
      selftest green (orchestrator re-verified). Real latent bug found (SS1:
      `hypothesize`/`jeopardize`/`penalize` in `IZE_NOUN_CAPABLE` contradict the
      docstring's stated exclusion). Baseline ~1-in-5 signal — 53 of 68 are
      `artifact` (mostly the legit CI/SBOM term-of-art). Brief:
      [`reviews/2026-07-23-0707-spellscan-s5-cold.md`](reviews/2026-07-23-0707-spellscan-s5-cold.md).

## Queue run 0959 — S2/S4 scanner builds + wrapscan/spellscan applies (moved 2026-07-23)

Opus-orchestrated queue run (Mike: "maximise plan use"), Sonnet executors in
worktrees, per-item close. Four items closed (a fifth, the RECORD.md
close-all-clear doctrine, stays live as a ⏳ review in ROADMAP.md).

### Anti-slop invariant scanners — S2 + S4 built (all five S1–S5 now built)

- [x] **Build the approved scanners S1–S5** — ALL FIVE BUILT + wired advisory.
      S2+S4 landed 2026-07-23 (queue run 0959): **S2 `pathscan`** (`b738f21`,
      merged) — bare-prose/backtick repo-path resolution, the half linkscan's
      markdown-link resolution can't see (triple-anchor: root / own-dir /
      outermost-`docs`-ancestor; 53 tests; 174-finding heuristic-noise baseline
      by design); **S4 `stampscan`** (`2fe97f3`, merged) — a new mechanism
      comparing an inlined-floor stamped block to its pinned canonical parent
      region (`stamp:begin source=… region=…` HTML-comment markers, wired to the
      real templates/CLAUDE.md↔PROPAGATION.md floor pair, byte-identical → CLEAN;
      46 tests; `narrow=<reason>` distinguishes a declared narrowing from a silent
      drop). Both Sonnet-built, Opus-verified, ship ADVISORY (`--warn` in
      `ci.yml`, absent from hook + `floor.yml` per don't-stack). Combined suite
      601 green. S1/S3/S5 built earlier (`72e8ecb`/`6077972`/`760260473`). Each
      of S2/S4 earns a queued ⏳ first-of-kind rule-4 review (live in ROADMAP.md)
      before any gate.

### wrapscan (S1) review applied — WS1–WS6 + option-A scope

- [x] **Apply wrapscan review findings WS1–WS6 + implement option-a scope** —
      DONE 2026-07-23 (queue run 0959, Sonnet `ceb3fda`, Opus-verified/merged).
      WS1 option-A scope live (`ci.yml` gates `docs/method docs/build
      docs/decisions`, `.wrapscanignore` the record/log/review stores);
      the 3 genuine over-wraps fixed (REPO-STANDARD:52, SIGNING:83,
      CONCURRENCY:232); WS2 tightened (structural pipe signal), WS4 sibling
      allow-marker padding exempted, WS3 accepted-and-documented as a gate-time
      residual (reprocessing an unclosed fence would false-positive on truncated
      pasted code — worse failure mode), WS5 documented wart. Suite 497 green,
      gated scope 0 findings. Stays ADVISORY — no flip. The wrapscan flip
      precondition (clean run over the gated doctrine surface) is now MET; the
      flip stays Mike's go/no-go (live in ROADMAP.md).

### spellscan (S5) review applied — SS1–SS4 + catalogue rename

- [x] **Apply spellscan review findings SS1–SS4 + tame the noise** — DONE
      2026-07-23 (queue run 0959, Sonnet `b910962`, merged `4872f07`,
      Opus-verified). SS1 (dropped `hypothesize`/`jeopardize`/`penalize`,
      verb forms preserved), SS2 (macron out-of-scope declared honestly),
      SS3 (allowlisted the CI/SBOM `artifact` term-of-art + OWASP ASVS/SAMM
      chapter names — general "produced-thing" sense deliberately kept
      flagged), `finalize`→`finalise` fixed, `catalog`→`catalogue` renamed in
      both frozen records (article quote left verbatim). Suite 65 spellscan /
      502 total green. Stays ADVISORY. Baseline 71→40 — not near-zero; the
      remainder is all genuine or preserved quotes. Surfaced a live follow-on
      (the ~36 general-sense `artifact` breaches in frozen records — Mike's
      call, live in ROADMAP.md) which also blocks the spellscan flip's
      near-zero re-baseline.

### wrapscan + spellscan flipped advisory→blocking (Mike's rulings, same run)

Both scanners built/reviewed/applied earlier this run were flipped to BLOCKING on
Mike's plain-language rulings during the close-out:

- **wrapscan → blocking.** Precondition met (option-A doctrine-surface scope,
  0 findings). atelier `ci.yml` dropped `--warn`; child `floor.yml` template
  gained a blocking wrapscan step + selftest (children re-baseline their record
  stores via `.wrapscanignore` on adoption — atelier's doctrine-surface scope is
  atelier-specific, so children scope `repo/docs` broadly and ignore their logs).
- **spellscan → blocking** + the **frozen-record `artifact` question RULED: keep
  history verbatim.** The ~36 general-sense `artifact` breaches live in frozen
  record stores; Mike ruled they are NOT retro-spelled. So spellscan is scoped to
  the live doctrine surface with a `.spellscanignore` netting the record stores
  (`docs/sessions/`, `docs/reviews/`, `docs/SESSIONS.md`, `docs/ROADMAP-DONE.md`,
  `*-DONE.md`/`*-ARCHIVE.md`). Re-baseline turned up 2 genuine doctrine-surface
  findings, both resolved honestly: ADR 0007's "Artifact signing/SBOM" is the
  software-supply-chain term-of-art (allow-marked, not mis-corrected to
  "Artefact"), and one general-sense `artifact`→`artefact` fixed in a decision
  record. atelier `ci.yml` dropped `--warn`; child `floor.yml` gained a blocking
  spellscan step + selftest with the same re-baseline note.

Both flips follow datescan's 0707 pattern (atelier blocks now; children adopt +
re-baseline at their next pin bump). Suite 601 green; atelier floor green at head.

## Enforcement propagation — the estate rollout (ADR 0008, done 2026-07-25)

Closed the propagation gap end to end: 13 of 13 children moved off vendored
floor copies onto a called floor. `floorfleet --remote --check` exits 0.

- [x] **Wire the 13 children** — thin caller + tracked `.githooks/pre-commit` +
      `core.hooksPath` + per-repo `.atelier-floor.json`, each repo's signing
      boundary preserved verbatim. Hygiene checks currently failing are declared
      `advisory` so the finding stays reported and visible on the board instead
      of reddening ten repos and drowning the one real credential signal.
- [x] **Repo-specific scoping preserved** — the networking child's leakscan
      tuning (shareable subtree only, IP/MAC rules off, because those shapes are
      *content* there) moved into config verbatim. Its device-config capture
      dirs went to `.secretscanignore` per Mike's ruling: scoping, not secrets.

## Licence gate enabled estate-wide (Mike ruled 2026-07-25)

Publish-readiness, not tidiness — Mike's correction of an earlier deferral.

- [x] **10 repos declare Apache-2.0 and pass the gate.**
- [x] **3 proprietary repos: `disabled`, with the reason recorded.** Measured,
      not assumed: with an unrecognised LICENSE, licenscan stops at "repo licence
      unrecognised" and verifies nothing further — it does **not** fall back to
      flagging a vendored copyleft file, proven against a fixture carrying
      exactly that, and an allow-marker on the LICENSE line does not restore it.
      So the tool gives these repos **no protection at all**, which is a stronger
      reason than "it is noisy".

## Scanner sharp edge — `--staged` + an absolute path covered nothing (done 2026-07-25)

- [x] **`secretscan`/`leakscan` now refuse an absolute positional path in
      `--staged` mode** (exit 2, naming the working form). git lists staged paths
      repo-relative, so an absolute one matched no prefix: the filter emptied the
      staged set and the scan exited 0 — a boundary check that covered nothing,
      indistinguishable from one that found nothing wrong. The silent-success
      class (linkscan L1) these tools already close for a *missing* path, reached
      through a different door.

      Found for real, not theorised: `tools/floor.py`'s first draft rendered
      absolute paths on the staged plane and every boundary check across the
      estate passed green; only the planted-secret commit tests caught it.
      `floor.py` was corrected at the time so the estate was never exposed, but
      the footgun stayed loaded for anyone calling the scanners directly.

      Fixed at the class, not the instance: those two are the *only* scanners
      with a staged mode, so there is no third waiting to be rediscovered.
      Verified live — absolute refused (rc 2), a relative subtree still blocks on
      a real finding (rc 1), whole-diff cover still blocks (rc 1). Pinned in both
      test suites. Commit `6998c2a`.

## Queue run 0702 — ccrepo v3 asks 1+3, cctranscript agent count (moved 2026-07-26)

Orchestrated queue run under Mike's standing brief. Records owned by the
orchestrator; workers committed in isolated worktrees and touched no record file.

### instruments — cctranscript reports agents *finished* beside agents *started*

- [x] **Exact agent count — BUILT 2026-07-26** (`3b38f3d`, merged `99d43d1`).
  The header carries both figures (`10 agents started · 15 finished`), `--json`
  splits them, and **unknown is distinguishable from zero**. Started reads the
  spawn calls (a ceiling — a skipped or stopped spawn still counts); finished
  reads the sibling `subagents/` directory, one log per agent that actually ran.
  **The reason this had been deferred turned out to be false, and that is the
  part worth keeping.** The item said a directory-sourced count would read zero
  under `--from-archive`, since archive mode resolves a single file. It doesn't:
  ccarchive's `captureClass` allows any `.jsonl` at *any depth*, so `subagents/`
  is mirrored — **92 such directories in the live archive**, and the same session
  renders an identical header live and archived. The deferral was reasoned from
  how the *path resolution* works rather than from what the *archive actually
  contains*, and one `ls` would have settled it. Verified by the orchestrator
  independently before merge, not taken on report.
  - **Two standing rules reconciled**, and the resolution generalises: split the
    field **set** from the field **value**. Both chips print on every run, so a
    side-by-side comparison never has a missing column; where the store never
    said, the second reads `finished unknown` rather than dropping out or
    asserting a zero the evidence doesn't support.
  - **Finished can legitimately exceed started**, and the figures are left
    **unclamped** so the reason stays visible: a nested agent logs into the
    *principal's* directory while the principal's own call count can't see it.
    Confirmed on a real session — `spawnDepth {1: 10, 2: 5}` against a header of
    `10 started · 15 finished`. Clamping would have hidden the nesting.
  - What archive mode *does* lose is each log's `.meta.json` sidecar (not a
    `.jsonl`, so outside the capture allowlist), which carries `agentType`,
    `description` and `spawnDepth`. So the count keys on the logs alone, never on
    the directory's entry count, and a finished-*by-type* breakdown is possible
    live but not archived — deliberately left out.

### instruments — ccrepo v3 asks 1 and 3 (`7cf8163`, merged `70bc1ad`)

- [x] **1. Time-bound the price table — a price is effective from A to B.**
  `PRICING` entries may be a list of `{from, to, base}` intervals (ISO dates,
  UTC, both ends inclusive, either end open) as well as a bare number, which
  still means "always" — the compatibility guarantee every existing
  `~/.claude/ccrepo-pricing.json` rests on, now pinned by a test. Each message is
  priced at the rate in force when it was **sent**, so a rate change no longer
  rewrites history. A timestamp inside no interval is **unpriced** — $0 and
  flagged, the same path an unknown model takes, never snapped to the nearest
  interval.
  - **Verified rather than assumed, exactly as the item asked:** no
    `ROLLUP_SCHEMA` bump was needed. `recipeSig` already `stableStringify`s the
    price table, so a flat and a time-bounded table sign differently and the
    ledger rebuilds itself; the event *shape* is unchanged, only its values move,
    which is what the signature covers. The previously-untested link (flat vs
    intervals actually signing differently) is now pinned; the
    mismatch-rebuilds half was already covered, so the new test says so rather
    than duplicating it.
  - **Live proof: ccusage cross-check Δ +$0.00 (+0.00%) over 423 sessions** — the
    oracle agreeing to the cent. Stated with its limit: that proves *no
    regression*, not that the post-2026-08-31 rate is right. Nothing can prove
    that yet, so the boundary is pinned in unit tests instead.
  - `sonnet-5`'s introductory `$2` (through 2026-08-31) and standard `$3` (from
    2026-09-01) are both entered, each correct on its own side of the date. This
    **dissolves the dated ⏳ watch** rather than doing it: the diary note became
    data, and the revert now needs nobody to remember it. Published numbers, not
    fitted ones.
  - **Unplanned, and worth keeping:** the unpriced footnote now names *which*
    gap it is. "Add to the price table" is wrong advice for a model already in
    it — that one needs an interval widened. The reason is derived at tally time
    rather than stored on the event, because a new cached field would have cost a
    `ROLLUP_SCHEMA` bump for something only the footnote reads.
- [x] **3. `-g session`.** A `DIMS` entry as predicted, not a grain change. Keys
  on the **full UUID** (a synthetic ordinal stays a display label, never a key)
  and prints an 8-character prefix in the human table only; `--json`/`--csv`
  carry the whole id, because a truncated id you cannot look up is worse than a
  wide one you can. The filter's private session getter is **gone**, so filtering
  and grouping can no longer disagree about what a session key is. `--top` was
  deliberately not added — it travels with ask 4. Answers "which session hit
  529k?", the one part of that question ccrepo previously couldn't.

## ccarchive encryption at rest — design pass (moved 2026-07-26)

Delivered `d913698`, merged `7701a62`; the design document itself lives at
[`instruments/ccarchive.encryption.design.md`](../instruments/ccarchive.encryption.design.md).
**The build is NOT done** — one decision stays open with Mike and is tracked live
in [`ROADMAP.md`](ROADMAP.md); this is the design pass's completed detail only.

- [x] **ccarchive: encryption at rest, secure-by-default (Mike, 2026-07-25)** —
  **design pass DELIVERED 2026-07-26** (`d913698`, merged `7701a62`) →
  [`instruments/ccarchive.encryption.design.md`](../instruments/ccarchive.encryption.design.md).
  Still not a build; what remains is 🎯 **one decision, Mike's**. **Two stubs
  below were answered by measurement, and both answers moved the question:**
  - ⚠️ **The zero-dep tension does not exist as framed.** AEAD isn't in
    *Python's* stdlib, which governs `tools/` — but ccarchive, ccrepo and
    cctranscript are **Node**, and `node:crypto` ships `aes-256-gcm`,
    `chacha20-poly1305`, X25519, `hkdfSync` and `scryptSync` (verified directly
    at merge, Node 24). Zero-dep and real AEAD are compatible here. The
    `openssl` fallback is **dead on capability, not reputation**: macOS
    LibreSSL 3.3.6 `openssl enc -aes-256-gcm` exits 1 with no usable ciphertext
    (reproduced at merge) — `enc` has no AEAD modes.
  - **The overhead is the process boundary, not key access.** Measured over the
    live archive: `age -d` ≈20.7 ms per file (≈27 s for a full sweep) against
    ≈0.50 ms in-process (≈0.6 s); keychain fetch 40–50 ms, once per process.
    Encryption adds ~2.7% to the gzip already run, and decrypt is ~6% of the
    gunzip already on the read path. **So encrypted-by-default is comfortably
    realistic and the plaintext opt-out really is a backstop, not the expected
    path** — which is what the direction assumed but could not yet show.
  - **The spine of the design:** compress then encrypt to a **public** X25519
    recipient (`<rel>.gz.age`), so the scheduled writer holds no secret, never
    prompts, and *cannot read what it writes*. Decrypt is the interactive path,
    where the keychain is already unlocked. Per-file, not a container — a
    container breaks incremental sync, iCloud eviction and append-only at once.
    Signing **stays**: AEAD protects a file's bytes, the signed manifest
    protects the *inventory* against deletion and rollback. `--verify` stays
    **keyless** via a new `cipherSha256`, so the scheduled integrity check
    doesn't silently become key-requiring.
  - 🎯 **The decision, in plain language: where does the crypto come from?**
    Every option gives a confidential archive; what differs is what you owe.
    **A** shell out to `age` everywhere — simplest, standard format forever, but
    `age` must be installed on every *reading* machine and full reads get ~27 s
    slower. **B** house format in `node:crypto` — nothing to install, fastest,
    but the archive is readable *only* by our code, a real durability risk for
    something meant to outlive its tools. **C** implement the age format both
    directions — no install, fast, standard, but we write the trickiest code in
    the estate twice over. **C′ (counselled)** write with the `age` binary,
    decrypt in-process — `age` needed only on the archiving machine, readers
    stay dependency-free and fast, format stays standard, and **we only author
    the half where a bug fails loudly**; an encrypt bug can mint weak files you
    discover years later. `age` is already installed on this machine. Counsel,
    not a decision.
  - **Named honestly rather than buried:** per-file encryption leaves session
    UUIDs, dash-mangled repo paths, file sizes and the whole `manifest.json` in
    the clear. ADP covers that residual on the iCloud leg; a NAS leg would not.
  - **Key loss is total data loss**, said plainly — an archive you cannot
    decrypt is not an archive.
  - Review **WARRANTED when it moves from design to build** — unchanged. The
    design pass authored no doctrine, so nothing is queued yet.
  Original brief kept below for the reasoning. **Direction (Mike):** ccarchive stores the archive
  **encrypted by default** (secure-by-default → confidential at rest), with an
  **explicit opt-out param** to store plaintext if the overheads bite (a loud
  opt-out, never a silent default); and **ccrepo + cctranscript gain live-decrypt**
  the same way they already live-decompress. **This raises the bar the 2026-07-23
  archive decision set:** that ruled the encryption concern "answered" by the
  iCloud **ADP E2E** layer — but ADP only protects the *iCloud copy*; tool-native
  encryption makes the bytes confidential *everywhere* (local disk, any copy, in
  transit, the deferred NAS leg). Complementary to ADP, not redundant.
  **Open design questions (stub — do not pre-decide):**
  - **Key management is the crux, not the crypto.** Where the key lives + how the
    consumers get it at read time. Keys → the person-level credential home
    (keychain / an age identity), **never atelier** (SECRETS right-plane).
  - **The overhead is key-*access*, not decrypt CPU** (symmetric decrypt is
    microseconds; the cost is unlocking the key per op). Lever: session-cached
    unlock / already-unlocked login keychain — then live-decrypt reuses the exact
    live-decompress read seam. So encrypted-default is realistic; the opt-out is a
    backstop, not the expected path.
  - 🔗 **Solve-once reuse:** the person-context portability design already wants an
    **age capsule with per-machine keys** for crown-jewels (rulings D1–D5). Same
    building block — "encrypt-at-rest, keys in the person-home". Solve the key
    infrastructure ONCE and reuse for both (a live instance of the *solve once,
    reuse the building block* capture above).
  - ⚠️ **Zero-dep tension (the one likely Mike-decision at the design pass):**
    AEAD encryption isn't in Python stdlib — it needs a crypto dep (`age` is the
    clean choice, already contemplated for the capsule) or shelling to `openssl`
    (footguns — not AEAD by default). This is the same tool-install-floor tension
    that *deferred* release-artifact signing/SBOM; weigh secure-by-default against
    the zero-dep house-tool pattern.
  - **Orthogonal to the existing manifest signing** (integrity ≠ confidentiality):
    keep both — sign for tamper-evidence, encrypt for confidentiality.
  Review WARRANTED when it moves from design to build (touches SECRETS.md +
  the instruments crypto surface).

### floorfleet reads the tracked shim — the hook question, half-answered estate-wide (2026-07-26)

- [x] **`floorfleet --remote` now checks the tracked shim.** Hooks used to be
  untracked, so the remote plane could say nothing about them. `.githooks/pre-commit`
  is a repo file now, so a new `shim:` column reports whether it exists and routes
  through the registry (`current`) rather than naming scanners itself (`legacy`) —
  and because it is a fact about the **repo**, `--remote` carries it as a genuine
  estate-wide claim. Proven live: **all 13 children `shim:current` on the remote
  plane**, which nothing could previously assert.
  - **The two facts are deliberately kept apart, in separate columns and separate
    footers.** `shim:` travels with a clone; `hook:` (whether `core.hooksPath`
    actually points at it) never does. Blurring them would let a reader over-claim
    on the remote plane, which is the exact failure the column exists to avoid. A
    test pins that both footers appear and stay distinct.
  - **The residual shrank rather than closed**, and the module docstring was
    rewritten to say so: it read "`--remote` cannot help: hooks are not in the
    repo", which stopped being true when the shim became tracked. It is now
    "whether *this clone* points at the shim is unknowable remotely" — real, but
    much smaller. CI stays the backstop for exactly that last step.
  - 21 floorfleet tests (was 16); `--json` carries `shim` via `asdict` unchanged.
    Original item text: **`floorfleet --remote` could check the tracked hook, and currently doesn't.** Hooks used to be untracked, so the remote plane could say nothing about them — but `.githooks/pre-commit` is now *in the repo*. The remote plane could verify the tracked shim exists and is the current one, leaving only `core.hooksPath` (genuinely per-clone) unknowable. A small change that moves a chunk of the hook question from "machine-local only" to "answerable estate-wide".

### ccrepo v3 ask 2 — filter by context size (moved 2026-07-26)

- [x] **`--context MIN-MAX`, open-ended either end, `k`/`m` suffixes** (`791bea6`). One selector flag rather than a `--context-min`/`--context-max` pair, matching how the other filters read as *what they select*.
  - **The grain is the point, and it is stated in `--help` and the man page:** context is a **per-session peak**, so this selects *sessions* whose peak falls in the band and admits all their messages. The message-grain reading was rejected as near-meaningless — every session ramps up through every band beneath its peak, so a message-level filter would match almost every session at almost every band.
  - Pairs with `-g session`: `-g session --context 500k-` is "which sessions blew past 500k" — the exact question that needed an ad-hoc script on 2026-07-26, now answerable by the tool.
  - A malformed range and an inverted one (lower bound above upper) both exit **2** with a message naming the accepted forms, never a silent match-everything.
  - Verified live by the orchestrator before merge rather than taken on report.

  Original spec: - [x] **2. Filter by context size — DONE 2026-07-26** (`791bea6`, merged). `--context 100k-500k` / `400k-` / `-100k`, `k`/`m` suffixes, selecting **sessions** by peak (not messages) as the ask specified. A malformed or inverted range exits 2 rather than silently matching everything — verified live, along with `-g session --context 400k-` returning only sessions that clear the band. Detail → [`ROADMAP-DONE.md`](ROADMAP-DONE.md) at next harvest. Original spec kept for the grain reasoning: `--context 100k-500k`, open-ended either end (`--context 400k-`, `--context -100k`), `k`/`m` suffixes — one selector flag rather than a `--context-min`/`--context-max` pair, matching how the other filters read as *what they select*. **The grain needs stating in `--help`, because it is the first filter whose unit isn't the message:** context is a **per-session peak** (design §4), so this selects *sessions* whose peak falls in the band and admits all their messages. The message-grain reading is available but near-meaningless — every session ramps up through every band beneath its peak, so a message-level filter matches almost every session at almost every band. Pairs directly with (3): `-g session --context 500k-` is "which sessions blew past 500k", the exact question that needed an ad-hoc script on 2026-07-26.

### ccrepo v3 asks 4 + 5 — multi-key sort, `--top`, sectioned help (moved 2026-07-26)

- [x] **4. Multi-key sort within a level, plus `--top`** (`ee36a91`). Built on
  Mike's **option A**: the comma stays positional per `-g` level, and multi-key
  chains additively on **`+`** (`--sort 'cost+name, time'`). The glyph was picked
  against the punctuation already in the flag — `,` means "next level" and `:`
  means direction, so `+` was the one gap. `--sort cost` still broadcasts to
  every level (a one-element chain), and an unknown key inside a chain still
  exits 2. Nothing written under v2 changed meaning.
  - **`--top <n>` truncates per level, not leaves-only** — `-g repo,model --top 5`
    keeps the top five repos *and* the top five models within each, shared by
    `treeRows`/`leafRows`/`--json`/`--csv` through one helper so every output
    shape truncates identically.
  - **TOTAL is preserved, and this was proven rather than argued.** `groupTree`
    computes every node's aggregate over the *entire* event set before any sort
    or truncation, so `--top` only slices which computed rows get listed. A
    first live check appeared to differ by two messages — that was the verifying
    session appending to its own log between runs, not truncation. Re-run over a
    **frozen** date range, the TOTAL row is byte-identical with and without
    `--top`. A footnote on the output says the total is untruncated.
- [x] **5. Sectioned `--help`** (`ece20b3`). SELECT · SHAPE · OUTPUT · SOURCE ·
  PRICING · META, with the trailing prose paragraph kept (it is the part that
  says what the numbers *are*). ccarchive and cctranscript deliberately
  untouched — whether they follow is a separate call, and three tools sectioned
  by drift is not a convention.
  - **The `--help` line guard moved 40 → 47, and the derivation is structural,
    not fitted:** one `OPTIONS` line became six section headers (+5) and two
    flags were added (+2). Verified at merge that **no blank-line padding** was
    introduced between sections, so each term is a real change rather than
    arithmetic reverse-engineered from the measurement — the failure the item
    was explicitly warned against. The derivation is commented in both the
    script and the test. Worth knowing: the budget now has **zero headroom**, so
    the next flag added forces the question again — deliberately, since that is
    what a budget is for.
  - ⚠️ **One judgement a future session may revisit:** the sections carry no
    blank line between them, which is what kept the budget honest but reads
    densely. Spacing would cost six lines and another grounded re-derivation.

  Original spec: - [~] **4. Multi-column sort — half of this exists, and the syntax collided.** *(claimed 2026-07-26-0702, wt: ccrepo-v3 · at: NOT started — `--top` and the within-level multi-key separator are both still open)* **Decided by Mike, 2026-07-26: option A** — the comma stays positional per group level, multi-key is additive on a second separator. Nothing already written stops working, and B (the only unwalkable-back option) is off the table. Two consequences worth stating rather than re-deriving: **C stops being a separate choice** — under A the flat outputs get the same within-level syntax for free, so there's no tree-vs-flat split to decide; and the separator glyph (`+` as sketched) is now an implementation detail, picked at build time against the other punctuation already in the flag. The collision that made this a decision, kept for the reasoning: `--sort` already takes `:asc`/`:desc`, so the direction half is built. But the existing flag is **positional per group level**, aligned to `-g`: `--sort cost,name` today means *"level 1 by cost, level 2 by name"*, not *"cost, then name as tiebreaker"* — which is what `--sort columnA,columnB` reads as. Same flag, same punctuation, two meanings. Worth naming why: in a **tree**, sort is inherently per-level — rows at different depths can't interleave — so "sort the whole table by two columns" only has a literal meaning under `--flat`/`--json`/`--csv`. Options: **A** keep the comma positional, add within-level multi-key on a second separator (`--sort 'cost+name, time'`); **B** re-read the comma as multi-key and move per-level elsewhere — breaks the documented v2 spec and every existing invocation; **C** multi-key only in the flat outputs, tree stays positional. A was recommended and chosen — purely additive, and `--sort cost` still broadcasts to every level. - [~] **5. Section the CLI surface.** *(claimed 2026-07-26-0702, wt: ccrepo-v3 · at: NOT started; note the `--help` ≤40-line guard will need a GROUNDED decision, never a figure fitted to whatever the sectioned output measures)* `--help` is one flat 25-line `OPTIONS` block and this batch adds at least three more flags to it. **Tiki is the named reference and the transferable part is the grouping, not the machinery** — tiki gets its panels from Typer's `rich_help_panel` (*Daily* · *Inventory & read-model* · *Adopt & recover* · *Diagnose & locate* · *Self-healing* · *Security* · *Meta*) plus an epilog that states exit codes; ccrepo's help is a hand-written string in Node, so it copies the *named sections*, not Typer. Proposed: **SELECT** (all filters, including `--since`/`--until`/`--context`) · **SHAPE** (`-g`, `--sort`, `--top`, `--flat`) · **OUTPUT** (`--json`, `--csv`, `--fx`, `--rate`) · **SOURCE** (`--from-archive`, `--dest`, `--materialise`, `--no-rollup`) · **PRICING** (`--no-billing`, `--no-reconcile`) · **META** (`-z`, `-h`). The trailing prose paragraph stays — it's the part that says what the numbers *are*. `--help` remains the summary and `man ccrepo` the long form (2026-07-21 convention). Whether ccarchive and cctranscript follow is a **separate** call: a convention is something repeated deliberately, and three tools sectioned by drift is not that.

### linkscan names the fix when the path is computable (moved 2026-07-26)

- [x] **`linkscan` prints the replacement path** where it is computable
  (`b89a306`) — `↳ did you mean: ../../tools/x.py` beneath the finding. Turns a
  17-item chore into 17 obvious edits.
  - **Two tiers, both requiring a *unique* answer**, because a confident wrong
    suggestion costs more than none: (1) the path resolves from the **repository
    root** — the commonest break by a wide margin, a root-relative path written
    inside a file two levels down; (2) exactly **one** file in the tree carries
    that basename, the moved-or-renamed case. Two candidates and it stays
    silent. Dot-directories are skipped: a match under `.github` is not
    something a reader can follow.
  - **Advisory only, and pinned as such** — a suggestion never changes a verdict
    or an exit code, and nothing is rewritten. A test asserts the suggested path
    *actually resolves*, so the tool cannot confidently mis-advise.
  - 668 python tests (was 661).

  Original item: **`linkscan` could name the fix for its commonest class.** *(claimed 2026-07-26-0845, wt: none — inline on main)* One repo carried 17 broken links of a single shape: a repo-root-relative path written inside a `docs/` file two levels down, so it resolves to `docs/<dir>/<path>` and 404s. The correct target is computable from the finding. Idea: print the suggested relative path alongside the error. Turns a 17-item chore into 17 obvious edits, and this shape will recur wherever records cite source files.

## Policy-as-code programme — A5a: the parent was not running its own floor (done 2026-07-27)

- [x] **`core.hooksPath` was unset in the atelier clone.** Every child had it
  set; the parent did not. So atelier committed through the vendored
  2026-07-12 three-scanner hook while the registry it authors served nine
  scanners to all 13 children. The repo that writes the policy was the only one
  not bound by it at commit time.
  - **Found by measurement, not by reading.** It was first reported inside a
    review pass that Mike later rejected on tier grounds, so the finding was
    correctly treated as unverified and re-derived from scratch on 2026-07-27
    (`git config core.hooksPath` → unset on atelier, `.githooks` on all 13
    children). A finding from a withdrawn pass is a lead, never a fact.
  - **Fixed by Mike** (`git config --local core.hooksPath .githooks`),
    deliberately left to him because it changes a machine, not the repo.
    Proven after, not asserted: the hook plane now reports **9/9 enforced and
    clean**.
  - 🔎 **The half that is still open, and is the more important half.**
    `floorfleet` discovery walks *children*, so atelier is structurally
    invisible to the board whose whole purpose is proving conformance. A
    machine-local setting is not a mechanism — nothing would have caught this,
    and nothing would catch it recurring on a fresh clone or a new machine.
    Carried as **A5b** on the live roadmap. Same defect one level up, which is
    the shape ADR 0008 exists to end.

## Policy-as-code programme — Track A: the fail-opens closed (done 2026-07-27)

Landed in worktree `track-a-fail-opens`, four commits, session record
[`2026-07-27-2301-track-a-fail-opens`](sessions/2026-07-27-2301-track-a-fail-opens.md).
Findings were counsel from the 2026-07-26 rule-4 Fable passes; the rulings were
Mike's (REVIEW rule 3). Tests 694 → 720, green in **both** environments (with a
machine term list, and with none). Every fix was driven live against the probe
that proved the defect, not asserted from the diff.

**The rulings, and the two measurements that decided them.** Both 🎯 items were
walked through in plain language first, and in both cases the roadmap's own
statement of the cost was wrong in the direction that made the strong fix
affordable.

- **A1/EP1** — the roadmap warned of "an immediate blast radius". Measured: of
  19 repos, **2** declare `scope`/`flags` and **all four declared paths
  resolve**; of 14 with a floor config, **0** lack their records tree. The
  structural reason it is safe: every no-advisory-form scanner defaults to the
  repo **root**, which always resolves, so the skip branch reaches a boundary
  check only through an *explicit* declaration — and the three docs-scoped
  scanners that need the skip are all advisory-capable. The cases do not
  overlap. **Zero children red.** Ruled **(a)+(c)**; (b), the stated-reason
  requirement, deferred to ride with C1's schema change rather than be decided
  twice.
- **A2/EP3** — the roadmap said requiring terms "fails closed on … every CI
  runner by design". Not for a hook-plane change: both workflows invoke
  `--plane ci` and the hook template is never invoked by CI; no test ran a real
  hook-plane `leakscan`. Ruled **(c)** — Mike asked why (a) was recommended
  over (c), was told that (a) makes the degraded-render path unreachable on the
  hook plane, and ruled (c) anyway for **measurement over inference**.

- [x] **A1 — a `scope` path resolving to nothing silently disabled the check.**
  Now a hard config error for any scanner with no advisory form; the skip
  survives for the softenable docs-scoped checks, which is the case it was
  written for. **Extended past the finding as written:** the review described a
  scope resolving to *nothing*, but the class is *any* declared path that does
  not resolve — one of two paths going missing halves a boundary check's cover
  the same way, so partial drift blocks too. `floorfleet` now reads `scope`,
  `flags` and a non-default `docs` on the board and in `--json`.
- [x] **A2 — the hook plane's `leakscan` cover was asserted, never enforced.**
  The hook template runs `leakscan --require-terms`. A `Scanner` may name the
  flag giving it full cover, so a plane omitting it renders **🟡 partial**
  rather than ✅ — CI's `leakscan` is structural-only permanently and now says
  so every run. `floorfleet` reports whether **this machine** carries a term
  list: a machine fact, not a per-child one, so it goes on the board once and
  asks `leakscan`'s own resolver rather than re-implementing the lookup.
- [x] **A3 — `floor.py` asserted cover it lacked.** Its docstring claimed
  `flags` was *"read out estate-wide by floorfleet"* when floorfleet read
  neither key. Settled by A1 **at the mechanism** rather than by softening the
  sentence, and pinned by tests so it stays checkable instead of becoming true
  once and drifting back.
- [x] **A4 — LS1–LS5, the repo-local seam's edges.** LS1 Actions log-command
  injection through a child-authored `why`, encoded at the point of
  interpolation. LS2 an executable non-Python script with no shebang crashed
  the floor with a traceback — now a clean BLOCK with the summary preserved.
  LS3 a committed symlink executed out-of-tree code; realpath containment now
  enforced, and the old test exercised lexical strings only, so it overstated
  the guard. LS4 unknown keys in a local declaration read past in silence — not
  cosmetic, since a `planes` typo runs a hook-only check on CI. LS5 a disabled
  local check lost its `local` marking.
- [x] **A5b — `floorfleet` has a parent row.** Classified on whether the
  parent's own workflows invoke `floor.py --plane ci`, with `floor.yml`
  excluded from that search: it runs the floor over the *caller's* tree, never
  the parent's, so reading it as proof would be the self-exemption A5a was.
  Named from the repo rather than the directory, since those differ in a
  worktree and this repo's doctrine says to take one for write-heavy work.

**Two things the work surfaced that were not in the brief**, both fixed here:

- **A contract test asserted the opposite of the ruling.** The registry test
  banned `--require-terms` on **both** planes, reading the two planes as one —
  right for CI, wrong for the hook, where it forbade the flag on the plane the
  design says carries the full cover. Narrowed to CI with its complement added,
  not deleted.
- **Three pre-commit tests were passing *because* the hook was degraded**, and
  were env-gated in the misleading direction: green on a laptop holding
  `~/.claude/leakscan-terms.txt`, red on every CI runner. They now pin a term
  list inside the fixture. Every suite run was done twice, and the LS1 test
  sets `GITHUB_ACTIONS` explicitly rather than inheriting it, because
  annotation mode is env-gated and a test that merely runs the floor would pass
  by never entering the branch it means to exercise.

**Estate consequence, deliberate.** A new machine or fresh clone now blocks on
its first commit until `~/.claude/leakscan-terms.txt` exists. Documented as a
once-per-machine step in the child CONTRIBUTING template, which said only "two
lines" before, and worded so the block reads as intended rather than as broken
tooling.

### The application's own cold pass — TA1–TA9 (done 2026-07-28)

- [x] **REVIEWED 2026-07-28** (rule-4 Fable cold pass): PASS-WITH-FINDINGS
  1M/4m/4n —
  [verdict](reviews/2026-07-28-0123-track-a-application-cold.md). Ruled by Mike
  the same day (TA1 → (a); TA2–TA9 → fix all eight) and applied in worktree
  `ta-findings-application`, session record
  [`2026-07-28-0214-ta-findings-application`](sessions/2026-07-28-0214-ta-findings-application.md).
  All nine applied, none deferred. Tests 720 → 733 Python (+207 node), green in
  both environments.

**The MAJOR, and the third measurement that decided a ruling.** TA1: the A1
scope guard tested path *existence*, not membership, so a declared scope that
resolved somewhere else — `/etc`, `..`, or an in-tree symlink pointing out —
passed the guard, rendered on the hook plane to a prefix matching nothing in
the staged diff, and exited 0. A boundary check vacated under a green tick.
The same commit series had closed exactly this lexical-vs-resolved gap for
`local.run` (LS3) and left fleet `scope` with neither half, so the asymmetry
sat inside one diff — and the guard's own comment claimed the class was shut.

Measured before costing, and the pattern held a third time: 14 configs across
the estate, 2 declaring `scope`, 4 declared paths, **every one relative and
in-tree**. Zero migrations, so the thorough fix (validate at parse, both
spellings, plus resolved containment for the symlink member) cost no more than
the narrow one. The cheap-vs-thorough trade this programme keeps expecting has
now failed to materialise four times.

**Applied beyond the letter of the ruling, named as such.** `local.*.scope`
feeds the same `subtrees`/`_render` path as fleet `scope` and carried the
identical hazard. The ruling named only fleet `scope`, but guarding one
spelling of "where does this check look" while leaving its siblings open *is*
the finding, so the rule was applied to both.

**Fixed at the claim rather than the mechanism, also named.** TA4: the 🟡
partial-cover note was read off argv and asserted a cover *level*, which the
scanner's own output could contradict on a machine holding a term list. The
floor cannot observe real cover without capturing child output, and streaming
scanner prose live is worth more than closing a gap that errs toward claiming
*less*. The note now states the invocation, which is true in both
environments; the 🟡 stays because a real runner holds no list.

**The rest.** TA2 rode free (rejected at parse, so an absolute scope never
reaches the scanner that used to crash on it). TA3 gives partial scope drift on
a *softenable* check a 🟡 and a "N of M scope paths missing" note — it must not
block, but shrunken cover reported as full is what this whole track is about.
TA5: `PARENT_RUN_RE` matched inside comments, so a parent that commented out
its floor step read `wired` on the board built to catch exactly that; comments
are now stripped by a quote-aware lexer, with both over-corrections pinned.
TA6 moved a module-import side effect into `setUpModule`. TA7: the board could
not discover children when run from a worktree — the mode this repo's doctrine
prescribes for write-heavy work — because the default search root was the
worktree's parent; it now resolves the main checkout, the same way the parent
row's label already did. TA8 restored EP2's MAJOR grade in the intent record.
TA9 gave AWA2 a grammar for multi-commit landings: the landing commit is the
one that *completes* the series.

## Policy-as-code programme — Track C: C1, the advisory grows an end date (done 2026-07-28)

- [x] **C1 — `advisory` takes a reason and an expiry** (phase 1). Ruled by Mike
  2026-07-28 (both fields hard-required · transition window rather than a flag
  day · a passed date reds the board and blocks nothing), applied the same day
  in `worktree-c1-advisory-schema`, session record
  [`2026-07-28-0244-c1-advisory-schema`](sessions/2026-07-28-0244-c1-advisory-schema.md).
  **A1 option (b)** was deferred out of the A1 ruling into C1 and ruled with
  it. 747 tests green. *Phase 1 only — the 17 declarations are not migrated and
  the legacy spelling is not yet removed; both live at C1b on the hot path.*

**What changed.** `advisory` was a bare list of scanner names carrying neither a
reason nor a review date, so nothing distinguished "three days into adopting
this check" from "softened in March and forgotten". `disabled` — the harder and
more visible opt-out — had demanded a stated reason all along; the softer one
demanded nothing, which is backwards. It is now `{name: {why, review-by}}` with
both required and the date validated as a real ISO 8601 date at parse, which is
what lets the ageing comparison downstream be a plain string compare.

**Expiry is reporting pressure, never a block.** A passed `review-by` renders 🔴
on the floor and on the fleet board — with the number of days it has been
standing, because "expired" reads identically on day one and day two hundred —
and exits 0. A commit failing because of a date somebody set months earlier is
how a forcing function turns into a `--no-verify` habit.

**The transition was the real design decision.** Children fetch `atelier@main`
at CI run time, so a hard error on the old spelling would have broken all ten
children's CI the afternoon it landed. The bare list still parses, marks itself
`legacy`, and renders 🟡 on every run and every board row. That debt is tracked
at C1b, not left implicit: a transition spelling still parsing in a month would
be C1's own decay one level up, which would be a fine joke and a real defect.

**A1(b).** Narrowing a check that may never be softened now states why — `scope`
gains a `{paths, why}` form, with the `why` required only for the five
boundary/integrity scanners, since narrowing a prose check is an ordinary
layout fact. No `review-by`: a narrowed scope is a permanent structural fact
about a repo, not dated debt waiting to be cleared. Estate reach: one
declaration.

**The measurement, and a pattern worth naming.** The roadmap said 11 advisory
declarations across 8 children; the sweep found **17 across 10**. That is the
fourth blast-radius figure this programme has stated wrongly — and the first
that *understated* the work, where the previous three all made a strong fix look
more expensive than it was. The lesson is not "the roadmap is optimistic", it is
that its numbers are not an input a ruling can rest on, in either direction, and
that re-measuring costs minutes.

## Boundary findings — the tracked data export (done 2026-07-28)

- [x] **High-entropy hits in a tracked data export** — ruled and executed
      2026-07-28. A business-system export committed to a repo, carrying
      token-shaped values. Three things generalise, and none of them were
      visible before the triage actually ran:
      **(a) Read what the values ARE, not just that they are high-entropy.**
      Here every hit sat on one field, and that field held customer-facing
      capability links — URLs whose unguessability *is* the access control.
      That is neither an API key nor a false positive, and the right action
      follows from the semantics, not the entropy score.
      **(b) A line-level allow-marker is not always available.** In a `.json`
      file it is impossible: JSON has no comment syntax, so the marker either
      breaks the file or is absorbed into a data value and falsifies it. Tested,
      not assumed. Where that holds, the accept branch collapses onto the
      file-scoped ignore — so the four branches are not always four.
      **(c) The scanner going green can be the failure mode.** Removing the file
      from the working tree clears the finding while changing the exposure not
      at all; the data stays one `git show` away. Deleting is still not one of
      the options — but *untracking* is the shape the mistake actually takes,
      and it looks like a fix on the board.

### The Track A cycle's terminal pass — TAA1–TAA4 (done 2026-07-28)

- [x] **REVIEWED 2026-07-28** (rule-4 Fable cold pass, taken from the queue
  by a Mike-spawned "do any review work" session — author of nothing in the
  chain): **PASS-WITH-FINDINGS 0 MAJOR / 1 minor / 3 notes** —
  [verdict](reviews/2026-07-28-1136-ta-application-cold.md). **The Track A
  review cycle CLOSED** on this pass (no-MAJOR terminal rule); the residue
  (TAA1–TAA3) went to the live backlog as a 🎯 ruling item for Mike.

Every live claim in the TA application re-ran true: both TA1 red legs
(`/etc` scope and the escaping symlink — rc 0 at `3fb6437`, rc 1 at HEAD),
TA5's wired→absent flip on a commented-out workflow line, TA6's import
hygiene, TA7's board run from a real worktree (parent + 13 children), the
`321bbd3` blast radius exact to the row (14 configs / 2 scoping / 4 unique
paths / 0 failing), 733 green at `d80f9d8`, and 759 + 207 green at HEAD in
BOTH environments (machine term list present and absent). Push telemetry
confirmed the TA9 grammar was met by its own series: the pointer left in
the same push as the completing commits.

The one substantive finding (TAA1) is an honesty lapse in a comment, not in
behaviour: the scope guard's class-members comment entered the series as an
overclaim ("the rest of that class"), was corrected to an underclaim
mid-series, and landed still claiming "(open)" two members that `321bbd3`
had shut — with the out-of-delta C1 commit later appending a correcting
tail while leaving the "(open)" labels. Same comment, three states, none
true at its landing.

### C1 phase 1's cold pass — C1F1–C1F3 (done 2026-07-28)

- [x] **REVIEWED 2026-07-28** (rule-4 Fable cold pass, same taker session as
  the Track A terminal pass — author of nothing in either chain):
  **PASS-WITH-FINDINGS 0 MAJOR / 1 minor / 2 notes** —
  [verdict](reviews/2026-07-28-1204-c1-advisory-cold.md). **The C1 phase-1
  review cycle CLOSED** (no-MAJOR terminal rule); residue C1F1–C1F3 queued
  🎯 for Mike beside C1b.

Every claim re-ran true before the intent record was opened: eight parse
edges refused by message with rc 1 and zero tracebacks; the three render
states live (expired 🔴 with rc 0 — red, never blocking, as ruled); all
four A1(b) edges as ruled; the estate measurement exact (17 advisory
declarations across 10 children, and exactly 17 🟡 unmigrated rows on the
live board); 747 green at `549930b`; the pointer pushed with its landing
commit. The one substantive finding (C1F1) is a render displacement: the
new advisory `why` occupies the note slot the TA3 drift warning uses, so a
softened check with a half-resolving scope shows its reason but not its
shrink outside `--json`.

### The estate-root widening's cold pass — ER1–ER4 (done 2026-07-28)

- [x] **REVIEWED 2026-07-28** (rule-4 Fable cold pass, third item taken by
  the same non-author taker session): **PASS-WITH-FINDINGS 0 MAJOR /
  1 minor / 3 notes** —
  [verdict](reviews/2026-07-28-1216-estate-root-widening-cold.md). **Cycle
  CLOSED** (no-MAJOR terminal rule); residue ER1–ER4 queued 🎯 for Mike.

The paragraph's evidence re-ran clean: the 63-across-19 sweep reproduces
exactly at word boundaries (a naive substring sweep returns 471 — matching
inside ordinary words — which vindicates the *shape* of C5's cry-wolf
concern while confirming the measured zero-ordinary-word claim), the
forward-only rule has held since landing with zero new mentions, and the
text withholds the name it says it withholds. The minor (ER1) is the
widening's own lesson one transition further: the rule is silent at the
private→public flip, the moment a scrub still buys everything back.

### The secretscan fragment-match fix's cold pass — SF1–SF4 (done 2026-07-28)

- [x] **REVIEWED 2026-07-28** (rule-4 Fable cold pass, fourth item for the
  same non-author taker session; the security floor's requested tier):
  **PASS-WITH-FINDINGS 0 MAJOR / 1 minor / 3 notes** —
  [verdict](reviews/2026-07-28-1220-secretscan-fragment-cold.md). **Cycle
  CLOSED**; residue SF1–SF4 queued 🎯 for Mike, SF1+SF2 as one
  low-charset-diversity family.

All four red legs reproduced on synthetic fixtures against the pre-fix
scanner; the three introduced-FP fixes hold with no new false positives
from the boundary change; the estate re-scan matches the claim (the one
moved figure is the ruled untrack of the data export); every committed
test value verified synthetic. The minor (SF1) is live-proven: the
kebab-slug exemption un-flags hyphenated diceware-style passphrases the
old scanner caught — the snake-case twin was already exempt, so the fix
completed a pre-existing hole's spelling rather than opening a class, but
the cost went unnamed. The pass also corrected two figures at reconcile:
the lowercase-hex gap is half its stated size (letter-leading only), and
the "entropy net catches ≥32 chars" aside holds only for mixed-class
values.

## Policy-as-code programme — Track B: the board learned to say "and passing" (done 2026-07-28)

### B2 + B3 — conformance and compliance, held apart (done 2026-07-28)

- [x] **`floorfleet` proves a repo CALLS the floor, never that its floor is
  GREEN.** (B2.) `--status` now reads each repo's latest floor run and reports
  it as a separate claim from wiring — `passing`, `failing`, `behind`,
  `actions-off`, `no-runs`, `unregistered`, `running`, `no-result`, `unknown`.
  Only `passing` is green; `unknown` is a red, so a board that could not read
  an answer never renders one.
- [x] **A blind spot worth closing cheaply** — a repo with Actions disabled
  reading as perfectly wired while running nothing. (B3, ranked-residual item
  4.) Closed in the same change, because it is the same defect: wiring is a
  fact about a FILE, and a file cannot tell you the runner was ever switched
  on, or that it passed.

**The first live run is the whole argument for the item.** `--remote --status`
against the estate: all 13 children reported `wired ✅` — and **5 of 14 repos
had been RED on their default branch since the 2026-07-25 rollout**, three days
unnoticed, every one of them showing as fully conformant on the old board. The
roadmap entry predicted this exactly ("the board can read 'all 13 ✓' while
several repos are failing every run"); it was not a hypothetical.

**The proposed shape for B3 was costlier than it needed to be, and that is
worth keeping.** The entry suggested one `actions/permissions` call per child.
That endpoint requires GitHub's **Administration** permission — the
repo-*settings* permission — so adopting it as a requirement would have widened
the scheduled check's token across the entire private estate to learn one
boolean. Instead the switch is read authoritatively **when the token happens to
carry that permission** and inferred from run history when it does not: a floor
that has never run once is the same practical absence whatever caused it. The
board then **declares which authority answered**, because a board that cannot
say how well it knows something is the same failure as one that reports green
on nothing. Permission requirements were read from GitHub's published
fine-grained-PAT reference rather than assumed.

**Design notes worth carrying.** `classify_run` is pure and the selftest drives
every branch offline, mirroring the split `classify` already used — the I/O
sits in `read_run`. `--check` without `--status` keeps its exact previous
meaning (conformance alone), so nothing standing on the old exit code moved;
`--status` widens it to require green. `behind` was added beyond the item's
ask: a SUCCESS conclusion against a commit that is no longer the branch head
says PASSING about code that was never scanned, which is the same
confidently-wrong family one step subtler. The parent row gained a `workflow`
field because atelier runs the floor from its own `ci.yml` rather than the
caller filename its children use, so its run history was otherwise
unaddressable. 12 new tests; suite 759 → 771, all green.

### B1 — the conformance check runs on a schedule (done 2026-07-28)

- [x] **B — scheduled workflow in a PRIVATE repo.** Mike ruled B on 2026-07-28
  from four costed options; built and pushed the same day. The estate-root repo
  hosts a daily workflow that checks out atelier, enumerates the account and
  asserts the full claim — every repo calls the floor **and** its floor is
  green. atelier is public, so a token spanning the private estate belongs in
  the private counterpart's secret store rather than the shop window; GitHub's
  schedule runs it whether or not a machine is switched on, which local cron
  (option C) cannot promise.

**The four options as they stood, preserved verbatim** — the decision is only
legible beside what it was chosen over:

- [x] **A — PAT in atelier's CI.** True continuous enforcement, catches drift
      within a day, no human in the loop. Cost: a read token spanning the whole
      private estate, living in the **public** repo's secret store. GitHub does
      withhold secrets from fork PRs, so it is not trivially stealable, but it is
      the largest concentration of the four. Needs rotation discipline.
      *(Not chosen 2026-07-28: B is strictly better for the same outcome.)*
- [x] **B — scheduled workflow in a PRIVATE repo.** Identical automation and
      identical benefit to A, with the token in a private secret store instead of
      the public one. Runs on GitHub's schedule regardless of whether any machine
      is on. Open question: which repo hosts it — the doctrine references a
      "private estate-root repo" as atelier's counterpart, but which repo that
      actually is has never been written down. **Answer that first; it is
      reusable well beyond this item.** *(CHOSEN 2026-07-28. The open question
      was answered 2026-07-28 and recorded in the estate root's own records; it
      stays unnamed in this public tree by the PROPAGATION.md rule.)*
- [x] **C — scheduled local run (cron/launchd).** `floorfleet --remote --check`,
      shouting on failure. **No new credential** — uses the existing `gh` login.
      Failure mode: a machine that is off does not check, so drift can sit for
      as long as the laptop does. *(Not chosen 2026-07-28: superseded by B,
      which does not stop checking when a laptop is off.)*
- [x] **D — add it to the session-close ritual.** Cheapest, zero infrastructure,
      and *rejected on this session's own evidence*: it is a discipline, not a
      mechanism, and the entire finding behind ADR 0008 is that a discipline
      logged as an intention decays silently. Recorded so the option is visibly
      considered and dismissed, not quietly skipped. *(Rejected 2026-07-25.)*

**The item's costing was wrong, and the reason generalises.** B1 read "the work
is small: the schedule, `--check` wiring, and a failure message", on the premise
that `floorfleet --remote` was remote end-to-end. It was not. `--remote` read
each repo's CONTENT from GitHub and still DISCOVERED children by walking the
directories beside the atelier checkout — so on a GitHub runner it would have
found no children and exited 2. Fail-safe, but not a check. Stated at the right
altitude: **the estate this board could see was the estate that happened to be
cloned on one laptop.** That is the same class as every other finding in this
programme, one level further out than any of them.

`--from-github <owner>` was therefore the real work. It also closes the blind
spot the tool documented about itself — a repo that exists and was never cloned
here was not reported as a red, it was not reported at all — and it lists repos
in the account carrying no atelier pin as *unenrolled*, so a repo that never
adopted the floor is a visible choice rather than silence. Swept on landing: 6
unenrolled, of which 3 are public (exactly the three already named in the
roadmap, so that figure was right) and 3 private and untouched since 2016.

**Two bugs found in the building, both the same family as the programme's
organising finding — a check that runs and covers nothing:**

- `users/{owner}/repos` returns PUBLIC repos only: 4 of 20 here. A tool whose
  whole claim is enumeration would have enumerated a quarter of the estate and
  reported clean. Both listings are now unioned and paginated.
- `_gh_json` accepted a `--jq` projection, and `--jq .sha` prints a BARE string
  which is not valid JSON. The parse failed, the caller read `None` as "head
  unknown", and the `behind` check was **inert on its first live run without
  ever erroring**. The helper now takes no `--jq`. The unit test had agreed with
  the defect, because its fixture returned the bare sha the buggy call appeared
  to produce — a fixture that models the wrong contract proves the wrong thing,
  and that is noted at the fixture rather than silently corrected.

**The token, and what was deliberately not asked for.** `FLOORFLEET_TOKEN`:
fine-grained, read-only, expiring, **Metadata + Contents + Actions** read.
`Administration: read` was declined — it would let the board read the repo-level
Actions switch directly, but it is the repo-*settings* permission and would have
widened the token across the whole private estate to learn one boolean, when run
history answers the same question. Minting stays Mike's (always-confirm floor
action); the agent wires around a secret and never creates one.

**It asserts the full claim and will be red before it is green.** Five children
were red on their default branches for three days when this landed. Narrowing
the gate to conformance alone would make the board green by not asking the
second question, which is precisely the failure the job exists to catch.

### B1 — the token, and the proof it works (done 2026-07-28)

- [x] **`FLOORFLEET_TOKEN` minted and the scheduled job proven end to end.**
  Mike minted it the same day: fine-grained, read-only, expiring 2026-10-27,
  **all repositories owned by the account**, read on actions + code + metadata,
  no user permissions, **no Administration**. Set into the estate-root repo's
  secret store by Mike directly, so the value never passed through an agent or a
  transcript.

**Why "all repositories" rather than the 13 named children — this is the part
worth keeping.** A token scoped to a named list cannot see repo 14. A new child
would not appear in the account listing at all, so the board would report it as
*nothing* rather than as a red — which is precisely the under-enumeration
failure the whole instrument exists to prevent, reintroduced through its
credential. Read-only `contents` + `actions` on the owner's own account is a
modest surface; a list-scoped token would have quietly defeated the tool.

**The proof.** A `workflow_dispatch` run on 2026-07-28 exercised the whole path
on a GitHub runner with **no local clones of anything**: 13 children plus the
parent enumerated from GitHub, every repo's latest floor run read, the six
unenrolled repos listed, and **exit 1 on the five red floors** — failing for the
right reason rather than on a configuration fault, which is the only distinction
that makes a red board worth having.

🔎 **The degraded-authority path was proven in production, not merely
unit-tested.** The board printed *"Actions-off was INFERRED (not read) for 14
repo(s)"*. The token deliberately carries no `Administration: read`, so the
repo-level Actions switch is unreadable, and the check fell back to run history
**and declared that it had done so**. Declining the wider permission was argued
on the grounds that the same question is answerable more cheaply; that argument
is now a demonstrated fact rather than a design claim.

One expected non-finding on the board, called out in the workflow's own comments
before it was ever run: `❌ personal-data term list: absent`. That list is
machine-local by design — it lives outside every repo — so a runner never has
one. It gates the HOOK plane on a developer's machine and does not gate this
job, and the board says so rather than leaving a reader to infer it.

### The two application passes — PA1–PA4, PSA1–PSA2 (done 2026-08-03)

The 2026-08-02 rulings application earned two rule-4 cold passes; both ran
2026-08-03 by a Mike-spawned Fable taker and both cycles closed terminal
(no MAJOR). Mike ruled all six residue findings the same day, each as
counselled, and the application landed within the hour.

- **PA1 [fixed]** — the PB3 rebase notice corrupted `--json` output under a
  subdir `--root` (reproduced: `json.load` raised on the prose-then-document
  stdout). The notice now prints to stderr and the JSON carries
  `rebased_to` — always present, `null` when `--root` was already the top,
  so the field set stays comparable run to run. The breaking probe is now a
  test.
- **PA2 [no change, decided]** — depth matching reds `config/.env.example`
  anywhere, and that shape is conventionally a deliberately-tracked
  template. Ruled leave-the-pattern: a name-shape carve-out is a permanent
  blind spot in a security scanner (SF1's lesson — real values get pasted
  into templates), and the reasoned ignore line is the designed,
  reviewable answer. If FP reports accumulate, Track E weighs them with
  data.
- **PA3 [fixed]** — a `#` glued to a glob silently truncated the exemption
  to a *different path* than written. Ruled fix-at-next-parser-touch, and
  the PA1 commit *was* the next touch, so it was discharged there: a
  no-space `#` is a loud config error (exit 2), tested.
- **PA4 [folded]** — publishscan's config-authored strings (globs echoed in
  errors, finding paths in output) print raw to terminals — C1F3's class.
  Named into C1F3's fix scope so one strip-at-parse change closes the class
  everywhere; no separate work item.
- **PSA1 [fixed]** — TOOLBOX's residual clause said "template", singular;
  two templates publish, and the local one discloses the `acceptEdits`
  default mode. The clause now names both and the mode bit. Ruled
  fix-at-next-TOOLBOX-touch; the records commit was that touch.
- **PSA2 [accepted]** — PS1's corrected standardise instruction reaches
  children at their next pin bump, with each child's own `publishscan` as
  the interim guard. That is the designed propagation model; the finding's
  value was making the dependency explicit, and it is now written in the
  verdict and here.

Verdicts:
[publishscan application](reviews/2026-08-03-0649-publishscan-application-cold.md) ·
[publish-surface application](reviews/2026-08-03-0653-publish-surface-application-cold.md).

## Doctrine — the harvest rides the `[x]` commit, enacted (done 2026-08-03)

Found 2026-07-26, enacted 2026-08-03 by the orchestrated run's inline claim —
which closed in the commit that landed the work, per the clause it was landing.
The preamble's checkbox-states paragraph gained two sentences: an `[x]` and its
harvest to this file are one commit, never two; and an inline claim (`wt: none`)
closes in the commit that lands its work. Rule-4 `⏳` queued in the same commit
(ROADMAP § Doctrine — review-owed). Entry preserved verbatim below.

- [x] (2026-08-03: enacted — the two preamble clauses landed; this entry is the
      grounding) **State, at the point of use, that marking `[x]` and harvesting
      to ROADMAP-DONE are one commit — not two.** The ROADMAP preamble defines
      the `[x]` state but says nothing about *when* the harvest happens, and the
      cold-content gate fires the moment an `[x]` lands on the hot path. So
      marking three items done in one commit and harvesting in the next leaves a
      window in which the **pushed** floor is red — which is exactly what
      happened on 2026-07-26 (`d847866` red, `0485540` green). Local scans were
      green throughout, because the harvest was already done on disk before the
      first push was checked; only the pushed floor saw the window.
      **This is the same shape as a ruling already made**, which is what makes
      it a candidate rather than a one-off: AWA2 put the `⏳` pointer *in the
      commit that lands the work* so no window exists where landed doctrine sits
      unpointed. Same argument, different marker — an `[x]` and its harvest
      belong in one commit so no window exists where a completed item sits
      stranded on the hot path. Both are instances of a more general rule worth
      naming if a third case appears: **a state change and the bookkeeping the
      floor demands of it ship together.**
      **A third instance arrived the same day, from the opposite direction — and
      it names the mechanism.** A post-outage recovery sweep found one item
      still `[~]` **claimed** whose work had shipped hours earlier (`b89a306`).
      Of the three states that is the worst to leave behind: a later session
      reads `[~]` as *a live session owns this* and skips it, so delivered work
      sits looking permanently in progress. The reason it was missed is
      structural, not carelessness — **every other item that run was claimed
      with a worktree, and merging the worktree forced a return to the roadmap.
      This one was claimed `wt: none — inline on main`, so nothing ever forced
      the return.** The forcing function was the worktree, and the item that
      skipped the worktree skipped the closing step with it. So the rule wants a
      second clause aimed at exactly that case: **an inline claim is closed in
      the commit that lands its work**, because there is no merge step later to
      remember it. Same family as the `[x]`/harvest pairing above — a state
      change and its bookkeeping ship together — and the same reason it keeps
      recurring: the bookkeeping is only reliable when something *makes* you do
      it. (Moved from ROADMAP.md 2026-08-03.)

## Estate-root widening pass residue — ER1–ER4 applied (done 2026-08-03)

Ruled 2026-07-28 (Mike, plain-language walk-through with per-option impacts);
cycle already CLOSED
([verdict](reviews/2026-07-28-1216-estate-root-widening-cold.md), 0 MAJOR /
1 minor / 3 notes, every count re-swept independently). Applied 2026-08-03 by
the orchestrated run as the terminal application of a closed cycle — no pointer
queued.

- [x] **ER1** — the making-public confirmation now includes the pre-flip scrub
      of the estate-root name (`AUTONOMY.md`, always-stop floor's making-public
      entry): a private child's onramp names the root by design, the flip
      publishes every mention at once, and pre-flip is the one moment a scrub
      buys everything back.
- [x] **ER2** — `PROPAGATION.md` now says where the local-path convention is
      defined: per estate, in its own private root's onramp — the one place the
      name may appear.
- [x] **ER3** — the "10 lines beside what it holds" figure restated as roughly
      8–10 and marked approximate on purpose; the exact figures (63/19) marked
      exact-and-reproduced.
- [x] **ER4** — the pointer convention fixed in `RECORD.md` § *Detail lives on
      demand*: a pointer to an addendum entry names "the `SESSIONS.md` entry of
      \<date\>", never the earlier detail file the addendum extends. The two
      broken instances live in closed/append-only records (the 2026-07-28
      SESSIONS addendum link and the widening pass's brief) — noted, left
      unrewritten by design; the convention stops the recurrence.
      (Moved from ROADMAP.md 2026-08-03.)

## Third-seat executor trial — runs 1–4, promotion landed (done 2026-08-03)

The trial Mike opened 2026-07-23 (`dadde1d`): dispatch routine, well-floored
items to the mid tier, keep the step-down only on the floor's evidence, record
the outcome either way. Four runs, nine dispatched items, one failure; the
promotion the data supported landed 2026-08-03 in `ECONOMICS.md` § *The
orchestrated-run tier split* (mid tier as standing executor for well-floored
known-pattern builds + prescriptively-reviewed fixes; discriminator floor
density, not nominal class; rule-4 `⏳` queued at landing). Run outcomes
preserved verbatim below. (Moved from ROADMAP.md 2026-08-03.)

  - **Run 1 outcome — 2026-07-23 (Opus-orchestrated queue run):** two items
    dispatched to Sonnet — the **cc-tools vocab audit** (`85b17dd`: clean
    single-file delivery, zero-drift finding correct on my review, 160/160 node
    tests, recommendation correctly *held as a recommendation* not baked) and
    the **S3 datescan build** (`6077972`: `tools/datescan.py` + 41 tests, suite
    372 green, advisory wiring correct, honest baseline reported, exemption
    limits documented honestly). **Both PASSED the orchestrator review with no
    hand-up and no rework** — first positive data point that Sonnet genuinely
    does the routine-docs and first-of-kind-scanner classes under the floor.
    **One run ≠ a standing tier claim** (extracted-from-practice wants
    corroboration): leave the trial open for a second run's data before
    promoting Sonnet to the standing executor seat for these classes. Note for
    contrast: the doctrine-text apex sweep + the correctness-sensitive ccrepo
    ledger were kept on **Opus** this run (doctrine-text + silent-failure class
    → capable tier, per ECONOMICS QR5) — the split behaved exactly as the tier
    rule predicts.
  - **Run 2 outcome — 2026-07-23 (0618 Opus-orchestrated queue run):** two more
    Sonnet items — the **S1 wrapscan** and **S5 spellscan** first-of-kind scanner
    builds (`72e8ecb`/`760260473`, advisory-only, 40+60 tests, suite 472). **Both
    PASSED** the orchestrator review no-rework, each surfacing an honest judgement
    call left to its ⏳ review. (Recorded in the 0618 session entry as "run 2" but
    not folded into this trial record until the 0707 run — reconciled here.)
  - **Run 3 outcome — 2026-07-23 (0707 Opus-orchestrated queue run):** one item
    to Sonnet — **applying the datescan DSR1–DSR8 review findings + re-baseline**
    (`b7b292c`). This is a *step up* from run 1's classes: not a fresh build or a
    docs audit but **modifying scanner detection logic** (a silent-failure class,
    the kind ECONOMICS QR5 nominally routes to the capable tier). It was
    dispatched to Sonnet because it was **exceptionally well-floored** — 41
    existing tests + selftest + a cold review naming exactly what to change — and
    the orchestrator (Opus) re-verified the suite and read the risk-bearing DSR3
    logic + header before merge. **PASSED with no rework**: all eight findings
    applied, baseline 60→0, and Sonnet independently **caught three further real
    bugs** the review hadn't named, declared the DSR3 silent-miss trade honestly
    in-header, and correctly *declined to guess* an un-derivable date (left an
    honest `allow`). **Reading:** the discriminator that worked was the *floor
    density*, not the nominal class — a well-floored silent-failure task with a
    prescriptive review is safely Sonnet-with-Opus-verify; a *thinly*-floored one
    still isn't. **Three runs now agree** (five Sonnet items, zero rework): the
    docs-audit, fresh-scanner-build, and prescriptively-reviewed-fix classes all
    clear the floor. This is now enough corroboration to **write Sonnet into
    ECONOMICS as the standing executor** for those classes — a small doctrine edit
    (self-authored ⇒ rule-4 ⏳ at landing) that a future session should take; the
    one guardrail the data supports is *floor density, not nominal class*, so the
    doctrine line must say "well-floored + prescriptively-reviewed", not "any
    routine work". The two first-of-kind *reviews* this run stayed on **Opus**
    (gate-flip judgement → capable tier) — split held as predicted.
  - **Run 4 outcome — 2026-07-23 (0959 Opus-orchestrated queue run) — NOT a
    clean sweep, and the exception is the useful data.** Four Sonnet items: the
    two review-applies (wrapscan, spellscan — prescriptively-reviewed-fix) and
    the **pathscan (S2)** build (fresh build of a *known* pattern — reused
    linkscan-shaped path resolution) all **PASSED no-rework**. The fourth,
    **stampscan (S4)**, did **not**: a genuinely-new mechanism (marker parsing)
    whose failure mode — parsing its own documentation as real markers and
    exit-2-blocking the floor — its fixtures couldn't anticipate. The defect
    surfaced **at head** and needed an orchestrator correction (unwire). This
    *confirms* the tier split's safety logic (catchable failure caught by
    floor + Opus review, precisely where the split says to pay for capability)
    and **sharpens the promotion line**: the discriminator is **floor density,
    not nominal class** — a fresh build of a *known* pattern is Sonnet-safe, a
    fresh build of a *novel mechanism* keeps Opus-verify-at-merge earning its
    keep (its floor is necessarily thin — fixtures can't cover an unknown
    failure mode). So the standing-executor doctrine line (still owed, future
    session) should read "well-floored builds of *known* patterns +
    prescriptively-reviewed fixes", and must **not** generalise to "any
    first-of-kind build". Four runs of data now; the promotion edit stays a
    future session's rule-4 doctrine act.

## secretscan residue + E6c — low variety is not innocence (done 2026-08-03)

SF1+SF2+SF3 ruled 2026-07-28 (Mike, walk-through with a live six-shape probe;
cycle already CLOSED, verdict
[secretscan fragment cold](reviews/2026-07-28-1220-secretscan-fragment-cold.md)),
then superseded in shape by E6c's general rule — in credential-key context,
low character variety is not evidence of innocence — and built to E6c by the
2026-08-03 orchestrated run in one secretscan change. Whole-shape carve-outs
now decide before every variety-reading gate on the assigned path (32+
unbroken alphanumeric runs, both hex leading forms, uppercase, base32; and
four-plus separator-joined word passphrases, both spellings); the ruled probe
went 2/6 → 6/6; placeholder/indirection/path suppression keeps precedence;
the blocking set only widened. SF3's canary suite: 16 shapes across the five
ruled families plus vendor formats, count pinned, contract stated at the top
of the test file. The triage record's ≥32-entropy aside carries its dated
correction at source, and the SF verdict's own quoted specimen carries a
reasoned allow-marker (the new rule flagging it is the finding fixed). Suite
830 → 846 green; selftest extended with both ruled shapes. Entry preserved
verbatim below. (Moved from ROADMAP.md 2026-08-03.)

- [x] (2026-08-03: applied, built to E6c) **secretscan pass residue — SF1–SF4, RULED 2026-07-28 (Mike,
      plain-language walk-through with per-option impacts and a live
      six-shape probe).** The rule-4
      pass ran 2026-07-28 (Fable): **0 MAJOR / 1 minor / 3 notes, cycle
      CLOSED** ([verdict](reviews/2026-07-28-1220-secretscan-fragment-cold.md)).
      All four red legs reproduced old-vs-new; the FP fixes hold; the
      estate figures verified (the 26→4 delta is the ruled untrack).
      **SF1+SF2** (minor+note, ruled together as one low-charset-diversity
      family) — the new kebab exemption un-flags hyphenated passphrases
      (caught before, clean now; the snake twin was already exempt), and the
      pre-existing lowercase-hex gap is half its stated size (digit-leading
      hex already flags; letter-leading slips) → **TAKE BOTH WHOLE-SHAPE
      CARVE-OUTS**: in assigned-secret context, a full-match 32+ lowercase
      hex value and a 4+ hyphenated/underscored lowercase-word value are not
      identifier/slug-suppressed. Cry-wolf risk is git SHAs, which rarely sit
      assigned to credential-named keys. **Ruled on a live probe, recorded
      because it sharpens the case**: of six credential-shaped assignments,
      four passed clean — both passphrase spellings and both letter-leading
      hex values — while only the digit-leading hex and the mixed-class
      password flagged. **Also carried, and it corrects a record**: the
      triage's "entropy net catches ≥32 chars regardless of key name" aside
      is true only for mixed-class values, and was probed false for this
      family — two 32-character values in the probe did not flag.
      **SF3** (note) — the corpus re-scan question answered: sound
      regression floor, insufficient acceptance test → **BUILD THE CANARY
      SUITE**: a standing fixture set of credential *shapes* (env-var, hex,
      base64, passphrase, connection string) that must always flag, run
      beside the corpus re-scan on gate changes. It would have caught SF1.
      **SF4** (note) — resolved at reconcile, no action.
      **Work owed: SF1+SF2 carve-outs, SF3 canary suite, and the triage
      record's entropy aside corrected.**
      **Superseded in shape, not in substance (Mike, 2026-07-28):** the two
      named carve-outs are now a special case of the general rule ruled under
      **E6c** — in credential-key context, low character variety is not
      evidence of innocence. Build to E6c; this entry is the grounding for
      why, and the probe evidence above still stands.

## B2+B3 FS rulings applied — the board carries its authority (done 2026-08-03)

FS1–FS5 ruled 2026-07-29 (Mike, all accepted, FS1 both legs), applied
2026-08-03 by the orchestrated run: discovery authority printed beside the
answer (footer + `--json`, loud warning on an empty private-capable listing),
the three-outcome remote read (`unknown` rows red `--check`; only HTTP 404
means "not enrolled"), the token spec's all-repos grant stated on every
surface atelier carries, the wired-denominator headline, archived/unreadable
counts printed even at zero, and the `green("")` docstring + selftest legs.
One out-of-scope crash fix landed with it: a repo carrying no
`.atelier-floor.json` felled `render` (advisory initialised as a bare list
where every reader expects the C1 dict) — the board felled by the very
absence it exists to report; fixed with a test. Suite +22 (66 → 88 in
floorfleet's own file); live `--from-github` end-to-end run clean. The
application's rule-4 pointer is queued (the FS1 MAJOR keeps the cycle open).
Ruling entry preserved verbatim below. (Moved from ROADMAP.md 2026-08-03.)

- [x] (2026-08-03: applied, pointer queued) 🎯 **B2 + B3 — REVIEWED 2026-07-29 (rule-4 Fable cold pass):
  PASS-WITH-FINDINGS — 1 MAJOR / 2 minor / 2 notes. FS1–FS5 RULED
  2026-07-29 (Mike): all accepted, FS1 both legs** — floorfleet gains a
  discovery-authority footer (which listings answered, counts, warning
  when the private-capable listing is empty); an unreadable `CLAUDE.md`
  renders `unknown`, never "no pin"; the consumer's token spec states
  the all-repos grant; plus the headline filter (FS2), the archived-skip
  footer line (FS3), the annotation (FS4) and the `green("")` docstring +
  selftest leg (FS5). Rulings verbatim + counsel:
  [B2+B3 cold pass](reviews/2026-07-29-1251-b2b3-floorfleet-status-cold.md).
  **Application owed as one build item (code + tests); the applier
  queues its rule-4 pointer in the landing commit.**

## TAA + C1F residues applied — the floor line tells the whole truth (done 2026-08-03)

Both ruled 2026-07-28 (Mike, plain-language walk-throughs), both cycles
already CLOSED
([TA application verdict](reviews/2026-07-28-1136-ta-application-cold.md) ·
[C1 advisory verdict](reviews/2026-07-28-1204-c1-advisory-cold.md)); applied
2026-08-03 by the orchestrated run as terminal applications — no pointers
queued. TAA1: the scope-guard comment re-labelled, all class members shut,
pinned by a source-text test. TAA2 + C1F1 unified as one note-joining design
(the `elif` is gone; `why`, drift and cover notes join on the line). C1F2:
`days_over` on the floor line, twinned with floorfleet's wording and pinned
equal by test. C1F3 + PA4: C0 controls stripped at both ruled parse seams
(floor's whole-document config ingest; publishscan's ignore-file and output
surfaces) — drop-don't-escape, with the interpolation-point encoding kept as
the layered inner guard and the LS1 security test rewritten to say so.
Residue found honestly at application: `floorfleet` parses child configs
through its own seam and remains an open surface of the class — recorded as
a live Track C item. Suite +23. Both ruling entries preserved verbatim below.
(Moved from ROADMAP.md 2026-08-03.)

- [x] (2026-08-03: applied, terminal) **TA-application-pass residue — TAA1–TAA3, RULED 2026-07-28 (Mike,
      plain-language walk-through with per-option impacts).** The terminal
      cold pass returned 0 MAJOR / 1 minor / 3 notes
      ([verdict](reviews/2026-07-28-1136-ta-application-cold.md)); the cycle
      is closed, and per rule 3 the residue was Mike's to decide.
      **TAA1** (minor) — a comment in `floor.py`'s scope guard still labels
      two fail-opens "(open)" that the same series shut → **FIX**: two-line
      comment edit re-labelling both members shut, TA1 pointer kept.
      **TAA2** (note) — the two 🟡 notes share one report field via `elif`,
      so a future softenable scanner with a cover flag would silently drop
      its scope-drift note → **JOIN THE NOTES** (chosen over the
      comment-only variant: same cost, and a joined note can't decay the way
      a comment relies on a future reader honouring it).
      **TAA3** (note) — AW6 doesn't say whether a second queued pointer over
      the same files discharges the delta-list widening duty → **HOLD for a
      third instance**, per the reviewer's counsel and the >2 promotion
      rule; this is the second recorded case.
      **Work owed: TAA1 + TAA2.**
- [x] (2026-08-03: applied, terminal) **C1-pass residue — C1F1–C1F3, RULED 2026-07-28 (Mike, plain-language
      walk-through with per-option impacts).** The terminal pass
      returned 0 MAJOR / 1 minor / 2 notes
      ([verdict](reviews/2026-07-28-1204-c1-advisory-cold.md)); cycle
      closed, residue Mike's per rule 3.
      **C1F1** (minor) — on the floor's human line, an advisory's `why`
      displaces the "N of M scope paths missing" drift note (it survives
      only in `--json`), so a softened check with shrinking cover shows the
      reason but not the shrink → **JOIN THE NOTES**, restoring the TA3 fix
      exactly where the board is worst-informed.
      **C1F2** (note) — the record says an expired advisory shows how many
      days it has stood "on the floor and the board", but the count renders
      on the board only → **ADD THE COUNT TO THE FLOOR LINE** (chosen over
      correcting the record: it makes both true, and puts the ageing
      pressure at commit time rather than on a board someone must go and
      look at).
      **C1F3** (note) — config-authored strings (`why`, disabled reasons)
      print raw to terminals; a hostile child config could embed escape
      sequences → **STRIP C0 CONTROLS AT PARSE**, closing the pre-existing
      class as well as C1's two new fields. Scope widened by the PA4 ruling
      (Mike, 2026-08-03): `publishscan`'s two config-authored surfaces —
      ignore-file globs echoed in error messages, and finding paths in
      output — are in this fix's scope, so one change closes the class
      everywhere. Low priority while the estate is single-owner; it becomes
      real on first outside adoption.
      **Work owed: all three.**

## The ⏳ pointer grammar mechanised + B4 wired (done 2026-08-03)

The FUNDED build (Mike, 2026-07-28) and the B4 HV rulings (Mike, 2026-07-29),
landed as one build per HV2 by the 2026-08-03 orchestrated run — a session
that authored none of the breaches. `tools/pointerscan.py`: the grammar
detector (seeded questions + three reviewer-direction families, each traceable
to a real instance) and the cycle-state detector (an item asserting a review
is owed while carrying that review's verdict; state read from the item's own
text, not an item↔verdict key — the only mechanical keys were measured at a
near-total false-positive rate by the 2026-07-26 audit, the failure
`harvestscan` fingerprints content to avoid, and order is the discriminator:
a verdict link alone is lawful, review-has-run evidence *preceding* an owed
claim is not). Scope settled on evidence: marker glyph in bullet or state
prefix, OR a review-obligation phrase inside an emphasis run, `[x]` never a
pointer — emphasis-scoping measured against plain-prose scoping, which swept
in two innocent discussion items including the FUNDED entry itself. **Pass
type ruled a lawful fourth field** beside {delta, intent record, tier}: tier
is the same class of fact, both route the review, the ceiling forbids an
evaluative account, not routing; the FG6 boundary specimen passes clean.

**The corpus corrections, recorded so nothing inherits the old figures:**
instance 2 was LOCATED (the pathscan S2 first-of-kind pointer, live
2026-07-24 → 2026-07-27, carrying three seeded questions — matching the
finding's "two of three pointed away from the load-bearing problem"); the
"five stale residues" of `98cef9e` were **seven** (the sweep had looked only
in § Doctrine — review-owed; two were still live at HEAD and were fixed in
the landing merge: the ADR 0008 entry and the floor-local seam entry, both
now stating "reviewed — the ruling is what is owed"); the "three instances"
of grammar breach were **19 distinct defects** across 424 roadmap revisions
(14 commits, 3.3%, every spot-check a true positive). A third live finding
was P6's marker misuse (`⏳` where a decision was owed) — re-marked `🎯`.

**B4 wiring per the HV rulings:** `harvestscan` registry-wired, scoped to
net-bulk-delete commits (≥50 net lines off `ROADMAP.md` alone — gating on the
watched pair nets a harvest to zero, 1 in-scope commit instead of 6),
warn-only; shipped-config replay reproduces the cold pass exactly (6 in
scope, 3 warn, 15 items, the dd7fcb74 incident caught). HV2: the pointer
exclusion is pointerscan's test now (the old copy saw two of four pointer
shapes). HV3 as ruled was measurably inert (session records hold almost no
checkbox items) — the survivor search gained prose paragraphs in the harvest
destinations only, and the widening's effect was measured before landing
(107 → 85 firing commits across the ungated history). HV4: plane wording
fixed (--staged reads the INDEX). The replay harness ships as `--replay`.
Suite +42 across the build; both selftests green; all acceptance pairs
correct. Handed up, recorded as open work: a warn-only registry scanner
renders `✅ enforced` on the floor board (EP3's class — decide together).
The three source entries preserved verbatim below.
(Moved from ROADMAP.md 2026-08-03.)

- [x] (2026-08-03: closed by the FUNDED build) 🎯 **The `⏳` pointer steered its own reviewer — THIRD instance,
      2026-07-28.** Two queued pointers carried their authors' full reviewer
      agendas inline, against the ROADMAP's own refs-only ceiling; the taker
      read them before a brief existed to defer them, and it measurably steered
      the pass — two of three seeded questions pointed away from the
      load-bearing problem. The ceiling is stated in this file's own preamble
      and was not enforced by anything.
      **A third instance arrived on 2026-07-28, and it is the sharpest
      evidence yet, because the author had read this very finding hours
      earlier.** The B4 pointer was queued carrying a seeded first question
      ("is a 26.9% firing rate the right ground for *do not wire*") plus the
      author's own doubt about his verdict. Refs-only survived being *written
      down as an open finding*, in the same file, in the same session that
      then broke it. Stripped on the next commit when Mike asked for the
      review to be queued and it was re-read.
      **By this file's own recurrence rule** — three instances of a trivial
      failure is a defect in the system producing it, not in the person — the
      argument for a forcing function is made. **Mike funded it 2026-07-28**;
      specified as its own item immediately below, deliberately left unclaimed
      for a fresh session.

- [x] (2026-08-03: built, pointerscan landed) **FUNDED (Mike, 2026-07-28) — mechanise the `⏳` pointer grammar.**
      Unclaimed on purpose: this is the work that closes the finding directly
      above, and it wants a session that did not write the breach.

      **A correction to carry, because it changes where this goes.** The first
      sketch said "`reviewscan` is the natural home". It is not, and the
      premise was never checked before being written down — the same shape as
      the two false blockers this programme already records. `reviewscan`
      **explicitly refuses to lint ROADMAP sections**, and that refusal is a
      recorded decision (the 2026-07-18-0820 record), on the grounds that a
      lint demanding structure under every roadmap heading fires on prose and
      gets trained away. Honouring that rejection is in its module docstring.
      The tool that *already* parses `⏳` list items in `ROADMAP.md` is
      **`sizescan`** (`_LIVE_ITEM`, for harvest integrity), and
      `harvestscan.is_pointer()` already isolates pointers from work items —
      two existing building blocks rather than a new tool.

      **First question the work must answer, not assume:** is this the same
      rung the 0820 record rejected? Arguably not — that rejection was about
      demanding a field under *every roadmap heading*, whereas this binds only
      the `⏳` item type, of which there are rarely more than three at a time
      and whose form is formulaic by definition. But that argument is the
      author's, it is exactly the kind that has been wrong here before, and it
      should be tested rather than inherited.

      **What is actually mechanisable.** "A field outside {delta, intent
      record, tier}" sounds crisp and is not detectable — the failure is
      *evaluative* content, which is judgement. What the three real instances
      share is narrower and testable: a **seeded question** or an explicit
      **instruction to the reviewer**. Instance 1 carried *"Aim a reviewer at
      the one real trade … Is that right for a security floor?"*; instance 3
      carried *"the pass's first question is whether …"*. A question mark
      inside a `⏳` item, plus a short phrase list of reviewer-direction
      forms, catches all three.

      **Acceptance corpus — located, not assumed.** Instance 3 is recoverable
      as a pair (`ff8080b` wrote it, `7ca1f1d` stripped it), which gives a
      must-flag and a must-stay-silent version of the same pointer. **Instance
      1 is still LIVE in this file** — the ADR 0008 entry's *"Aim a reviewer
      at the one real trade … Is that right for a security floor?"* — so the
      guard has a real specimen to prove itself against on day one, and a real
      finding to fix. Instance 2 was not located this session; find it or
      record that it could not be found, rather than inheriting "two" on
      faith. **A boundary specimen joined the corpus by the FG6 ruling
      (Mike, 2026-08-03):** the F1 pointer carried *"Design/intent pass per
      REVIEW.md §…"* — an instruction to the reviewer, but a procedural one
      (pass type), not evaluative and not a seeded question. Whether
      pass-type is a lawful fourth field beside {delta, intent record, tier}
      is this build's to settle, decided on the corpus rather than pre-ruled.

      🔎 **And that live specimen already breaks the obvious scoping.** The
      ADR 0008 entry carries a reviewer agenda but is marked `[ ]`, with
      "review owed" *mid-body* rather than in its lead — so a guard scoped to
      the `⏳` marker alone would miss the one instance still standing.
      `harvestscan.is_pointer()` has the same limit (marker, or lead-6-words).
      Settle the scope before the detector: **what makes an item a
      queued-review pointer** is the prior question, and getting it wrong
      makes the check cover nothing while reporting clean — this programme's
      organising defect, which it would be embarrassing to reproduce in the
      guard against reproducing failures.

      **A second detector rides the same scope decision — the stale pointer
      (Mike, 2026-08-03).** The grammar check above asks *what may a pointer
      say*; the same parse answers *is the pointer still true*. An item
      claiming a review is owed while a matching `docs/reviews/` verdict
      exists is a mechanically detectable contradiction. Raised by a `ros`
      session as atelier's call, correctly — the guard is shared-floor, not
      child-local. It needs the same prior question settled and reuses the
      same two building blocks, so this is one build, not two; splitting it
      would make a third original of *what makes an item a queued-review
      pointer*.

      **The count was wrong on first telling, and the corrected count does
      not clear the threshold.** The raising session said four instances and
      read that as past promote-at-three. A sweep of this file found
      **five** — all in § *Doctrine — review-owed*, all from **one commit**
      (`98cef9e`, the nine-pass queue take), which prepended verdicts to nine
      items and stripped the stale wording from only four. One occurrence
      with five residues is not five recurrences: the ladder's threshold is
      **not** met, and the case for wiring rests on the detection being
      near-free once the scope is settled. Recorded this way so a later
      session does not inherit "past the threshold" on faith.

      **The residue named a sharper defect than the one detected.** All five
      said "review queued" when the review had run and what was owed was
      Mike's *ruling*. Existence-of-verdict catches the contradiction; reading
      the cycle states — owed → reviewed → ruled → applied → closed — says
      which state the item is actually in. Which of the two the guard carries
      is the build's to settle. **Acceptance corpus:** the five were cleaned
      in the commit adding this paragraph, giving a must-flag/must-stay-silent
      git pair in the same shape as instance 3's, rather than a live specimen.

      **Advisory first**, whatever the scope: a pointer is fixable in the same
      commit that writes it, so the warning lands at the one moment it costs
      nothing.

- [x] (2026-08-03: applied, pointer queued) 🎯 **B4 — REVIEWED 2026-07-29 (rule-4 Fable cold pass):
  PASS-WITH-FINDINGS — 1 MAJOR / 2 minor / 2 notes; every recorded
  figure reproduced exactly. HV1–HV5 RULED 2026-07-29 (Mike): the shelf
  verdict is OVERTURNED on the pass's measurement — WIRE `harvestscan`,
  scoped and advisory:** registry entry firing only on net-bulk-delete
  roadmap commits (≥50 net lines removed), warn-only, never blocking.
  Evidence: 6 in-scope commits in the 391-commit history, 3 warns, all
  justified, the `dd7fcb74` incident caught; strict delete-only rejected
  (it misses the incident, +48/−184). HV2 — the pointer exclusion's
  dependency on the FUNDED `reviewscan` ⏳-grammar check is named and
  they build together. HV3 — survivor search widened to
  `docs/sessions/` + `docs/reviews/`, effect measured by the replay
  harness before landing. HV4 — usage wording + the staged-vs-working
  seam handled in the wiring build. HV5 lapsed under HV1. Rulings
  verbatim + counsel:
  [B4 cold pass](reviews/2026-07-29-1306-b4-harvestscan-cold.md).
  **Application owed as one wiring build item (scope + tests + registry
  + HV2–HV4 folds); it queues its rule-4 pointer at landing.**


## The 2026-08-05 queue take — five cold passes, every cycle closed (done 2026-08-05)

The whole rule-4 queue of the 2026-08-03 orchestrated run taken by a
Mike-spawned Fable session (author sessions uninvolved), claimed on `main`
before the worktree per CONCURRENCY § Claiming work. All five passes returned
**0 MAJOR** and every open cycle closed terminal: pointer-grammar build + B4
wiring (both cycles), the FS application (B2+B3), the mid-tier
standing-executor doctrine, the E6 application (the intent cycle), and the
landing-equals-bookkeeping clauses. Findings held for Mike's ruling in the
ROADMAP § *Doctrine — review-owed* item of the same date; verdicts:
[pointer-grammar + B4](reviews/2026-08-05-1238-pointer-grammar-b4-wiring-cold.md) ·
[FS application](reviews/2026-08-05-1244-fs-application-cold.md) ·
[mid-tier executor](reviews/2026-08-05-1248-mid-tier-standing-executor-cold.md) ·
[E6 application](reviews/2026-08-05-1253-e6-application-cold.md) ·
[landing-equals-bookkeeping](reviews/2026-08-05-1258-landing-equals-bookkeeping-cold.md).
The five refs-only pointers this take discharges are preserved in the
verdicts' brief sections verbatim (each brief opens with its queue ref), so
the pointer text is not duplicated here.
