# Enforcement census — EVIDENCE, ECONOMICS, COMMUNICATION, DATA-PROTECTION

Board item `020/220`, slice 3 of the census. Run 2026-11-16 (UTC) by a worker
of queue run 78ca. This is a measurement record, not doctrine: it changes no
rule, and it builds no guard. It uses slice 1's method, states and row format
(`docs/method/census/2026-11-16-1142-record-review-concurrency.md`) and slice
2's fold conventions
(`docs/method/census/2026-11-16-1204-apex-autonomy-guards-propagation.md`), so
the three slices add up.

## What this asks

For each rule in four governing documents: if it is broken, what sees it? Each
rule gets one state, defined as in slice 1.

- **enforced**: a mechanical check reads the breach. The row names the check,
  the plane it runs on (the pre-commit hook, the commit-message hook, CI, a
  harness hook) and whether it **blocks** or **warns**. *partial* means the
  check covers some of the rule and the rest is unguarded.
- **directive-only**: nothing mechanical sees a breach. Where a self-run
  instrument would report it if a session chose to run it (`ccclose`,
  `cclive`, `floorfleet.py`), the row says *instrument* and the state stays
  directive-only: nothing invokes those tools, so nothing sees the breach
  unless the breaker looks.
- **unenforceable, accepted**: the fact that would license or condemn the act
  is outside any check's evidence window (`GUARDS.md` § *Before building a
  check: the evidence window*), or the house has recorded a decision not to
  build the check, and the reason is stated. Accepted as of 2026-11-16.

A directive-only rule also gets the place its breach could be seen:

- **diff**: the breach is in the committed change itself (paths, lines, file
  names, the commit message). A commit-plane check could read it.
- **record**: the breach shows only by joining records outside one diff: board
  state over time, CI run history, review files read against each other, the
  model ids a session transcript carries.
- **invisible**: the breach leaves nothing in the tree or the repo's records.
  At most a session transcript holds it, and some of those are reachable by a
  harness hook before the act (the before-plane, `115/100`).

## Method, and what it did not do

1. Read `EVIDENCE.md`, `ECONOMICS.md`, `COMMUNICATION.md` and
   `DATA-PROTECTION.md` in full at the commit the worktree was cut from (the
   slice-3 board claim of run 78ca). That includes what landed in them on
   2026-11-16 UTC: `EVIDENCE.md` §18 extended and §19 to §21 new, and
   `ECONOMICS.md` § *Session hygiene* item 1 reworded (`270/050`). Each
   sentence that tells a future agent to do or not do something is a rule.
   Grounding stories, bearings, history paragraphs, the scrubbed worked
   example and pure permissions are not counted (`ECONOMICS.md` § *Triggering
   reviews*'s inline-or-batched choice is a permission; `COMMUNICATION.md`'s
   account of the removed prose and reply planes is history).
2. **Cross-slice folds.** A rule these files restate from a censused document
   is not counted again, as in slice 2. Folded here: `ECONOMICS.md`'s
   review-tier sentence into `REV17`; its independence and cold-spawn
   sentences (sub-agents, triggering reviews) into `REV3`, `REV5` and `REV13`;
   its "earns the full ceremony" list into `REV39`; its bulk-off-the-hot-path
   paragraph into `REC25` and `REC26`; *One doctrine, tiered authority*'s first
   paragraph into `APX18`, `AUT29` and `AUT30`; the run-open role check that
   states and proceeds into `CON69`; spend past a cap into `AUT18`.
   `DATA-PROTECTION.md`'s read-before-write into `AUT32` (DATA-PROTECTION
   states it for any write, AUTONOMY for what the agent did not create); its
   verified restore point, snapshot-first and data-plane slow lane into `AUT12`,
   whose bullet points here; its "encode it" section into `AUT31`.
   `COMMUNICATION.md`'s end-of-run ask list restates its own rows COM10, COM11
   and COM14 and is folded into them.
3. **`EVIDENCE.md` §7 is folded into `REC28`.** `RECORD.md` § *Absolute
   dating* restates it and cites it (`(EVIDENCE §7.)`), and slice 1 counted it
   there with `datescan`. The two differ in reach: §7 bans `recently`,
   `currently` and `new this year` in any claim, and `datescan` excludes
   `recently`, `currently` and `soon` by design. That gap is named under the
   defects below, not counted as a second rule.
