# Enforcement census — docs/build/, templates, root CLAUDE.md, SECURITY.md, README.md

Board item `020/220`, slice 6 of the census, the first slice outside
`docs/method/`. Run 2026-11-23 (UTC) by a worker of queue run 608d. This is a
measurement record, not doctrine: it changes no rule, and it builds no guard. It
uses slice 1's method, states and row format
(`docs/method/census/2026-11-16-1142-record-review-concurrency.md`) and the
fold conventions of slices 2 to 5, so the six slices add up. Slice 5
(`docs/method/census/2026-11-23-1651-reach-secrets-signing-storage-toolbox-session-open.md`)
is the one this continues.

## What this asks

For each rule in the files below: if it is broken, what sees it? Each rule gets
one state, defined as in slice 1.

- **enforced**: a mechanical check reads the breach. The row names the check,
  the plane it runs on (the pre-commit hook, the commit-message hook, CI, a
  harness hook, a session-open hook, or a tool's own guard at the call) and
  whether it **blocks** or **warns**. *partial* means the check covers some of
  the rule and the rest is unguarded.
- **directive-only**: nothing mechanical sees a breach. Where a self-run
  instrument would report it if a session chose to run it, the row says
  *instrument* and the state stays directive-only.
- **unenforceable, accepted**: the fact that would license or condemn the act
  is outside any check's evidence window (`GUARDS.md` § *Before building a
  check: the evidence window*), or the house has recorded a decision not to
  build the check. None of the 68 rules here is accepted (see *Doubts*).

