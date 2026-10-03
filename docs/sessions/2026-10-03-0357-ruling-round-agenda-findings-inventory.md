# Ruling inventory: unruled cold-review findings in `docs/reviews/`

As of HEAD `306c7c2` (2026-10-03 UTC). The pass was read-only: all 136 files
in `docs/reviews/*.md` were read in full, excluding `withdrawn/` and `drafts/`.
I also checked the board (`docs/roadmap/**`), `docs/ROADMAP-DONE.md` and
`CHANGELOG.md` for ruling records, and checked cited sentences and code at HEAD.
I did not read `docs/SESSIONS.md` or `docs/sessions/`, except the 0925 batch
table needed for the cross-check.

"Ruled" means a ruling by Mike, recorded either in the verdict file or on the
board. The following are **not** counted as rulings:
- "cycle closed, 0 MAJOR" statements
- "House rules for this run" sections
- "Follow-up checklist" sections
- dispositions made by the author or builder

**Severity normalisation:** HIGH, Blocking and MAJOR count as MAJOR; MEDIUM and
MODERATE count as MODERATE; LOW and MINOR count as minor; nit and note count as
note.

**Prefix collisions to keep in mind:**
- AA: AA1–AA5 belong to the 2026-07-26 apex-accountability pass; AA6–AA13 to the 2026-08-17 authority-absolute pass.
- PS: pathscan uses it, and so does publish-surface.
- SR: used by both onramp and size-rebalance.
- F, G, C, R, A, H, L, B, N: each reused by many early passes.
- RC10 is cited on board `160/190:5` for an unrelated estate-root verdict.

---

## 1. Scale

| Status | Files | Notes |
|---|---|---|
| **Unruled** | **41** | All 20 files from the 2026-09-25 batch, plus 21 earlier ones (listed below) |
| **Partly ruled** | **8** | IR, WS (wrapscan), BS, GA, CMF, RG, AA6–13, BG |
| **Author-disposed, never put to Mike** | **16** | 14 pre-rule-3 files (2026-07-10 to 07-12), plus the datescan and spellscan code passes |
| **Ruled by Mike** | **71** | Includes 9 whose ruling is recorded only on the board or in ROADMAP-DONE (EP, LS, PS, ST, TA, TAA, C1F, ER, SF, SR/size-rebalance) |
| Total | 136 | |

The 21 earlier unruled files:
- 2026-07-26 passes: AA1–5, EE, WO, RF
- 2026-08-05 passes: PG, FF, MT, EA, LB, SE
- 2026-08-09 passes: C5R, CM, TD, CR, AB, LK
- 2026-08-15 passes: LR, CS
- 2026-08-17 passes: CH, SW, RR

| Unruled findings | MAJOR | MODERATE | minor | note |
|---|---|---|---|---|
| 0925 batch (20 files) | 9 | 52 | 86 | 62 |
| Earlier files | 6 | 49 | ≈71 | ≈82 |
| **Total** | **15** | **101** | **≈157** | **≈144** |

- 7 of the 101 MODERATEs are already **moot**: CMF2, CMF5, CMF6, RG2 and RG3 because of the 2026-09-18 destroy ruling, plus LR3 and CH4 (see §6).
- Of the 15 MAJORs, **12 are FLEET** (they reach child repos) and 3 are ATELIER-ONLY.
- 7 unruled files carry only minors or notes: AA1–5, EE, WO, MT, EA, LB, SE.

**Cross-check of the 0925 batch (step 4): ✅ no mismatch.** Recounting all 20
`2026-09-25-0715-*.md` verdicts by finding ID gives exactly 9 MAJOR, 52
MODERATE, 86 minor and 62 note. Every row of the table in
`docs/sessions/2026-09-25-0705-review-batch-twenty-cold-passes.md` matches.
One file is wrong internally: **RC**'s restated line (around `:695`) still says
"3 MODERATE / 5 minor", even though the same file re-rates RC4 to minor. The
real count is 1/2/6/6, which is what the session table and board `160/320`
already use.

---

## 2. MAJOR — unruled (15)

Ordered FLEET first, then by how urgent the reviewer said it was. **Blast**
means: FLEET reaches child repos through inherited doctrine, the floor, a
template, a skill or an ADR; ATELIER-ONLY means atelier's own board, records or
instruments.

