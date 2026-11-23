# Enforcement census — ACCESS, CONVENTIONS, DOCUMENTATION, GLOSSARY, MECHANISMS, PRINCIPLES

Board item `020/220`, slice 4 of the census. Run 2026-11-23 (UTC) by a worker
of queue run 608d. This is a measurement record, not doctrine: it changes no
rule, and it builds no guard. It uses slice 1's method, states and row format
(`docs/method/census/2026-11-16-1142-record-review-concurrency.md`) and the
fold conventions of slices 2 and 3
(`docs/method/census/2026-11-16-1204-apex-autonomy-guards-propagation.md`,
`docs/method/census/2026-11-16-1220-evidence-economics-communication-data.md`),
so the four slices add up.

## What this asks

For each rule in six governing documents: if it is broken, what sees it? Each
rule gets one state, defined as in slice 1.

- **enforced**: a mechanical check reads the breach. The row names the check,
  the plane it runs on (the pre-commit hook, the commit-message hook, CI, a
  harness hook, a session-open hook) and whether it **blocks** or **warns**.
  *partial* means the check covers some of the rule and the rest is
  unguarded.
- **directive-only**: nothing mechanical sees a breach. Where a self-run
  instrument would report it if a session chose to run it, the row says
  *instrument* and the state stays directive-only: nothing invokes those
  tools, so nothing sees the breach unless the breaker looks.
- **unenforceable, accepted**: the fact that would license or condemn the act
  is outside any check's evidence window (`GUARDS.md` § *Before building a
  check: the evidence window*), or the house has recorded a decision not to
  build the check, and the reason is stated. Accepted as of 2026-11-23.