A directive-only rule also gets the place its breach could be seen, as in
slices 1 to 5: **diff** (the committed change itself), **record** (only by
joining records outside one diff) or **invisible** (nothing in the tree or the
repo's records).

## Method, and what it did not do

1. Read in full, at commit `0cc8aa35` (the commit the worktree was cut from):
   `docs/build/README.md`, `docs/build/REPO-BOUNDARY.md`,
   `docs/build/REPO-STANDARD.md`, the root `CLAUDE.md`, `SECURITY.md` and
   `README.md`, and all 24 tracked files under `docs/build/templates/`: the
   child `CLAUDE.md`, `CONTRIBUTING.md`, `SECURITY.md`, `README.md`,
   `CHANGELOG.md`, `NOTICE`, `LICENSE`, `gitignore`, `claude/settings.json`
   and `settings.local.json`, the three workflows, `tools/check_links.py` and
   the `docs/` set (ARCHITECTURE, ECONOMICS, ROADMAP and its store, decisions,
   reviews, sessions).
2. A rule is a sentence that tells a future agent to do or not do something.
   Not counted: grounding stories and cases; dated status notes; the *Still
   owed* list in `docs/build/README.md`; the splitting section's account of how
   two splits went and what could not be grounded; descriptions of what a
   template contains; and in the templates the verbatim Apache-2.0 text of
   `LICENSE`, the placeholder lines of `NOTICE`, `CHANGELOG.md` and `README.md`,
   the seed allowlist's command list, and `settings.local.json`'s one key.
   Those state no rule of their own. The seed allowlist is a design question,
   not a rule (see *Doubts*).
3. **Templates: only the rules the templates state to adopters are counted.**
   The stamped doctrine block in the child `CLAUDE.md` is word for word the
   floor region of `PROPAGATION.md`, which slice 2 counted once (`PRO3`). It
   folds there, and its tests are cited where a row leans on them.
4. **Cross-slice folds.** A rule these files restate from a censused document
   is not counted again. Folded here:
   - `docs/build/README.md`: "points up to `method/` rather than copying it, a
     second copy drifts" into `EVI9` and `PRO15`. The file counts no rule.
   - `REPO-BOUNDARY.md`: never reshape a repo you do not own, counted once at
     `RST30`; "apply `REPO-STANDARD.md` in full, sized to type" into `RST2`;
     the publish-is-a-floor-action note into `AUT2`. In the splitting section:
     one home per fact, one direction of flow, never fork, a change made
     upstream into `EVI9` and `PRO15`; build the guard first and prove it
     fails, a guard that skips silently when its data is absent is the defect,
     into `EVI21`, `EVI19` and `GRD10`; migrate in measured stages, a moved
     result stops the stage, into `PRI63`; every temporary bridge gets a dated
     delete-item into `PRI30`; cold reviews at stage boundaries into `REV39`;
     the list of what the principal had to correct restates items already
     counted (`BND7` to `BND9`) and counts no row.
   - `REPO-STANDARD.md`: "grounded, not invented" into `APX2`, `APX15` and
     `REC3`; "points up, never re-states method" into `EVI9` and `PRO15`;
     comments say why into `REC4`; ADR and review-record names
     `<date>-<HHMM>-<slug>`, `HHMM` in UTC, retired-scheme names kept, into
     `CON23`, `REC7`, `CNV6` and `REV28`; when to write an ADR and when not into
     `REC17`; the review brief's lifecycle and the deferred sibling into
     `REV3`; the repo ECONOMICS file carrying only what is repo-local into
     `PRO15` and `ECO32`; `.claude/settings.json` never committed, uniform
     rather than visibility-conditional, into `TLB9`; the stamped doctrine
     block and the pin into `PRO2`, `PRO3` and `PRO5`; the signing bake into
     `SGN4`; delete-branch-on-merge into `CON53`; commit and push proceed into
     `AUT1`; publishing is always a floor action into `AUT2`; ask only when
     genuinely ambiguous into `EVI17`; the stated-exception grammar into
     `PRI56`; the `.atelier-floor.json` layering (a shared floor, a local
     append, narrow never contradict, a dated advisory's `kind`) into `PRO41`,
     `PRO12`, `GRD17`, `GRD20` and `GRD22`; the `visibility` key checked against
     GitHub, the one red, into `AUT3` and `AUT2`; the roadmap item flip into
     `REC23` and the generated, never hand-edited index into `REC22`;
     "history keeps what a push published" into `REC24`'s class and `AUT2`.
   - Templates: the read order's recovery sweep and the cold-reviewer skip into
     `CON57` and `REV11`; the child floor workflow naming no scanner, every
     push, and cancelling superseded runs into `PRO41`, `ECO11`, `ECO14` and
     `ECO16`; the Linux-by-default runner into `ECO13`; the false-positive
     hatches into `GRD13` and `GRD15`; an advisory's reason, `review-by` and
     `kind`, and the fleet-board red on a passed date, into `GRD20`, `GRD17`
     and `GRD18`; the dated bar on advising or disabling `sizescan` into
     `GRD21`; a reason on a narrowed unsoftenable check into `GRD22`;
     `sign-boundary` into `SGN13`; the good-change list into `CNV8`, `REC4`,
     `REC17`, `REC7`, `CON48`, `APX2` and `REV39`; the whole child
     `ECONOMICS.md` into `ECO1`, `ECO2`, `ECO3`, `ECO5`, `ECO9`, `ECO19`,
     `ECO21`, `ECO23`, `ECO25`, `ECO26` and `ECO30`; the roadmap legend's
     states, claim line and `[x]` flip into `REC22`, `REC23`, `CON28`, `CON33`
     and `CON34`, its queued-review rule into `REV15`, and its design-item
     review line into `REV41` and `REV42`; the reviews README as a stamped,
     narrowing-free pointer into `PRO50` (this file is further evidence for
     `PRO50`: `ReviewsTemplateTest` pins it, and its own comment says
     `stampscan` does not compare it); the deferred sibling into `REV3`; the
     decisions README's acceptance and append-only lifecycle into `REC18` and
     `REC19`; the sessions README into `REC7` and `REC5`; `LICENSE` and
     `NOTICE` into `RST9` and `RST10`; the `gitignore` into `RST14`.
   - Root `CLAUDE.md`: the sync, autostash and worktree reads into `CON18`,
     `CON4`, `CON11` and `CON14`; the board index rebuild into `REC22`; the
     hand-up PR read into `PRO37`; the personal-data constraint into `RST21`
     to `RST25` and `DAT6`; "live the doctrine" and "ground everything" into
     `APX1`, `APX2`, `APX15` and `REC3`; "report your problems, atelier is not
     exempt", the evidence mark, no silent workaround, and the class-only
     rule for a private reporter into `PRO17`, `PRO18`, `PRO19` and `PRO27`;
     the standing grant into `AUT1`; the repo's visibility statement into
     `AUT3`; conventions and the session file into `CNV4`, `CNV6`, `CNV8`,
     `REC7` and `CON23`.
   - `SECURITY.md`: the severity and recurrence-prevention step on a confirmed
     fix into `REV25`; the private route and the honest response promise into
     `RST12` and `RST13`; "takes no third-party dependencies" into `PRI8` (and
     a defect, below); "pins the actions it uses" into `TPL8`; scanner fixes
     arriving at floating `main` and doctrine fixes at a pin bump into `TPL6`
     and `PRO5`.
   - `README.md`: no personal data beyond the closed list into `RST21` to
     `RST25`; a public announcement staying the principal's call into `RCL2`;
     the fail-closed hook into `RDM2`; the plugin carrying no version
     (the SHA is the version, ADR 0002) is a description and counts no row.
5. Listed every check that could see a breach: the floor registry (21 entries
   by `tools/floor.py`, the 19 hook-plane checks and the two commit-message
   checks), both atelier workflows and the three template workflows, the tests
   that pin the templates (`tools/test_templates.py`,
   `tools/test_personal_data.py`, `tools/test_floor.py`,
   `tools/test_precommit.py`, `tools/test_pathscan.py`), the harness and
   session-open hooks, and the instruments' tests and `man` lint.
6. Before writing *enforced* against a rule, read the code and cite the
   function or the test. Before writing *directive-only*, looked for the
   check by name and by the phrase the rule uses in `tools/`, `instruments/`,
   `.github/`, `skills/`, `commands/` and `docs/build/templates/`.
7. Measured, where a measurement says whether a candidate guard would fire on
   the live tree (figures are in the rows and the candidates). Counts are from
   this worktree's tracked files at the commit above, by grep and small
   scripts, not by a scanner, with these exceptions: `indexscan` and the three
   `--help` reads were run (the first over a scratch copy of `docs/build/` with
   a declaration added; nothing in the tree was changed), and two GitHub
   settings were read with `gh api` (GET only).
8. Did not read `docs/SESSIONS.md` or the contents of `docs/sessions/`; file
   names there were listed once, for a measurement.

## docs/build/README.md

No rule. It is an index of the layer, a description of what the templates
carry and a dated status list. Its one directive, that the layer points up and
never copies, folds (method 4). Its content is wrong in three places, named in
*Doctrine defects*. It has no row table.

## REPO-BOUNDARY.md

The file's last section is, by its own header, a draft of what could be
grounded and no more: "a checklist to test against the next split, not a
settled method". Its eleven numbered items are counted as the rules they read
as, five of them folded (method 4), and the doc's own status is carried in
`BND6` to `BND11`'s "draft" note.

| Id | Rule (section) | State | Guard, or where a breach shows |
| --- | --- | --- | --- |
| BND1 | Advise proactively: when a new piece of work appears, say which boundary it wants and why, before scaffolding anything and without being asked (*Standing behaviour*) | directive-only | record: the transcript shows whether a boundary was named before the scaffold, readable by `cctranscript`. Nothing reads the order. The scaffold act (`git init`, `gh repo create`) is in a Bash call's command text, which no hook reads for this |
| BND2 | Run the five discriminators (visibility or audience, release cadence, ownership or access, reuse, blast radius or lifecycle); the strongest usually decides; prefer the smallest boundary that satisfies those that fire; if none fire it is not a repo, and a thing with no independent clock is a component, not a minted repo (*The test*, *The three shapes*) | directive-only | invisible: the answers to the five questions are written nowhere, and the decision leaves only its outcome (a repo or a folder) |
| BND3 | A monorepo folder is justified by a shared operational surface (one CI, one doctrine block, one access boundary) over pieces individually meaningful, each folder keeping product-in-a-subfolder; a folder that wants to go public or ship on its own clock has outgrown it and splits; the accidental monorepo is the trap (*The three shapes*) | directive-only | invisible: `.atelier-floor.json` declares one `visibility` per repo, so a mixed-visibility folder is unreadable by the floor, and `publishscan` reads paths, not intent |
| BND4 | When the discriminators are balanced, prefer the reversible direction: start as a component or monorepo folder and split when a discriminator actually fires; do not pre-split for a hypothetical reuse or a hypothetical public release (*When it's genuinely ambiguous*) | directive-only | invisible: a pre-split is a new repo, and the speculation is not recorded |
| BND5 | When a discriminator does fire, split promptly, since the cheapness of splitting decays as a folder gathers references, its own CI and a doctrine block; deferring a fired discriminator is how the accidental monorepo forms (*When it's genuinely ambiguous*) | directive-only | record: a board item that defers a split, if one exists; invisible otherwise |
| BND6 | State the bar and the capability list before the first move of a split: what it must achieve and what the new home must be able to do (*Splitting*, 1; draft) | directive-only | record: the split's board item or hand-off, where it exists. The doc says the bar and list were never itemised, so there is no shape to read |
| BND7 | Put a four-line routing test in every onramp a session on either side of a split reads, the user-level one too when one side may not name the other: came from the private side so it goes private; generic and written with synthetic examples so it goes public; both so split it and never carry the motive across; unsure goes private (*Splitting*, 2; draft) | directive-only | diff for atelier's own onramp: its `CLAUDE.md` carries no routing test, and atelier is on neither side of a split, so none is owed. Invisible for a child's onramp and for the user-level one (outside every tree) |
| BND8 | Records never cross a split, however well cleaned: session logs, history, board items and decisions stay with the side that made them (*Splitting*, 3; draft) | directive-only | record: a record file whose content was made on the other side. `namescan` and `leakscan` read a name or a listed term, never provenance, so a copied record with no listed term passes |
| BND9 | Judge a leak by meaning; keywords back it up: the gate's first layer is a read for meaning attested by hash, with token lists as a backstop only (*Splitting*, 6; draft) | directive-only | diff, judgement: a gate whose only layer is a token list. `leakscan` is shape plus a machine-local term list by design (`ACC9`), so it is the backstop layer the rule names; no meaning layer exists in the tree to be breached |
| BND10 | Rename refuse-first, with a script that also copies the assistant memory keyed by path, so the move does not orphan it (*Splitting*, 9; draft) | directive-only | invisible: a rename of a repo directory and a user-level memory path are both outside every tree |
| BND11 | Hand off with a file carrying a "settled, do not re-ask" list, so a fresh session does not reopen a ruling (*Splitting*, 11; draft) | directive-only | record: a hand-off file, where one exists. Whether the list was written at all leaves nothing to read; the doc says the file's fields were not grounded |

## REPO-STANDARD.md

| Id | Rule (section) | State | Guard, or where a breach shows |
| --- | --- | --- | --- |
| RST1 | Product in a subfolder: where a repo has a deployable or product artefact it lives in a subfolder (`site/`, `src/`, `pkg/`), the root holding only meta (README, `docs/`, licence, CI, tools); a strong default whose honest exceptions are the sizing table's two (an infra repo is its config tree; a docs repo's content may live at root), and any other departure needs a stated reason (*The default that binds*; the stated-exception grammar is `PRI56`, folded) | directive-only | diff, judgement: "product" is declared nowhere (`.atelier-floor.json` names records, licence and visibility, and `roots.pathscan` names source roots only for path resolution), so no check can say what sits at the wrong level. Measured on atelier: no product tree; `tools/`, `instruments/`, `skills/`, `commands/` and `.claude-plugin/` sit at the root as the shipped surface |
| RST2 | Decide the repo's type first (static site, package, infra, docs) and apply the matching set, sized to it: a five-file site needs no ADR directory on day one, an infra repo's CI may honestly be a config linter and nothing more; sizing is a judgement, not a menu (*Size the standard to the repo type*; ask only if genuinely ambiguous is `EVI17`, folded) | directive-only | invisible: the type is declared nowhere, so neither a missing nor an extra file can be read against it. Measured: atelier declares no type (see *Doubts*) |
| RST3 | Honest CI: `ci.yml` is a real correctness gate sized to the repo; where it cannot cover something it says so in a comment and leaves a documented human step; "nothing at all" is honest only when written down, and an infra repo with no linter states a no-gate note, never a silent absence (*Size the standard*, *ci.yml*) | directive-only | diff, judgement: a green step that cannot fail is a readable shape (`continue-on-error: true`, `\|\| true`). Measured: 0 hits in the 5 workflow files; two `exit 0` lines in the reusable floor, each printing `::warning::` first. The templates' honesty is pinned only for the floor ones (`ChildFloorWorkflowTest`); the two CI templates carry the comment in prose (`ci-static.yml` names the human-in-a-browser step) with no test |
| RST4 | Seed from `templates/` and fill every placeholder with real, grounded content; a doc that cannot be grounded is a stub with a visible `<!-- TODO -->` that says so, never lorem ipsum or invention; do not churn blindly, since a plausible-but-wrong doc is a regression (*The standard file set*, *Process: standardise*, 3; grounding overlaps `REC3`, `APX15`) | directive-only | diff, in the child's tree: an unfilled `<name>`, `<subfolder>` or `<!-- TODO -->` left in a doc. The stamp tokens are the one class something reads: `pins.py` (instrument, report-only) reads an unfilled `<SHA>` as drift. Nothing reads the rest; the child's tree is out of reach from here, and atelier's own three root files carry none (measured, 0 hits) |
| RST5 | README: public-facing; what it is, why, a structure table, run or setup, develop, licence (*Root*) | directive-only | diff: sections absent from a README. Measured: atelier's root README has a structure table and no Run, Develop or Licence heading (the licence is named under *Sharing*); whether the standard binds a doctrine repo's README is not stated |
| RST6 | CLAUDE.md: the session onramp: a read order (ARCHITECTURE, ROADMAP, the newest few session files), hard constraints, layout, the dev loop, and for a repo inheriting doctrine the stamped block (the block is `PRO2`, folded) (*Root*) | directive-only | diff, judgement. Measured: atelier's root `CLAUDE.md` has a read order, hard constraints and a layout and no dev-loop section; its read order is its own (sync, apex, README, sessions, roadmap, hand-up PRs) and names no ARCHITECTURE |
| RST7 | CONTRIBUTING.md: dev setup, what makes a good change, and the two record disciplines, pointing a human contributor at them in repo-local terms (*Root*) | directive-only | diff. Measured: atelier has no `CONTRIBUTING.md`; its wiring steps and good-change rules sit in `CLAUDE.md` and `README.md` |
| RST8 | CHANGELOG.md: Keep-a-Changelog shape, newest first, everything under *Unreleased* until there is a reason to tag; the SHA is the version (ADR 0002 records why) (*Root*) | directive-only | diff, judgement. Measured: atelier's `CHANGELOG.md` states the shape in its header, keeps everything under *Unreleased* and groups by *Added* and *Changed* under a dated heading |
| RST9 | LICENSE: one permissive licence chosen per repo, the house default Apache-2.0 (ADR 0004), the copyright line set to the right holder (*Root*) | enforced, partial (blocks, hook + CI) | `licenscan.py` (registry): a LICENSE present and recognised; every declaration (a `pyproject.toml`, `package.json`, badge) naming the same SPDX licence as LICENSE; a foreign SPDX header in a source file blocks when it is copyleft into permissive. `.atelier-floor.json`'s `licence` is the assertion. Unseen: that the holder line names the right holder, and that the choice is permissive |
| RST10 | NOTICE only if the repo bundles third-party code, listing each component and its licence (*Root*) | directive-only | diff: a vendored component with no NOTICE entry. `licenscan`'s foreign-header check is adjacent and does not read NOTICE. Measured: atelier has no `NOTICE` and bundles no third-party code (a dependency pinned in a manifest is not bundled) |
| RST11 | SECURITY.md is seeded only once the repo is public or about to be: a private repo has no external reporter, so it is a publish-time artefact like LICENSE (*Root*) | directive-only | diff: a `SECURITY.md` in a repo whose `.atelier-floor.json` declares `"visibility": "private"`. The floor reads the declaration for its visibility line and nothing joins it to this file. Not a breach at atelier (public) |
| RST12 | SECURITY.md content: scoped to what the repo ships; the response expectation stated honestly (a solo-maintained repo says best-effort, no guaranteed timeline); no bug bounty claimed that does not exist; points reporters at GitHub Private Vulnerability Reporting (*Root*) | directive-only | diff, judgement: a claim stronger than its evidence (`APX2`'s class). Measured: atelier's `SECURITY.md` says best-effort, no response time, no bounty, and points at the Security tab |
| RST13 | Enabling private vulnerability reporting is part of the same seeding act, and verified with `gh api repos/<owner>/<repo>/private-vulnerability-reporting` reading `enabled: true`; a policy routed through a disabled switch is a broken control (*Root*) | directive-only | record. Instrument: `tools/flipcheck.py` reads the setting as one of five pre-flip platform settings, GET-only and report-only with no failing exit (its docstring), run by the making-public gate and by no hook or CI step; `floor.py` has no read of it. Measured by `gh api` on 2026-11-23: atelier reads `enabled: true` |
| RST14 | .gitignore always ignores OS litter and both Claude settings files, adding language litter per type (*Root*) | enforced, partial (blocks, hook + CI) | The consequence, not the line: `publishscan.py` refuses a tracked `.DS_Store`, `.claude/settings.json` or `.claude/settings.local.json` at any depth (`TLB9`, folded) and the cache directories (`STG8`). A `.gitignore` missing the lines is read by nothing: the first `git add` of the file is what is refused. Measured: atelier's `.gitignore` names both settings paths |
| RST15 | A check a repo adds for itself under `local` in `.atelier-floor.json` may not take a fleet check's name, and one whose script is missing blocks rather than passing quietly (*.atelier-floor.json*) | enforced (blocks, hook + CI) | `floor.py` raises `ConfigError` on a `local.<name>` that collides with a registry name ("the local seam ADDS checks, it never replaces one"), and a declared script that is missing fails closed (`tools/test_floor.py`, `test_declared_but_missing_script_blocks`: exit 1, "fail closed" on stderr) |
| RST16 | `roots.pathscan` in `.atelier-floor.json` declares extra resolution roots, each with a mandatory `why` (*.atelier-floor.json*) | enforced (blocks: a config error) | `pathscan.py` raises `FloorConfigError` for a missing `why` or `paths` ("a declared root nobody can state the point of is one nobody will re-check"). `tools/test_pathscan.py` pins the absolute, escaping and ghost-path refusals; none omits `why`, so the `why` refusal is code with no test (measured by reading the tests) |
| RST17 | The test of where a rule belongs is not how specific it feels: if another repo would want it, it goes upstream to atelier's registry rather than a `local` check (*.atelier-floor.json*) | directive-only | diff: a `local` declaration. Measured: atelier's `.atelier-floor.json` has no `local` key. A child's declarations are not readable from here; `floorfleet` (instrument) lists them |
| RST18 | ARCHITECTURE.md is compact current truth, the stack and why; deliberation compresses away and the ADRs keep it (*docs/*) | directive-only | diff, judgement. Measured: atelier has no `docs/ARCHITECTURE.md`; the same facts sit across `README.md`, `docs/method/` and ADRs, and the doc says the set is present "to the degree the type earns" |
| RST19 | The board is a record store: `roadmap/<NNN>-<section>/<NNN>-<slug>.md`, each section with a README, `roadmap/README.md` carrying the legend, `ROADMAP.md` the generated index (the form and the never-hand-edit are `REC22`, folded); a done item stays in its own file as `[x]` with no archive file; a repo with no `docs/roadmap/` gets the store form from the template; a repo on the retired one-file board is converted by the health sweep (`skills/fleet-sweep`, healthy item 6), never retyped or hand-edited into shape; a frozen `ROADMAP-DONE.md` is cut by `tools/archivecut.py`; an existing board's items are never overwritten by the template (*docs/*, *Process: standardise*, 3) | enforced, partial (blocks, hook + CI) | `sizescan` blocks a board kept as a flat running log (its cold-content gate, `GRD16`, `GRD21`) and the `board` check blocks a stale index. The route (by sweep and by `archivecut`, never by hand) and "never overwritten" are unread |
| RST20 | The session log is a folder: one file per session named `<date>-<HHMM>-<slug>.md` for its start in UTC (`REC7`, `CON23`, `CNV6`, folded), the folder the index so no file lists it, its README explaining the folder, the newest few read at open and the session's own file written before finishing; a repo still keeping the retired one-file index (`SESSIONS.md`, with any `SESSIONS-ARCHIVE.md`) has it retired by `tools/archivecut.py --cut`, never by hand (*docs/*) | directive-only | diff: a recreated `docs/SESSIONS.md` or a hand-edited index in a repo that has `docs/sessions/`. Measured: atelier has neither file. The template side is pinned (`TemplateBoardTest.test_session_log_template_is_the_folder_form` asserts no `SESSIONS.md` in the template set and the README equals `archivecut`'s header); no check reads a child's tree |
| RST21 | Personal data: the default in every repo is to avoid it: real people's names, contact details and addresses; health, family and financial detail; any identifier that points at one person, such as an account name (*Repo-craft conventions*, *The default, in every repo*) | enforced, partial (blocks, hook + CI) | `leakscan.py` structural rules block the shapes (`email`, `nz-phone`, `nz-address`, `nz-bank-account`, `nz-ird`, `payment-card`, `iban`, `coordinates`, `pii-key-context`) and, on the hook plane only, the machine-local term list. A person described in paraphrase passes, as the doc says; a name nobody listed passes. `RST25` and `RST28` read the account-name class for a repo that declares public. `DAT6` is the third-party-data neighbour (folded) |
| RST22 | Estate detail (hostnames, topology, machine-local paths, client names) is not PII, but the same default and the same recording apply, and a public repo holds none (*The default*) | enforced, partial (blocks, hook + CI) | `leakscan.py` structural rules `ipv4`, `ipv6` and `mac-address` (hook and CI) and the local term list (hook only: `--require-terms` is on the hook plane's template, and CI is structural-only by design). `ACC9`'s reading holds: shape and listed terms, never purpose. Unseen: topology in prose, a hostname or client name not in the list |
| RST23 | The purpose test: an exception stands only if the work the repo was ordered for cannot be done or understood without that very datum, and the record names the work; a purpose a placeholder, a role or an invented example would serve equally fails; "useful", "harmless" and "public elsewhere" are not purposes (*The purpose test*) | enforced, partial (blocks, CI test; atelier only) | `tools/test_personal_data.py:test_every_entry_says_why_and_how_granted_and_where` fails an entry with no `Why held`. Whether the stated purpose passes: nothing reads it (`pdlistscan.py`'s docstring: it "checks where, never whether the reason is good") |
| RST24 | Who grants: in a public repo only the principal, in his own words, and the list is closed until he adds to it; a session that thinks one is needed stops and asks and never adds an entry itself; in a private repo the principal's order is the grant, and the session records what the work needs, marks it as its own call and not a ruling, and asks when unsure (*Who grants one*) | enforced, partial (blocks, CI test; warns for a public child until 2027-03-08) | `test_personal_data.py:test_list_is_closed` pins the set of entry ids (`EXPECTED_IDS`) and says to update it only on his grant; `ClaimWordingTest.test_standard_says_who_grants_in_a_public_repo` pins this very wording ("In a public repo only the principal grants", "in his own words"). A session editing the test and the list together passes both: the test names the grant but cannot read one. `pdlistscan.py` (registry; `unlisted-marker`, `unlisted-holder`) reaches a child that declares public, warning until `PERSONAL_DATA_WARN_UNTIL`. The private-repo half (own call, not ruling) is unread |
| RST25 | Where it is recorded: one list per repo, `docs/PERSONAL-DATA.md`, each entry giving the data, why it is held, how it was granted and the narrowest set of files it may stand in; a repo with no such file holds no exceptions; a test keeps it matching the tree (*Where it is recorded*) | enforced, partial (blocks, CI test + registry) | `test_personal_data.py` (`RegisterMatchesTreeTest`: every holder of a listed string is a named place, every named place still holds it, personal-data markers stand only in named places); `pdlistscan.py` `no-list` for a repo declaring public (warning until 2027-03-08, then blocking). "Narrowest" is unread: `PD1`'s place list names `docs/roadmap/**` and the other record stores, which is as wide as the stores |
| RST26 | An exception with no entry is a breach to fix, not a line to document around: remove it, or ask the principal for a grant; in a public repo history keeps what a push published, so tell him (*Found unrecorded*) | directive-only | record: the finding is read (`RST25`) but the response is not; whether the session removed it, asked, or told him is in its report only |
| RST27 | When a private repo widens: read its list first; each entry the new audience would see needs the principal's word again, and history holds what HEAD no longer shows; widening stays a floor action (`AUT2`, folded) (*When a private repo widens*) | directive-only | record: the flip's confirmation record. Instrument: `publishscan --history` reads history for paths (`AUT5`), not for list entries |
| RST28 | A marker records that someone judged a line; it is not a grant, and in a public repo it needs one (*What the scans do and do not do*) | enforced, partial (blocks, CI test; warns for a public child until 2027-03-08) | `test_personal_data.py:test_personal_data_markers_stand_only_in_named_places` and `pdlistscan.py` `unlisted-marker`, over the eleven personal-data scopes (`PERSONAL_SCOPES`). An unscoped marker (which exempts every structural rule) is left to `leakscan`'s judgement, as the docstring says |
| RST29 | A new repo's remote is created private; the authority to create it is the principal's ask for a repo with a remote, not "push is recoverable"; if the ask did not clearly include a remote (standardising an existing repo, a local experiment), confirm before creating one (*Process: a new repo*, 5; publishing is `AUT2`, folded) | directive-only | invisible, before-plane reachable: `gh repo create` is in the command text a `PreToolUse` hook is handed, and no hook reads it (`modelguard` reads the model flag, `secretguard` printing verbs). After the act, `check_visibility` reds only a repo declared private that GitHub says is public |
| RST30 | Do not standardise a third-party repo: check the remote's owner before touching anything; a repo under someone else's organisation is not yours to reshape (*Repo-craft conventions*; `REPO-BOUNDARY.md`'s ownership discriminator points here) | directive-only | invisible, before-plane reachable: the owner is in `git remote -v`; no hook reads it. Instrument: `ccclose` lists the other repos a session touched, which shows the touch after the fact |
| RST31 | An installed CLI ships both `--help` and a man page, which do different jobs; a repo-internal script that runs in place owes a good `--help` only (the scope: a tool the repo installs onto an operator's machine, published to `PATH` and used away from the repo) (*Repo-craft conventions*) | enforced, partial (blocks, CI) | `ci.yml` step *man page lint* runs `mandoc -T lint` over every `instruments/man/*.1`, and per-instrument tests pin a page's existence and shape (`ccarchive`, `ccclose`, `ccrepo`, `cctranscript` in the `*.test.js` files; `ccapple`, `ccfleet` in `test_*.py`). Measured on 2026-11-23: of the 10 CLIs `instruments/install` links onto `PATH`, 9 have a page and `ccstatusline` has `--help` and no page; three pages (`cclive`, `ccmail`, `ccopen`) are pinned by no test. Nothing ties the installer's tool set to the page set |
| RST32 | `--help` is the digest: concise and scannable, fits a screen, a one-line synopsis, the options as a flat list, at most a closing line or two with the pointer to `man <tool>`; it is not where rationale or worked examples belong (*Repo-craft conventions*) | enforced, partial (blocks, CI test) | A one-screen budget is pinned for four tools, each its own number: `ccarchive` 22 lines (`instruments/ccarchive.test.js`), `cctranscript` and `ccclose` 24, `ccrepo` 47 (`HELP_LINE_BUDGET`, "grounded"). "Fits a screen" has no stated number. Measured by running `--help`: 9 tools print 21 to 46 lines (`ccrepo` 46, `ccmail` 36, `ccfleet` 29), and `ccmail` and `ccfleet` are pinned by no budget. Content (no rationale) is unread |
| RST33 | The man page is the full reference: what the tool is and why, every option explained, and the sections a digest cannot carry (`FILES`, `EXAMPLES`, `EXIT STATUS`, `NOTES`, `SEE ALSO`), in plain language (*Repo-craft conventions*) | enforced, partial (blocks, CI test) | `mandoc -T lint` reads roff form for every page (`ci.yml`). `instruments/ccarchive.test.js` asserts a `.TH` line and six sections (NAME, SYNOPSIS, DESCRIPTION, OPTIONS, EXAMPLES, SEE ALSO), not `FILES`, `EXIT STATUS` or `NOTES`. The other pinned tools assert existence. "Plain language" and "why" are unread |
| RST34 | Keep prose detail in one place, the page, and where the repo has tests pin the superset relation mechanically: every flag `--help` prints appears in the page; the doc adds that "atelier's `instruments/` tests do" (*Repo-craft conventions*) | enforced, partial (blocks, CI test) | Pinned for 2 of the 10 tools: `instruments/test_ccfleet.py` and `instruments/test_ccapple.py` ("flags in --help but absent from man/..."). Measured by a script over the nine pages: 0 flags missing in any page, so the relation holds without a pin for seven tools. The doc's "tests do" overclaims: 2 of 10 (a doctrine defect, below) |
| RST35 | Ship pages as roff under `man/` and have the installer publish them to `~/.local/share/man/man1`, which macOS and BSD `man` and man-db derive from `PATH`; a hard-set `MANPATH` overrides that (*Repo-craft conventions*) | directive-only | invisible: a construction, not a check. `instruments/install` globs `man/*.1` and links each, so a page placed there is published; nothing reads that a tool's page was placed there (`RST31`) |
| RST36 | New repo: `git init` and set the git identity (instance-local) (*Process: a new repo*, 1; the signing bake is `SGN4`, folded) | directive-only | record: git config, outside the tree. Measured: 299 of atelier's last 300 commits carry one author name and address; the 300th carries the same address with a shorter name. No check reads author identity (`signscan` reads the signing key; `namescan` and `quotescan` read messages) |
| RST37 | Standardise an existing repo: audit first against the file set, what is present, missing and wrong (*Process: standardise*, 1) | directive-only | invisible: an audit's result is a message. `skills/fleet-sweep` performs one per repo (a later slice) |
| RST38 | Apply the safe mechanical bits uniformly: `.gitignore` hygiene, and `git rm --cached` any committed OS litter or either `.claude/` settings file (the old step said to commit the allowlist, and the sentence outlived the ruling once) (*Process: standardise*, 2) | enforced, partial (blocks, hook + CI) | The state, not the act: `publishscan` refuses a tracked litter or settings file (`TLB9`, `STG8`, folded). That the act is done uniformly across a fleet: `floorfleet` (instrument) |

## Templates (docs/build/templates/)

Only rules the templates state to adopters, as asked; boilerplate and
placeholders carry none (method 2).

| Id | Rule (file, section) | State | Guard, or where a breach shows |
| --- | --- | --- | --- |
| TPL1 | The four stamp tokens (`<atelier-path>`, `<SHA>`, `<visibility fact>`, `<visibility check>`) appear in the template set only in the (file, token) pairs create-repo's stamp step fills; a new token means changing the fill step and the inventory together (`CLAUDE.md` header; the test docstring) | enforced (blocks, CI test) | `tools/test_templates.py:TemplateSetPlaceholderInventoryTest` (the exact pair set, set-wide); `TemplateBlockSyncTest.test_block_carries_exactly_the_four_placeholders` and `test_prose_placeholder_count_matches_block` for the `CLAUDE.md` side. Unread: the fill step itself (skill text) and any non-stamp placeholder (`<name>`, `<subfolder>`) |
| TPL2 | No template names a model tier; seats only, and which model fills a seat stays person-local (child `ECONOMICS.md`) | enforced (blocks, CI test) | `tools/test_templates.py:TemplateSetNamesNoModelTest` walks every file under `templates/` for the tier names and `claude-<n>` ids, trailer lines excepted. `ECO32` is its method-doc neighbour (folded) |
| TPL3 | Hooks and `hooks.atelierTools` do not travel: before the first commit on any new clone or machine, set `core.hooksPath .githooks` and `hooks.atelierTools`; a fresh clone commits unscanned until then (child `CLAUDE.md` *Hard constraints*; `CONTRIBUTING.md` *Development setup*) | enforced, partial (blocks at the hook once wired; CI backstop) | Wired: `.githooks/pre-commit` blocks when `floor.py` is missing under the resolved tools directory (`tools/test_precommit.py` pins it with real commits). Unwired: the hook never runs and nothing in the clone says so; CI re-runs the floor over the pushed tree (`floor.yml`), which catches content and not the missing wiring, and the hook's header names `floorfleet` (instrument) as what catches a clone that never ran it |
| TPL4 | Once per machine, copy `leakscan-terms.example.txt` to `~/.claude/leakscan-terms.txt` and fill it in; without it the first commit blocks, deliberately (`CONTRIBUTING.md`) | enforced (blocks, hook) | `tools/floor.py`'s `leakscan` entry passes `--require-terms` on the hook plane and not on CI; `leakscan.py` exits 2 without a term list. CI is structural-only by design and says so. That the list is *filled in* with real terms is unread |
| TPL5 | Prove it landed: `git config --get core.hooksPath` must print `.githooks`, and `floor.py --list --plane hook` must print the checks, since the second alone does not prove git will invoke the hook (`CONTRIBUTING.md`) | directive-only | record: the transcript. `ContributingTemplateTest.test_the_prove_it_command_proves_git_will_invoke_the_hook` pins that the template tells the reader to run both; nothing sees them run |
| TPL6 | A child's floor workflow is a thin caller that floats at `@main` by default, since the newest scanner is safest; a deliberate pin is two edits, the `uses:` ref and `with: atelier-ref:` set to the same SHA, because pinning `uses:` alone freezes the transport and still runs the registry from atelier's tip (`workflows/floor.yml`; `SECURITY.md`'s uptake paragraph; the "names no scanner" half is `PRO41`, folded) | enforced (blocks, CI test) | `ChildFloorWorkflowTest`: `test_calls_main_not_a_pinned_sha`, `test_a_deliberate_pin_is_documented_as_two_edits` (`atelier-ref` and "two edits" in the text), `test_calls_ateliers_reusable_floor`, `test_names_no_scanner`. A child that pins `uses:` alone and ignores the comment: unread from here (`floorfleet`, instrument, reads children) |
| TPL7 | A workflow declares least privilege, `permissions: contents: read` (`workflows/floor.yml`; `ci.yml`) | enforced, partial (blocks, CI test) | `ChildFloorWorkflowTest.test_least_privilege` and `ReusableFloorWorkflowTest.test_least_privilege` pin the two floor workflows; atelier's `ci.yml` declares it (no test pins it). The two CI templates, `ci-python.yml` and `ci-static.yml`, declare none: 2 of 5 workflow files measured, so a child seeded from them takes the repository's default token permissions |
| TPL8 | Third-party actions are SHA-pinned and not tag-pinned, since a movable tag can ship new code into a trusted build; the trailing tag is the label, bump both together and re-resolve the SHA (`workflows/ci-python.yml`, `ci-static.yml`; `ci.yml`; `SECURITY.md` says the repo pins what it uses) | directive-only | diff: a `uses:` whose ref is not 40 hex. Measured: 11 `uses:` lines across the 5 workflow files, 10 pinned, the 11th the deliberate floating first-party call (`TPL6`). No scanner reads workflows; `tools/README.md` *Supply chain* is the stated home. The templates' pins lag atelier's own (`checkout` v4 against v5, `setup-python` v5 against v6) and nothing reads that either |
| TPL9 | A decision record carries Status, Date, Review, Context, Decision, Rejected and Consequences; Review is a stated judgement (a queued pointer or `not warranted`, grounds); Draft is the only mutable state (`docs/decisions/README.md`, `template.md`; acceptance and append-only are `REC18`, `REC19`, folded) | enforced, partial (blocks, hook + CI) | `reviewscan.py:scan_record` blocks a dated record with no review line (`REV41`, folded). The other six section names are unread. Measured by a heading-or-label read: of the 8 records dated from 2026-07-21 (where `reviewscan` starts), 5 name all seven; 3 do not (a draft with no *Rejected*; two design proposals under their own section shapes) |
| TPL10 | A review brief carries Subject, Type, Scope, Load-bearing assumptions to challenge, Grounding, Non-goals, and the `Board` and `Status` header lines (`docs/reviews/README.md`, *Format*; the scope rule is `REV21`, folded) | enforced, partial (warns, hook + CI) | `reviewscan.py:header_warnings` warns on a new file lacking `**Board:**` or `**Status:**` (`REV33`, folded). The six body fields are unread. Measured by a crude read: 40 of 262 dated review files carry no "load-bearing" wording at all |
| TPL11 | Fill the placeholders and delete the guidance comments as you go (`CLAUDE.md` and `SECURITY.md` headers) | directive-only | diff, in a child's tree: a leftover `<!-- ... -->` guidance block or `<name>` in a root file. Nothing reads a child's tree; atelier's three root files carry none (measured, 0 hits). Overlaps `RST4` |
| TPL12 | Commit messages: `area: imperative subject`, a why-dense body and a Co-Authored-By trailer (child `CLAUDE.md` *Conventions*; root `CLAUDE.md` *Conventions*, counted here) | directive-only | diff, the message. Measured over atelier's last 300 commits: 299 carry an `area: ` subject, 300 the trailer, 38 have no body beyond the trailer. The commit-message plane runs `namescan` and `quotescan` only, which read names and quotations, never shape |

## Root CLAUDE.md

| Id | Rule (section) | State | Guard, or where a breach shows |
| --- | --- | --- | --- |
| RCL1 | The read order at session start: sync first (folded), then the apex, the README, the newest few session files (with the recovery sweep and the cold-reviewer skip, folded), the generated `ROADMAP.md`, and the open hand-up PRs, whose landing is the first act of a session that finds one; the rest of `docs/method/` is read on demand (*Read order at session start*) | directive-only | record: the transcript. Instrument: `ccopen` runs the reads as code, and its design note says the reads "are today prose" a session can skip silently; it is self-run from the session-open prompt, and nothing invokes it |
| RCL2 | The making-public floor is spent; the next deliberate widening, a public announcement, a published package or a plugin/skills bundle, stays the principal's call and never the agent's initiative (*Autonomy in this repo*; `README.md` says the same of the announcement) | directive-only | invisible, before-plane reachable: a publish (`gh release create`, `npm publish`, `twine upload`) is in the command text a hook is handed, and none reads it. `check_visibility` reads only the repo's visibility, which a package publish does not change. The sentence is also stale (see the defects) |
| RCL3 | Commits are made under the configured git identity, the repo's published author name and address (*Conventions*) | directive-only | diff, the commit's author header. Measured: 299 of the last 300 carry it exactly (see `RST36`); no check reads author identity |

## SECURITY.md

| Id | Rule (section) | State | Guard, or where a breach shows |
| --- | --- | --- | --- |
| SPL1 | A flaw in what the repo ships is in scope and handled as a vulnerability: a scanner in `tools/` that fails to catch what it claims to (a false negative, or one induced to pass unsafe content), a template that ships an insecure default into every repo that copies it (an over-permissive workflow permission, an unpinned action, a leaky `.gitignore`), and doctrine that followed as written leads an adopter into an unsafe practice (*Scope*, in scope) | directive-only | invisible: a report arrives privately and leaves no trace in the tree until a fix lands. Each class has a partial reader (`TPL7`, `TPL8` for the template class) |
| SPL2 | Out of scope: an adopter's own estate and wiring, third-party actions and toolchain (report upstream), and the documented limits of the scanners: a report that a scanner misses a class it already declares out of reach is a documentation pointer, not a vulnerability (*Scope*, out of scope) | directive-only | record: the report's disposition. Each tool's stated limits sit in `tools/README.md` and the tool's docstring; nothing reads that a report was routed by them |

## README.md

| Id | Rule (section) | State | Guard, or where a breach shows |
| --- | --- | --- | --- |
| RDM1 | Adopting: you become the principal; read the worked example for its shape and instantiate it as yourself, with your own personal context, estate and decisions; the doctrine in `docs/method/` is the general part meant to travel (*If you're adopting this*; repeated at the end of *Install as a Claude Code plugin*) | directive-only | invisible: an adopter's act, outside every tree here. The mechanism it names is `create-repo`'s instance profile (`~/.atelier/instance.yaml`, never committed) |
| RDM2 | After a plugin update, re-run `/atelier:install-hook` in a repo hooked from a GitHub install: the hook's scanner path is pinned to the installed plugin version, and until then the hook blocks and never waves through (*Install*) | enforced, partial (blocks, hook) | The fail-closed half: `tools/pre-commit.sample` (and `.githooks/pre-commit`) block when `floor.py` is not found under the resolved tools directory, pinned by `tools/test_precommit.py` with real commits. The re-run is unread, and an old plugin version directory that still resolves would run older checks silently: unverified from here |

## Directive-only rules, grouped by where a breach shows

**Diff-visible (19).** BND7, BND9; RST1, RST3, RST4, RST5, RST6, RST7, RST8,
RST10, RST11, RST12, RST17, RST18, RST20; TPL8, TPL11, TPL12; RCL3. Seven name a
shape a scanner could read from the added lines: TPL8 (a `uses:` ref that is not
a SHA), TPL12 (a subject with no `area:` and a missing trailer), TPL11 (a
leftover template placeholder), RST3 (a step that cannot fail), RST5 (a README
missing named sections), RST11 (a `SECURITY.md` in a repo declared private) and
RST20 (a recreated `SESSIONS.md`). The rest are judgement over what a document
should contain.

**Record-visible (12).** BND1, BND5, BND6, BND8, BND11; RST13, RST26, RST27,
RST36; TPL5; RCL1; SPL2. Four rest on a record the doctrine keeps off this repo
(BND6, BND8, BND11 in the split's own records; RST36 in git config).

**Invisible (12).** BND2, BND3, BND4, BND10; RST2, RST29, RST30, RST35, RST37;
RCL2; SPL1; RDM1. Three are before-plane reachable from the command text of a Bash
call (RST29, RST30 and RCL2's publish); none is decidable outright from one
command, as the earlier slices found.

## Counts

| Doc | Rules | enforced (of which partial) | blocks | warns | directive-only | diff | record | invisible | unenforceable, accepted |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| docs/build/README.md | 0 | 0 (0) | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| REPO-BOUNDARY.md | 11 | 0 (0) | 0 | 0 | 11 | 2 | 5 | 4 | 0 |
| REPO-STANDARD.md | 38 | 16 (14) | 16 | 0 | 22 | 13 | 4 | 5 | 0 |
| templates/ | 12 | 8 (4) | 7 | 1 | 4 | 3 | 1 | 0 | 0 |
| root CLAUDE.md | 3 | 0 (0) | 0 | 0 | 3 | 1 | 1 | 1 | 0 |
| SECURITY.md | 2 | 0 (0) | 0 | 0 | 2 | 0 | 1 | 1 | 0 |
| README.md | 2 | 1 (1) | 1 | 0 | 1 | 0 | 0 | 1 | 0 |
| Slice 6 | 68 | 25 (19) | 24 | 1 | 43 | 19 | 12 | 12 | 0 |
| Slice 5 | 73 | 19 (14) | 15 | 4 | 54 | 12 | 15 | 27 | 0 |
| Slice 4 | 106 | 5 (5) | 4 | 1 | 99 | 60 | 9 | 30 | 2 |
| Slice 3 | 94 | 9 (9) | 8 | 1 | 81 | 20 | 7 | 54 | 4 |
| Slice 2 | 129 | 27 (19) | 15 | 12 | 101 | 36 | 23 | 42 | 1 |
| Slice 1 | 158 | 19 (11) | 14 | 5 | 133 | 35 | 33 | 65 | 6 |
| Running total | 628 | 104 (77) | 80 | 24 | 511 | 182 | 99 | 230 | 13 |

As in slices 1 to 5: *diff*, *record* and *invisible* split the directive-only
count, each rule once, under the place a breach first shows. *blocks* includes
the CI test pins (RST24, RST25, TPL1, TPL2, TPL6 and the rest fail the run after
a push) and the tool's own refusal at the call (RST15, RST16). The running total
counts one rule twice, EVIDENCE §17 as `EVI24` and as `CON21`; nothing in this
slice adds a second such pair, so net of it the running total is 627 distinct
rules. The state changes recorded since earlier slices (*Doubts*) are not
applied to the totals: each slice's counts stay as that slice found them.

Reading the table. Slice 6 is the most mixed yet: 25 of 68 rules (37%) have a
check, against 26% for slice 5, and 19 of those 25 cover only part of the rule.
The split is by file, not by topic. `REPO-STANDARD.md` is 16 of 38 enforced
because its two big blocks are things a scanner can read: the personal-data rules
sit under a closed list with a test and a scanner, and the repo-craft block's
`man` rules sit under the instruments' CI. `REPO-BOUNDARY.md` is 0 of 11: it is
advice about a decision (is this a repo), and the decision leaves no artefact
that records why, so the checklist at its foot is as unobservable as the
boundary call above it. The templates are the clearest result of the slice: 8
of 12 are pinned by the template test suite, and the pattern is that a *shape*
(a placeholder inventory, a model name, a workflow that names no scanner) is
pinned and a *practice* a child must follow (SHA-pin an action, write a body, run
the prove-it command) is not. Across the six slices, 17% of the 628 rules have
any mechanical check, and 77 of those 104 cover only part of the rule.

## Top five guard candidates

Directive-only, breach visible in the diff, and costly when it happens:

1. **TPL7 and TPL8, workflow hygiene: pinned actions and declared
   permissions.** A scan of `.github/workflows/*.yml` and
   `docs/build/templates/workflows/*.yml` for two shapes: a non-local `uses:`
   whose ref is not 40 hex (with a reasoned marker for the deliberate floating
   first-party call), and a missing top-level `permissions:` block. It reads
   the two promises `SECURITY.md` makes about this repo and names as in-scope
   template flaws ("an over-permissive workflow permission, an unpinned
   action"), which nothing reads. Measured: 11 `uses:` lines in 5 files, 10
   pinned and the 11th the named exception; `permissions:` absent from 2 of 5
   files (`ci-python.yml`, `ci-static.yml`), so the first run finds two real
   gaps in what every child that seeds a CI workflow copies. Cheap: a line
   regex, no YAML parser, stdlib. It ranks first because the finding ships to
   every child.
2. **CON23 and REC7, record file-name shape.** A new file under
   `docs/decisions/`, `docs/reviews/` or `docs/sessions/` named other than
   `<date>-<HHMM>-<slug>.md`, with the retired schemes (the `000N-` ADRs, the
   dated-only and `-NN-` counter names before 2026-07-15) as a dated
   exemption. It is the rule `REPO-STANDARD.md` and three templates each
   repeat, and `reviewscan`'s name pattern selects files and refuses none
   (`REV28`). Measured: `docs/reviews/` 0 of 262 breach; `docs/decisions/` 1
   of 12 (`2026-11-09-board-states-design.md`, dated after the scheme and with
   no `HHMM`); `docs/sessions/` has 12 names after 2026-07-15 without a time
   segment, some of them in a counter or slug scheme whose end date the
   doctrine does not give, so this slice does not count them as breaches. A
   gated cutoff makes it land with one finding, a real one.
3. **SPL (the dependency claim) and PRI8, a dependency manifest outside a
   declared set.** A check that a tracked `requirements*.txt`,
   `constraints.txt`, `package.json` with dependencies or `pyproject.toml` sits
   only under a path an ADR or a marker names. It would tie
   `SECURITY.md`'s "takes no third-party dependencies" to the tree. Measured: 2
   tracked manifests in 1758 files, both in `instruments/browser-fetch/`,
   which ADR 0006's 2026-07-12 addendum admits; so the check fires once and
   the answer is a reasoned marker citing that addendum. The value is the first
   run: it surfaces that the policy sentence is broader than the ADR (a defect,
   below), and it guards the next instrument that adds a dependency quietly.
4. **docs/build/README.md, a declared index over `templates/`.** An
   `indexscan:maps dir=templates match=*` declaration, with the README's prose
   rewritten to name each entry. Measured on a scratch copy with the
   declaration added: 10 of 12 entries unlisted (`CLAUDE.md`, `CONTRIBUTING.md`,
   `SECURITY.md`, `gitignore`, `claude`, `workflows` and four more). It would
   have caught the three stale statements in the README's contents (a
   `SECURITY.md` template it never names; "both CI workflows" over three;
   `tools/linkscan.py` named as a template). `pathscan` cannot catch the wrong
   tool name, because that path resolves at atelier's own root. Cost: the
   prose rewrite; the declaration is one line.
5. **RST31 and RST34, one test over the installer's tool set.** A test that,
   for each CLI `instruments/install` links, asserts a page exists, that every
   flag its `--help` prints appears in the page, and that `--help` stays within
   a stated budget. Measured: of 10 installed CLIs 9 have a page, so one fires
   (`ccstatusline`: either a page or a reasoned exemption, since it is a status
   line command and not operator-invoked); every flag is already in its page
   (0 missing across nine pages); three pages are pinned by no test and two
   tools by no `--help` budget. It would also make "atelier's instruments
   tests do" true (2 of 10 today).

Next after these, each measured: a commit-message shape check on the
commit-message plane, `area: ` subject and trailer, fires 1 subject in 300
commits (`TPL12`), and the why-dense half cannot be read; an ADR
section-name read beside `reviewscan`'s review-line read fires 3 of 8 records
(`TPL9`), and two are design proposals, so it would be noisy; a
`SECURITY.md` in a repo declared private (`RST11`), a recreated `SESSIONS.md`
(`RST20`) and a leftover placeholder in a root file (`TPL11`) each land clean
(0 hits), and are tripwires rather than cleanups.

**Not diff-visible, a read of GitHub.** Two host settings the standard states
are read by nothing on the hook or CI plane: private vulnerability reporting
(`RST13`; `flipcheck` reads it once at the flip) and delete-branch-on-merge
(`CON53`; `floorfleet` does not read it). On 2026-11-23 both read as the doctrine
wants for atelier (`enabled: true`; `delete_branch_on_merge: true`). A fleet read
of the two is an instrument change, not a diff guard.

**Before-plane note for `115/100`, not a diff guard.** Two rules in this slice
have a breach in a command's text: `RST29` (creating a remote that is not
private, or creating one unasked) and `RST30` (touching a repo whose remote
owner is not the principal's). `gh repo create` and `git remote -v` are both in
what a `PreToolUse` hook is handed. Neither is decidable from the command alone
(whether the ask included a remote is in the conversation); a hook could ask,
not decide.

## Doctrine defects found, not fixed here

Each is owed its own board item (`PROPAGATION.md` § *Pointing up*) where it has
none; none is changed by this file.

- **`docs/build/README.md`'s contents are wrong in three places.** It lists
  `tools/linkscan.py` among the shipped templates; the template tree ships
  `tools/check_links.py` and `linkscan.py` is atelier's own scanner. It never
  names the `SECURITY.md` template, which exists. It says "both CI workflows"
  while three ship (`ci-python.yml`, `ci-static.yml`, `floor.yml`). `pathscan`
  passes the first because `tools/linkscan.py` resolves at atelier's root.
- **`REPO-STANDARD.md`'s `floor.yml` bullet describes the retired scaffold.**
  It says the workflow "checks atelier out beside the repo and runs its public
  `tools/` scanners" and that "licenscan is a publish gate, left commented until
  the repo settles a licence". The shipped template is a thin caller that names
  no scanner (ADR 0008; `ChildFloorWorkflowTest.test_names_no_scanner` pins it)
  and carries no commented `licenscan`; the licence assertion lives in
  `.atelier-floor.json`. The bullet's second half is the statement ADR 0008
  removed.
- **`REPO-STANDARD.md` claims "atelier's `instruments/` tests do" pin the man
  page's flag superset.** Two of the ten installed tools do (`RST34`).
- **`SECURITY.md` says the repo "takes no third-party dependencies (zero-dep
  stdlib Python and Node)" and cites `tools/README.md`, *Supply chain*.** That
  section says the *tools* take none; the repo is wider. `instruments/browser-fetch`
  pins `mcp` and `playwright` in a tracked `requirements.txt`, admitted by ADR
  0006's addendum ("capability tools whose value requires deps"). The policy's
  scope statement is broader than its source and than the tree. Slice 5 named
  the same fact against `PRI8`'s measurement; this is its second home.
- **Root `CLAUDE.md` lists "a plugin/skills bundle" as part of the live floor,
  the next widening that "stays" the principal's call, while `README.md` says
  atelier "is now packaged as an installable plugin/skills bundle" and
  `.claude-plugin/` is tracked.** One state, stated both ways; the sentence also
  says "the making-public floor is **spent**", which is right, and then lists a
  widening already taken.
- **Root `README.md` is stale in four places.** Its `STORAGE.md` line says
  "iCloud = backup/offline, laptop = disposable", and `STORAGE.md` retired the
  iCloud leg on 2026-07-14 (slice 5 named the same line in
  `docs/method/README.md`: a second instance, in a second index). Its *Status*
  says "Early. The `method/` layer is standing up first; the `build/` layer ...
  follow", while `docs/build/` and its 24 templates exist. Its *What you get*
  list names four of the plugin's six skills (`fleet-sweep` and `review-drain`
  are absent). Its *Structure* table omits `skills/`, `commands/` and
  `.claude-plugin/`, which are the plugin.
- **The child `floor.yml` template carries a dated clause that becomes false in
  every copy on one date.** It says `sizescan` "may not be declared advisory or
  disabled from 2026-12-09. Until then it still can, and its line says so."
  `GRD21`'s code carries the date; the template text is stamped into children
  once and nothing re-stamps it, so each copy reads as a live statement of a
  past rule after the date, with no owner for the edit.
- **`REPO-STANDARD.md`'s file set is not met by atelier and nothing says which
  type atelier is.** It has no `docs/ARCHITECTURE.md` or `CONTRIBUTING.md`, and
  its read order names no ARCHITECTURE. The standard sizes by type and says the
  set is present "to the degree the type earns"; no `type` is declared in
  `.atelier-floor.json`, so a gap and a sizing call read the same (`RST2`).

Checked and found sound: `REPO-STANDARD.md`'s statement that a repo declared
private that GitHub says is public is "the one red" (`check_visibility` returns
`enforced, 1` for exactly that case and a stale `public` declaration only
partial); the roadmap command string in the roadmap template matches the one in
`REPO-STANDARD.md` and the test pins it; the plugin carries no version
(`.claude-plugin/plugin.json` has none, as the README says); the personal-data
list's closure and the wording that says who grants are both pinned by a test;
the `commit.gpgsign` bake and the `fleet-sweep` "healthy item 6" named in the
standard both exist.

## Doubts and unverified points

- **No rule is counted unenforceable and accepted in this slice.** The nearest
  candidates are `BND2` (whose condemning fact is a judgement about
  independence) and `RST23`'s "whether the purpose passes"; neither was counted
  accepted because no document says the cost is unobservable.
- **`REPO-BOUNDARY.md`'s splitting section is a self-declared draft** from the
  principal's pick among options offered, not his words as a ruling, and its
  items rest on a hand-up atelier has not re-driven. `BND6` to `BND11` are
  counted as rules because they read as instructions; if the doc's own status
  is the stronger reading, six rules move to "not counted".
- **The seed allowlist is not judged.** `templates/claude/settings.json`
  pre-approves `Bash(git:*)`, `Bash(python3:*)`, `find`, `sed`, `mv` and `cp`.
  The doctrine says the file is "the commands a session runs unprompted" and
  treats publishing it as a reconnaissance exposure, but never states how a
  breadth that includes a force-push or a history rewrite sits beside
  `AUTONOMY.md`'s always-confirm floor, where an allow rule removes the
  harness's prompt and the floor's stop is the agent's own. This census names the
  question and judges nothing; no rule is counted from the file (method 2).
- **`ccstatusline` may not belong to `RST31`.** The rule's scope is a tool "used
  away from the repo"; `ccstatusline` is a status-line command wired in
  settings, linked onto `PATH` by the installer. If it is out of scope the
  measure is 9 of 9.
- **Template CONTRIBUTING says the hook "is tracked (`.githooks/pre-commit`)".**
  `create-repo` copies it there; `/atelier:install-hook`, the route the
  README advertises, installs into git's untracked hooks directory. Two wirings
  exist for one hook; the skills and commands slice is the place to judge it.
- **Two private repos are named in the root README as provenance, and a child
  repo is named in `REPO-STANDARD.md`'s settings ruling.** Whether naming a
  private repo with its visibility is the joined name and posture `REC31`
  accepts as unenforceable, or the private child `PRO28` bars from a public
  worked example, is a judgement this census did not make and counted no
  breach for, as in slices 4 and 5.
- **Sixteen commits touched six of this slice's files since 2026-11-01** (the
  three build docs and the three root files; the templates not counted), and
  earlier slices' doctrine files have moved further (slice 5 recorded sixteen
  for slices 1 to 3). The census is a count at a time with no sweep that
  re-reads a changed file. `AUT17`'s re-grade (slice 5) and `PRI8`'s correction
  are still unapplied to the totals.
- **`gh api` was called twice, both GET**, against the repo's public data;
  the `enabled: true` and `delete_branch_on_merge: true` figures are those
  reads at one moment.
- **Counts in the measurements are crude where said so.** The "load-bearing"
  read of 262 review files (`TPL10`), the heading-or-label read of eight ADRs
  (`TPL9`), and the file-name tallies are greps and a small script, with no
  hand check of each hit.
- **Rule boundaries are a judgement**, as in slices 1 to 5; the folds are named
  in the method. Several rows join sentences the doc states
  separately (`RST19`, `RST20` and `RST31` to `RST35` are the longest), and a
  stricter split would raise the count.

## Remaining doctrine, outside `docs/method/` and not in this slice

Listed only, not censused, in the order the item's scope reads:

1. **`docs/decisions/`**: ADRs `0001` to `0008` and the dated decision records
   (20 files, with the directory's own `README.md` and `template.md`, which
   this slice read as templates and counted at `TPL9`).
2. **Skills and commands**: `skills/` (six skills) and `commands/` (four
   commands), `instruments/atelier-menu/SKILL.md`, and the plugin manifests
   under `.claude-plugin/`, which state the bundle's description.
3. **The validators' own stated rules**: the declarations in `tools/floor.py`'s
   registry, each scanner's docstring, `tools/README.md`, `instruments/README.md`
   and the `*.design.md` notes, where a rule is stated as what a check does.
   This slice cited several (`TPL6`, `RST15`, `RST16`, `RST23`) without
   censusing them.
4. **`docs/PERSONAL-DATA.md`** (the closed list) and the generated
   `docs/ROADMAP.md` index's standing rules. `RST23` to `RST25` and `RST28`
   count the *standard's* personal-data rules; the list's own entries and its
   preamble are not censused.
5. **`docs/roadmap/README.md` and `docs/reviews/README.md` at atelier's own
   root**, the live originals that the templates copy; they were read for the
   folds and not given rows.

Within this slice's scope nothing is left out: every file named in the brief
was read in full and every rule in it is a row or a named fold.