| # | ID · pass | Claim (plain) | Surface | Counsel (≤15 words) | Blast | Urgency stated | Overtaken? |
|---|---|---|---|---|---|---|---|
| 1 | **AR1** · AR (AP rulings applied) | ADR 0008's 2026-08-23 amendment says `main` has "no branch protection and no ruleset" and signing is "warn-first". A ruleset has been active since 2026-08-09 (deletion, non-fast-forward, required signatures, admin bypass). The amendment was false when written and is false at HEAD. | ADR 0008, amendment at L178–185 (verified L179–180) | A second dated amendment stating the live state; correct `115/180`. | FLEET | FAIL, security; cycle OPEN; "lowers the urgency, not the severity" | No. Lineage EP7 → AP1 → AR1; `140/020` still open |
| 2 | **RC1** · RC (0918 registry code) | `conflictscan --staged` and `leakscan --staged` only recognise a literal `+++ b/` header. Under `diff.noprefix` or `mnemonicPrefix` they scan nothing and exit 0. Proven live on a staged conflict marker and a staged email. | `tools/conflictscan.py:554`, `tools/leakscan.py:912` (verified) | Force the src/dst-prefix flags; pin with a scratch-repo test; single-source the parser. | FLEET (hook-plane floor) | FAIL; "route as a security finding with a recurrence step" | No. Its vehicle, `115/080` parts 2–3, is unclaimed |
| 3 | **RU1** · RU (report-up duty) | The floor bullet carries the rules that protect atelier from a hand-up, but not the one that protects a private child from naming itself. A private child "can file a compliant-looking hand-up that discloses itself on four irretractable surfaces". | `PROPAGATION.md` floor region :171–182; template :83; blockscan map | Add "class only, name yourself on no surface" to both copies; map subsections. | FLEET | One-way disclosure; cycle OPEN | No. Same defect rated MODERATE as **NP6**. The blockscan half is in flight (`320/340`, unmerged `bd09b1b`) |
| 4 | **AR8** · AR (formed at reconcile) | The 2026-08-23 AP1 ruling ("branch protection is not enabled") rested on a premise Mike's own 2026-08-09 ruling had already falsified: a ruleset with owner bypass, applied that day. The second ruling was under-briefed. | AP1 ruling; ADR 0008; the ask template | Re-brief AP1 with the live read; ask which ruling stands; ask template names prior rulings. | FLEET | Apex's informed-ruling condition; cycle OPEN | None |
| 5 | **DR1** · DR (DA rulings applied) | The corrected "reached him" rule branches on a display mode the session cannot observe. In the verdict's words, "the fix removed a false claim and installed an unevaluable condition". It is a rule-3 challenge to the briefing behind DA1. | `COMMUNICATION.md` § Asking for a ruling :229–234; `PROPAGATION.md:137`; template :49 | One branchless rule: account in a completed message, device in the next turn. | FLEET | Cycle OPEN | None (conditional still at HEAD) |
| 6 | **BA1** · BA (BW rulings applied) | The 2026-09-20 rewrite (`b2a54f1`) deleted the "dirty sibling state line is a stop" sentence, which had been ruled twice (BS1(c), BW4). It now points at CF3, whose branches cover the case in neither branch. | `CONCURRENCY.md` § On a split board :304–306; § Claiming at a dirty primary checkout (CF3) | One ruling folding `010/160` and `320/120`; put the operative sentence in CF3's branch list. | FLEET | Cycle OPEN; "the next move is the principal's" | No. Same defect rated MODERATE as **SG2** |
| 7 | **SK1** · SK (scratchpad clause) | Subagents inherit the orchestrator's scratchpad as something they can read. REVIEW rule 1 calls orchestrator-held deferral "the one arrangement that may honestly be called structural"; on this harness it is not. | `CONCURRENCY.md` § Orchestrated queue runs, scratch clause; `REVIEW.md:95` | Add a read-surface sentence; downgrade "structural" to "strong default with audit trail". | FLEET | Highest-stakes review shape; cycle OPEN | Practice changed (siblings moved out); the doctrine is unchanged |
| 8 | **HP1** · HP (harvestscan prefix filter) | The survivor index is rebuilt once per watched file, so the "bounded" pass is slower than the quadratic code it replaced: 248 s against 82 s on the hook plane. The exactness claim holds. | `tools/harvestscan.py:488` (verified) | Build the index once per scan; add a split-board-shaped count test. | FLEET (warn-only registry) | "invites `--no-verify`, which silences the whole floor"; cycle OPEN | None |
| 9 | **SW1** · SW (coldsweep) | `--also-exclude` with an absolute, `..`, wrong-case or typo'd path excludes nothing, while the provenance line claims it was excluded. | `tools/coldsweep.py` `_parts()` | Anchor absolute paths to root; normalise `..`; exit 2 when an entry matches zero files. | FLEET (REVIEW rule 2 mandates the tool) | "don't lean on rule 2 unqualified until SW1–SW3 land"; OPEN since 2026-08-17 | None; tool unchanged since `613132e` |
| 10 | **SW2** · SW | `--root` pointed at a subdirectory, or at a child whose `docs` lives elsewhere, bars zero files and still claims the bar applied. | `coldsweep.py` `BARRED`, `walk()` | Read the floor config's `docs` key; warn when the default bar matches nothing. | FLEET | Same rider | None |
| 11 | **SW3** · SW | Nested harness worktrees under `.claude/worktrees/` (596 files that should be barred by name) and gitignored material are searched. | `coldsweep.py` `walk()`/`NOISE` | Use a gitignore-aware file list, or skip `.claude/worktrees`. | FLEET | "live on this estate today" | None; **LW2** re-finds the class |
| 12 | **RF1** · RF (record pushed floor) | The reason given, "CI runs checks a local scan does not", contradicts the one-registry design. The real gap is when the scan ran and over which tree, plus paths the hook never covered. | `RECORD.md` § close all-clear (:121–124, verified) | Keep the rule; reword the reason to tree-state timing and hook-cover gaps. | FLEET | "a wrong why in doctrine propagates to every adopter who reads it" | None; unruled since 2026-07-26 |
| 13 | **CC1** · CC (ccmail build) | The delegation-first ruling left out two things: keyless delegation still reaches "any mailbox in the domain", and the route relies on the cloud CLI's plaintext refresh token. No route's exposure to a compromised session is stated. | ADR 0006 2026-09-09 addendum; `instruments/ccmail`; README; man page | Re-brief Mike; add a per-route compromise line to the controls list. | ATELIER-ONLY (instrument; sets precedent) | Rule-3 challenge to the briefing; cycle OPEN | None |
| 14 | **C5R1** · C5R (C5 term-list remeasure) | The C5 item's "sharpest cost" is mis-composed. One of the "six private children" is public, and about 90 % of the 58 lines are not the prescribed act. It also flags a false live-proven claim in a public child's session log. | Board `020/030`, cost argument | Restate the cost; count the public child's lines as true positives. | ATELIER-ONLY (informs a FLEET leakscan decision) | Raised to Mike "regardless of C5" | None |
| 15 | **C5R2** · C5R | The 2026-08-06 deletion precedent is misdescribed against its source ADR, which grounded the deletion on proportionality, not on a missing escape hatch. | `020/030`, precedent paragraph | Restate: the defect removed the narrow option; Mike then ruled on other grounds. | ATELIER-ONLY | "should not be re-litigated on the item's account of it" | None |

🚩 **One more MAJOR is ruled but not closed.** **ST3** (stampscan's template
markers carry `source=docs/method/PROPAGATION.md`, which cannot resolve in a
child). Mike ruled "FUND THE FIXES NOW" on 2026-08-04, but there is no
per-finding ST3 disposition, and it still stands as the bar on registry wiring
(`020/110`, `[ ]`). FV3 and FV11 (2026-09-25) lean on it.

---

## 3. MODERATE — unruled (101), grouped by surface

Columns: ID · pass · claim · counsel (≤15 words) · blast · overtaken.
"none" means no evidence of a fix or supersession was found at HEAD.

### 3.1 REVIEW.md and review tooling (coldsweep, reviewscan, queue pointers): 10

| ID · pass | Claim | Counsel | Blast | Overtaken? |
|---|---|---|---|---|
| RR2 · RR | Rule 4's off-tier orchestrator condition ("forms no finding") can only be attested, and nothing says which orchestrator acts count as judgement. | Put the orchestrator's reviewer-facing instructions in the verdict; name the allowed direction. | FLEET | None; precursor is A3 (2026-07-15) |
| SW4 · SW | The barred set exists only as a code tuple. Rule 2's prose bars only prior reviews, and the onramp's "read the SESSIONS tail" step collides with that bar. | Name the set once in rule 2; add a cold-session exception to the onramp. | FLEET | None |
| SW5 · SW | The provenance line and the `--include-barred` warning go to stdout after the hits, which breaks the pipeline contract. | Send diagnostics to stderr, warning first. | FLEET | None |
| SW6 · SW | An unreadable file is silently skipped and counted as swept. | Report the path; exit 2. | FLEET | None |
| SW8 · SW | The tool is named on no reviewer-facing surface except rule 2, and there is no story for running it in a child. | One line each in the review-brief skill, the reviews template and the README. | FLEET | None |
| SW11 · SW | `--include-barred` silently drops every `--also-exclude`. | Clear only the default bar; keep the extra excludes; say so. | FLEET | None |
| LW2 · LW | coldsweep computes its bar on the relative path, so a nested worktree's copy of a barred verdict prints as an ordinary hit. | Prune `.git`-file directories; bar `.claude/worktrees/*`. | FLEET (via rule 2) | None; same class as SW3 |
| LW1 · LW | `reviewscan` descends into a nested worktree and blocks the primary checkout's commit because of a sibling's draft brief (probed live). | Apply the same prune, or route through `filewalk`; add a test. | FLEET | None (`reviewscan.py:302,339`); re-found as **FW7** (minor) |
| SK4 · SK | The pass's own queue pointer instructs the reviewer, which breaks rule 4's refs-only ceiling. | Fix the wording; the landing session runs `pointerscan` on what it writes. | ATELIER-ONLY | No. pointerscan still flags `380:1`. In tension with the TR reconcile's reading that a lens hint is lawful |
| CH1 · CH | The channel's message classes have no fence against the review-independence rules, so an author can message a would-be cold reviewer. | Add an independence fence, or disclose every message. | FLEET | Queued at `280/040`, unruled |