A directive-only rule also gets the place its breach could be seen, as in
slices 1 to 3: **diff** (the committed change itself), **record** (only by
joining records outside one diff) or **invisible** (nothing in the tree or the
repo's records).

## Method, and what it did not do

1. Read `ACCESS.md`, `CONVENTIONS.md`, `DOCUMENTATION.md`, `GLOSSARY.md`,
   `MECHANISMS.md` and `PRINCIPLES.md` in full at the commit the worktree was
   cut from. Each sentence that tells a future agent to do or not do
   something is a rule. Not counted: grounding stories and cases, history
   and status notes, the teaching example in `PRINCIPLES.md` §11, the quoted
   statement in §10, the three worked readings and the *Not decided here*
   paragraph in `MECHANISMS.md`, descriptions of what a mechanism or a
   Diátaxis mode is, and pure permissions (the peer adopter substituting its
   own defaults; the bare `/atelier` menu as the one user-level exception).
   `GLOSSARY.md`'s definitions are not rules; only its four sentences about
   how the file itself is kept are.
2. **Cross-slice folds.** A rule these files restate from a censused document
   is not counted again. Folded here:
   - `ACCESS.md` step 1 (the grant is the owner's, recorded, never
     originated, one domain per approval) into `AUT14`, `AUT15` and `AUT22`;
     step 2's two scoped credentials into `DAT4`; step 4's contradiction
     stops you into `AUT32`; step 5's "encode it" into `AUT31`; step 6's
     capable-model-first into `AUT29`; step 7's Zero Trust half into `PRI24`;
     step 2's standing-credential debt clause into `PRI21`.
   - `CONVENTIONS.md`'s `YYYY-MM-DD` and no-relative-date half into `REC28`;
     its UTC-date half into `REC29`; its "the onramp is a pointer" into
     `EVI9`.
   - `DOCUMENTATION.md` principle 1 and principle 4 into `EVI9` and `PRO15`;
     principle 2 into `REC1` (with `PRO1`); principle 3 into `APX2` and
     `REC3`; the AI-consumer section's "point, do not re-derive" into `EVI9`;
     its "children apply and never silently contradict" into `PRO12`; the
     doctrine-tooling-is-a-platform bullet into `AUT25`.
   - `GLOSSARY.md`'s entries restate rules already counted: *Cold review*,
     *Intent record* and *Delta* into the `REV` rows; *Child*, *Bearing*,
     *Thin anchor* and *Floor* into `PRO2`, `PRO12` and `PRO14`; *Harvest*
     into `APX17`; *ADR* into `REC17`; *Worked case* into `APX15`; *Stated
     bridge* into `PRI30` here.
   - `MECHANISMS.md`'s "doctrine text is the zeroth option: say it once, in
     its home, and point at it" into `EVI9`.
   - `PRINCIPLES.md`: DRY into `EVI9`; build the way back before the way
     forward into `AUT12` (and `DAT1` to `DAT3`'s neighbourhood); "secrets
     never land inline" into `AUT10`; personal data "held only for a recorded
     purpose" into `DAT6`; cost "a written policy" into `ECO7` and `AUT18`;
     observable by design into `APX1`, `EVI19`, `GRD23` and `GRD24`; every
     fact carries provenance and every claim its test into `EVI1`, `EVI11`
     and `APX2`; prevention or cheap failure, and the §10 requirement on every
     guard, into `GRD1` and `GRD2`; §11's "cannot work from reading alone" into
     `EVI28`; the precedence ladder's rung 2 into `APX2`; the situation tests
     "timer vs event", "state vs stateless", "codified or hand-done",
     "standing or ephemeral credential", "one-off or recurring" and "whose
     failure is it" into the principle each applies (`PRI16`, `PRI17`,
     `PRI30`, `PRI21`, `PRI32`, `PRI5`).
3. **`SECRETS.md` is not censused yet.** `ACCESS.md` steps 2, 3 and 7 restate
   it ("one credential, one entity, one system"; "right plane"; cheap
   rotation). They are counted here as `ACC` rows. When `SECRETS.md` is
   censused its restatements should fold into `ACC2`, `ACC3` and `ACC8`
   rather than count twice, the same way slice 3 handled `EVIDENCE.md` §17.
4. Listed every check that could see a breach: the floor registry
   (`python3 tools/floor.py --list`: 19 entries), both workflows and the
   shipped workflow templates, the tests that pin them
   (`tools/test_templates.py`), the harness and session-open hooks
   (`tools/modelguard.py`, `tools/prefixhook.py`, `tools/idhook.py`,
   `tools/floorhook.py`, `tools/stashscan.py --hook`) and what this machine's
   user-level Claude Code settings actually wire, and the self-run
   instruments.
5. Before writing *enforced* against a rule, read the code that does it and
   cite it as file and function. Before writing *directive-only*, looked for
   the check by name and by the phrase the rule uses, in `tools/`,
   `instruments/`, `.github/`, `docs/build/templates/`, `skills/` and
   `commands/`.
6. Measured where a measurement would say whether a candidate guard would
   fire on the live tree (the figures are in the rows and the candidates).
   They are counts from this worktree's tracked files at the commit it was
   cut from, taken by grep and a small AST pass, not by a scanner.
7. Did not read `docs/SESSIONS.md` or `docs/sessions/` (the run's bounds).

**On the session-open and harness hooks.** The user-level settings read at
this census wire `tools/prefixhook.py` and `tools/idhook.py` as `SessionStart`
hooks and `tools/modelguard.py` as a `PreToolUse` hook on `Agent|Bash`, all
three from the primary checkout of this repo. Slice 3 recorded the
`modelguard` hook as a user-level copy of a different text and left a
one-source question open (`ECO4`). At this census the wired file is atelier's
own, so that question is closed for this machine. `ECO4` stays as slice 3
counted it. `prefixhook` is the only session-open hook any row here depends
on (`MEC5`); a clone of this repo on another machine has none of it, because
no `hooks.json` ships in `.claude-plugin/`.

## ACCESS.md

| Id | Rule (section) | State | Guard, or where a breach shows |
| --- | --- | --- | --- |
| ACC1 | Walk the onboarding sequence in order; no step's power exists before the earlier step's guard (*The onboarding sequence*, *The gate, in one line*) | directive-only | invisible: the order is in a session's acts on a system outside the repo. The doc's "invents no new rule" claim is checked above: its one owned exception is `ACC5`; the rest fold or are counted below |
| ACC2 | Take the narrowest credential that does the job, minted fresh for this domain: never reused from another system or shared with another entity, never an admin-all credential because the platform offered one (step 2) | directive-only | invisible to the repo: scope and reuse are platform facts. A scope claim written into a repo file is judgement on the diff. `SECRETS.md`'s own copy folds here when censused (method 3) |
| ACC3 | The credential's value lives only in the encrypted store; config, inventory and code hold a reference; its mint and rotate procedure is written before connecting (step 3) | enforced, partial (blocks, hook + CI) | The value half: `secretscan.py:scan_text` blocks a credential value in a tracked file (counted at `AUT10`), and `publishscan.py:matches` refuses a tracked environment file. Store-first ordering and a procedure written before connecting: unseen |
| ACC4 | The first ring is read-only: enumerate and reconcile before touching anything, and no write of any kind in the first ring (step 4) | directive-only | invisible: the reads and writes are on a system outside the repo. A write command in the session is before-plane reachable only where the hook can read the command text; the first-ring state is not in it |
| ACC5 | The destructive gate is encoded as a check the tooling enforces before the write credential goes live, not before the destructive operation: the doc's one owned tightening of `DATA-PROTECTION.md` (step 5) | directive-only | invisible: "before the credential goes live" is an event on a platform. Where the gate lands as tool code, the tool's own check is diff, judgement |
| ACC6 | Where a platform issues only one broad credential, hold the first ring behaviourally, encode the gate before any write is performed, and name the gap as tracked debt (step 5, *The honest fallback*) | directive-only | record: the debt belongs in the instance's debt list, which is off-repo (ACC9) and so cannot be read here |
| ACC7 | Widen in rings, read then additive and reversible writes then destructive: a ring opens only after the prior one proved safe and the next ring's gate is in place; never jump to the widest ring the credential permits (step 6) | directive-only | record: how far each domain's rings have been walked is held in the instance's access map (off-repo). `PRI63` is the same shape for change rollout |
| ACC8 | Treat a new domain as untrusted until proven, assume the credential can leak, and design cheap rotation and a bounded cadence in from the first connection (step 7) | directive-only | invisible. The Zero Trust half is `PRI24`; the rotation half is `SECRETS.md`'s (method 3) |
| ACC9 | The estate access map, the per-domain mint and rotate procedures and the standing-credential debts live in the instance, protected under `DATA-PROTECTION.md`, never in this repo; each onboarding extends the map (*What lives elsewhere*) | enforced, partial (blocks, hook + CI) | What would put it here: `leakscan.py:scan_lines` blocks the shapes such a map carries (an IPv4, a MAC, an email, a listed host or device term from the machine-local list) over content and paths, and `secretscan` the credential values; it reads shape and listed terms, not purpose, so a prose map with no address and no listed term passes. That each onboarding extends the map: invisible (off-repo) |

## CONVENTIONS.md

| Id | Rule (section) | State | Guard, or where a breach shows |
| --- | --- | --- | --- |
| CNV1 | Declare a default frame once, at the boundary where the values live, and carry it silently from there; no per-value label (rule 1) | directive-only | diff, judgement: a doc, schema or column carrying a time, price or measurement with no default declared anywhere above it |
| CNV2 | Label a deviation from the declared default, or a collision where several frames coexist with no default; where a mislabel is costly, labelling every value is the deliberate exception (rule 2) | directive-only | diff, judgement. `datescan` flags a non-ISO date shape (folded at `REC28`), not a missing label |
| CNV3 | Preserve data we do not own as received, and record its frame as metadata alongside, never rewritten into the payload (ELT, not ETL); this outranks normalising to the default (rule 3) | directive-only | invisible: the act is a session's ingest. The clause says no repo under the doctrine has a live ingestion surface yet; the first one is its proving ground |
| CNV4 | Time is UTC at rest and local on presentation, labelled where doubtable; record identifiers are UTC-forward (*The declared defaults*, Time) | directive-only | diff: a machine timestamp carrying a non-`Z` offset or no designator. A local clock reading stamped `Z` is `REC29`'s accepted ground. Measured: 6 tracked files outside the record stores hold a `T` stamp with no designator (test fixtures, and an example config whose key `reset_utc` names the frame) |
| CNV5 | Currency is NZD; a bare `$` is NZD; another currency is labelled (Currency) | directive-only | diff, judgement: a `$` figure in a doc that means another currency, or a foreign amount with no code |
| CNV6 | Machine-authored timestamps are strict ISO 8601 with `T` and `Z`; record identifiers use the filename-safe `YYYY-MM-DD-HHMM`; prose stamps are `YYYY-MM-DD` plus `HHMM UTC` (Date and time format) | directive-only | diff: a stamp in the wrong one of the three shapes. `datescan.py` reads the date half (`non-iso-date`, `invalid-iso-date`, folded at `REC28`); `indexscan.py` warns on an `HHMM` that predates its file, in opted-in indexes only. Nothing reads the `T`/`Z` shape or a colon in an identifier |
| CNV7 | Text is UTF-8; a tool that mangles `Māori` is a silent frame break (Text encoding) | directive-only | diff: a tracked text file with non-UTF-8 bytes or U+FFFD. `wrapscan`, `spellscan` and `leakscan` decode with `errors="replace"`, so an undecodable file is read lossy and reported clean, not unknown (`EVI19`'s contract covers unreadable files, not undecodable ones). Measured: all 1751 tracked text files decode strictly; 2 test files hold U+FFFD on purpose |
| CNV8 | Spell in New Zealand English: organise, licence (Language / dialect) | enforced, partial (blocks, hook + CI) | `spellscan.py` denylist of US-to-NZ alternations, blocking on both planes. Scope is `docs/method`, `docs/build` and `docs/decisions` only (`.atelier-floor.json`, scope declared with its reason): `skills/`, `commands/`, tool docstrings, `README.md` and the frozen record stores are unread. A curated list, not exhaustive |
| CNV9 | Macrons (tohutō) on te reo Māori words and place names are correct (Language / dialect) | directive-only | diff: a te reo word without its macron. `spellscan.py` says so itself: out of scope, it would need a wordlist. Measured: no unquoted `Maori` in any tracked file; the four hits all name the misspelling |
| CNV10 | When a default changes, date the change in the table: a default is safe only while it is the current stated one (*What lives elsewhere, and maintenance*) | directive-only | diff: an edit to the defaults table with no dated line beside it |

## DOCUMENTATION.md

| Id | Rule (section) | State | Guard, or where a breach shows |
| --- | --- | --- | --- |
| DOC1 | Extend Diátaxis where it is silent; do not contradict it (*The what/who*) | directive-only | invisible, judgement |
| DOC2 | Name the developer cell separately from the expert user: the reader who extends a tool needs explanation (architecture and purpose docs, why-comments, ADRs), not only deeper reference (*The what/who*) | directive-only | diff, judgement: a repo whose docs are reference only. Presence of an `ARCHITECTURE.md` is a child's file standard (`docs/build/REPO-STANDARD.md`), not read by any floor check |
| DOC3 | The machine contract (`--json` shapes, exit codes, flag names) is documented and versioned like an API, complete and stable; a schema change moves its version, because a broken schema is a documentation failure (*The consumer axis*, *What great means per cell*) | directive-only | diff: a changed `--json` payload with no version move. Measured: no `--json` payload in `tools/` or `instruments/` carries a version field (31 of 47 non-test tools emit one); see the defects |
| DOC4 | The machine contract carries the entire result (findings, provenance, what would prove it wrong, what was skipped), never a lossy subset of the human render; the human view is a rendering of the machine truth, never the reverse (*Grounding*) | directive-only | diff, judgement: the payload built beside the text it renders. Partly held by habit: the `linkscan` payload carries findings, suppressed counts and coverage. The skipped-and-dropped half is `EVI19`'s and `GRD23`'s |
| DOC5 | Each artefact serves one cell of the two axes; no artefact serves everyone; the artefact is the one its cell needs, nothing grander (*What "great" means per cell*, *The artefact inventory*) | directive-only | invisible, judgement |
| DOC6 | An error message states what is wrong, why, and what to do, as data where a machine consumes it (named cause, evidence, remedy, not a bare stack trace); an error that guesses is worse than one that says what it checked (*Two cells earn emphasis*) | directive-only | diff, judgement: a raised string or printed error in tool code |
| DOC7 | Meet the reader at the point of need and at their altitude: the error at the failure site, the docstring at the call site, the `--help` at the prompt (principle 5) | directive-only | invisible, judgement |
| DOC8 | Word a rule for the moment of decision: its own sentence names the situation the reader will be standing in, then the act, and is not keyed to a condition a scanner could evaluate; it binds new and changed rules as a review question, with no scanner (principle 6) | directive-only | diff, judgement: a rule written as "no X in file Y". The census answer the doc asks for: no scanner is worth building, because the breach is a sentence's meaning; the question has no home yet (see the defects) |
| DOC9 | The situation is a clause in the rule's own sentence, never a directive preamble bolted onto each rule; a rule that would need a paragraph to name it is reworded or split, not padded (principle 6) | directive-only | diff: an identical opening repeated across rules is a string a grep can read; whether a clause earns its place is judgement |
| DOC10 | A child's docs cover its own intent and live-proven deltas; for the platform's semantics they point to the vendor's docs and never mirror them: ship the harvester, not the harvest (*The vendor-docs seam*) | directive-only | diff, judgement: a block of vendor text copied into a doc. The wrapper documents the wrapping, never the wrapped |
| DOC11 | The child owns the seam: the quirks, version-specific behaviours and API gotchas it has live-proven against the platform are documented where the vendor's docs are wrong, silent or surprising (*The vendor-docs seam*) | directive-only | invisible: an omission |
| DOC12 | A pointer to vendor docs carries its own proving rung ("verified against" a named version), not a bare link (*The vendor-docs seam*) | directive-only | diff: a vendor link in a doc with no version or verification beside it. `linkscan` reads whether an internal link resolves, not what an external one is pinned to |
| DOC13 | A durable doc is read cold by unknown consumers, so it declares its altitude and carries its own context rather than leaning on a known reader (*Relationship to COMMUNICATION.md*) | directive-only | diff, judgement |

## GLOSSARY.md

| Id | Rule (section) | State | Guard, or where a breach shows |
| --- | --- | --- | --- |
| GLO1 | A term already defined canonically elsewhere gets a pointer line, never a duplicate; only terms with no single canonical home are defined in full (opening) | directive-only | diff, judgement: a second definition of a term in another file. `linkscan.py:resolve` blocks a pointer whose file no longer exists, not one whose section name has drifted |
| GLO2 | A term earns an entry when it carries intent across two or more docs (the admission rule) | directive-only | diff, judgement: a new entry for a one-doc term |
| GLO3 | Until the principal's ratify pass, entries are recommendations, not doctrine (the status banner) | directive-only | record: board item `160/120` holds the owed pass; nothing stops an agent citing an entry as ruled |
| GLO4 | The listed terms carry one precise, non-interchangeable meaning: use *cold review* for a pass whose spawn meets rule 4 and not for fresh context alone, *floor* for the inlined subset, and so on (opening, *Process*) | directive-only | diff, judgement: a doc using a defined term in a looser sense. Nothing reads term usage |

## MECHANISMS.md

| Id | Rule (section) | State | Guard, or where a breach shows |
| --- | --- | --- | --- |
| MEC1 | Choose a mechanism for a new need on purpose, by the four axes in the order given: blocked or judged; automatic or deliberate; one repo or the estate; cost to carry (*Four axes*) | directive-only | invisible. The status says the order is the guide's reading, not a ruling |
| MEC2 | If a machine can decide it and the cost of a miss is real, build a guard; if it is judgement, it is doctrine text, or a skill for a procedure worth a checklist (axis 1) | directive-only | diff, judgement: a judgement rule given a scanner, or a decidable one left as prose. This census is the instrument that lists the second kind (`PRO46`) |
| MEC3 | Check that the enforcement point can deliver the remedy, not only detect the fault: a `Stop` hook fires after the reply has streamed, so it can detect a bad reply and cannot retract it (axis 1) | directive-only | invisible: a design choice made before any guard exists |
| MEC4 | Pick the weakest trigger that still catches the failure (axis 2) | directive-only | diff, judgement: a hook where a command would catch it |
| MEC5 | A thing that helps the principal work with Claude has one home, atelier, and a skill or command one prefix, `/atelier:`: it is born in the plugin, never in `~/.claude/skills`, `~/.claude/commands` or a repo's `.claude/` (*Where it lives and what it is called*) | enforced, partial (warns, session open) | `tools/prefixhook.py` (`SessionStart`, wired in this machine's user-level settings, read at this census) names any entry in the user skills directory other than `atelier` and `synced`, any file in the user commands directory, and any entry in the repo's own `.claude/skills` or `.claude/commands`; `--check` gives the same list as an exit code. It warns and always exits 0 on the hook path, by design (axis 1). Unseen: a stray created after the session opened; a helper that is not a skill or command and lives in another repo; any clone without the user-level wiring |
| MEC6 | Private content does not move the home: a skill that needs an estate's values is general and lives here, the values sit in a private config it reads; a skill that cannot be split is a board finding, not a reason to ship it under another name (*Where it lives and what it is called*) | directive-only | diff, judgement. `leakscan` blocks estate-shaped data and listed terms in the public skill (`PRO10`, `PRO28`'s term-list question); an unlisted estate value written into a skill passes |
| MEC7 | Moving an existing tool into atelier from another repo is told to the principal first, item by item (*Where it lives and what it is called*) | directive-only | record: the paired commits in two repos, the tool added here and removed there, with no ask between them. Neither repo's diff shows the other |

## PRINCIPLES.md

| Id | Rule (section) | State | Guard, or where a breach shows |
| --- | --- | --- | --- |
| PRI1 | Keep the core job running when a part fails: reduced service instead of failing whole; the targets that can proceed do, the ones that cannot are skipped and reported loudly (§1 graceful degradation; the *whose failure* test's remote-peer half) | directive-only | diff, judgement: a batch verb that aborts the run on one failed target |
| PRI2 | Compartmentalise so a failure in one partition cannot cascade: per-unit error isolation, separate sessions, a bad input for one item never sinks the others (§1 bulkhead) | directive-only | diff, judgement |
| PRI3 | A failing or hanging dependency is skipped on a timeout and never waited on indefinitely; fail fast, return a fallback (§1 circuit breaker) | directive-only | diff: a network call with no timeout is readable in code. Measured: 58 of 65 `subprocess` calls in `tools/` carry no timeout, nearly all local `git`; the one `urlopen` has `timeout=10`. A guard would have to scope to calls that can leave the machine |
| PRI4 | The state a component lands in on failure is the safe one: wipe to known good, quarantine the unknown, default destructive actions to deny (§1 fail-safe) | directive-only | diff, judgement |
| PRI5 | Reject our own bad data at the edge, strict schema and canonicalising validators; degrade gracefully on a remote peer's failure; a unit whose own plan is partial is refused (§1 fail-fast; *whose failure is it*) | directive-only | diff, judgement |
| PRI6 | Design the unhappy path: every feature specifies what happens when the dependency is offline, the field missing, the write rejected, the secret will not decrypt (§1) | directive-only | invisible: an omission |
| PRI7 | An operation longer than a session, or touching data not recoverable from elsewhere, gets three answers in advance: does it survive the operator going away; can it resume without redoing work, and can an interruption leave something that looks finished but is not; how is completion proved, not assumed (§1) | directive-only | invisible: the plan not made before starting. Below the threshold it is not a checklist |
| PRI8 | Before adopting an external dependency, establish how you keep working without it (a fallback, an export path, a swappable seam, a degraded mode), and adopt only once that exit exists (§1) | directive-only | diff: a new dependency is visible (an import, a requirements file, a service); whether an exit was stated is judgement. Measured: every import in `tools/` and the Python instruments is standard library, so the zero-dependency limit case holds on the live tree with nothing guarding it |
| PRI9 | Prefer the simple design over the clever one; when two designs work, ship the smaller (§2 KISS) | directive-only | diff, judgement |
| PRI10 | Components talk through narrow, explicit contracts, not shared internals (§2) | directive-only | diff, judgement |
| PRI11 | Do one thing well: one job per verb, small sharp tools composed, structured output designed to feed the next program (§2 Unix philosophy) | directive-only | diff, judgement |
| PRI12 | A tool that prints for a human also offers the same result machine-readable (`--json` and honest exit codes); omitting it needs a stated reason; an interactive surface is out of scope (§2) | directive-only | diff: a tool added with no `--json` flag. Measured: 31 of 47 non-test `tools/*.py` name `--json`, and 18 of the 19 floor-registry scanners do (the exception is `board.py`); of the 16 without, several are hooks or libraries with nothing for a human to read, and the census did not sort the rest |
| PRI13 | Design a service API first: the contract is the single source of truth, the capabilities land behind it before any surface, and every surface rides it; a web front end holds presentation only. Binds producers, not consumers of a third party's system (§2) | directive-only | invisible to atelier: it has no service of its own to read. The doc says the first case is yet to come |
| PRI14 | One responsive web app, mobile-first; never fork the web surface into a separate mobile edition (a native client riding the API is a different thing) (§2) | directive-only | invisible to atelier: no web surface in the tree. The doc says no shipped worked case exists yet |
| PRI15 | A commodity sub-feature sits behind a swappable seam, as a default implementation of an interface; when nothing needs the default, adopt the mature product outright; a security-critical one is held to §5 (§2) | directive-only | diff, judgement |
| PRI16 | Prefer events and triggers to polling and timers; a timer needs a stated need and a stated staleness bound (§3; *timer vs event*) | directive-only | diff: a `schedule:` or `cron:` trigger, or a sleep loop, with no stated need. Measured: zero `schedule` or `cron` triggers in the 2 workflows and 3 templates |
| PRI17 | Stateless and asynchronous by default: derive desired truth from the source, treat the live system as actual truth, re-derive each run; persistent state only where the value is real and the staleness managed, since undated state is a future lie (§4; *state vs stateless*) | directive-only | diff, judgement |
| PRI18 | A verb is idempotent and convergent: running it twice is safe and the second run a no-op; one that is not re-run-safe says so loudly and is not automatable (§4) | directive-only | diff, judgement |
| PRI19 | Privacy, security and cost are design inputs from the first line; name what could attack a surface before building it, right-sized, not full STRIDE (§5) | directive-only | invisible: an omission. A review's security lens at design altitude (`REVIEW.md`) reads it when a review runs |
| PRI20 | Secure by default: a new surface (a config key, service, flag, port, permission, exposed path) opens closed or minimal, and opening it needs a stated reason (§5) | enforced, partial (CI test, blocks the run) | `tools/test_templates.py` asserts `contents: read` in the shipped child floor workflow (`ChildFloorWorkflowTest.test_least_privilege`) and in the reusable floor workflow (`ReusableFloorWorkflowTest`). That is one surface kind in two files; a new workflow's permissions, a new port, key or flag: unseen |
| PRI21 | Credentials are the smallest set the task needs, granted at the moment of use and expiring; a standing, broad, forever credential needs a stated reason and is tracked debt, not a resting state (§5; *standing or ephemeral*; `ACCESS.md` step 2's debt clause) | directive-only | record: the standing-credential debt list is the instance's, off-repo. A credential in the tree is `AUT10` |
| PRI22 | An external credential is regenerated by code kept behind a one-off human approval, never a hand-kept irreplaceable token; the secret store is itself reproducible, throw it away and regenerate (§5, §7) | directive-only | invisible: the store and the procedure are off-repo |
| PRI23 | A credential used rarely is deleted between uses and its rebuild made cheap, automated and tested (§5; the doc calls it a one-case claim) | directive-only | invisible |
| PRI24 | Zero Trust, right-sized: no asset trusted by default, verify explicitly, least privilege, assume breach, network location alone grants no trust; implement what is achievable and name the gap; a location control is defence in depth, never the trust decision; an unmet tenet is tracked debt (§5) | directive-only | invisible, judgement |
| PRI25 | Any hash or checksum we emit (a verification pass, a manifest, a cache key, a fingerprint) uses SHA-2 or stronger, never MD5 or SHA-1; what we verify against, git's object ids and a format that mandates its checksum are out of scope (§5) | directive-only | diff: `hashlib.md5(` or `.sha1(`, `createHash('sha1')`, `md5sum`, `sha1sum`, a bare `shasum` (SHA-1 by default). Not clean on the live tree: `instruments/ccfleet:review_log` builds a log-file suffix with `hashlib.sha1` (see the defects). The doc says a scanner would fire on every exemption; the exemptions are vendor values and quoted digests, not constructor calls |
| PRI26 | Where the principal holds a standing preference about a primitive (compression, encoding, key size, cipher suite, RNG source), do not pick one silently on adequacy grounds: take the stated one or ask (§5) | directive-only | invisible |
| PRI27 | The sweep for stale claims after a refined learning covers the whole repo: the doctrine surface, the plugin surfaces (`skills/`, `commands/`), the templates, and children's inlined floor blocks at each next pin bump; a surface not on the list is added to it, not swept by memory (§6) | directive-only | diff, judgement: a superseded statement left in `skills/`, `commands/` or a template after a doctrine change. `blockscan` reads the floor block's source co-change (warn-only, CI) and `stampscan` declared stamped copies; neither reads a skill's prose |
| PRI28 | No snowflakes: infrastructure is reproducible from code and secrets alone; a setting living only in a running system is a latent outage (§7) | directive-only | invisible to atelier: live systems are children's. The census of the child repos is the later one |
| PRI29 | The code is the source of truth and the live system is a cache: desired state in version control, the live system a convergence target, never the master (§7) | directive-only | invisible to atelier |
| PRI30 | Codify before you converge: a hand-action may precede its codification only as a logged, temporary bridge with a follow-up, or a documented permanent exception where codifying is unsafe (such as severing the agent's own access); never as steady state (§7; *codified or hand-done*) | directive-only | invisible: an unlogged hand-action leaves nothing in the tree; a logged one shows on the board |
| PRI31 | Design out the work: prefer the design that makes a future class of effort impossible over one that makes it manageable (§8) | directive-only | diff, judgement |
| PRI32 | Build the reliable tool once and reuse it when a task will recur; build it tested and honest; a task that truly happens once is done directly (§8; *one-off or recurring*) | directive-only | invisible, judgement: a recurring hand-task leaves no diff until someone writes it down |
| PRI33 | Solve a problem once and compose from the blocks already held, within a repo and across the fleet by the up, down and lateral flows (§8) | directive-only | diff, judgement: a second implementation of one capability. Across repos: record, not joined by any check |
| PRI34 | The payback comes from real, observed recurrence or a real avoided class of work; a predicted recurrence carries its test; no gold-plating (§8 *The discipline*) | directive-only | invisible, judgement |
| PRI35 | Data, whether application, system or user, carries the time dimension its domain implies, modelled as part of designing the data (§9) | directive-only | diff, judgement: a schema or data model with no time field. atelier holds records, not application data; the reach is the children's |
| PRI36 | Keep world time and record time apart; collapsing them into one column makes two question classes unanswerable; a dataset that needs only one says which and why (§9) | directive-only | diff, judgement |
| PRI37 | A stored conclusion (`verified`, `approved`, a price, a status) carries when it was established and by what method, and by whom where that matters (§9) | directive-only | diff, judgement: a boolean or status field with no sibling date or method |
| PRI38 | Work confidence out from the source, method and age when asked; never store a bare per-fact score; where a single method itself varies, a few named levels, never a number (§9) | directive-only | diff, judgement. The doc records this as an answer from options, not a ruling in the principal's words |
| PRI39 | Model an entity's lifecycle as dated transitions, not a boolean: ask whether the real question is "since when, and what before that?" (§9) | directive-only | diff, judgement |
| PRI40 | A hard delete destroys the dimension: prefer a dated end-state; where a delete is required (a privacy erasure) it is a deliberate, recorded act (§9) | directive-only | diff, judgement: a delete verb in a data-holding tool |
| PRI41 | "Unknown" is not "none": an open interval is legitimate, and a single null must not stand for both "no end yet" and "never established" (§9) | directive-only | diff, judgement |
| PRI42 | Carry the minimum dimension the later questions need (was it true then, what changed since, how stale, what did we believe at the time); less is the defect, more than the questions justify breaks KISS, and for personal data a retention limit can mean less (§9) | directive-only | diff, judgement |
| PRI43 | The time-dimension principle binds retrofits: add the dimension now so the clock starts now, record the unrecoverable stretch honestly, and leave the fix to the repo that owns the data (§9 *Scope*, ruled 2026-08-09) | directive-only | record: a child's board shows the retrofit item or its absence. atelier's part ends at the principle and the pointer |
| PRI44 | Engineer for the failure being cheap, not impossible: recoverability is what licenses action, so the work goes into the way back (§10; the guard requirement is folded at `GRD1`) | directive-only | invisible, judgement |
| PRI45 | A control that makes you reluctant to act is failing, even while nothing has gone wrong: the cost is paid in things not done (§10) | unenforceable, accepted | The doc states the ground itself: the cost "never appears in an incident record". The fact that would condemn the control is an act that did not happen, which sits in no diff, record or transcript a check can read (`GUARDS.md` evidence window). Accepted as of 2026-11-23 |
| PRI46 | Where a thing may leak, shape it so the leak carries no advantage: a token whose form reveals no structure, a store opaque to whoever holds the wrong half (§10) | directive-only | diff, judgement: an identifier or token format that encodes structure |
| PRI47 | Prove a recovery by exercising it: an unexercised restore is an assumption, since "we could restore" and "we have restored" read identically until exercised (§10) | directive-only | record: a dated exercise against a claim that one works. `DAT1`'s corroboration is the neighbour |
| PRI48 | Claim the freedom that the detection and the recovery you have actually exercised support, and no more; detection has no cheap proof and is the leg most likely assumed (§10, the precondition) | directive-only | invisible |
| PRI49 | Reason from first principles, not by analogy or convention: others went another way, the market never adopted it and it has always cost this much are evidence to weigh, never verdicts to inherit (§11) | unenforceable, accepted | A method of thought: the reasoning that preceded a conclusion is not in any commit. Its checkable trace is the graded rejection (`PRI51`), which is where the guard candidate sits. No recorded decision against building; the ground is the evidence window. Accepted as of 2026-11-23 |
| PRI50 | Ask of every base claim what kind of barrier it is (a law is a fundamental; a price, a market choice or a toolchain's limit is a state of the world); a claimed fundamental is a claim; first principles raises the bar for a rejection and does not lift the evidence duty (§11) | directive-only | diff, judgement: a rejection in a record that rests on cost or market non-adoption |
| PRI51 | Before an option is rejected, grade it by the kind of barrier (impossible, forbidden, improbable, not-yet-known-how, done-but-elsewhere) and write the grade down (§11) | directive-only | diff: a `## Rejected` entry with no grade. A presence check; `reviewscan` reads that a decision record has a review line, not its rejected options |
| PRI52 | Every grade carries its scope (the universe, this part, this toolchain, this market); a grade with no scope overclaims (§11) | directive-only | diff: a grade word with no scope beside it |
| PRI53 | Cost is a bar, not a verdict, and market non-adoption is weak evidence; the grade governs the record, not the spend, which stays with the always-confirm floor (§11) | directive-only | diff, judgement. The spend half is `AUT18` |
| PRI54 | A not-now grade (forbidden, improbable, not-yet-known-how) gets a row in one register naming the option, its grade and its reopening input, added in the same change that grades it (§11) | directive-only | diff: a grade added with no register row in the same commit. No register exists in this repo (the phrase "reopening input" appears only in `PRINCIPLES.md`), so the rule cannot be walked here yet |
| PRI55 | The decision template asks for the grade; a record's rejected options with no grade are an incomplete record (§11) | directive-only | diff: `docs/decisions/template.md` has a `## Rejected` section and no grade slot, as the doc says ("that is owed"); board item `160/150` records the debt |
| PRI56 | When principles collide and no precedent fits, decide and record the ruling in the code comment at the site, the roadmap item and, if it generalises, a new precedent line here; a stated deliberate exception is fine, a silent violation is the defect (*Trade-offs*; the opening) | directive-only | diff, judgement: a design choice that departs from a principle with no stated reason |
| PRI57 | When two principles want different designs, the higher overrules the lower: protect the system and its data; tell the truth; keep the core job running; hold the security posture; keep it simple and consistent; keep it cheap (*Precedence*) | directive-only | invisible, judgement. The apex sits above the ladder |
| PRI58 | Read-only and reversible work is permissive and ungated; destructive work is fail-safe, with gates, confirms and re-checks at execute and restore contracts (*Is the action reversible?*) | directive-only | diff, judgement: a destructive verb in tool code with no re-check at execute. The autonomy half is `AUT1` and `AUT12` |
| PRI59 | An action on uncertain data is refused; a claim on uncertain data is allowed with honest confidence and a discriminator that survives the alternatives; prefer the conservative miss to the false claim (*Claim or action?*) | directive-only | invisible, judgement |
| PRI60 | Match a control to its threat, not stricter: a guard that blocks legitimate routine work trains the operator to loosen it (*Gate sizing*) | directive-only | record: allow-marker and ignore-glob density against a guard over time. `GRD29` is the neighbour |
| PRI61 | When one field or path seems to want different semantics from its siblings, keep the mechanism uniform and make the special need loud; escalate to a true special case only when the threat model changes, and record the trigger (*Special case vs uniform mechanism*) | directive-only | diff, judgement |
| PRI62 | While a fix's own justification is unproven, hold the narrowest live-proven scope (*Mitigation under uncertainty*) | directive-only | diff, judgement |
| PRI63 | Roll a change out in rings, bench then one production node then fleet, observing between, and ask what the last ring showed; skipping a ring needs a stated reason (*Widen in rings*) | directive-only | record: a rollout's order across nodes or repos. `ACC7` is the same shape applied to access |

## Directive-only rules, grouped by where a breach shows

**Diff-visible (60).** ACC: none. CNV1, CNV2, CNV4 to CNV7, CNV9, CNV10;
DOC2, DOC3, DOC4, DOC6, DOC8, DOC9, DOC10, DOC12, DOC13; GLO1, GLO2, GLO4;
MEC2, MEC4, MEC6; PRI1 to PRI5, PRI8 to PRI12, PRI15 to PRI18, PRI25, PRI27,
PRI31, PRI33, PRI35 to PRI42, PRI46, PRI50 to PRI56, PRI58, PRI61, PRI62.
Only 17 name a shape a scanner could read from the added lines: CNV4, CNV6,
CNV7, CNV9, CNV10, DOC3, DOC9, DOC12, PRI3, PRI8, PRI12, PRI16, PRI25, PRI51,
PRI52, PRI54, PRI55. The other 43 are design or wording judgement and stay
review work, which is the shape of `PRINCIPLES.md`: it is a statement of
what good design is, and a diff shows the code, not whether the code is
simple, decoupled or honest about its unhappy path.

**Record-visible (9).** ACC6, ACC7; GLO3; MEC7; PRI21, PRI43, PRI47, PRI60,
PRI63. Four of these (ACC6, ACC7, PRI21, PRI43) rest on a record the doc
itself keeps off this repo: the instance's access map and debt list, or a
child's board. They are visible to a session that reads the instance, not to
a check in atelier.

**Invisible (30).** ACC1, ACC2, ACC4, ACC5, ACC8; CNV3; DOC1, DOC5, DOC7,
DOC11; MEC1, MEC3; PRI6, PRI7, PRI13, PRI14, PRI19, PRI22, PRI23, PRI24,
PRI26, PRI28 to PRI30, PRI32, PRI34, PRI44, PRI48, PRI57, PRI59. No rule here
is one a harness hook could decide outright from a command or a question
payload (ACC4's write verbs and PRI59's action on uncertain data are the
nearest, and neither is machine-decidable). The acts are on platforms and
live systems outside the repo (ACC), in a session's design thinking (PRI6,
PRI7, PRI59), or in children's tools (PRI13, PRI14, PRI28, PRI29).

## Counts

| Doc | Rules | enforced (of which partial) | blocks | warns | directive-only | diff | record | invisible | unenforceable, accepted |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ACCESS.md | 9 | 2 (2) | 2 | 0 | 7 | 0 | 2 | 5 | 0 |
| CONVENTIONS.md | 10 | 1 (1) | 1 | 0 | 9 | 8 | 0 | 1 | 0 |
| DOCUMENTATION.md | 13 | 0 (0) | 0 | 0 | 13 | 9 | 0 | 4 | 0 |
| GLOSSARY.md | 4 | 0 (0) | 0 | 0 | 4 | 3 | 1 | 0 | 0 |
| MECHANISMS.md | 7 | 1 (1) | 0 | 1 | 6 | 3 | 1 | 2 | 0 |
| PRINCIPLES.md | 63 | 1 (1) | 1 | 0 | 60 | 37 | 5 | 18 | 2 |
| Slice 4 | 106 | 5 (5) | 4 | 1 | 99 | 60 | 9 | 30 | 2 |
| Slice 3 | 94 | 9 (9) | 8 | 1 | 81 | 20 | 7 | 54 | 4 |
| Slice 2 | 129 | 27 (19) | 15 | 12 | 101 | 36 | 23 | 42 | 1 |
| Slice 1 | 158 | 19 (11) | 14 | 5 | 133 | 35 | 33 | 65 | 6 |
| Running total | 487 | 60 (44) | 41 | 19 | 414 | 151 | 72 | 191 | 13 |

As in slices 1 to 3: *diff*, *record* and *invisible* split the directive-only
count, each rule once, under the place a breach first shows. *blocks* includes
the CI test pin (PRI20), which fails the run after a push rather than
refusing the commit. `MEC5` is the one warn-only row: it warns at session
open and never blocks. The running total counts one rule twice, EVIDENCE §17
as `EVI24` and as `CON21` (slice 3's method step 4); nothing in this slice adds
a second such pair, so net of it the running total is 486 distinct rules.

Reading the table. Slice 4 is the least enforced yet: 5 of 106 rules (5%)
have any check, against 10% for slice 3, and all five cover only part of
their rule. Two of the six documents have no enforced rule and `PRINCIPLES.md`, with 63,
has one: `DOCUMENTATION.md` is a doctrine of how to write for a reader, `GLOSSARY.md`
is a file about its own upkeep, and `PRINCIPLES.md` governs design, where the
only check found is a pinned token permission on the shipped floor workflow.
`ACCESS.md` is the exception that proves the pattern: it is a runbook for
events on other people's platforms, and its two enforced rows are the
repo-side shadows (a credential value or an estate map must not reach git).
Two rules are accepted, both on the evidence-window ground: a cost paid in
things not done, and a method of thought. Across the four slices, 12% of the
487 rules counted have any mechanical check, and 44 of those 60 cover only
part of the rule. The census also measured the live tree against the
rules a guard would read, and found one standing breach of a rule's text
(`PRI25`, the SHA-1 suffix) and one unmet doctrine rule (`DOC3`, no version
field on any machine payload).

## Top five guard candidates

Directive-only, breach visible in the diff, and costly when it happens:

1. **PRI25, a weak hash constructor in code we write.** `hashlib.md5(` and
   `hashlib.sha1(`, `createHash('md5')` and `createHash('sha1')`, `md5sum`,
   `sha1sum`, and a bare `shasum` (which defaults to SHA-1), across `tools/`,
   `instruments/`, `skills/`, `commands/` and the templates. The first run
   would not be clean: `instruments/ccfleet:review_log` builds a log-file
   suffix with `hashlib.sha1`. That is the evidence the rule is breached with
   no one seeing it, and it needs an allow-marker with a reason for the
   exemptions the doc names (a vendor's published digest, a quoted
   historical one).
2. **CNV9, `Maori` with no macron.** The doctrine's own named example, and
   the principal's standing preference. `spellscan.py` leaves macrons out
   because it has no wordlist; a one-word denylist entry in its existing
   alternation family does not need one. Measured: no unquoted hit in 1751
   tracked text files, so it lands clean, and the quoted mentions already
   sit in code spans or quotation, which the scanner's exemptions read.
3. **PRI12, a floor-registry scanner with no `--json`.** A test that every
   `tools/floor.py` registry entry's tool accepts `--json`: 18 of 19 do
   today, the nineteenth (`board.py`) a generator. It turns the "twin or a
   stated reason" rule into a presence check with the stated reason as the
   exemption, in the registry's own declaration fields.
4. **PRI16, a timer with no stated need.** A `schedule:` or `cron:` trigger
   in any workflow or template without an adjacent need and staleness bound,
   in the allow-marker's reason shape. Today there is none, so the check is a
   tripwire, not a cleanup; a scheduled trigger on a public repo's CI is also
   spend (`AUT18`) and a new trust surface (`AUT16`).
5. **CNV7, a tracked text file that does not decode strictly.** The scanners
   read with replacement characters, so an undecodable file or a mangled
   `Māori` is reported clean. A strict decode of each tracked text file, with
   the result `unknown` (exit 2, `EVI19`'s contract) where it fails, closes
   the frame break the rule names. Measured: 1751 files, none fails; two test
   files carry U+FFFD on purpose and need the marker.

Next after these, each measured: a non-standard-library import or a
requirements file under `tools/` (PRI8, `PRINCIPLES.md` §8's zero-dependency
case; clean today by an AST pass over `tools/` and the Python instruments); a
`uses:` line not pinned to a full 40-hex SHA outside atelier's own reusable
floor workflow (the §8 supply-chain case; all 10 third-party `uses:` lines in
the workflows and templates are pinned, and nothing enforces it); a `--json`
payload with no version field (DOC3, 0 of 31 today, a conformance question
before it is a guard, see the defects); CNV4's bare `T` timestamp (6 files, but
the key-name exemption makes it noisy); a grade slot on the decision template
(PRI55, known and owed). The rule-wording rule (DOC8) has no guard worth
building and one missing home, below.

## Doctrine defects found, not fixed here

Each is owed its own board item (`PROPAGATION.md` § *Pointing up*) where it
has none; none is changed by this file.

- **`DOCUMENTATION.md` principle 6 binds new and changed rules "as a review
  question (could a reader find this from where they stand?)", and no review
  asks it.** The phrase appears in `DOCUMENTATION.md` only: not in
  `REVIEW.md`'s standing checklist (the seven checks every review runs
  unasked), not in the review-brief skill, not in the brief template. A rule
  that names review as its enforcement is a directive with no home for the
  question (`GUARDS.md` § *A rule with no home*'s class). The doc asks this
  census to say whether a scanner is worth building: it is not, and the
  question needs a home in `REVIEW.md`'s checklist.
- **`DOCUMENTATION.md`'s machine-contract rule has no counterpart in the
  tree it governs.** It says a machine contract is "versioned like an API" and
  that a schema change moves its version. 31 of atelier's 47 non-test tools
  emit `--json`, and none of their payloads (nor any instrument's) carries a
  version field. Either the rule's reach is a child's tools and says so, or
  atelier's own payloads owe a field; the doctrine does not say which.
- **`instruments/ccfleet` writes a SHA-1 suffix into a file name, against
  `PRINCIPLES.md` §5.** The rule lists "a cache key, a fingerprint" among
  what the estate emits, and says SHA-256 costs approximately nothing; the
  suffix in `review_log` is a short SHA-1 of the repo and item. A tree
  conformance gap, not a doctrine fault. Changing the hash renames the log a
  resumed reviewer looks for; the function already has a `legacy` name path
  for an earlier change, which is the shape the fix would follow.
- **`PRINCIPLES.md`'s opening and its trade-offs section still scope
  themselves to §1 to §9.** The precedence ladder and the situation tests
  "resolve collisions among the design principles §1–9", while §10 and §11
  exist and one situation test ("Prevention, or cheap failure?") already
  cites §10. A stale scope sentence by two sections.
- **`GLOSSARY.md` says *stated bridge* is "defined once, in `PRINCIPLES.md`
  §7"; §7 defines the hand-action bridge only.** The wider sense the entry
  gives (a gap, a hand-action or a standing exception, carried openly as
  tracked debt) is assembled from §5's credential and Zero Trust bullets and
  §7. The entry is wider than its stated one home.

Checked and found sound: `ACCESS.md`'s claim to invent no new rule, apart from
the step 5 tightening it names (`ACC5`); `MECHANISMS.md`'s one-example claim
for an in-estate MCP server (`instruments/browser-fetch/` exists);
`GLOSSARY.md`'s section pointers into `00-APEX.md` (every named heading
exists).

## Doubts and unverified points

- **`ECO4`'s one-source doubt (slice 3) is closed for this machine.** The
  wired `modelguard` is atelier's own file at the primary checkout (method
  note above). Slice 3's count is unchanged.
- **`MEC5` is enforced only where the user-level settings are.** The hook
  ships with no plugin `hooks.json`; the wiring is a person-local setting, so
  the state holds on this machine. A fresh clone or a second machine has
  nothing watching.
- **The footer of `DOCUMENTATION.md`** records a cold pass that ran
  2026-07-20 and a closed cycle. Principle 6 (2026-11-17) and the
  doctrine-tooling bullet (2026-11-16) landed after it and say they are
  agent-drafted; board item `160/1510` queues the pass for the first. The
  census did not read the review queue beyond finding that item.
- **`CNV8` and `CNV9` share one scanner, counted separately** because the
  doctrine line holds two invariants and `spellscan.py`'s own docstring says
  it checks one.
- **Two worked cases name a child's tool** in `PRINCIPLES.md` §2 and in
  `DOCUMENTATION.md`. `PRO28` bars naming a private child repo in a public
  doctrine file. Whether that child is private is the term list's call; the
  census did not judge it and counted no breach.
- **`GLO3` is counted a rule** because the banner tells a reader how to treat
  the entries. A stricter reading would call it status, not a rule, and the
  glossary would have three.
- **`PRI45` and `PRI49` counted accepted** on the evidence-window ground, not
  on a recorded decision not to build. A stricter reading would leave `PRI49`
  directive-only, invisible.
- **Rule boundaries are a judgement**, as in slices 1 to 3; the folds are
  named in the method.
- **Unverified**: whether `modelguard`'s and `prefixhook`'s wiring survives a
  second user-level settings file on another machine; whether any instrument
  outside the floor registry emits `--json` for what it prints for a person
  (PRI12 was measured on `tools/` only).
- **Self-run instruments** were counted directive-only, as before.

## Remaining docs for later slices

`docs/method/`: `REACH.md`, `SECRETS.md`, `SIGNING.md`, `STORAGE.md`,
`TOOLBOX.md`, and `docs/method/session-open/`. `SECRETS.md` will fold into
`ACC2`, `ACC3` and `ACC8` where it restates them (method 3). Then, on
`REVIEW.md` rule 3's definition, the doctrine outside `docs/method/`:
`docs/build/`, the ADRs, the skills and commands, the templates and the
validators' own stated rules.