4. **`EVIDENCE.md` §17 is counted here, at its home (EVI24).** `CON21`
   (slice 1) is `CONCURRENCY.md`'s one-bullet pointer to it. Slice 1 could not
   know the pointer's target would be censused, so the running total below
   carries this one rule twice; it is named there rather than re-cutting
   slice 1. §17 is censused as it stands, including its stated ground for
   having no guard, which board item `115/410` records as contradicted.
5. Listed every check that could see a breach: the floor registry
   (`python3 tools/floor.py --list` on the hook, CI and msg planes), both
   workflows and the shipped workflow templates under `docs/build/templates/`,
   the tests that pin them (`tools/test_templates.py`) and the cross-scanner
   contract tests (`tools/test_unreadable_files.py`,
   `tools/test_selftest_quiet.py`), the harness hook `tools/modelguard.py` and
   what this machine's user-level Claude Code settings actually wire, and the
   self-run instruments (`ccclose`, `cclive`, `floorfleet.py`).
6. Before writing *enforced* against a rule, read the code that does it and
   cite it as file and function. Date windows are stated where a check listed
   `enforced` warns at present: `attribscan` until 2027-02-08
   (`ATTRIBUTION_WARN_UNTIL`), `pdlistscan` until 2027-03-08
   (`PERSONAL_DATA_WARN_UNTIL`).