### 3.2 CONCURRENCY.md: 10

| ID · pass | Claim | Counsel | Blast | Overtaken? |
|---|---|---|---|---|
| HF1 · HF | The sync-bookend prose says autostash parks a peer's work "onto a stash stack shared by … every worktree". Probed, that is false. The real harm, staged files coming back unstaged, is omitted. | Replace the mechanism clause with the measured behaviour; keep the gate. | FLEET | None (`:181–187`) |
| CH2 · CH | The new "ask" cue lets an empty peer list or no reply read as being alone. | Only a positive answer counts as a fact. | FLEET | None |
| CH3 · CH | Law 3's tie-break doesn't fix which tree it runs on or what a tie does (0–0 is usual), and the child's precondition was dropped. | Restore the precondition and add a tie rule. | FLEET | None |
| CH4 · CH | "Never `stash`" contradicts the mandated `git pull --rebase --autostash` at session start. | Reconcile the two rules. | FLEET | **Topically yes.** `320/210` FIXED 2026-09-18 gated the bookend (`:177`); does not cite CH4 |
| CH5 · CH | The "abridge before recording" rule lives only in the on-demand section, while the floor tells children to relay rulings across repos. That is a privacy gap. | Put the abridgement rule, or a pointer to it, in the floor sentence. | FLEET | None |
| SG2 · SG | The sweep deleted the only imperative statement of the dirty-sibling stop: "A rule asserted to stand has no sentence that states it." | One imperative sentence in CF3 until `010/160` is ruled. | FLEET | No. **Same defect as BA1 (MAJOR)** |
| SG3 · SG | The relaxation put to Mike says "dirty" but is true only for *unstaged* edits. A sibling's staged edit gets absorbed into the claim commit. | Change "dirty" to "unstaged" in three places before the ask. | FLEET | No. Same as **BA3** (minor) |
| SK2 · SK | The scratch clause justifies absolute paths by citing a cwd hazard in § Integration hygiene that is not there. | Land the hazard there, or drop the citation. | FLEET | None |
| TR1 · TR | Both run-open surfaces tell an off-tier session to leave every ⏳, omitting rule 4's off-tier orchestrator shape. | Add "or runs it in reviewer-plus-orchestrator shape, disclosed" on both surfaces. | FLEET | None; re-raises **RR5** (minor, unruled) and `320/320`(b) |
| TR3 · TR | The orchestrator seat's "does the job well" has no evidence test and no signal to hand up on. | Point at the verifiability test; name 2–3 seat signals. | FLEET | None |

### 3.3 PROPAGATION.md (membership, pointing-up, the stamped floor): 19

| ID · pass | Claim | Counsel | Blast | Overtaken? |
|---|---|---|---|---|
| CM1 · CM | "Every repo the principal works an agent in" annexes repos he does not own (upstream clones, forks, client repos). Met live at reconcile. | Bound it: "owns or controls". | FLEET | None (`:354`, verified) |
| CM2 · CM | A ruled exclusion has no recorded home. | Name the private estate-root repo as the home. | FLEET | None |
| CM3 · CM | Child-recorded exemptions have no estate-visible register or revisit trigger, and conflict with REVIEW step 4. | A fixed, greppable grammar; say which rule governs. | FLEET | None |
| RU2 · RU | The merge-time no-harm check is done by eye; two occurrences already trip the escalation ladder. | Write the check as a command; queue a branch/title lint. | FLEET | ≈ **NP2** |
| RU3 · RU | A hand-up that adds an item goes DIRTY (conflicting) once `main` moves, and no doctrine names the fix. | One sentence: merge `main` in and rebuild; don't rebase. | FLEET | Instance being landed on unmerged `qr-land-handups`; the rule is unchanged |
| RU4 · RU | "An atelier session that finds one lands it" has no trigger; 11 PRs stood open for three weeks. | Add `gh pr list` (open hand-ups) to the session-start read. | ATELIER-ONLY in effect | **Worse:** 8 report PRs open on 2026-10-03 |
| RU5 · RU | The duty binds "every repo", but all three filing shapes assume the estate; a plugin-only adopter cannot comply. | Name fork+PR or an issue, or narrow the sentence to the estate. | FLEET | None |
| RU6 · RU | `SECURITY.md` routes a vulnerability-class doctrine defect privately; § The duty routes it publicly. Neither names the other. | Security-class defects go private first; the public item lands with the fix. | FLEET | None |
| RU7 · RU | § The instance names a child the forge reports as PRIVATE, with no ruling behind it. | Apply `320/330` option (a): "a private child". | FLEET (by location) | No. = **PV2**, **NP8**; `320/330` open |
| RU12 · RU (reconcile) | A hand-up's item number is allocated on the child's base, so collisions only show at merge. | Run `board.py check` on landing; treat numbers as provisional. | FLEET | None; **NP7 disputes** RU12's collision count |
| NP1 · NP | The bullets say "no repo token", but rule 2 also forbids hosts, clients and secrets. The applier narrowed Mike's "rule 2 wins, everywhere". | Widen to token, host, client, secret; name slug and filename. | FLEET | None (`:532,593`) |
| NP2 · NP | The precedence is prose-only on all four surfaces, and the failure has recurred at least three times. | A pre-push term-list check, or state that the surfaces are unwatched. | FLEET | None; ≈ RU2 |
| NP6 · NP | The safety floor's pointing-up bullet lacks the class rule and the precedence, and blockscan missed the `###` edit. | One clause in the bullet; map blockscan per `###`. | FLEET | Floor half = **RU1 (MAJOR)**; guard half in flight (`320/340`) |
| PV1 · PV | "The house had no gap" was falsified by the PU-1 correction, and PROPAGATION and CONCURRENCY now disagree about one event. | Reword both: the house prescribed a path-blind command. | FLEET | None (`:647`; CONCURRENCY `:119`) |
| AK1 · AK | The stamped Asking bullet's five-item list closes a list the apex leaves open (six items plus "any other consideration"). | Add the catch-all to both copies in one commit. | FLEET | None (`:140`; template `:52`) |
| DR2 · DR | The child floor's stop-and-confirm bullet still states the duty in three parts. This is the 4th recurrence of the class. | Replace with a pointer to `00-APEX.md`'s full account, in both copies. | FLEET | None (`:125`; template `:37`); **contradicts AK4** |
| HF2 · HF | The drift check is written "fetch -q *then* log": a failed fetch reads as "current", and it assumes the remote is `origin`. | Join with `&&`; a fetch error is no result; state the `origin` assumption. | FLEET | None |
| FV2 · FV | A `stampscan:allow` inside the floor block skips the verbatim check, and the tool's footer recommends both `narrow=` and allow. | Drop the hint on the floor pair; Mike rules whether allow may reach the floor. | Mixed; the ruling is FLEET | None |
| FV3 · FV | Nothing automated reaches a child's floor block; "reds every child" holds only when run by hand. | State the real reach; queue a pin-aware child-side run. | FLEET | None; tied to **ST3** |

