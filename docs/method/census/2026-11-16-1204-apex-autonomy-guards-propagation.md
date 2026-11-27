# Enforcement census — APEX, AUTONOMY, GUARDS, PROPAGATION

Board item `020/220`, slice 2 of the census. Run 2026-11-16 (UTC) by a worker
of queue run 78ca. This is a measurement record, not doctrine: it changes no
rule, and it builds no guard. It uses slice 1's method, states and row format
(`docs/method/census/2026-11-16-1142-record-review-concurrency.md`) so the two
slices add up.

## What this asks

For each rule in four governing documents: if it is broken, what sees it? Each
rule gets one state, defined as in slice 1.

- **enforced**: a mechanical check reads the breach. The row names the check,
  the plane it runs on (the pre-commit hook, the commit-message hook, CI, a
  harness hook) and whether it **blocks** or **warns**. *partial* means the
  check covers some of the rule and the rest is unguarded.
- **directive-only**: nothing mechanical sees a breach. Where a self-run
  instrument would report it if a session chose to run it (`ccclose`,
  `pins.py`, `flipcheck.py`, `floorfleet.py`), the row says *instrument* and
  the state stays directive-only: nothing invokes those tools, so nothing sees
  the breach unless the breaker looks.
- **unenforceable, accepted**: the fact that would license or condemn the act
  is outside any check's evidence window (`GUARDS.md` § *Before building a
  check: the evidence window*), and the reason is stated. Accepted as of
  2026-11-16.

A directive-only rule also gets the place its breach could be seen:

- **diff**: the breach is in the committed change itself (paths, lines, file
  names, the commit message). A commit-plane check could read it.
- **record**: the breach shows only by joining records outside one diff: board
  state over time, CI run history, refs and pull requests, platform settings,
  a child repo's tree read from the parent.
- **invisible**: the breach leaves nothing in the tree or the repo's records.
  At most a session transcript holds it, and some of those are reachable by a
  harness hook before the act (the before-plane, `115/100`).

## Method, and what it did not do

1. Read `00-APEX.md`, `AUTONOMY.md`, `GUARDS.md` and `PROPAGATION.md` in full
   at the commit the worktree was cut from (the wave-5 board claim of run
   78ca). Each sentence that tells a future agent to do or not do something is
   a rule. Bearings, grounding stories, prior-art tables, framing and pure
   permissions are not counted (`AUTONOMY.md`'s "a repo may record a narrower
   posture"; `GUARDS.md`'s visibility scope statement and its table of which
   commits the hook plane reaches, which are facts, not directives).
   Clauses that only restate one rule are folded into it.
2. **Cross-slice folds.** A rule these files restate from a slice-1 document is
   not counted again: `AUTONOMY.md`'s bulk deletion show-first is `REC24`, its
   "keep the work resumable" is `CON74`, and `PROPAGATION.md`'s
   carrier-never-delivers is `CON49`. Where a rule sits in two of these four
   files it is counted once, at the row that names the fold (APX9, APX18,
   PRO15).
3. **The floor region counts once, in PROPAGATION.** The `floor:begin` /
   `floor:end` region is a stamped summary of rules whose homes are elsewhere
   (the apex, the always-confirm list, concurrency, session rhythm, asking,
   pointing up). Its bullets are not counted as rules here: each is counted at
   its canonical home, in this slice (APEX, AUTONOMY, PROPAGATION's own
   sections), in slice 1 (CONCURRENCY, RECORD) or in a later slice
   (COMMUNICATION for asking, ECONOMICS for overload). What the region adds as
   rules of its own, that it is present, stamped and verbatim, is PRO2 and PRO3.
4. Listed every check that could see a breach: the floor registry
   (`python3 tools/floor.py --list` on the hook, CI and msg planes), the floor's
   own config validation and its CI-only visibility line, `.githooks/`, both
   workflows (`.github/workflows/ci.yml` runs `stampscan` and `blockscan`
   advisory and atelier-only, outside the registry), the tests that pin
   doctrine copies (`tools/test_templates.py`), `tools/allowmarker.py`, and the
   self-run instruments (`pins.py`, `floorfleet.py`, `flipcheck.py`,
   `publishscan --history`, `ccclose`).
5. Before writing *enforced* against a rule, read the code that does it and
   cite it as file and function. Date windows are stated where a check listed
   `enforced` warns at present: `attribscan` until 2027-02-08, `namescan` until
   2027-05-03, `quotescan` until 2027-05-31, malformed allow-markers until
   2026-12-09 (`MALFORMED_GRACE_UNTIL`), the `sizescan` advisory and disabled
   bar from 2026-12-09, and `pins.py`'s floor-copy report until 2026-12-09.
6. **Not counted:** a warn-only authority-surface check under construction in
   the same queue run. It is not on `main` at this census.
