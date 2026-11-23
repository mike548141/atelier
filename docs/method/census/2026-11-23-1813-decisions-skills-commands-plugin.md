# Enforcement census — decisions, skills, commands, plugin manifests

Board item `020/220`, slice 7 of the census. Run 2026-11-23 (UTC) by a worker
of queue run 608d. This is a measurement record, not doctrine: it changes no
rule, and it builds no guard. It uses slice 1's method, states and row format
(`docs/method/census/2026-11-16-1142-record-review-concurrency.md`) and the
fold conventions of slices 2 to 6, so the seven slices add up. Slice 6
(`docs/method/census/2026-11-23-1730-build-boundary-standard-templates-root-files.md`)
is the one this continues.

## What this asks

For each rule in the files below: if it is broken, what sees it? Each rule gets
one state, defined as in slice 1.

- **enforced**: a mechanical check reads the breach. The row names the check,
  the plane it runs on (the pre-commit hook, the commit-message hook, CI, a
  harness hook, a session-open hook, a tool's own guard at the call, or the
  host's own refusal) and whether it **blocks** or **warns**. *partial* means
  the check covers some of the rule and the rest is unguarded.
- **directive-only**: nothing mechanical sees a breach. Where a self-run
  instrument would report it if a session chose to run it, the row says
  *instrument* and the state stays directive-only.
- **unenforceable, accepted**: the fact that would license or condemn the act
  is outside any check's evidence window (`GUARDS.md` § *Before building a
  check: the evidence window*), or the house has recorded a decision not to
  build the check. None of the 116 rules here is accepted (see *Doubts*).

A directive-only rule also gets the place its breach could be seen, as in
slices 1 to 6: **diff** (the committed change itself), **record** (only by
joining records outside one diff) or **invisible** (nothing in the tree or the
repo's records).

## Method, and what it did not do

1. Read in full, at commit `61415154` (the commit the worktree was cut from):
   `docs/decisions/README.md`, `template.md`, the eight numbered records
   (`0001` to `0008`) and the twelve dated records; the six skills under
   `skills/` with every bundled file (`create-repo`: `SKILL.md` and
   `instance.yaml.example`; `fleet-sweep`: `SKILL.md` and four prompts;
   `queue-run`; `review-brief`; `review-drain`: `SKILL.md` and three prompts;
   `session-onramp`); the four commands in `commands/`; both manifests in
   `.claude-plugin/`; and `instruments/atelier-menu/SKILL.md`, which is the
   bare `/atelier` skill the plugin cannot carry.
2. A rule is a sentence that tells a future agent to do or not do something.
   **A decision record counts the rules it states as standing, not its
   history**: the context, the options weighed and the evidence it gathered are
   not counted. A record whose status binds nothing (`draft`, `proposed`) is
   not a rule source; the three open ones are listed below and counted at zero.
   **A skill counts its constraints, gates and standards, not each step of its
   procedure**: "run `ccfleet drain --max N` in the background" is a step;
   "one driver per `kit_dir`" is a constraint. Not counted: the skills' and
   commands' front matter; grounding stories; lists of what a prompt's
   variables are; the output shapes' field names beyond what a reader checks;
   and the verbatim Apache text and placeholder lines in the manifests.
3. **Cross-slice folds.** A rule these files restate from a censused document
   is not counted again. Folded here:
   - `docs/decisions/README.md` and `template.md`: when to write a record into
     `REC17`; the file name `<date>-<HHMM>-<slug>`, retired names kept, into
     `CON23`, `REC7` and `CNV6`; the section set and the Review line into
     `TPL9` and `REV41`; "draft binds nothing", acceptance by the principal,
     append-only after acceptance, and the revoked and superseded forms into
     `REC18`, `REC19` and `REC20`.
   - `0001`: children point up, the parent is canonical and a child is wrong
     until the conflict is resolved upward, into `PRO2`, `PRO12`, `PRO13` and
     `PRO15`. `0002`: the pin is a SHA, the drift check and the `origin/main`
     addendum, into `PRO4`, `PRO5` and `RST8`. `0003` is superseded and states
     nothing. `0004`: one permissive licence, Apache-2.0, into `RST9`.
     `0005`: the leak boundary on every commit, the floor spent and the next
     widening the principal's, into `AUT2`, `AUT3`, `AUT10`, `RST21` to
     `RST25` and `RCL2`; the adopter's half of the voice into `RDM1`; naming
     private repos as provenance into `PRO28`.
   - `0007`: a dedicated signing key, the machine-level setup, the `create-repo`
     bake, one tracked `allowed_signers` kept append-only, the adoption
     boundary, no history rewrite, and artefact signing deferred, into `SGN2`,
     `SGN3`, `SGN4`, `SGN5`, `SGN9`, `SGN12`, `SGN13` and `SGN16`; the
     activation gated on the principal registering a key into `AUT16`.
   - `0008`: decisions 1 and 2 (call, never copy; declare non-enforcement) into
     `PRO41`, `GRD20` and `GRD22`; decision 3 (conformance enumerated) into
     `PRO44`; decision 4 (the tracked hook) into `TPL3` and `TPL5`; decision 5
     (the parent runs the floor it ships) into `PRO42` and `PRO43`; decision 6
     (a repo may add, never soften) into `RST15`, `RST17` and `GRD22`; the
     "adopting repos go red first" consequence into `GRD20`.
   - The dated records: `2026-07-13` into `CON23`; `2026-07-15` into `CNV3`,
     `CNV4`, `CNV6`, `REC28` and `REC29`; `2026-07-18` and `2026-07-19` into
     `REV39`, `REV41`, `REV42`, `PRO45`, `PRO49` and `PRO50`; `2026-07-21-0744`
     into `REV41`; `2026-07-21-0748` into the `create-repo` rows below, `SGN4`
     and `PRO9`; `2026-07-23` into `ECO1`, `ECO2`, `ECO7` to `ECO9`, `ECO19`,
     `ECO21` and `ECO32`; `2026-08-05` into `REC31` and `REC32`; `2026-08-15`
     into `REC22`, `REC23` and `CON28` to `CON31` (its one new rule is `DEC20`).
   - The six skills restate method rules and nothing else; the folds are named
     where a skill's rows are. The stamped-copy skills (`review-brief`,
     `queue-run`) are `PRO49` and `PRO50`'s subject; `REV22` and `CON78`
     already count their two pins, and `SOP1` to `SOP3` count the queue-run
     delivery rules, so `queue-run` adds one row only.
   - The commands: `/atelier:install-hook`'s "re-run after a plugin update"
     into `RDM2`; `/atelier:fleet-pins`' failed fetch is no result, and a pin
     bumped only after reading the commits, into `PRO4` and `PRO5`;
     `/atelier:worktree`'s base outside a synced folder into `CON2` and its
     "say why" into `CON4`; the hatches `/atelier:scan` names into `GRD8` and
     `GRD15`.
   - The prompts under `fleet-sweep` and `review-drain` carry a repeated block
     of ground rules. Each of these is a restatement and is folded, not counted
     per prompt: follow the repo's own `CLAUDE.md` where stricter, run `cclive`
     then `git status`, and leave another session's dirty work (`CON4`, `CON6`,
     `CON14`, `CON18`); explicit paths, the whole staged diff, a model-naming
     trailer, never `--no-verify` (`CON7`, `TPL12`, `GRD27`); work only in the
     given worktree (`CON1`); a pick is an answer and never a ruling (`COM19`,
     `COM20`); a public repo's records name no private repo (`REC32`, `PRO28`);
     niced single-process test runs (`CON77`); the workhorse seat, no
     subagents unless a read would flood context (`ECO2`, `ECO5`, `ECO6`);
     CI at the pushed head is evidence and a worker's green is not (`REC13`,
     `CON46`); an off-tier orchestrator forms no finding (`REV18`); the
     partition of the held-back sibling (`REV5`, `CON63`); a degraded pass is
     topped up (`REV38`); and "report what broke first" (`APX1`).
4. Listed every check that could see a breach: the floor registry (21 entries
   by `tools/floor.py`), both atelier workflows, the tests that pin skills
   (`tools/test_templates.py`, `tools/test_queue_run_single_source.py`), the
   tests of every instrument a skill drives (`instruments/test_ccfleet.py`,
   `ccmail.test.js`, `ccarchive.test.js`, `test_ccapple.py`,
   `test_atelier_menu.py`), the tests of the tools a command drives
   (`tools/test_pins.py`, `test_worktree.py`, `test_precommit.py`) and the
   instruments' `man` lint.
5. Before writing *enforced* against a rule, I read the code and cited the test
   or the function; before writing *directive-only*, looked for the check by
   name and by the phrase the rule uses in `tools/`, `instruments/`, `.github/`,
   `skills/`, `commands/` and `docs/build/templates/`. **Suites run at this
   commit, all passing:** see *Doubts* for the list and counts.
6. **What the floor reads of `skills/` and `commands/`.** The registry runs the
   whole-tree checks over these directories (`secretscan`, `leakscan`,
   `conflictscan`, `linkscan`, `publishscan`, `pdlistscan`, `licenscan`), and
   not the doc-prose checks: `datescan`, `wrapscan`, `spellscan`, `pathscan`,
   `pointerscan` and `attribscan` default to the `docs` root, and
   `.atelier-floor.json` narrows `wrapscan`, `spellscan` and `pathscan` to
   `docs/method`, `docs/build` and `docs/decisions` (and `pathscan` to the root
   files). So the skills, the commands and the manifests, which are doctrine by
   the function test, sit outside every prose scanner. Run by hand over them for
   this census: `spellscan` 0 findings, `datescan` 0, `attribscan` 2 (advisory;
   `create-repo` line 120 and `review-brief` line 142), `pathscan` 16 (all
   shapes of a path the scanner cannot resolve: an `$SRC/`-prefixed path, a
   child-relative template path, and the retired file names a skill names in
   order to retire them), `wrapscan` 109 (a mix of front matter, which must be
   one line, and real prose).
7. Measured, where a measurement says whether a candidate guard would fire on
   the live tree. Counts are from this worktree's tracked files by grep, `ast`
   and small scripts, not by a scanner, except where a scanner is named. Two
   GitHub settings were read with `gh api` (GET only).
8. Did not read `docs/SESSIONS.md` or the contents of `docs/sessions/`.

## The decision records that bind nothing

Counted at zero, because the README says a draft or proposed record "binds on
nothing" and these three are open:

| Record | Status | What it would add if accepted |
| --- | --- | --- |
| `2026-10-03-0641-the-exception-register` | draft, reworked 2026-11-09 | one central exception file per repo, each entry narrowed to a string; supersedes `GUARDS.md`'s "git supplies who and when". Owes a re-review (Fable) and the principal's acceptance |
| `2026-11-09-1334-check-declaration-standard` | proposed, design only | a `Declares` entry on every registry check, reported as warnings, with a census of 16 checks; review owed |
| `2026-11-09-board-states-design` | proposed | two state tiers (`[-]`, `[/]`), a required word on closed-not-delivered items, a counted roll-up; review and ruling owed |