7. Did not read `docs/SESSIONS.md` or `docs/sessions/` (the run's bounds).

**On the harness hook.** Slice 1 left open whether `modelguard` is wired for
sessions here (REV17). Read on this machine at this census: the user-level
Claude Code settings wire a `PreToolUse` hook on `Agent|Bash`, and the file
they name is not atelier's `tools/modelguard.py`. It is a user-level hook file,
a symlink into another repo on this machine, whose docstring states the same
check and whose text differs from atelier's. So the check runs here, from a
second copy. ECO4 counts it as enforced on that evidence; the copy question is
under the doubts below.

## EVIDENCE.md

| Id | Rule (section) | State | Guard, or where a breach shows |
| --- | --- | --- | --- |
| EVI1 | A durable artefact carries its provenance written down: source, method, when verified, how far to trust it (§1) | directive-only | diff, judgement: a claim in a file with no source beside it |
| EVI2 | An in-flight claim can answer for its provenance on demand, and a guess is labelled a guess unprompted (§1) | directive-only | invisible: the claim lives in a reply |
| EVI3 | A claim inherits the weakest tier it rests on; never present `ai-inference` or `secondary-commentary` with primary's confidence; un-sourced recall is `ai-inference` (§2) | directive-only | invisible in a reply; diff, judgement where it lands in a record |
| EVI4 | Record the acquisition method; a high-risk method under a claim that matters is confirmed a second way before it is reported settled (§3) | directive-only | invisible |
| EVI5 | A reported fact from one uncheckable source is marked unverified or left out (§4) | directive-only | invisible |
| EVI6 | Fact and interpretation are never blended without labelling which is which (§5) | directive-only | invisible |
| EVI7 | Draft, proposed or in-flight material carries a status and its next milestone, never the settled thing's weight (§6) | directive-only | invisible; diff, judgement in a record |
| EVI8 | Store the rule that produces a value, not the derived value; a cached value is tagged an estimate with a `last_verified` date (§8) | directive-only | diff, judgement |
| EVI9 | One fact, one home: cross-reference the single source by a stable identifier, never copy (§9) | directive-only | diff, judgement. `stampscan` reads declared copies of doctrine only, not facts |
| EVI10 | Renaming a referenced identifier means grepping its referrers first (§9) | enforced, partial (blocks, hook + CI) | `linkscan.py:resolve` blocks a Markdown link whose file or anchor no longer resolves; `pathscan.py:iter_candidates` warns on a backtick path. A renamed board id, scanner name or term referenced in plain prose: unseen |
| EVI11 | Every non-static fact names the event that forces re-verification and a calendar fallback; on a source change, dependants are re-checked and the change logged, never just the date bumped (§10) | directive-only | diff, judgement |
| EVI12 | Invest verification depth where the model is weak (traps, dated deltas, currency, local exposure), not on recall (§11) | directive-only | invisible, judgement |
| EVI13 | Where evidence lives in files a validator asserts the discipline and green is part of done; prefer a checkable file home for a claim (§12) | directive-only | invisible: an omission. No validator reads §1 to §11 over atelier's own records; the dating rule is the one checked (folded at REC28) |
| EVI14 | Climb the acquisition ladder to the cost of being wrong, record the rung stopped at, and state a blocked climb as a gap, never a settled claim; stakes outrank §11 (§13) | directive-only | invisible |
| EVI15 | A scanner delta compares per-finding output, never totals (§13, the principal's ruling of 2026-08-23) | directive-only | invisible; diff, judgement where a record reports a delta |
| EVI16 | A second party's agreement counts as corroboration only if it opened a source the first did not (§13) | directive-only | invisible |
| EVI17 | A missing value goes to the principal only when no authoritative source exists, sources genuinely conflict or the call is his by right; a lookup is done first (§13) | directive-only | invisible: the hand-up is an ask in the transcript |
| EVI18 | An instrument reports success only for what it confirmed, by read-back, never by exit 0 or the absence of an exception (§14) | directive-only | diff, judgement: the instrument's code |
| EVI19 | "Unknown" is a required output: a skipped target says skipped, a bounded sweep names what it dropped, an unreachable check returns unknown, never pass (§14) | enforced, partial (CI test, blocks the run) | `tools/test_unreadable_files.py` pins nine floor scanners to exit 2 on an unreadable file (`report.py`'s contract); the dropped-scope half is `report.py:suppressed_line` and `coverage_line` (counted at GRD23, GRD24). Instruments outside the floor: unverified |
| EVI20 | An instrument's output states how it knows and when, so a reader can tier it (§14) | directive-only | diff, judgement |
| EVI21 | A test drives an instrument through a known failure and asserts it reports the failure (§14) | enforced, partial (CI, blocks the run) | `.github/workflows/floor.yml` step `scanner selftests` runs every registry scanner's `--selftest` before the floor; `ReusableFloorWorkflowTest.test_selftests_run_before_the_floor` and `test_selftests_are_driven_by_the_registry` pin it. Whether each selftest holds a failing fixture: unverified. Instruments and other tools: diff, unguarded |
| EVI22 | A test of a belief about an external system counts as evidence only after an outside authority enters the loop; "mutation-verified" is quoted as wiring evidence only (§15) | directive-only | diff, judgement |
| EVI23 | A fixture of another program's output is captured, not typed, and the test records program, version and date captured (§16) | directive-only | diff: a parser fixture with no provenance line. The doc says nothing tells a captured fixture from a typed one; that is the capture half, and the recorded-provenance half is a presence a check could read |
| EVI24 | Run the check as its own command, read the output, then act, for any act (§17) | directive-only | invisible to the tree. The doc's ground for no guard, that nothing inspects a session's shell invocations, is contradicted by the `PreToolUse` hook that reads Bash command text (`tools/modelguard.py:offending`; board `115/410`), so it is not counted accepted. Before-plane reachable: a check chained by `&&`, `;` or a pipe to the act it guards. Also `CON21` |
| EVI25 | A negative result carries weight only after the same instrument shows a positive in the same run; mandatory before an irreversible act (§18) | enforced, partial (CI, blocks the run) | For the floor's own clean results only: the `scanner selftests` step proves each scanner fires on its fixtures before the floor's negative is trusted (EVI21's check). A session's own negative (an empty listing, a zero count): invisible |
| EVI26 | Before retrying a write after a client error, re-query the state; a re-query during the same outage is not corroboration (§18) | directive-only | invisible |
| EVI27 | An unhealthy transport is a reason to stop and re-establish; nothing concluded while it is down counts (§18) | directive-only | invisible |
| EVI28 | Before recording that something cannot work, run a cheap, safe, disposable test if one exists; if none does, label the verdict reading-only (§19) | directive-only | diff, judgement: an impossibility claim in a record with no test result beside it |
| EVI29 | State a negative per part and offer the part that works; a request for three things is not a set (§19) | directive-only | invisible |
| EVI30 | Before adding a resource, list the ones that exist; before inventing a pattern, read the file beside the one being edited (§20) | directive-only | invisible: the listing that was not run. The doc's "a lint cannot know the estate" is a commit-plane ground; a child's canonical resource file is the child's to build |
| EVI31 | A clean mechanical error profile is no evidence of a sound session; an instrument built from harness counters never reports "healthy" as if it had looked at trust (§21) | directive-only | diff, judgement: the instrument's output wording |
| EVI32 | A scanner of the agent's own logs keys a signal to a harness-set marker and a grouping to the recorded identity, never to prose or a resembling path (§21) | directive-only | diff, judgement (the doc says so) |

## ECONOMICS.md

| Id | Rule (section) | State | Guard, or where a breach shows |
| --- | --- | --- | --- |
| ECO1 | Read the marginal token's billing state off the current plan, never off habit (*Match the model to the job*) | directive-only | invisible |
| ECO2 | The cheapest model that can do a good job is used for every job, orchestration included: building on the cheapest-drawing tier that genuinely does it; review and the stuck hard problem on the capable or named tier | directive-only | record (the transcript's model id per seat) |
| ECO3 | Reviews are scoped and short: the reviewer gets the diff, range or named files, not the repo; findings, not rewrites; fixes applied on the building model | directive-only | record (the brief and the verdict) |
| ECO4 | A session picks its own tier and its sub-agents' tiers itself, states the tier, and does not ask the principal which to use | enforced, partial (harness hook, blocks) | A `PreToolUse` hook denies an `Agent` call with no `model` and a `claude` launch with no `--model` (`tools/modelguard.py:main`, `offending`; on this machine the wired file is a user-level copy, see the method). It makes the tier a choice; which tier, stating it, and not asking: invisible |
| ECO5 | Delegate for fan-out, parallel independent slices and fresh-context verification; not for a single known lookup, a tight loop, or work whose correctness turns on detail a report drops (*Sub-agents*) | directive-only | invisible, judgement |
| ECO6 | Once delegated, the work is not also done inline; the conclusion enters the main context, never the transcript | directive-only | invisible |
| ECO7 | Before token-heavy build work, state the running model, its billing state and its cap distance; unknown trips the guard; flag and confirm before spending when a guard trips (*the self-check*) | directive-only | invisible: the statement is in the reply |
| ECO8 | At a cap the session stops at a safe point, records, and hands the principal delay-or-pay (the confirmation itself folded at AUT18) | directive-only | invisible |
| ECO9 | Capacity never picks the tier: a cheaper model is lawful where the work's risk permits it and forbidden as a response to a low allowance (*Two hard edges*) | unenforceable, accepted | The same model choice is licensed or condemned by its reason alone, and the reason lives in the session's reasoning: outside every window, a before-plane included. `modelguard` sees that a model was named, never why |
| ECO10 | A private repo's CI capacity error is reported as an empty tank, not debugged as a broken workflow (*The compute pool*) | directive-only | invisible |
| ECO11 | The publish-safety floor fires on every push by default; trimming it is the estate's per-repo call, never atelier's to prescribe | enforced, partial (CI test, blocks the run) | `ChildFloorWorkflowTest.test_push_trigger_covers_every_branch` in `tools/test_templates.py` pins the shipped child template's push trigger to every branch. A child's edited trigger: instrument (`floorfleet.py` names a trigger that fires on nothing) |
| ECO12 | Cost never buys down safety; publication is never cost-driven; cost is optimised last (*Cost is the lowest precedence* folded) | directive-only | invisible: the motive |
| ECO13 | Each repo uses the cheapest runner class: every job Linux by default, a dearer class only for a narrow, isolated slice, never an OS matrix across every job (*Runner class*) | directive-only | diff: `runs-on` naming a macOS or Windows runner, or an `os:` matrix, in a workflow file. The templates default to Linux (`ci-python.yml`, `ci-static.yml`); no test pins it (none found) |
| ECO14 | Cancel superseded runs | directive-only | diff: a workflow with no `concurrency` group carrying `cancel-in-progress`. atelier's `ci.yml` and the child floor template carry it; the shipped `ci-python.yml` and `ci-static.yml` templates do not; nothing pins it |
| ECO15 | Path filters only where a job guards part of the tree, never on the publish-safety floor | directive-only | diff: a `paths` or `paths-ignore` key under the floor workflow's triggers. `test_push_trigger_covers_every_branch` reads `branches:`, not `paths` |
| ECO16 | No duplicate triggers: scope `push` to the branches that need it unless the second run earns its minutes | directive-only | diff, judgement on "earns": an unscoped `push` beside `pull_request` |
| ECO17 | Self-hosted or cloud runners only by a deliberate decision, never unprompted | directive-only | diff: `runs-on: self-hosted` or a runner label outside the hosted set |
| ECO18 | Price the job, not the token; when a hand-up looks likely, escalate up front (*One doctrine, tiered authority*) | directive-only | invisible |
| ECO19 | Hand-ups are noisy: state what was attempted and where the work exceeded the model, record it, route it up to the principal; never a silent stall or a degraded attempt | directive-only | invisible: an omission |
| ECO20 | In a run, the capable tier orchestrates and reviews and the workhorse executes; first-of-kind, structural and doctrine-text items escalate to the capable tier (*The orchestrated-run tier split*) | directive-only | record (the workers' model ids against the item class) |
| ECO21 | Fan-out runs below the workhorse on the cheapest tier that genuinely does it, never as a response to a low tank | directive-only | record (sub-agent model ids) |
| ECO22 | The executor seat steps down only by a per-run trial kept on the floor's evidence; the mid tier executes known patterns and prescriptive fixes; a novel mechanism keeps capable-tier verify-at-merge | directive-only | record |
| ECO23 | Ceremony matches the cost of being wrong: self-verifying work over reviewed machinery does not earn its own brief-to-verdict cycle (*Match the ceremony to the risk*) | directive-only | invisible, judgement |
| ECO24 | Don't stack: no gate is built on unreviewed tooling or doctrine; a new scanner is reviewed before it is wired into CI | directive-only | record: a registry entry added in `tools/floor.py` read against the review files for that scanner |
| ECO25 | Stay in one line of work; an unrelated pivot earns a fresh session; never break only because one item went green (*Session hygiene* item 1) | directive-only | invisible |
| ECO26 | Never switch model mid-session (item 2) | directive-only | record: two model ids in one transcript. Instrument: `ccclose` lists the models its transcript stream saw, and checks nothing |
| ECO27 | Mind the cache TTL (item 3) | directive-only | invisible |
| ECO28 | Reset by record, not by compaction: write the session record, then restart; in-place compaction is a rescue; a bare wipe only after the record (item 4) | directive-only | invisible |
| ECO29 | Heavy skills are not invoked speculatively, above all on a usage-billed session (item 5) | directive-only | invisible |
| ECO30 | Point, don't paste (item 6) | directive-only | invisible |
| ECO31 | Surface a session boundary rather than cross it silently; under overload pick a safe stopping point, record, put the work away, hand the rest on (item 7) | directive-only | invisible |
| ECO32 | The estate's own numbers (model roster, prices, CI allowance, session overhead) stay person-local, never in this doc (header and foot) | directive-only | diff, judgement: a price or plan figure added to doctrine |

## COMMUNICATION.md

| Id | Rule (section) | State | Guard, or where a breach shows |
| --- | --- | --- | --- |
| COM1 | Keep a maintained calibration in the principal's person-level layer, covering the axes the doc lists (*Two things, kept separate*; *The axes*) | directive-only | invisible to the repo |
| COM2 | The calibration is person-local and pointed at, never copied into any repo, a private one included; the scrubbed snapshot is the one sanctioned exception (*Person-local, pointed at, never copied*) | enforced, partial (blocks, hook + CI) | `leakscan.py:scan_lines` blocks personal-data shapes and the machine-local terms; `pdlistscan.py:scan` reads public repos against the closed list (warns until 2027-03-08). A calibration's style lines carry no shape: unseen |
| COM3 | Maintain it like a record: a reply that lands notably well or badly is written back, dated (*Maintain it like a record*) | directive-only | invisible to the repo |
| COM4 | Defaults to serve, not rules to recite; ordering, tone dosage, icon aptness, survey against recommendation stay judgement (*Defaults to serve*; *What stays judgement, honestly*) | unenforceable, accepted | The doc's own ground: none of it is checkable, "and no scanner should pretend otherwise". The deciding fact is a reader's reaction, outside any window |
| COM5 | Before sending, introduce once every term a reader could not have met (*Accessibility of the language*) | unenforceable, accepted | A check built 2026-08-09 fired on 90.6% of 6,764 replies and was deleted the same day: a reader's knowledge spans years and is outside any one text (`020/270`). One attempt on one corpus, the doc says |
| COM6 | The machine-decidable prose rules: no reference code before its meaning, no unexpanded acronym, no mid-sentence bracketed aside, sentences within length | unenforceable, accepted | A recorded decision not to build, as REV42: `plainscan` removed 2026-09-18 for noise nobody acted on, and the reply plane destroyed because a `Stop` hook cannot retract a streamed reply (board `020/360`). Detectable, no deliverable remedy on the reply plane |
| COM7 | Before calling write-time discipline the only control, check whether the rule is machine-decidable; before enforcing it, check that the enforcement point can deliver the fix | directive-only | diff, judgement: a doctrine claim of unenforceability, or a new check, with no such test recorded |
| COM8 | Before asking, establish there is a decision: evidence that settles it is reported, never voted; absent evidence offers "find out first" (*Asking for a ruling*) | directive-only | invisible |
| COM9 | When he answers the frame instead of the question, stop asking in that shape and re-examine the form | directive-only | invisible |
| COM10 | Every ask goes through the structured decision device where one exists; with none, the same content as prose | directive-only | invisible: a prose ask leaves no device call |
| COM11 | The account is written as text first and the device carries the choice alone, in the same turn; the turn never ends between them; the account is never trimmed to fit, and one only read from a file has reached nobody | directive-only | invisible. Before-plane reachable in part: a hook on the device could read whether the turn wrote text first |
| COM12 | A decision genuinely his is an options question, never one option to countersign; the options are real, not only do-nothing or pass-elsewhere | directive-only | invisible, judgement |
| COM13 | The device's fields are content: options labelled accurately, the owed recommendation marked, an overrule offered as keep, modify or stand aside, a taste-based recommendation saying so | directive-only | invisible. Before-plane reachable in part: a marked recommendation in the payload |
| COM14 | One question at a time; the tool's ceiling is never a target | directive-only | invisible. Before-plane reachable: the question count in the device payload |
| COM15 | The long form goes in session text; the box holds the question, options and recommendation; no option previews | directive-only | invisible. Before-plane reachable: description length and preview fields |
| COM16 | The box makes sense on its own: proof-read, no reference ids, document numbers or unexplained acronyms; quote a short text under decision | directive-only | invisible. Before-plane reachable: an id shape (`020/220`, a finding prefix) in the payload |
| COM17 | Answer what he asked before putting a choice | directive-only | invisible |
| COM18 | Check parallel sessions before asking (`CONCURRENCY.md` § *The channel*) | directive-only | invisible. Instrument: `cclive` |
| COM19 | A line recording his decision carries a mark: ⚖️ with his quoted words and their context, or 💬 with the pick quoted, who offered the options and "an answer, not a ruling" (*The record marks*) | directive-only | diff: a decision line added with neither mark. Nothing reads the marks |
| COM20 | A pick is never written as a ruling; words typed in reply to a question are an answer unless he says otherwise | enforced, partial (warns until 2027-02-08, hook + CI) | `attribscan.py:scan_text` reports the attribution word with no quotation, citation or demotion within three lines. A pick written that way beside a board id passes, because a board id is a citation: the commonest shape escapes |
| COM21 | Sort each question by what it blocks: nothing, take the reversible default and say so; one branch, park it in the durable record and proceed; the whole run, ask it first while he is present (*When to ask*) | directive-only | invisible |
| COM22 | Proceed on an assumption only where the work is recoverable; name it in the record and repeat it in the end-of-run ask | directive-only | invisible |
| COM23 | A floor item never proceeds on assumption, whatever "don't stop to ask" says; it queues | directive-only | invisible. The floor acts are AUTONOMY's rows |
| COM24 | Away is a mode only his words declare; declared, the parked-asks cadence binds the whole run; absent it, ask through the device | directive-only | invisible |

## DATA-PROTECTION.md

| Id | Rule (section) | State | Guard, or where a breach shows |
| --- | --- | --- | --- |
| DAT1 | Where an act is irreversible, a tool's own report is not sufficient: corroborate from the artefacts (*Where the act is irreversible*) | directive-only | invisible (the doc: no scanner) |
| DAT2 | Never overwrite an executable a running invocation is reading; write a new path and rename, or version the name | directive-only | invisible: the act is a session's write at run time |
| DAT3 | A tool that rewrites itself or a sibling script follows write-then-rename | directive-only | diff, judgement: an in-place write in a tool's code |
| DAT4 | Where a system separates data from control, hold two scoped credentials, the control one unable to touch the data (*The data plane is the slow lane*) | directive-only | invisible to the repo; record on the platform's token scopes |
| DAT5 | Prefer reproducible state; keep the irreplaceable set small and guard it hardest (*Reproducibility is data insurance*) | directive-only | invisible, judgement |
| DAT6 | Third-party and personal data: hold the minimum, never widen its exposure, never move it somewhere less protected, honour deletion and retention (*Other people's data*) | enforced, partial (blocks, hook + CI) | Into git only: `leakscan.py:scan_lines` blocks personal-data shapes; `publishscan.py:matches` refuses tracked logs, databases and dumps. Every move outside git: invisible |

## Directive-only rules, grouped by where a breach shows

**Diff-visible (20).** EVI1, EVI8, EVI9, EVI11, EVI18, EVI20, EVI22, EVI23,
EVI28, EVI31, EVI32; ECO13, ECO14, ECO15, ECO16, ECO17, ECO32; COM7, COM19;
DAT3. All but EVI23, ECO13, ECO14, ECO15, ECO17 and COM19 need judgement a
scanner cannot make, and stay review work. ECO16 is diff-visible and needs
judgement only on whether the second run earns its minutes.

**Record-visible (7).** ECO2, ECO3, ECO20, ECO21, ECO22, ECO24, ECO26.

**Invisible (54).** EVI2 to EVI7, EVI12 to EVI17, EVI24, EVI26, EVI27, EVI29,
EVI30; ECO1, ECO5 to ECO8, ECO10, ECO12, ECO18, ECO19, ECO23, ECO25, ECO27 to
ECO31; COM1, COM3, COM8 to COM18, COM21 to COM24; DAT1, DAT2, DAT4, DAT5. Of
these, EVI24 is an act a before-plane hook could read from the command text,
and COM11, COM13, COM14, COM15 and COM16 are asks a hook on the question
device could read from its payload: the class `115/100` is about. COM14 and
COM16 are machine-decidable outright (a question count; an id shape), and a
`PreToolUse` deny reaches the session before the principal sees the box, so
unlike the removed reply plane the remedy is deliverable.

## Counts

| Doc | Rules | enforced (of which partial) | blocks | warns | directive-only | diff | record | invisible | unenforceable, accepted |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| EVIDENCE.md | 32 | 4 (4) | 4 | 0 | 28 | 11 | 0 | 17 | 0 |
| ECONOMICS.md | 32 | 2 (2) | 2 | 0 | 29 | 6 | 7 | 16 | 1 |
| COMMUNICATION.md | 24 | 2 (2) | 1 | 1 | 19 | 2 | 0 | 17 | 3 |
| DATA-PROTECTION.md | 6 | 1 (1) | 1 | 0 | 5 | 1 | 0 | 4 | 0 |
| Slice 3 | 94 | 9 (9) | 8 | 1 | 81 | 20 | 7 | 54 | 4 |
| Slice 2 | 129 | 27 (19) | 15 | 12 | 101 | 36 | 23 | 42 | 1 |
| Slice 1 | 158 | 19 (11) | 14 | 5 | 133 | 35 | 33 | 65 | 6 |
| Running total | 381 | 55 (39) | 37 | 18 | 315 | 91 | 63 | 161 | 11 |

As in slices 1 and 2: *diff*, *record* and *invisible* split the
directive-only count, each rule once, under the place a breach first shows.
*blocks* includes the CI test pins (EVI19, EVI21, EVI25, ECO11), which fail the
run after a push rather than refusing the commit, and ECO4's harness deny,
which refuses the call before it runs. A rule whose checks mix both responses
is counted at its strongest (COM2 blocks through `leakscan`; its `pdlistscan`
half warns). The running total counts one rule twice, EVIDENCE §17 as EVI24
and as `CON21` (method step 4); net of it, 380 distinct rules.

Reading the table. Slice 3 is the least enforced of the three: 9 of 94 rules
(10%) have any check, and every one of those covers only part of its rule.
That is the shape of these documents. EVIDENCE governs claims, and most claims
live in replies, which its own §12 says no validator can reach; it states that
"the rules above are only real if something checks them", and of §1 to §11
the one checked is the dating rule, through `RECORD.md`'s copy. ECONOMICS
governs model choice and session conduct, which leave a model id in a
transcript at most; its one harness-plane check (ECO4) is the first in the
census that blocks before the act, and it is wired from a copy. COMMUNICATION
is where the house tried hardest and stopped deliberately: two planes built
and removed, three rules accepted on recorded grounds. What it leaves is the
ask itself, and five of its rules are readable before the principal sees the
box. Across the three slices, 14% of the 381 rules counted have any mechanical
check, and 39 of those 55 cover only part of the rule.

## Top five guard candidates

Directive-only, breach visible in the diff, and costly when it happens:

1. **ECO15, a path filter on the publish-safety floor**: a `paths` or
   `paths-ignore` key added under a floor workflow's triggers leaves every push
   outside the filter unscanned, in a tree that publishes wholesale. The
   template test already reads that block for `branches:`; the same read
   could refuse `paths`.
2. **ECO17, a self-hosted runner added unprompted**: `runs-on: self-hosted`
   in a workflow. On a public repo a fork's pull request can run code on the
   runner's host; it is also spend and a new trust surface (`AUT16`) the doc
   holds for a deliberate decision.
3. **ECO13, a dearer runner class across platform-independent jobs**: a
   `runs-on` naming macOS or Windows, or an `os:` matrix over every job, in a
   private repo's workflow burns the allowance at up to ten times the Linux
   rate and, with billing attached, fails open into overage.
4. **COM19 with COM20's gap, a decision recorded with no mark**: a line
   recording the principal's decision with neither ⚖️ nor 💬. A pick recorded
   under his authority turns a session's framing into binding doctrine, the
   loop `COMMUNICATION.md` describes; `attribscan` reads one word and passes it
   beside any board id.
5. **EVI23, a captured-output fixture with no provenance**: a fixture for a
   parser of another program's output, added with no program, version or
   capture date. Captured-against-typed stays review work; the missing record
   is a presence check, and a typed fixture passes forever while wrong.

Next after these: ECO14 (a workflow with no superseded-run cancel), ECO16 (an
unscoped `push` beside `pull_request`), ECO32 (a price or plan figure in
doctrine). The before-plane pair COM14 and COM16 rank above all five on cost
to the principal's attention, but they are not diff-visible; they belong to
`115/100`'s list.

## Doctrine defects found, not fixed here

Each is owed its own board item (`PROPAGATION.md` § *Pointing up*) where it
has none; none is changed by this file.

- **EVIDENCE §17's stated ground for no guard is false** (EVI24): "nothing
  inspects a session's shell invocations", while a `PreToolUse` hook reads
  Bash command text before it runs. Already filed: board `115/410`.
- **EVIDENCE §19 says a pointer is still owed that has landed.** Its last
  sentence reads that a pointer from `REVIEW.md` § *Re-run every "live-proven"
  claim* to §19 "is still owed". `REVIEW.md` carries it ("The negative
  counterpart is `EVIDENCE.md` §19", `320/570`), committed minutes after §19.
  A stale claim in doctrine, the sweep `00-APEX.md` asks for in the same commit.
- **EVIDENCE §7's banned words and the house's date guard disagree,
  unrecorded.** §7 bans `recently`, `new this year` and `currently`;
  `datescan` excludes `recently`, `currently` and `soon` on purpose, and the
  doctrine uses them undated (`ECONOMICS.md` § *The orchestrated-run tier
  split*: "as this estate currently fills it"). Either §7 overstates the rule
  or the exclusion is a gap §7 should name; neither file says which.
- **ECONOMICS keeps the model roster person-local and names it.** Its header
  and foot say the exact models stay out of this doc; its body names the
  estate's review tier and mid tier by product name, each marked as the
  present filling. If naming the tier is intended, the foot overstates.
- **DATA-PROTECTION's write-then-rename rule has no home.** It says the
  convention "belongs in whatever governs how a tool is written"; no file
  under `docs/build/`, `docs/method/`, `skills/` or `commands/` carries it
  (searched by phrase). A rule assigned to an unnamed home is
  `GUARDS.md` § *A rule with no home*'s class.

## Doubts and unverified points

- **The guard ECO4 counts runs from a second copy.** The wired hook is a
  user-level file outside atelier whose text differs from `tools/modelguard.py`;
  the census did not diff the two for behaviour, only read that both deny an
  unnamed model on `Agent` and `claude` launches. Atelier's own file is wired
  by nothing on this machine. That is a one-source question (EVI9), recorded
  here rather than counted.
- **Slice 2's AUT14 may be stale by one commit.** `quotescan`'s authority
  surfaces (a warn-only line on any change to `docs/method/AUTONOMY.md`, the
  floor region and settings `permissions`, board `115/110`) reached `main`
  minutes before slice 2's own commit, after its worktree was cut. Slice 2
  counts AUT14 directive-only; at this census it reads enforced, partial,
  warns. The running total keeps slice 2's figure.
- **COM6 and COM4 counted as accepted** follow slice 1's REV42 precedent: a
  recorded decision not to build counts as accepted, not as an unexamined gap.
  A stricter reading would count COM6 directive-only, diff-visible on the
  committed prose plane.
- **Rule boundaries are a judgement**, as in slices 1 and 2; the folds are
  named in the method and in the rows.
- **Unverified**: whether every floor scanner's selftest holds a failing
  fixture (EVI21, EVI25); whether instruments outside the floor honour the
  unknown-output contract (EVI19); whether the device's own schema already
  refuses a single option (COM12).
- **Self-run instruments** were counted directive-only, as before.

## Remaining docs for later slices

`docs/method/`: `ACCESS.md`, `CONVENTIONS.md`, `DOCUMENTATION.md`,
`GLOSSARY.md`, `MECHANISMS.md`, `PRINCIPLES.md`, `REACH.md`, `SECRETS.md`,
`SIGNING.md`, `STORAGE.md`, `TOOLBOX.md`, and `docs/method/session-open/`.
Then, on `REVIEW.md` rule 3's definition, the doctrine outside `docs/method/`:
`docs/build/`, the ADRs, the skills and commands, the templates and the
validators' own stated rules.