7. Did not read `docs/SESSIONS.md` or `docs/sessions/` (the run's bounds).

**On `115/110`.** Its map (2026-08-15) has no file of its own; the item's
summary is what survives, and this slice checks that summary against the tree
as it stands. Its headline was that `00-APEX.md` is entirely prose-only and the
always-confirm floor has no mechanical backing. **For APEX it holds**: none of
the 18 rules below has a check (one is accepted as unenforceable, the
dilemma rule, on the item's own ground). **For the floor it holds in part.**
Of the eleven always-confirm stops (AUT2, AUT10, AUT12 to AUT14, AUT16 to
AUT21), two are enforced: a flip to public on a repo declared private reds the
next CI run (`floor.py`'s visibility line, `260/050`), and a committed
credential is blocked (`secretscan`). A third, AUT14, is touched only
incidentally: `publishscan` refuses a tracked agent allowlist, for publication
reasons. `flipcheck.py` reads the platform settings and judges nothing. The item's two
"reachable today" checks: the visibility comparison is built, on CI, as
detect-and-alert after the act; the diff-path trigger on edits to
`AUTONOMY.md` or an allowlist is not on `main`, and widening one's own authority
(AUT14) is still seen only by a person reading the diff.

## 00-APEX.md

| Id | Rule (section) | State | Guard, or where a breach shows |
| --- | --- | --- | --- |
| APX1 | If uncertain, say so; if something broke, say so first; name a skipped step (*Honesty is absolute*) | directive-only | invisible: the report lives in the transcript |
| APX2 | Never a claim stronger than its evidence; "done and verified" means exercised and observed | directive-only | invisible in a reply; where the claim lands in a record, diff, judgement. No check reads a claim against its evidence |
| APX3 | A caveat that makes a good result look worse is mandatory | directive-only | invisible: an omission |
| APX4 | Surface a genuine dilemma; never silently resolve it | unenforceable, accepted | A silently picked fork leaves no artefact on any plane, a before-plane included: the fact that would condemn it (that a fork existed) is in the agent's reasoning only. `115/110`'s ground, and it stands |
| APX5 | Purposefully withholding relevant information is dishonesty; a value the doctrine bars is withheld only with its existence and location declared (*Truth, honesty, transparency*) | directive-only | invisible |
| APX6 | The full account is offered unprompted; filtering is the listener's waiver, never the teller's shortcut | directive-only | invisible |
| APX7 | Never overrule the principal, in any situation, including one where he seems uninformed (*The principal's authority*) | directive-only | invisible |
| APX8 | A challenge to a ruling is raised to him and never licenses acting as if it were not given; an extracted approval is challenged by supplying the account and asking again, never by declining to obey | directive-only | invisible |
| APX9 | At an always-confirm stop, an approval given without the account is re-briefed before the irreversible act (`AUTONOMY.md`'s restatement folded here) | directive-only | invisible: the order of briefing and act is in the transcript. The acts themselves are the AUT rows |
| APX10 | Once the account is offered he may waive it; the agent never refuses the decision or polices his diligence | directive-only | invisible |
| APX11 | Before asking for a ruling or acting on his overrule, owe what, why, likely impacts, the options with their trade-offs, and a recommendation with its reasoning, in plain language (the scaling clause is a relaxation, folded) | directive-only | invisible: the ask is in the transcript. A before-plane hook on the question device could read its payload for a recommendation; none exists |
| APX12 | Every fact in the ask is verified, or marked as not verified | directive-only | invisible |
| APX13 | Treat outcomes as evidence; a surprise either way is a finding (*Adaptation is continuous*) | directive-only | invisible |
| APX14 | Don't fear the hard road; every model takes it and escalates where it must | directive-only | invisible |
| APX15 | A doctrine or design change rides on repeatable proof, extracted from decided practice | directive-only | diff, judgement: a method-file change citing no grounding |
| APX16 | The proof duty is never a bar the agent holds against the principal | directive-only | invisible |
| APX17 | Harvest, then encode: a learning lands in doctrine, a tool or a record; a refined learning's stale claims are swept in the same commit | directive-only | diff, judgement: stale claims left elsewhere in the tree. The encode half is an omission |
| APX18 | One doctrine for every model; a less capable model escalates rather than improvising past its limit (*Who it binds*; `AUTONOMY.md`'s two restatements folded) | directive-only | invisible. `modelguard` makes a spawn name a model, not obey this |

The canonicality clause (children inline a short floor and never restate the
apex in full) is counted at PRO15.

## AUTONOMY.md

| Id | Rule (section) | State | Guard, or where a breach shows |
| --- | --- | --- | --- |
| AUT1 | Proceed without asking on recoverable work; asking for what the owner would only grant is itself a cost (*The one rule*, *Always proceed*) | directive-only | invisible |
| AUT2 | Making a private thing public confirms: a visibility change, a collaborator, an external audience (*Always confirm*) | enforced, partial (CI, reds the run after the act) | `floor.py:check_visibility` with `github_visibility`, CI plane only: declared private and GitHub public is the one red. It cannot stop a flip and sees one at the next CI run. Collaborators and external sends: invisible to the repo |
| AUT3 | Know your repo's visibility before you push; every repo states it in `CLAUDE.md` and can verify it | enforced, partial (warns, CI) | `floor.py:check_visibility` prints 🟡 when `.atelier-floor.json` declares nothing. The `CLAUDE.md` statement is not read, and nothing compares the two |
| AUT4 | The making-public confirmation includes the pre-flip scrub of lines joining the estate root to its holdings | directive-only | record: the tree at the moment of the flip, which is not a commit |
| AUT5 | The scrub runs last, over the gate's own records; the gate runs `publishscan --history` | directive-only | record. Instrument: `publishscan.py:run_history` |
| AUT6 | A planted canary is reconciled shape by shape | directive-only | diff: a gate record with no line per planted shape |
| AUT7 | The pin is current at the flip; the drift check runs and the inlined floor is compared | directive-only | record. Instrument: `pins.py` (floor-copy report, report-only until 2026-12-09) |
| AUT8 | Before the flip the gate reads and records five platform settings; an unruled value goes in front of the confirmation | directive-only | record (platform state). Instrument: `tools/flipcheck.py` (GET only, exit 0 whatever it reads; `260/130`) |
| AUT9 | Flip and harden are one sitting; the flip is unfinished until protections read back | directive-only | record. Instrument: `flipcheck.py` run again after the flip |
| AUT10 | A commit carrying a credential is a making-public event; secret-scan before pushing | enforced (blocks, hook + CI) | `secretscan` (registry, no advisory form), `secretscan.py:scan_text`; the hook plane runs before any push |
| AUT11 | Secrets are cheaply rotatable; rotate on a cadence that keeps an undetected exposure short | directive-only | invisible to the repo |
| AUT12 | Truly destructive or irreversible acts confirm; a verified restore point exists first | directive-only | invisible (a before-plane hook could read `rm -rf`, a force-push or `gh repo delete` in the command text) |
| AUT13 | Lockout-class changes confirm, or a tested out-of-band rollback is staged | directive-only | invisible to the repo |
| AUT14 | Widening your own authority confirms: editing this file, another repo's autonomy block or a permission allowlist | directive-only | diff: an edit to `docs/method/AUTONOMY.md`, a `CLAUDE.md` autonomy block or a tracked allowlist. `publishscan.py:matches` refuses a tracked `.claude/settings.json` for publication, which stops a tracked allowlist only incidentally; untracked and user-level settings: invisible. `115/110`'s sharpest finding, unchanged on `main` | <!-- pathscan:allow: the agent settings file publishscan refuses to track, named as the thing refused -->
| AUT15 | Grants change only on the owner's explicit dated words; the agent records a grant, never originates one | directive-only | diff: a grant row or autonomy line added with no quotation or citation. `attribscan` needs an attribution word, which a grant row lacks; `quotescan` guards one other file |
| AUT16 | New trust surfaces (deploy keys, webhooks, CI secrets, app installs, OAuth grants) confirm | directive-only | record (platform state); diff only where a workflow starts reading a new secret |
| AUT17 | Secrets: no direct handling of a stored value, and no use beyond its provisioned purpose | directive-only | invisible (before-plane reachable from the command text). `secretscan` sees a value only once committed (AUT10) |
| AUT18 | Spend beyond the plan confirms | directive-only | invisible. `modelguard` makes a spawn name its model; it does not price it |
| AUT19 | People and safety confirm; merging other people's work is people-adjacent | directive-only | record: a merged pull request whose author is not the owner |
| AUT20 | Installing an unapproved tool confirms | directive-only | invisible (before-plane reachable: an install command) |
| AUT21 | Deploy-on-push of a new content class confirms | directive-only | diff, judgement on what is a new class |
| AUT22 | A grant in one context is not a grant for the next | directive-only | invisible |
| AUT23 | Contradictory instructions are asked about with both sources named | directive-only | invisible |
| AUT24 | A refused call is never re-routed through another tool; the refusal goes to the principal through the device (*A refused call is an ask*) | directive-only | invisible (before-plane reachable). Instrument: `ccclose:checkBypasses` lists workaround-shaped commands |
| AUT25 | The doctrine does not restate a third party's limits (*A limit the tooling imposes*) | directive-only | diff, judgement |
| AUT26 | Name a limit met, in the record and to the principal | directive-only | invisible |
| AUT27 | Carry on with what does not depend on the limit; hand it up when the session cannot manage it | directive-only | invisible |
| AUT28 | Change a declined request, never smuggle it; where narrowing costs quality, stop and ask | directive-only | invisible |
| AUT29 | First-of-kind, structural or live-blast-radius work goes to the cheapest model that can do it and dig itself out (*Who acts*) | directive-only | record (the transcript's model id) |
| AUT30 | A less capable model runs pattern-following work behind a mechanical gate | directive-only | invisible |
| AUT31 | Encode the policy: a live-risk constraint becomes a gate, not a note | directive-only | invisible: an omission |
| AUT32 | Before deleting or overwriting what the agent didn't create, look first and surface a contradiction (*Before you destroy*) | directive-only | invisible |

> **Update 2026-11-27 (`115/550`, defect 5 of the slice 8 census).** The
> `AUT14` row and the figures above stand as this census recorded them;
> nothing in them was rewritten. Since `b462fd7d` (2026-11-16, board `115/110`),
> `quotescan` reads an edit to `AUTONOMY.md`, the floor region and its stamped
> copies in a `CLAUDE.md`, and the `permissions` value of a settings file, and
> asks for the principal's words in the commit body. So `AUT14` is now
> **enforced, partial (warns)**: advisory on every plane and date, never
> blocking, and still blind to an unstamped floor copy and to a widening
> through any settings key but `permissions`. `AUT15` is partly read (a grant
> edited in `AUTONOMY.md`). The running totals keep slice 2's figures, as slice
> 6 said they would.

## GUARDS.md

| Id | Rule (section) | State | Guard, or where a breach shows |
| --- | --- | --- | --- |
| GRD1 | Every guard declares cheap-failure or forbids-the-act (*The fourth requirement*) | enforced, partial (warns, CI) | The posture is one of the five fields `floor.py:declarations_report` reads, printed on the CI plane with no exit code. Presence, not truth |
| GRD2 | A test that arrives after a guard is grounds to declare, never to unwire a working gate on the author's judgement; a failing guard is a finding for the principal | directive-only | diff: a registry entry removed, or a check's state lowered, in `tools/floor.py` |
| GRD3 | Forbid at a construction site you control; make the failure cheap at a read site (*Choosing between them*) | directive-only | diff, judgement. Unaudited, the doc says |
| GRD4 | A guard declares who it protects from whom, and the writer it assumes (*Declare the threat model*) | directive-only | diff: no declaration field holds it |
| GRD5 | A pathspec commit is safe only when the other staged paths are identified | directive-only | invisible. `sweepscan` warns on a whole-index commit, not on this (CON6 and CON7 are its neighbours) |
| GRD6 | A guard that knows its own work by a convention states the convention where the guard lives | directive-only | diff, judgement |
| GRD7 | Before building a check, ask whether its licensing context fits its evidence window; if not, directive or widen first; existing checks too (*Before building a check*) | enforced, partial (warns, CI) | The evidence-window field in `floor.py:declarations_report`, presence only; the judgement is review work |
| GRD8 | A reasoned allow-marker brings the missing context inside the window; a bare marker exempts nothing | enforced (blocks, hook + CI) | `allowmarker.py:marker_rx`, each scanner's reason-required form; `sizescan.py:parse_allow` likewise. A bare marker leaves the finding standing |
| GRD9 | Every check states the five declaration fields, or states that it cannot (*What every check declares*) | enforced, partial (warns, CI) | `floor.py:declarations_report` and `read_declaration` (whether a citation or replay resolves), on the CI plane and `--declarations`; no exit code reads it. `--list` shows 0/5 to 2/5 per check at this census |
| GRD10 | A replay test fails when the check stops firing | directive-only | diff, judgement: the test's content. `floor.py:_replay_problem` checks that a replay resolves, not that it fails |
| GRD11 | Undeclared axes default to worst case (*What a finding is assessed on*) | directive-only | invisible |
| GRD12 | Assessment and response stay separate | directive-only | diff, judgement |
| GRD13 | Use the narrowest granularity level and the narrowest scope in it; a guard with more than one rule supports rule-scoped allowance (*Granularity*) | directive-only | diff: a new ignore-file glob, `disabled` entry or unscoped marker. `allowmarker.py:covers` and `is_blanket` provide the scoped lane; nothing measures what a new allowance exempts |
| GRD14 | A malformed scoped marker exempts nothing (grace to 2026-12-09) | enforced (warns until 2026-12-09) | `allowmarker.py:is_malformed`, `_warn_malformed`, `in_malformed_grace`; after the date the marker is not honoured |
| GRD15 | An acceptance (marker, ignore glob) carries a reason; the grant date comes from version control (*Acceptance and deferment*) | enforced, partial (blocks, hook + CI) | Markers: GRD8. Globs: `allowmarker.py:load_ignore_globs` raises a config error on an unreasoned glob; used by most scanners, and whether every scanner outside that list refuses one is unverified |
| GRD16 | The cold-content gate takes no acceptance: no marker, no glob | enforced (blocks, hook + CI) | `sizescan.py:_inert_hatches` names a hatch inert; `cold_item_count` blocks regardless |
| GRD17 | A mandate's date never moves later; an unlabelled date reads as a mandate (*Who may move a deferment's date*) | enforced, partial (warns, hook) | `floor.py:moved_later` prints a line when a staged `review-by` on a mandate or unlabelled advisory moves later than HEAD; never blocks. No house date exists to compare a child against (the doc says so) |
| GRD18 | A ruling that sets a fleet date names its kind; a date of unknown kind is asked about and recorded | directive-only | diff: a `review-by` added with no `kind`. `floor.py:_load_advisory` validates a kind given and requires none; `floorfleet` prints "date kind not recorded" (instrument) |
| GRD19 | A guard never lowers its own response on its own judgement (*Provenance, not direction*) | directive-only | diff: a scanner code change that lowers a response instead of a declaration doing it |
| GRD20 | A repo lowers a check's response only with a reason and an end date, visible in the fleet view (*Ruled 2026-11-09*; adoption's advisory-first lane folded) | enforced, partial (blocks, hook + CI) | `floor.py:_load_advisory` refuses an advisory with no `why` or `review-by` (config error); `_load_disabled` accepts an undated or bare-string `disabled` and warns (`320/800`) |
| GRD21 | `sizescan` is barred from `advisory` and `disabled` from 2026-12-09 | enforced (warns until 2026-12-09, then blocks) | `floor.py:advisory_barred`, `disabled_barred`; the floor line names the date before it |
| GRD22 | Narrowing a never-softened check by `scope` or `flags` states a why; `flags` may not re-aim or neuter a check | enforced (blocks, hook + CI) | `floor.py`'s `Config` validation (`scope.<name>` needs a `why`), `_load_flags`, `forbidden_flags` |
| GRD23 | Fail noisy, then subtract: a clean result counts what was suppressed and by which mechanism, names scope reductions, and keeps the set retrievable (*Fail noisy*) | enforced, partial (CI tests, block the run) | `report.py:suppressed_line`; 11 test files pin a suppressed line. Scanners with no such pin: unverified |
| GRD24 | Coverage is accounted: what was looked at, known zeros printed, "not in scope" said | enforced, partial (CI tests, block the run) | `report.py:coverage_line`, used by 27 of 46 `tools/*.py` files; the floor's own line pinned in `tools/test_floor.py`. No test asserts every scanner prints it (none found) |
| GRD25 | A reason lives on the line or in the file a reviewer reads, never where the exemption makes it unreadable (*Who, why, when*) | directive-only | diff |
| GRD26 | `.leakscanbinaries` lines carry `by=`, `session=` and `on=` | enforced (warns, hook + CI) | `leakscan.py`'s `PROVENANCE_FORM`: a line without them warns |
| GRD27 | Side-stepping is observable: a bypass is a recorded event, or it is a hole (*Side-stepping*; adoption by bypass folded) | directive-only | record. CI re-scans pushed content, so a `--no-verify` commit's content is caught but the bypass is not recorded. Instruments: `ccclose:checkBypasses` (flags `--no-verify`), `floorfleet` (unwired clones); `floor.py:commit_msg_hook_note` names a missing commit-msg hook. `C4` is the open build |
| GRD28 | A rule earned is homed on a surface a future session reads; a commit message or record is not a home (*A rule with no home*) | directive-only | diff, judgement: a commit message stating a rule with no doctrine, tool or template change beside it |
| GRD29 | A false positive is a guard defect fixed in the guard; an allowance written for one is recorded as debt (*When a guard is wrong*) | directive-only | diff: a new marker reason describing a false positive, with no item cited |

## PROPAGATION.md

| Id | Rule (section) | State | Guard, or where a breach shows |
| --- | --- | --- | --- |
| PRO1 | A commit that changes what a method file, skill or command tells a session carries its `CHANGELOG.md` line in the same commit (*The mechanism* point 1; *What the version signal is worth*) | directive-only | diff: a commit touching `docs/method/`, `skills/` or `commands/` with no `CHANGELOG.md` change |
| PRO2 | Every child `CLAUDE.md` carries the standard block at its top: floor, pointer, pin, drift check, visibility fact (*The standard child doctrine block*) | directive-only | record: the child's tree, outside atelier's diff. Instruments: `pins.py` (`unstamped`), `floorfleet.py` |
| PRO3 | The floor region, counted once: the canonical text sits between the `floor` markers; every copy is stamped and word for word, never narrowed, and a `stampscan:allow` marker cannot switch the comparison off | enforced, partial (CI test, blocks the run) | atelier's copies: `tools/test_templates.py`, `TemplateBlockSyncTest.test_stamped_block_matches_canonical` (character for character) and `test_stamp_markers_sit_on_their_own_lines`; `stampscan.py:_is_floor_block` refuses `narrow=` on the floor (atelier CI, `--warn`). Children's copies: `pins.py:check_copy` at each child's pin, an instrument, report-only until 2026-12-09 |
| PRO4 | Run the drift check at session start against the parent's `origin/main` through the tools setting; a failed command is no result, never "current" | directive-only | invisible. Instrument: `pins.py` (fleet) |
| PRO5 | The pin moves only by a deliberate per-repo bump after reading the delta, and is bumped even when the delta does not bear | directive-only | record: the pin against the parent's log. `pins.py` is read-only by design |
| PRO6 | The block stays lean: one bullet per irreducible concern, nine, no line figure; a concern leaves only by redundancy, never by trimming a live safety statement; the verify-the-act rule stays behind the pointer | enforced, partial (warns, CI, atelier only) | `blockscan.py:check_integrity` (`--check --warn`) warns when a mapped bullet's anchor stops resolving: six of nine bullets. A clause trimmed inside a bullet, or a bullet added: diff, unguarded |
| PRO7 | A non-floor stamped copy narrows only by `narrow=<reason>`, declared by the child; narrowing to nothing is drift; a declaration excuses omission only | enforced, partial (warns, CI, atelier only) | `stampscan.py` (`--warn`, atelier CI). Children's stamps are not reached (ST3) |
| PRO8 | atelier's canonical floor text may compress its source but never contradict it; a change to the apex, floor, concurrency or estate-pointer doctrine reviews the block's wording | enforced, partial (warns, CI, atelier only) | `blockscan.py:check_costaged` (`--against HEAD^ --warn`): a mapped source section changed with its bullet unmoved. Contradiction itself: judgement. The three unmapped bullets: unguarded |
| PRO9 | The bundled-mode variant is stamped verbatim with exactly two substitutions; a scaffold never improvises its wording | directive-only | diff (the scaffold's text). No test pins the variant (none found in `tools/test_templates.py`) |
| PRO10 | Estate facts are referenced from the estate root, never re-derived or copied down into a child; a list of every repo never reaches a public surface | directive-only | diff, judgement. Whether `leakscan`'s machine-local term list names repos: unverified (as REC32) |
| PRO11 | Bind the property, not the role: a rule that names categories of repo exempts the writer's own | directive-only | diff, judgement |
| PRO12 | A child may narrow or append and never silently contradict; a conflict stands only as a principal-ruled exemption recorded in the child; a resolution lands in the parent (*The layer-override rule*, *Who is a child*) | directive-only | diff in the child, judgement |
| PRO13 | On a live collision the stricter reading wins until resolved upward; the parent never points down for truth | directive-only | invisible |
| PRO14 | Every repo the principal owns or controls and works an agent in is a child unless he rules an exclusion; an unclear case goes to him; an exclusion is recorded in the estate root | directive-only | record. The instruments discover repos directory-locally on one machine (the doc says so) |
| PRO15 | A child never repeats doctrine the parent owns: it points up or uses a stamped copy (APEX's "never restate it in full" folded) | directive-only | diff in the child, judgement: an unstamped restatement is invisible to `stampscan`, which reads only declared copies |
| PRO16 | An exemption is re-tested when the rule it departs from moves | directive-only | record (children's exemptions against the parent's change) |
| PRO17 | Every repo reports its problems with the doctrine to atelier; potential is the standard (*The duty*) | directive-only | invisible: an omission |
| PRO18 | With evidence where it exists, marked unevidenced where not; never a suspicion dressed as a finding | directive-only | diff, judgement |
| PRO19 | The reporter stops at the report and never silently works around a rule it thinks wrong | directive-only | invisible |
| PRO20 | A hand-up's mechanism claim is re-driven before it becomes house text, and the record says so | directive-only | record |
| PRO21 | atelier files its own doctrine defects as board items and never fixes the wording in passing | directive-only | diff, judgement: telling a defect fix from an ordinary edit is judgement |
| PRO22 | Check the parent's actual file first, never your own block; a rule the parent already owns is a findability defect (*Check the parent's file first*) | directive-only | invisible |
| PRO23 | A house question is closed by the house; a local session never records an open house question as settled | directive-only | diff, judgement. `attribscan` sees only an attribution word without evidence (warns until 2027-02-08) |
| PRO24 | Whose rule: one true in a repo sharing none of this stack is the house's (*The test*) | directive-only | invisible, judgement |
| PRO25 | File in the parent's board by the shape you can reach; hold-and-flag is not filing and is never recorded as filing (*The route*, step 1) | directive-only | record |
| PRO26 | A doctrine defect that is a vulnerability takes the private route first; the public item lands with the fix | directive-only | diff, judgement: a public item describing an unfixed vulnerability |
| PRO27 | Rule 2: a private child's filing carries the class only, with no repo token on the branch, PR title, commit subject, PR body or item | enforced, partial (warns, msg plane) | `namescan.py:scan_message` (branch and commit title against `leakscan`'s machine-local terms; public repos only; warns until 2027-05-03) and `leakscan` on the item's added lines (hook). PR titles and bodies: unread |
| PRO28 | A worked example in a public doctrine file names no private child repo | directive-only | diff. The term-list question of PRO10 |
| PRO29 | The child keeps one line of repo-shaped instruction, pending upstream and naming the parent item: not the rule, the reasoning or the narrative (step 3) | directive-only | diff in the child, judgement |
| PRO30 | Every pending-upstream line begins `Pending upstream:`, then an ISO UTC date and the parent item or `unfiled` | directive-only | diff: a line shape a grep can read; no check reads it |
| PRO31 | The incident goes in the child's record (step 4) | directive-only | record |
| PRO32 | At the pin bump a pending-upstream line becomes a pointer; one surviving past its landed item is drift | directive-only | record. The enumerator (`310/020`) is not built |
| PRO33 | A hand-up branch is `report-<subject>-<HHMM>` with no repo token, never a re-used or re-created name (*Report without harming the parent*) | directive-only | record: the ref history. `namescan` sees a private name in the branch (PRO27), not the form or the reuse |
| PRO34 | The commit's first line and the PR body say it is a filed finding | directive-only | diff: the commit's first line |
| PRO35 | Open the PR before you stop | directive-only | record. Instrument: `ccclose:checkBranches`, `checkPrs` (whether they test this case: unverified) |
| PRO36 | Touch your own item and nothing else: no claim, no doctrine edit, no rebase onto a moved `main`, no reference to your own item number | directive-only | diff: a `report-` branch whose change touches more than its item and the index. The doc names `handupscan` as the next rung, unbuilt |
| PRO37 | The parent lands an open hand-up (opens the PR, merges on the floor's evidence, says the content is the child's and unreviewed, never rewrites the reporter's history), looking for them at open as its first act | directive-only | record (open pull requests and their age) |
| PRO38 | Before merging, check the head ref, title, body and file set by command | directive-only | record (pull-request metadata). `namescan`'s CI plane reads pushed ref names after the fact, report-only |
| PRO39 | Resolve an index conflict by a merge in the parent's worktree with the index rebuilt, never a rewrite of the reporter's branch; a number collision moves the later item | enforced, partial (blocks, hook + CI) | `board.py:_run_check` refuses a hand-merged index and `number_collisions` a collision (the checks counted at REC22); merge-not-rewrite: record |
| PRO40 | Between any two repos, the sender names in its own record where it filed (*The same route between any two repos*; queue-never-deliver is CON49; redaction to a public target is PRO27) | directive-only | record |
| PRO41 | A child calls the parent's enforcement and never holds a copy of which checks run; an opt-out is a declaration (*Enforcement propagates too*) | enforced, partial (CI test, blocks the run) | `tools/test_templates.py`, `ChildFloorWorkflowTest.test_names_no_scanner` and `test_calls_ateliers_reusable_floor` pin the scaffold template; `floor.py:_load_disabled` refuses a list and accepts a bare reason string. A child's own edited workflow: instrument (`floorfleet`) |
| PRO42 | The parent runs the floor it ships, scoped by the same config | enforced (blocks, hook + CI) | `.githooks/pre-commit` names no scanner and runs `floor.py`; `ci.yml` runs `floor.py --plane ci`; `tools/test_precommit.py` pins the hook. See the defect below on atelier-only steps |
| PRO43 | A parent's local narrowing carries its reason beside it in its config, and the rule says so where it is stated | enforced, partial (blocks, hook + CI) | `floor.py` refuses a reasonless `scope` or `flags` on a never-softened check (GRD22) and a reasonless advisory (GRD20); a `scope` on a softenable check may omit it. The statement beside the rule: diff, unguarded |
| PRO44 | Landing is proved by enumeration, never by scaffolding or a pin bump (*Enumeration, not assumption*) | directive-only | invisible: the claim in a report. Instruments: `floorfleet`, `signfleet` |
| PRO45 | When a rule keeps breaking, climb (framing, mechanism, remove the situation), testing each rung against the recorded occurrences; never restate louder (*When a rule keeps breaking*) | directive-only | diff, judgement: a doctrine commit that restates a rule already present |
| PRO46 | Framing is owed by every rule up front; a check not built is a decision with its reason recorded | directive-only | invisible: an omission. This census is that record for its slices |
| PRO47 | A second noticed occurrence triggers the ladder; the third promotes a pattern into doctrine | directive-only | invisible |
| PRO48 | The mining pass runs on the principal's word, files board items with evidence and recurrence, and proposes changes without making any | directive-only | record: telling the pass's commits apart needs its session known |
| PRO49 | Three independent statements of one rule are consolidated into one in the owning file, covering every reading (*One statement, stamped copies*) | directive-only | diff, judgement |
| PRO50 | A copy at the point of use is stamped, names its source and is narrowing-free | enforced, partial (CI test, blocks the run) | `QueueRunSkillTest.test_marked_as_stamped_copy` and `ReviewBriefSkillTest.test_marked_as_stamped_copy` in `tools/test_templates.py` pin two skills; `stampscan` (`--warn`, atelier CI) reads declared copies. An undeclared copy is invisible to both |

## Directive-only rules, grouped by where a breach shows

**Diff-visible (36).** APX15, APX17; AUT6, AUT14, AUT15, AUT21, AUT25; GRD2,
GRD3, GRD4, GRD6, GRD10, GRD12, GRD13, GRD18, GRD19, GRD25, GRD28, GRD29;
PRO1, PRO9, PRO10, PRO11, PRO12, PRO15, PRO18, PRO21, PRO23, PRO26, PRO28,
PRO29, PRO30, PRO34, PRO36, PRO45, PRO49. In PRO12, PRO15 and PRO29 the diff is
the child's, which atelier never sees. APX15, APX17, AUT21, AUT25, GRD3, GRD6,
GRD12, PRO11, PRO18, PRO21, PRO23, PRO26, PRO45 and PRO49 need judgement a
scanner cannot make, and stay review work.

**Record-visible (23).** AUT4, AUT5, AUT7, AUT8, AUT9, AUT16, AUT19, AUT29;
GRD27; PRO2, PRO5, PRO14, PRO16, PRO20, PRO25, PRO31, PRO32, PRO33, PRO35,
PRO37, PRO38, PRO40, PRO48.

**Invisible (42).** APX1 to APX3, APX5 to APX14, APX16, APX18; AUT1, AUT11,
AUT12, AUT13, AUT17, AUT18, AUT20, AUT22, AUT23, AUT24, AUT26 to AUT28, AUT30
to AUT32; GRD5, GRD11; PRO4, PRO13, PRO17, PRO19, PRO22, PRO24, PRO44, PRO46,
PRO47. Of these, AUT12, AUT17, AUT20 and AUT24 are acts a before-plane hook
could read from the command text, and APX11 is an ask a hook on the question
device could read: the class `115/100` is about.

## Counts

| Doc | Rules | enforced (of which partial) | blocks | warns | directive-only | diff | record | invisible | unenforceable, accepted |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 00-APEX.md | 18 | 0 (0) | 0 | 0 | 17 | 2 | 0 | 15 | 1 |
| AUTONOMY.md | 32 | 3 (2) | 2 | 1 | 29 | 5 | 8 | 16 | 0 |
| GUARDS.md | 29 | 14 (8) | 7 | 7 | 15 | 12 | 1 | 2 | 0 |
| PROPAGATION.md | 50 | 10 (9) | 6 | 4 | 40 | 17 | 14 | 9 | 0 |
| Slice 2 | 129 | 27 (19) | 15 | 12 | 101 | 36 | 23 | 42 | 1 |
| Slice 1 | 158 | 19 (11) | 14 | 5 | 133 | 35 | 33 | 65 | 6 |
| Running total | 287 | 46 (30) | 29 | 17 | 234 | 71 | 56 | 107 | 7 |

As in slice 1: *diff*, *record* and *invisible* split the directive-only count,
each rule once, under the place a breach first shows. *blocks* includes the CI
test pins (PRO3, PRO41, PRO50, GRD23, GRD24) and AUT2's CI red, which fail the
run after a push rather than refusing the commit. A rule whose checks mix both
responses is counted at its strongest (PRO3 blocks through its test; its
`stampscan` half warns). A check that warns until a date (GRD14, GRD21) is
counted as it behaves at this census.

Reading the table. GUARDS is the best-enforced document in either slice (14 of
29), and the reason is structural: its rules govern the checks themselves, and
the floor validates its own config, so a lowering written into
`.atelier-floor.json` meets code. What GUARDS leaves directive-only is the
lowering that does not go through that config: a registry entry removed, a
scanner's response lowered in code (GRD2, GRD19). APEX has no check at all,
as `115/110` found. Of the always-confirm floor's eleven stops, the two that
touch publication (a flip, a committed credential) are enforced; the stops that
touch authority, destruction, lockout, spend, people, tools and trust have no
check. Across both slices, 16% of the 287 rules counted have any
mechanical check, and 30 of those 46 cover only part of the rule.

## Top five guard candidates

Directive-only, breach visible in the diff, and costly when it happens:

1. **AUT14, the agent widening its own authority**: a diff that edits
   `docs/method/AUTONOMY.md`'s floor or grant table, a `CLAUDE.md` autonomy
   block, or a tracked allowlist. The floor's highest-blast-radius stop, and
   the one `115/110` named first; a path trigger reads it with no new plane.
   (Under construction in the same run, warn-only; not on `main`, so counted
   here as directive-only.)
2. **AUT15, a grant recorded without the owner's words**: a grant row or
   autonomy line added with no quotation or citation of him. `attribscan` and
   `quotescan` already read this form on other surfaces; neither reads these.
3. **GRD2 with GRD19, a guard lowered outside the declared lane**: a commit
   that deletes a registry entry, moves a check from `enforced` to
   `warn-only`, or edits a scanner to stop blocking, in `tools/floor.py` or a
   scanner file. Children run the floor from atelier's `main`, so one such diff
   unguards the fleet at their next CI run, and none of it passes through the
   config validation that holds GRD20.
4. **PRO1, doctrine changed with no CHANGELOG line**: a commit touching
   `docs/method/`, `skills/` or `commands/` that adds nothing to
   `CHANGELOG.md`. Since the plugin dropped its `version`, that file is a
   plugin-only adopter's sole drift signal (the doc says the bundled drift
   check is weaker than it reads).
5. **GRD13, an over-wide allowance**: a new ignore-file glob, `disabled` entry
   or unscoped marker. The reason is enforced (GRD15, GRD20); the width is not,
   and the doc calls a too-wide allowance a defect because everything inside it
   goes unguarded and nobody chose that. A check could count what the new
   allowance exempts at the commit that adds it.

Next after these: PRO36 (a hand-up touching more than its own item, the unbuilt
`handupscan`), PRO34 (a hand-up whose first line does not say so), PRO30 (a
`Pending upstream:` line of the wrong shape), AUT6 (a canary record with no line
per shape), GRD18 (a fleet `review-by` with no `kind`).

## Doctrine defects found, not fixed here

Each is owed its own board item (`PROPAGATION.md` § *Pointing up*); none is
changed by this file.

- **Visibility has two homes and nothing joins them.** `AUTONOMY.md` says every
  repo states its visibility in its `CLAUDE.md`; the floor's visibility check
  reads `.atelier-floor.json`'s `visibility` key. Two declarations of one fact,
  compared to each other by nothing: a repeat in `PROPAGATION.md`'s own sense.
- **The "one list" of always-confirm stops is two lists.** `00-APEX.md` says
  `AUTONOMY.md` § *Always confirm* holds the list once, and `PROPAGATION.md`
  calls the floor block a narrowing-free restatement. The block adds bulk
  deletion from a record store (in `AUTONOMY.md` it sits under § *Before you
  destroy or overwrite*, not § *Always confirm*) and leaves out deploy-on-push
  of a new content class and the merging of other people's work.
- **"A parent enforcing something its children don't" has no carve-out.**
  `PROPAGATION.md` § *Enforcement propagates too* calls that the defect one
  level up; `ci.yml` deliberately runs `stampscan`, `blockscan` and the
  signature planes in atelier only, with reasons in its comments (their paths
  exist only in atelier). The rule as written condemns a choice the workflow
  documents; either the rule wants a parent-only-subject exception or the
  steps are the defect.

## Doubts and unverified points

- **The floor-region reading** (method step 3) is this census's: the region's
  bullets are counted at their homes, and the region itself at PRO2 and PRO3. A
  reading that counted each bullet in PROPAGATION would add nine rows and double
  count their sources.
- **Rule boundaries are a judgement**, as in slice 1; the folds are named in
  the rows and in the method.
- **Unverified**: whether every scanner outside `allowmarker.load_ignore_globs`'s
  callers refuses an unreasoned glob (GRD15); suppressed-line pins for scanners
  with no such test (GRD23); whether `leakscan`'s machine-local term list names
  private repos (PRO10, PRO28); whether `ccclose`'s branch and PR checks catch
  an unopened hand-up PR (PRO35).
- **A possible slice-1 gap.** `GUARDS.md` § *A rule with no home* points at
  `RECORD.md` § *What the principal said arrives three ways*; slice 1's rows
  name no rule from that section. It is RECORD's to count, so it is not counted
  here.
- **Self-run instruments** were counted directive-only, as in slice 1. `pins.py`
  will fail its own run on a differing child floor copy from 2026-12-09; nothing
  runs it unasked, so PRO3's child half stays an instrument after that date.

## Remaining docs for later slices

`docs/method/`: `ACCESS.md`, `COMMUNICATION.md`, `CONVENTIONS.md`,
`DATA-PROTECTION.md`, `DOCUMENTATION.md`, `ECONOMICS.md`, `EVIDENCE.md`,
`GLOSSARY.md`, `MECHANISMS.md`, `PRINCIPLES.md`, `REACH.md`, `SECRETS.md`,
`SIGNING.md`, `STORAGE.md`, `TOOLBOX.md`, and `docs/method/session-open/`. Then,
on `REVIEW.md` rule 3's definition, the doctrine outside `docs/method/`:
`docs/build/`, the ADRs, the skills and commands, the templates and the
validators' own stated rules.