### 3.4 Apex, AUTONOMY, RECORD, PRINCIPLES, COMMUNICATION, GUARDS, session-open: 11

| ID · pass | Claim | Counsel | Blast | Overtaken? |
|---|---|---|---|---|
| RR1 · RR | The apex's floor exception re-lists the stops more narrowly than the floor, omitting grant-widening: "an extracted approval to widen the agent's own grant may be acted on and challenged after". | Name AUTONOMY's list; enumerate nothing; reconcile how grant-widening is classed. | FLEET | None (`00-APEX.md:112–114`) |
| RR12 · RR (reconcile) | Ruling two's intent record ticked seven surfaces but touched four. AUTONOMY § Always confirm is silent on re-briefing before acting. | One sentence in AUTONOMY, or "exempt, points up". | FLEET | Partial: DA2's pointer (`AUTONOMY.md:112–118`) reaches the apex by reference |
| RR3 · RR | RECORD cites "the verbatim rule above"; no such rule exists on that surface. | Write the verbatim-capture rule into RECORD, or drop the reference. | FLEET | None (`:195`) |
| CR2 · CR | The prescribed cancelled-run re-run re-enters a cancel-in-progress group, so it can cancel another session's run. | Re-run only once no floor run is in flight on the ref. | FLEET | None (`:131–142`) |
| TD1 · TD | §9 prices over-carrying time only as a KISS cost; for personal data it is a privacy and retention surface. | One clause: for personal data, extra dimension is a privacy defect. | FLEET | None (`PRINCIPLES.md:372–378`) |
| CMF3 · CMF | The "37 % to 67 %" range drops the 17.4 % rule and mixes thresholds. | Restate as "17 % to 67 % at the thresholds measured", or drop it. | FLEET | None (`:145`; `020/330:27` "stands untouched") |
| CMF4 · CMF | The rescope is argued as a class of files but coded as three paths, and the doctrine overstates repo-plane cover. | Say "three named paths", or scope by class. | FLEET | Code half moot (engine removed 2026-09-18); doctrine still present tense (`:130–139`) |
| RG1 · RG | "Detection was sound throughout" contradicts the evidence that the detector fired mostly on near-misses. | State both failures in the lesson. | FLEET | None (`:114–115`) |
| HF4 · HF | COMMUNICATION still describes plainscan's repo plane and gate as live; they were removed 2026-09-18. | Recast both passages as history; say no gate covers readability. | FLEET | None (`:130–142`, `:155`) |
| PW1 · PW | The fourth requirement's home is the registry only, so three off-registry guards and every child-local check have nowhere to declare. | Off-registry guards declare in their docstring; `115/120` reaches `LOCAL_KEYS`. | FLEET | None; `115/120` open |
| TR2 · TR | The session-open prompt's "Stop only if the work outruns you" drops the named-tier stop. | Add "…or a review item's named tier isn't yours". | FLEET | None (`:24`) |

### 3.5 ADR 0008 and floor scanners (`tools/`): 20

| ID · pass | Claim | Counsel | Blast | Overtaken? |
|---|---|---|---|---|
| AR2 · AR | floorfleet's boundary row says the ruleset blocks force-push without reading the bypass actors, and cites the stale sentence. | Read `rulesets/{id}`; print the bypass. | ATELIER-ONLY | None |
| AR3 · AR | AP4's terms-path check misses three neighbours: an empty file passes under `--require-terms`, a directory gives a traceback, an empty env var falls back silently. | Refuse empty values; `OSError` → exit 2; pin all 4 cases. | FLEET | None (lineage EP3 → AP4 → AR3) |
| RC2 · RC | The URL carve-out hides a bare token in the userinfo position. It blocked before 2026-09-18 and is now green fleet-wide. | Never exclude userinfo; add a test and a selftest case. | FLEET | None (`secretscan.py:497–513`) |
| RC3 · RC | `conflictscan --staged` reports wrong line offsets and keeps a trailing tab (the `320/290` defect re-created the same day); leakscan too. | Lift secretscan's hunk counter, or single-source the parser. | FLEET | None |
| BL1 · BL | date/spell/wrapscan stop reading a line after 8 KiB, so a finding past that point exits 0, and `--json` is silent. | Overlapping windows or fail closed; add `lines_truncated` to JSON. | FLEET | None |
| BL2 · BL | The hook plane is not bounded: `--staged` buffers the whole diff, so CHANGELOG's "every guard … bounded" overclaims. | Stream the staged diff; scope the CHANGELOG claim. | FLEET | None (`CHANGELOG.md:9`) |
| SP1 · SP | secretscan's window-seam dedupe is wrong both ways: it double-lists tokens and collapses distinct ones. | Always add to the seen-set; key on absolute offset. | FLEET | None; = **BL3** (minor) in leakscan |
| SP2 · SP | An unreadable file now scans clean (exit 0), and the comment "matches the old behaviour" is false. | Count `files_unreadable`; exit 2; add a chmod-000 test. | FLEET | None; same class as FW8, SP11 |
| SP3 · SP | The 50k finding cap is charged before dedupe and allow-marker subtraction, with one budget for advisory and blocking. A blocking finding can be listed nowhere. | Separate blocking budget; charge the cap after subtraction. | FLEET | None |
| SP4 · SP | No test exercises the window seam or the cap. | Seam and cap fixtures through `main --json`. | FLEET (indirect) | None; ≈ FW3, LW8 |
| FW1 · FW | On Python before 3.14, the walk's `.git` check raises PermissionError, and all 11 guards die with a traceback. | `try/except OSError`; give `os.walk` an `onerror`. | FLEET | None; routed to `115/080` pt 2 (adjacent: in-flight `115/210`) |
| FW3 · FW | No test imports `filewalk`. | Build `test_filewalk` from the ledger fixture. | FLEET (indirect) | None; = **LW8** (rated a note) |
| FW8 · FW | 7 of 11 guards silently skip an unreadable file and report clean, while 4 exit 2. | Count `files_unreadable` everywhere; rule exit 2 per guard. | FLEET | None |
| FV1 · FV | stampscan identifies the floor by spelling, not by file: four respellings let a narrowed floor pass clean. | Compare resolved paths; test all four spellings. | ATELIER-ONLY mechanism (enforces a FLEET rule) | None (`:362`) |
| PW2 · PW | The leakscan and secretscan headers now say "declared", but their bodies still list three bullets. | Add a fourth bullet, or revert the header. | FLEET (text) | None |
| PG1 · PG | The pointerscan docstring says it "reads staged content honestly"; it reads the working tree. | One-sentence fix, or a `--staged` mode. | FLEET | None (`:127`) |
| AB1 · AB | The E3 fingerprint carve-out reaches credential-keyed values, which "regressed from blocking". The "unreachable" test is refuted and the ruled scope exceeded. | Exclude credential-keyed lines, demote to advisory, or pin as a canary. | FLEET | None (named a standout at `150/README:16`) |
| LK1 · LK | A malformed scoped allow-marker re-parses as the unscoped form and exempts every structural rule. The reviewer argues it is MAJOR. | Fail closed; add two canaries. | FLEET | None (`leakscan.py:107–114`) |
| BG3 · BG | "Passes wrapscan in any repo" is true of today's data, not by design: an allow-marked line renders to 187 columns. | Exempt generated files, or wrapscan the generated output in a selftest. | FLEET | None; "needs Mike's own answer" |
| BG4 · BG | The corrections never reached `tools/README`, CHANGELOG or the `board.py` docstring (stale `$ATELIER_TOOLS` spelling). | Sweep all three files. | FLEET | Partly: README:103 still stale; class recurs as BW5, PT3 |

