# Ruling inventory — the 81 open 🎯 items on atelier's board

Read 2026-10-03 (UTC) from `docs/ROADMAP.md` (`grep -n '^- \[ \] 🎯'` → 81 lines) and every linked item file in the working tree, nested sub-bullets included. A peer session is live and has claimed several non-🎯 items on 2026-10-03 (`qr-*` worktrees); none of the 81 files was dirty at read time. Ids are `<section>/<item>`; full paths in the appendix. Review findings inside verdict files were **not** inventoried — only the wrappers that point at them.

## 1. Scale

81 items await Mike. **15 are review-verdict wrappers** — "cycle CLOSED, findings await Mike's ruling round" — covering about 138 findings across 18 verdict files (≈150 with C5's twelve) (020/215, 160/010–070, 160/100–110, 160/220–230, 280/030, 290/050, 290/060). **66 are standalone decisions.** One of those, C5 (020/030), also has its own verdict, C5R1–C5R12, and the verdict reshapes the decision, so it is counted as standalone. By blast radius: **FLEET 66 · ATELIER-ONLY 9 · UNSURE 6**. FLEET here means a change to `docs/method/`, to the floor block and its template stamp, or to a `tools/*.py` guard that children run by call under ADR 0008. **About 13 items look partly or wholly overtaken** (see the staleness column). Section 150's README warned about this on 2026-08-09: "Expect the count to shrink on contact" — and that class has been recorded six times. Most of the standalone FLEET items are new doctrine *proposals* (whether a rule earns a line, and where it lives). Very few are build approvals.

## 2. Inventory, grouped by surface

Columns: **id** · **subject** · **decision asked** · **options offered / recommendation** · **surfaces** · **blast** · **deps / wrapper** · **staleness risk**

### A. Review-verdict wrappers (REVIEW.md rule 3 ruling round) — another agent inventories the findings

| id | subject | decision asked | options / rec | surfaces (delta) | blast | deps / wrapper | staleness |
|---|---|---|---|---|---|---|---|
| 020/215 | Laws-removal apex pass findings | Rule LR1–LR9 (0 MAJOR, 3 MODERATE) | Verdict counsel; LR3 explicitly "principal to confirm" | `00-APEX.md`, PROPAGATION floor block, `build/templates/CLAUDE.md` stamp | FLEET | `reviews/2026-08-15-1031-laws-removal-apex-cold.md`, LR1–LR9 | LR2 "appears resolved" by `c782e14`; LR3 appears restored-and-closed by `1b46d05` |
| 160/020 | Child-membership + work-locality findings | Rule CM1–CM13 (3 MODERATE: CM1 unbounded "every repo", CM2 no home for exclusions, CM3 no exemption register) | Verdict counsel | `PROPAGATION.md` § Who is a child, `CONCURRENCY.md` § Stay in your lane | FLEET | `reviews/2026-08-09-0820-child-membership-work-locality-cold.md`, CM1–CM13 | PROPAGATION has been heavily edited since (310 route, 320/190 rule 2), so some CM findings may have moved |
| 160/030 | PRINCIPLES §9 time-dimension findings | Rule TD1–TD3 | Verdict counsel | `PRINCIPLES.md` §9, `method/README.md`, `CONVENTIONS.md` | FLEET | `reviews/2026-08-09-0821-principles-9-time-dimension-cold.md`, TD1–TD3 | Touches 115/020 (confidence/provenance metadata) |
| 160/040 | Cancelled-run clause findings | Rule CR1–CR6 (CR2: the prescribed re-run can cancel a peer's run) | Verdict counsel | `RECORD.md` § The session log | FLEET | `reviews/2026-08-09-0822-record-cancelled-run-clause-cold.md`, CR1–CR6 | — |
| 160/050 | Five 2026-08-05 passes' residue | Rule FF1–FF4, PG1–PG7, EA1–EA3, MT2–MT3, LB1–LB2; the item also folds in "the P6 ADR ruling" | Verdict counsel (FF4: classes-only rewrite) | `floorfleet.py`, `pointerscan.py`, secretscan/E6, mid-tier doctrine, landing clauses | FLEET | Five verdicts: `reviews/2026-08-05-{1244-fs-application,1238-pointer-grammar-b4-wiring,1253-e6-application,1248-mid-tier-standing-executor,1258-landing-equals-bookkeeping}-cold.md` | "SCHEDULED 2026-08-09" sitting never recorded rulings; the P6 part duplicates 260/080 |
| 160/060 | F1/GUARDS rebuild seventh pass | Rule GA1–GA3 | GA1: single-source the loader, or record copies as design | `GUARDS.md`, ten scanners' reason loaders | FLEET | `reviews/2026-08-05-1320-f1-guards-allowances-cold.md`, GA1–GA3 | **GA1 effectively ruled**: 115/080 "FUNDED by Mike 2026-09-20", part 1 done. GA2–GA3 notes remain |
| 160/070 | Sitting's five doctrine edits | Rule SE1–SE2 (notes) | Notes only | Five small doctrine edits of 2026-08-04 | FLEET | `reviews/2026-08-05-1301-sitting-five-edits-cold.md`, SE1–SE2 | Notes only; likely quick to dispose |
| 160/100 | E6b advisory + E3 fingerprint | Rule AB1–AB6 (AB1: carve-out exceeds ruled scope, reaches credential-keyed values) | Verdict counsel | `tools/secretscan.py`, `tools/floor.py`, `ci.yml`, `tools/README.md` | FLEET | `reviews/2026-08-09-0825-e6b-advisory-e3-fingerprint-cold.md`, AB1–AB6 | Section 150 named AB1 a standout; unruled |
| 160/110 | E7 leakscan build | Rule LK1–LK6 + G2 reach note (LK1: malformed scope fails open; reviewer argues MAJOR) | Verdict counsel | `tools/leakscan.py`, terms example | FLEET | `reviews/2026-08-09-0826-e7-leakscan-build-cold.md`, LK1–LK6 | LK1 interacts with C5 (020/030) scoped markers |
| 160/220 | Board-generator child-truth | Rule BG1–BG14 (BG1/BG2 already ruled at 290/060) | Verdict counsel; "BS1 and BG1/BG2 … rule together" | `tools/board.py`, `pointerscan.py`, `tools/README.md`, CHANGELOG | FLEET | `reviews/2026-08-17-0730-board-generator-child-truth-cold.md`, BG1–BG14 | BG1/BG2 ruled 2026-08-17 (funded, not yet built) |
| 160/230 | 0817 ruling-round application | Rule RR1–RR14 (RR1 the apex floor list is narrower than AUTONOMY's; RR2 orchestrator condition only attestable) | Verdict counsel | `REVIEW.md` r3/r4, `00-APEX.md`, PROPAGATION floor + stamp, `RECORD.md`, `GUARDS.md`, `COMMUNICATION.md` | FLEET | `reviews/2026-08-17-1000-ruling-round-application-cold.md`, RR1–RR14 (RR8 = AA9) | — |
| 280/030 | Channel section findings | Rule CH1–CH16 (CH4: "never stash" vs mandated autostash) | Verdict counsel | `CONCURRENCY.md` § The channel, PROPAGATION floor bullet, template stamp | FLEET | `reviews/2026-08-17-1000-channel-doctrine-cold.md`, CH1–CH16 | CH1 is also queued at 280/040; CH4 overlaps the autostash fix 320/210 (✅) |
| 290/050 | BS1 ruled; board-store residue | Rule BS2–BS14 (BS1 itself RULED 2026-08-17) | Verdict counsel | `tools/board.py`, `CONCURRENCY.md` § On a split board, board-store ADR | FLEET | `reviews/2026-08-15-1030-board-store-migration-cold.md`, BS2–BS14 (010/050 🛑 holds the cycle) | BS1 wording applied; 010/020 BUILT 2026-09-20 |
| 290/060 | BG1/BG2 ruled; BG3 open | Rule BG3: does the generated index get a wrapscan exemption ("needs Mike's own answer")? Plus BG4 | BG3 "re-opens the generated-file exemption question the author withdrew" | `tools/board.py`, wrapscan, `.atelier-floor.json` | FLEET | Same BG verdict as 160/220 | BG1/BG2 funded, untaken. Rule BG3 with 160/220 |
| 160/010 | `cctranscript --search` findings | Rule CS1–CS14 (CS1 regex gate, CS2 exit code, CS3 no privacy caution) | Verdict counsel | `instruments/cctranscript`, man page, design doc | ATELIER-ONLY | `reviews/2026-08-15-1032-cctranscript-search-cold.md`, CS1–CS14 | cctranscript has changed since (210/100 ✅, 210/050 claimed on 2026-10-03). Re-check CS1–CS2 at HEAD |

### B. `GUARDS.md` — what a guard must declare and how it may be built

| id | subject | decision asked | options / rec | surfaces | blast | deps | staleness |
|---|---|---|---|---|---|---|---|
| 115/010 | Evidence-window rule for guard design | Mint the rule *"a guard may only enforce a rule whose licensing context fits inside its evidence window"* into GUARDS.md, or not | Proposed wording given; cost: "some existing guards fail" | `GUARDS.md` (new prior-question section) | FLEET | Pairs with 115/120; feeds 400/010 | — |
| 115/120 | Every guard declares its purpose and proves it fires | Adopt a four-field declaration (rule cited, grounding incidents + replay, purpose gap, evidence window) on every registry entry | Strong prior art cited; "at least four current guards fail the bar"; FOLDED with PT1 (fourth-requirement slot) 2026-08-23 | `GUARDS.md`, `tools/floor.py` registry `why`, scanner canary suites | FLEET | Needs 115/010; carries PT1's ruling | — |
| 320/020 | Strict where we author, forgiving where we read | Add a "which side of the boundary decides forbid vs make-cheap" rule to the fourth requirement | Proposal from a child; no rec; unmeasured against atelier's guards | `GUARDS.md` fourth requirement | FLEET | Companion to 320/050 | — |
| 320/050 | A guard declares who it protects from whom | Add a threat-model declaration (protects a reader from an artefact vs a writer from a peer writer) | Proposal; shape 3 reproduced at the parent, shape 2 by registry read | `GUARDS.md`, `floor.py` (11 of 15 hook checks read the worktree) | FLEET | Same class as 320/060, 320/390, 010/160 | — |
| 320/030 | Capture, don't compose, test fixtures | Adopt "fixtures for parsed program output are captured, with the producing version recorded", and choose the home | Home undecided: `EVIDENCE.md` or `GUARDS.md`; may merge with a seam rule | `EVIDENCE.md` / `GUARDS.md` | FLEET | — | — |
| 110/100 | Exceptions narrower than a line; binaries unscanned | Mike's concern is exceptions "too broad", down to "just the specific characters". Decide whether to fund span-level allowances, and whether guards scan binary contents at all | "Not scoped to a mechanism"; span markers need a span concept in every parser | `GUARDS.md` § Granularity, `secretscan.py`/`leakscan.py` marker parsers, `_looks_binary` | FLEET | Binary half overlaps 020/150 (G3 binary, RULED BLOCKING 2026-08-04, funded) | Binary half partly decided by G3 |
| 020/170 | F1 rebuild: two rulings owed | Confirm the GUARDS.md model supersedes E6d(i)'s *escalate-only* wording with FG2's *provenance* constraint (declared, reasoned, expiring) | Recorded in the doc; "not assumed" | `GUARDS.md`, E6d (020/140) | FLEET | Was also owed D1's consequence | **Half overtaken**: D1's consequence RULED 2026-08-09 (section README). Only E6d(i) remains |

### C. Guard posture and the programme frame (policy-as-code; PROPAGATION § When a rule keeps breaking)

| id | subject | decision asked | options / rec | surfaces | blast | deps | staleness |
|---|---|---|---|---|---|---|---|
| 020/240 | Ladder: "framing OR mechanism" vs "both, always" | Does the rule-breaking ladder gain a floor (rung 1 framing never optional; rung 2 owed wherever a check can see the moment), or stay "stop at the first rung that fits"? | Stated as a posture change; no rec | `PROPAGATION.md` § When a rule keeps breaking | FLEET | Frames 020/220, 020/230; gated in practice by 115/170 | — |
| 020/220 | Census: which rules have a forcing function | Commission an enumeration of all doctrine into enforced / directive-only / unenforceable-accepted | Scope "all doctrine" on REVIEW rule 3's definition | All `docs/method/`, ADRs, templates, skills; `GUARDS.md` bar | FLEET | 320/390 cites it; 310/130 wants a sibling census | — |
| 020/230 | Directive wording as a design duty | Make "framing at the point of use" a design obligation on every rule, not just a remedy after breakage | No rec | `PROPAGATION.md` rung 1, all doctrine | FLEET | Sibling of 020/240 | — |
| 115/100 | Build a before-plane (harness hooks) | Fund guards that act *before* the act (session-start or pre-tool hooks, distributed permissions) | No design. Lesson from the withdrawn reply gate: must sit before the act | Harness plane: `.claude-plugin/`, hooks, permission template | FLEET | "Item 1 of four"; only thing that could mechanise 020/230; 115/170 asks whether to add at all | — |
| 390/020 | Private-data repos rest on a confirm rule, not a control | Choose a mechanism to stop private/client repos being published or shared | Pre-push/pre-share check · forge org policy · periodic visibility audit; none chosen | `AUTONOMY.md` § Always confirm, `DATA-PROTECTION.md`, possibly floor/hook | FLEET | Same frame as 020/220–240; neighbour of P3 260/050 | — |
| 115/170 | Guard layer is ~75% of open work | Proportionality: should the estate keep spending most capacity on guards? "Every item in this section is downstream of the answer" | Not rhetorical; 4,598 floor findings, none blocking | Board priorities across 020/115/320 | ATELIER-ONLY | **Gates** 115/220 explicitly, and in effect 115/100, 115/120, 020/220 | Mike has funded guard work since (115/080, 2026-09-20) without ruling this |

### D. Floor and scanners (`tools/*.py`, floor registry, CI workflows)

| id | subject | decision asked | options / rec | surfaces | blast | deps | staleness |
|---|---|---|---|---|---|---|---|
| 020/030 | C5: the estate-root term on leakscan's term list | Re-rule how the term list handles a term with volume (118 lines). Must be ruled *together with* 020/050 (C5R5/C5R6) | 1 per-term scoping (narrow, reasoned, dated; **recommended**, on volume alone) · 2 shapes-only + records carve-out · 3 accept ~125 reds · 4 decline the term (honest fallback) | `tools/leakscan.py`, machine-local term list, `GUARDS.md`, PROPAGATION name↔posture split | FLEET | Hybrid: verdict `reviews/2026-08-09-0708-c5-term-list-remeasure-cold.md` C5R1–C5R12 (2 MAJOR); LK1 (160/110) | C5R4: every figure drifted within hours, so rule on classes, not numbers |
| 020/040 | Scanner verdict needs a third state | Add an "all found, all accepted" headline (exit codes unchanged, `clean` kept in JSON), for leakscan and siblings | Fix shape given; "lands on its own" | `tools/leakscan.py` `render_human` + sibling scanners, `--json` | FLEET | Same class as G3 | — |
| 020/120 | D3: signscan cannot fail CI | Flip signscan from `--warn` to blocking ("the flip is Mike's, pairs with his key rotations") | No options | `.github/workflows/ci.yml`, `floor.yml` (reusable; children call it), `SIGNING.md` | FLEET | Key rotations | Still `--warn` on both planes at HEAD (verified) |
| 020/350 | Bidi / zero-width chars in a board `why` | Strip the override set, escape it visibly, or accept and record | Three options; no rec | `tools/floor.py` `strip_controls` | FLEET | FR3 follow-on | — |
| 260/050 | P3: floor should know repo visibility | Make visibility a declared, platform-verified floor input, and tighten the floor on public repos | Shape given; open: declared-private-but-actually-public = "live breach" | `tools/floor.py`, `.atelier-floor.json`, licenscan, publishscan; "ADR-worthy" | FLEET | F1's FG1 requires the model to say whether P3 is in scope; 320/380; 390/020 | Not built (no visibility input in floor.py) |
| 320/060 | Require a path-scoped commit where worktrees exist | Floor blocks whole-index commits when `git worktree list` > 1 unless marked | Proposal with 3 limits; "atelier is structurally multi-worktree", so the tax hits every commit | `tools/floor.py`, `GUARDS.md`, `CONCURRENCY.md` | FLEET | With 320/050, 310/020; "one guard or three" | — |
| 320/080 | `quotescan` | Build a guard checking quotes attributed to Mike against the transcript corpus (forbids the act) | Proposal; hazards measured; the 320/070 rule must land in the **same commit** | new `tools/quotescan.py`, floor registry, `RECORD.md` | FLEET | **Depends on 320/070**; 320/100 shows its blind spot | — |
| 320/310 | Should pathscan block? | Make pathscan blocking instead of warn-only | "When to decide: after 320/010's declared roots ship… measure what is left" | pathscan in floor registry | FLEET | **Waits on 320/010** (claimed on 2026-10-03, `qr-pathscan-fp`) and 320/170 | Premature until 320/010 lands |
| 020/070 | C1b: delete the legacy bare-list spelling | Unclear: dates RULED 2026-08-09 ("default, not mandate"); what remains is phase 2 (remove legacy parse) plus one repo's migration | — | `tools/floor.py` (legacy still parses), children's `.atelier-floor.json` | FLEET | C2 (020/080) | atelier's own config has no bare-list `advisory` now; the migrated declaration's `review-by 2026-09-01` has passed. Reads as work, not a decision |
| 115/220 | Streaming line readers are 3–4 mechanisms | Part 1b now, fold into part 2/3, or defer pending 115/170 | Ranked by risk: shape 3 (five identical copies) cheap; shapes 1/4 plausible; leave shape 2 (linkscan fences) | ten `tools/*scan.py` readers | FLEET | **Explicitly waits on 115/170**; under 115/080 | — |
| 020/140 | E6: secretscan posture + impact axis | Nothing visibly owed: E6a/E6b/E6c DONE, E6d and the estate view RULED, builds pending | — | `SECRETS.md`, `tools/secretscan.py` | FLEET | E6d build pairs with one child's declaration; estate view lives in the private estate root | **Likely stale as a 🎯**: the only Mike-owed piece (E6d(i) supersession) sits at 020/170 |
| 020/020 | B4 roadmap-deletion guard (harvestscan) | "Fund the next step or leave it a hand-run tool" | Three wireable shapes listed | `tools/harvestscan.py`, floor registry | FLEET | Duplicate of 230/020 | **Overtaken**: HV1 (2026-07-29) "principal overturned the verdict"; floor.py registry wires harvestscan warn-only with `--only-bulk-deletes` |
| 230/020 | Nothing catches a deleted roadmap item | (a) fingerprint guard · (b) advisory-only · (c) decline, keep manual audit | Three options | `harvestscan`/`sizescan`, ROADMAP.md | FLEET | Duplicate of 020/020 | **Overtaken** by HV1 (an advisory, scoped variant is wired) and by the per-item board split (deletion is now a file removal, so the "staged ROADMAP.md vs HEAD" design is stale) |
| 020/010 | The five red floors | Unclear: "each is that repo's own call to clear" | — | children's floors | UNSURE | B2 `--status` | Found 2026-07-28 (5 of 14 red), more than two months ago; no Mike decision is stated |

### E. `PROPAGATION.md` — floor block, naming in public trees, pointing up

| id | subject | decision asked | options / rec | surfaces | blast | deps | staleness |
|---|---|---|---|---|---|---|---|
| 320/380 | Floor visibility bullet: tense, and naming the root's path | (i) "is public" → "is **ever made** public"? (ii) Must canonical say that spelling the local path defeats the rule? | (i) proposed wording; (ii) "stated as a question, not a proposed fix" | Floor region in `PROPAGATION.md` + `build/templates/CLAUDE.md` stamp | FLEET | Visibility cluster (260/050, 020/030) | Hand-up owed since Mike's 2026-08-17 "restore canonical and hand the wording up" |
| 310/130 | Parent holds accommodations children can't inherit | Does PROPAGATION owe a rule? (a) declare parent-local narrowings readably · (b) forbid un-offered accommodations · (c) only write down the diagnostic | "Candidates, deliberately not chosen"; census not run | `PROPAGATION.md`, `.atelier-floor.json` scope block, stampscan | FLEET | 320/160 (stampscan can't check a child) | — |
| 310/120 | Pointing up names only atelier as parent | Generalise the route to other parents (for example a private root receiving asset registrations) | "Not decided here": does class-only relax for a private parent? Filing surface? | `PROPAGATION.md` § Pointing up / Who is a child | FLEET | With 310/140, 390/010 | — |
| 310/140 | A PR as the carrier between any two repos | Adopt PRs for sideways and downward routes. **Key fork: does the PR *file* an idea (queue) or carry the *fix* (delivery)?** | Fork named; rule should key on the target's visibility | `PROPAGATION.md` § Pointing up / Report without harming, `CONCURRENCY.md` § What the channel is not | FLEET | 310/120, 310/020, 280/050, 410 | — |
| 310/020 | Nothing enumerates what the estate owes the house | Choose a child-side machine-readable marker convention (across ten children) so an upstream-debt instrument can exist | "Wants its own ruling"; price against stampscan wiring | `PROPAGATION.md` § Pointing up, new tool beside `floorfleet.py`/`pins.py` | FLEET | Track D stampscan residue (020/110) | — |
| 260/080 | P6: estate-internal context in public records | Write the Decision and Rejected sections of the drafted ADR: open-estate transparency (name×posture join the only bar) vs class-level detail vs bind-by-surface | Draft argues both postures, plus a third shape | `docs/decisions/2026-08-05-1233-estate-internal-context-in-public-records.md` (Status: draft, Decision empty, verified), `RECORD.md` | FLEET | Umbrella over 020/050, 320/330; also folded into 160/050 | Live |
| 020/050 | Name↔posture join keeps recurring here | Standing gap: scrub, accept the records as historical and bind only new writes, or take the C5 term | Rewriting the 7 live lines "worth doing whatever C5 is ruled" | atelier live files and records; `PROPAGATION.md` name↔posture | ATELIER-ONLY | **One ruling with C5 020/030** (C5R5/C5R6); under P6 260/080 | 7-line count measured 2026-08-09; may have drifted |
| 320/330 | Does the naming precedence reach doctrine prose? | Should public doctrine name a private child, even in a worked example? | (a) rewrite as "a private child" · (b) keep PU-2's naming as history · (c) case by case | `PROPAGATION.md` § Pointing up and § Report without harming (two instances) | ATELIER-ONLY | Under P6 260/080; split from 320/190 | — |
| 310/040 | Queue the block-trim finding in the child | Sequencing already ruled ("once that's ready… queue it"); the gate was 310/050 | — | one child's `CLAUDE.md` (queued there, not edited here) | ATELIER-ONLY | Was blocked on 310/050 | **Gate cleared**: 310/050 is ✅ RUN and RULED. Now an action, not a decision; not found in the child's board by grep |

### F. Board vocabulary and rollout (`tools/board.py`, roadmap legend)

| id | subject | decision asked | options / rec | surfaces | blast | deps | staleness |
|---|---|---|---|---|---|---|---|
| 310/060 | State vocabulary too narrow to index by | How the generated index shows dispositions (declined, superseded, parked, in-flight) | 1 renderer reads a prose marker · 2 `disposition:` field · 3 more brackets (Mike's phrasing; reverses 2026-07-22 tri-state) · 4 two axes. "None is recommended" | board README legend, `tools/board.py` (renders every `[x]` as ✅), `CONCURRENCY.md` § Claiming | FLEET | Settles 010/100's house half and the non-🎯 310/070; reaches ten children at pin bump | — |
| 010/030 | Fleet rollout of the split board | "Order and timing Mike's" for the remaining monolithic boards | — | children's boards | FLEET | — | docker-heap split 2026-08-17 (`211a00d`), after the item's reading; **only nova remains** (274 lines, untouched since 2026-08-09). BS1 slip note superseded by 010/020 BUILT |
| 010/100 | ros used `[~]` for "partially delivered" | Normalise / admit a fourth state / record the divergence | Three options | board README, `CONCURRENCY.md` § Claiming | FLEET | 310/060 | **Overtaken**: ros README says Mike ruled 2026-08-17 and all 38 were re-keyed to `[ ]`. The house-vocabulary half is 310/060 |

### G. `CONCURRENCY.md`

| id | subject | decision asked | options / rec | surfaces | blast | deps | staleness |
|---|---|---|---|---|---|---|---|
| 010/160 | CF3 dirty-sibling stop | Is CF3 an index-safety rule (relax: only same-item dirt stops, now that `rebuild --from-index` exists) or a peer-presence rule (keep)? | Both readings are supportable; throughput cost reasoned, not counted | `CONCURRENCY.md` § Claiming at a dirty primary checkout | FLEET | 010/020 ✅; non-🎯 320/120 (CF3 branch list) | — |
| 280/050 | Talk first | Make "ask the owner first" the first resort, with git and the rules as fallback ("talk to decide, write to hold") | Item's reading only; open: idle owners, onramp step 1, floor clause re-ordering | `CONCURRENCY.md`, floor concurrency clause, onramp `CLAUDE.md` | FLEET | 360/020, 360/010, 280/040 (review contamination), CH1–CH5 | — |
| 360/010 | Off-repo concurrency: name and announce | Adopt rule 1 (owner-bearing names for launched jobs) and rule 2 (the announcement covers hosts, jobs, remote files, services); rule 3 (durable host claims) is separate | "Do NOT design a locking protocol"; decide 1+2 and ship | `CONCURRENCY.md`, session-open announcement (floor) | FLEET | 280/050 | — |
| 320/390 | A check in the same invocation as the act isn't a check | Adopt the child's rule (any act) as house doctrine, and choose its home | CONCURRENCY vs `EVIDENCE.md` ("when a reading counts as evidence") | `CONCURRENCY.md` § Integration hygiene or `EVIDENCE.md` | FLEET | Adjacent to 320/220 ✅ ("verify the act"); 020/220 | — |
| 360/020 | Cross-repo session coordination | Pick a mechanism (or none) for seeing what sessions in *other* repos hold | Estate index · estate-wide channel · build only 310/020 first; none chosen | `CONCURRENCY.md` § The channel / Claiming | FLEET | 280/050 is "its cheapest first answer"; 310/020 | — |

### H. How we work and build (`COMMUNICATION`, `RECORD`, `EVIDENCE`, `PRINCIPLES`, `GLOSSARY`)

| id | subject | decision asked | options / rec | surfaces | blast | deps | staleness |
|---|---|---|---|---|---|---|---|
| 420/010 | An ask stops the whole run | When a session asks, and what it does with unblocked work meanwhile | Candidates: sort by what it blocks, front-load, park-and-proceed, proceed on a stated assumption, floor never proceeds, presence mode, visible waits | `COMMUNICATION.md`, `CONCURRENCY.md` (durable open question), `AUTONOMY.md` floor, session-open prompt | FLEET | 320/110, 280/050, 300, 410 | — |
| 320/110 | The ask device manufactures decisions | Add "establish that a decision exists first; a settled matter is a *record*; absent evidence → *find out first*" | Candidate wording given; one incident | `COMMUNICATION.md` § Asking for a ruling, `00-APEX.md` "genuine dilemma" | FLEET | 420/010 | — |
| 320/070 | A transcript has three principal-authored channels | Adopt (1) a mid-turn instruction is first-class and is homed before the turn ends; (2) audits state which channels (and authorship filter) they read | Twice-evidenced (320/100 corroboration) | `GUARDS.md` ("rule with no home"), `RECORD.md`, audit practice; cctranscript | FLEET | **Must land before or with** 320/080 | Its strongest atelier instance (210/100) is now ✅ fixed; the rule is still unwritten |
| 320/100 | Unquoted attributions; claims outrun evidence | (1) a form-check flagging "ruled / his instruction" without quote or citation; (2) evidence for the rung decision on "never a claim stronger than its evidence" | "Cheap direction, offered not prescribed" | `RECORD.md` § An approval…, `00-APEX.md`/`EVIDENCE.md`, possible scanner | FLEET | 320/080, 320/070, 020/240 | Non-🎯 310/080 is a live instance of the attribution defect |
| 220/010 | Instruments can't see a trust failure | Add to `EVIDENCE.md` that harness metrics don't measure trust | Self-authored, so it queues a rule-4 review | `EVIDENCE.md` | FLEET | Pairs with 220/020 | — |
| 220/020 | Evidence hygiene: you're inside your own corpus | Add "key self-analysis signals to harness markers, never prose" | Same | `EVIDENCE.md` | FLEET | 220/010 | — |
| 370/010 | Prefer artefacts over reports | Does "irreversible action: corroborate the tool's report from artefacts" earn a line, and where? Plus "never overwrite a running executable" | "Decide alongside 350"; no mechanical check | `EVIDENCE.md`/`PRINCIPLES.md` (unnamed), tool-writing conventions | FLEET | 350/010, 380/010 | — |
| 380/010 | Show a positive control first | Does "an instrument shows a known positive before its negative counts" earn a line, inside 370 or beside it? | Narrative argues *beside* | `EVIDENCE.md`; `CONCURRENCY.md` (method cross-check) | FLEET | 370/010 | — |
| 330/010 | SHA-2 or better for every hash | Home the rule (plus the class "don't pick a primitive silently"), then sweep | "Likely `PRINCIPLES.md` or conventions"; no scanner reflexively | `PRINCIPLES.md`/`CONVENTIONS.md`, estate tools sweep | FLEET | 350/010 | — |
| 350/010 | Verification exact, not probable | Does "use the primitive's full strength; never compare a truncation" become a rule, and where? Then sweep | Same home candidates; a check is a dataflow problem, so leave it to review | `PRINCIPLES.md`/`CONVENTIONS.md` | FLEET | 330, 370, 380 | — |
| 340/010 | Long-running ops need a way back | Extend the undo principle with three questions (survive operator loss, resume safely, prove completion) above a threshold | One paragraph beside the undo rule; threshold is the hard part | undo rule, file unnamed (`AUTONOMY.md` holds hard-to-undo) | FLEET | — | — |
| 160/120 | Glossary ratify pass | Mike reads `GLOSSARY.md` end to end: wording, full-definition entries (principal, agent, session, doctrine), admission rule | Action for Mike | `docs/method/GLOSSARY.md` | FLEET | Non-🎯 160/130 (complex vs complicated) rides with it | SEED banner still present (verified) |
| 115/020 | Confidence on a fact: stored or computed? | (a) computed from method · (b) stored coarse rank · (c) a decision bar | **Counsel (a), with (b) where confidence varies within a method**; "the child repo owns the fix" | a child's build; `PRINCIPLES.md` §9 provenance | UNSURE | 160/030 (TD) | Unclear whether this is a house rule or a ruling for one child |
| 200/030 | R1: recurrence count mechanical; mining cadence | Choose cadence and trigger (schedule vs review close); widen the corpus to transcripts; does "make adjustments" mean propose items or edit doctrine? | Last point "not decided here and should not be assumed" | anti-slop registry (section 200), `PROPAGATION.md` § When a rule keeps breaking, cctranscript | UNSURE | 020/220 | — |

### I. `instruments/` (ADR 0006 layer)

| id | subject | decision asked | options / rec | surfaces | blast | deps | staleness |
|---|---|---|---|---|---|---|---|
| 210/030 | ccarchive encryption: where the crypto comes from | A `age` everywhere · B house format · C reimplement age · **C′ (counselled): encrypt with `age`, decrypt in-process** | C′ counselled | `instruments/ccarchive`, design doc, `SECRETS.md` | ATELIER-ONLY | The same decision as 210/020; review warranted at build | — |
| 210/020 | ccarchive encryption at rest (parent line) | Same decision as 210/030 | — | same | ATELIER-ONLY | Duplicate 🎯 of 210/030 | Counts twice in the 81 |
| 210/140 | ccgrab web-media instrument | Unclear: placement RULED 2026-09-09; open is scope (one platform vs a general scraper) and, implicitly, whether to fund | "Small set of named handlers plus a generic manifest grep"; posture fixed (public, ungated only) | `instruments/`, ADR 0006 addendum at build | ATELIER-ONLY | — | — |
| 210/160 | ccarchive counts files, not sessions | Does "session transcripts" mean top-level `.jsonl` only, or the whole transcript class? | Item says "whoever builds this should decide" | `instruments/ccarchive` report and `--json` | ATELIER-ONLY | — | 🎯 may only mark that Mike originated it |

### J. New territory — no mechanism chosen yet

| id | subject | decision asked | options / rec | surfaces | blast | deps | staleness |
|---|---|---|---|---|---|---|---|
| 400/010 | Which mechanism should a new need take? | Commission a decision rule among guard, skill, slash command, hook, instrument and MCP server, and choose where it lives | Four candidate axes; home undecided (`GUARDS.md`? new `build/` doc? ADR?) | `GUARDS.md`, `ECONOMICS.md`, ADR 0006, `COMMUNICATION.md` hook lesson | FLEET | 115/010, 115/100 | — |
| 390/010 | Repo relationships beyond parent/child | Model consumer-of-asset and subject-cluster relationships, or rule it not atelier's problem | Registry file · per-repo prose · "not atelier's" ("worth taking seriously") | `REACH.md` § The credential boundary, `PROPAGATION.md` | UNSURE | 310/120, 310/140 | — |
| 410/010 | Sessions with no repo | What a repo-less session reads, records and hands on | Home-dir onramp · standing scratch repo · move to the target repo first | user-level onramp (outside repo), `RECORD.md`, session close | UNSURE | 310/140, 280/050, 360/020, 240 | — |
| 300/030 | Census: what would the estate notice and restore? | Unclear: Mike already ruled 2026-08-17 "looked at next"; the census must run in the private estate root | — | private estate-root repo; atelier gets only the class | UNSURE | 300/020 re-rank | Already ruled to proceed; the 🎯 may only mean "launch it there" |

## 3. Clusters — one ruling settles several

1. **Visibility and naming in public trees.** P6 ADR 260/080 is the umbrella. Ruling it decides 020/050 and most of 320/330, and frames C5 020/030 (C5R5/C5R6 say C5 and 020/050 "are one ruling"). It also bears on 320/380(ii) and on FF4 inside 160/050. Do P6 first, then C5 with 020/050.
2. **Guard proportionality first.** 115/170 is a gate. 115/220 waits on it explicitly. It decides appetite for 115/100, 115/120, 020/220, 320/080 (new guard), 320/060 (new block), 320/310 (block), 020/120 (block) and 260/050 (tightening).
3. **What a guard must declare.** One GUARDS.md sitting covers 115/010 + 115/120 (already carries PT1) + 320/020 + 320/050 + 320/030, and 400/010 if the mechanism-choice rule lands in GUARDS.md.
4. **Directive vs enforced posture.** 020/240 is the posture ruling. 020/220 (census) and 020/230 (wording duty) follow from it; 115/100, 390/020 and 320/390 are instances.
5. **Shared checkout and the staged sweep.** 320/050, 320/060, 320/390 and 010/160, plus CH4 in 280/030 (and the non-🎯 320/350 and 320/120). One ruling on *talk first vs path-scoped commit vs worktree-by-default* settles most of them.
6. **Cross-repo routes and awareness.** 280/050 (talk first) and 310/140 (PR carrier) are the cheap answers. Ruling those two largely answers 360/020's first step, 410/010's hand-on, 310/120's filing surface and part of 390/010. 310/020 is the instrument behind them.
7. **Principal attribution.** 320/070 → 320/080 (ordering constraint: same commit) + 320/100. Ruling 320/070 is the prerequisite.
8. **How-we-build one-liners.** 330/010, 350/010, 370/010, 380/010, 340/010, 220/010, 220/020 and 320/030 all ask "does this earn a line in PRINCIPLES/EVIDENCE, and where?" 370 and 380 explicitly ask to be ruled with 350.
9. **Asking.** 420/010 + 320/110, both on `COMMUNICATION.md` § Asking for a ruling (and the existing ask-in-the-device standing rule).
10. **Board vocabulary.** 310/060 settles 010/100 (already ruled locally in ros) and the non-🎯 310/070; it pairs with BG3 at 290/060 (rendering of the generated index).
11. **Close-outs needing only confirmation** (no new judgement): 010/100, 020/020, 230/020, 020/140, F1's D1 half of 020/170, GA1 in 160/060, LR2/LR3 in 020/215, 310/040 (gate cleared), 010/030 (only nova left).
12. **Duplicated 🎯 lines:** 210/020 = 210/030; 290/060 BG3 ⊂ 160/220; 160/050's P6 = 260/080.
13. **Glossary:** 160/120 with non-🎯 160/130.

## 4. Items whose ask is ambiguous

- **020/010** — "each is that repo's own call to clear". No decision for Mike is stated. Candidate to drop the 🎯.
- **020/070** — dates already RULED. The rest is phase-2 deletion of the legacy parse, which reads as work. Whether Mike must approve the deletion (or a new deadline, now that 2026-09-01 has passed) is unstated.
- **020/140** — headline says "RULED… all his call, none built". Every child is ruled or done, so the 🎯 seems to persist only as a header glyph.
- **020/170** — "the model supersedes E6d(i)'s escalate-only wording". It is unclear whether Mike is asked to *confirm* a supersession the doc already wrote, or to *test* FG2's hypothesis first ("a hypothesis to test at design… E6d stands unchanged until the rebuild lands"). The two readings conflict.
- **020/050** — mixes a no-ruling action ("rewrite the seven live lines… needs no ruling") with a ruling (accept vs widen the rule). Only the second is Mike's.
- **110/100** — the commission is clear ("just the specific characters") but the ask is not: fund span markers? Decide binary scanning (partly done by G3)? The item says "not scoped to a mechanism".
- **115/020** — counsel is (a), but "the child repo owns the fix either way". Unclear whether Mike is setting a house rule or ruling for one child.
- **200/030** — three asks stacked: cadence and trigger, corpus widening, and what "make adjustments" licenses. Only the last is plainly Mike's.
- **210/140 / 210/160** — 🎯 sits on build-detail questions the text hands to "whoever builds this".
- **300/030** — already ruled "looked at next". The residual act is commissioning a session elsewhere.
- **310/040** — the gate has cleared, so this is an action, not a decision.
- **360/010** — asks to decide rules 1 and 2 and defer rule 3, but rule 2 touches the floor announcement (FLEET) while rule 1 is a host convention. Rule them separately.
- **390/010** — includes "not atelier's problem at all"; the first question is jurisdiction, not mechanism.
- **160/050** — one wrapper over five verdicts with five prefixes plus a P6 reference. It needs splitting before a round can walk it.
- **320/380 (ii)** — the filer says it does "not know which way this should fall". It is a genuine open question with no proposal.

## Appendix — id → item file

| id | path |
|---|---|
| 010/030 | `docs/roadmap/010-board-store-migration-per-item-files-mik/030-fleet-rollout-of-the-split-board.md` |
| 010/100 | `docs/roadmap/010-board-store-migration-per-item-files-mik/100-ros-carries-38-items-using-a-different-tilde.md` |
| 010/160 | `docs/roadmap/010-board-store-migration-per-item-files-mik/160-cf3-s-sibling-stop-is-now-stricter-than-its-cause.md` |
| 020/010 | `docs/roadmap/020-policy-as-code-programme-five-tracks-mik/010-the-five-red-floors-themselves-are-now-open-wo.md` |
| 020/020 | `docs/roadmap/020-policy-as-code-programme-five-tracks-mik/020-b4-the-roadmap-deletion-guard-built-measured-a.md` |
| 020/030 | `docs/roadmap/020-policy-as-code-programme-five-tracks-mik/030-c5-re-ruling-owed-the-composed-term-list-execu.md` |
| 020/040 | `docs/roadmap/020-policy-as-code-programme-five-tracks-mik/040-a-scanner-s-verdict-has-two-states-and-needs-t.md` |
| 020/050 | `docs/roadmap/020-policy-as-code-programme-five-tracks-mik/050-the-join-c5-guards-was-written-twice-more-on-2.md` |
| 020/070 | `docs/roadmap/020-policy-as-code-programme-five-tracks-mik/070-c1b-migrate-the-remainder-then-delete-the-lega.md` |
| 020/120 | `docs/roadmap/020-policy-as-code-programme-five-tracks-mik/120-d3-signscan-cannot-fail-ci.md` |
| 020/140 | `docs/roadmap/020-policy-as-code-programme-five-tracks-mik/140-e6-the-floor-s-posture-and-the-dial-that-makes.md` |
| 020/170 | `docs/roadmap/020-policy-as-code-programme-five-tracks-mik/170-f1-rebuild-the-block-vs-advise-model-from-base.md` |
| 020/215 | `docs/roadmap/020-policy-as-code-programme-five-tracks-mik/215-rule-4-cold-pass-queued-laws-removal.md` |
| 020/220 | `docs/roadmap/020-policy-as-code-programme-five-tracks-mik/220-a-the-census-nobody-has-run-which-rules-have-a.md` |
| 020/230 | `docs/roadmap/020-policy-as-code-programme-five-tracks-mik/230-b-the-half-with-no-owner-doctrine-that-reaches.md` |
| 020/240 | `docs/roadmap/020-policy-as-code-programme-five-tracks-mik/240-the-posture-change-this-implies-stated-so-it-i.md` |
| 020/350 | `docs/roadmap/020-policy-as-code-programme-five-tracks-mik/350-bidi-and-zero-width-strip-decision.md` |
| 110/100 | `docs/roadmap/110-estate-duplication-exception-audit-mike/100-two-granularities-the-2026-08-09-audit-never-asked-about.md` |
| 115/010 | `docs/roadmap/115-guardrail-architecture-mike-commissioned/010-mint-the-evidence-window-rule-as-guard-design.md` |
| 115/020 | `docs/roadmap/115-guardrail-architecture-mike-commissioned/020-confidence-on-a-fact-stored-field-or-computed.md` |
| 115/100 | `docs/roadmap/115-guardrail-architecture-mike-commissioned/100-the-before-plane-is-empty-and-it-is-the-only.md` |
| 115/120 | `docs/roadmap/115-guardrail-architecture-mike-commissioned/120-every-guard-declares-the-purpose-it-answers-to.md` |
| 115/170 | `docs/roadmap/115-guardrail-architecture-mike-commissioned/170-the-guard-layer-is-consuming-the-programme.md` |
| 115/220 | `docs/roadmap/115-guardrail-architecture-mike-commissioned/220-the-line-readers-are-three-mechanisms-not-one-with-parameters.md` |
| 160/010 | `docs/roadmap/160-doctrine-review-owed/010-rule-4-review-queued-tier-fable-pass-type-code.md` |
| 160/020 | `docs/roadmap/160-doctrine-review-owed/020-the-child-membership-work-locality-cycle-close.md` |
| 160/030 | `docs/roadmap/160-doctrine-review-owed/030-the-principles-9-cycle-closed-2026-08-09-0-maj.md` |
| 160/040 | `docs/roadmap/160-doctrine-review-owed/040-the-cancelled-run-clause-cycle-closed-2026-08.md` |
| 160/050 | `docs/roadmap/160-doctrine-review-owed/050-five-rule-4-fable-cold-passes-ran-2026-08-05-e.md` |
| 160/060 | `docs/roadmap/160-doctrine-review-owed/060-a-seventh-pass-the-f1-guards-md-rebuild-the-tw.md` |
| 160/070 | `docs/roadmap/160-doctrine-review-owed/070-a-sixth-pass-the-same-day-the-sitting-s-five-d.md` |
| 160/100 | `docs/roadmap/160-doctrine-review-owed/100-the-e6b-e3-cycle-closed-2026-08-09-0-major-ab1.md` |
| 160/110 | `docs/roadmap/160-doctrine-review-owed/110-the-e7-leakscan-cycle-closed-2026-08-09-0-majo.md` |
| 160/120 | `docs/roadmap/160-doctrine-review-owed/120-glossary-ratify-pass-mike.md` |
| 160/220 | `docs/roadmap/160-doctrine-review-owed/220-rule-4-cold-pass-queued-board-generator.md` |
| 160/230 | `docs/roadmap/160-doctrine-review-owed/230-rule-4-cold-pass-queued-the-0817-ruling-round.md` |
| 200/030 | `docs/roadmap/200-anti-slop-invariant-registry-promote-rec/030-r1-the-recurrence-count-has-to-become-mechanic.md` |
| 210/020 | `docs/roadmap/210-instruments-open-features/020-ccarchive-encryption-at-rest-build-not-started.md` |
| 210/030 | `docs/roadmap/210-instruments-open-features/030-the-one-decision-and-it-gates-the-build-where.md` |
| 210/140 | `docs/roadmap/210-instruments-open-features/140-ccgrab-web-media-capture-instrument.md` |
| 210/160 | `docs/roadmap/210-instruments-open-features/160-ccarchive-reports-file-counts-not-session-counts.md` |
| 220/010 | `docs/roadmap/220-observability-of-the-collaboration-itsel/010-doctrine-candidate-the-mechanical-instruments.md` |
| 220/020 | `docs/roadmap/220-observability-of-the-collaboration-itsel/020-doctrine-candidate-evidence-hygiene-a-scanner.md` |
| 230/020 | `docs/roadmap/230-file-size-hygiene-new-2026-07-14/020-nothing-catches-a-roadmap-item-that-is-deleted.md` |
| 260/050 | `docs/roadmap/260-sharing-public-since-2026-07-10-adr-0005/050-p3-the-floor-does-not-know-whether-a-repo-is-p.md` |
| 260/080 | `docs/roadmap/260-sharing-public-since-2026-07-10-adr-0005/080-p6-rpi-f5-estate-internal-context-accumulating.md` |
| 280/030 | `docs/roadmap/280-cross-session-channel-mike-commissioned/030-rule-4-cold-pass-queued-the-channel-section.md` |
| 280/050 | `docs/roadmap/280-cross-session-channel-mike-commissioned/050-talk-first-the-channel-as-first-preference.md` |
| 290/050 | `docs/roadmap/290-ruling-round-2026-08-17-the-cold-run-find/050-bs1-wording-now-fund-the-staged-plane-build.md` |
| 290/060 | `docs/roadmap/290-ruling-round-2026-08-17-the-cold-run-find/060-bg1-bg2-apply-as-counselled.md` |
| 300/030 | `docs/roadmap/300-posture-recover-cheaply-mike-commissioned/030-what-would-this-estate-actually-notice.md` |
| 310/020 | `docs/roadmap/310-pointing-up-the-child-to-parent-route/020-nothing-enumerates-what-the-estate-owes-the-house.md` |
| 310/040 | `docs/roadmap/310-pointing-up-the-child-to-parent-route/040-queue-the-block-trim-finding-in-cbom-after-the-cycle.md` |
| 310/060 | `docs/roadmap/310-pointing-up-the-child-to-parent-route/060-the-board-state-vocabulary-is-too-narrow-to-index-by.md` |
| 310/120 | `docs/roadmap/310-pointing-up-the-child-to-parent-route/120-the-route-is-atelier-specific-any-parent-repo-needs-one.md` |
| 310/130 | `docs/roadmap/310-pointing-up-the-child-to-parent-route/130-the-parent-holds-accommodations-the-child-cannot-inherit.md` |
| 310/140 | `docs/roadmap/310-pointing-up-the-child-to-parent-route/140-a-pr-as-the-carrier-between-any-two-repos.md` |
| 320/020 | `docs/roadmap/320-child-filed-findings-via-pointing-up/020-proposal-strict-where-we-author-forgiving-where-we-read.md` |
| 320/030 | `docs/roadmap/320-child-filed-findings-via-pointing-up/030-proposal-capture-do-not-compose-fixtures.md` |
| 320/050 | `docs/roadmap/320-child-filed-findings-via-pointing-up/050-proposal-a-guard-declares-who-it-protects-from-whom.md` |
| 320/060 | `docs/roadmap/320-child-filed-findings-via-pointing-up/060-proposal-the-floor-requires-a-path-scoped-commit.md` |
| 320/070 | `docs/roadmap/320-child-filed-findings-via-pointing-up/070-proposal-a-transcript-has-three-channels.md` |
| 320/080 | `docs/roadmap/320-child-filed-findings-via-pointing-up/080-proposal-quotescan-and-the-corpus-that-would-libel-him.md` |
| 320/100 | `docs/roadmap/320-child-filed-findings-via-pointing-up/100-unquoted-attribution-is-invisible-to-quotescan-and-a-corroboration-for-070.md` |
| 320/110 | `docs/roadmap/320-child-filed-findings-via-pointing-up/110-proposal-the-ask-device-manufactures-decisions.md` |
| 320/310 | `docs/roadmap/320-child-filed-findings-via-pointing-up/310-should-pathscan-block-instead-of-warn.md` |
| 320/330 | `docs/roadmap/320-child-filed-findings-via-pointing-up/330-does-the-naming-precedence-reach-doctrines-own-prose.md` |
| 320/380 | `docs/roadmap/320-child-filed-findings-via-pointing-up/380-the-floor-s-public-tense-and-whether-it-should-name-the-root.md` |
| 320/390 | `docs/roadmap/320-child-filed-findings-via-pointing-up/390-missing-house-rule-a-check-in-the-same-invocation-as-the-act-is-not-a-check.md` |
| 330/010 | `docs/roadmap/330-sha-2-or-better-for-every-hash-mike-commissioned/010-name-the-rule-and-find-where-the-house-already-br.md` |
| 340/010 | `docs/roadmap/340-long-running-operations-need-a-way-back-mike-comm/010-the-rule-and-where-it-attaches.md` |
| 350/010 | `docs/roadmap/350-verification-must-be-exact-not-probable-mike-comm/010-decide-the-rule-then-sweep-for-discounted-checks.md` |
| 360/010 | `docs/roadmap/360-concurrency-beyond-the-repo-mike-commissioned/010-name-what-you-launch-then-widen-the-announcement.md` |
| 360/020 | `docs/roadmap/360-concurrency-beyond-the-repo-mike-commissioned/020-parallel-sessions-across-different-repos-have-no-shared-view.md` |
| 370/010 | `docs/roadmap/370-the-report-can-lie-while-the-work-is-fine/010-prefer-artefacts-over-reports.md` |
| 380/010 | `docs/roadmap/380-silence-read-as-an-answer/010-make-the-instrument-show-a-positive-first.md` |
| 390/010 | `docs/roadmap/390-repo-relationships-beyond-the-tree-mike-comm/010-consumer-and-subject-cluster-relationships-have-no-model.md` |
| 390/020 | `docs/roadmap/390-repo-relationships-beyond-the-tree-mike-comm/020-shed-and-client-data-repos-rely-on-a-confirm-rule-not-a-control.md` |
| 400/010 | `docs/roadmap/400-choosing-among-implementation-mechanisms-mike-comm/010-no-doctrine-says-which-mechanism-a-new-need-should-take.md` |
| 410/010 | `docs/roadmap/410-sessions-without-a-repo-mike-commissioned/010-no-doctrine-covers-a-session-with-no-tree.md` |
| 420/010 | `docs/roadmap/420-when-to-ask-mike-commissioned/010-an-ask-stops-the-whole-run-decide-when-to-ask.md` |