Four more records carry `draft` and state decisions already in force through
doctrine slices 1 to 6 counted (`2026-07-18`, `2026-07-19`, `2026-07-21-0744`,
`2026-07-23`). They are counted through their doctrine (folds above), and the
status mismatch is a defect below.

## docs/decisions/ (README, 0001 to 0008, the dated records)

New rules only; every other rule these twenty records state is folded (method
3). `DEC1` to `DEC3` come from the README; `DEC4` and `DEC5` from `0002` and
`0008`; `DEC6` from `0005`; `DEC7` to `DEC18` from `0006` and its
addenda; `DEC19` from `0008`; `DEC20` from the board-store record; `DEC21` from
`0006`.

| Id | Rule (section) | State | Guard, or where a breach shows |
| --- | --- | --- | --- |
| DEC1 | An addendum that states a live state of the world dates it "as of <date>", never "at HEAD", and carries the read beside the claim (README, AR1 and AR5) | directive-only | diff: the phrase `at HEAD` in a record. Measured: 1 hit in 22 files (`0008`'s 2026-08-23 amendment, which predates the rule and is frozen), 0 since. A tripwire for the stale-claim shape; "the read beside the claim" is judgement |
| DEC2 | The README's index names every record in the directory (README, *Index*; the declaration is `indexscan:maps dir=. match=*.md exclude=template.md`) | enforced, partial (warns, hook + CI) | `tools/indexscan.py`, warn-only in the registry (`--warn`). Run over `docs/decisions`: clean, 20 entries mapped, 12 dated lines compared. Partial: presence and date order only; whether an index line is true is unread (the line for `0006` still says "(ccrepo, cctranscript)" while the record admits eleven more tools) |
| DEC3 | A record's Status is `draft`, `accepted`, `revoked <date>` or `superseded by <file>`, and draft is the only mutable state (README; `template.md` offers `draft \| accepted`) | directive-only | diff: the `Status:` line. Measured over the 20 records: 12 `accepted`, 1 `superseded`, 5 `draft`, 2 `proposed`. `proposed` is in no spec; `0007` and the register record add free text to the word. A vocabulary check fires twice on the first run |
| DEC4 | atelier's `main` is append-only: never force-pushed, deleted or rewritten, because every child's pin is a SHA on it (`0002`, *Consequences*; `SGN12` folds the signing instance) | enforced, partial (blocks, host ruleset) | The ruleset on `main` refuses the push at the host. Read 2026-11-23: `gh api repos/<owner>/atelier/rules/branches/main` lists `deletion`, `non_fast_forward` and `required_signatures`, and `bypass_actors` is empty. `tools/floorfleet.py` reds the parent row when `deletion` or `non_fast_forward` is missing (`BoundaryTest`), but `floorfleet` is self-run and no CI step runs it. A ruleset is a GitHub setting, so editing it leaves no diff; the owner account can still do so (`0008`'s "what this does not close") |
| DEC5 | The control that makes the floating `@main` call safe is `main`'s own protection, in three legs at three strengths: branch protection and signed commits in force for every account, review on the registry post-hoc (`0008`, the 2026-10-16 amendment, which supersedes the 2026-08-23 one) | enforced, partial (blocks, host ruleset; reds, `floorfleet`) | Legs 1 and 2 as `DEC4` (`required_signatures` active, no bypass actor at the read). Leg 3 is post-hoc by design (`REV35`'s queued pass, directive). `floorfleet` shows `required_signatures` as informational and does not read the bypass list (the record's AR2, open) |
| DEC6 | The doctrine stays addressed to its worked-example principal by name and is not genericised; a README framing note tells an adopter they are the principal (`0005`, *Decision* 1; the adopter's half folds at `RDM1`) | directive-only | diff, judgement: a commit that rewrites the voice. Nothing reads voice; the record rejects genericising knowingly, on the grounds that the name is attribution and not sensitive data |
| DEC7 | An instrument belongs in `instruments/` only if its value is the Claude teammateship (observing, extending or preserving it); the test is purpose, not runtime, and general machine or estate utilities stay with the estate they serve (`0006`, *Decision* and the 2026-07-12 and 2026-07-17 addenda) | directive-only | diff, judgement: a new entry in `instruments/`. `indexscan` (warn-only) makes the README name each entry, so a new tool cannot arrive unlisted; it does not ask whether it belongs. Measured: 13 entries in the README table |
| DEC8 | `tools/` holds the enforcing checks, Python and zero-dependency; the zero-dep ethos holds where it can and flexes only for a capability instrument whose value needs dependencies (`0006`, *Decision* and the 2026-07-12 addendum) | directive-only | diff: an import outside the standard library in `tools/` or in a Python instrument other than `browser-fetch`. Measured by an `ast` read of 113 Python files against `sys.stdlib_module_names`: 0 non-stdlib imports. A tripwire that lands clean. `SECURITY.md`'s wider claim ("the repo takes none") is the defect slice 6 named |
| DEC9 | A capability instrument that needs dependencies pins them (`requirements.txt`), constrains them (`constraints.txt`) and keeps its runtime a regenerable venv outside the repo (`0006`, 2026-07-12 addendum) | directive-only | diff: `instruments/browser-fetch/` carries both files (`mcp==1.28.1`, `playwright==1.61.0`); where the venv lives is `setup`'s code, which nothing checks. A manifest anywhere else would be what slice 6's manifest-location candidate sees |
| DEC10 | Instruments install by a per-tool symlink into `~/.local/bin` through one idempotent `instruments/install`, never by putting the folder on `PATH`; the installer touches only symlinks it owns and never clobbers a real file (`0006`, *Decision*) | enforced, partial (tool's own guard, blocks at the call) | `instruments/install` skips a name whose target is a real file and only re-points links that point back into the directory. No `test_install` pins it. "Not the folder on `PATH`" is invisible: a shell profile is outside every tree |
| DEC11 | An instrument that writes keeps its target in a personal store outside any repo and refuses a destination inside a git work tree; the schedule is machine-local (`0006`, the 2026-07-17 and 2026-09-09 addenda: `ccarchive`, `ccmail`) | enforced, partial (blocks, CI test) | `ccmail.test.js` ("insideGitWorkTree finds the enclosing repo", "resolves symlinks, so a --dest reached through one is caught", "the sweep refuses the home directory and a git work tree as a cache root") and `ccarchive.test.js` ("insideGitWorkTree detects a .git ancestor at any depth", the symlinked-destination case); `node --test` runs in CI. Partial: a later writing instrument that omits the guard is unseen, and "no personal data in the code" is `leakscan`'s shape reach only |
| DEC12 | An instrument that holds a credential to a third-party account carries four controls: one read-only scope on the operator's own account; the secret never in a repo (Keychain, no plaintext fallback, and off macOS it refuses to store); the fetched data never in a repo; nothing personal in the shipped code (`0006`, 2026-09-09 addendum and its amendment) | enforced, partial (blocks, CI test + hook) | The scope is pinned (`ccmail.test.js`, "the consent URL carries state and an S256 PKCE challenge" asserts `gmail.readonly`); the data guard is `DEC11`; the keychain's absent and failed states are tested ("a Keychain read that fails is an error", "unavailable off macOS"). `secretscan` reads a committed secret; `leakscan` reads personal shapes. The refusal to store off macOS is in code (`ccmail` lines 42 and 163 to 178) with no test naming it |
| DEC13 | A credential-holding instrument's ADR entry states what a compromised session on this machine can read with it, per route (`0006`, 2026-11-09 addendum: "required of every future credential-holding instrument") | directive-only | record: `ccmail` carries the table and is the one instrument holding a credential today. Nothing lists which instruments hold one, so a second holder without an entry would be found only by reading `instruments/` against the record |
| DEC14 | An instrument that holds a credential or opens attacker-supplied bytes lists its threats and where each is answered; an absent list is itself a finding (review CC3, in the 2026-11-09 addendum) | directive-only | record: the table in `0006` covers `ccmail` and `ccpdf`. `ccapple` reads other people's private content; the 2026-11-01 addendum names its controls, not a threat table. A scanner cannot read "opens attacker-supplied bytes" |
| DEC15 | `ccpdf`'s setup refuses to shadow a real poppler and prints its own uninstall line, and its renderer refuses a page over a pixel budget (64 million by default, `CCPDF_MAX_PIXELS`) before allocating (`0006`, the third 2026-09-09 addendum and the 2026-11-09 threat table) | enforced, partial (tool's own guards, block at the call) | `ccpdf/setup` lines 28 to 35 refuse and exit; `pdfrender.swift` lines 98 to 108 hold the budget. No CI test: `ccpdf` is Swift and macOS-only and `ci.yml` does not run it. `ccpdf/selftest`, which `setup` runs before the binary goes on `PATH`, proves rendering and the output file name only |
| DEC16 | An instrument that reads another app's private store opens every store read-only through one function, requires a filter and a cap on every search, never reads or decrypts a locked note, never selects a credential-shaped column and has no write path (`0006`, 2026-11-01 addendum: `ccapple`) | enforced (blocks, CI test) | `instruments/test_ccapple.py`: `OpenReadOnly.test_write_is_refused_and_file_unchanged` and `test_uri_asks_for_ro_and_immutable`, the per-store `test_requires_a_filter`, `test_locked_note_listed_flagged_never_read`, `test_credential_shaped_columns_never_reach_any_output` (plants sentinel values), `test_no_query_selects_a_wildcard_or_a_credential_column` (reads the source) and `test_read_only_the_store_is_unchanged`. Runs in CI. It binds `ccapple` alone; a later instrument "inherits it as precedent" (the record's words) with no mechanism to say so |
| DEC17 | `ccmail`'s attachment cache is private (directories 0700, files 0600, tightened on every run) and its message folders expire after 30 days; the sweep touches only message-id folders, never follows a symlink, and refuses a root that is a symlink, the home directory or a git work tree (`0006`, 2026-11-09 addendum) | enforced (blocks, CI test) | `ccmail.test.js`: "cacheHygiene makes a world-readable cache private", "deletes message folders older than 30 days", "the sweep never follows a symlink entry out of the cache", "only touches message-id folders", "refuses a cache root that is a symlink", "the cache retention is 30 days", "new attachment files are 0600 and new directories 0700, whatever the umask" |
| DEC18 | A message id is refused unless lowercase hex before any network call or path join, and a sender's filename is sanitised (separators, controls, bidirectional overrides, length) with collisions suffixed and never overwritten (`0006`, 2026-11-09 threat table, first rows) | enforced (blocks, CI test) | `ccmail.test.js`: "a message id that is not hex is refused before any network call or path join", "safeName strips path separators", "safeName removes bidirectional overrides and control characters", "a symlink planted at the destination name is not written through", "two attachments with one name become two files, not one overwritten" |
| DEC19 | The floor registry carries its own contract tests, because a bad change to it reaches every wired repo on its next push (`0008`, *Consequences*) | enforced, partial (blocks, CI test) | `tools/test_floor.py` (for example `test_declared_but_missing_script_blocks`) and `floor.py --selftest`, run by `unittest discover -s tools`. Partial: nothing requires a new registry entry to arrive with a test of its own (`GRD10`, directive-only) |
| DEC20 | A board item file opens with its checkbox line and carries no front matter: state lives in the first line and nowhere else, since a second vocabulary would be one fact in two homes (`2026-08-15`, *Decision*) | enforced, partial (blocks, hook + CI) | `tools/board.py` reports a file with no state line ("no state line — an item file opens with its checkbox line", near line 918) and the `board` registry check fails on it. A file opening with `---` has no state line, so front matter is caught as a side effect; I found no test that names the case |
| DEC21 | Before offering the principal a build option, read what the estate already holds (its registry and tools); a brief wrong on a fact is re-briefed (`0006`, 2026-09-09 amendment: "check what already exists before offering to build"; the re-brief half folds at `APX9`) | directive-only | invisible: the option sits in a conversation |

## skills/session-onramp

Folded: the apex restated in § 1 (honesty, "if something broke say so first",
"done is exercised and observed", a caveat that makes a result look worse is
mandatory, adaptation continuous, capability scopes authority) into `APX1` to
`APX4`, `APX13` and `APX18`; `cclive` at open into `CON14`; "you become the
principal" into `RDM1`.

| Id | Rule (section) | State | Guard, or where a breach shows |
| --- | --- | --- | --- |
| SCO1 | Read the doctrine on demand and never wholesale: the apex and the always-confirm floor bind from the start; the rest is opened when a change touches it (§ 3; the root `CLAUDE.md` line folds at `RCL1`) | directive-only | invisible: which files a session opened is in its transcript only |
| SCO2 | Before acting, read `AUTONOMY.md` § *Always confirm* itself: it is the one list of what you stop and confirm, and the skill does not restate it (§ 2) | directive-only | invisible: a read. `AUT` rows count the list's items |

## skills/queue-run

The skill adds only delivery (`SOP2`, `SOP3`: counted as enforced, partial in
slice 5; `CON78`, `CON58`, `REV13`, `CON70`: its pinned phrases). One row has
no earlier home.

| Id | Rule (section) | State | Guard, or where a breach shows |
| --- | --- | --- | --- |
| QRN1 | The skill and the prompt never say a run "loses nothing": the honest form is "at most the item in flight" (QR7) | enforced (blocks, CI test) | `tools/test_templates.py`, `QueueRunSkillTest.test_loses_nothing_overclaim_evicted` asserts the phrase absent from the skill plus the prompt text. The text set does not include `CONCURRENCY.md`'s section, so the doctrine's own wording is unpinned |

## skills/review-brief

A stamped copy of `REVIEW.md` (`PRO49`, `PRO50`). Folded: the commitment
trigger (`REV39`), independence and the cold run (`REV1`), the brief's parts
and the four lenses (`REV21`, `REV23`, `REV22`), the body-free commit read with
`--also-exclude` and the `merge-base --is-ancestor` check (`REV10`), the
session-log skip (`REV11`), the security lens and `/security-review` (`REV24`),
re-running every live-proven claim (`REV26`), the two header lines (`REV33`),
the standing checks V1 to V7 (`REV27`), the method record (`REV34`), who
applies a finding (`REV12`), the verdict appended below a divider (`REV30`),
the deferred sibling and its fold (`REV3`, `REV5`, `REV6`), and "budget decides
how many reviews run, never how" (`REV40`). The lens roster, the commitment
trigger and the stamped-copy marker are pinned by `ReviewBriefSkillTest` and
`LensRosterParityTest` (`REV22`).

| Id | Rule (section) | State | Guard, or where a breach shows |
| --- | --- | --- | --- |
| RBF1 | A re-run line for this repo's Python tests is `cd tools && python3 -m unittest test_<name>` (or `discover -s tools -p 'test_<name>.py'`), never the dotted `tools.test_<name>`; every environment fact and file name a brief states is read off the machine before it is written (item 5, AR7) | directive-only | diff: a brief naming `unittest tools.test_`. Measured: 40 of 264 files in `docs/reviews/` contain the dotted form and 38 contain the right one. The dotted hits mix real re-run lines with prose describing the failure (the first one read is the latter), so a grep is not rankable as it stands |
| RBF2 | Reproduce the floor (build, tests, selftests) before working the lenses (*Running it*) | directive-only | invisible: a review log may record it (`REV34`'s method record); nothing reads whether it was done first |

## skills/create-repo

`create-repo` is the delivery vehicle for `REPO-STANDARD.md`, and most of its
steps restate that standard's rules. Folded: the standard is atelier's and is
read first, not re-derived (`PRO15`, `RST4`); boundary check first (`BND1`, the
first rule of `REPO-BOUNDARY.md`); size to the type (`RST2`); fill placeholders
with grounded content or a visible stub, LICENSE verbatim, the NOTICE
copyright line, locale spelling (`RST4`, `RST9`, `RST10`, `TPL11`); the board
as a store, the index generated and never hand-edited, no `ROADMAP-DONE.md`
seeded (`REC22`, `RST19`); the doctrine block stamped, bundled mode verbatim
(`PRO2`, `PRO9`, `TPL1`); the stamp tokens pinned by `TemplateSetPlaceholderInventoryTest`
(`TPL1`); neither `.claude/` settings file committed (`TLB9`); the signing bake
from the profile (`SGN4`); an advisory or scoped check declared in
`.atelier-floor.json` and never by dropping a scanner (`PRO41`, `GRD20`); the
first session file (`REC7`); a new remote authorised by the ask, publishing a
floor action (`RST29`, `AUT2`); delete-branch-on-merge (`CON53`); standardise
an existing repo, `git rm --cached` of a tracked settings file (`RST37`,
`TLB9`); never touch another owner's repo (`RST30`).

| Id | Rule (section) | State | Guard, or where a breach shows |
| --- | --- | --- | --- |
| CRP1 | The skill carries no identity of its own: the eight facts (git identity, remote account, workspace path, copyright holder, locale, exemplars, signing posture, doctrine source) come from the instance profile, referred to by key name and never hard-coded (intro, Step 1; `2026-07-21-0748`) | enforced, partial (blocks, hook + CI) | `leakscan` reads personal-data shapes over `skills/` (the example's email line carries `leakscan:allow: RFC 2606`, which shows the scan reaches it) and `pdlistscan` reads the closed list over the whole repo. A name, an account or a path is not a shape, so a hard-coded handle passes |
| CRP2 | The profile is `~/.atelier/instance.yaml`, in the adopter's home, never in a repo and never committed (Step 1; `2026-07-21-0748`) | directive-only | diff: a tracked `instance.yaml`. Measured: `git ls-files` shows only `skills/create-repo/instance.yaml.example`. `publishscan`'s names do not include the profile's name; `leakscan` would catch its email shape, not its other keys |
| CRP3 | Resolve the doctrine source in two modes (live: `atelier_path` or a sibling `../atelier`; bundled: the plugin's install directory), set `$SRC`, and confirm the eight load-bearing templates are readable; on any `MISSING`, stop and say so, and never scaffold from memory (Step 0) | directive-only | invisible: a run's outcome. The eight names the skill's loop lists all exist under `docs/build/templates/` today (checked); the list is hand-copied, so a template rename would make the loop say `MISSING` at run time, not at commit |
| CRP4 | Say back why the standard exists (reasoning recorded, independent peer review, behaviour tested for real) before scaffolding (Step 0, *Why this exists*) | directive-only | invisible: a sentence in a session |
| CRP5 | With no profile, fill it interactively: ask the principal for each key of `instance.yaml.example`, offer its defaults, write the file, and invent no value; `exemplars` and `atelier_path` are optional (Step 1) | directive-only | invisible: an off-repo file and a conversation |
| CRP6 | Copy with the stated renames (`gitignore` to `.gitignore`, `claude/` to `.claude/`, `workflows/ci-<type>.yml` to `.github/workflows/ci.yml`, `workflows/floor.yml` to `.github/workflows/floor.yml`) and put the product in its subfolder (Step 3) | directive-only | diff, judgement: a scaffold commit's tree. The rename map has no test, and `ci-<type>` has two templates (`ci-python`, `ci-static`) for the four types the standard sizes, so the map for `infra` and `docs` is unstated |
| CRP7 | Stamp `<atelier-path>` sibling-relative and never absolute, and fill it in every stamped file that carries it, found by grep and not by the skill's list (Step 5) | directive-only | diff, in a child's `CLAUDE.md`, `CONTRIBUTING.md` and reviews README: an absolute path where `../atelier` belongs. Not readable from atelier, which holds no child; `stampscan` reads only the floor region. The inventory test (`TPL1`) keeps the grep list from going stale unseen |
| CRP8 | Prove the stamp mechanically over the whole tree: delete the templates' guidance comments first, then grep the six tokens for no hit anywhere, then run the block's own drift check verbatim, and in bundled mode expect the stamped `<VERSION>` from `grep '"version"'` of the plugin manifest (Step 5) | directive-only | record: a self-run proof. The bundled-mode half cannot pass as written: `.claude-plugin/plugin.json` has no `version` key (removed 2026-10-18, commit `140a1902`), so there is nothing to print and nothing to fill `<VERSION>` from. See *Doctrine defects* |
| CRP9 | Wire the hook in a tracked directory, not `.git/hooks`: copy `pre-commit`, `pre-merge-commit` and `commit-msg` into `.githooks/`, `chmod +x`, `git config core.hooksPath .githooks`; add no scanner line to the hook and copy no scanner into the child (Step 6; `0008` decision 4) | enforced, partial (blocks, CI test) | `tools/test_precommit.py` pins the three samples byte-identical to `.githooks/` (`assertEqual` at lines 133, 197 and 511), and `ChildFloorWorkflowTest.test_names_no_scanner` pins the child workflow as a thin caller. `deadhook.py --status` reads a clone's wiring when run. A child that copies a scanner into its own tree is unseen |
| CRP10 | `hooks.atelierTools` is stored as an absolute path: a relative one resolves only from the main checkout and blocks every worktree commit (a fleet-wide bug of 2026-07-19) (Step 6) | enforced, partial (blocks at the call) | `.githooks/pre-commit` fails closed when the tools path does not resolve (`tools/test_precommit.py`, the baked-config resolution tests and its fail-closed cases). It makes the mistake loud at the first commit; it does not stop the config being written wrong |
| CRP11 | Prove the hook once in a new repo: stage a fake secret and see the commit blocked (Step 6; the same fact `TPL5` folds for the contributing text) | directive-only | invisible: a one-off act. `deadhook.py --status` reads wiring, not behaviour |
| CRP12 | Standardising an existing repo never overwrites an existing board's item files with the template's starter ones and never converts a one-file board or session log by hand; point at the store conversion (`fleet-sweep` item 6) and `archivecut --cut` (*Process: standardise*) | enforced, partial (warns, hook + CI) | `harvestscan --only-bulk-deletes` reads a bulk deletion of a record store's items at the hook and on CI (`REC24`, folded, warns). A hand-typed conversion that loses nothing is unseen, and so is a starter file written over an item that is not deleted |
| CRP13 | `instance.yaml.example` is the single source of the profile's schema and the skill restates none of it (intro, Step 1) | directive-only | diff: a new key in the example with no change to the skill's count, or the reverse. Measured: the example has 8 top-level groups and the skill says "eight facts", which match; the count is prose with no pin, the skill restates two defaults (`visibility: private`, `signing: false`) in Step 1, and the ADR said "seven" until its 2026-07-23 amendment |

## skills/fleet-sweep (SKILL.md and the four prompts)

Folded: see method 3, the ground-rule block repeated in all four prompts. The
sweep's own constraints follow. The "billing rule" and the limits are rows; the
steps are not (method 2).

| Id | Rule (section) | State | Guard, or where a breach shows |
| --- | --- | --- | --- |
| FSW1 | A repo is healthy when seven items hold; the principal may narrow or extend the list in the rulings file, which wins (*What healthy means here*) | directive-only | invisible: the rulings file is private and the list is read from the skill each run |
| FSW2 | Item 1: the repo's pin is origin/main's and its floor copy is identical (`pins.py` says `current` and `identical`) | directive-only | record: `pins.py --check` and `floorfleet`, both self-run instruments; the sweep runs them at step 1 and nothing runs them between sweeps (`PRO5` and `PRO44` fold the bump itself) |
| FSW3 | Item 3: every mandatory item and dated obligation in the doctrine delta since the repo's old pin is applied | directive-only | record: the digest (step 2) names them and a worker reads a repo's conformance by hand; `floorfleet` reads only that the floor is called |
| FSW4 | Item 4: a review is *owed* only where the item's own text, or the principal's words on it, says one is required; a bare `⏳`, `REVIEW.md`'s triggers or a writer's view do not count and go to the principal as a list, never into a brief | directive-only | record: the brief set read against the item's text. See *Doubts* on the tension with `REV13`'s `⏳` pointer |
| FSW5 | Item 5: the principal's queue (open decisions, questions, rulings, actions) is de-duplicated within and across repos, and answered items are marked with the citation | directive-only | record: needs a join of every repo's records; nothing reads it |
| FSW6 | Item 6: no record store is one growing file and none is missing: the session log is the folder `docs/sessions/` alone, the board is per-item files plus the generated index with done items included, a repo with no board gets the empty store, a `SESSIONS.md` is retired by `archivecut --cut`, and any other one-file entry list becomes one file per entry (exempt: `CHANGELOG.md` and reference documents) | enforced, partial (blocks, hook + CI) | `sizescan --check` reds a monolithic board's hot path and a flat running log (`REC25`, folded) and the `board` check holds the index against the item files where `docs/roadmap/` exists. Unseen: a repo with no board (`board` passes it as out-of-scope and says so), a surviving `SESSIONS.md` (a recreated one lands clean, slice 6 `RST20`) and any other one-file list. `archivecut --cut` carries its own proof at the call |
| FSW7 | Item 7: nothing is left behind by past sessions: per repo no stale pull requests or branches, leftover worktrees, stashes, untracked files or claims held by a dead session; per machine no orphaned processes, dead worktree or temporary directories, or temporary configuration a session added and forgot (a scheduled job, a permission or firewall rule, a service override) | directive-only | invisible for the machine half; record for the repo half (`cclive`, `gh pr list`, `git worktree list`). `CON26` and `CON53` are the per-branch rules; this is the sweep's standard |
| FSW8 | Act only on what is provably this sweep's own or provably stale (merged into the mainline, its owner not live per `cclive`, nothing holding it open per `lsof`, and for a worktree a clean tree and no held claim); remove a worktree without `--force`; report each removal with its proof; never delete work you cannot prove spent | enforced, partial (blocks at the call, git) | `git worktree remove` without `--force` refuses a dirty tree, and the skill names that refusal as the guard. "Provably stale" is judgement; nothing reads a removal's proof (`REC24` folds the record-store case) |
| FSW9 | Repo work never runs as an `Agent` subagent of the orchestrator: each repo's worker is a `claude -p` session `ccfleet` starts inside a worktree whose basename is the repo, so per-repo cost tools bill the repo; the orchestrator's own repo is done inline (*The billing rule*) | enforced, partial (blocks, CI test) | `instruments/test_ccfleet.py`, `EndToEnd.test_run_bills_the_repo_and_cleans_up` (worktree basename is the repo, cleaned after). A session that spawns an `Agent` for repo work anyway is unseen: the label is a harness fact `ccrepo` reads afterwards (instrument) |
| FSW10 | In scope are the repos the config lists and no others: an unlisted repo found on disk or on the forge is reported and never touched; exempt even when listed: an archived repo, a fork, a repo whose owner is not the profile's `remote.account`, each read from the forge; an owner that cannot be read is listed for the principal, not adopted; a listed, unpinned repo is adopted and not put as a question (step 1; `RST30` folds the owner half) | directive-only | invisible: the config is private; the forge read is a command |
| FSW11 | The doctrine digest is made once per origin/main short SHA, by one headless Opus session in atelier that reads `git diff <oldest pin> origin/main -- docs/method docs/build/templates` in full and writes the child obligations: mandatory on bump, dated gates, advisory, self-check commands, greps for restatements the delta makes stale (step 2) | directive-only | record: the digest file, per sweep. A digest that read the diff in part is unseen; every worker takes its obligations from it |
| FSW12 | The jobs file puts red CI and the nearest dated gates first (step 4) | directive-only | record: the jobs file's order |
| FSW13 | Every label in a jobs file is unique: a label names one job's result, and a repeat is refused before anything starts (step 4) | enforced (blocks, CI test) | `test_ccfleet.py`, `EndToEnd.test_a_jobs_file_whose_labels_repeat_is_refused_before_anything_starts` |
| FSW14 | The tier is the cheapest that does the seat well: cheaper where `pins.py` and CI would catch a worker's mistake, Opus where a mistake is silent or cannot be recalled (public repos, a client's repo, anything near secrets) (step 4; `ECO2` and `ECO18` fold the general rule) | directive-only | record: the jobs file's tier column. The "silent or irrecoverable" classification is read by nothing |
| FSW15 | The repo's notes in the config carry every fact a worker would otherwise fetch, and every ruling it must not cross (step 4) | directive-only | invisible: the config is private |
| FSW16 | A prompt launches only with every placeholder filled; the skill's table names each prompt's variables, and the example config fills every shipped prompt (*The variables the prompts need*) | enforced (blocks, CI test) | `ccfleet` refuses an unfilled placeholder (`EndToEnd.test_unfilled_placeholder_is_refused`; `ccfleet check --prompt` names them). `Config.test_the_example_vars_fill_every_shipped_prompt` (FL12) fails when a shipped prompt gains a placeholder the example config, the skill's table or `ccfleet` does not supply, and when a prompt is added without being listed |
| FSW17 | One driver per `kit_dir`: a second `drive` or `drain` on the same `kit_dir` is refused while one runs, and a second sweep takes its own `kit_dir` (step 5) | enforced (blocks, CI test) | `Locks.test_a_second_taker_is_refused` (the refusal says "one driver per kit_dir"; a dead holder leaves no stale lock) |
| FSW18 | A re-run skips a job only when its result is a clean end; a job cut off (a nonzero exit, an error, no `RESULT` line, a time limit) keeps its worktree and work and runs again; one drive writes one day's result folder, and a re-run after UTC midnight passes `--day` (step 5) | enforced, partial (blocks, CI test) | `test_drive_runs_every_job_then_resumes_by_skipping`, `test_an_unclean_run_keeps_its_worktree_and_drive_runs_it_again`, `test_drive_keeps_one_results_day`, `test_a_session_past_its_time_limit_is_ended`, `ErrorEnds`. Not pinned: the human step of passing `--day` |
| FSW19 | A worktree holding uncommitted work is never force-removed; the re-run or the principal's list takes it (step 5) | enforced, partial (blocks, CI test) | `test_a_worktree_holding_work_is_never_removed`. "By hand" is the unguarded half (`FSW8`) |
| FSW20 | Briefs owed (6a): one headless Opus brief-writer per brief, one writer at a time per repo (`drive --serial-per-repo`), healthy item 4's definition in every writer's prompt, the held-back sibling saved straight to `HELD_DIR`, and never a brief for work this session built | enforced, partial (blocks, CI test) | `test_drive_runs_every_job_then_resumes_by_skipping` pins the serial case ("the second beta job starts only after the first ends"), and FL12 pins that `HELD_DIR` is supplied. Never briefing work this session built is directive (the brief's spawn provenance, `REV19`, is the record) |
| FSW21 | Asks are de-duplicated (6b) in three phases: a cheap per-repo extract, one Opus pass over all repos for duplicates, answered and overtaken items, then per-repo mechanical fixes only (cross-link duplicates, mark answered with the citation); a merge or close on judgement goes to the principal as one list; never delete a record, supersede it | directive-only | record: the extract files (`asks.tsv`) and the repos' item edits. A deletion from a record store is `harvestscan`'s (`REC24`, folded) |
| FSW22 | Before any bulk ask, an Opus session reads every judgement row in its source context (item, thread, cited record) and not the gist, splits the rows by what "approve" would do, and asks a row that is really a question as one, never offering it for approval (6b, the check) | directive-only | invisible: the reading is in a session. Grounded in the skill: a gist alone put rows before the principal that could not be approved with confidence |
| FSW23 | Report outcome first: a table per repo (pin, CI, conformance, leftovers, reviews pending, briefs written and to write, decisions owed, actions owed, open work with an hours estimate), then the asks, the account as text then the device in the same turn (step 7; `COM10` folds the device) | directive-only | invisible: a final report. The workers' machine-read shape is `FSW30` |
| FSW24 | Before asking anything, search every repo's records (board items, session logs, decisions, reviews) for the principal's earlier answer; one found is cited and marked answered, never asked again; each ask carries its evidence up front (step 7) | directive-only | record: an ask against the repos' records, which needs a join (`COM18` folds the parallel-sessions check) |
| FSW25 | Close: the orchestrator's session record names every worker session id and commit, and no job worktree is left unaccounted for: a kept one is taken by a re-run or listed with its evidence (step 8) | directive-only | record: `ccclose` reads a close (instrument, self-run); `ccfleet` names a kept worktree on its job's `KEPT` line |
| FSW26 | A public repo's prompt never names a private repo: `ccfleet` refuses to launch one containing a configured private name, whole-word and joined forms alike; the list is only as good as its curation, so the worker prompt says it too (*Limits paid for*) | enforced, partial (blocks, CI test) | `Render.test_private_names_blocked_for_public_and_unknown`, `test_private_name_match_is_whole_word`, `PrivateNameForms`, `EndToEnd.test_public_prompt_naming_a_private_name_is_refused` and `test_a_public_prompt_naming_a_joined_private_name_is_refused`. An unconfigured name passes (the skill says so) |
| FSW27 | Workers never run review-tier work or cold passes, never write to live systems, never touch secrets, history, visibility, Actions switches, branch protection, deploy keys, webhooks or app grants, never bulk-remove from a record store, spend money or install tools; each is a stop-and-report (*Limits paid for*; the 🛑 line of the prompts) | directive-only | invisible: a headless session's act. The before-plane (`115/100`) reaches `gh repo edit`, `git push --force` and `git filter-repo` in command text, but `ccfleet` loads none of the user-level settings, so a user-level hook is not in a worker's path (`test_a_launch_loads_no_user_grant_but_keeps_its_guards`; see *Doubts*). The list is in five homes that differ (*Doctrine defects*) |
| FSW28 | Workers run with the narrowest permission mode that does the work and never a bypass mode by default; `ccfleet` loads no user-level grant, so the config is the whole grant (*Limits paid for*) | enforced, partial (blocks, CI test) | `Config.test_the_example_config_loads_and_bypasses_nothing` (FL10), `EndToEnd.test_a_launch_loads_no_user_grant_but_keeps_its_guards`, `test_check_says_when_a_permission_mode_is_set`, `test_claude_args_may_not_take_the_settings_flags_back`. An adopter's config can still set a bypass: `ccfleet check` says so and does not refuse |
| FSW29 | A split of a record store runs only when `cclive` shows the repo idle, proves line preservation by script (every original line present; only index headers and re-pathed links may differ), reports the counts, and never rewrites history (*Limits paid for*; worker prompt task 2; adopt prompt task 3) | directive-only | record: `archivecut --cut` carries its own proof at the call (instrument, self-run); the idle check is a `cclive` read taken once |
| FSW30 | A worker writes a line beginning `RESULT:` only in its final message, and the final message takes the stated shape; `DONE` is claimed only when the pin is current and identical and every workflow is green at the pushed head, or the only red is one reported as needing the principal (worker prompt; the other three prompts for their shapes) | enforced, partial (blocks, CI test) | `ccfleet` takes the last `RESULT:` line (`ResultWords.test_the_last_result_line_is_the_verdict`), a missing one reads UNKNOWN (`test_no_result_line_is_unknown`) and an error end is never read as clean (`ErrorEnds`); an earlier stray line is outvoted, not prevented. The `DONE` condition is checked afterwards by `pins.py` and `gh run list` (self-run) |
| FSW31 | A worker's session record names the dispatch ("a fleet health sweep, orchestrator session X") and its commits; in a public repo it names no other repo (worker prompt task 4; adopt prompt task 5; brief prompt method 4) | directive-only | record: the session file in each repo; the public half is `REC32` and `PRO28` (folded) |
| FSW32 | The adoption worker checks whose repo it is before any write, even though the orchestrator checked: archived, a fork, another owner's, or an owner it cannot read means write nothing and finish BLOCKED with the evidence (adopt prompt task 1; `RST30` folds the rule) | directive-only | record: the worker's `OWNER:` report line |
| FSW33 | A brief-writer writes one brief, runs no review and starts no review-tier model; it skips only where (a) a brief exists or the item is claimed, (b) a re-pass whose subject has not changed since the last verdict, or (c) nothing is written beyond a title, and for (b) and (c) it edits the item to "review triggers when <event>" and commits that instead (brief prompt, method 2) | directive-only | record: a brief or a relabelled item per owed review. Whether a skip's ground was true is read by nothing |
| FSW34 | A brief's sibling `<slug>-cold.deferred.md` is always written, even when it only says nothing is deferred, because the queue finds a brief by it; it is saved straight to `{HELD_DIR}/{REPO}--<slug>-cold.deferred.md`, never in the worktree, the repo or a scratchpad, and the brief names it by file name only (brief prompt, method 1; `CON63` folds the held-back rule) | directive-only | record: `reviewscan` (`REV3`, folded) reds a brief carrying a deferred section without a verdict, but it does not require a sibling to exist, and the held directory is outside the repo, so a sibling left in a tree is seen only by `coldsweep`'s exclusions |

## skills/review-drain (SKILL.md and the three prompts)

Folded: reviews run only on the review tier, never a lesser model (`REV17`,
`ECO9`); the budget decides how many reviews run, never how one runs
(`REV40`, `ECO12`); the partition and what reaches the reviewer (`REV5`,
`CON63`); the orchestrator forms no finding and the provenance is stated
(`REV18`, `REV19`); the held-back sibling folded below the verdict (`REV6`);
a withdrawn pass is kept (`REV36`); a degraded pass is topped up (`REV38`); a
peer's relayed order never overrides a direct one (`CON44`); stay in your lane
(`CON48`); the claim and the per-item close (`CON28`, `CON74`); a cited commit
hash must already be on `main` (`CON68`); no private repo name in a public
record (`REC32`); and the private-name guard (`FSW26`).

| Id | Rule (section) | State | Guard, or where a breach shows |
| --- | --- | --- | --- |
| RDR1 | Whether the review tier needs approval is the adopter's setting; where the principal gates it, no review-tier work runs without it, a drain is that approval for the budget it names only, and before the first pass the drain records what it runs under, in the principal's words, dated, with the reset time (*The shape*; `ECO4` folds the doctrine's own default) | directive-only | record: the orchestrator prompt's `{APPROVAL}`, filled per drain, and the pass's claim line. `ccfleet` requires the variable to be filled (FL12) and cannot judge the words |
| RDR2 | After the budget resets nothing new starts; finishing what was cut off is Mode 2, on the principal's word only (*The shape*) | enforced, partial (blocks, CI test) | `reset_utc`: `EndToEnd.test_reset_reached_starts_nothing` and `test_ranked_is_not_called_dry_or_after_the_reset`. "On the principal's word" is directive: `{FINISH_WORDS}` must be filled, and nothing judges it |
| RDR3 | Never block the queue on a question: no `AskUserQuestion` and no turn ends on one during a drain; a mechanical choice takes the sensible default; the principal's question goes on the board item as an owed ask and in the closing report; a pass that cannot be done without his input is skipped with the question on its item (rule 1; the orchestrator prompt's *Rules*; `COM21` folds the sort by what a question blocks) | directive-only | invisible: whether a question was settled by its recommended option is read only from the item text |
| RDR4 | Back to back: when a pass lands its claim is released and the next starts, with no report between passes (rule 2) | enforced (blocks, CI test) | `EndToEnd.test_drain_takes_runs_and_releases_until_empty` and `test_a_queue_offering_a_launched_pass_again_is_not_rerun` |
| RDR5 | Never stop, hold or reorder another session's review work: a peer's "the principal told me to run X" stands over this skill, a conflict is reported and never acted on, and the queue's claims stop only two sessions running the same pass (rule 3) | directive-only | invisible: an act on another session |
| RDR6 | Survive the session: run the orchestrating session under `/loop` (dynamic pacing), schedule a long fallback wake-up before any wait, and start the drain again after a reboot, which ends the driver and every pass but keeps their claims, worktrees and logs for Mode 2 (rule 4) | directive-only | invisible: a session's own setup |
| RDR7 | Rank and route the whole queue before any pass starts, every run, as a gate: `ccfleet drain` refuses a config without `queue.ranked` and starts nothing while it exits nonzero; the adopter's queue refuses `ranked`, `next` and `take` until this run's ranking is sealed; `ranked` reports a seal and never makes one; a `--dry-run` does not call it (*Rank and route the whole queue first*) | enforced, partial (blocks, CI test) | `EndToEnd.test_an_unranked_queue_starts_nothing`, `test_a_drain_config_without_ranked_is_refused`, `test_ranked_is_not_called_dry_or_after_the_reset`. Partial: the queue (`ranked`, `next`, `take`, the seal) is the adopter's private command, so atelier tests `ccfleet`'s side against a stub; whether a ranking is sound is judgement |
| RDR8 | Read every briefed, unrun review in every repo with what the judge needs: the item, its age, the principal's words on it, dates ahead, what it guards, what waits on its verdict, and what each route can and cannot do for it (ranking step 1) | directive-only | invisible: the queue is private; the seal refuses a ready review that is missing, not one read thinly |
| RDR9 | Rank by judgement: the principal's direction first (this run's words, then standing words on an item), then importance, urgency (a real date first), the risk the review mitigates (credentials, public exposure, live or irreversible paths, money) and the value of the work it unlocks; a pass whose core needs a live write last; a standing repo order breaks ties only (ranking step 2) | directive-only | invisible: the ranking is private |
| RDR10 | Route each review only to a route that reaches local quality: the route drawing the budget that lapses soonest goes first when a lapse is near, otherwise the cheapest capable route (batch where the review fits, then credit, then the included budget), cost breaking a tie; a review needing probes or re-run lines does not fit a single-request batch; unsure means the local route; quality is never traded for price or for a lapse (ranking step 3; `REV40` folds the budget rule) | directive-only | invisible: the routing is private and sealed in the adopter's queue |
| RDR11 | The seal states the principal's words for this run (or "none given") and refuses while a ready review is missing, unreasoned, on a closed route, or on a later route than the best it fits without saying why, or while two budgets are open and either lapse time is unknown; a seal lasts one run and no seal outlives the first lapse among the budgets it routes to (ranking step 4) | directive-only | invisible: the seal logic is in the adopter's queue command, which is not in this repo and was not read; atelier's side is `RDR7`'s refusal |
| RDR12 | Each route takes only its own reviews in rank order; the local route takes its own first and then another route's not-yet-started reviews, never from a budget that lapses before its own; a review briefed after the seal runs last on the local route until it is ranked and the ranking sealed again | directive-only | invisible: as `RDR11` |
| RDR13 | A review the principal has tied to a route by name is not spilled to another route: his words outrank the skill's spill, and the seal marks such a review not spillable (the general question stays open for him) | directive-only | invisible: as `RDR11`; the open question is named in *Doubts* |
| RDR14 | A review that "needs a brief" is a defect fixed on Opus between drains and not a state to report; only owed reviews get a brief; never brief a pass whose subject this session built (*Briefs are never left owed*) | directive-only | record: the queue's owed set against the briefs; `FSW4` and `FSW33` are the sweep's side |
| RDR15 | Tell the live sessions once (`ListAgents`, then `SendMessage`): quote the approval, ask each to claim a pass through the queue before running it, give no other instruction and never ask a session to wait for this one (Mode 1 step 2) | directive-only | invisible: messages between sessions |
| RDR16 | The driver starts one pass per stagger only while load, memory and disk have headroom; the ceiling is live in `<kit_dir>/max`; it stops on an empty queue, the reset, the stop file, a pass reporting `BUDGET EXHAUSTED` or three unclean ends in a row; a stop file older than the driver is ignored and said once (Mode 1 steps 1 and 3) | enforced (blocks, CI test) | `Gate`, `PacingFiles` (stale stop file ignored, max file read live), `EndToEnd.test_drain_stops_after_three_unclean_ends_and_keeps_claims`, `test_max_0_is_a_ceiling_of_0`, `test_reset_reached_starts_nothing` |
| RDR17 | A pass that ends before its session starts comes back off the launched list and counts toward the unclean stop; a `--dry-run` keeps its own list, so a rehearsal cannot empty the real queue; a drain that says "queue empty" having started nothing while `next` still offers a pass is a fault to report, never an empty queue (Mode 1 step 3) | enforced (blocks, CI test) | `test_a_pick_that_never_starts_comes_off_the_list_and_counts`, `test_a_dry_drain_leaves_the_real_drain_its_queue`, `test_a_failing_queue_next_is_not_an_empty_queue`, `test_drain_with_an_empty_queue_exits_4` |
| RDR18 | A pass ends clean only when its session exited 0, ended on no error and its verdict is `DONE` or `SKIPPED`; only then are the claim released and the worktree removed; any other end (a nonzero exit, an error, a usage limit, no report) keeps the claim, the worktree and the review log for Mode 2; a worktree holding uncommitted work is never force-removed, by `ccfleet` or by hand (Mode 1 step 4) | enforced, partial (blocks, CI test) | `test_a_nonzero_exit_keeps_the_worktree_and_is_not_done`, `test_a_cut_off_pass_keeps_its_claim_and_its_worktree`, `test_a_worktree_holding_work_is_never_removed`, `ErrorEnds`. "By hand" is the unguarded half |
| RDR19 | Every launch sets `CLAUDE_CODE_PRINT_BG_WAIT_CEILING_MS=0` (a background subagent is otherwise killed about ten minutes after the orchestrator's last turn) and gives `claude -p` stdin from `/dev/null` (*Lessons paid for*) | enforced (blocks, CI test) | `EndToEnd.test_every_launch_sets_the_wait_ceiling_and_the_config_env`; `ccfleet` passes `stdin=subprocess.DEVNULL` at lines 826 and 869, which no test names |
| RDR20 | A verdict is read from the session transcript only from the last assistant text carrying the final output's `ITEM:` line, and never after a nonzero exit or an error end; the prompts forbid writing a `RESULT:` or `ITEM:` line anywhere but the final output (*Lessons paid for*) | enforced, partial (blocks, CI test) | `TranscriptFallback` and `ErrorEnds.test_an_error_end_never_reads_the_transcript` pin the reading; the prompts' ban on a stray line is text only (the reader outvotes a stray line, `FSW30`) |
| RDR21 | Read-only reads of live systems are allowed as a review needs them and live writes never: a pass whose core needs a live write is skipped as `NEEDS LIVE WRITE` and ranked last, a single such check is marked `NOT RUN`, a verb of unsure effect counts as a write, fields are allowlisted before printing, and no live capture is left in scratch (*Lessons paid for*; orchestrator prompt step 4) | directive-only | invisible: a live call in a headless session; the before-plane reaches a write verb in command text only where a hook runs (`FSW27`) |
| RDR22 | Several briefs can share one board item and the claim is per item, so the queue's `next` must skip an item already claimed (*Lessons paid for*) | directive-only | invisible: the adopter's queue; `ccfleet`'s launched-list test covers a queue that re-offers a pass, not an item with a held claim |
| RDR23 | When the limit hits, a pass whose act 2 is already written needs only a fold, run by `ccfleet run ... --prompt fold-prompt.md --item ITEM` on a cheaper tier; on a clean `RESULT` ccfleet releases the claim and removes the worktree, any other end keeps both, a clean `RESULT` that leaves unlanded work reads `UNLANDED` and keeps them, and the held copy is deleted by the drain session once it reads `DONE` (*Lessons paid for*) | enforced, partial (blocks, CI test) | `test_a_fold_releases_and_puts_its_worktree_away`, `test_a_clean_pass_that_leaves_unlanded_work_keeps_its_claim_and_resumes`, `test_unlanded_may_not_be_a_release_word`, `test_a_refused_release_keeps_the_pass_worktree_and_exits_2`. "On a cheaper tier" and the held-copy deletion are directive |
| RDR24 | A sandboxed API route (no network, no `gh`, temp-only writes) cannot match a local pass whose brief leans on those, so briefs are triaged before they go there, and a degraded pass gets a full local re-run, put to the principal (*Lessons paid for*; `REV38` folds the top-up rule) | directive-only | record: a verdict states its route; the triage is private |
| RDR25 | Resume (Mode 2) only on the principal's word, and start nothing new; read each cut pass's reviewer transcript first, un-claim one whose reviewer did almost nothing (restarting is new work) and move its review log into a dated `review-logs/withdrawn/` file, kept and never handed to the item's next reviewer; resume the rest through `ccfleet resume` (*Mode 2*) | enforced, partial (blocks, CI test) | `ccfleet`'s side: `test_resume_fills_every_value_and_checks_the_release`, `test_two_resumes_of_one_session_cannot_run_at_once`, `test_resume_without_an_item_calls_no_queue_command`, and `test_review_logs_never_collide_and_a_fresh_pass_inherits_none` (a new pass that finds a log at its path moves it). "On the principal's word" and "almost nothing" are judgement; `REV36` folds the withdrawn rule |
| RDR26 | If the reviewer cannot be reached on resume the pass reports FAILED; it is never handed to a replacement reviewer or a lesser model, and the claim, worktree and log stay for the principal's word (*Mode 2*; the resume prompt) | directive-only | invisible: a failed `SendMessage` and what a session does next; `REV17` and `ECO9` fold the general rule |
| RDR27 | A reviewer writes only its review log and the brief file (act 1 below a `---` divider, an updated Status line, the file's own column width, absolute dates) and never commits, pushes, opens a GUI app or leaves a live capture in scratch (*The reviewer prompt*) | directive-only | diff: files changed in the pass's worktree beyond the brief. The orchestrator commits by pathspec (`git commit -- <brief>`, prompt step 5), so a stray file is left out of the commit, not refused |
| RDR28 | The reviewer keeps a running review log at `{REVIEW_LOG}` (outside the repo, one path per pass): each check and its result with the exact command or file and line, each candidate finding with its evidence and deciding criterion, each point checked and not raised; no secrets or live captures; a fresh pass starts with no log, and a file already at its path is an earlier pass's, never handed to a fresh reviewer (the orchestrator stops and reports) | enforced, partial (blocks, CI test) | `test_review_logs_never_collide_and_a_fresh_pass_inherits_none`, `test_a_pass_and_its_resume_share_one_review_log_path`, `test_review_log_hash_is_sha2_and_earlier_names_are_still_found`. The log's content is `REV34`'s judgement; "no secrets in it" is reached by `secretscan` only after a fold into a committed brief |
| RDR29 | The review log is private while the pass runs: until act 2 is saved no other session reads, edits or comments on it or steers the review, except on the principal's order or to stop harm; at the fold the orchestrator appends it verbatim under the stated heading and deletes the file (*The reviewer prompt*) | directive-only | record: the fold heading in the brief, once folded. A read of the log before act 2 leaves no trace |
| RDR30 | The close: count the verdicts from the rows (the result files in every day folder the drain ran across, and the launched list), never from memory; `review-logs/` holds only the logs of passes whose claim is held, and any other log left there is appended verbatim to its brief, landed and deleted; remove the drain's one-off config entries; write a session record in each repo touched and one in the estate root naming every pass, session and commit (*Close*) | directive-only | record: result files against the report; `ccclose` reads a close (instrument, self-run). A close once reported totals from memory and was wrong twice (the skill) |
| RDR31 | The per-pass orchestrator forms no finding, writes no severity and never reads the held sibling's contents; on the barred check (the brief bars its session, or a run constraint cannot be met) it reports SKIPPED with the reason; a check that needs a live write is `NOT RUN`, and where the core needs one it does not start the reviewer (orchestrator prompt, steps 1 and 3) | directive-only | invisible: a headless session that reads nothing it should not leaves no trace; `REV18` folds the off-tier orchestrator's disclosure |
| RDR32 | The orchestrator never edits the reviewer's text: a gate that blocks act 1 goes back to the reviewer by `SendMessage`, and the only edits at the fold are form-only gate fixes (wrap, date or spelling markers on verbatim quotes), said under the fold heading (orchestrator prompt steps 5 and 7; fold prompt) | directive-only | diff: the fold commit against act 2's text; nothing compares them |
| RDR33 | A fold-only session runs no review-tier model, spawns no subagent, forms no finding, writes no severity and changes no reviewer text; it commits, folds, flips the item, rebuilds the board and lands (fold prompt) | directive-only | invisible: the fold session's model is set by whoever calls `ccfleet run`; the tests pin the release behaviour and not the tier |
| RDR34 | On a usage-limit error the orchestrator or reviewer stops at once, leaves the claim and the worktree as they are (never removed or reset: it may hold the reviewer's unsaved act) and reports `BUDGET EXHAUSTED` with "at act N" and the reviewer's agent id (orchestrator prompt *Rules*; resume prompt) | enforced, partial (blocks, CI test) | `test_a_cut_off_pass_keeps_its_claim_and_its_worktree` and `test_drain_stops_after_three_unclean_ends_and_keeps_claims` pin `ccfleet`'s keeping; the agent's own stop-at-once and its report are text |
| RDR35 | A pass's final output is `RESULT: <DONE\|SKIPPED\|BUDGET EXHAUSTED\|FAILED>` alone on its line, then `ITEM`, `VERDICT`, `RULINGS OWED`, `COMMITS` and `NOTES`, with any reason in `NOTES` (orchestrator prompt) | enforced, partial (blocks, CI test) | `ResultWords.test_plain_endings_read_as_their_first_word`, `test_no_result_line_is_unknown`, `Harvest`. `ccfleet` reads `RESULT` and `ITEM`; the other four fields are unread |

## commands/

Four commands, each a prompt the user invokes; their front matter is not a
rule. The menu that lists them is pinned (`PLG3`).

| Id | Rule (section) | State | Guard, or where a breach shows |
| --- | --- | --- | --- |
| CMD1 | After `/atelier:install-hook`, prove the hook once (the scanners' selftest, `deadhook.py --status`, optionally a staged test secret refused and then removed), report the result honestly, and tell the user that the hook guards only this clone, must be re-run after a plugin update or uninstall, and that `git commit --no-verify` is for a real emergency only | directive-only | invisible: the report. `deadhook.py --status` is an instrument; the re-run half is `RDM2`'s (enforced, partial: the hook blocks until re-pointed), folded |
| CMD2 | Install the three hooks into the directory git reports for this clone (`git rev-parse --git-path hooks`) and store `hooks.atelierTools` as the resolved absolute path, never the literal `${CLAUDE_PLUGIN_ROOT}`, which is undefined at commit time | enforced, partial (blocks at the call) | the stored-path half is `CRP10` (the hook fails closed on an unresolved path). The install location contradicts `0008` decision 4 (a tracked `.githooks/` with `core.hooksPath`): two wirings for one hook, already a slice 6 doubt, now read at both homes (*Doctrine defects*) |
| CMD3 | `/atelier:scan` runs the four scanners in order from the repository root, treats exit 2 as a real failure and never as clean, reports a secret or leak first and plainly, never softens a real finding, and tells the user the two hatches for a false positive (an inline marker, or a root-relative ignore glob; `GRD8` and `GRD15` fold the hatches) | directive-only | invisible: what a session reported. Each scanner's own exit contract is tested in its own suite; `EVI19` folds "unknown is a required output" |
| CMD4 | `/atelier:worktree`: run from inside the target repo; with no argument run `list`; a guarded `remove` that refuses protects unmerged work, so say so and stop and never force it | enforced, partial (blocks at the call) | `tools/worktree.py remove` refuses a worktree with uncommitted or unmerged work (`tools/test_worktree.py`). "Stop and never force it" is text, and `git worktree remove --force` is available to a session outside the tool |
| CMD5 | `/atelier:fleet-pins`: pass `--atelier <live checkout>` when running from the plugin so the SHAs compare against real history; a failed fetch exits 2 as no result and not as no drift; do not recommend bumping a pin without showing the intervening commits, because reconciling a stale child is a pin bump after reading them and not a blind edit | enforced, partial (blocks at the call) | `tools/test_pins.py`, `test_failed_fetch_is_no_result_not_no_drift` and `test_default_fetches_and_measures_against_origin_main`. "Show the commits before recommending" and "pass `--atelier`" are text (`PRO4` and `PRO5` fold the doctrine) |

## .claude-plugin/ and instruments/atelier-menu

| Id | Rule (section) | State | Guard, or where a breach shows |
| --- | --- | --- | --- |
| PLG1 | The plugin carries no `version`: each commit is its own version, on the principal's close-out answer of 2026-10-18 (`180/040`), and putting one back reverses that choice and is his call (`PROPAGATION.md` § *The bundled-mode variant*) | directive-only | diff: a `"version"` key in either manifest. Measured: 0 in both files. A tripwire that lands clean; the doctrine's own bundled-mode drift check greps for the key (*Doctrine defects*) |
| PLG2 | The plugin ships the whole repo (`source: "./"`) and packages no second copy of doctrine, templates or tools (`2026-07-21-0748`, *Rejected*) | directive-only | diff: a duplicated tree. Measured: `marketplace.json` sets `source: "./"` and `git ls-files` lists one `docs/method/PROPAGATION.md`. Nothing would see a copy placed under another root |
| PLG3 | The bare `/atelier` skill shows `menu.py`'s output as it is, with at most one line naming what it is before the table; when the user names a command it shows the menu and tells them the exact command to type, and does not run it (`instruments/atelier-menu/SKILL.md`) | directive-only | invisible: what a session printed. The content is pinned: `instruments/test_atelier_menu.py` (`test_lists_every_plugin_command`, `test_skill_is_named_atelier`) holds that every skill and command appears, read from front matter at run time. `MEC5` folds the skill's home outside the plugin |

## Counts

Each rule counted once, under the state and place it first shows. Slice 7:

| Area | Rules | Enforced (partial) | blocks | warns | Directive-only | diff | record | invisible | Accepted |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| docs/decisions/ | 21 | 12 (9) | 11 | 1 | 9 | 6 | 2 | 1 | 0 |
| session-onramp | 2 | 0 (0) | 0 | 0 | 2 | 0 | 0 | 2 | 0 |
| queue-run | 1 | 1 (0) | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| review-brief | 2 | 0 (0) | 0 | 0 | 2 | 1 | 0 | 1 | 0 |
| create-repo | 13 | 4 (4) | 3 | 1 | 9 | 4 | 1 | 4 | 0 |
| fleet-sweep | 34 | 12 (9) | 12 | 0 | 22 | 0 | 15 | 7 | 0 |
| review-drain | 35 | 13 (9) | 13 | 0 | 22 | 2 | 5 | 15 | 0 |
| commands | 5 | 3 (3) | 3 | 0 | 2 | 0 | 0 | 2 | 0 |
| plugin and menu | 3 | 0 (0) | 0 | 0 | 3 | 2 | 0 | 1 | 0 |
| Slice 7 | 116 | 45 (34) | 43 | 2 | 71 | 15 | 23 | 33 | 0 |
| Slice 6 | 68 | 25 (19) | 24 | 1 | 43 | 19 | 12 | 12 | 0 |
| Slice 5 | 73 | 19 (14) | 15 | 4 | 54 | 12 | 15 | 27 | 0 |
| Slice 4 | 106 | 5 (5) | 4 | 1 | 99 | 60 | 9 | 30 | 2 |
| Slice 3 | 94 | 9 (9) | 8 | 1 | 81 | 20 | 7 | 54 | 4 |
| Slice 2 | 129 | 27 (19) | 15 | 12 | 101 | 36 | 23 | 42 | 1 |
| Slice 1 | 158 | 19 (11) | 14 | 5 | 133 | 35 | 33 | 65 | 6 |
| Running total | 744 | 149 (111) | 123 | 26 | 582 | 197 | 122 | 263 | 13 |

As in slices 1 to 6: *diff*, *record* and *invisible* split the directive-only
count, each rule once, under the place a breach first shows. *blocks* includes
the CI test pins (the `ccfleet`, `ccmail` and `ccapple` suites fail the run
after a push) and the tool's own refusal at the call. The running total counts
one rule twice, EVIDENCE section 17 as `EVI24` and as `CON21`, so net of it the
running total is 743 distinct rules. The state changes recorded since earlier
slices (slice 5's `AUT17` re-grade, slice 4's `PRI8` correction) are not
applied to the totals: each slice's counts stay as that slice found them.

Reading the table. Slice 7 has 45 of 116 rules (39%) with a check, against 37%
for slice 6, and 34 of the 45 cover only part of the rule. The split is by
what a skill drives. `fleet-sweep` and `review-drain` are 25 of 69 enforced
because `ccfleet` holds their constraints as code and
`instruments/test_ccfleet.py` (88 tests) pins them: one driver per `kit_dir`,
a cut-off pass keeps its claim and worktree, a drain starts nothing until the
queue is ranked. The other 44 rules in those two skills are what a *session*
does with the tool: how it ranks, what it asks, what it reports. Nothing reads
those. `create-repo` is 4 of 13 for the same reason (its hook and stamp rules
sit on `test_precommit.py` and `test_templates.py`; its profile and its
proofs do not). `session-onramp`, `review-brief` and the decision records'
own rules are almost all text, and the decision records' standing rules are
mostly folded because the doctrine files already carry them. Of the six skills,
two (`review-brief`, `queue-run`) carry a stamped-copy marker and a CI test;
the other four restate doctrine with no marker and no pin. Across the
seven slices, 20% of the 744 rules have any mechanical check, and 111 of those
149 cover only part of the rule.

## Top five guard candidates

Directive-only, breach visible in the diff, costly when it happens, ranked by
what a first run on the live tree would find:

1. **PRO1, a CHANGELOG line with a skill, command or manifest change.** A
   commit-plane check: a commit that stages a path under `skills/`,
   `commands/` or `.claude-plugin/` and does not stage `CHANGELOG.md`, with a
   reasoned marker for a typo or wrap-only change. Measured: 17 of the last 40
   commits touching those paths carry no CHANGELOG line, and all 17 subjects
   read as behaviour changes (`ccfleet: make the config the whole grant`,
   `skills: review-drain reads a cut-off pass as cut off`, and
   `fleet-sweep: a missing board fails health`). It ranks first because
   `PROPAGATION.md` names the CHANGELOG as "the one signal left" for a
   plugin-only adopter now that the manifest has no version (*The bundled-mode
   variant*). The same path-only check over `docs/method` is 3 of 60 (census
   files excluded) and would be mostly noise there: many of those commits are
   wrap or link changes, so it should start on the plugin surfaces only.
2. **DEC review lines against the reviews that exist.** A check that a decision
   record whose review line says "queued" or "owed" does not have a file in
   `docs/reviews/` that names the record and holds a verdict. Measured on the
   8 post-boundary records: 3 read `queued` beside a finished pass
   (`2026-07-21-0744`: verdict at line 235 of `2026-07-21-0913-review-line-artefact-cold.md`;
   `2026-07-23-0001`: `PASS-WITH-FINDINGS` in `2026-07-23-0222-economics-billing-states-cold.md`;
   `2026-08-05-1233`: `VERDICT WRITTEN 2026-11-15` in
   `2026-11-09-0126-private-state-type-only-cold.md`), and a fourth
   (`2026-08-15-0610`) is contradictory: its own amendments cite the pass's
   findings (BS1) while the brief's Status still reads "REVIEW NOT RUN".
   `reviewscan` checks presence only, by design, and `pointerscan` reads
   roadmap files, so it scanned 0 files over `docs/decisions`. The class has
   recurred: three records had to be corrected by hand on 2026-11-01.
3. **A stamped-copy marker or a declared "holds its own rules" marker on every
   skill.** A test over `skills/*/SKILL.md`. Measured: 2 of 6 skills carry the
   marker and a pin; `session-onramp` restates the apex, `create-repo`
   restates the repo standard, `fleet-sweep` restates `RECORD.md` and
   `ECONOMICS.md`, and `review-drain` restates `CONCURRENCY.md`, with no
   marker or pin on any. This is the drift class that shipped twice (F3 and
   SL1) and the one the two pins were written for; `session-onramp`'s
   companion list already omits two of the six skills (*Doctrine defects*).
4. **Ground-rule parity across the four `fleet-sweep` prompts.** A test that
   the shared 🛑 never-list and the answer-not-a-ruling bullet are identical
   across `worker-prompt`, `adopt-prompt`, `task-prompt` and `brief-prompt`, or
   that they are one included block. Measured: three wordings of the list across
   the four prompts (worker and task match; adopt drops "(board, session logs,
   ADRs, reviews)"; brief drops "bulk-remove", "spend money" and "install
   tools"), and the skill's own *Limits paid for* line is a fifth, shorter form.
   `FL12` already pins which placeholders each prompt has; none pins the text
   they share.
5. **Standard-library imports only under `tools/` and in Python instruments.** A
   tripwire. Measured: 0 of 113 files import outside the standard library
   (`browser-fetch`, which `0006` admits, is excluded). It lands clean and ties
   `0006`'s `tools/` rule to the tree; it is also the check that would have
   made `SECURITY.md`'s "takes no third-party dependencies" either true or
   visibly scoped (slice 6, defect).

Next after these, each measured:

- Scope `spellscan` and `datescan` (and `attribscan`) to `skills/` and
  `commands/`: spelling 0 findings, dates 0, attribution 2 (advisory). Free
  today, and closes the gap that the doctrine-by-function surface has no prose
  check (method 6). `wrapscan` over the same paths is 109 findings, many of them
  front matter that must stay on one line, so it needs a front-matter exemption
  first; `pathscan` is 16, all false-positive shapes.
- A Status vocabulary check on decision records: fires twice (`proposed`).
- A `"version"` key tripwire in the manifests (`PLG1`): 0 hits; it is also the
  check that would flag the day the bundled-mode proof starts to work.
- `instance.yaml` named in `publishscan`'s tracked-file list (`CRP2`): 0 hits;
  it holds a name and an email, so `leakscan` would see part of it already.
- A test that `create-repo`'s eight-template `MISSING` loop and the example's
  key count match the tree (`CRP3`, `CRP13`): 0 hits today.
- `at HEAD` in a decision record (`DEC1`): 1 hit, frozen, pre-rule.
- The dotted `unittest tools.test_` form in a brief (`RBF1`): 40 hits mixed,
  not rankable.

**Not diff-visible, a read of GitHub.** `DEC4` and `DEC5` rest on a host
ruleset that leaves no diff. `floorfleet` reads two of its three legs when
someone runs it. On 2026-11-23 the ruleset read `deletion`, `non_fast_forward`
and `required_signatures` with no bypass actor. A scheduled `floorfleet
--check` is an instrument change, not a diff guard.

**Before-plane note for `115/100`, not a diff guard.** `FSW27` and `RDR21`
bar a worker's live write, a force-push and a history rewrite, all of which are
visible in a command's text. Whether a before-plane hook reaches a `ccfleet`
worker depends on the repo's own settings: `ccfleet` loads no user-level
settings. A hook installed at user level, which is where the person-local
guards sit, is not in a worker's path.

## Doctrine defects found, not fixed here

Each is owed its own board item (`PROPAGATION.md` § *Pointing up*) where it
has none; none is changed by this file.

- **`create-repo`'s bundled-mode proof cannot pass, and `<VERSION>` has no
  source.** Step 5 fills `<VERSION>` from "the `version` in
  `$SRC/.claude-plugin/plugin.json`" and proves the stamp by expecting that
  `grep '"version"'` prints it. Commit `140a1902` (2026-10-18) removed the key
  from both manifests, and neither has one. `PROPAGATION.md` says the drift
  check in this mode is "weaker than it reads"; the skill's step and its proof
  say nothing of it, and the 2026-07-21 record's "version bump on the manifests"
  consequence is a state that no longer exists. A bundled-mode scaffold either
  stamps an empty version or stops at an unsatisfiable proof.
- **Four of the five `draft` decision records state decisions already in
  force, and two use a word the README does not define.** `2026-07-18`,
  `2026-07-19`, `2026-07-21-0744` and `2026-07-23` are `draft`; their substance
  is in `REVIEW.md`, `ECONOMICS.md`, `reviewscan` and CI. The README says a
  draft "binds on nothing" and acceptance is the principal's call, so by the
  README's own text these four bind nothing while the doctrine they drove binds.
  `2026-11-09-1334` and `2026-11-09-board-states-design` use `proposed`, which
  no spec lists. Separately, three post-boundary records still say their review
  is "queued" beside a finished pass (candidate 2). Whether to accept, revoke
  or amend each is the principal's call; this file does not make it.
- **The `/atelier:scan` command runs four of 21 floor checks and calls them the
  publish-safety floor.** The command names `secretscan`, `leakscan`,
  `licenscan` and `linkscan`; so do both manifest descriptions ("publish-safety
  scanners (secret / leak / licence / link)"). The registry carries 21 entries,
  including `publishscan`, `pdlistscan`, `sizescan` and `board`. It is the one
  way a plugin-only adopter runs the scanners by hand, and it is a subset.
- **One hook, two wirings, now read at both homes.** `0008` decision 4 and
  `create-repo` step 6 say the hook is tracked in `.githooks/` with
  `core.hooksPath`; `/atelier:install-hook` copies it into git's hooks
  directory for the clone and tells the user it guards that clone only.
  `git rev-parse --git-path hooks` follows a set `core.hooksPath`, so the two
  coincide where the path is set; where it is not, the command installs the
  untracked form the decision was made to end. Slice 6 raised this from the
  template side.
- **`session-onramp`'s companion list omits two of six skills, and both
  manifest descriptions omit three.** The list stops at `create-repo`,
  `worktree` and `fleet-pins`; `fleet-sweep` and `review-drain` are absent, as
  they are from the root README (slice 6). `plugin.json` and `marketplace.json`
  name the onramp, review, scaffolding, scanners and the two commands, and omit
  `queue-run`, `fleet-sweep` and `review-drain`. The menu is generated from
  front matter and does not have this fault (`instruments/test_atelier_menu.py`).
- **The 🛑 never-list is in five homes and they differ; the reviewer prompt is
  in two.** See candidate 4. A brief-writer's prompt omits "spend money;
  install tools"; the skill's *Limits paid for* omits both those and the
  branch-protection, deploy-key and webhook items. Separately,
  `review-drain/SKILL.md`'s *The reviewer prompt* section and
  `orchestrator-prompt.md` step 4 each state what the reviewer is told, and the
  prompt names the skill's section as "your template" while adding items the
  section lacks (allowlisting provider fields before printing; no captures left
  in scratch). One fact, two homes (`V4`).
- **`PRO1` is the plugin adopter's only drift signal and is skipped in 17 of 40
  recent commits to the plugin surfaces.** `PROPAGATION.md` makes the CHANGELOG
  line "the one signal left". Measured at candidate 1. The rule is
  `directive-only` (`PRO1`) and nothing reads its breach.
- **`fleet-sweep` item 4 and `REVIEW.md` rule 4 use "owed" two ways.** Rule 4
  has the author queue a `⏳` pointer when a cold pass is owed; the skill says
  "a bare `⏳` ... do not count" as owed and sends it to the principal as a list.
  The skill's narrower sense is deliberate (a review's brief waits for the
  principal's approval of the review tier), but both documents use the word and
  a `⏳` pointer is the item text saying a review is required. A reader of one
  document would conclude the other is wrong. Named as a question, not a
  verdict (*Doubts*).

Checked and found sound: the queue-run skill is delivery only and its
pins hold (`test_queue_run_single_source.py`); `ReviewBriefSkillTest`
and `LensRosterParityTest` pass against `REVIEW.md`'s current roster; the
plugin carries no version, as `README.md` says; `instruments/install`, the
tracked hooks and the samples agree byte for byte (pinned by `test_precommit`);
`ccfleet` refuses to launch a prompt with an unfilled placeholder and
`Config` (FL12) holds the shipped prompts to it; the host ruleset on `main`
reads as `0008`'s 2026-10-16 amendment says.

## Doubts and unverified points

- **No rule is counted unenforceable and accepted in this slice.** The nearest
  candidates are `RDR9` and `RDR10` (the ranking and routing of a private queue
  are judgement by design) and `RDR13`'s open question; none was counted
  accepted because no document says the cost is unobservable. A reader may
  grade them the way slice 3 graded `ECO9`.
- **Skill step boundaries are a judgement.** A skill is procedure, and this
  census counts constraints and standards, not each step (method 2). A
  stricter count that made every "run X" a rule would raise the total and the
  directive-only share; a looser one would fold more of `fleet-sweep` into
  `CON` rows. Several rows join sentences the skill states separately
  (`FSW6`, `FSW7`, `FSW21`, `RDR10` and `RDR30` are the longest).
- **The adopter's queue and the seal were not read.** `review-drain` says the
  queue's `ranked`, `next` and `take` refuse until a ranking is sealed; those
  commands live in the adopter's private config, outside this repo. Rows
  `RDR8` to `RDR13` are graded on what the skill says and on `ccfleet`'s test
  against a stub, and nothing here confirms the seal does what the skill says.
- **Whether a `ccfleet` worker runs a repo's own hooks was not established.**
  The test name `test_a_launch_loads_no_user_grant_but_keeps_its_guards` says
  the launch "keeps its guards"; I did not read what guards, so `FSW27`'s
  before-plane note is a hypothesis about where a hook could run, not a
  measurement.
- **One open question is stated inside a skill.** `review-drain` says whether a
  seal's spill may move a review the principal tied to a route by name is "the
  adopter's principal's to rule" and leaves it open (`RDR13`). It binds until
  he rules, and is the one place a skill declares a gap in its own rule.
- **`create-repo` step 7 stages with `git add -A`.** `CON7` bars it. The
  command block sits in the new-repo process only, and in a brand-new repo with
  no worktree beside it the hazard `CON7` guards is absent. Not counted as a
  breach; the skill and the rule read differently on the page.
- **`ci-<type>.yml` has two templates for four types.** The standard sizes a
  repo as static, package, infra or docs; `ci-python.yml` and `ci-static.yml`
  exist. What an infra or docs repo copies is unstated (`CRP6`).
- **The command allowlists were not judged.** `fleet-pins` and `worktree` grant
  `Bash(git:*)` and their bodies run only `python3` (the tool runs `git`
  inside). `AUT14` makes a widened allowlist a confirm; whether a grant wider
  than the body needs is a defect was not decided.
- **The hatches the commands name were not each probed.** `scan.md` lists
  `licenscan:allow:` and `.licenscanignore`; `install-hook.md` lists
  "`.*scanignore` globs". The scanners' own allow-marker lists are the source
  (`tools/README.md`); I did not check each name.
- **Counts in the measurements are crude where said so.** The CHANGELOG ratio
  reads the last 40 commits that touch three paths (the oldest dated 2026-10-18)
  and the docs/method ratio the last 60 since 2026-11-21 with the census files
  excluded; the 17 subjects were sampled, not each diff read. The
  `docs/reviews` grep for the dotted unittest form is by line and counts prose.
  The `ast` import read ran on Python 3.14.6; the hooks run under 3.9, where
  `sys.stdlib_module_names` does not exist, so a built check would need its own
  list.
- **Every suite cited ran at this commit and passed.** `test_ccfleet.py`
  (88 tests), `test_templates.py` with `test_queue_run_single_source.py` (67),
  `test_ccapple.py` with `test_atelier_menu.py` (124), the `ccmail` and
  `ccarchive` node suites (300), and in `tools/` `test_precommit`, `test_board`,
  `test_floorfleet`, `test_pins`, `test_worktree`, `test_reviewscan`,
  `test_indexscan` and `test_floor` together (753). A pass shows the pin holds
  today; it does not show a pin exists for every sentence of a rule.
- **Earlier slices' doctrine files have moved since they were censused**
  (slices 5 and 6 each recorded sixteen commits). This slice did not re-measure
  it. The census is a count at a time, and `AUT17` and `PRI8` are still
  unre-graded.

## Remaining doctrine, outside `docs/method/` and not in this slice

Listed only, not censused, in the order the item's scope reads:

1. **The validators' own stated rules**: the declarations in `tools/floor.py`'s
   registry, each scanner's docstring, `tools/README.md`,
   `instruments/README.md` and the `*.design.md` notes, where a rule is stated
   as what a check does. This slice cited several (`DEC2`, `DEC8`, `DEC20`)
   without censusing them.
2. **`docs/PERSONAL-DATA.md`** (the closed list) and the generated
   `docs/ROADMAP.md` index's standing rules. `RST23` to `RST25` count the
   *standard's* personal-data rules; the list's own entries are not censused.
3. **`docs/roadmap/README.md` and `docs/reviews/README.md` at atelier's own
   root**, the live originals the templates copy; read for folds and given no
   rows.
4. **`ccfleet --doc` and `instruments/man/ccfleet.1`**, the runner's own
   reference, which a skill points at. They state what the tool does, and the
   tool's tests were read for that; the pages themselves were not censused.

Within this slice's scope nothing is left out: every file named in the brief
(`docs/decisions/`, the six skills and their bundled files, the four commands
and the two manifests) was read in full, and every rule in it is a row or a
named fold. The three open decision records count at zero by design.