### 3.6 Board tool and board content: 13

| ID · pass | Claim | Counsel | Blast | Overtaken? |
|---|---|---|---|---|
| BA2 · BA | `ls-files` quotes non-ASCII paths, so a macron-named item drops out of `rebuild --from-index` and the hook passes. | `ls-files -z`; add a macron test. | FLEET | None (`board.py:406`); = **SG1** |
| SG1 · SG | The same defect, also present in `harvestscan.list_markdown`. | One shared `-z` helper. | FLEET | = BA2 |
| BS2 · BS | The index projects the first physical line: 52 of 124 titles are fragments, and claims or flags on continuation lines vanish. | Project the logical line; add a realistic fixture. | FLEET | Partly mitigated (`index_title` strips the claim) |
| BS3 · BS | 58 non-checkbox bullets (17 🎯, 1 ⏳) became section-README narrative the index cannot see. | Promote them to items, or render README ⏳/🎯 lines. | ATELIER-ONLY | None |
| BS4 · BS | Nothing bounds the index's size, and sizescan's remedy still says "harvest to ROADMAP-DONE". | A decided bound plus a split-board remedy string. | FLEET | None (`sizescan.py:309`) |
| BS5 · BS | The legend and claim rules moved off the onramp read into a linked file. | Name the board README in the read order. | ATELIER-ONLY | None |
| LR1 · LR | Open item `160/140` still tells children to adopt a "three-element floor". | Reword to two elements; add open items to the sweep. | ATELIER-ONLY | None |
| LR3 · LR | An open item Mike wrote was deleted rather than closed. | Close it as fixed by `1b46d05`; rule that removal closes, never deletes. | ATELIER-ONLY | **On its face, yes** (`1b46d05`); needs Mike's confirmation |
| LR4 · LR | "Children shed the Laws sentence at their next pin bump" is stated as fact; 13 of 17 children still carry it. | Make the claim honest; add a read-only floor-block match check. | ATELIER surface, FLEET drift | None (`CHANGELOG.md:292`) |
| C5R3 · C5R | A coined paraphrase sits in quotation marks, and a second item cites it (a testimony loop). | Strip the quote marks; attribute to the ADR. | ATELIER-ONLY | None |
| C5R4 · C5R | Every atelier-side figure went stale within hours. | Rule on classes and mechanisms, never on frozen numbers. | ATELIER-ONLY | None |
| C5R5 · C5R | Option 1 puts scope grants in an unversioned, unreviewable machine-local term list. | Give them a versioned home (the estate root) and a validation path. | FLEET (if built) | None |
| C5R6 · C5R | Option 1's scope entry silently pre-decides the unruled standing-gap question. | Put both to Mike as one ruling. | ATELIER-ONLY | Board repeats "the two are one ruling" |

### 3.7 Skills and plugin: 3

| ID · pass | Claim | Counsel | Blast | Overtaken? |
|---|---|---|---|---|
| AK2 · AK | The `session-onramp` skill inlines its own apex and floor, lacks the informed-confirmation text and the Asking bullet, and no scanner reads it. | Stamp §2 from the block, or reduce §§1–2 to pointers. | FLEET | None; same class as RR8/AA9 |
| HF3 · HF | The drift/sync fix never reached the create-repo skill (`..HEAD`), queue-run `:49` or `pins.py:300`; `030/110` is unlinked. | One item fixing both skills and `pins.py`; close `030/110`. | FLEET (skills) | None |
| SK3 · SK | "The dispatch prompt says so", but no dispatch surface carries it. | One sentence in queue-run skill step 5, plus the recipe. | FLEET | None |

### 3.8 Instruments and parent-side tools: 8 (all ATELIER-ONLY)

| ID · pass | Claim | Counsel | Overtaken? |
|---|---|---|---|
| CS1 · CS | `--regex` pre-filters on raw JSON, so patterns containing quotes, backslashes or anchors never match, and the man-page workaround fails. "0 hits" reads as absence. | Skip the pre-filter for those classes; correct NOTES; add tests. | None |
| CS2 · CS | `--search` with no term prints a whole transcript and exits 0. | Set from the flag's presence; test the trailing case. | None (`:127–128`) |
| CS3 · CS | There is no threat enumeration, and no warning that output is private transcript content. | A NOTES paragraph plus a README sentence: shapes and counts, never excerpts. | None |
| CC2 · CC | Attachments are written with modes 755/644, with no retention rule and no documented clear. | Use 0700/0600; document a clear; add a retention line. | None |
| CC3 · CC | No threat enumeration was done before the build. | A threat list in the ADR for credential or untrusted-input instruments. | None |
| CC4 · CC | `ccpdf` has no bitmap cap and no sandbox: 104 s and 4.4 GB, then an out-of-memory kill. | Refuse above a pixel budget; consider `sandbox-exec`. | None |
| CC10 · CC | Both ccmail routes were down on 2026-09-26, so no session could open an attachment. 🎯 This needs Mike. | Mike runs `ccmail --auth` and/or refreshes the cloud login. | Not re-checked (would need a live call) |
| FF1 · FF | `floorfleet --remote` with `gh` missing gives a traceback; the contract says exit 2. | Catch `OSError` at the three `gh` call sites. | None |

### 3.9 Records and privacy: 2

| ID · pass | Claim | Counsel | Blast | Overtaken? |
|---|---|---|---|---|
| FF4 · FF | The earlier FS verdict on public `main` names four private children next to their red state. That is a name × posture join, the fourth instance. | Rewrite classes-only; tally it as the 4th instance. | ATELIER-ONLY (public exposure) | None (`2026-07-29-1251…:120–121`) |
| CR1 · CR | The decision's grounds cite saved metered minutes, but this public repo's runs are free. | Re-ground on ECONOMICS' hygiene-regardless-of-meter rule. | ATELIER-ONLY | None |

### 3.10 Moot under the 2026-09-18 "destroy the hook, archive the engine" ruling: 5

CMF2, CMF5, CMF6, RG2 and RG3 concern `tools/hooks/plain-reply.py` and plainscan.
Both were deleted 2026-09-18 (`020/360`). The board box "close RG3, CMF2, CMF6,
CMF8, BG14 as moot" at `290/070:49–51` is still `[ ]`. **One tick closes them.**

---

## 4. Minor and note gists for unruled and partly-ruled files

Counts are of unruled findings only.

| Pass (file) | m/n | What the minors and notes cluster around |
|---|---|---|
| AA1–5 (07-26 apex-accountability) | 3/2 | Apex wording precision: the grounds-not-gate guard, half-applied RASCI, two roots of authority, "every running cost", the liability register. AA1's evidence was undercut by the Laws removal (LR9). |
| EE (07-26 escalation rung) | 3/3 | A missing "blocked but source exists" ground; the beside-the-ladder model against the REACH and ECONOMICS ladders; no hand-up pointer; a cited ban with no home; the quote is not verbatim. |
| WO (07-26 way-out) | 3/2 | The REACH citation is misattributed; there is no "stated exit" requirement; it collides with §2's adopt-outright clause; the retrofit claim is unproven; the exit is an attack surface. |
| RF (07-26 pushed floor) | 4/0 | The "pending" state has no durable home; no named way to observe the run; "floor at head" is undefined for trimmed-floor children; "floor" clashes with the glossary. |
| PG (08-05 pointer grammar) | 1/5 | A line-1 kill switch; then the steering net, residue recurrence, boilerplate masking a deletion, two-parser marker drift, and a net-line gate blind to short deletions. |
| FF (08-05 FS application) | 0/2 | The `unknown` state covers two different kinds of not-knowing; mixed planes in one board row. |
| MT (08-05 mid-tier) | 0/3 | Promotion provenance (sound); "well-floored" has no pre-dispatch test; a section reference retargeted inside a merge. |
| EA (08-05 E6 application) | 0/3 | TOTP `*_seed` keys are missing from `SECRET_KEY_RX`; the standalone test import fails; the EI4 correction sits only in the recap. |
| LB (08-05 landing=bookkeeping) | 0/2 | The inline-claim clause is unenforced; the `[x]` legend leaves "archive-only" implied. |
| SE (08-05 five edits) | 0/2 | The sweep baseline is verified clean; the tier bar now lives on three surfaces. |
| GA (08-05 F1 guards) | 1/2 | GA1: ten copies of the reason loader. Funded via `115/080` on 2026-09-20, but no ruling is recorded. The notes cover a historical mention blocking at the hook, and a suppressed set reachable only by grep. |
| C5R (08-09) | 3/3 | Census method, option-2 figures transposed, the GUARDS grant-date half; C5R10 (a path can't carry a marker, **contradicts LK6**), the option-4 tension, the frozen-record marker edge. |
| CM (08-09 membership) | 5/5 | Edges of the queue lane: "answerable" overclaims, the lane dead-ends at an unwired child, visibility crosses without warning, practice is stricter than the rule. Notes: ADR grey band, unattributed quote, glossary entry. |
| TD (08-09 §9 time) | 1/1 | "Never reached" overstates against §6; record time bundles three clocks. |
| CR (08-09 cancelled run) | 1/3 | The config claim is stated unconditionally in inherited doctrine; positive phrasing; a ~90 s vs 101 s discrepancy. |
| AB (08-09 E6b/E3) | 2/3 | A "never shrinks" docstring that is false; fingerprint suppressions counted but not located; tally semantics; softening channels silent on the board. |
| LK (08-09 E7 leakscan) | 2/3 | No NFC normalisation (macrons); `/` and `+` missing from the separator class; a cwd-fragile test; an ignore glob disables term cover; a path self-exempts via marker text. Also one un-ID'd G2 reach note. |
| BS (BS2–14) | 5/4 | Test counts; `board` missing from the floor docstring pin; the ADR missing from the index; `rebuild` overwrites a hand-kept board; code-span glyphs lifted as flags. Notes include BS10 (private names with counts). |
| LR (08-15 Laws removal) | 2/4 | LR2 was fixed in `c782e14`. LR5's "within the agent's own safety values" is still absent from the apex. Pointer overlap; the paraphrase that caused LR3. |
| CS (08-15 cctranscript) | 6/5 | The timing figure didn't reproduce; `--utc` shifts `--since`; astral characters are missed; the tally ignores the window; subagent logs fall outside the search, unstated; `--list` crashes on EACCES. |
| CMF (unruled part) | 2/2 | CMF7 bookkeeping (pointer late, no CHANGELOG entry); CMF8 hook defects (moot); grounding source unverifiable; verified claims. |
| RG (unruled part) | 3/2 | RG5's "roughly a third" (the reconcile half-disproves it and recommends a note); RG6 docstring (moot); RG7 no CHANGELOG entry; RG8 leftover state file; RG9 stale item. |
| AA6–13 (08-17 authority) | 2/4 | AA8: the challenge path covers only rulings the agent asked for. AA9: the onramp skill lacks the authority sentence (= RR8, AK2 class). AA12: the child floor omits the waiver. AA13: unmet (RR12). |
| BG (unruled part) | 4/6 | Stale child guidance in item 030; plainscan fired on the index; a tautological home-directory test; a subdirectory run exits 0 silently; dead `GENERATED_MARKS`; BG11 names private children. |
| CH (08-17 channel) | 11/4 | CH6 takes a position on `030/140`; a miscount, half-stated git commands, a wrong floor pointer, the channel never defined, no CHANGELOG entry; loose restatements; the child's post-commit check was not extracted. |
| SW (08-17 coldsweep) | 2/1 | Test and selftest gaps; the intent record must be excluded by hand (fired live in the BG pass); docstring overclaims. |
| RR (08-17 ruling round) | 5/5 | The GUARDS "rule with no home" grounding is overstated; "orchestrator" names two roles (RR5, re-raised by TR1); the apex's "But" reads against the wrong sentence; RR8 = AA9 = the AK2 class. |
| RP (design) | 0/1 | RP8's transcript-report counsel is unfunded; largely moot since the engine was archived. |
| **0925 batch** | | |
| AR | 2/2 | ADR 0008's `review:` line is stale; the pin test cites a non-existent sentence; AP3 residue (`--end-of-options`); AR7(a) = RC10. |
| BA | 4/2 | "Dirty" vs "unstaged"; the `--rebuild` spelling regressed; no CHANGELOG entry; the 2026-09-20 run record is missing; five surfaces restate the whole mechanism. |
| DR | 1/6 | The scaling clause is a second original; an archived grounding instrument; wrapscan passed 87 columns; subagents have no device; the "verbatim" quote is only the tail of the steer. |
| PV | 3/1 | PU-2's "stands unchanged" is the seam with `320/330`; no CHANGELOG entry; the PU-2 grounds are the applier's, written in the ruling's voice. |
| AK | 1/4 | The no-device clause was dropped; blockscan double-fires (AK4, **contradicts DR2**); the rule says how to ask, not whether; the list's provenance is paraphrase. |
| RU | 3/1 | "Nine findings" is stale; no board section for atelier's own reports; step 1 lacks a format pointer. |
| HF | 6/2 | Gate 2's reason is wrong; the bookend fails in a new worktree (no upstream); verify-the-act is unscoped and absent from the child block; hand-up mechanism claims entered doctrine untested. |
| RC | 6/6 | The RC4 gap is documentation only; Unicode line separators fool the floorfleet lexer; a bare `rebuild` runs a check; a `++ ` line forges a header; plural-rule misses; symlink following. |
| TR | 6/2 | "Role check" residue; the REVIEW intro miscites rule 4; no tier check at ⏳ selection; the ECONOMICS:47 clause; the record rounds three up to "all four". |
| FV | 4/4 | "Three boundaries" heads four bullets; doctrine and scanner key on different things; child-facing surfaces lack the rule; the fleet leg was closed on a one-off measurement. |
| SP | 5/2 | pathscan declared roots: type validation, a lexical-only escape check, an unbounded per-file read, roots missing from the README. SP11: two unreadable-file contracts exist. |
| NP | 4/3 | `HHMM` has no stated frame; re-filings should cite the item; an asymmetry the applier introduced; a closed `320/190` hides an unruled question; the collision count is wrong. |
| BL | 6/5 | Overlap double-reporting (= SP1a); bounds documented for one tool; memprobe fails open on unknown arguments; fitted ceilings; 60 s ceilings go red under load. |
| SK | 3/3 | A redundant provenance paragraph; "per-project" should be per-user; the orchestrator wrote to the scratch root; the brief's sweep didn't bar everything. |
| SG | 6/3 | Unmerged and intent-to-add entries misdiagnosed; locale decoding; a git failure reads as "no board"; three items ask about one CF3 clause; the eleven-vs-ten test count. |
| HP | 5/3 | Wall-clock ceilings; the bucket bound is overstated; the `ceil` is exact only at 0.6; a dash-led `--against` (CWE-88); an empty intent record. |
| LW | 5/3 | pointerscan has the same walk; submodule pruning is untested; the skip is undocumented; landing-record overclaims; a false intent premise never put to Mike. |
| FW | 5/5 | No README entry; nine stale "copyable alone" claims; skip-set iterator hazard; FW7 = LW1; an empty intent record; design notes handed to `115/080` and `115/220`. |
| CC | 6/2 | Symlinks followed, no `realpath`, unvalidated message id; same-name overwrites; man page vs behaviour; no `state`/PKCE; the record contradicts its body. |
| PW | 5/3 | An eighth unswept copy (`method/README:86`); post-ruling guards declare nothing; "declared" means two things; the two limits are spelled differently. |

---

## 5. Clusters: one ruling disposes of several findings

| # | Cluster | IDs | One ruling that would settle it |
|---|---|---|---|
| C1 | **CF3 dirty-sibling stop** | BA1 (M), SG2, SG3, BA3, SG8, SG10, SG12; board `010/160`, `320/120`, `030/140` | Rule `010/160` once and restore the operative sentence in CF3, worded "unstaged" not "dirty" |
| C2 | **ADR 0008 control clause** | AR1 (M), AR8 (M), AR2, AR4, AR5; `140/020`, `115/180` | Re-brief AP1 against the live ruleset and pick which ruling stands, then amend the ADR |
| C3 | **Rule-3 challenges to a briefing** (re-brief owed) | AR8, CC1, DR1 | One re-briefing sitting covering all three |
| C4 | **Staged-diff parser** | RC1 (M), RC3, BL2, RC8 | Single-source `staged_added_lines` with forced prefixes and streaming (`115/080` pts 2–3) |
| C5 | **"Unreadable file is a clean pass"** | SP2, FW8, SW6, SP11, FW13; FW1 adjacent | One contract for every guard: count `files_unreadable` and exit 2 |
| C6 | **Nested worktree walking** | LW1, LW2, SW3 (M), FW7, LW3 | Route every walker, including coldsweep, through `filewalk` with a `.git`-file prune |
| C7 | **coldsweep defects** | SW1–SW3 (M), SW4–6, SW8, SW11, LW2, SK9 | Fund one coldsweep fix item; SW4's doctrine half rides with it |
| C8 | **Missing tests on shared mechanisms** | FW3, SP4, LW8 | Fund `test_filewalk` plus secretscan seam/cap fixtures together |
| C9 | **Pointing-up naming / class rule** | RU1 (M), NP6, NP1, NP2, RU2, RU7, PV2, NP8; `320/330` | Rule `320/330` and the floor clause together |
| C10 | **Parent's half of hand-ups** | RU3, RU4, RU12 (count disputed by NP7) | One paragraph: merge-not-rebase, provisional numbers, open-PR check at session start |
| C11 | **Child floor and onramp restatement drift** | DR2, AK1, AK2, RR1, RR12, RR8/AA9, PW3, HF2 | Pointer-ise the floor and stamp or point the onramp skill in one commit |
| C12 | **COMMUNICATION after plainscan's removal** | HF4, CMF3, CMF4, RG1, RC12, DR4 | One history-recasting sweep of COMMUNICATION |
| C13 | **Plain-reply hook, moot set** | CMF2, CMF5, CMF6, RG2, RG3, RG6, RG8, RG9, CMF8, BG14, RP1–RP5 | Tick `290/070:49–51` "close as moot" |
| C14 | **Private name × posture in public records** | FF4, C5R1, C5R4, CM7, CM8, BS10, BG11; RU7 | A classes-only sweep under `030/070` |
| C15 | **Off-tier orchestrator** | RR2, RR5, TR1, TR2, TR3; `320/320` | One rule-4 orchestrator ruling |
| C16 | **RECORD close and floor sub-points** | RF1 (M), RF2–5, CR2, CR3–6 | One RECORD § all-clear rewrite |
| C17 | **C5 term-list** | C5R1–C5R12 | The board already says option 1 and the standing gap are "one ruling" |
| C18 | **Apex authority wording** | AA1–5, AA8–13, RR1, RR12, LR5 | One apex wording pass |
| C19 | **Board generator** | BS2–BS5, BG3, BG4, BG5–13, BA2/SG1 | One `board.py` fix item; BG3 needs Mike's own answer |

---

## 6. Overtaken or partly overtaken: evidence

- **LR3**: `1b46d05` restored and closed the item. The verdict at L247 says "on its face, `1b46d05` resolves LR3", and `215:13–14` says Mike's confirmation is needed.
- **CH4**: `320/210` "FIXED 2026-09-18" gated the session-start autostash (`CONCURRENCY.md:177`). It does not cite CH4.
- **CMF2, CMF5, CMF6, RG2, RG3** (and minors RG6, RG8, RG9, CMF8, BG14, RP1–5): the hook and engine were deleted 2026-09-18 (`020/360`). `290/070:49–51` is unticked.
- **CMF4**: the code half is moot; the doctrine half is still present tense at `COMMUNICATION.md:130–139`.
- **BG1 (ruled)**: substantially fixed by `1b3ba12` (2026-08-24, via `010/150`), but `290/060` still reads "FUNDED, untaken". BG2's third resolution branch is still missing.
- **BS2**: partly mitigated, since `index_title` now strips the claim (`board.py:196–205`). The state and flags still come from the first physical line.
- **RR12**: partial. DA2's pointer change landed at `AUTONOMY.md:112–118`, but no record says RR12 was addressed.
- **SK1**: practice only. Siblings were moved out of the scratchpad mid-batch, but REVIEW.md:95 still says "structural".
- **RU3**: the instance is being fixed. PRs 84–93 are being landed on the unmerged `qr-land-handups` branch; the rule is unchanged.
- **RU1 / NP6, guard half**: `320/340` was claimed 2026-10-03 (`qr-blockscan-unmapped`, unmerged `bd09b1b`). Whether it covers `###` subsections is unverified.
- **IR5** (MODERATE): fixed inside the pass by the reviewer (`interruption-resilience:245`). Mike never ruled it.
- **lean-files F1/F2/F4**: fixed per `CHANGELOG.md:1938–1958`; who ruled them is unnamed. F3 was ruled by Mike.
- **Stale "await ruling" lines**: `200/README:108` (pathscan) and `:131` (stampscan). Both were ruled 2026-08-04.
- **Stale file headers**: the BS verdict L6 still says "BRIEF WRITTEN, REVIEW NOT RUN"; RP L9 still says "RUNNING"; `290/070:40` is unticked though `:57` records the ruling.
- **No HEAD fix** was found for any other unruled finding in the 0925 batch. No commit since `c1a2f12` (2026-09-21) touches a cited surface.

---

## 7. Flags for the ruling sitting

- 🚩 **Two conflicting Mike rulings on AP1**: 2026-08-09 ("ruleset with owner bypass, plus a machine-check", applied) against 2026-08-23 ("re-word to the truth … not enabled"). AR8 is exactly this.
- 🚩 **The same defect is rated differently by two passes.** Rule each pair once:

  | Defect | Lower rating | Higher rating |
  |---|---|---|
  | Dirty-sibling stop | SG2, MODERATE | **BA1, MAJOR** |
  | Floor naming clause | NP6, MODERATE | **RU1, MAJOR** |
  | reviewscan nested walk | FW7, minor | **LW1, MODERATE** |
  | No `test_filewalk` | LW8, note | **FW3, MODERATE** |
  | "Dirty" vs "unstaged" | BA3, minor | **SG3, MODERATE** |
  | Overlap double-report | BL3, minor | **SP1a, MODERATE** |

- 🚩 **Contradictions between findings:**
  - DR2 (blockscan's stop-and-confirm red is genuine) vs AK4 (a coarse false positive needing an allow marker).
  - C5R10 vs LK6.
  - SK4 vs the TR reconcile ("lens hint lawful").
- 🤔 **Code passes are queued as "principal's to decide"**: RC, BL, HP, LW, SP, FW. Their briefs carry no rule-3 clause, and REVIEW step 4 allows `[rejected: grounds]` for ordinary code. One class ruling could hand the pure-code findings back to the builder.
- 🤔 **The 16 author-disposed files were never put to Mike.** All their MAJOR and MODERATE findings are tagged `[fixed]`, and most are verified later. The files:
  - 14 from 2026-07-10 to 07-12: foundation, create-repo, linkscan, method-layer, post-method, child-ci, put-away, instruments, plugin, principles-8, communication, reach, record-private, signing.
  - Plus datescan and spellscan (code; the flips were ruled).

  The pre-rule-3 MAJORs among them are create-repo C1–C2, post-method B1/B2/B14, instruments 1–3, record-private R1–R2 and signing G1–G3. It is an open question whether to ratify them en bloc.
- **Other counting anomalies:**
  - PT's Overall was never restated after its reconcile (the final count is 1/3/3/4).
  - The IR heading at L85 says "2 MEDIUM"; the final count is 3.
  - concurrency-claiming-work says "four MEDIUM" but five are labelled.
  - method-layer says 13 dispositions, but its table has 14 rows.
  - TR8 is called a "wording note" yet tallied as minor.
  - FW says its cycle "may close once the rulings are recorded", while the board says it CLOSES.
- 🚩 **A private child's repo name appears verbatim** in this public repo: in the PU pointer (`160/280:12`) and in PV5's reconcile (L482–484). It is grounded in Mike's PU-2 ruling, which `320/330` now contests. Not reproduced here.
- 🚩 **The AA7 ruling is applied incompletely.** RR12 found AUTONOMY untouched, and AA13 is unmet.
- **A peer queue run is in flight** (`306c7c2`): stampscan cover, pathscan false positives, blockscan unmapped headings, ccarchive shrink, the cctranscript pool, and the `115/210` interpreter contract. `115/210` is adjacent to FW1. The run could overtake parts of RU1/NP6 (guard half), FV1–3 and BG3; check before ruling.
- ⏳ **The FS1 reviewer's token** (FLOORFLEET_TOKEN, all-repos grant) **expires 2026-10-27**, per `030/README:149`. Renewing it is a human step.
