# Changelog

All notable changes to atelier. Format: [Keep a Changelog](https://keepachangelog.com/);
newest first. Everything stays under _Unreleased_ until there's a reason to tag.

## [Unreleased]

### Changed (2026-11-09 — how a question reaches the principal, and what comes back: `320/820`, `420/020`, `020/270`)
Doctrine wording only; no scanner or tool changes.
- **His method for asking (`320/820`).** `COMMUNICATION.md` § *Asking for a
  ruling* carries his written method in his words: one question at a time, long
  form in the session, a short box, proof-read with no reference IDs; and, from
  his reactions to failed asks, answer his question first, real options only,
  check peers first. The four-question sentence now states the tool's limit and
  points at the practice. An account a session only read has reached nobody.
- **An answer is not a ruling (`420/020` parts a and b).** The same section
  defines the two classes in his words and the ⚖️ and 💬 record marks.
  `RECORD.md` points at it. The sweep of old records and any guard stay open.
- **The unmet-term check (`020/270`).** `COMMUNICATION.md`, the language axis:
  before sending, check every term a reader could not have met and introduce it
  once. A scanner for this was measured and rejected, so it stays wording.

### Added (2026-11-09 — `ccclose` tells a running agent from a cut one, `210/380`)
- **`ccclose` check 12 has a fourth agent state, *still running*.** An agent
  with no end recorded was always called cut mid-flight, so a close under a
  live worker read as "the agent is dead". It is now running when its
  transcript last grew under ten minutes ago (`FRESH_MS`) and the parent has
  recorded nothing more than ten minutes after it, and its line says how long
  ago. The bound comes from a census of 3,587 agent logs: 99.9% of gaps
  between records are 600 s or less, the longest a foreground command runs.
  Running still fails the check; cut is kept for an agent gone quiet. A new
  `still running` count sits in the summary line, `--json` `counts` and the
  identifiers block. `210/070` was measured and declined: a missing
  `end_turn` flags 130 completed agents for every 50 failed ones. The same
  census found the parent records a `failed` status that `ccclose` does not
  yet know (`210/400`).

### Changed (2026-11-10 — `reviewscan` says "not in scope"; floor `disabled` gets an end date)
- **`reviewscan` no longer prints "clean" over a scan that matched no decision
  record (`320/770`).** A repo whose records are named `NNNN-slug.md` has none
  in scope, because the date gate reads the filename. The scan now says "not in
  scope", counts the numbered records it did not read (`--json`:
  `unread_numbered_records`), and keeps its exit status. Reading dates from
  numbered records stays open on the item.
- **A floor `disabled` entry can carry `{"why", "review-by"}` (`320/800`).** The
  bare string still parses. A missing or passed `review-by` warns on the floor
  line and in `floorfleet` (🟡 undated, 🔴 passed, with its age) and changes no
  exit status. The 2026-12-09 bar on `disabled.sizescan` is unchanged. Making it
  a block is owed, with a date and a fleet probe.

### Changed (2026-11-09 — the principal's answers on `160/340`, `115/020`, `310/160` applied)
His answers to options a session offered (answers, not rulings in his own
words, except where quoted).
- **The sizescan bar now covers `disabled` too, from the same date
  (`160/340`; *"Bar both"*).** `floor.DISABLED_BARRED_FROM` (a separate table,
  2026-12-09) makes a `disabled.sizescan` entry a config error from that date,
  as `advisory.sizescan` already is. Until then the entry works, and its floor
  line, `floorfleet` and `--json` (`barred_from`, now also set on a disabled
  result) name the date. A repo with no board needs no entry: the check passes
  on an empty tree. No repo on the machine lists it today.
- **`pins` blocks an unstamped copy from 2026-12-09 (`160/340`; *"Require a
  stamp by 9 Dec"*).** From `COPY_BLOCKS_FROM` four floor-copy states fail
  `--check`: `drift`, `unstamped`, `no-reference` (an old pin: bumping it
  fixes it) and `malformed`. `skipped` and `unchecked` stay report-only. A repo
  archived on GitHub is exempt, since it can no longer be changed: `pins` asks
  `gh repo view`, only from the date and only about a child that would
  otherwise fail; if that cannot be established the child is not exempt and the
  line says so. `--json` `floor_copy` gains `blocking_states`, `would_fail`,
  `failing` and `archived_exempt`.
- **`PRINCIPLES.md` §9 and `EVIDENCE.md` §3: confidence is worked out from the
  source (`115/020`; *"Work it out from the source"*).** Compute it from how a
  fact was obtained, who supplied it and its age; store a rough rank only where
  one method itself varies, never a bare score. House rule only; no tool.
- **The board-states design draft is revised to his answers (`310/160`).** A
  maybe-later item is plain open work with no mark (his words); the waiting
  field narrows to a real blocker and is put to him as the one open question;
  only he may close commissioned work, a session may retire its own idea; the
  known 45 non-delivery ticks are fixed and the rest left. Still a draft.

### Changed (2026-11-09 — three review rulings applied: `160/790`, `160/340`, `160/020`, `200/030`)
Mike's answers of 2026-11-09 (answers to options offered, not rulings in his own
words, except where quoted); the reviewers' counsel on the rest applied as written.
- **The floor's report-only lane is barred for `sizescan` from 2026-12-09
  (`160/790` HX1; *"Bar it; nova converts"*).** The check enforces the board's
  design (a short main board, each item's detail in its own file), and the
  floor's `advisory` form was a lane round the ruling's *"Never allow it"* that
  its briefing never named. `floor.ADVISORY_BARRED_FROM` makes an
  `advisory.sizescan` declaration, in either spelling and however reasoned or
  dated, a config error from that date, so the floor blocks and says why. Until
  then it still works: the check's floor line, `floorfleet` and `--json`
  (`barred_from`, always present) name the date. A reasoned `disabled` entry is
  untouched. Two children declare it today and must remove it and convert their
  boards before the date. The registry `why` carries the forbid-the-act
  declaration, and the child `floor.yml` template no longer teaches adopters to
  declare sizescan advisory.
- **sizescan's wording and listing (`160/790`).** The docstring and README no
  longer say nothing silences the gate without naming the floor lane (HX1);
  GUARDS.md names the one finding an ignore glob cannot accept, with the fixture
  remedy (fence the `[x]` lines), and the allowmarker docstring points at it
  (HX3). A roadmap under a store-named directory is not read for cold content, and
  the `suppressed:` line now counts those (`N roadmap(s) under a store directory`,
  `roadmaps_in_store_dirs` in `--json`): a new known-zero part, so runs before and
  after this entry do not compare on that line (HX3). The completed-item listing
  neutralises control and format characters through a new shared
  `report.safe_text` (HX2); the other scanners that echo tracked text still do not
  use it. Reworded: characters, not columns (HX5); "derived there" (HX7); the
  two by-design exceptions to "a hatch is never silently ignored" (HX8); this
  repo's own `.sizescanignore` comment (HX10). HX4 is record only: between the
  landing commit and the next one a glob over a gated roadmap printed a count of
  files by glob that it had not suppressed, so counts on that line from
  2026-10-16 08:12 to 15:28 UTC do not compare with later ones. HX6 was already
  done (`skills/review-brief`); HX9 needs nothing.
- **`stampscan` and the floor stamp (`160/340` FV1, FV2, FV5).** The floor is now
  identified by the file its `source=` resolves to, so a respelled path (`./docs/`,
  `docs//`, a `..` segment, a case-folded name where the filesystem agrees) is
  still the floor. A `stampscan:allow` marker inside a floor stamp is ignored: the
  block is compared and the result says so, and the floor's red never offers
  `narrow=` or the marker as a way out. PROPAGATION.md's bullet names the stamp of
  the `floor` region rather than `region=floor`, and says an already word-for-word
  copy carrying `narrow=` narrows nothing. `findings` gain an always-present
  `floor` field. A `.stampscanignore` glob can still skip a whole file.
- **Who is a child (`160/020`; *"Own or control"*).** PROPAGATION.md reads
  repos the principal owns or controls, with exclusions recorded in the estate
  root's private records, and a repo he neither owns nor controls outside the
  rule without a ruling (CM1, CM2). "Answerable" is now "decidable, not
  enumerable", naming the discovery gap (CM4); the three verbs point at the layer
  rule instead of restating it (CM5); an exemption is re-tested when the rule it
  departs from moves, and the two homes are stated (CM3). CONCURRENCY.md's queue
  lane names the fallback for a target with no queue (the estate root's board,
  the narrower of the two offered), the visibility of the target (CM6, CM7), and
  what a finder that declines the lane owes (CM12). The quotation is attributed
  (CM9) and the glossary defines *Child* (CM11). CM8 and CM10 need nothing; CM13
  corrects a frozen record and waits for it to be next touched.
- **The mining pass (`200/030`).** PROPAGATION.md states it: on the principal's
  word, about monthly, a session reads the transcripts and files board items,
  proposing changes and never making them. TOOLBOX.md § *Background jobs* records
  what he ruled out (a standing helper registered as a login item) and what is
  fine (a background job inside a live session); the flat "no background jobs"
  line on `210/190` carries a dated correction.

### Changed (2026-11-09 — `ccarchive` rollback check `160/670`; the rule-copy report `160/340`)
Mike's answers of 2026-11-09 (an answer, not a ruling) and his words on the
copy report, *"The approve the report only option for 1 month and then we move
to blocking per option 2"*, applied as the reviewers counselled.
- **`ccarchive` notices a rolled-back archive (HD1).** Each save carries a save
  number in `manifest.json.sig`, bound to that manifest by its own MAC, and the
  machine keeps a small 0600 record of the last save beside the signing key. An
  index older than the record (or the same number over a different index, or
  vanished) is `rolled-back`: runs, `--restore` and dry runs refuse it (exit
  2), `--verify` and `--audit` report it (exit 1). A sync fault looks the same,
  so the message says what to check. A volume ahead of the record, or no record,
  is adopted. Archives signed before this have no number and start a record.
- **`--rekey` verifies first (HD2, HD3).** It checks the index under the old
  key and refuses anything but `verified` (exit 2, nothing minted or changed);
  `--rekey --accept-unverified` is the deliberate clear and names the state it
  cleared. HD2's fuller fix (a key per destination) is not built: `man
  ccarchive` now says that no roll brings two archives across under one key.
- **`tools/pins.py` reports each child's floor copy (`160/340` FV3, FV11;
  `020/215` LR4).** It runs `stampscan`'s own comparison on the stamped floor
  block against the floor text **at the child's own pin**, with the four
  placeholders put back. **Report-only until 2026-12-09, blocking from then**
  (one dated constant, `COPY_BLOCKS_FROM`, printed on every run): from it a
  copy that differs fails `--check`. `unstamped`, `no-reference`, `skipped`
  and `malformed` copies are reported and never fail. The floor-narrowing
  bullet in `PROPAGATION.md` now says what does and does not reach a child's
  copy.
- **The copy and its sources agree (AK1, AK3, DR2, RR1, RR8, RR12).** The floor
  region and the template stamp (byte-identical, one commit) restore the
  options list's sixth item and the no-device clause, and point the
  stop-and-confirm account at `00-APEX.md` instead of restating it. The apex
  names the floor by reference to `AUTONOMY.md` § *Always confirm*, which gains
  the order sentence (re-brief before the act). `skills/session-onramp` § 2 is
  a one-line pointer instead of a third hand-kept copy. Children inline the old
  block until their next pin bump.
- **Doctrine written down.** A parent's local narrowing is written where its
  children can read it, with the diagnostic (`310/130`, option a); verify-the-act
  stays behind the pointer, not in the block (`160/310` HF8). The Laws entry
  below carries a dated correction that its shedding was a convention (LR4).

### Changed (2026-11-09 — `ccmail` cold pass applied: `210/130`)
Mike answered *"Keep it, lock the cache"* to the options offered on the review's
major finding (an answer, not a ruling); the reviewer's counsel on the rest was
applied as written. Review: `docs/reviews/2026-09-25-0715-ccmail-build-cold.md`.
- **The delegated route stays and its reach is written down (CC1).** ADR 0006
  gains a 2026-11-09 addendum, and `man ccmail`, the README and the tool's own
  header say what anyone able to run a command as the operator could read:
  every mailbox the delegated identity covers on route 1, resting on the cloud
  CLI's own stored login file; one mailbox on route 2, with the token one
  `security` command away. ADR controls for future credential-holding
  instruments now require that line, per route. Not built: refusing a subject
  unlike the cloud login's own identity (offered, not part of the answer).
- **The cache is private and expires (CC2).** Directories 0700, files 0600,
  whatever the umask; every run tightens looser existing paths and deletes
  message folders untouched for 30 days, with one line on stderr. The sweep
  never follows a symlink and refuses a root that is a link, `$HOME`, `/` or in
  a work tree; tests pin each limit. `rm -rf ~/.cache/ccmail` is documented.
- **Threat list in the ADR addendum (CC3); standing-credential pointer (CC9).**
  The superseded 0600-file fallback line in the ADR's controls is marked
  withdrawn. The private-registry entry is owed outside this repository.
- **`ccpdf` refuses an oversize page (CC4).** A 64-megapixel default budget,
  `CCPDF_MAX_PIXELS` to adjust, a named error before allocation, asserted by the
  selftest. Re-run `instruments/ccpdf/setup` to install it. A sandbox profile was
  considered and not built (reason in the ADR).
- **Write path (CC5, CC6, CC11).** Files are created with `wx` (no write through
  a planted symlink), the repo guard resolves real paths, a message id must be
  hex, same or colliding names are suffixed instead of overwritten, name caps
  count bytes and cap the extension, one failing attachment no longer aborts the
  batch (exit 1, each named), a part with no id and no data is skipped, bidi and
  control characters are removed from names and listings, requests time out
  after 60 seconds, `&#x..;` references decode, and an unreadable Keychain is an
  error rather than "nothing stored".
- **Docs against behaviour (CC7) and consent (CC8).** `--get` with no value, or
  followed by an option, is refused (the man page no longer says a bare `--get`
  means all); `--status` is described as several calls; a partial selector miss
  is warned; the README points at the right addendum. The loopback consent now
  sends `state` and a PKCE challenge and ignores a callback without the state.
- **Overtaken, not built:** CC10 (no route live): the cache shows downloads from
  late September to 8 November, so the tool is in use; no probe was run. CC13
  concerns the review's own records and the board item's pointer, which this run
  may not edit. CC12 was a clean note.

### Changed (2026-11-09 — three more cold-pass applications: `020/050`, `160/910`, `160/270`)
Mike answered options a session offered on each; those are answers, not rulings
in his own words. The reviewers' counsel was applied as written, as far as each
answer left it standing.
- **The independence of a cold reviewer is fixed at the reader, not at every
  writer (`160/910`, `160/930`, `160/230` RR2, `280/030` CH1).** His pick:
  *"Fix the reviewer's side"*. A cold reviewer **skips the session-log step** of
  its read order (`CLAUDE.md` step 4, the child template's step 3, the
  review-brief skill's spawn-prompt line, `REVIEW.md` rule 2), and the
  writer-side "side doors" duty in `REVIEW.md` rule 1 and its `RECORD.md`
  sentence are withdrawn. The new text cites the three recorded occurrences by
  date and names what stays accepted. `REVIEW.md` rule 1's scope sentence now
  covers any brief that carries deferred material, whoever wrote it (DS11);
  rule 4 has the reviewer record the orchestrator's reviewer-facing instructions
  in the verdict's provenance and says what orchestrator direction may contain
  (RR2); rule 2 names the body-free commit read and why plain `git show` is the
  trap, and the re-run duty has its home in § *Re-run every "live-proven"
  claim* (BF5, BF15). CH1 was already met by `280/040` (disclosed contact;
  `CONCURRENCY.md` § *What the channel is not*). `tools/coldsweep.py --commit`
  now leaves the board store out when no `--path` is given and names it (BF1),
  prints only the message's first line (BF2), exits 1 when nothing is in scope
  and names each `--path` that matched nothing (BF3), reads an absolute
  `--also-exclude` correctly or refuses it (BF4), refuses a `--root` below the
  repository top (BF9) and a shallow clone's boundary commit (BF10), and has
  tests for its untested guards (BF6, BF7). `coldsweep` is not a floor check:
  no repo's build changes. Not applied: DS2, DS4, DS6 to DS8 (they concern the
  withdrawn writer-side duty), and the board item DS12 asked to queue for a
  warn-only shape check (moot with the duty).
- **The estate-root repo gets no special naming rule (`020/050`, `020/030`).**
  His pick: *"Treat like any private repo"*. The sentence that named it only in
  a private child's onramp, never in any public tree, is gone from the floor's
  *Estate resources* bullet (its stamped template copy kept identical) and from
  `PROPAGATION.md`, which keeps a short, dated account of the withdrawal.
  `RECORD.md` says it is an ordinary private repo (name allowed; what it holds
  and its condition by type only); `TOOLBOX.md` and `AUTONOMY.md` no longer lean
  on the old rule. The one audit paragraph that named private repos beside their
  configuration is rewritten generically, and the ADR on estate-internal context
  carries a dated correction of its "worked examples keep their names" sentence
  (superseded by the `320/330` answer). From the C5 cold pass: C5R3's invented
  quotation is corrected on `020/250`; C5R9's missing grant-date clause is added
  to `GUARDS.md`. The rest of the C5 findings concern the term-list options and
  fall with the dropped blocked-word idea. Forward only: nothing already
  published is rewritten.
- **An ask's account always arrives as a finished message of its own, before the
  device (`160/270`, DR1, DR3).** His pick: *"Always, as two steps"*. The rule no
  longer branches on a display mode no session can see; `COMMUNICATION.md`
  § *Asking for a ruling*, the floor's *Asking* bullet and its stamped template
  copy (kept identical) say so, at the stated cost of one extra turn per ask.
  The apex's account list points at the scaling sentence in
  § *Make the ask valuable*, and that section's quote is no longer called the
  whole calibration. Not done here: DR2 (the floor's confirm bullet), which goes
  with the rule-copies work.

### Changed (2026-11-09 — four cold-pass applications: 160/050, 090, 100, 470)
Mike answered options a session offered on each; those are answers, not rulings
in his own words. The reviewers' counsel was applied as written, taking the
narrower option where one was offered. Scanner behaviour changes reach every
child at its next CI run; each was probed against every floor-carrying repo on
this machine, old scanner against new, and no repo's blocking result changed.
- **`floorfleet` survives a missing `gh` (`160/050`, FF1).** All three `gh`
  call sites go through one wrapper that maps an unstartable binary to the
  documented failure values. `--remote` degrades to unknown rows, which red
  `--check`, instead of a traceback. `pointerscan`'s docstring no longer
  claims a staged read it does not perform (PG1) and documents its first-line
  file hatch (PG2, kept, not dropped).
- **`leakscan` refuses a term list that holds no terms (`160/090`, AR3).** A
  zero-byte or comments-only list satisfied `--require-terms`, loaded nothing,
  and printed "structural + local". Under `--require-terms` (the hook plane) it
  is now exit 2; without the flag it degrades like an absent list, with a
  warning naming the file, and the pass line says "structural only". CI passes
  no `--require-terms`, so no child's CI changes. An unreadable list (a
  directory, a mode-000 file) is exit 2 with a remedy, not a traceback. A
  set-but-empty `--terms ""` or `$ATELIER_LEAKSCAN_TERMS=` is refused under
  `--require-terms` and means "not set" without it. `floorfleet`'s board no
  longer calls an empty list full cover. AR4 was already fixed. AR2 is largely
  moot, the bypass having been removed: only the informational-signature
  comment is re-grounded. AR5 to AR7: the pin test cites the real rule, the
  `floor.yml` comments say why `github.repository` is exempt from the env-routing
  rule and that `--warn` never covers an environment error, `signscan` passes
  `--end-of-options` to `git rev-list`, `REVIEW.md` rule 3 says an ask names any
  prior answer on the same finding (AR8), `decisions/README.md` says "as of
  <date>" for live-state addenda, and the review-brief skill says to read
  environment facts off the machine.
- **`secretscan`: a fingerprint under a credential key blocks (`160/100`, AB1).**
  `api_key: SHA256:<body>` passed fully clean after E3, because the assigned
  rule only ever saw the short algorithm token. The carve-out is now off on any
  line that names a credential key, which restores the pre-E3 block. Fingerprints
  in prose context stay suppressed, as ruled. Suppressions are now located
  (`path:line`, human and `--json`, first 50) as well as counted (AB3). AB2 and
  AB4 to AB5 are docstring and comment corrections; AB6 is a recorded note.
- **`publishscan`: the hatch is visible, and the patterns are tighter at the
  edges (`160/470`).** PL1 (non-ASCII paths) was already fixed by `260/120`
  and is now pinned on a macron-named directory. Every run prints
  `suppressed: N never-publish path(s) by .publishscanignore`, zero included, lists
  the first ten, and `--json` carries them all, on the default and history
  planes (PL2). Behaviour changes: paths match with **case folded**, so `.ENV`,
  `ID_RSA` and `server.KEY` red as their lower-case spellings do (PL7);
  `.*_history` and `._*` match the basename only (PL6); `Thumbs.db` is no longer
  shadowed by `*.db`, and the selftest asserts every entry is reachable (PL8);
  the remedy quotes the path and says how a glob matches (PL11, PL13). The
  registry `why` and the README heading now name the class, the left-out list
  lives in one place (PL4), and one comment no longer describes what a survey
  found tracked (PL3; the pushed commit body is a frozen record).

### Changed (2026-11-09 — the hand-up route: parent-side duties, scope of the duty, vulnerability-class defects, `160/300` RU2–RU6, RU12)
Mike's answer of 2026-11-09: the cold pass's counsel applied as written. RU1 and
RU7–RU11 were applied or settled earlier.
- **Children: nothing to do.** The edits are in `PROPAGATION.md` § Pointing up,
  outside the stamped floor region.
- **An atelier session reads the open hand-up PRs at open and lands any it finds
  first (RU4, with RU2).** Eleven had stood open for three weeks until the
  principal asked. `CLAUDE.md`'s read order gains the `gh pr list` step.
- **The merge-time check is a command (RU2).** `gh pr view <n> --json
  headRefName,title,body,files`: a `report-` head with no repo token unless that
  repo is public, a title and body that say hand-up and name no private repo,
  files that are the item and the index only. The harm is one-way, so it is read
  before the merge. The branch-and-title lint is the next rung and is not built; the
  pass asked for it as its own item, which this commit does not file.
- **An index conflict is resolved by merging in the parent's worktree (RU3):**
  `git merge --no-ff`, `--rebuild`, never a rewrite of the reporter's branch; the
  filer is told to expect the conflict, not dodge it.
- **A hand-up's number is provisional (RU12):** the parent runs `board.py --check`
  after each landing and moves the later-landing item itself.
- **The duty is the principal's repos (RU5), the narrower of the two options.**
  An adopter outside the estate is not bound, and the text says which routes it
  has: hold-and-flag, a fork and PR, an issue, `SECURITY.md` for a vulnerability.
- **A doctrine defect that is a vulnerability goes private first (RU6),** with its
  public item landing with the fix.

### Changed (2026-11-09 — the third "another session is live" cue ends in an action, and the cue wording is made true, `160/560`)
Mike's answer of 2026-11-09: the cold pass's counsel applied as written.
- **Children: nothing to do.** The edits are in `CONCURRENCY.md` § The trigger and
  § The channel, which a child reads through the pointer, not in the stamped block.
- **The ask cue ends in an action (TC1).** A peer's answer that names this repo is
  the dirty-tree case without the dirt: move to a worktree and announce your file
  set. It was the one cue of the three that ended in knowledge.
- **The ask is a fact only when a peer answers (TC2).** An empty list or no reply
  is silence and licenses nothing; § The channel's *Hello* sentence says the same.
  This also applies `280/030`'s CH2, which the note there now records.
- **The counts and the accuracy (TC3, TC4).** "Two blind spots" is "two more", and
  says the opening paragraph's blind spot is the first; "discoveries you make by
  accident" is "reach you by being told or by stumbling on the evidence". CH7's two
  halves are both done, and `280/030` says so (TC7).
- **Not done, by the pass's own word:** TC5 and TC6 are notes with no action owed.

### Changed (2026-11-09 — `blockscan`'s advisory report: nothing routes it to a person, `160/430`)
- `tools/README.md` says the unmapped-heading report stays in the CI log, where it
  already is, and that nothing routes it to a person (CU10). Documentation only.

### Changed (2026-11-09 — `SECRETS.md` says what its permanent bridges rest on, `160/570`)
- The imposed-cap and break-glass bridges are not the shapes `PRINCIPLES.md` §7
  licenses (temporary, or unsafe to codify); they rest on §5's credential rule
  (*Honest pattern*, *name the gap*), and §7 supplies the grammar's name. One
  paragraph in `SECRETS.md`; no child action.

### Changed (2026-11-09 — `cctranscript --list` marks an unreadable mirror instead of dying, `160/680`)
- **Children: none use it; nothing blocks.** One damaged or unreadable mirror used to
  abort the whole listing with a raw stack trace. The row now reads `(unreadable —
  <reason>)` in the text listing, `firstPrompt: null` with `unreadable: true` in
  `--json`, the command exits 0 and the other rows list (the per-row guard
  `--search` already has; FP1 counsel iii, folded from `CP4` and `CS11`). A readable
  row carries no `unreadable` key, as an unevicted one carries no marker. The man
  page says so.

### Changed (2026-11-09 — `cctranscript`'s header prints the mid-turn and harness chips at zero, `160/880`)
Settled by the principal's standing steer that report fields stay comparable.
- The header line read side by side with another session's now has the same
  fields every run: `N mid-turn` and `N harness` print at `0` where they used to
  vanish. A script that matched `2 you · 2 Claude · 2 harness` needs `· 0 mid-turn`
  between. The README's "the field set never varies" is true again without its one
  stated exception; the context chip still drops when the size is unknown.

### Changed (2026-11-09 — the new-repo reviews template leads on independence, names one applier and the child's seat names, `160/590`)
Mike's answer of 2026-11-09: the cold pass's counsel applied as written. Which
tier reviews is untouched: the principal still names it.
- **Children: nothing to do, and nothing blocks.** `docs/build/templates/docs/
  reviews/README.md` is copied at creation and no check compares it, so a repo
  created earlier keeps the text it was given (this is also the entry the
  commit that retired the model names in this file, `77fc609`, lacked). A repo
  that wants the new wording re-copies the file from atelier.
- **It leads on independence (TT1).** The retired sentence made "a more capable
  model" the practice's subject, which `REVIEW.md` § *Why review* rejects: the
  first sentence now says an independent session on the capable seat reviews,
  and that capability is the multiplier on top, not the precondition.
- **One applier, with the doctrine carve-out and the spawn test (TT2, TT4).**
  The seat that built the work applies findings on ordinary code; self-authored
  doctrine, by function (prose or code), is reviewed from a session its author
  neither started nor instructed, its findings are the principal's, and decided
  ones go to a hand that wrote neither the doctrine nor the verdict. The closing
  paragraph no longer names a second applier.
- **The same seat names as the child's `ECONOMICS.md` (TT3):** capable seat,
  workhorse seat; the model-per-seat naming is said to be person-local and held
  there. "Principal-named review tier", board vocabulary a child never sees, is
  gone from the file.
- **"Stamped" is said to mean what it does (TT5):** `create-repo` fills the
  placeholders when it copies the file; `stampscan` does not compare it.
- **Pinned (TT6):** `test_templates.py` fails if any file in the template set
  names a model tier (co-author trailers aside), and pins the three changes above.
- **Routed, not done here:** a sweep of existing children for the retired
  sentence belongs to a session that may touch those repositories (TT5).

### Changed (2026-11-09 — a run that stops at a dirty checkout has a way to sync and land, and one term for "no upstream", `160/520`)
Mike's answer of 2026-11-09: the cold pass's counsel applied as written. The
skill the pass reviewed has since been cut back to a pointer at the prompt, so
the wording lives in the parent now.
- **Children: the floor bullet changes one clause.** "where there is a remote"
  is now "where the branch has an upstream" in `PROPAGATION.md` and the template,
  identically. A child's own stamped copy follows at its next pin bump; nothing
  blocks on the difference before then.
- **After the stop, sync without touching the tree (SY1).** `CONCURRENCY.md`
  § Integration hygiene gains a bullet: `git fetch origin` is always safe at a
  dirty checkout; base the worktree on `origin/<branch>`; make a claim at the
  primary checkout after `git merge --ff-only origin/<branch>`, which succeeds
  when the incoming commits touch none of the stranger's dirty paths and refuses,
  changing nothing, when they do (then CF3: sync, take the next item, touch
  nothing). Sync first: `git pull --rebase` refuses at a dirty tree. Re-driven
  in a scratch repo before it became text. § Claiming work's "Push rejected"
  line points at it.
- **One term (SY3)**: "upstream", the thing git tests. A fresh worktree branch
  has a remote but no upstream and uses `pull --rebase --autostash origin main`.
- **Dirty means anything `git status` shows, untracked included (SY5)**, and a
  run resumed after a context cut runs the recovery sweep before the gate (SY4).
  A repo whose read order repeats the bookend does not run it twice (SY7).
- **SY2 is already met:** the skill holds no copy of step 2 any more.
- **SY6, partly:** the plugin has carried no `version` since 2026-10-18 (each
  commit is its own), so there is nothing to bump. `PROPAGATION.md` now says the
  bundled-mode drift check is weaker than it reads and that the plugin's
  `CHANGELOG.md` is the one signal left. Putting a `version` back reverses a
  choice of the principal's and is not taken here.

### Changed (2026-11-09 — `pathscan`'s brace expansion is capped per file, a bare `./` path is a citation, and the residuals are written down, `160/490`)
Mike's answer of 2026-11-09: the cold pass's counsel applied as written.
- **Children: nothing blocks.** `pathscan` is warn-only on every child's hook and
  CI (`--warn` in the registry template), so no exit code moves. The child probe
  (every repo with a floor config, scanning `docs`) found 22 repos unchanged and
  two that each gain two warn-only findings, all `./` paths in a span that held
  only the path. Such a span now prints a finding where it printed none; add
  `pathscan:allow` if the command is meant to be absent.
- **One file may expand to at most 1,024 alternatives (PX1).** The cap was per
  token (64), so a line of 25,000 wide tokens cost about 100 s even after the
  finding cap. A token past the file's allowance is skipped whole and **counted**:
  the summary line prints `N brace token(s) past the 1024-alternative per-file
  cap` every run, a known zero included, and `--json` carries
  `brace_tokens_over_cap`. The busiest real file in the corpus used 35. The
  test counts disk lookups, not seconds, so a slow machine cannot flake it.
- **A bare `./` path is a citation unless an argument follows (PX2).**
  `` `./x.sh run` `` is still a command and skipped; `` `./tools/x.sh` `` is
  checked. `./`-led spans that held only the path were silently clean before.
- **A finding names the text as written (PX5)** (`expanded from the written
  `docs/x{1,2}.md``), and **the human line strips control and bidi characters
  (PX6)** (`report.strip_controls`, the filter `report.broken` already used).
- **The residuals are stated (PX3, PX4, PX7, PX9, PX10)** in the module
  docstring and `tools/README.md`, with `--help` naming both behaviours: a
  comma-less group drops its whole token, a path against a brace is unseen, the
  `./` rule reads one line's backtick parity, an expansion can name a path
  outside the root, and a quantifier expands to targets nobody wrote.
- **`--selftest` now exercises both behaviours (PX11)**, and a boundary test pins
  64 alternatives yielding 64 and 65 skipped.
- **Not done:** the registry `why` keeps its one-line purpose (the behaviours are
  residuals, not purposes); PX12 is left as it stands.

### Changed (2026-11-09 — the board generator's line-width promise is tested on its real output, `160/220`)
Mike's answer of 2026-11-09: the cold pass's counsel applied as written. BG1 and
BG2 stay the funded fix at `290/060`; BG11 needs nothing.
- **Children: nothing to do, and nothing blocks that did not.** No generated
  index text changes; the child probe (every repo with a floor config) found no
  change in any `board` result.
- **The promise is held by a test (BG3).** `test_board.py` and `board --selftest`
  run the real `wrapscan` over a whole generated index built from stressing items
  (flags, long claims, long titles, a wrapped title, a long slug). The one case
  not held is named in the `board.py` docstring and `tools/README.md` and pinned
  by a test: an item with a sibling-only allow-marker. The generated-file
  exemption question (`010/070`) stays open for that case.
- **The selftest no longer fails with `HOME=/` (BG7)** and now checks the
  in-tree branch, the one that emits a path, for a machine-local path.
- **A hand run from a subdirectory finds the board (BG8).** With no `--root`,
  `board` uses the git toplevel; the floor always passes `--root`.
- **Stale wording swept (BG4, BG9, BG10).** The module docstring and the README
  no longer give the superseded spelling or the withdrawn residual; the 2026-08-17
  entry carries a dated correction.
- **Dead code removed (BG13).** `GENERATED_MARKS` in `board.py` was never read.
- **Already moot (BG6, BG14):** `plainscan` and its reply hook were removed
  (`020/360`). **No change:** BG5's guidance half was corrected in place on
  `010/030`, which now says its fleet table is a dated reading; BG12 concerns a
  brief that was folded and deleted.

### Changed (2026-11-09 — three cold-pass applications: `160/380`, `160/450`, `260/050`)
Mike answered options a session offered on each; those are answers, not rulings
in his own words. The reviewers' counsel was applied as written.
- **Held-back review notes never live in the shared scratchpad (`160/380`).**
  The harness hands every agent the orchestrator's own scratchpad, so a sibling
  `.deferred.md` held there is one read from any reviewer. `CONCURRENCY.md`
  § *Orchestrated queue runs* now says where such material goes (a user-local
  directory outside the repo, every worktree and any harness scratchpad, never a
  reviewer's working directory), names the recipe (`<scratchpad>/<worker>/`),
  grounds *absolute* on the argument, softens "binds" to "reduces", writes the
  test that says when the rule is spent, and adds a close-time listing of the
  scratchpad root. `REVIEW.md` rule 1 no longer calls an orchestrator-held store
  "structural" unless the bytes never sit on a path the reviewer is given; rule 2
  counts a fourth hand-written-exclusion instance; rule 4 has the author run
  `pointerscan` on the pointer it writes. Owed and not done: the dispatch
  sentence in the queue-run prompt and skill, which hold no rule of their own.
- **A dated rule carries a `mandate` or `default` kind the checkers read
  (`160/450`).** `.atelier-floor.json` advisories take an optional `kind`;
  `floor.py` validates it and shows it, `floorfleet.py` shows it and says aloud
  when it is missing (an unlabelled date reads as a mandate). On the hook plane a
  mandate's or unlabelled `review-by` moving later than HEAD's is a warn-only
  line. `GUARDS.md` gains the scope, the house readings marked as such, and the
  cross-links with `PROPAGATION.md` and `REPO-STANDARD.md`; the template and the
  `floor.py` docstring use a placeholder date. `coldsweep.py` warns when an
  `--also-exclude` matches nothing. No existing date is labelled by this change:
  labelling is each repo's own edit, and which kind a date is needs the principal.
  Not built: a fleet-wide house-date declaration for the board to compare to.
- **Each repo may declare its visibility, checked against GitHub in CI
  (`260/050`).** `"visibility": "public" | "private"` in `.atelier-floor.json`.
  Inside Actions only, `floor.py` reads GitHub's live answer (the event payload
  if the API is unreachable): declared private but public is a red build with a
  loud alert; the reverse, an unreadable answer, and no declaration all warn and
  never block. It detects and alerts and cannot stop a flip. Not built: what a
  public declaration tightens, and the daily external check, which is `390/020`'s.

### Added (2026-11-09 — child-and-parent relationship doctrine, six items)
Mike approved the recommendation on each item on 2026-11-09 as a pick from
options a session offered (an answer, not a ruling in his words). Doctrine
wording only; no scanner or tool is built.
- **The floor binds a repo made public later (`320/380`).** The estate-resources
  bullet reads "is public, or is ever made public", with one sentence that
  spelling the actual path defeats the convention. The canonical region and
  the template's stamped copy change together; children's copies update at
  their next pin bump.
- **No private child in a worked example (`320/330`).** `PROPAGATION.md` § *The
  route* rule 2 reaches doctrine's own prose; the worked examples, bearings and
  instances in eight method files and the build README say "a private child".
  Acts done to a repo and the extraction origin's provenance citations are left,
  pending his word.
- **A greppable marker for owed-upstream lines (`310/020`).** `Pending
  upstream:`, an ISO date and the parent item or `unfiled`. The enumerator is
  not built.
- **Only parent and child is modelled (`390/010`).** One generic line points
  other relationships at the estate root's registry.
- **One route between any two repos (`310/120`, `310/140`).** `PROPAGATION.md`
  § *The same route between any two repos*: a PR files an idea and never the
  fix, redaction keys on the target's visibility, an issue where there is no
  write access. How the target learns a PR arrived is undecided.
- **Splitting a repo (`320/580`).** A draft section in `REPO-BOUNDARY.md`
  from one hand-up's testimony, with what could not be grounded listed.

### Changed (2026-11-09 — a stranger's edits stop a claim of the same item only, `010/160`, `160/260`)
Mike answered *"Stop only for the same item"* (2026-11-09; an answer to the options a
queue run offered, not a ruling in his words). `CONCURRENCY.md` § *Claiming at a dirty
primary checkout* (CF3): a session finds a peer's uncommitted edits, still does its work
in its own worktree, and stops a claim only where the peer's edits touch the item it
wants; a different item beside a live peer is claimed with `--rebuild --from-index`, by
pathspec. The old stop and its "stricter than its cause" paragraph are gone; a peer's
staged entries and a monolithic board are named as the cases it does not cover.
- **The 2026-09-25 cold pass's other findings.** BA1: the sibling case now has its
  operative sentence in CF3's branch list, and the ADR, `010/020` and `010/030` are
  corrected to say the stop had lived in an interim sentence the 2026-09-20 sweep
  deleted. BA3: the surfaces say *unstaged* where that is the guarantee, and state that
  a peer's *staged* line is this commit's content. BA4: `--rebuild` is the one spelling.
  BA5: this closure of BS1's residual (2026-09-20, `010/020`) was never logged; it is
  here. BA6: the docstring of `tools/board.py` is canonical and the README, roadmap
  README and `CONCURRENCY.md` keep a clause and a pointer. BA7: the docstring names the
  live residuals. BA8: a late closing note on the 2026-09-20 run's record. BA2 (a quoted
  item path dropped from the index plane) was already fixed by `115/260`.

### Changed (2026-11-09 — `ccclose --identifiers` credits a commit only on evidence, `160/960`)
Mike answered *"Credit only on evidence"* (2026-11-09; an answer, not a ruling in his
words) to a cold pass that found the block crediting a concurrent session's
same-subject commit as fact (IE1 to IE14). The Commits line now lists a commit
only where one command of the session or its subagents made it: the subject, the
repo, a result that is not an error and the time must all fit, one command to one
commit; a commit command quoted in a heredoc, grep or echo is no evidence. What
does not fit prints as unconfirmed and says why. Also: subagent merges are
result-checked, the "left out" line is worded as the heuristic it is, a squash
titled like the session's own commit is unconfirmed, a claim a peer closed is no
longer "still open", a left-out squash's board movement is listed apart, unread
subagent transcripts are counted, a message's first paragraph is folded as git
folds it. The limits (worker sessions are not read; a leading comment hides an
item's state line; the under-credit forms) are written into `ccclose.design.md`
§15.1, the man page, the README and `RECORD.md`. The JSON gains fields and
changes no existing meaning; the credited lists are the stricter ones.

### Changed (2026-11-09 — E6d(i) replaced: a repo may lower a check's response, declared and expiring, `020/170`)
Mike answered *"Allow if declared + expiring"* (2026-11-09; his word, picked
from options). Doctrine only; no tool changes.
- **`method/GUARDS.md` § *Provenance, not direction***: a repo may lower a
  check's response only with a written reason and an end date, visible in the
  fleet view; the tool never lowers one on its own judgement. This replaces
  E6d(i)'s "impact may only raise a response, never lower it" wording (also
  noted at E6d(i) in the E6 board item and in `method/README.md`); E6d(ii) and
  (iii) are untouched. A table sets each lowering mechanism against the rule:
  floor `advisory` meets it, floor `disabled` has a reason but no end date,
  `scope` / `flags` are ruled permanent facts, and line markers and ignore
  globs stay acceptances. The two gaps are follow-ups, not built here.

### Changed (2026-11-09 — the shared allow-marker grammar fails closed; the E7 leakscan counsel applied, `160/480` and `160/110`)
Mike answered *"Strict, with a warning period"* (2026-11-09; his word, picked
from options). The reviewers' other counsel is applied as written; the shared
reader in `tools/allowmarker.py` carries most of it, so one edit reaches every
scanner.
- **A malformed scoped marker exempts nothing from 2026-12-09 (AM2, and LK1,
  which is the same finding).** `leakscan:allow:ipv4:` with no reason, a space
  inside a composed scope, a trailing comma, a scope the scanner cannot take:
  each used to be read as the unscoped form with the scope word for a reason,
  and exempted every rule on its line, both boundary guards included. Until
  `MALFORMED_GRACE_UNTIL` (a dated constant, no flag or variable moves it) it
  still does and every run warns on stderr; from the date it is a mention.
  `python3 tools/allowmarker.py --census` lists them. A census of every repo
  with a floor found no live malformed marker, only documentation mentions.
- **A marker inside an inline code span is a mention (AM3).** Every reader
  blanks code spans first; only `stampscan` did before.
- **`reviewscan`'s deferral waiver reads the shared grammar (AM1)**: it was a
  raw substring with no reason, the one hatch the extraction missed. A
  `deferral`-scoped marker no longer also waives check 1 (AM4); `pathscan`
  declares its one kind.
- **A marker naming no rule is counted (AM10)** in `leakscan`, `secretscan`,
  `datescan`, `linkscan` and `spellscan`: `N marker(s) naming no rule` on the
  suppression line and `markers_naming_no_rule` in the JSON.
- **Cleanups.** The scope group is single-sourced, so a reader cannot ask for
  one the pattern lacks (AM8); the two dead `ALLOW_MARKER_RX` constants and the
  stale comment above one are gone (AM7, AM12); the ignore-file headers say
  `fnmatch`, not gitignore (AM6, pinned); the grammar, a scanner by scope table
  and the unit of reuse are in `tools/README.md` § *Allow markers and ignore
  files* (AM5, AM13), and the review-brief skill says to check the review
  worktree carries the subject (AM11). AM9 was already closed by `160/730`'s
  control-character stripping and is now pinned.
- **`leakscan`: LK2** plain and `forms:` terms are compared in Unicode NFC, and
  each line is tried as written and in NFC. **LK3** the derived-form separator
  takes `/` and `+`. **LK6** the path plane no longer honours a marker spelt in
  a filename. **LK4** the staged-path tests skip outside a git work tree. LK5
  was a note for operators and needed no change. The staged-plane reach note
  stays with the principal.

### Added (2026-11-08 — five session-and-ask doctrine additions)
Mike approved the recommendation on each item on 2026-11-09 (his date) as a pick from
options a session offered (an answer, not a ruling in his words). Doctrine
wording only; no scanner or tool changes, and the session-open prompt is untouched.
- **Off-repo concurrency (`360/010`).** `CONCURRENCY.md` § *Beyond the repo*:
  an owner marker on anything launched on a shared host, and the open-of-session
  announcement widened to hosts, long jobs, shared remote files and live
  services; a rate-limited API's lockout is named as a disguised collision.
  A claim that outlives its session stays deferred; no locking protocol.
- **A decision exists before the ask (`320/110`).** `COMMUNICATION.md` §
  *Asking for a ruling*: a settled matter is a record, an open one is a
  decision, absent evidence adds "find out first"; a principal answering the
  frame is evidence against the form.
- **When to ask (`420/010`).** `COMMUNICATION.md` § *When to ask*: sort a
  question by what it blocks, park and proceed on branch-blocking ones, proceed
  on a named assumption only where recoverable, never on a floor item, and away
  as a mode he declares. The harness-notification question stays open.
- **Talk first (`280/050`).** `CONCURRENCY.md` § *Talk first*: talk to decide,
  write to hold; silence sends a session to the orphan-claim rules, and talk-first
  never reaches a cold reviewer. The onramp read order and the propagated floor
  clause are not changed here.
- **A session with no repo (`410/010`).** `RECORD.md` § *A session with no
  repo*: a thin person-level onramp, move to the repo before recording, a plain
  close in the reply, named hand-on routes, and the privacy line travelling with
  any output. The onramp file itself is person-local and not built here.

### Added (2026-11-09 — eight approved doctrine items: five rules, a mechanism guide, a guard declaration pair, and the bidi escape)
Mike picked each from options offered on 2026-11-09 (an answer, not a ruling in
his words). No scanner is added; the one code change is the floor's text seam.
- **Capture, do not compose (`320/030`).** `EVIDENCE.md` §16: a fixture of
  another program's output is captured from it and records what produced it.
- **A check in the same invocation as its act is not a check (`320/390`).**
  `EVIDENCE.md` §17, with a pointer bullet in `CONCURRENCY.md`. Not
  mechanisable, so no guard.
- **A negative needs a positive control first (`380/010`).** `EVIDENCE.md`
  §18; mandatory where the negative authorises an irreversible act.
- **Corroborate from the artefacts; never overwrite a running executable
  (`370/010`).** `DATA-PROTECTION.md`; write a new path and rename.
- **Forbid or make cheap: the side of the boundary the writer is on
  (`320/020`) and who a guard protects from whom (`320/050`).** `GUARDS.md`,
  the second with the pathspec caveat (the paths must be identified, not
  merely foreign). Atelier's own guards are not yet audited against either.
- **Which mechanism a new need should take (`400/010`).** New
  `docs/method/MECHANISMS.md`. The item's premise that the one MCP server is
  third-party was stale (`instruments/browser-fetch/` is in this repo); the
  guide follows the tree.
- **The floor escapes the bidi override and isolate set visibly (`020/350`).**
  `tools/floor.py` `strip_controls` renders U+202A-202E and U+2066-2069 as
  `<U+XXXX>` instead of passing them to the terminal; joiners and zero-width
  spaces are left alone. No local child's config carries any, and the fleet
  report is byte-identical before and after.

### Changed (2026-11-08 — six cold-pass reviews applied as counselled: §9 privacy, the cancelled-run clause, pointing up, the hand-up fixes, stated-bridge pointers, the template history)
Mike approved applying each reviewer's counsel as written on 2026-11-09 (his
date), each item closing when applied with no new Fable re-check. Doctrine
wording and one fleet-view tool; no scanner's blocking behaviour changes.
- **PRINCIPLES §9 prices the time dimension as a privacy cost too (`160/030`).**
  For personal data, record-time trails and by-whom fields joined to identities
  are themselves personal data and a retention limit can make the lawful answer
  *less* dimension; "prefer a dated end-state" is a default, not a licence. §9
  now says it sits beside §6 (which dates the system's own facts), "never
  reached" is softened, and record time is named as a family sized by the same
  question test. The roadmap shorthand "no hard delete" for §9 is softened to
  match the hedged doctrine.
- **The cancelled-run clause (`160/040`).** A re-run now waits for a quiet
  group, because it re-enters the same `cancel-in-progress` group and would
  cancel a concurrent session's in-flight run. The clause is conditional on
  the floor running under `cancel-in-progress` (as atelier's `ci.yml` does; a
  child's caller workflow may not). The all-clear is stated positively:
  conclusion `success` on a run for your own SHA. The "~90 seconds" is "about
  100". **Correction to the 2026-08-09 entry above ("a cancelled floor run is
  not an all-clear"), which stands as written:** it justified keeping
  `cancel-in-progress` by minutes saved, but public-repo Actions runs are free
  (`ci.yml`'s COST NOTE), so no metered minute is saved here. The decision
  survives on `ECONOMICS.md`'s rule that cost hygiene applies regardless of
  meter, and on runner and queue contention; where it saves metered minutes is
  in a private child's caller workflow, which was not examined.
- **Pointing up: the instance no longer says the house had no gap (`160/280`).**
  Correcting the index check to plain `git diff --cached` (PU-1, 2026-08-22)
  made the instance narrative false: the house rule had prescribed a path-blind
  pipe, so the child's compression was faithful and its gap real. The Bearing
  in `CONCURRENCY.md` and § *The instance* in `PROPAGATION.md` now say so, and
  that what was owed upstream was the finding, not a duplicate rule. The PU-2
  note no longer states the reviewer's grounds in the principal's voice. The
  2026-08-22 application itself had no entry; it is added in its own date
  place below.
- **The 2026-09-18 hand-up fixes (`160/310`).**
  - The sync-bookend prose states the measured mechanism: autostash puts dirty
    work back without its index state (a peer's staged files return unstaged),
    and on a collision leaves conflict markers and the change on the shared
    stash stack. Gate 2's reason is corrected (a no-upstream pull gains nothing
    and fails with a hint that invites a wrong repair), the worktree form
    (`git pull --rebase --autostash origin main`) is named, and the onramp
    gains the missing branch: dirty work that is yours is committed or backed
    out first.
  - The drift check is `fetch -q && log --oneline <SHA>..origin/main` in the
    block, the template and `PROPAGATION.md` point 4: a fetch error is no
    result, not no drift, and the remote is assumed to be `origin`. This moves
    the pin the children read; delivery is at each child's next pin bump
    (`030/120`). `skills/create-repo` runs the same form.
  - `tools/pins.py` measures against `origin/main` after a fetch, as a child's
    own check does. A failed fetch exits 2; `--head` keeps the local checkout
    as the explicit offline choice. Pinned by four tests.
  - Verify-the-act says it binds any act whose success the session did not read
    from that act's own output, and names `git ls-remote origin main`. It stays
    behind the block's pointer rather than in the lean block.
  - `COMMUNICATION.md` describes the removed prose plane as history, and says no
    gate covers the readability floor at HEAD. § *Pointing up* gains the duty
    to re-drive a hand-up's mechanism claim before writing it into a method
    file. Two ADRs gain addenda for the drift range.
- **Stated-bridge citations (`160/570`).** The `SECRETS.md` bridge sites cite
  `PRINCIPLES.md` §7 with the phrase (and §5 for the standing-credential
  case), including the third site the phrase-keyed sweep missed; `ACCESS.md`
  gains the same citation, `GLOSSARY.md` gains an entry, and the
  tracked-debt restatement in `SECRETS.md` points at its §5 source.
  `REVIEW.md` V5 says a cross-reference is checked for the rule it reaches,
  not only the file it finds.
- **The template history's framing (`160/940`).** `session-open/README.md`
  says what the history does not show: the first four dates' wrong offset, the
  session counts that differ by two, version 31's unconfirmed recurrence,
  unmarked removals and single-use versions. It no longer presents the
  spellscan exemption as covered by the 2026-07-23 ruling. No published commit
  and no prompt text was touched; the earlier prompt history is not re-reviewed.

### Changed (2026-11-09 — the grace notice reaches the floor's board, a plain title's marker travels, and the grace's removal list is complete, `160/970`)
Mike's answer of 2026-11-09: the cold pass's counsel applied as written.
- **Children: nothing to do, and nothing blocks that did not.** The index a
  child already holds renders as before; the child probe (every repo with a
  floor config, both planes) found no change in any `board` result.
- **The grace notice now shows on the floor's board (PP5).** `board --check`
  prints one `board advisory: N finding(s)` line (1 on a run that accepted an
  old-form index, else 0) and `floor.py` reads it, so a green run that used the
  grace reads `🟡 board enforced (🟡 1 advisory finding(s) — reported, not
  blocking)` instead of a plain tick, in CI and at the hook. The exit code does
  not move. The notice says the end is **2026-11-18 in UTC** (a hook on a UTC+13
  machine flips at 13:00 local that day), that the remedy on the staged plane is
  `--from-index`, and points a `wrapscan` child at `tools/README.md`'s advice to
  scope `wrapscan` off the generated index. When the run also fails for another
  reason it says the ✗ lines are the failure, not the notice.
- **A marker on a plain title's second line travels (PP2).** With no bold span
  the title is the first 70 characters of the paragraph, so a line-two fragment
  is reproduced into the index line; its `allow` marker now travels with it
  instead of being dropped. No existing item is affected. Not taken: restoring
  the head-only title fallback, which would re-title lines in children that have
  rebuilt and turn their index stale.
- **The span is 31 days, not 30 (PP8)**, and "one release" is a date because
  this repo tags none; both are said in the code, and `010/190` carries the
  question to put to the principal.
- **The removal list is complete (PP4).** The `LEGACY` comment in `board.py` and
  `010/190` name everything the grace touches: `today`, `_today_utc`, the
  `_entry` seam, the `escape` parameter, the imports and the test classes whose
  import breaks first.
- **Tests (PP3, PP9):** the end date is pinned; the default-date path runs; the
  legacy renderer is held against stored pre-010/170 output; the indented-only
  rule is asserted; `StagedPlane` turns commit signing off so a host with an
  unreachable signing key no longer errors twelve tests.
- **Stated, not changed (PP6, PP7):** a code span that wraps across lines masks
  what it spans, as the renderer reads it (`_mask_code`); `tools/README.md`
  gains the paragraph rule and the grace's duration.
- **Not done here, routed:** the child list for the cut-off comes from `board`
  on each checkout (PQ1, on `010/190`); the Python version floor (PQ2) and the
  load-bound `test_pins.BoundedMemory` timeout (PQ3) are for their own items.

### Changed (2026-11-09 — `ccclose` reads an ask typed as a slash command's argument, and the harness classification says what it assumes, `160/880`)
Mike's answer of 2026-11-09: the cold pass's counsel applied as written.
- **An ask typed after a slash command is now read (HC1).** `ccclose` stripped
  `<command-args>` along with the command's name, on the ground that none of them
  held a sentence of the principal's; `<command-args>` holds exactly what they
  typed. It is now unwrapped, so the ask is listed and the record counts as a
  turn. A command with empty arguments is still no prompt. `cctranscript` shows
  such a record, and the `--list` label, as `/name args` instead of raw XML
  (`--json` `text` follows).
- **The "only `<browser_instruction>` rides on a real prompt" claim was
  re-driven against the local store (HC2).** It holds: other harness elements
  occur inside prompts only mid-prose, as a mention or a paste, so no per-block
  classification and no wider `JOINED_TAGS`. The census is written into the
  comment, without counts.
- **The two tools' text difference is stated (HC3):** `cctranscript` keeps a
  quoted harness wrapper in a prompt's text (all but `<browser_instruction>`);
  `ccclose` strips every wrapper when it looks for asks. The man page no longer
  says only a block a browser extension "prepends" is removed: a prompt that
  quotes one loses the quote. Counts of `you` taken before 2026-10-16 included
  what is now `harness` (HC12). The `--search` design note gains the departure
  bullet for the harness role, and says it rides in the `prompts+replies`
  layer (HC4). The README's "field set never varies" names its one exception
  (HC11).
- **Tests pin the assumptions (HC5)** in both directions: a lone pasted wrapper,
  a wrapper riding on a prompt, malformed wrappers, a command with arguments,
  and a guard that principal text survives every wrapper strip.
- Not taken: HC7 (regex cost, anchoring), HC8, HC9, HC10 (notes).

### Changed (2026-11-09 — cctranscript's first-prompt column states what a damaged mirror does, and the head-read size is one constant, `160/680`)
Mike's answer of 2026-11-09: the cold pass's counsel applied as written.
- **The "can never change an answer" claim is withdrawn for a damaged mirror
  (FP1).** gzip checks its data only in the trailer, and the first-prompt column
  reads a prefix, so a corrupted prefix that still decodes is trusted: it can
  list wrong or partial text where the whole-file read refuses, and a mirror cut
  off after its first prompt lists that prompt where it used to abort the
  listing. The code comments, the man page (`--from-archive`) and this entry now
  say so. The session you pick still renders through the strict read, which
  refuses. Integrity is `ccarchive --verify`'s job. Not taken: printing a marked
  row instead of aborting when the fallback throws (the pass called it optional,
  and it changes the listing's output).
- **Tests pin both ends (FP2).** A mirror cut off after its first prompt, and a
  damaged prefix that still decodes (level-0 gzip, one byte flipped), are now
  asserted, so the contract is explicit rather than accidental. The partial-line
  comment gives the real reason a cut prefix's last line is dropped.
- **A small mirror with no prompt is inflated once, not twice (FP6, FP5).** When
  the prefix read is the whole file, its strict inflate is the answer. The
  prefix is also out of scope before the fallback inflates the whole file.
- **One named constant for the 64 KB head read (FP7)**, `HEAD_BYTES`, for the
  cwd sniff, `gunzipHead`'s floor and the first-prompt bound. The comment no
  longer carries the archive's counts (FP9).
- **Two stale statements fixed (FP4):** `ccrepo`'s "gzip has no cheap partial
  read" comment and the `ccarchive` charter's line that cctranscript still
  gunzips every mirror for one column.

### Changed (2026-11-09 — four scanner cold passes applied: floor-stamp switch, boundary guards read tracked files, linear email and URL rules, exit contract kept, `160/430`, `160/600`, `160/720`, `160/730`)
Mike's answer of 2026-11-09 ("Approve all 17"): the reviewer's counsel applied as
written, each item closing when applied, with no new Fable re-check. Every
behaviour change below was run against each child's configured scope before it
landed, old tool against new. No child's exit code changed. One child's output
did: the boundary guards now read a tracked `.pyc` under a `__pycache__` folder
there, and the G3 binary gate reports it as a warning that blocks from
2026-11-18 unless the file is listed or untracked.
- **`stampscan --require-floor-stamp` (CU1).** `--require-stamps` certifies that
  some stamped block was compared, not that the floor is stamped; its help and
  README now say so. The new switch exits `2` unless a compared block names the
  floor pair. Under `--json` an unmet demand prints the document with
  `clean: false` and `require_stamps_unmet` (CU2). Nothing wired passes either.
- **`blockscan`'s unmapped-heading report (CU3-CU8).** "N other heading(s)", not
  "top-level"; fences pair by the shared rule (a three-backtick line inside a
  four-backtick fence no longer ends it); a map `path` outside `--root` is a
  config error; heading text and paths are escaped in human output; the
  report's blind spots are stated. CU10 (where the advisory report should land)
  is a ruling and is not applied.
- **The three boundary guards read tracked files under skip-named folders
  (GW1).** `secretscan`, `leakscan` and `conflictscan` pass
  `read_tracked_under_skip=True`: a credential committed at `.vscode/`, `venv/`
  or `node_modules/` no longer passes the whole-tree plane. Every other guard
  keeps its skip. Also in `filewalk`: no yielded path has a symlinked parent
  (GW4), every git call runs with `core.fsmonitor=false` (GW5), and a git that
  fails for a tree carrying a `.git` entry says so once (GW2). Tests pin the
  three behaviours the module relied on with none (GW3), and a shape matrix.
  The README gains `filewalk.py`'s entry and the stale `os.walk` line is fixed
  (GW6); `linkscan`, `reviewscan` and `pointerscan` still walk their own way
  (GW7, on the board).
- **`leakscan`'s `email` rule and `secretscan`'s `basic-auth-url` and `URL_RX`
  are linear (GT1).** A greedy class restarted at every word boundary, so a 1
  MiB line of `1-1-1-…` cost over ten minutes in a blocking hook. `anchoredrx.py`
  tries the original pattern once per run; the matches are the same, proven on a
  fuzzed corpus. A gate is now declared on its rule and the table is derived
  (GT2, GT3); the suites prove every gate necessary over lines generated from
  each rule's own regex, and that no gated rule is case-insensitive unless its
  gate is flag-aware. `test_scanner_rules.py` pins the three rules the two
  scanners copy and runs every rule table through boundary-rich lines at two
  sizes (GT5, GT9); `pathscan`'s scheme-URL regex is listed there as known
  quadratic (`BP9`). The earlier gate speed figures (3x and 4.6x) were measured
  once on a corpus that is not in the repository (GT7).
- **An unreadable file is a broken scan, not a clean one (RT1).** `secretscan`,
  `leakscan`, `datescan`, `spellscan`, `wrapscan` and `sizescan` swallowed the
  error and printed `clean`; they exit `2` with the shared `cannot read` line.
  A file that vanishes mid-walk stays a silent skip. A crash is exit `2` with
  its traceback, not `1` (RT4); an unreadable ignore file is the `cannot read`
  line, not a traceback; a relative target climbing out of `--root` is refused
  (RT7); control and bidi characters are stripped from every `broken` message
  (RT3); `report.advisory_count_line` is the one home of the line `floor.py`
  parses (RT6); and a staged scope that left nothing to scan says so on stderr
  (RT2; the spelling refusals were already in, `115/360`, `160/950`).
  The "copyable alone" claims in eleven places are corrected (RT5), the exit
  contract is stated once in the `report.py` section with pointers (RT10), and
  the review-brief skill gives the re-run invocation that runs (GT6).

### Changed (2026-11-09 — four cold-pass reviews applied: the staged diff, indexscan's date rule, sizescan's hatches, `160/800`, `160/810`, `160/830`, `160/850`)
Mike's answer of 2026-11-09 ("Approve all 17") applied the reviewers' counsel as
written. Scanner changes were run against every child before landing.
- **The staged diff is read by a pinned command (`160/800`).** `git diff` ran
  under whatever the committer's settings said. `diff.suppressBlankEmpty` with
  `diff.interHunkContext` or `GIT_DIFF_OPTS` (which git applies over the
  command line) fused hunks and printed bare blank context lines, so
  `secretscan`, `conflictscan` and `leakscan` all refused a legitimate diff
  with exit 2. The two settings are pinned, `GIT_DIFF_OPTS` is dropped from the
  child's environment, and `--no-relative` keeps paths root-relative from a
  subdirectory. A refusal now says it is not a finding and how to see the raw
  diff, and `floor.py` no longer reads an advisory count off a scanner that
  exited 2 (it reported "the count contract has drifted" beside the real cause).
- **Two kinds of change were invisible to the staged guards.** The filter is now
  `ACMRT`: a regular file that replaces a symlink (or the reverse) is a
  typechange, which `ACMR` never showed to any guard. A `-diff` or `binary`
  attribute staged with a text file made git print "Binary files differ" and no
  line, so a secret in it reached `secretscan` and `conflictscan` (`leakscan`
  already read such a file whole). A path git calls binary whose index copy has
  no NUL in its first 8000 bytes is now read again with `--text`; a genuinely
  binary file is never turned into lines. `diff.<driver>.textconv` is left
  unpinned on purpose, and the reason is recorded beside the command.
- **Not changed, and said so:** the staged plane still holds the whole diff in
  memory (`160/800` SX6): what an over-long staged line should do is a ruling to
  ask for. `leakscan`'s path-name cover for empty, renamed and binary files was
  already built (`G3`) and is now pinned by a test. `--staged --root` naming
  another repo was already refused (`160/950`).
- **`conflictscan` and `leakscan`: one input class moved with `115/300`
  (`160/830`).** The entry above said no exit code moved. An added line holding
  a form feed, vertical tab, NEL, U+2028 or a lone CR before a conflict marker
  was split by `str.splitlines`, so the marker looked like a line of its own
  and was flagged at a wrong number. It is now one line, as in git and on the
  whole-tree plane, so `conflictscan` no longer flags it (exit 1 to 0 on that
  contrived input). `leakscan` keeps its finding at the correct line. Both
  planes' agreement is pinned.
- **`indexscan`'s date rule (`160/810`).** `before=` now scopes the date rule as
  it scopes `unlisted`: a line that links a frozen entry is not date-checked, and
  is counted under `by_before` when it would have fired. A marker whose scope
  names no kind (a typo, `Date-Mismatch:`) exempts nothing and is reported
  `stale-allow`; the first version read it as an `unlisted` exemption. The dated
  line count is the lines judged (an impossible date is not in it). The marker
  count is split by what each exempted (`--json`: `by_allow_marker_kind`). The
  finding names the three causes of a misdated line and says to append the
  marker after the link. The registry's `why` names the date rule.
- **`sizescan` (`160/850`).** An archive store's header marker with a scope the
  tool does not recognise has always exempted the integrity check, as the
  unscoped form does; the docs said it was inert. The docs are corrected, and
  the report now names it under "Unrecognised scope (still exempting)", counts
  it on the `suppressed:` line (a new part, `N unrecognised scope(s) (read as
  unscoped)`) and carries it in `--json` as `unrecognised_scopes`. The
  behaviour itself is left to `115/230`. `RECORD.md` and the tool's docs no
  longer say that prose-shaped cold content is "caught at review": no tool and
  no scheduled review looks for it. The docstring no longer calls the
  2026-10-16 answer a ruling.

### Changed (2026-11-09 — G3 review applied: who allowed it and when, the gate before the ignore file, raw XMP read, `160/980`)
Mike's answers of 2026-11-08 on the cold pass of `020/150`, plus the reviewer's
counsel on the rest. G3 itself still warns only until **2026-11-18, which he
made firm for every child**.
- **Each `.leakscanbinaries` line records who allowed it and when (GM5).** The
  line's comment also carries `by=<principal-ruled|principal-answer|agent>
  session=<id|human> on=<YYYY-MM-DD>`, the exception register's vocabulary. A
  malformed one is a config error. `--binary-entries` prints it on every line
  (`by=agent` plus the session id in a Claude session, `by=CHOOSE` otherwise,
  refused until a person picks). **A line written before this, reason only,
  still loads and prints a warning naming its line; it never blocks.** No date
  makes that a block: that is Mike's to rule, and it sits against the held
  exception register (`110/100`), which would carry the same three fields.
  `--json` gains `binary_provenance`, and the `suppressed:` line a field.
- **A `.leakscanignore` glob no longer skips the gate for a binary (GM9).** The
  gate runs before the ignore file: a tracked binary under a glob needs its
  hash-bound entry like any other. Text and untracked files under a glob are
  skipped as before. On the hook plane too.
- **A PNG `Raw profile type xmp` chunk is decoded and its text scanned (GM4)**,
  like XMP in a JPEG or WebP; it was the one XMP form the text rules never saw.
  A raw `exif`, `iptc` or `xmp` profile that does not decode is reported
  **UNREADABLE** and blocks as `<set>:unknown`.
- **The hook reads the manifest the commit holds (GM12):** the index copy, none
  when the commit holds none. It prints a note when the working copy differs.
- **A manifest path that is absolute or climbs out with `..` is a config error
  (GM6)**; it used to load and sit in the inventory matching nothing.
- **`floor.py` also refuses `--root`, `--terms` and `--staged` in `flags`
  (GM8)**, and abbreviations of them: they re-aim a check, and a repeated
  option keeps its last value. The `_render` docstring no longer claims that
  appending stops displacement. A test now checks that no real scanner flag is
  a prefix of a forbidden one.
- **Wording (GM1, GM3, GM7, GM10, GM13, GM14):** the README and `leakscan.py`
  attribute the grace's option text to the queue run and cite the label Mike
  chose; the sets are said to be data types, with `020/450` as the field-level
  keep; 2026-11-18 is stated as firm; a stale "four arguments" and "after the
  date" are corrected; the tests' Python floor (3.11) is named; and the blanket
  refusal's textual equality and the JPEG walker's unbudgeted linear cost are
  each stated. `allowmarker.read_reasoned_parts` is new (the two places a
  reason can sit, before they are merged); `read_reasoned_lines` is built on
  it and unchanged.

### Changed (2026-11-09 — public records describe a private repo's state by its type only, `260/080`)
- **A new write-time rule for every public record: say what condition a
  private repo was in by its type, not its name.** "A private child was failing
  a check", not the repo's name beside the result. Naming a private repo
  anywhere else, including an act done to it such as a pin bump, stays allowed,
  and the older name-plus-sensitive-posture bar stands beneath it. Forward only:
  the existing mentions are not scrubbed, since pushed history is permanent.
  The estate-internal-context ADR is now accepted (postures A and B rejected,
  C adopted) and the rule is a short paragraph in `docs/method/RECORD.md`
  § The record is public. It is Mike's pick from options a session offered
  (2026-11-08), not a ruling in his words, and the ADR says so. The doctrine
  edit is self-authored, so a rule-4 cold pass is owed. No scanner enforces it;
  the name x posture scanner item can now be re-specified against this line as
  an advisory aid.

### Added (2026-11-09 — doctrine: the principal speaks through three channels, `320/070`)
- **`RECORD.md` gains § *What the principal said arrives three ways*, with two
  rules.** The principal reaches a session by the opening prompt, by mid-turn
  messages and by question-box picks. (1) A mid-turn instruction counts exactly
  like an opening one, and one meant to stand is written down where later
  sessions will see it. (2) Any audit of what he asked says which of the three
  channels it read, because a read of one is a confident negative about the
  rest. The section also carries the finding's own warning: a channel's record
  type is not its authorship (only 43.3% of mid-turn records are human-typed),
  so a corpus must name how it tells his typing from injected text. Grounded in
  the 2026-08-21 estate measurement (24.3% of what he typed arrived mid-turn)
  and in `cctranscript`'s one-channel read (`210/100`). Source: the
  principal's pick of "Adopt both rules" from offered options, 2026-11-08, an
  answer rather than a ruling in his words. `GUARDS.md` § *A rule with no home
  is not a rule* gains a pointer, and `README.md` lists the section.
- **Not done here:** `320/080` (`quotescan`) must build its corpus on this
  section's two halves and land with or after it; `320/100`'s form-based check
  for unquoted attribution is untouched.

### Changed (2026-11-09 — the "when a rule keeps breaking" ladder gains a floor, `020/240`)
- **`docs/method/PROPAGATION.md` § *When a rule keeps breaking* now says what
  every rule is owed and what it has to earn.** The ladder was a remedy for a
  rule that had already broken: stop at the first rung that fits. The
  policy-as-code aim ("enforced and directive") asked whether every rule owes
  both from the start. Answer, recorded as the new subsection *What is owed,
  and what is earned*: framing is owed by every rule up front (rung 1 as a
  design obligation, not a remedy); a mechanism is owed only where its value
  beats its cost, ranked against all other work, with recurrence the usual
  but not the only evidence of value. A check not built is a recorded
  decision, not silence. The ladder's climbing rule is unchanged.
  Mike, 2026-11-09, picked "Written always, checker by value" from options the
  queue run offered; that is an answer, not a ruling, and the text says so. It
  rests on his own words of 2026-11-08 on `115/170`: *"It is about balancing
  importance and priority to do the work that is most valuable"*. No blanket
  check-building follows. Census work (`020/220`) and the framing obligation
  (`020/230`) are not done by this change.

### Changed (2026-11-08 — personal data: the claim made true, one closed list, and who grants, `160/630`)
- **atelier's hard constraint no longer says each personal-data exception is
  "declared where it appears".** The cold pass measured the account name on 27
  lines with no declaration (PI1), so the claim was false. The claim is now
  "listed in one place", and that place exists: `docs/PERSONAL-DATA.md` names
  every exception atelier holds (the account name, the author's full name and
  email, the first name used as the doctrine's voice, and the git author
  identity on every commit), with why it is held, how it was granted and the
  files it may stand in. The principal chose this route from offered options
  (an answer to options, 2026-11-09, not a ruling in his words).
- **The list is closed, and only the principal opens it (PI2).**
  `docs/build/REPO-STANDARD.md` § Personal data and atelier's `CLAUDE.md` now
  say that in a public repo an exception is the principal's alone to grant, in
  his own words; a session that thinks it needs one stops and asks, and an
  allow-marker is not a grant. The flat prohibition now also names other
  people's names, contact details and addresses, which the old sentence
  omitted. "Purpose" has a test (the work cannot be done or understood without
  that very datum; a placeholder, a role or an invented example would fail it),
  and the standard says what happens to an exception found unrecorded, to a
  private repo's exceptions when it widens, and what the scans can and cannot
  judge (PI3, PI8, PI9).
- **A test keeps the list matching the files.** `tools/test_personal_data.py`
  fails the suite if a listed string stands in a tracked file no entry names,
  if an entry names a place its string has left, if a personal-data
  allow-marker stands outside a named place, if the set of entries changes
  without the test changing with it, or if a surface goes back to the old claim.
  One entry (the first name) cannot be pinned to files and says so.
- **One rule across the four passages (PI4, PI5, PI7, PI10).** The child
  templates `docs/build/templates/CLAUDE.md` and `CONTRIBUTING.md` now carry the
  same default, purpose test, recording place and public-repo grant rule, so a
  child reading only its own files gets the whole rule; the estate-detail class
  (hosts, paths, client names) is back, labelled as not PII. The verbatim
  quotation in the standard now opens where his words open. The personal-data
  constraint sits outside the stamped doctrine block, so `stampscan` cannot tell
  an existing child its copy is stale: children created before this date still
  carry the old sentence until someone updates them.
- **The old "shareable-only" framing is gone from the surfaces the cold pass
  found (PI6):** `tools/leakscan.py` (docstring and `--help` description),
  `tools/floor.py` (the registry's reason, which every child's floor prints),
  `tools/README.md`, `tools/secretscan.py`, `commands/scan.md`,
  `commands/install-hook.md`, the create-repo skill, `docs/method/PRINCIPLES.md`
  and `README.md`. Wording only: no scanner behaviour changed, so no child's
  result changes.
- Not changed: making `leakscan` itself refuse a personal-data allow-marker in
  a public repo unless it matches the closed list. The scanner has no notion of
  a repo's visibility or of a list, and the cold pass's counsel was the
  doctrine sentence, so this stays a follow-up.

### Changed (2026-11-08 — the report-up duty: the floor block now carries the privacy rule, `160/300`)
- **The short text every child reads at session start now tells a private repo
  to describe a doctrine problem by its class only.** The `floor` region's
  *Doctrine problems point up* bullet carried the rules that protect the parent
  (name the branch, say it is a hand-up, open the PR, touch only your item) and
  omitted the one that protects the child: atelier is public and a push cannot
  be retracted, so a private repo must not name itself or its contents (hosts,
  clients, secrets) on the branch, PR title, commit subject, PR body or item
  (cold pass RU1, `docs/reviews/2026-09-25-0715-report-up-duty-cold.md`; the
  principal chose "add privacy line now", 2026-11-08). The clause is in the
  canonical `floor` region (`docs/method/PROPAGATION.md`), its stamped copy
  (`docs/build/templates/CLAUDE.md`) and atelier's own `CLAUDE.md` § Hard
  constraints. Children pick it up at their next pin bump, where `stampscan`
  reds a stale copy.
- **Three wording fixes from the same pass (RU8–RU10), all in
  `PROPAGATION.md` § Pointing up:** the "nine findings" sentence now says the
  *first* nine in board section `320` (it holds many more); § The duty names
  section `320` as the home of atelier's own reports; § The route step 1
  points at `docs/roadmap/README.md` for the board's format and rebuild step.
- Not changed, still the principal's: RU2–RU7 and RU12. `blockscan`'s
  subsection blind spot stays filed as `320/340`.

### Changed (2026-11-09 — `/atelier:queue-run` runs the committed prompt, and the cold pass's other findings, `160/900`)
- **The command reads the committed copy of the principal's session-open
  prompt and never the working file, and says so when an edit is pending
  (QK1).** A local-path install loads the clone in place, so uncommitted text
  in the prompt was run with no hook, test or review having seen it. The
  skill now has the run read `git show HEAD:` on the file from the plugin
  root, check `git status --porcelain` on it, and report a pending edit in its
  opening lines; an install that is not a git checkout reads the file and says
  so. The prompt's wording is untouched. The skill also gives the bundled
  doctrine path, `${CLAUDE_PLUGIN_ROOT}/docs/method/CONCURRENCY.md`, for when
  the prompt's `../atelier` path does not resolve (QK3). Mike, 2026-11-08:
  *"Keep edit; read committed only"*.
- **`tools/test_queue_run_single_source.py` sees more (QK9).** List markers,
  emphasis and numbering are stripped before the copy check, so a bullet copied
  without its dash is caught; every paragraph of the skill body must be a known
  delivery job and may name only the two known files, so a new rule or an
  instruction pointed at another file fails; and the committed read, the
  pending-edit warning, the no-checkout case and the bundled doctrine path are
  pinned. A paraphrase is still invisible to it, as the skill header says.
- **Teardown has three legs, and merges before it removes (QK6).**
  `CONCURRENCY.md` § *Orchestrated queue runs* no longer rests on the harness
  notice alone: the notice reaches a live orchestrator only, a worker run as a
  separate session gives none, and a worker that never pushed leaves the only
  copy in its worktree. Merge or push from the worktree path first; the third
  leg is `git worktree list` plus a check for a process still using the
  worktree. `RECORD.md` now points at it.
- **Stale and duplicated statements cut (QK7, QK8, QK10, QK13, QK14).** The
  identifiers list is `RECORD.md`'s alone, with `CONCURRENCY.md` pointing at it;
  two sentences made stale by the command and by the prompt's standing "away"
  paragraph are corrected; the `install-hook` re-run sentence is scoped to
  GitHub installs; `docs/method/README.md` indexes `session-open/`; "adds
  nothing" now reads "adds no rule of its own" where it was stated; a
  threat-model note for the prompt as an instruction channel is in the
  session-open README; and `RECORD.md` gains the addendum clause for the
  identifiers block and a line holding a mid-run push to `main` to the
  full-suite bar (QK2's lesson).

### Fixed (2026-11-09 — the staged guards' positional reader lets git resolve a scope, `115/360`, `160/950`)
- **A `--staged` scope spelt by case or Unicode normalisation differently from
  git's no longer reads clean.** `secretscan`, `leakscan` and `conflictscan`
  filtered the staged diff by comparing each positional's text with git's path
  list. A scope of `Docs` for git's `docs`, or a decomposed (NFD) directory name
  for git's NFC, passes the floor's filesystem `exists()` check on a
  case-folding disk, matched nothing, and the guards printed clean over a staged
  live-shaped secret at the hook (the Fable cold pass's QS1, MAJOR; CI caught it
  only after the push). The reader (`report.resolve_staged_scope`) now asks git
  what each positional names, as one literal root-anchored pathspec against the
  index and the commit's removals, and exits 2 for a positional git does not
  know: a typo, the wrong case, a glob, an unexpanded `~`, a directory the repo
  lacks (QS2). Spelling is normalised with `posixpath` (QS10).
  **What changes for a caller:** a hand-typed `--staged tikii/` or a scope that
  names no tracked path now exits 2 instead of 0. A scope naming tracked paths
  the commit does not touch still passes. The floor never hands the guards a
  missing directory (it blocks first), so no declared scope is turned away.
- **The same reader serves five more staged scanners**, and they inherit the
  change: `datescan`, `sizescan`, `spellscan`, `reviewscan` and `wrapscan`
  call `report.scope_staged` too, so a `--staged` scope naming nothing git
  knows now exits 2 for them as well (their `test_scope_narrows_the_staged_set`
  fixtures now track the directory they narrow to). The floor already skips a
  softenable check whose scope directory is absent, so no declared scope
  changes behaviour.
- **`--root` must be the repo the process runs in (QS3).** The staged diff is
  git's view of the current directory. A cwd in another repo with `--root` here
  read that repo's index under this repo's rules and printed clean; it now
  exits 2. A cwd in a subdirectory of the same repo is fine: positionals are
  root-relative whatever the cwd.
- **`--help` for `paths` and `--root`** says so (QS5); `tools/README.md` now
  describes the reader and its refusals, and "Wiring it in" points scoping at
  the floor's `scope` key rather than at editing the hook (QS6).
- **Tests.** Each guard's `StagedPositionalScope` pins the prefix boundary
  (`docs-extra`), the exact-file positional, the refusals above, a Unicode
  variant, the wrong-repo cwd and a subdirectory cwd (QS4, QU1);
  `test_report.py` and `test_floor.py` pin the reader and the hook-plane case.
  The suite no longer needs Python 3.11 in `test_leakscan.py` or 3.10 in
  `test_allowmarker.py` and `test_pathscan.py`, and the staged-reader fixtures
  no longer inherit the host's commit-signing config (QS9). `test_pins.py`'s
  bounded-memory pins time out at 600 s, a hang guard, instead of 60 s, so a
  loaded machine no longer reds the suite as a memory defect (QU3).

### Added (2026-11-07 — secretscan: an exempt file is still read for a real private key, `115/380`)
- **A file a `.secretscanignore` glob skips now gets one narrow, advisory
  check: real private-key material (`exempt-private-key`).** The scanners' own
  test files are exempt on the promise that their fixtures are fictional, and
  nothing held them to it: on 2026-11-06 a worker put four working private keys
  into `tools/test_secretscan.py`, every check passed, and only a human read
  caught it. The check reads the file (streamed, bounded) for a PEM block with
  any `... PRIVATE KEY` label whose body decodes to a private key's DER outline
  (an `OPENSSH` body to `openssh-key-v1`), and for a base64 run of at least 100
  decoded bytes that decodes to the same outline (PKCS#8, PKCS#1/DSA or SEC1),
  joining the adjacent quoted fragments a Python test writes a key as. A
  header alone, a placeholder or truncated body, a certificate and a public key
  are not hits. It reuses the PEM bound and the DER helpers of `320/790`.
  Every other rule stays skipped for the file, so a reasoned glob works as
  before. **Advisory:** a hit is counted in the existing `secretscan advisory:`
  line and the exit code does not move; the summary line's field set is
  unchanged, and `--disable exempt-private-key` turns it off. On this repo's
  tree it finds nothing. `tools/test_secretscan.py` (`Exempt*`) builds every key
  at test time from `synthetic_private_der`; `tools/README.md` has the section,
  with the known gaps stated.

### Changed (2026-11-06 — secretscan: a public certificate's body no longer trips the entropy net, `320/790`)
- **A PEM `CERTIFICATE` or `PUBLIC KEY` block is exempt from the entropy rule
  as a whole, not just its BEGIN line.** The carve-out was per line, so a fresh
  14-line certificate staged alone gave 8 `[medium/entropy]` findings, and a
  comment cannot go inside a PEM block. A child's only route was a whole-file
  `.secretscanignore`, which blinds every rule to the file. The body lines now
  take the existing public-key carve-out and are counted in the same
  `by public-key line` field, so the summary line keeps its field set. Only the
  entropy rule is suppressed: named and assigned rules still run on every line.
  It fails closed. The block must close with the matching END line within 2048
  body lines; every line between must be pure base64 of at most 76 characters,
  on consecutive file lines; the decoded body must be one DER `SEQUENCE` that
  accounts for every byte and whose first element is itself a `SEQUENCE` (the
  shape a certificate and a public-key record share, and which PKCS#8, PKCS#1
  and SEC1 private keys, opening with an `INTEGER`, do not have; stdlib only,
  a check on shape and not a parse). A private-key header, a stray line, a
  missing END, a private key's body under a certificate header or a forged
  wrapper around a non-DER secret voids the whole block, and a `PRIVATE KEY`
  block is never covered. Each certificate in
  a chain is judged on its own. In `--staged` mode a diff that adds only body
  lines is judged against the index copy of the file, so the enclosing block is
  seen rather than assumed; a file with no candidate line never reads a blob.
  `tools/test_secretscan.py` (`PublicPemBody*`) pins each condition with a case
  that fails on the naive version; `tools/README.md` has the section.

### Fixed (2026-11-03 — ccclose: board ids in board order, `210/370`)
- **`ccclose --identifiers` lists board items in number order.** The lists
  sorted their ids as text, so `160/1000` printed before `160/986`. Each digit
  run now compares as a number, as `board.py` does since `010/200`.

### Fixed (2026-11-03 — ccapple: a missing filter is always exit 2, `210/340`)
- **`ccapple` now checks the filter before it looks for a store.** A search run
  with no filter on a Mac that lacks the store (`messages`, `calendar`,
  `notes`, `photos`) used to exit 1 and name the missing store, when the real
  fault was the missing filter. It now exits 2 and names the filters it needs,
  the same as `contacts`, `reminders` and `home` already did. One shared check,
  `require_filter`, runs in `main()` before any store is resolved, and each
  search function still carries it as its own guard, so the "search, never
  dump" gate is unchanged. A search that does have a filter but no store still
  exits 1. `instruments/test_ccapple.py` runs all seven subcommands under an
  empty `HOME` to pin both statuses (121 cases); the manual's "Search, never
  dump" paragraph says the check comes first.

### Fixed (2026-11-03 — board: item and section numbers sort as numbers, `010/200`)
- **Children: no index changes.** `board.py` sorted section and item file
  names as text, so a `1000-` item would have sorted before `130-` in the
  generated index. It now sorts by the leading number, then the name, on both
  the worktree and the staged plane. Every board today numbers its items at
  one width per directory, so every current index is byte for byte the same;
  the first four-digit number will now land at the end of its section.

### Changed (2026-11-03 — datescan: blockquoted lines report their dating without blocking, `115/090`)
- **Children: no child goes red from this, and some will see a new count.**
  A blockquoted (`>`) line used to be skipped whole, so a relative date in one
  of your own `>` callouts passed unseen. Every check now runs on it, and each
  hit is listed in a `🟡 REPORT-ONLY FINDINGS` block, never in the exit code.
  The board shows `🟡 datescan enforced` with the count. No action is needed;
  read the list, and fix a callout's date the way you would any other.
- **Nothing that blocked stops blocking.** `test_datescan.BlockingSetPinned`
  pins every check that blocked. datescan prints
  `datescan advisory: N finding(s) — reported, not blocking.` on every run,
  zero included, and its floor entry now carries `advisory_count`. `--json`
  keeps `clean` and `findings` for blocking findings, and adds `blocked`,
  `counts` and `advisory`. Measured before landing across the estate: no exit
  code or blocking count moved. A bare "today" with no date cue still passes
  unreported, because as a report it would be a flood; the design note says
  why. Mike's answer of 2026-11-03 ("Carry on to datescan").
  Design: `tools/datescan.off-rules.design.md`.

### Changed (2026-11-03 — leakscan: rules that are off report without blocking, `115/090`)
- **Children: no child goes red from this, and some will see a new count.**
  A rule you turn off with `--disable` (the `flags` entry for leakscan in
  `.atelier-floor.json`) used to drop its hits unseen. It now still runs, and
  each hit is listed in a `🟡 REPORT-ONLY FINDINGS` block, never in the exit
  code. A child that disables a class will start seeing that class's hits, and
  the board shows `🟡 leakscan enforced` with the count. No action is needed;
  read the list, and remove anything that is real personal data.
- **A withdrawn rule reports too.** `diagnosis-key`, the diagnosis/diagnoses
  key withdrawn from the key-context vocabulary for noise, now runs on every
  scan as report-only. `--disable diagnosis-key` is refused (exit 2): it has
  no blocking form to switch off. Exempt a line with
  `leakscan:allow:diagnosis-key: <reason>` if it is noise worth silencing.
- **Nothing that blocked stops blocking.** No rule is demoted, and
  `test_leakscan.BlockingSetPinned` pins every rule that blocked. leakscan
  prints `leakscan advisory: N finding(s) — reported, not blocking.` on every
  run, zero included, and its floor entry now carries `advisory_count`, as
  secretscan's, licenscan's and conflictscan's do. `--json` keeps `clean` and
  `findings` for blocking findings, and adds `blocked`, `counts` and
  `advisory`. Measured before landing across the estate: no exit code moved.
  Mike's answer of 2026-10-16 ("Report-only for off rules") narrows the EI6
  ruling for this case only; `SECRETS.md` § *The boundary's posture* is amended
  to say so. Design: `tools/leakscan.off-rules.design.md`.

### Changed (2026-11-03 — `cctranscript` reads a task notification the same way whichever record carries it, `210/260`)
- **Children: no action.** A background-task notification that the harness
  writes as an `attachment` · `queued_command` record (command mode
  `task-notification`) now shows in `cctranscript` as a grey `harness` turn,
  counted in the header's harness chip and found by `--search` as harness. It
  was invisible before, while the same notification as a user record was shown.
  - It opens **no exchange** and has no ref (`null` in `--json`): this channel
    was never read, so numbering it would shift refs already quoted. Replies
    after it keep counting under the exchange they sit in. The user-record
    notification keeps its number, as `210/250` ruled.
  - Included: only `queued_command` with command mode `task-notification` and
    origin absent or its own. Excluded: a peer's cross-session message, a typed
    prompt, any other attachment type, and any unrecognised mode or origin.
  - `ccclose` needed no code change: it never numbered these, and a new test
    pins that its exchange numbers and ask refs are identical with and without
    such records.

### Changed (2026-11-03 — `datescan`, `reviewscan` and `sizescan` read the staged index at the hook, `320/600` second slice)
- **Children: no action, and one behaviour change at the hook.** On the hook
  plane the last three scanners that read the working tree now run `--staged`,
  as `spellscan` and `wrapscan` did in the first slice; CI's whole-tree read is
  unchanged. This completes `320/600`. Two ends: an unstaged draft on disk no
  longer reds another writer's commit in a shared checkout, and a staged defect
  no longer passes because its disk copy was fixed after `git add`.
  - `datescan --staged` is the line scanners' shape: the staged Markdown file is
    read whole from the index (so fence context is right) and a finding is kept
    only on a line the commit adds.
  - `reviewscan --staged` and `sizescan --check --staged` judge **whole files**
    (a record has its review line; a roadmap holds no completed item; an
    archive store holds no live marker), so an added-lines filter would be the
    wrong unit and would miss a deletion-only edit that drops a review line.
    They judge the whole staged copy of each record, brief, roadmap or archive
    store the commit touches, by the code that judges the disk copy. A file the
    commit does not touch is no longer read at the hook; its state is CI's.
  - Net effect on a green child: none can turn red from this. A file the
    commit does not touch is not read, and a touched file is judged by the
    verdict CI would give it.
  - New shared helper in `report.py`: `staged_paths` (every path the staged
    change adds, copies, modifies or renames to, whether or not it adds a line).

### Changed (2026-11-03 — a scanner's `--selftest` prints only its verdict, `320/690`)
- **Children: no action.** `board`, `datescan`, `pathscan`, `spellscan`,
  `wrapscan`, `conflictscan`, `sizescan` and `stampscan` ran their engine over
  deliberate fixtures and printed the engine's reports in the floor's own
  shape (`✗ conflictscan: 7 finding(s) — commit blocked.` over
  `docs/broken.md`). A CI log then held fixture findings beside real ones, in
  the same stream and with the same glyph, and a child's red run was diagnosed
  from them. The selftest step now prints `selftest OK — <scanner>` and
  nothing else; a failing selftest prints `selftest FAILED — <scanner>` then
  its captured output, each line prefixed `selftest (<scanner>):`. The exit
  codes are unchanged. Shared helper: `report.quiet_selftest`. A test per
  scanner (`tools/test_selftest_quiet.py`) runs the real subprocess and
  asserts the output is that one line.

### Added (2026-11-03 — ccclose counts the scratch folder and flags a refused delete re-routed, `180/170`, `180/180`)
- **A thirteenth check, *Scratch folder empty*.** ccclose reads the session's
  scratch folder from the transcript's environment record and counts the
  files and folders left in it, listing the files. Anything left warns: clear
  it, or name each as a loose end. Empty or gone passes; a transcript with no
  environment record is not applicable. A close had said "the scratch folder
  is clean" over about 98 files.
- **The workaround check flags a refused delete reached by another route.**
  After a delete is refused (a deny rule, the classifier, the principal), a
  later delete that uses only other routes (`rm`, `rmdir`, `unlink`,
  `find -delete`, Python's `rmtree` or `os.remove`, pathlib, Node's `fs`) is
  listed. A retry by the refused route is not. Inline shell commands in the
  parent transcript only; the man page names what it misses.
- `RECORD.md`: a loose end the session cannot clear makes the close "not ready
  until you decide", put through the decision device. `AUTONOMY.md`: a refused
  call is put to the principal, never routed around.

### Added (2026-11-03 — G3 keeps IPTC, XMP and PNG text field by field, `020/450` part 2)
- **A `.leakscanbinaries` line can now keep named IPTC datasets, XMP
  properties and PNG text keywords**, as it already could Exif and GPS fields
  (part 1). Write `<digest>:iptc:By-line,Credit`, `<digest>:xmp:dc:creator`
  or `<digest>:png-text:Author,Creation%20Time`, each under one reason. IPTC
  fields use the IIM dataset names (`iptc:2:250` for one the table lacks,
  `iptc:8BIM-0x03ED` for another Photoshop resource); XMP fields are the
  packet's top-level `prefix:property` names, written in full; PNG text uses
  the chunk keyword with `%XX` for any byte outside `A-Za-z0-9_.-`. Names
  only, never values, in every output. The XMP reader is stdlib expat with
  no DOCTYPE or entity accepted. Anything unreadable is `<set>:unknown` and
  blocks until named; any field present and not named blocks, naming it; a
  field the file lacks is a stale line.
- **Children have until 2026-12-18 to move to field-level lines.** A
  type-level `iptc`, `xmp` or `png-text` line keeps working, with the same
  warning part 1 gave `exif`, until `TYPE_LEVEL_UNTIL`; from that day the set
  blocks until its fields are named. `--binary-entries` prints one line per
  field and re-lists a type-level line's fields. `icc` and `jpeg-comment` have
  no fields and are unchanged. This completes `020/450`.

### Changed (2026-11-03 — `spellscan` and `wrapscan` read the staged index at the hook, `320/600` first slice)
- **Children: no action, and one behaviour change at the hook.** On the hook
  plane `spellscan` and `wrapscan` now run `--staged`: each staged Markdown file
  is read from the git index (whole, so fence context is right) and a finding is
  kept only if it sits on a line the commit adds. Two failures end: an unstaged
  draft on disk no longer reds another writer's commit in a shared checkout, and
  a staged US spelling or over-long line no longer passes because its disk copy
  was fixed after `git add`. Net effect on a green child: none can turn red from
  this, since a file the commit does not touch is no longer read and a staged
  file is read only on its added lines (a defect already in an edited file is
  left to CI, whose whole-tree read is unchanged). New: `spellscan --staged` and
  `wrapscan --staged` (repo-relative scope paths, as for the other staged guards)
  and two shared helpers in `report.py` (`staged_added_by_path`, `staged_blob`).
  `datescan`, `reviewscan` and `sizescan` still read the working tree at the
  hook; they are the item's later slices.

### Changed (2026-11-03 — the repo-local check seam is now in the README and the hook sample, `320/560`)
- **Children: a check of your own already has a home.** `local` in
  `.atelier-floor.json` names a script your repo ships, and the floor runs it in
  your hook and your CI (add-only, fail-closed, visible on the board). It was
  documented only in `floor.py`'s docstring and `REPO-STANDARD.md`, and a child
  filed a hand-up for a capability it already had. `tools/README.md` now carries
  a section with a one-declaration example, and the hook sample's header points
  at it. Documentation only; no behaviour changes.

### Added (2026-11-03 — a `pre-merge-commit` hook, so a clean `git merge --no-ff` runs the hook plane, `115/340`)
- **Children: copy the merge hook beside your `pre-commit`.** Git never ran
  `pre-commit` for the commit a clean `git merge --no-ff` writes, so a queue
  run's merges (and any merge of two branches that were each green) reached
  history with no hook plane having read the combined tree. atelier now ships
  `tools/pre-merge-commit.sample` and a tracked `.githooks/pre-merge-commit`: it
  hands over to the `pre-commit` in the same directory, names no scanner, and
  fails closed if that sibling is missing. To take it, in a repo that tracks
  its hooks: `cp <atelier-path>/.githooks/pre-merge-commit .githooks/ && chmod
  +x .githooks/pre-merge-commit` (a legacy install copies the `.sample` into
  `.git/hooks/`); `create-repo` and `/atelier:install-hook` now do this for new
  installs. Nothing turns red on its own: a repo without the file is as it was.
  `--no-verify` skips it as it skips `pre-commit`. `cherry-pick`, `revert` and
  `rebase` still have no client-side hook that can refuse, so CI is the only
  plane that reads their commits (`docs/method/GUARDS.md` § *Which commits the
  hook plane reaches*). `floorfleet` does not yet report a child missing the
  merge hook.

### Added (2026-11-03 — G3 keeps Exif and GPS metadata field by field, `020/450` part 1)
- **A `.leakscanbinaries` line can now keep named Exif and GPS fields**, not
  just the whole Exif set. Mike, 2026-10-19: *"I did mean fields as in GPS
  versus the camera model. Things like exif, iptc, xmp are data types, nto
  fields"*. Write `<digest>:exif:Make,Model,LensModel  path  # why` and
  `<digest>:gps:GPSLatitude,GPSLongitude  path  # why`. leakscan reads the
  Exif tag numbers (stdlib only, bounded, never the values) and names each
  from the Exif / TIFF / GPS tables; a tag not in the table is written by
  number (`exif:0x9999`), and a block it cannot walk is `exif:unknown`. Any
  field present and not named blocks as `binary-metadata`, naming it; a field
  the file lacks is a stale line. One reason may cover several fields. No
  wildcard, and `gps` alone is refused (list the tags).
- **`--binary-entries` prints one line per Exif or GPS field**, and a note on
  merging fields that share a need into one line.
- **Type-level lines keep working, with a warning, until 2026-12-18.** An
  `exif` line written before this keeps the whole set, GPS included. Until
  that date each scan prints a warning naming the fields the file carries and
  asking for field-level lines; the JSON output carries them under
  `binary_type_level`, and the `suppressed:` line counts them. From 2026-12-18
  such a line keeps nothing and the set blocks. The date is a constant
  (`TYPE_LEVEL_UNTIL`), a month after the G3 grace ends (2026-11-18), with no
  flag or setting to move it. Sets whose fields are not read yet (IPTC, XMP,
  PNG text, JPEG comments, ICC, unknown) are unaffected.
- **Not yet:** IPTC datasets, XMP properties and PNG text keywords as fields,
  which is the remainder of `020/450`.
### Fixed (2026-11-03 — leakscan `nz-phone` no longer reads digit runs inside hex digests, `320/470`)
- **A digit run inside a 16+ character hex run is not a phone number.** The
  rule's `(?<!\d)`/`(?!\d)` lookarounds accepted a hex letter beside the
  digits, so a committed SHA-256 could trip `nz-phone` on a nine-digit run
  between two hex letters. A separator-free match inside such a run is now
  skipped; spaced, dashed, `+64` and bracketed phones are never skipped, so
  prose keeps its reach. A child that dropped all leakscan cover on a digest file with a
  `.leakscanignore` glob can remove the glob.

### Added (2026-11-03 — `conflictscan` reports tool-call markup saved into a file, as an advisory, `320/490`)
- **A new advisory finding, `tool-markup`.** A file written by the harness's
  write tool sometimes ends in the call's own closing markup (a last line of
  just the content tag's closer, then the invoke block's). `conflictscan` now
  reports a column-0 line that is exactly either closing tag, or that starts
  with an opening `invoke name=` or `parameter name=` tag. **Children: read
  this at your pin bump.** It is advisory, not blocking, because the estate
  holds frozen instances (three children carry one or more): it prints
  `conflictscan advisory: N finding(s) — reported, not blocking.` on every run
  (a known zero included), the floor board shows the count, and the exit code
  does not move. A doc that quotes the markup on purpose takes
  `conflictscan:allow: <reason>` after the tag; a frozen record that carries
  the leak takes a reasoned glob in `.conflictscanignore`. This repo exempts
  its two session records that end that way; records are not rewritten.
  The `--json` output gains `blocked`, `counts` and `advisory_over_cap`.

### Fixed (2026-11-03 — `pathscan` no longer reads a child's inlined floor as the child's own tree, `320/610`)
- **Children: no more `[missing-path] method/TOOLBOX.md` on a verbatim floor
  copy.** The floor region names atelier's `method/TOOLBOX.md`, which no child
  can resolve, and an allow-marker in the child's copy reads as drift to the
  hand stamp check. `pathscan` now skips the text between `stamp:begin
  source=docs/method/PROPAGATION.md region=floor` and `stamp:end` in a repo
  that does not hold `docs/method/PROPAGATION.md`; `stampscan` is what checks
  that text. The same path elsewhere in the file still reports, and atelier's
  own tree (which holds the source) is scanned as before. Measured over the
  estate's repos: exactly one finding fewer in each child that stamps the floor.

### Fixed (2026-11-03 — `ccclose --identifiers`: worktrees made in a loop, `210/360`)
- **A loop-made worktree is listed, and a dropped one is counted.** After
  `210/330`, `for n in a b; do git worktree add … /p-$n …; done` was dropped
  silently, so the block under-counted. An add inside a `for` loop over plain
  words (no glob, brace, variable or command substitution) is now expanded once
  per word. Any add still unresolved is counted, and the Worktrees field prints
  one line, "N worktree adds not resolved", so the reader knows to fill them
  in. The line is absent when every add resolved; `--json` carries
  `worktrees.unresolved`. A `-b` branch holding an unresolvable variable is now
  counted too, rather than listed with the raw `$VAR` as its name. No path is
  ever guessed.

### Fixed (2026-11-03 — `ccclose --identifiers`: an unexpanded worktree path, `210/330`)
- **A worktree path held in a shell variable is no longer invented.**
  `W=/abs/path && git worktree add --detach $W origin/main` was listed as
  `<cwd>/$W`, a worktree that never existed. `worktreeAdds` now expands
  `$NAME` / `${NAME}` from a literal assignment earlier in the same command or
  the transcript, as the message-file reader does, and drops an add whose path
  (or `cd` / `-C` directory, for a relative path) it cannot resolve. A prefix
  assignment (`W=/p git worktree add $W`) is not seen by that command's own
  expansion and does not count.

### Fixed (2026-11-03 — `ccclose --identifiers`: backdated commits, `210/320`)
- **Backdated commits: pinned, not changed.** The window already judged a commit
  by its committer date; the reported gap was commits made by a script, which
  no commit command of the session names and which print as unconfirmed. A test
  now holds the committer-date rule against a commit whose author date is 90
  days back. The man page and design note say so.

### Changed (2026-11-03 — a claimed item's index line fits `wrapscan`, and a bracket in a title no longer breaks its link, `320/730` · `320/450` §2)
- **Children: read this at your pin bump.** `board.py` used to print a whole
  `(claimed …, wt: …)` fragment ahead of a 70-column title on the index line,
  so a claimed item's line came out at 170 to 320 columns and a child that
  runs `wrapscan` over its generated `ROADMAP.md` was refused at the commit.
  Children met it (`320/730`, `320/750`); the stopgap (rebuild with the pinned `board.py`)
  only works until the grace ends on 2026-11-18. Now the title is cut at a
  word boundary, with `…`, so no space of the line lies past column 85, and a
  long claim is shown as the date without the time, then with the worktree
  name cut. A short claim is unchanged. The full fragment stays in the item
  file.
- **The line is still over 85 columns, and that is expected.** Every index line
  ends in a store path, and `wrapscan` passes a line whose overflow is one
  unbreakable token. Fitting the spaces is what makes the line pass; the path
  cannot be shortened. If your `wrapscan` scope or version lacks that
  exemption, the line will still be reported, and the choices are yours:
  exempt the generated index from `wrapscan`, or scope `wrapscan` as this repo
  does (`docs/method`, `docs/build`, `docs/decisions`). A worktree name that
  cannot be cut to 8 columns leaves its line over; none is known.
- **Brackets in a bold title** (`320/450` §2). `[` and `]` in a title come out
  as `&#91;` and `&#93;` in the generated link text, which GitHub renders as the
  brackets. Before this, a `]` closed the link early and a `]` followed by `(`
  opened a second link that `linkscan` reported as missing. A rebuild changes
  the index line of any item whose title carries a bracket.
- **Rebuild once after the bump.** `board --check` goes stale on every claimed
  item and every bracketed title until `board --rebuild` is run and staged. The
  grace to 2026-11-18 still accepts the previous projection byte for byte.

### Added (2026-11-01 — `ccapple`, a read-only reader for the Apple apps' local stores)
- **A session can now look things up in the Apple apps.** `instruments/ccapple`
  searches Contacts, Messages, Calendar, Reminders, Notes, Photos and the Home
  layout on a Mac, through the SQLite files iCloud already syncs there. Before,
  a session could name what the operator keeps in those apps and could not open
  any of it. Subcommands: `status`, `contacts`, `messages`, `calendar`,
  `reminders`, `notes`, `photos`, `home`. Manual: `man ccapple` (installed by
  `instruments/install`, with the other pages).
- **The limits are in the code, and tests pin them.** Every store is opened
  read-only and immutable (`mode=ro&immutable=1`, `PRAGMA query_only=ON`) through
  one function. Every search refuses to run without a filter and is capped by
  `--limit` (default 20). A password-protected note is listed and never read or
  decrypted. The Home reader names its columns and never selects the
  credential-shaped ones sitting beside them. There is no write path.
- **First Python instrument, and the first to read other people's private
  content.** Standard-library Python 3.8 or later (exercised on 3.9 and 3.14).
  ADR 0006 has a new addendum recording both stretches and the controls a later
  reader of a personal store should meet. It needs one thing no session can
  grant: Full Disk Access for the terminal, set by the operator in System
  Settings. `ccapple status` says which stores open and why any does not.
- **Tests and CI.** `instruments/test_ccapple.py`, 119 `unittest` cases on
  synthetic stores (no real data), run in CI by a new step beside the Node
  suite: `python3 -m unittest discover -s instruments -p 'test_*.py'`. One test
  pins the `--help`/man-page relation REPO-STANDARD asks for: every flag any
  `--help` prints appears in `man/ccapple.1`.
- **Vocabulary.** `--since`/`--until` take `YYYY-MM-DD` or the compact
  `YYYYMMDD` that `ccrepo` and `cctranscript` use, so the word means one thing;
  `instruments/README.md`'s flag table has a `ccapple` column. Its result cap is
  `--limit`, as in `ccmail --search`.
- **Found while building, not fixed:** a no-filter run on a Mac that lacks the
  store exits 1 rather than 2 (`210/340`).

### Changed (2026-10-19 — one reason may keep several named metadata sets, `020/440`)
- **A `.leakscanbinaries` set line may name several metadata sets under one
  reason:** `<digest>:icc,xmp  path  # why these sets are kept`. Each set is
  named explicitly; there is no wildcard, and any set the file carries that
  no line names still blocks. Mike, 2026-10-19: *"I am fine with one reason
  applying to multiple fields of metadata, but it should be specific e.g.
  fields A, B, and C allowed because of X"*. Two set lines may now share a
  reason; a set line still may not just repeat the file line's reason.
  Nothing changes for a manifest already written one set per line.
  These sets are data types (Exif, XMP, and so on), not the fields he meant:
  his next sentence was *"I did mean fields as in GPS versus the camera
  model"*. The field-level keep is `020/450`, built after this (see the
  entries above) (`160/980` GM3).

### Added (2026-10-18 — leakscan gates binary files, warning only until 2026-11-18, `020/150`)
- **What G3 checks.** `leakscan` no longer skips a tracked binary in
  silence. A binary (an image, PDF, font, archive) needs an entry in
  `.leakscanbinaries` at the repo root that matches its exact bytes, by a
  SHA-256 prefix, with a reason. A changed file needs listing again. PNG,
  JPEG and WebP metadata is sorted into named sets (`exif`, `iptc`, `xmp`,
  `icc`, `png-text`, `jpeg-comment`, `unknown`). Every set the file carries
  needs its own `<digest>:<set>` line, reasoned with the need for keeping
  that set; one blanket reason is refused (Mike's answer, 2026-10-18). Text
  metadata is still scanned by the normal rules. An entry for a file or set
  that is not there is stale. The staged hook now also reads the names of
  binaries, empty new files and pure renames.
- **Nothing blocks before 2026-11-18.** Until then the four G3 findings
  (`binary-unlisted`, `binary-changed`, `binary-metadata`,
  `binary-stale-entry`) print as warnings naming that date and their remedy,
  and the exit code is unchanged. Mike chose a grace period of about 30
  days (the option labelled "Grace period (Recommended)"; the option text
  was the queue run's, not his words); the exact date was the queue run's
  pick, and he made it firm on 2026-11-08 (`160/980`). Every other leakscan
  rule still blocks today, including a personal-data hit in an image's text
  metadata.
- **What each child does, before the cut-off.** Run
  `python3 <atelier>/tools/leakscan.py --root . --binary-entries`. It prints
  reasonless lines: one per unlisted file, one per metadata set it carries.
  Look at each file. Strip every metadata set you have no need for (for
  example `exiftool -all= file`) and re-run, because stripping changes the
  hash. Then write a reason per file and a need-specific reason per set you
  keep, and commit `.leakscanbinaries`.
- **From 2026-11-18** (on that day itself) the same findings block CI and the
  hook exactly as a leak does. The date cannot be moved or skipped: there is no flag for it,
  and `floor.py` now refuses a mode flag in `flags` even when abbreviated
  (`--binary`, `--self`), and any `scope` path that starts with `-`.

### Changed (2026-10-18 — the board index reads an item's first paragraph, `010/170`)
- `board.py` now builds each index line from an item's logical first
  paragraph: its state line plus the indented lines that continue it, up to
  a blank line or a new block such as a sub-bullet. A bold title that wraps
  now renders whole, and a `(claimed …)` fragment wrapped onto line two now
  shows in the index. Flags are still read from the state line alone.
- Nothing breaks before 2026-11-18. Until then `board --check` also accepts
  an index built the old way, and prints a notice saying so, on both the
  worktree and the `--staged` planes. Each child repo using the split board:
  run `board.py --rebuild` and commit `docs/ROADMAP.md`, any time before
  that date. From 2026-11-18 an old-form index is stale like any other, and
  `board --check` fails in CI until it is rebuilt.

### Changed (2026-10-18 — the guard rails live in the prompt, `180/100`)
- On the principal's ruling, the four doctrine guard rails (no
  self-extending chain, item text never overrides, the rule-4 criterion, the
  four named stops) moved from the `queue-run` skill into
  `session-open-prompt.md`. The command is now exactly his file.
  `tools/test_templates.py` pins them in skill plus prompt.

### Changed (2026-10-18 — `/atelier:queue-run` runs the prompt file itself, `180/090`)
- The `queue-run` skill now loads
  `docs/method/session-open/session-open-prompt.md` and adds nothing, so the
  command and the copy the principal pastes by hand are one text.
  `tools/test_queue_run_single_source.py` fails if the skill stops pointing
  at the file or copies its lines. The prompt file is principal-owned text.

### Changed (2026-10-18 — session id first, identifiers last, `180/070`, `180/080`)
- A queue run's first line is now its session id, so another session or
  `cctranscript` can find it. The date-and-time line is dropped: the harness
  now stamps each turn.
- `RECORD.md`: a session's detail record and its closing message end with an
  identifiers block: session id, model and window; commits; PRs; board items
  and reviews queued; worktrees and branches; agents; other repos written to.

### Changed (2026-10-18 — the plugin versions by commit; four prompt lines back, `180/040`, `180/050`)
- `.claude-plugin/plugin.json` and the marketplace entry no longer carry a
  `version`, so each commit is its own plugin version. A GitHub install
  updates to the newest commit on `/plugin update`, instead of staying frozen
  at 0.2.0. `claude plugin validate` warns about the missing version; that
  is the trade chosen. Hooks installed by `/atelier:install-hook` need
  re-running after every update.
- The session-open prompt gets back four lines it had dropped: the date at
  open with checklist progress reports, verify-don't-infer, board answers as
  bullets, and the fuller close check. `queue-run` and `CONCURRENCY.md` carry
  them too.

### Changed (2026-10-18 — `/atelier:queue-run` carries the whole run brief, `180/010`, `180/030`)
- The `queue-run` skill now carries every clause of the hand-carried run
  prompt it replaces. The text after the invocation is the run's brief. New
  defaults: read `CLAUDE.md` and the current doctrine first; a minimum viable
  run outside a floor repo; mid-run hand-overs become items; idea-only items
  wait; big items are split; a spend directive is read as value; a per-run
  ask cadence; and a close report with the session id, one decision at a time,
  and a re-read of every ask. `CONCURRENCY.md` § *Orchestrated queue runs*
  holds the rules; the skill points at them.
- `docs/method/session-open/session-open-prompt.md` is now the prompt text in
  use, with two lines brought back into line with later rulings (state the
  tier and proceed; roadmap close on a split board).
- The README says how to install from a local clone so the doctrine stays
  current: a local-path marketplace loads the plugin in place.

### Changed (2026-10-16 — harness text is not the principal's, `210/250`)
- `cctranscript` no longer counts harness text in user records as your
  prompts. A background task's notification, a meta record and a slash
  command's output echo now have the role `harness`: grey and clipped in the
  render, a separate header count, full text in `--json`. An injected
  browser-instruction block is removed from the prompt it was joined to.
  Harness text keeps its exchange number, so refs already quoted do not
  move. On 12 recent sessions, "you" fell from 181 to 56. `ccclose` shares
  the one classifier.

### Added (2026-10-16 — `ccclose`, the close-out checker, `020/180`)
- `ccclose` checks a session's close from a fresh read of the repo, GitHub
  (through `gh`) and the session's transcript, never from the session's
  memory. It prints the session id, transcript and window, then eleven
  checks: worktrees, branches, pushes, PRs, the session record, the board,
  live claims, the floor at the pushed head (full SHA; a cancelled run is not
  a pass), review pointers, workaround-shaped commands and the working tree.
  It ends by listing the principal's close-out asks from the transcript,
  under *Asked of this close — answer each*.
- Read-only, and usable in any repo: conventions are detected, and an absent
  input prints "not applicable" rather than a pass. Attribution is by the
  transcript window, and that heuristic is printed on every run. Design note
  `instruments/ccclose.design.md`, man page `ccclose(1)`. Not yet installed
  onto the machine's path.

### Fixed (2026-10-16 — the floor's advisory count, `115/320`)
- `floor.py` reads a scanner's advisory count only from that scanner's own
  whole count line, and takes the last one. A file named like the count line
  could make the board read its number off a blocking finding line.
- `conflictscan`, `board` and `licenscan` are pinned as checks a child cannot
  soften, beside the four already pinned, in the selftest and the tests.

### Removed (2026-10-16 — sizescan's size advisory, `115/270` c)
- `sizescan` no longer measures length: the line references,
  `sizescan:budget=N`, and the size-advisory output and JSON fields are gone
  (Mike's ruling, 2026-10-05, no arbitrary size limits; his answer
  2026-10-16, "Remove it"). The cold-content and harvest-integrity gates are
  unchanged and no exit code changes anywhere. Prose-shaped cold content is
  now caught at review only.
- A hatch left with nothing to exempt is reported as inert, in the report,
  in `--json` (`inert_hatches`) and on the `suppressed:` line.
  `size-advisory` stays a retired scope name so a stale scoped marker is
  not read as the unscoped one. Across 29 repos: exit codes unchanged, 28
  advisory lines gone, 2 inert hatches named.

### Changed (2026-10-16 — licenscan's warn is real, `115/290`)
- `licenscan`'s `medium` findings (a permissive header under a different
  permissive licence, an unknown declaration, an unrecognised LICENSE) now
  report in a `🟡 ADVISORY FINDINGS` block at exit 0. `high` findings still
  block. The text had called these a warn while every one counted toward
  exit 1 (Mike's answer, 2026-10-16: make the warning real).
  `licenscan advisory: N finding(s)` prints on every run and the floor board
  reads it as it reads `secretscan`'s; `--json` gains `blocked`, `counts`
  and `response`. Across 29 repos: 6 go red to green, 2 stay red on a `high`
  finding, none goes the other way.
- `pathscan`'s docstring says it is a registry entry (since 2026-08-05), and
  `floor.py`'s "no advisory form by design" names publishscan's exception.

### Fixed (2026-10-16 — staged findings at their real line, `115/300`)
- `conflictscan` and `leakscan` report a staged finding at its real line in
  the file. Both numbered a finding by its position among the file's added
  lines, so a marker staged on line 5 under four unchanged lines was
  reported at line 1. They now use the line number `report.staged_added`
  already yields, as `secretscan` did. Only the number changes: no format,
  rule or exit code moves, and whole-tree output is byte-identical.

### Changed (2026-10-16 — three guard fixes, `115/270`, `115/280`, `320/430`)
- `sizescan`: no hatch silences the cold-content gate any more (Mike's
  2026-10-05 ruling). The gate used to be exempted by an unscoped
  `sizescan:allow` header, a `cold-content` scope or a `.sizescanignore` glob.
  Now it is not, and the report names any such hatch as present but unable to
  exempt. The three still quiet the size advisory. Each flagged file lists its
  completed items as `line N: text`, capped run-wide (`--json`: `cold_listed`,
  `cold_hatches`, `cold_items_over_cap`). The `.sizescanignore` count is real
  now, where before it always printed 0. No exit code changes in any of 30
  repos.
- `secretscan`, `conflictscan` and `leakscan` read the staged diff through one
  structural reader (`report.staged_added`), so an added line that begins
  `++ ` can no longer pose as a file header and hide the lines after it. The
  reader fails closed (exit 2) on a diff it cannot fit, splits on the newline
  byte only, and pins the diff prefixes. Staged output is byte-identical on a
  realistic change set, apart from the findings the hole used to hide.
- `indexscan` gains `date-mismatch`, warn-only: a dated index line that links
  a date-named file must not predate it. It checks only that direction,
  because later-dated lines are legitimate addenda. Slug drift is not checked.
  0 findings in atelier and its siblings.

### Changed (2026-10-05 — allow-markers that name a kind, and finding IDs, `115/080` part 3)
- `licenscan`, `sizescan` and `pointerscan` read a marker's scope and ignored
  it, so any marker exempted every kind. A scope that names one of their kinds
  now exempts that kind only. The unscoped form, and a scope naming none of
  the kinds, exempt exactly what they did before, so no existing marker
  changes meaning. Every other marker form gives byte-identical output in 422
  fixture runs, and 174 runs over 29 real trees are identical. No marker in
  any of those trees names one of the three scanners' kinds.
- Nine scanners end each finding line with `  [<scanner>:<kind>]` and add an
  `id` to each `--json` finding (`ids` in `sizescan`). The kind is the scope
  the scanner's marker accepts, so the ID copies into the narrowest marker.
  Every finding line changes; nothing else in the output does, and no exit
  code changes.

### Added (2026-10-05 — what the first flip's transcripts add to the pre-flip gate, `260/110`)
- `AUTONOMY.md`'s making-public clause gains three lines from `260/090`'s
  harvest. The scrub runs last and covers the gate's own records, including any
  join of a private repo's name to its scan state. A planted canary is
  reconciled shape by shape. The doctrine pin is current at the flip.
- `publishscan --history`, opt-in: the same never-publish rules over every path
  ever added on a branch, tag or remote-tracking ref, each hit reported with
  its oldest adding commit and whether the tip still tracks it. Streamed; a
  shallow clone exits 2. Default output is byte-identical (120 of 120 runs: four
  flag sets over 29 local repos and one fixture, plus the selftest). Round 3 adds `*.egg-info/`, which no sibling
  repo tracked at its tip, so no repo went red.

### Changed (2026-10-05 — one shared exit and reporting contract for the guards, `115/080` part 3)
- `tools/report.py` holds the exit codes (0 clean · 1 blocking findings · 2 the
  scan broke) and the report lines fourteen scanners printed as copies. Every
  per-guard difference is a parameter. Output is byte-identical: 453 of 453
  fixture cases and 38 of 38 real-tree cases. Namespaced finding IDs were
  surveyed and not built, because they would change every finding line.

### Changed (2026-10-05 — leakscan and secretscan: per-rule pre-filters, `110/130`)
- Each rule skips its regex on a line that provably cannot match it, using a
  cheap test its own pattern makes necessary. Output is byte-identical, proven
  by CLI comparison and a 1.15-million-line differential fuzz. It is about 3×
  faster for leakscan and 4.6× for secretscan on a 50 MB corpus. No rule,
  finding, suppression or exit code changed.

### Added (2026-10-05 — the standing reviewer checklist and a test-evidence rule, `200/050`, `200/020`)
- `REVIEW.md` § *The standing checklist*: seven checks every review runs
  unasked (V1–V7, approved 2026-07-23), each pointing at where it is already
  doctrine and at the findings that grounded it. The review skill carries a
  stamped copy.
- `EVIDENCE.md` §15, *A test cannot falsify its own code's assumption*: a test
  that encodes a belief about an external system is evidence of wiring, not of
  correctness, until an authority outside the author's code enters the loop.
  Minted on Mike's ruling of 2026-08-03; he signed off its wording and home on
  2026-10-05.

### Added (2026-10-05 — `indexscan`: a hand-kept index stays true to its directory, `200/010`)
- A new warn-only floor guard. An index opts in with one
  `<!-- indexscan:maps dir=… match=… -->` line, and the guard then reports every
  entry in that directory that the index never names. `exclude=`, `before=` and
  a reasoned per-entry `indexscan:allow:` marker cover deliberate gaps. No
  declaration means no check, so nothing changes for a repo until it opts in.
  atelier declares its decisions, tools, instruments and sessions indexes.

### Changed (2026-10-05 — cctranscript: the first-prompt column reads a prefix, `210/180`)
- `--list --from-archive` finds each mirror's first prompt in a bounded 64 KB
  prefix, and falls back to the whole-file read only when the prefix holds
  none. Output is byte-identical; listing CPU fell from about 27 s to about 7 s
  on one real archive. A corrupt mirror whose first prompt sits in its intact
  prefix now lists a row instead of aborting the listing.

### Added (2026-10-05 — ccarchive: a real calendar schedule, `210/230`)
Mike's ruling: the schedule option comes back as a schedule, not a run at every
login, and his own machine stays manual. In plain terms:
- **`ccarchive --install-schedule [--at HH:MM]`** sets up one run a day at a clock
  time (default 03:00 local). **macOS:** a launchd agent with
  `StartCalendarInterval`, no `RunAtLoad`, no `StartInterval`, no `KeepAlive`;
  launchd runs a slot missed in sleep once on wake. It is loaded with
  `launchctl bootstrap`. **Linux:** a systemd *user* timer and one-shot service
  (`OnCalendar`, `Persistent=true`, so a missed run is caught up), enabled with
  `systemctl --user`. Where `systemctl --user` is unavailable it refuses (exit 2),
  installs nothing and prints a crontab line to paste. Other platforms are refused.
  A `--dest` given at install is baked in; the scheduled run does not see the shell's
  environment. Installing never runs an archive, and lingering is never enabled.
- **`--schedule-status`** (read-only: file, time, loaded/enabled) and
  **`--uninstall-schedule`** (unloads, removes the files, and also removes an older
  login-style agent, saying so). Re-installing unloads the old one first.
- The schedule options are a mode of their own: they refuse to ride along with an
  archive, verify, restore or lock option, and `--at` is validated (two-digit 24-hour
  `HH:MM`) before anything is written. The "removed by name" refusal is gone;
  genuinely unknown options are still refused.
- **Tests cannot reach a real scheduler.** Every `launchctl` / `systemctl` call goes
  through one function; with `CCARCHIVE_SCHEDULER_LOG` set it records the arguments it
  would have run and executes nothing. Every test sets it, plus a throwaway HOME, and
  two tests fail if a scheduler could be reached or a second call site appears.
- The man page gains a SCHEDULING section (both platforms, sleep and missed-run
  behaviour, macOS listing any background job under Login Items → Allow in the
  Background, Linux lingering, uninstalling) and a short DESIGN section of the tool's
  goals, saying encryption is planned and not yet built.

### Changed (2026-10-05 — ccarchive hardening: the archive can no longer lose or overwrite a good copy)
Mike's aim, setting the run: *"I want to be able to rely on it to protect my
session transcript data as I expect it too"*. Built in three parts from the two
cold reviews' findings (`210/210`), in plain terms:
- **Safer writes (part A).** Every write into the archive (mirror, manifest,
  signature, a restored file) goes to a temporary file first and is swapped in, so
  a kill part way can never leave a half-written copy that looks fresh, and an
  iCloud-offloaded mirror is replaced without being read (the cause of every
  failure in the field log, `210/200`). One unreadable file, one bad mirror, no
  longer stops a run: it is named, the rest carries on, and the run exits 1 at the
  end. A run that cannot finish says so in one line and exits 2 (never a stack
  trace). `--restore` checks the archived bytes against the recorded hash before it
  writes. **The schedule installer is gone** (`210/190`): ccarchive installs
  nothing and is run by hand; the old flags are refused by name.
- **A trust model (part B).** The signed index is the record of what ccarchive
  itself wrote. A run checks the index's signature before it writes anything and
  stops, exit 2, if it does not verify (`--rekey` is the deliberate clear). A
  private, signed **intent journal** beside the key lets the next run put back
  exactly the mirrors a killed run had written, and nothing else. Any other file in
  the archive is adopted only if it is byte-identical to the live copy; otherwise it
  is moved to `_untrusted/` (never deleted) and the run exits 1. A **lock**
  stops two runs overlapping, with `--lock-status` to tell a stuck one and
  `--clear-lock` to clear it. Unknown options are refused, so a typo never runs an
  archive.
- **Two kinds of data (part C, Mike's model).** *Transcripts* (and subagent logs,
  prompt history, tool-result sidecars) only ever grow at the end. If one shrinks or
  is rewritten in place, the archived copy is **never** overwritten: the changed
  live version is kept aside under `_anomalies/` (signed), the run says so and exits
  1, and it says "still differs" rather than copying it again on every run;
  `--force` makes the live version current and keeps the old mirror. This retires
  the old behaviour where a same-size rewrite quietly replaced the mirror. *Memory
  notes and subagent metadata* are edited over time: when one changes other than by
  appending, the previous mirror is kept as a dated version under `_versions/`
  (renamed, never read), the new one is current, and the run **exits 0**. That
  closes `210/010` — the daily run no longer goes red every time a memory note is
  condensed. Whether a change is a pure append is tested from the signed entry
  alone (the first recorded-length bytes must hash to the recorded value), without
  reading the mirror.
- **Cheaper, honest runs (part C).** Older index entries (from before a mirror's size
  and time were recorded) are checked once each on ordinary runs, a few per run so a
  run stays quick, and never from an offloaded mirror; progress shows as "N checked,
  M remain". The report now counts what a person recognises (`210/160`): files,
  **sessions** (a top-level `<uuid>.jsonl` only), **subagent transcripts**, a per-kind
  breakdown, what the archive holds in total, and the corrupt count. `--audit`
  checks the index's signature and never calls an unverified index clean; an edited
  memory note shows as `revised`, not drift. The manifest and its signature are now
  swapped so that a kill between them cannot leave a pair that reads as tampered.
- **Docs and tests.** The man page gained ENVIRONMENT (every `CCARCHIVE_*`
  variable, test seams included), KEPT COPIES, a complete EXIT STATUS, an honest
  account of what a thrown error versus a hard kill leaves behind, and a corrected
  ONE BAD FILE; new tests pin the regression shape (`HL11`), a checkpoint test the
  checkpoint can fail (`MC3`), and a drift guard for the environment variables.
  `ccrepo --from-archive` also skips the new `_anomalies/` and `_versions/` areas.

### Changed (2026-09-20 — queue run: the morning rulings, and the guard layer made bounded)
- **Every guard now runs in bounded memory and linear time** (Mike's ruling,
  `020/370`, `020/380`): *"it should not matter how much it scans it should no
  have this affect."* 14 guards and fleet tools measured; the tree-walkers
  stream (`os.walk` with in-place pruning, fixed read chunks, a line window
  with an overlap so a match straddling a cut survives) and findings past a
  fixed cap are **counted, never dropped**. Worst case before → after:
  `secretscan` 432 MB → 52 MB, `datescan` 268 MB → under an 8.5 MB bound,
  `licenscan` and `stampscan` from whole-repo-resident to flat. `board`,
  `pointerscan` and `signscan` were **measured and pinned, not rewritten** —
  their growth is legitimate and linear. The fleet tools take a size gate
  grounded in the file class (largest real `CLAUDE.md` in the estate: 72 KB
  against a 2 MiB cap).
- **The requirement's time clause caught four defects no memory measurement
  would show:** `spellscan`'s path/URL regex backtracked catastrophically
  (107 s on one 1 MB line), `linkscan` ran two quadratic passes (a 20,000-file
  tree did not finish in three minutes; 17 s now), and `harvestscan`'s
  similarity pass is quadratic in item count — split out unfixed as `020/400`
  rather than patched around.
- **`memprobe`** (new): the shared measurement harness every guard's
  bounded-memory test builds on. It measures from a fresh minimal interpreter,
  because a forked child inherits its parent's page accounting on Linux — the
  harness was reading the test process's own footprint back as the child's.
- **`blockscan`** (new, advisory, atelier-only — Mike's ruling, `320/300`):
  a commit that changes a method-doc section the child doctrine block
  summarises must move the block's bullet in both `PROPAGATION.md` and the
  scaffold template, or carry a reasoned allow marker. Deliberately **not** in
  the shared floor registry: every path it names exists only in atelier.
- **`stampscan`** reds a `narrow=` on the inlined floor (Mike's ruling,
  `115/030`) — the scanner's verdicts were inverted against the doctrine.
- **`pathscan`** reads extra resolution roots declared per repo in
  `.atelier-floor.json` (Mike's ruling, `320/010`): a `src/<pkg>` layout was
  three quarters of one child's false positives.
- **Doctrine — the cheapest model that does the job well takes every seat**
  (Mike's ruling, `320/320`): orchestration is no longer reserved for the top
  model, and the run-open check states its tier and proceeds instead of asking
  the principal. Cold review passes keep their principal-named tier.
- **Doctrine — a private child's name stays out of every surface a filing
  creates** (Mike's ruling, `320/190`): branch names, PR titles, commit
  subjects and PR bodies, not just the item text. The report branch form loses
  its repo token.
- **Doctrine — the inlined safety floor is copied verbatim** (Mike's ruling,
  `115/030`): no compression, no declared narrowing.

### Changed (2026-09-18 — queue run: the hand-up fixes and four rulings)
- **plainscan removed** (Mike's ruling, `020/360`): the unwired reply hook
  destroyed, the warn-only floor scanner taken off the registry — it printed
  ~6,050 unread findings per commit. Engine archived at git tag
  `archive/plainscan-2026-09-18`.
- **conflictscan added, enforced** (Mike's ruling, `320/200`): committed
  merge-conflict markers now block on both planes; a bare `=======` counts
  only inside an open conflict.
- **leakscan terms match their plural** (Mike's ruling, `320/240`): `Terms`
  and `Terms'` hit alongside `Term`; `regex:` terms unchanged.
- **secretscan** (`320/290`): a published URL's scheme, host and path are no
  longer entropy candidates (query and fragment still are); `--staged`
  reports the real line on spaced paths and multi-hunk files; the entropy
  regex no longer hides an unrecognised `key=value`.
- **board** takes `--check` / `--rebuild` (bare words still work) and the
  never-soften prose lists are pinned to the registry by a test
  (`010/090`, `020/340`).
- **floorfleet** strips control characters from child floor text
  (`020/060`) and reads atelier's own `main` ruleset, red when force-push or
  deletion blocking is missing (`140/010`).
- **worktree.py**: four defects fixed; `list` measures against
  `origin/<main>` (Mike's ruling, `110/020`). **pins** anchors on the main
  checkout (`210/110`). **pathscan** skips home paths (`320/170`, one class).
  **cctranscript** reads the principal's mid-turn messages without moving any
  published ref (`210/100`).
- **Doctrine:** the child block's ask bullet matches the ruled wording
  (`320/250`); the session-start sync reads `git status` first and needs a
  remote (`320/210`); **Verify the act, not the absence of an error**
  (`320/220`); the drift command reads `..origin/main` after a fetch
  (`320/260`); "self-removing" corrected (`310/110`).

### Fixed (2026-08-22 — the index check shows paths, and the instance is named; entry added 2026-11-08)
Mike ruled the two pointing-up findings on 2026-08-22 and the application landed
without a log entry, so the 2026-08-18 entry below read as the last word on the
index check. Added belatedly on the 2026-09-25 cold pass's counsel (`160/280`).
- **PU-1 — the check is plain `git diff --cached`.** `CONCURRENCY.md` § *The
  trigger* had prescribed `git diff --cached -U0 | grep '^@@'`, a pipe that
  strips the paths the check exists to show. It now says to read the whole
  staged diff, paths included.
- **PU-2 — the repo is named.** The veil over the instance in `PROPAGATION.md`
  and the Bearing in `CONCURRENCY.md` was dropped on his ruling.

### Changed (2026-08-23 — the ruling-round applications: AP and FR, the code half)
- **pathscan excludes records by default, estate-wide** (FR2, Mike's
  ruling): `docs/reviews`, `docs/sessions`, `docs/SESSIONS.md`,
  `docs/ROADMAP-DONE.md` and `CHANGELOG.md` never come clean without
  falsifying the record — the default children inherited pulled them in
  while atelier's own rationale scoped them out. `--include-records`
  widens; an explicitly named records file always scans. Catalogue section
  written (FR1 — pathscan was the one registry scanner `tools/README.md`
  had never heard of).
- **The board strip covers C1** (FR3): U+009B is a one-byte CSI alias some
  terminals honour in UTF-8; the bidi/zero-width set is queued as its own
  decision (`020/350`). Post-strip key collisions now refuse loudly
  instead of silently merging (FR4); a declared disable renders over an
  off-plane skip (FR6).
- **ADR 0008's boundary clause re-worded to the truth by appended
  amendment** (AP1, security): the named controls (branch protection,
  blocking signatures, pre-landing registry review) are not in force; the
  amendment states what is, and the machine-checked boundary is funded at
  `115/180`. Decision 2's softenable list corrected the same way (AP2;
  test-pin queued at `020/340`). The reusable floor workflow routes
  `sign-boundary` through `env:` (AP3); an explicitly set leakscan terms
  path that does not resolve is now an error, never a quieter scan (AP4).
- FR5's count note, recorded not re-measured: the 2026-08-06 entry's
  "eleven children" and "sixteen board rows" count different sets —
  atelier's children vs every discovered fleet row; both stand.

### Changed (2026-08-23 — the ruling-round applications: DA, BW, PT)
- **The ruling-ask doctrine corrected on its own cold pass** (DA rulings,
  applied under Mike's verbatim over-engineering steer): the account must
  have *reached* the principal before the choice is put — the "on screen
  while he decides" spelling was false under focus mode; the briefing
  duty's three sibling spellings and the section's opener now point at the
  apex list instead of restating it; the section moved below the worked
  example; one folded *Make the ask valuable* paragraph carries the
  approved refinements; `EVIDENCE.md` gains the scanner-deltas-compare-
  per-finding line.
- **The board hook's condition said straight on five surfaces** (BW
  rulings): the "only when worktree and index agree" phrasing named the
  state in which the hook *misses*; every spelling now says the hook reads
  the worktree and cannot vouch for a rebuild that ran unstaged. CF3's
  queue test widened to any item's state line; `board.py`'s two residual
  accounts merged; the ADR corrected by appended amendment; the unwind
  list lives in the funded staged-plane item.
- **The fourth guard requirement homed** (PT rulings): the declaration
  lives in the floor registry beside `why`, folded with `115/120` as one
  standard; `GUARDS.md`'s preamble says four requirements; the seven
  three-requirement code banners swept; `PRINCIPLES.md` §10 carries the
  two limits, drops the wrong `ACCESS.md` case pointer, and the two case
  docs (`SECRETS.md`, `DATA-PROTECTION.md`) now point up per the ruled
  stamped-copies half.
- **Belated entry for the 2026-08-17 posture landing** (PT6): `PRINCIPLES.md`
  §10 (posture — strength is what you are free to do) and `GUARDS.md`'s
  fourth requirement landed 2026-08-17 without a CHANGELOG entry, against
  convention; recorded here rather than backdated.

### Added (2026-08-18 — `PROPAGATION.md` § *Pointing up*: the child-to-parent route)
- **The route a child takes when it earns a rule the house owns.** The doctrine
  said children point up and never said *where*, so the only loaded surface a
  child session could reach was its own onramp. Four parts: **check the
  parent's actual file first, never your own inlined block**; a whose-rule-is-it
  test; a four-step route (file the finding in atelier's board · carry the class
  and never a private child's specifics · keep at most one repo-shaped
  pending-upstream line naming the parent item · put the incident in the child's
  own record); and the close, where that line becomes a pointer at the child's
  next pin bump.
- Mike commissioned it 2026-08-18 and ruled the child-side allowance the same
  day: **one line rather than nothing**, because forbidding the local write
  without removing the exposure that causes it leaves the child knowingly
  unprotected between learning and landing.
- Stated in the section itself: it is **rung 1 until something enumerates it**.
  `floorfleet.py` and `pins.py` answer *is this child current*; nothing answers
  *is anything owed to the house*. The instrument is funded as its own item.
- `GUARDS.md` § *A rule with no home is not a rule* gains the cross-repo
  pointer — its "queue the homing" clause is what a child session reads at the
  moment this decision is made, and it did not say the home may be elsewhere.

### Fixed (2026-08-18 — the canonical child block's index rule was lossy and mis-pointed)
- The block's concurrency bullet said *read the staged hunk headers before every
  commit* and pointed at `CONCURRENCY.md` § *The channel*. The phrase reads as
  covering only what you staged; the rule lives in § *The trigger*. A child
  session reasoned from that compression, concluded the house had a gap it does
  not have, and authored ~300 words of duplicate rule marked owed upstream —
  the instance that produced § *Pointing up*. Both defects fixed in
  `PROPAGATION.md` and in `docs/build/templates/CLAUDE.md`.
- `CONCURRENCY.md` § *The trigger* gains the clause the compression dropped:
  read `git diff --cached` as the **whole index, not your own hunks**, and a
  stale entry needs no live peer — an index outlives the ref that fed it, so a
  path staged before you opened or left behind by a peer's `update-ref` landing
  is still there to be committed under your message. Bearing added.
- **Ten children carry both defects** (swept, not estimated) and clear them at
  their own next pin bump; no new occasion invented.

### Changed (2026-08-17 — BS1 ruled: the hook-plane board guarantee, said plainly)
- The four surfaces that said a stale roadmap index *cannot* be committed
  (`tools/board.py` docstring, `tools/README.md`, `docs/method/CONCURRENCY.md`
  § *On a split board*, the board-store ADR by appended amendment) now say it
  is caught **on CI unconditionally, and at the hook only when worktree and
  index agree** — the hook-plane check reads the worktree, so a
  rebuilt-but-unstaged index and a rebuild that absorbed a sibling's dirty
  item line both pass the hook (BS1, cold pass 2026-08-15; the principal's
  ruling 2026-08-17). CONCURRENCY adds: a dirty sibling item state line is a
  stop for claiming from that checkout. The staged-plane check (`010/020`) is
  funded as the fix.

### Added (2026-08-17 — `coldsweep`, the cold-sweep exclusion guard)
- `tools/coldsweep.py` — the tree search a rule-4 cold reviewer runs, with
  `REVIEW.md` rule 2's barred paths (`docs/SESSIONS.md`, `docs/sessions/`,
  `docs/ROADMAP-DONE.md`, `docs/reviews/`) excluded by **default**. The wide
  sweep is `--include-barred` and prints a disclosure banner. Not a floor
  check and not in the registry: it gates no commit.
- Built on the principal's ruling (2026-08-17) after the exclusion defect's
  **third** recorded instance — a hand-written exclusion compared as a text
  prefix against output whose prefix is a platform detail, so the bar matched
  nothing and the sweep ran wide open. The rule had been restated after each
  instance. `coldsweep` filters on relative path **parts** instead, so every
  spelling of a barred path bars the same files and a same-prefix sibling
  directory is not swept up; both directions pinned by tests (20 tests).
- Exit codes follow `grep`: 0 matched, 1 no match, 2 the search failed.

### Changed (2026-08-17 — Mike's ruling round on the cold-run findings)
- `docs/method/REVIEW.md` rule 4 states what the named review tier binds — the
  judgement that forms findings, not every hand a pass passes through. A
  reviewer is on the tier without exception; an orchestrator holding the
  context partition, the sibling release and the commits may be off-tier, on
  two binding conditions: it forms no finding and writes no severity, and the
  arrangement is disclosed in the claim, the pointer and the verdict.
- `docs/method/00-APEX.md` gains the always-confirm-floor exception to the
  extracted-approval rule: at the floor, an extracted approval is re-briefed
  **before** the irreversible action, never challenged after it. Restated in
  `REVIEW.md` rule 3, the `PROPAGATION.md` floor block and the byte-identical
  `docs/build/templates/CLAUDE.md` stamp.
- `docs/method/RECORD.md` gains § *An approval is not the whole ruling* — when
  a recommendation is approved with reservations, the reservations go into the
  record beside the approval and each becomes a check the build must answer.
  `docs/method/GUARDS.md` gains its class, § *A rule with no home is not a
  rule*. `COMMUNICATION.md` keeps the grounded instance and points at both.

### Fixed (2026-08-17 — the board generator writes for the repo it lives in)
- `tools/board.py` emitted `tools/board.py` into three strings a **child**
  reads: the index banner, the index preamble and the stale-index remedy the
  check prints. Children call the floor's tools and never vendor them
  (ADR 0008), so all three named a file that is not there — including the one
  instruction at the top of the one file readers are told never to hand-edit.
  The rebuild instruction is now resolved per root: repo-relative where the
  tool sits inside the tree it rebuilds, the hook's own `$ATELIER_TOOLS`
  spelling where it does not, and never an absolute path (a machine-local fact
  has no business in a file that may be public). The banner names no path at
  all and drops 115 → 69 columns.
- The index no longer repeats a section's path as its link **text**
  (`*[Narrative](…)*`, not `*Narrative: [<dir>/README.md](…)*`), which
  `pathscan` resolved: 28 false findings per commit here, 49 in the first
  child, on every commit, warn-only — a check that always fires is a check
  nobody reads. The `##` heading above already names the section.
- The `GENERATED` marker is matched as a prefix against **both** spellings, in
  `board.py` and `pointerscan.py`, so no repo needs a flag day; an index built
  before today keeps its pointerscan skip until its next rebuild.
- Eye-flags and the claim fragment now render **before** the link, not after
  it. `wrapscan` exempts a line whose overflow is one unbreakable token, and an
  item line ends in a store path — so a trailing ` 🎯` put a space after that
  path, the overflow gained a legal wrap point, and the exemption stopped
  applying. In the first child, 13 of the index's 14 findings were exactly its
  13 flagged lines. The 14th was the preamble, now wrapped at the house width.
  A reader also gains a flag column that aligns.
- Net effect: the generated index passes `wrapscan` **and** `pathscan`
  unscoped, in a repo with no `scope` block and no ignore file. `faves` can
  delete the `.wrapscanignore`/`.pathscanignore` pair it opened to land its
  split; `ros` and `shed` never write one. The floor-policy question this was
  heading for — whether a `GENERATED` marker exempts a file from the prose
  gates fleet-wide — is not needed for the board and is not asked.
- Found by `faves`, the first child to adopt the split board, which had
  papered over the first defect with a delegating shim. That shim can go.
- **Corrected 2026-11-09 (`160/220`, BG4, BG9, BG10).** The entry above is
  kept as written; four of its claims were wrong or have been overtaken. The
  child spelling it gives (`$ATELIER_TOOLS` alone) was replaced within the hour
  by the hook's resolution order. "Passes `wrapscan` unscoped, in any repo" is
  true of the renderer's output except for an item carrying a sibling scanner's
  allow-marker and no `wrapscan:allow`, which `tools/README.md` now states and
  `test_board.py` pins. The `pathscan` finding left over (`F1/GUARDS.md`) was a
  false positive from a title fragment, not "a real stale path". And "28 false
  findings per commit here" was a hand run: this repo scopes `pathscan` away
  from the index, so the per-commit cost was the first child's, not this one's.

### Changed (2026-08-15 — the principal's authority is absolute; his rulings are conditioned)
- `00-APEX.md` § "The principal's authority is conditioned on being informed"
  is retitled *"The principal's authority is absolute; his rulings are
  conditioned on being informed"* and corrected (Mike's ruling, 2026-08-15):
  the earlier text put the condition on the *authority* ("not exercisable
  uninformed"). Now: the authority is absolute and never decays — the agent
  can never overrule the principal, in any situation, including one where it
  believes him uninformed. What being informed conditions is the *ruling*:
  a ruling the agent asked for is challengeable on whether the principal
  was informed, and even an informed ruling stays challengeable by an
  independent review session; a challenge is raised *to* the principal by
  re-briefing, never by declining to obey. An "extracted approval" now
  stands as the principal's word but is open to challenge — no longer "not
  a decision the doctrine recognises". Restatements aligned: `RECORD.md`,
  `AUTONOMY.md`, `CONCURRENCY.md`, `REVIEW.md` rule 3, and the child floor
  block in `PROPAGATION.md` + `build/templates/CLAUDE.md` (stampscan:
  identical). Children pick the floor change up at their next pin bump.
- **"Surface a genuine dilemma; never silently resolve it" is restored as
  honesty doctrine** (Mike's ruling, 2026-08-15, in the same sitting). It
  had left with the Laws caveat that carried it; it now lives in `00-APEX.md`
  § "Honesty is absolute" as an in-practice bullet — a fork quietly picked on
  the principal's behalf is a withheld choice, and withholding is dishonesty
  ("the truth, the whole truth, and nothing but the truth"). Restored to the
  child floor block, the template stamp, and the `session-onramp` skill under
  the honesty bullet, not a Laws one.

### Removed (2026-08-15 — the Three Laws and the Zeroth leave the apex)
- `00-APEX.md` § "Then the Laws" deleted in full (Mike's ruling: intent
  stated 2026-08-04, executed 2026-08-15). The apex is now **honesty, then
  adaptation** — the level-0 frame is a duo, not a trio. Every restatement
  surface swept: `README.md`, `method/README.md`, `GLOSSARY.md`,
  `PRINCIPLES.md` (§0 intro + precedence ladder), `PROPAGATION.md`
  (fail-safe line, SR2 concern list, the inlined child floor block), the
  byte-identical `build/templates/CLAUDE.md` stamp, and the
  `session-onramp` skill. The floor block's "surface a genuine dilemma"
  line left with the Laws caveat it summarised — and was restored the same
  day as honesty doctrine (entry above). Children's floor blocks
  shed the Laws sentence at their next pin bump (same propagation lane).
  *(Correction, 2026-11-09, `020/215` LR4: that was a convention, not
  behaviour. Nothing enforced the shedding and a pin bump with no re-copy
  reddened nowhere; children are due to shed it, and `tools/pins.py` now
  reports each child's floor copy against the floor at its own pin.)*
  The Laws-ladder raw note is closed as *not required*, kept in full.
  Historical records and review verdicts are untouched — every history
  layer (git, session logs, closed board items) keeps the Laws' full
  story: they were there, and they were removed. (Mike's clarification,
  2026-08-15: history is kept everywhere it is recorded, not git alone.)

### Changed (2026-08-15 — the board store: one file per item, a generated index)
- `docs/ROADMAP.md` (4,063 lines) split to one file per item under
  `docs/roadmap/<section>/` with section narrative in per-section READMEs;
  `ROADMAP.md` is now a ~250-line **generated index** (board-store ADR,
  Mike ruled 2026-08-15). All 4,063 lines accounted for in the move;
  linkscan and harvestscan clean across it.
- New `tools/board.py` (+13 tests): index generator + item-file validator,
  registered as the enforced `board` floor check on both planes — a stale
  index blocks with the remedy printed; repos without `docs/roadmap/` pass
  as out-of-scope, said aloud.
- `harvestscan` watches the board directory (a watched store may be a
  directory, expanded at the OLD revision so a deleted item file is
  enumerated, not skipped; +3 tests). `pointerscan` reads item files by
  directory and skips the generated index.
- `docs/ROADMAP-DONE.md` frozen: a done item now stays in its own file as
  `[x]`; the harvest step and its red-window failure mode are retired.
- Doctrine moved with the mechanism (RECORD.md board section, CONCURRENCY.md
  claiming on a split board, CLAUDE.md read order, board README legend).

### Fixed (2026-08-10 — pathscan no longer invents a truncated path)
The first defect a child repo has reported to this board under Track F's
queue-never-deliver rule, closed in the repo that owns the code while the
reporting repo left its 14 lines flagging. **The reported diagnosis was wrong
and the correction is the more useful half:** `faves` named dot-directories,
and its repro supported that reading because `/.well-known/security.txt` was
the only shape it had. The trigger is a **hyphen**, anywhere before the
token's last `/` — `/docs/some-dir/x.md` truncates to `dir/x.md` with no dot
in it. `_PATH_TOKEN`'s lookbehind excluded `\w`, `.`, `/`, `*` and `?` but not
`-`, while the token class accepted `-`; since a run of token characters can
only be blocked at its start by a preceding `/`, the hyphen was the one place
a match could resync mid-token and emit a path nobody wrote. The header had
always claimed leading-`/` mentions are skipped, and that was true only of
paths with no hyphen — which is why the class hid behind a bullet that read as
correct. The invariant is now stated where it binds: **the lookbehind must
exclude every character the token class accepts, plus `/`** — the same hole,
and the same fix, as the `*`/`?` exclusion two lines above it. On this repo's
own corpus 8 findings dropped, 208 → 200, every one the defect: six
`repo/SKILL.md` from `~/.claude/skills/create-repo/SKILL.md`, one
`plugin/plugin.json` from a just-blanked `<plugin-path>` placeholder — the
exact case the header names as skipped and which was not — and
`known/security.txt` from the E8 board entry itself, the bug report being
mangled by the bug it reported. The gated doctrine surface was and stayed
clean. Root-anchored paths are still skipped **whole**, so a genuinely broken
one still goes unflagged; that named false negative is unchanged and now
carries a test that says so, because the defect was the truncation and never
the skip. Module tests 76 → 86, suite 1284 → 1294.

### Added (2026-08-09 — cctranscript can search every transcript)
Mike asked for this on 2026-07-26 — *"something that lets you search all the
transcripts using regex or for a simple term"* — and the design pass settled it
on 2026-07-27 leaving no decision open for him. `--search`, with
`--regex`/`--case`, `--since`/`--until`, `--top` and `--materialise`. The shape
follows the measurements rather than intuition: a whole-file regex **gate**
first, so a file that misses is never parsed; `/i` case-folding, which is free,
instead of lowercasing the text, which is not; and **no index**. latin1 decoding
is the fastest option of all and is rejected outright, because it silently
corrupts macrons and this estate writes te reo Māori with them — a test pins
`Māori`/`tohutō` matching while `Maori` does not. Tests 38 → 62.
**DONE condition 13 is only partially met, and the design was wrong about why:**
its claim that the `N.M` refs are free does not hold at file grain, since a ref
counts every preceding turn — so parse-only-the-survivors and exact refs are
mutually exclusive. Correctness won, a file passing the gate is parsed whole,
and the honest numbers are 1.22–1.32× a bare read for a selective term against
3.7× for one present in every session. The flaky wall-clock guard became a
structural one. A second unmentioned defect: the raw-JSON gate could miss an
escaped spelling of a term (6 escaped `ā` in the live store against 6,698 raw),
so literal terms now gate on an alternation of every form the term can take and
match against the decoded text. The build also closes the design's named
doctrinal loose end — `instruments/README.md`'s `--materialise` note argued the
flag's *absence* from cctranscript was principled because it never read every
file, and `--search` **is** the bulk read, so the note now states the
flags-follow-operation rule in both directions. Rule-4 pointer queued at
landing; the item itself said review was warranted at the design-to-build move.

### Fixed (2026-08-09 — worktree.py works from inside a worktree)
The tool that is CONCURRENCY.md as a command failed at the one cwd an operator
is most likely to be in when they land work. From inside a linked worktree,
`list` labelled that worktree's branch `main` and showed no ahead/behind,
`land <feature>` said `no worktree found`, and `start` produced
`<repo>-<old-feature>-<new-feature>`. **The recorded diagnosis was wrong and
the correction is the more useful half:** the branch was already per-worktree
and already right — what came from the cwd was *repo identity*, because
`toplevel(Path.cwd())` answers "which checkout am I in" and three sites spent
it as "which repo is this". The ahead/behind counts were likewise never
dropped, only suppressed, since `render_list` gates the `↑/↓` flag on
`not is_main`. Identity now comes from the first entry of `git worktree list
--porcelain`. Separately, `remove`'s merged-guard asked a ref a direct push
never moves (`git branch --merged <local main>`), refusing branches that
`merge-base --is-ancestor HEAD origin/main` confirms are contained — which
teaches `--force` as the routine escape from a safety check. The referent is
now `origin/<main>` then local `<main>`, each verified real, an empty ref list
meaning **not merged**, and no network by default. One fail-open the switch
would have introduced was caught in the same pass: a detached worktree's branch
reads as the literal `"HEAD"`, which `merge-base` would have resolved in the
main tree and called merged. Tests 12 → 27 on the module, suite 1222 → 1237.
Five pre-existing defects the fix surfaced were queued rather than taken.

### Added (2026-08-09 — the subagent metadata sidecar is archived)
Mike ruled this a new capture class on 2026-07-28 and it is now built.
Every `<uuid>/subagents/agent-<id>.jsonl` has a sidecar recording facts that
exist nowhere else: `toolUseId`, the join key back to the spawning `tool_use`
block in the parent session log; `spawnDepth`/`parentAgentId`, which resolve
the nesting ambiguity cctranscript's own finished-agents comment names; and
`model`, the tier an agent actually ran on — the fact the queue-run tier
discipline is asserted against, held in one copy on a disk with a pruning
clock. The new `subagent-meta` class is scoped to `subagents/` rather than
name-matched at any depth: the allowlist admits **known** classes and leaves
the unrecognised out visibly, and the cost of the narrow reading is recorded
with it. Two of the item's five build notes needed no code at all — restore
mapping and manifest/integrity fall out of keying everything on `<rel>.gz` —
and both were proved rather than reasoned. The shrink guard turns out to be
**inert** on this class (0 of 545 sidecars rewritten more than a second after
creation), so no size or class exception was carved into a working guard for
an event never observed. The backfill needs no code either, verified with a
sidecar whose mtime was backdated a year and still taken on the next ordinary
run. Tests 95 → 99, `mandoc -T lint` clean, no new flags. Every recorded
figure was stale in the same direction — 425 → 545 sidecars, 66 KB → 85.8 KB
— with the census shape intact, which is the sweep-never-adjust rule paying
out again.

### Fixed (2026-08-09 — secretscan's last invisible subtraction is counted)
`PUBLIC_KEY_RX` skips a line's entropy pass entirely, the deliberate carve-out
that stops an SSH public key reading as a credential. It predated the GUARDS
counted-suppression model, so the lines it wrote off appeared in no tally.
Whether the finding was still true was the crux, because the clean line
already ended `1 public-key fingerprint(s)` — a *different* subtraction (E3's
whole-shape carve-out, counted inside the entropy loop). Settled by probe, not
by reading: the same 68-char body naming `ssh-ed25519` went clean with every
tally at zero, while the bare control returned a blocking finding. A blocking
finding vanished and no number moved — the exact state GUARDS rule (b) exists
to forbid. On this tree it was hiding **two** real suppressions, both genuine
SSH allowed-signers keys. The carve-out now sits inside the span loop so it
can count what it writes off; the suppression itself is byte-identical. The
new field is **appended** and prints at zero, because two runs of this board
get read side by side. Tests 122 → 134; suite 1210 → 1222.

### Changed (2026-08-09 — the parent states its own reasons, and two stale items close)
`GUARDS.md` rule (c) binds atelier identically to any child, and atelier's own
`scope` block had been narrowing three checks with no reason travelling with
the declaration. Migrated to the reasoned spelling — which also clears the
atelier-side precondition C1b phase 2 names, since the legacy bare-list form
cannot carry a `why` at all. The reasons were **lifted, never invented**: WS1's
2026-07-23 option-A ruling with its measured ~6:1 noise-to-signal, Mike's
2026-07-23 frozen-history ruling, and PS4's records-named-out ground. Each
declaration also states what cover is given up, the half a scope declaration
usually omits. Alongside it, two `[ ]` items that the tree had already closed
came off the hot path — the spellscan reason class (fixed at the class in
`8276a54`; re-enumerated at HEAD as 14 regex sites across 12 scanners rather
than taken on the commit message's word) and the floor-local-seam verdict
pointer, which had **diagnosed itself** as residue in its own text and still
sat there as `[ ] 🎯`, inflating the count of rulings Mike was said to owe.
Naming residue is not clearing it.

### Fixed (2026-08-09 — an allowance reason may open with a quote)
Found by the estate exception audit, from a live failure rather than a read:
a PUBLIC child's floor went red on a line whose allow-marker read correctly
to every human who had reviewed it — `# leakscan:allow: "2 Lane" is a PCIe
lane count, not an NZ street address`. The reason's first character had to
match `\w`, so a leading quote made the marker unparseable and the finding
still blocked — **silently**, because a voided marker and an absent one
produce identical output. Quoting the flagged token is the clearest way to
write these reasons, and the rule punished exactly that phrasing; nine live
markers across three children were void this way. Fixed at the class rather
than the instance: all 12 scanners carried the same `\w` and all 12 change
together (14 regex sites), admitting straight and typographic opening
quotes. What the `\w` protected is kept, and is why this is not a widening
to `\S` — a documentation mention must never read as a live exemption, so
`<!-- datescan:allow: -->`, `leakscan:allow: <reason>` and a bare
`leakscan:allow:` all still exempt nothing. 1210 tests green. The audit
lesson recorded with it: **reading an allowance's reason checks rule (c) and
nothing else** — whether it actually suppresses is a separate question the
estate had no way to ask.

### Added (2026-08-09 — who is a child, and where work lands)
Mike ruled both halves during the estate-wide duplication and exception
audit, and neither was written down — which is how one restated doctrine
survived in four children while every one of them passed every check.
`PROPAGATION.md` § *layer-override* now states that **adoption is the
default**: every repo the principal works an agent in is an atelier child
unless he rules a specific exclusion, so the enumerating boards' denominator
is every repo he uses rather than every repo already wired. And it splits
what a child may hold into three verbs — **add** freely, **never repeat**
(a restatement is a second original that drifts silently; point up, or use
a stamped copy), **never conflict** unless the principal rules a specific
exemption recorded in the child. That last lane was missing: the existing
bullets could express an unresolved contradiction but not a ruled one, so a
deliberate exemption read as drift to the next session. `CONCURRENCY.md`
§ *Stay in your lane* gains work-locality, sharpening its existing
another-repo fence rather than minting a second original: a fix lands in a
session working that repo, never delivered sideways by the session that
found it — but the finder **may queue** the finding and its proposed fix in
that repo's own roadmap. Queue, never deliver.

### Added (2026-08-09 — the deliberate term-list hatch)
Mike ruled the D1-consequence: a leakscan marker whose scope NAMES
`local-term` explicitly — with a reason — exempts term-list hits on that
line (`leakscan:allow:local-term: <reason>`; scopes compose with commas).
The unscoped marker still never reaches the term list: D1 closed the
ACCIDENTAL silencing route and this opens only the deliberate one, where
naming the highest-confidence layer is the human judging exactly that
layer, on the record, counted in the tally. The three published-identity
lines (ADR 0005's named worked example) carry the scoped form, and the
full local-cover scan is green again — reviewers' re-run obligation stops
opening on a standing red.

### Changed (2026-08-09 — the reason rule bites the legacy spelling on boundary checks)
EP1(b) as landed exempted the legacy bare-list `scope`/`flags` spelling —
it cannot carry a `why` — so the ruled forcing function would only have
arrived when C1 phase 2 retires that spelling. **Mike ruled bite-now
(2026-08-09):** on a scanner with no advisory form (secretscan, leakscan,
linkscan, reviewscan, licenscan) the legacy spelling is now a config
error naming the reasoned form as the remedy. Softenable checks keep
parsing the legacy list until C1 phase 2 — that flag day stays C1's.
Measured blast radius at the ruling: one declaration estate-wide moves
from exempt to blocked; the fix is its one-line `why`. Six test fixtures
that used the legacy spelling on boundary scanners moved to the reasoned
form (their questions unchanged); the two transition-exemption tests now
pin the bite and its softenable boundary.

### Changed (2026-08-09 — a cancelled floor run is not an all-clear)
`RECORD.md` already required a close that pushes to carry the **pushed** floor
run's result rather than the local scan. The rule had a hole its grounding case
could not have shown, found live this session: `ci.yml` runs the floor under
`cancel-in-progress: true`, so a second session pushing to the same ref cancels
the in-flight run for the earlier commit. It ends `cancelled` — neither pass nor
fail — and **no run ever reports on the commit that was pushed**. A later
commit's green run is not a substitute: it evidences a different tree, and is
only reassuring at all when your commit is an ancestor of it.
- Written as a sub-bullet at the point of use, not a new section: read the
  *conclusion*, never just "the run finished"; on `cancelled`, re-run against
  your own SHA and wait for that.
- The cancellation itself is correct behaviour — `cancel-in-progress` is what
  stops a busy ref burning Actions minutes on superseded trees — so the fix is a
  reading discipline, not a config change. Whether it recurs often enough to earn
  a machine check is left to evidence; one instance grounds a clause, not a
  build. Rule-4 `⏳` queued.

### Changed (2026-08-09 — §9 ruled: it binds retrofits, and results carry their derivation)
Mike ruled the two consequences §9 landed without deciding, and added a clause
the venue-guide case had been sitting on all along.
- **§9 binds retrofits as well as new designs.** No grandfathering, decided on
  the asymmetry the open item named: deferring a retrofit is not cost-free
  waiting, it is ongoing loss, since each day without the dimension is another
  day nobody can reconstruct. The obligation is bounded honestly in the doctrine
  rather than left maximal — **start the clock now**, never backfill dates that
  are gone (inventing them would breach §0), and record the unrecoverable stretch
  instead of leaving it implicit.
- **The repo that owns the data owns the fix.** atelier's part ends at the
  principle and the `PROPAGATION.md` pointer carrying it; a child reads §9 through
  its SHA-pinned pointer and raises its own item at the point of use. No per-child
  ledger is kept here — that would be a second source of truth for work this repo
  does not do. What the ruling leaves genuinely open is recorded as such: a
  pointer delivers doctrine reliably, but a *retrofit* needs someone to notice it
  applies to data already shipped, and whether that gap is real is left to be
  evidenced rather than pre-solved with a check.
- **A stored result carries its derivation, not only its date** — a new §9 clause,
  generalised by Mike from the `verified` field in the doc's own case. A field
  holding a *conclusion* (`verified`, `approved`, a price, a status) needs **when
  it was established and by what method** stored alongside it. Without that the
  assertion is unfalsifiable and un-ageable: an owner-confirmed fact and a
  scraper's two-year-old guess render identically. This is `EVIDENCE.md` §3
  (acquisition method sets error risk) applied at the data layer, and it is the
  clause that makes staleness *computable* rather than felt — a refresh policy can
  only exist if each value knows its own age and how expensively it was obtained.

### Added (2026-08-08 — PRINCIPLES §9: data carries its time dimension)
A new design principle, minted by Mike: **data — application, system or user —
carries the time dimension its domain implies.** §1–8 govern the code and the
system; none of them reached the data the system holds about the world. The gap
was structural rather than an oversight — code gets a time dimension free from
git, so nobody has to learn to ask "when?" for code, and the habit never
transfers to data, which has no equivalent. Nothing supplies the dimension
retroactively, and the absence stays invisible until the first question that
needs it cannot be answered.
- **§9 as landed:** two clocks kept apart (*world time* — when it was true out
  there; *record time* — when we learned it, and how stale that now is);
  lifecycle transitions with dates instead of booleans, since `closed: true`
  loses *when*, cannot represent a reopening, and rewrites history as it flips;
  a hard delete destroys the dimension outright and is a recorded act under
  precedence rule 1, never the default way a thing stops being current; open
  intervals are legitimate and "unknown" is not "none" — one null standing for
  both is undetectable to the next reader; and the dimension is sized by the
  questions the domain will ask, not by ceremony, so full bitemporality is the
  heavyweight end most data does not earn.
- **Seams named, so no rule duplicates another.** `CONVENTIONS.md` governs the
  *frame* a stamp is read against; §9 governs whether the stamp exists at all —
  a dataset can satisfy every convention and still be undateable, and that note
  now sits in both docs. The *state vs stateless* situation test ("undated state
  is a future lie") is §9's instance for derived snapshots and points up to it.
  `RECORD.md` is the same instinct already applied to our own record, which is
  why the record reads cold years later and most application data does not.
- **Grounded, not invented:** the generalised case is a live fleet dataset whose
  records carry one nullable "verified" field and no world time — it cannot say
  when an entity began, when it entered the dataset, or tell a temporary closure
  from a permanent one. Named in §9 as the first retrofit case and honestly
  marked **unclosed**. Whether §9 obliges retrofits at all, or binds new designs
  only, is queued as Mike's ruling (`ROADMAP.md` § *PRINCIPLES §9*); rule-4 `⏳`
  queued in § *Doctrine — review-owed*.

### Added (2026-08-07 — the third render state, and pathscan reaches the estate)
Three ruled items on one surface, landed together because they are one story:
the board was overstating how much of the floor actually gates.
- **A warn-only check no longer wears a blocking check's green tick** (ruled
  2026-08-04 by Mike: *build the third render state*; handed up by the
  2026-08-03 pointer-grammar build, which correctly refused to decide it).
  `harvestscan` and `pointerscan` exit 0 whatever they find — deliberately,
  and the registry said so in prose — while the floor printed `✅ enforced`
  beside them, the same mark a scanner that blocks earns. That is EP3's
  *identical output for materially different cover* moved off leakscan's two
  planes and onto the registry itself, on every repo in the estate. The board
  now draws three states, on the hook render, the ci render, `--json` and
  `--list` alike:

      ✅ linkscan    enforced
      👁️  pathscan    warn-only  (warn-only wiring — reports findings, can
                                  never block this build)
      ⚠️  wrapscan    advisory   (adopting the check)  [review by 2026-09-01]

  The wording is pinned against E6b's 🟡 *"N advisory finding(s) — reported,
  not blocking"*, which lands on a check that **does** gate and let these
  particular findings through. Both notes are about findings that did not
  block and they mean opposite things about cover, so they share no vocabulary
  and the state column is the discriminator.
  **Derived, never listed.** A set of warn-only names beside the registry would
  drift the first time a line changed and nothing would say so — the
  vendored-policy shape `floor.py` exists to end. The state comes off the entry
  two ways: `--warn` in the plane's own argv, or a `warn_only` declaration for
  the checks that have no blocking form to switch off and so carry no flag to
  read. The two are pinned to each other in **both** directions by the selftest
  and the suite, against the registry's own second statement of the same fact
  (a check with no blocking form declares `advisory` identical to its enforced
  form).
  **What this does NOT change: any exit code.** `--warn` is about FINDINGS. A
  warn-only check returning non-zero has hit something its warn flag was never
  about — an unreadable tree, a missing input, a config error — and that still
  blocks, exactly as it did when these entries carried `enforced`. A render fix
  that quietly turned an environment error into a pass would be an unruled
  softening hiding inside a fix for overstated cover.
- **`pathscan` is in the registry — PS5, and it reaches every child** (D1,
  ruled FUND THE RESCOPE 2026-08-04; the rescope landed 2026-08-05 and the
  promotion was held only while a `floor.py` cold pass cycle was open — every
  cycle closed 2026-08-06). It ran from a bespoke step in atelier's own
  `ci.yml` and **nowhere else**: a check the parent enforces and no child has
  ever heard of, which is ADR 0008's vendored-policy defect one level up. One
  registry line retires that step. **Say the cost plainly: this arrives in
  every child's hook and every child's CI on their next push, with no child
  edit — that is the point of the promotion, and eleven children get output
  they did not ask for.** Warn-only is what makes it affordable, and it is
  warn-only because `--warn` is in the registry template rather than beside it:
  **the flip to blocking is still a separate ruling**, now a one-argument
  change that would reach the whole estate at once. The scope the bespoke step
  ran with — the doctrine surface plus the live root files, records
  deliberately out because they can never come clean without markers that would
  falsify the record — moved to `.atelier-floor.json`, exactly where wrapscan's
  and spellscan's already live. The registry default for a child is the records
  tree, like its sibling prose checks; it does not guess at a child's root
  files. Verified against the retired step: same 1 finding, same 10
  suppressions, byte for byte.

### Fixed (2026-08-07 — C1F3's third surface: the fleet board)
- **`floorfleet` sanitises child-authored config text before printing it**
  (C1F3 residue, found at the 2026-08-03 application). The strip landed at the
  two ruled parse seams — `floor.py`'s whole-document config ingest and
  `publishscan`'s ignore-file and output surfaces — and the board was missed,
  because it reads child `.atelier-floor.json` files through its **own**
  tolerant parsers rather than `floor.Config.load`. It is also the surface that
  reads repos this operator does not control. Measured on the fixture, both
  directions: before, five ANSI escapes, a BEL and a NUL from one child's
  `why`, disabled reason and local-check description reached the terminal
  verbatim — `\x1b[2J` clears the screen, `\x1b[1A` overwrites the row above,
  `\x1b[32m` repaints the rows after it green, on a board whose whole job is to
  be believed about which repos are guarded. After: zero, with ordinary text —
  em dashes, macrons, the reasons themselves — byte-identical. The finding's
  own text said the class reaches *"both floor and board"*.
  Applied with **`floor.strip_controls` itself**, made public for the purpose,
  over the parsed document before any reader below it. A second copy here would
  be exactly the per-surface list the shared function exists instead of: one
  would gain a case, the other would not, and nothing would say which.
- **A child config that is a JSON array no longer takes the whole board down.**
  Caught while wiring the strip: `json.loads` returned a list and the next line
  called `.get` on it, an `AttributeError` outside the `except ValueError` that
  was meant to contain a bad config. It now lands where unparseable JSON does —
  that repo's row reads unreadable, and the other fifteen still render.

### Added (2026-08-06 — the ADR 0008 cold pass applied: EP1(b), EP9)
Mike ruled EP1–EP10 on 2026-08-04, all as counselled. The three MAJORs'
substance had already landed on 2026-07-27; what this build adds is the one
MAJOR residue and the seven smaller findings.
- **`flags` on a check that may never be softened states a reason** (EP1(b)),
  in the same object spelling `scope` has carried since C1:
  `{"args": [...], "why": "..."}`. `scope` says where a check LOOKS and
  `flags` says how it RUNS, and both shrink real cover on the boundary and
  integrity checks a child may not turn off — `scope` gained the rule on
  2026-07-28 and `flags` did not. It matters because `FORBIDDEN_FLAGS` is a
  **blocklist** of four mode arguments, and blocklists underblock: a rule
  switched off by name, or a positional matching no staged path, reduces cover
  without touching the list. A missing reason is a config error, so it fails
  closed with the working spelling named in the remedy. A softenable check's
  `flags` stay reason-free, and the pre-C1 bare-list spelling still parses for
  the length of the transition. `floorfleet` reads both spellings, so the 🔧
  cover-reduction line does not go quiet as the estate migrates.
  **Measured blast radius, not estimated:** two such declarations exist
  estate-wide — one in the exempt legacy spelling, one already carrying a
  reason. **No repo goes red at its next push.** The forcing function arrives
  with C1 phase 2, when the legacy spelling becomes an error.
- **A missing `python3` blocks with a remedy that is not the bypass** (EP9).
  The hook guarded `floor.py`'s absence with a three-line fix and the
  interpreter's with nothing, so on a machine without `python3` the only
  actionable line a contributor saw was `--no-verify`. Fail-closed was never
  in doubt; being told how to skip scanning instead of how to scan was. Driven
  by a real commit on a PATH carrying git and no interpreter.

### Fixed (2026-08-06 — four things ADR 0008's surfaces claimed but did not do)
- **A deliberate pin is TWO edits, and now says so** (EP4). The ADR's own
  escape hatch from the accepted estate-wide blast radius is "children may pin
  deliberately" — and pinning `uses:` does not do that: the reusable workflow
  checks atelier out at `atelier-ref`, default `main`, so a `uses:`-only pin
  freezes the transport while the registry and every scanner still arrive from
  the tip. Documented at both points of use, and `floorfleet`'s board detail
  now reads *"workflow pinned; scanners still float unless atelier-ref is set
  too"* rather than the flatly untrue *"propagation frozen here"*.
- **The registry-driven selftest loop reads the calling repo** (EP5). It
  enumerated the runner's *workspace* — which holds `repo/` and `atelier/` as
  siblings and no config at all — so the `disabled` filter beside it was inert
  and read as though it were working. Now `--root repo`. The second half was a
  decision the counsel left open, taken here: the loop **skips `local` checks**
  with a comment saying the child's own CI owns proving its own check, because
  atelier neither ships nor reviewed that code and demanding a `--selftest`
  answer would impose a new contract on every repo using the seam. atelier's
  own `ci.yml` takes the same skip — the parent is not special, and the day it
  declares a local check its CI must not surprise-red.
- **The prove-it-landed command proves the claim that bites** (EP10). It
  printed the registry, which proves the tools path resolves and the config
  parses — and not that git will ever invoke the hook. It now prints
  `git config --get core.hooksPath` first: with that unset or mistyped, a clean
  registry prints while every commit goes unscanned.
- **`floorfleet`'s stated blind spots name trigger shape** (EP8). A caller
  whose `on:` carries only `workflow_dispatch` reads `wired ✅` while nothing
  runs on push. The concession named conditions and disabled workflows and not
  this; the classifier is unchanged, its honesty is not.

### Changed (2026-08-06 — ADR 0008 gains two clauses it was missing)
Both appended and dated rather than rewritten — it is a decision record.
- **Decision 6: a repo may ADD a check of its own, never soften one** (EP6).
  The repo-local `local` seam landed on 2026-07-26 with its doctrine written at
  every point of use except this one, so the record described only subtraction
  and a reader concluded the seam did not exist.
- **A named control for the floating `@main`** (EP7). The consequence list
  accepted the estate-wide blast radius without ever naming what holds it: the
  control is atelier `main`'s own protection — branch protection, signed
  commits, review on the registry — and a compromise there is **arbitrary code
  in every child's CI**, not merely a broken floor. That is the reason the
  signing trust root is pinned while the scanners float; the two calls point
  opposite ways on purpose.

### Added (2026-08-06 — leakscan reaches for the PII half: the E7 build)
The 2026-08-03 sweep found `leakscan` **materially behind** `secretscan`:
two layers against three, no label context, no placeholder suppression, and
a block of values under explicit personal-data key names probing completely
clean. Mike ruled the fixes on 2026-08-04; this is that build. Every new
rule ships with must-flag *and* must-pass tests.
- **The missing third layer — `pii-key-context`** (G1, the highest-value
  fix by a wide margin). A non-placeholder value assigned to an explicit
  personal-data key name is now a finding even when the value alone matches
  no shape at all: date of birth, bank account, passport, driver licence,
  NHI, tax number, medication, prescription, allergy, blood type, patient,
  next of kin, emergency contact, maiden name, home address, plate. This is
  the only possible net for those classes — the sweep's own don't-add list
  rules out detecting any of them by shape, because letters-plus-digits is
  also the shape of a SKU and a bare date rule would fire on every record
  in the estate. It ships **with placeholder suppression** (leakscan had
  none of any kind before now) and with **its own canary suite**, on
  secretscan's SF3 pattern: 27 shapes enumerated, the count pinned, and the
  contract written down — a canary going quiet is a detection regression,
  never a fixture to update. Thirteen placeholder shapes are pinned the
  other way, so the two suites are each other's guard rails.
- **File PATHS are scanned, not just contents** (G2). A file whose *name*
  carries an address or a person leaks exactly as much as one whose body
  does, and the name was never read. All three layers now run over each
  repo-relative path, reported at line 0 and rendered as such. Measured
  cost, before and now: **zero findings** across this repo's whole tree.
  A binary's name is read even though its body cannot be.
- **Financial identifiers as a class** (G4): payment cards with a **Luhn**
  check and an issuer-range guard, IBANs by **ISO 7064 mod-97**, and the NZ
  hyphenated bank-account field shape. The self-validating checks are what
  make a digit run safe to flag at all; the **compact all-digit forms stay
  key-context-only**, as ruled.
- **Term-list derived forms** (G6), **opt-in per term** via a new `forms:`
  prefix: one entry now covers a name's slug, snake, dotted, camel-case,
  run-together and double-spaced spellings — the forms a name actually
  leaks as. Opt-in stays opt-in (zero-separator matching is the operator's
  judgement to make, not the tool's), and `tools/leakscan-terms.example.txt`
  documents it with the line-based limit stated.
- **The bracketed NZ phone form** (G7) — the one common spelling missed.

### Fixed (2026-08-06 — six defects in leakscan's existing rules)
- **The IPv6 rule stops reading punctuation as an address** (D2, and **E4**
  with it — one fix, both entries). It fired on any three colon-separated
  hex-ish groups, which is also a clock time, a port map, a ratio and a hex
  colour triplet — a false-positive class far wider than the two clock
  times originally recorded. It now requires a compression marker or four
  or more groups, with both directions pinned; a Python slice and a C++
  scope resolution are not addresses either. Real and compressed addresses,
  including the ULA shapes the estate uses, still flag.
- **The IPv4 safe set widens to what carries no topology** (D3): every
  contiguous netmask (computed, not listed), the unspecified and broadcast
  addresses, the loopback net and the well-known public resolvers. These
  produced findings whose only possible resolution was an allow-marker,
  which is the class `GUARDS.md` says to fix at the rule. RFC 1918, CGNAT
  and link-local space are deliberately still flagged.
- **The address rule stops reading figure references as addresses** (D4):
  abbreviated and ordinary-word street suffixes now require at least one
  capitalised word in front of them. The distinctive full-word suffixes
  keep the permissive form.
- **MAC addresses report once** (D5). Six colon-separated hex pairs are
  also a valid IPv6 shape, so the same characters reported twice. The
  narrower rule wins, an exempted MAC is not re-reported by the wider one,
  and disabling the narrower rule leaves no blind spot.
- **Fixed-value safe addresses match exactly** (D6): the safe-set test was
  a prefix match, so a longer final octet was exempt for free. Network
  prefixes still match by prefix, which is the correct semantics for them.
- Two live allow-markers in the tree are now unnecessary as a result (a
  rendered clock time, and a MAC's IPv6 double-report). Left in place —
  removing them is a separate, deliberate edit.
- **NOT built, and untouched:** G3 (binary/media blocking, ruled but a
  separate and larger behaviour change) and G5 (international phone,
  deferred by ruling).
### Added (2026-08-06 — secretscan gets a second response, and E3 rides with it)
- **E6b — the advisory tier is built** (ruled 2026-07-28; unblocked 2026-08-04
  once its consumer was named, per EI1). A `secretscan` finding now carries a
  **response** as well as a rule, and only one of them touches the exit code:
  **block** for every named vendor format, `assigned-secret` and `high-entropy`;
  **advisory** for the new `low-variety-entropy` rule, which reports and exits 0.
  The **blocking set never shrinks** — every input that exited non-zero before
  the tier still does, with the same finding, pinned by a
  `BlockingSetNeverShrinks` suite that re-runs all 16 canaries against the
  *response* rather than only against detection.
  What the tier buys: the narrowing site the E6 intent cold pass named (EI4) is
  `HIGH_ENTROPY_RX`'s mixed-class requirement, which excluded every single-case
  run — git SHAs and checksums, but also lowercase-hex *secrets* — from the
  context-free net entirely. That path now reports on E6c's already-ruled whole
  shape (an unbroken 32+ alphanumeric run is key material; names do not run 32
  characters unbroken), so a hex-encoded credential outside an assignment is
  seen instead of invisible. **No new threshold was introduced** — the length is
  E6c's, the mixed-class split is the existing net's; only the response is new.
- **Its three consumers, built with it rather than after it.** EI1's finding was
  that an advisory finding nobody reads is cover, not coverage:
  **(1)** the pre-commit hook prints them at the commit that would introduce
  them; **(2)** every CI push re-prints **all** of them tree-wide (`--plane ci`
  scans the repo root, pinned by a test so a future `scope.secretscan`
  narrowing cannot end the guarantee in silence); **(3)** `floor.py`'s board
  carries `🟡 N advisory finding(s)` on the check's own line. The count is read
  off **that run's output** — no state file, nothing to go stale, nothing to
  forget to update. It cannot quietly vanish either: the scanner prints its
  known zero, and a missing count line renders 🔴 *"the count contract has
  drifted"* rather than a silent green. The seam is pinned from both sides by
  `test_floor.py::AdvisoryCountContract`, which runs the real scanner.
  Tree-wide at landing: **21 advisory findings**, counted from the run rather
  than estimated — 12 SHA-pinned Actions digests (workflows and the `create-repo`
  workflow templates), 2 sha256 checksums in an instrument's tests, and 7 test
  and selftest fixtures, 4 of which this change itself added. Every one of them
  is a hash. That number is the widening working, not a defect, and it is
  deliberately left unsuppressed: a board that reads 🟡 21 is the ruling's
  "persistent count that cannot quietly vanish" doing its job on day one.
- **E3 — public-key fingerprints no longer block** (ruled 2026-08-04, Mike).
  `ssh-keygen -l` prints `SHA256:<43 base64 chars>`, which is a mixed-class
  32+ run at entropy ~5.9 and therefore a *blocking* high-entropy hit — two of
  eight findings in one child were this shape. A fingerprint is public material
  by definition: it is published so a key can be verified, and it is one-way.
  Suppressed **whole-shape, never fragment** — the standing lesson of
  2026-07-28, when four real credentials walked past suppressions that matched
  on a fragment. A `SHA256:` prefix in front of a body of the wrong length is
  not a fingerprint and still blocks. Canaried **both directions** so the
  carve-out cannot widen in silence, and **counted** in the suppression tally
  (GUARDS.md rule (b)) rather than applied invisibly, which is more than
  `PUBLIC_KEY_RX` beside it has ever done. The legacy colon-joined hex MD5 form
  is recognised too; it produces no finding to suppress today (`:` is not in the
  entropy net's character class) and is canaried so a future widening cannot
  start flagging it by accident.
- Tests 1060 → 1103 (`test_secretscan` 89 → 122, `test_floor` 98 → 108). One
  existing contract changed **deliberately and on the record**:
  `test_context_free_path_is_unchanged` asserted *no finding of any kind* on a
  bare git SHA, which was right while `block` was a finding's only possible
  response. It is now `test_context_free_blocking_set_is_unchanged` — the claim
  E6c actually made — with the advisory half asserted separately rather than
  left unpinned.

### Fixed (2026-08-06 — the queue take's ruled findings applied)
The 2026-08-06 rule-4 cold passes returned 0 MAJOR each (all three cycles
closed); Mike ruled the residue the same day and these are the fixes, each
probed both directions:
- **licenscan's last reasonless hatch closed** (LC1/LC2): the
  unknown-license suppression keyed on a raw substring, so a bare marker —
  or prose merely *mentioning* the marker text — silently retired the warn.
  It now requires the same reasoned marker every other site does, and the
  retirement is tallied, never silent. Five unreachable `-only`/`-or-later`
  alias entries removed (LC4) — the suffix strip runs before the lookup.
- **stampscan's canonical side learns code context** (SD1): region
  extraction now reads the same fence/code-span-stripped view the stamp
  hunt does, so a fenced *example* of region markers can no longer shadow
  the real region (identical copies read as drift against example text —
  latent, never fired live). The live PROPAGATION shape (markers outside a
  presentational fence) extracts verbatim as before. A suppression tally
  with known zeros joins the output (SD3) — first live run made 98
  silently-skipped files visible — and a whitespace-only `narrow=` is no
  longer a declaration (SD4; the marker still parses, the declaration is
  void, so the diagnostic stays a clear silent-drop drift). SD3 discharges
  what remained of D2 residue (b); its loader half had already landed with
  the ten-loader sweep.
- **`PROPAGATION.md` stops contradicting the live tree** (SD2): the
  stamp-discipline paragraph still said stampscan was "shelved on a parser
  defect… watched by nothing" — rewritten to the current truth (advisory
  in atelier, registry wiring barred, blocking a later ruling).
- **Five stranded tests rejoin every invocation** (LC3/PD1): the 0228793
  merge left `Allowances` classes below `unittest.main()` in two suites, so
  direct file runs silently dropped them. Moved up; direct and discovery
  runs agree again. True suite totals at HEAD: licenscan 56 (incl. 2 new
  LC1/LC2 tests), stampscan 75 (incl. 10 new SD tests), pathscan 76.
- Accepted as recorded, not fixed (Mike, same sitting): licenscan's
  multi-LICENSE first-in-walk pick (LC5, pre-existing), the fence-closer
  length asymmetry (SD5, cosmetic), and the pathscan/linkscan double-report
  on broken link-text paths (PD3, deliberate on both sides).

### Added (2026-08-05 — guard governance, and every allowance made narrow, noisy and reasoned)
- **`docs/method/GUARDS.md` — how a guard's findings are *governed*.** Track F/F1
  rebuilt against Mike's three rules for granting an exception: as **narrow** an
  allowance as possible, **noisy** (it fails as it is scanned, and the exceptions
  are then applied to remove the expected, explicitly accepted noise), and
  **reasoned**. Three assessment axes (identification confidence · probability of
  harm · impact of harm) with undeclared axes defaulting to worst-case;
  assessment kept separate from response; a granularity ladder (line / check /
  repo) that is what makes "as narrow as possible" checkable at all; acceptance
  (indefinite + reason) distinguished from deferment (temporary + expiry).
  Discharges FG1–FG6. The load-bearing change is **provenance, not direction**: a
  guard may never lower its own response, but a declared, reasoned,
  principal-visible act may — carrying an expiry where the claim rots. Tested
  rather than inherited, as ruled: a lawful downward lane already existed in
  three places, so escalate-only never described this estate. Prior art verified
  at pickup (Semgrep's confidence/likelihood/impact, CodeQL's precision vs
  problem.severity, CVSS v4.0's Threat and Environmental groups).

### Changed (2026-08-05 — all twelve scanners onto the model)
- **Every allow-marker now needs a stated reason.** `\b<marker>:\s*\w` — the
  form `datescan`/`pathscan`/`stampscan` already used — in the nine that
  accepted a bare substring match. A marker with no reason is a *mention*.
- **Rule-scoped markers where a scanner has more than one rule**
  (`leakscan:allow:ipv4: <reason>`), so a marker written for a false-positive
  email no longer silently exempts a MAC address on the same line. Deliberately
  NOT added where a scanner has one rule; the reason is stated in each
  `parse_allow` docstring so the asymmetry reads as a decision.
- **Every scanner reports what it suppressed**, with known zeros printed so two
  runs compare side by side. 37 suppressions in leakscan, 14 in secretscan, 4
  declarations in licenscan — all previously behind a bare `✓ clean`.
  `--disable` names the rules it disabled, too.
- **An ignore glob must state its reason** in all ten loaders — trailing
  `# reason` or a stanza comment — and an unreasoned one is exit 2, not a
  warning. All 31 live entries pass unchanged.
- **D1 applied** (Mike, 2026-08-04): an allow-marker exempts structural rules
  only; the machine-local term list always runs.

### Fixed (2026-08-05)
- **A prose mention was holding a live exemption.** A session log reading
  a loopback address followed by the words "marked `leakscan:allow`" was exempt because the sentence
  mentioned the marker. CI runs leakscan structural-only full-tree; it would
  have gone red there.
- **A dual-marker form where only the second marker carried a reason**
  (`# secretscan:allow / leakscan:allow: fixture`) was honoured on a substring
  match, in three live lines including the pre-commit test's planted secret.
- **The reason character class was `\S`, which accepts `-->`** — so
  `<!-- datescan:allow: -->`, a marker with no reason in the commonest Markdown
  spelling, parsed and exempted. Caught by datescan's own DSR8 test; corrected
  in all seven scanners it had reached.

### Changed (2026-08-05 — pathscan reaches the corpus that motivated it)
- **A fourth anchor, and the root files are finally in scope** (PS1). A file
  with no `docs/` ancestor now resolves candidates against the repo's
  `docs/` tree — the docs-relative shorthand every root file in this house
  actually writes. Before it, the scanner could not see its own motivating
  case: S2's first citation is a root README naming `docs/decisions/`, and
  the wired step scanned `docs/` only. Anchors 3 and 4 are mutually
  exclusive by construction, and the finding text names whichever was tried.
- **The gateable surface is stated, and it is not the default.** Records
  (`docs/reviews/`, `docs/sessions/`, and — named explicitly —
  `CHANGELOG.md` and `ROADMAP-DONE.md`) legitimately name the tree as it
  stood when written; with no time axis they can never come clean without
  allow-markers that would falsify the record. The doctrine surface plus
  the live root files can, and now does: the advisory CI step scans exactly
  that surface, at zero findings on landing day.
- **Extensionless tokens get a `.md`/`.markdown` retry** (deferred Q2) —
  GitHub's directory-index convention, so `tools/README` finds
  `tools/README.md`. Grounded in the convention, not the count, and
  monotone-safe. **Date/time placeholders are exempt** (PS3): `YYYY`/`HHMM`
  in a token is a naming template, not a claim. `MM`/`DD` alone are not
  cues.
- **The docstring stops overclaiming** (PS8). It said the heuristic caught
  "every cited occurrence"; B11 — seed from a bare single-segment
  directory token — is a shape the regex cannot match at all. Two of
  three, now said plainly. The single-segment floor was always defensible;
  the claim was not.
- **Four named limits added, none of them new behaviour** (PS2, PS3, PS6,
  PS7): emphasis-wrapped paths are invisible; a `TODO` about something
  else masks a real break on its line; indented code blocks *are* scanned;
  the line-local blanking pass misses a placeholder span that wraps. Plus
  the silent false negative all four anchors buy — existence somewhere is
  not correctness.
- **The gated surface's residual is burnt to zero**: the review's one live
  true positive fixed (`docs/build/README.md` named a scanner by its
  pre-rename path) and the false positives marked with written reasons —
  including four in decision records, where a marker annotates and the
  record stays verbatim.
- `tools/test_pathscan.py` 53 → 73 tests; `--selftest` gains a root-file
  probe so anchor 4 and the index retry are proven on a box without the
  unittest file. Registry promotion (PS5) is deliberately NOT in this
  delta — it waits on the open floor.py cold pass — and the scanner stays
  advisory; the flip is still a decision.

### Fixed (2026-08-05 — stampscan's wiring blocker cleared; the convention gets its doctrine)
- **A document about stampscan is no longer a stamp** (ST1, the wiring
  blocker). The marker parser read markers anywhere it scanned — prose,
  fences, code spans alike — and a stray marker is a config error `--warn`
  never downgrades, so ordinary documentation reddened the whole floor and
  the scanner was unwired within three days of being built. It now strips
  fenced blocks and inline code spans before marker-hunting, as every
  sibling does. Recognition only: a stripped line still enters a payload
  verbatim, so comparison is untouched. Named residual: a raw, line-start
  HTML-comment marker in bare prose still reads as live — defensible because
  rendered Markdown hides raw HTML comments, so real documentation uses a
  code span.
- **The end marker is anchored again** (ST7). It was matched by a bare
  search anywhere on a line, forced by the template closing its stamp inline
  on a divider to keep a frozen test's verbatim slice intact — and that
  search-anywhere match was the widest single contributor to the false
  stray-ends above. `test_templates.py`'s `template_block()` now strips
  marker lines, the template's end marker sits on its own line, the regex
  anchors, and a new test pins the placement so the compromise can't return.
- **Narrowing to nothing is drift** (ST2, ruled 2026-08-04). An empty
  stamped block passed clean with any `narrow=` token — one word could
  vacate an entire inlined floor while the check reported green. Empty is
  now drift however it is declared. A genuine partial narrow still passes.
- **`source=` is confined to `--root`** (ST4). It accepted `../` traversal,
  and pathlib silently discards the root for an absolute path — a crafted
  stamp could aim the scanner at any file on the machine and get one of its
  lines echoed back in the drift hint. Escaping the root is now a config
  error (`unconfined-source`).
- **The convention that "borders on a doctrine act" is now written down**
  (ST5). `PROPAGATION.md` states what a stamp is, what `narrow=<reason>`
  declares, that narrowing to nothing is drift, and who may declare a
  narrowing — the child repo, in its own tree, with the reason written
  down. `tools/README.md` gains its section; `.stampscanignore` ships the
  house net. Measured while landing it: the parser fix alone clears the
  live tree, so the ignore file is the standing net for the residual, not a
  load-bearing patch.
- **Honesty fixes** (ST6): the duplicate-line residual overstated — a
  greedy two-pointer subsequence test is exact for membership, and
  adversarial probes agreed; what it lacks is which occurrence matched, a
  hint-quality limit only. `render_human` de-duplicates note kinds.
- **Wired advisory in atelier's own `ci.yml`, and nowhere else.** Not in
  `floor.py`'s registry: that reaches every child at once (ADR 0008), and
  ST3 is open — the template's stamp pins a `source=` path that exists only
  in atelier, and the child-side resolution story must be pin-aware, since
  a child pinned at a SHA may lawfully differ from atelier@main.
- `tools/test_stampscan.py` 46 → 65 tests; `tools/test_templates.py`
  37 → 38; `--selftest` gains the ST1/ST2/ST4 cases so a box without the
  unittest file proves them too.

### Fixed (2026-08-05 — licenscan under a licence it can't name, and the classifier that was right all along)
- **A LICENSE we can't name is still a LICENSE** (E1). An unrecognised body used
  to end the scan at one medium `unknown-license` finding: the per-file SPDX
  header checks never ran, and an allow marker on the LICENSE line didn't
  restore them. The silence covered the worst case there is — a proprietary
  repo publishing a vendored copyleft file. The body is now read as a
  *declared* custom licence (`LicenseRef-UNRECOGNISED`, or an explicit
  `LicenseRef-` id it names). Which known licence it is stays unanswerable and
  is no longer asked; whether it carries GPL/AGPL/LGPL/MPL terms forward is
  answerable — it does not — so copyleft under it blocks exactly as it does
  under a permissive licence.
- **The allow marker now means what it says.** On a LICENSE line it retires the
  unrecognised-body warn and leaves the header checks running; an explicit
  `LicenseRef-` id needs no marker at all, being a deliberate declaration
  rather than a failure to recognise. `--expect` compares against the custom
  id too, so a CI assertion of Apache-2.0 can't pass on an unnameable body.
- **PyPI trove classifiers resolve to SPDX ids** (E2).
  `License :: OSI Approved :: Apache Software License` is the *correct* way a
  Python package names Apache-2.0, and licenscan read it as an unrecognised
  declaration and blocked — friction aimed at a repo that had done the right
  thing. Sixteen unambiguous classifiers now map before the
  unrecognised-declaration check. Ambiguous family names — `BSD License`, the
  unversioned `GPL`/`LGPL` — are absent on purpose and still degrade to the
  warn: friction, never a guessed version.
- **What it still won't say**: under a custom repo licence, metadata
  declarations aren't compared (there is no id to compare with) and a
  permissive foreign header goes unremarked — only the copyleft call is made.
- `tools/test_licenscan.py` 37 → 52 tests; `--selftest` gains the proprietary
  poison-pill and classifier cases, so a box without the unittest file proves
  both.

### Added (2026-08-03 — the queued-review pointer gets a forcing function)
- **`tools/pointerscan.py` — two advisory guards on the `⏳` pointer.** *Grammar:*
  a pointer that seeds the reviewer's first question steers the pass it is
  queuing, against the refs-only ceiling `ROADMAP.md` and `REVIEW.md` both state;
  recorded three times, the third written hours after its author read the finding
  recording the first two. *Cycle state:* an item asserting a review is owed while
  carrying the verdict of the review that ran, with the state it is actually in
  named — reviewed, ruled, applied — because all five recorded residues said
  "review queued" when what was owed was the principal's ruling.
- **The scope decision is the deliverable, not the regexes.** *What makes an item
  a queued-review pointer* is settled in the module docstring on four recorded
  specimens: the marker glyph in the bullet or the state prefix, **or** a
  review-obligation phrase inside an emphasis run. Scoping to the glyph alone
  provably misses the one specimen still standing when this landed, which would
  have been a check that runs, exits 0 and covers nothing.
- **Pass type ruled a lawful field** beside {delta, intent record, tier}: tier is
  already lawful and is the same class of fact — both route the review, neither
  says anything about the delta's merits, and the ceiling forbids an evaluative
  *account*, not routing.
- **It lints no field into existence.** The 2026-07-18 record rejected a lint
  demanding a review line under every roadmap heading, and `reviewscan` honours
  that refusal. This forbids content in one narrow, self-identifying item type —
  a different rung, and it is its own tool rather than a fold into `sizescan`,
  whose advisory declaration would otherwise silently soften it too.
- **On day one it found three live findings**, including a stale residue in a
  section the recorded sweep of "five" had not looked in.

### Changed (2026-08-03 — B4's shelf verdict overturned; `harvestscan` joins the registry)
- **`harvestscan` is wired, scoped and warn-only** (HV1, ruled 2026-07-29). The
  author's own "do not wire, not even advisory" rested on the *unscoped*
  measurement; its cold pass measured a variant the entry had named but never
  measured. Scoped to commits shedding ≥ 50 **net** lines from `ROADMAP.md`, the
  whole history holds 6 in-scope commits, of which 3 warn — all justified, and
  the motivating incident caught. Net, not delete-only: that incident was
  +48/−184, so the entry's first-ranked variant would have missed it.
- **The pointer exclusion is `pointerscan`'s test now** (HV2). The copy inside
  `harvestscan` read the marker or the item's first six words, and the recorded
  corpus has four pointer shapes of which that saw two — so it was forgiving
  items nothing then policed.
- **The survivor search reaches the stores that actually receive harvests**
  (HV3) — `docs/sessions/` and `docs/reviews/`, and their **prose**, not only
  their list items. Widening the file list alone was measurably inert: those
  stores hold almost no checkbox items, so a harvest written up as a paragraph
  still read as vanished.
- **The plane wording says what is read** (HV4): `--staged` reads the INDEX —
  what the commit is about to be — and the default reads the working tree. The
  old wording said "staged/working" while the code read the working tree only.
- **The replay harness ships** (`--replay`). The cold pass had to rebuild it from
  the tool's pure functions to check the recorded figures, and HV3 required the
  effect of widening to be measured before landing; neither is possible against a
  harness that lives only in a session's scratch space.

### Changed (2026-08-03 — joined notes, ageing on the line, control strip)
- **The floor's human line stopped choosing between its notes** (TAA2 + C1F1
  as one design): an advisory's `why`, its scope-drift note and its cover
  note now join on the line instead of an `elif` picking one; an expired
  advisory's days-over count prints on the floor line, not the board alone
  (C1F2), so the ageing pressure lands at commit time.
- **Config-authored strings are stripped of C0 controls at the parse seam**
  (C1F3 + PA4): `floor.py` strips the whole parsed config document;
  `publishscan` strips ignore-file lines and git output. A hostile child
  config's escape sequences arrive as inert visible text — removal at
  ingest, with the interpolation-point encoding kept as the inner guard.
- The scope guard's comment stopped calling two shut fail-opens "(open)"
  (TAA1), pinned by a source-text test.

### Changed (2026-08-03 — the board says which authority answered)
- **`floorfleet` now carries its discovery authority beside its answer**
  (FS1–FS5 applied): a footer states which listings answered with counts,
  archived and unreadable tallies print even at zero, and an empty
  private-capable listing warns loudly. A remote read now has three outcomes —
  only HTTP 404 means "not enrolled"; auth/rate-limit/server failures render
  `unknown` rows that red `--check` instead of masquerading as outsiders. The
  token spec states the all-repos grant on every surface the repo carries.
  Plus one crash fix: a repo carrying no floor config no longer fells the
  board that exists to report it.

### Changed (2026-08-03 — low variety is not innocence)
- **`secretscan` no longer treats low character variety as evidence of
  innocence in credential-key context** (E6c, generalising the ruled SF1+SF2
  carve-outs): in assigned-secret context, a 32+ unbroken alphanumeric run or
  a four-plus-word separator-joined passphrase flags regardless of the
  identifier/slug suppressions; the ruled six-shape probe went two-of-six to
  six-of-six and the blocking set only widened. A 16-shape **canary suite**
  (SF3) now pins the gate: a canary going quiet is a detection regression,
  never a fixture to update.

### Changed (2026-08-03 — ER1–ER4 applied; the mid tier earns its seat)
- **The making-public confirmation now includes the pre-flip scrub** of the
  estate-root name (`AUTONOMY.md`); `PROPAGATION.md` says where the local-path
  convention is defined (per estate, in its private root's onramp) and restates
  the co-occurrence figure as approximate; `RECORD.md` fixes the addendum
  pointer convention — name "the `SESSIONS.md` entry of a date", never the file
  the addendum extends. (ER1–ER4, ruled 2026-07-28.)
- **`ECONOMICS.md` promotes the mid tier to standing executor** for well-floored
  builds of known patterns and prescriptively-reviewed fixes — four recorded
  trial runs, discriminator floor density, explicitly not any first-of-kind
  build.

### Added (2026-08-03 — the boundary's posture becomes doctrine)
- **`SECRETS.md` now states the posture both boundary scans answer to**: find
  every secret, credential, private key and piece of personal data, so none of
  it reaches a public or insecure place. Over-flagging is the fail-safe
  direction for both scans by decision (the historical opposite tunings are
  recorded as found-and-decided); a coverage narrowing is the principal's
  decision, never a code comment; the credential scan's advisory tier is
  recorded as decided-not-built, gated on naming its findings' consumer.
  (E6a — ruled 2026-07-28/29, landed by the 2026-08-03 orchestrated run.)

### Added (2026-07-26 — the floor grows a repo-local extension point)
- **A child repo may now ADD a check, not only subtract one.** `.atelier-floor.json`
  gains a `local` block declaring checks the repo owns and ships: `run` (a path
  inside the repo) and `why`, plus optional `planes`, `args` and `scope`. They run
  beside the fleet checks on both planes and block the same commit.
- **Why it exists.** Everything the config could say was subtractive — which of
  atelier's checks a repo is *not* enforcing — and the tracked pre-commit shim is
  deliberately scanner-agnostic. A repo with a rule of its own (the forcing case:
  a tripwire whose blocklist names the estate's own tokens, which can never live
  in a shared repo) had to keep a bespoke hook and fall out of propagation
  entirely — the exact defect ADR 0008 closed — or lose the check.
- **It adds; it cannot replace.** A local name colliding with a registered scanner
  is a hard config error, `run` must resolve inside the repo, and the script is
  invoked directly rather than through a shell. `scope`/`flags` are refused for
  local names: a local check's scope and arguments live beside its declaration.
- **It fails closed and stays visible.** A declared check whose script is missing
  BLOCKS, as a missing shared scanner does — declaring a check you don't ship is
  not a way to look guarded. Local checks appear in `--list`, `--json`, the render
  (`· local`) and on `floorfleet`'s board (`➕`), which is the only place the
  estate will ever see a rule whose code is repo-specific by construction.
- **One softening vocabulary.** A local check named in `advisory`/`disabled` reads
  identically to a fleet one. The honest difference is stated: a fleet scanner's
  advisory swaps in its own `--warn` form, while the floor can't know a local
  check's flags, so advisory there downgrades the result, not the invocation.
- **A hook-only local check still lists on CI, as skipped with a reason** — the
  machine-local-data shape (leakscan's term list) applied to a child. Silence
  there would be indistinguishable from a check that ran and passed.

### Added (2026-07-26 — ccrepo prices by date and groups by session; cctranscript counts agents that finished)
- **A ccrepo price is effective from a date to a date.** A `PRICING` entry may
  now be a list of `{from, to, base}` intervals (ISO dates, UTC, both ends
  inclusive, either end omitted for open-ended) as well as a bare number, which
  still means "always" — the compatibility guarantee every existing
  `~/.claude/ccrepo-pricing.json` rests on, now pinned by a test. Each message is
  priced at the rate in force when it was **sent**, so a rate change no longer
  rewrites history. `sonnet-5`'s introductory `$2` (through 2026-08-31) and
  standard `$3` (from 2026-09-01) are both entered, each correct on its own side
  of the date, so the revert needs nobody to remember it.
- **A timestamp inside no interval is unpriced** — $0 and flagged, the same path
  an unknown model takes, never snapped to the nearest interval. The footnote now
  names *which* of the two gaps it is: a model missing from the table needs a
  price added, one already in it needs an interval widened, and the old single
  message gave the wrong instruction for half its cases.
- **No `ROLLUP_SCHEMA` bump, verified rather than assumed** — `recipeSig` already
  `stableStringify`s the price table, so a flat and a time-bounded table sign
  differently and the ledger rebuilds itself. The event *shape* is unchanged;
  only its values move, which is exactly what the signature covers.
- **`-g session`** joins the group dimensions, answering "which session hit
  529k?" — the one part of that question ccrepo previously couldn't. It keys on
  the full UUID (a synthetic ordinal stays a display label, never a key) and
  prints an 8-character prefix in the human table only; `--json`/`--csv` carry
  the whole id, because a truncated id you can't look up is worse than a wide one
  you can. The filter's private session getter is gone, so filtering and grouping
  can no longer disagree about what a session key is.
- **cctranscript reports agents *finished* beside agents *started*** —
  `10 agents started · 15 finished`. Started reads the spawn calls (a ceiling);
  finished reads the sibling `subagents/` directory, one log per agent that
  actually ran. Both chips always print: where the store never said, the second
  reads `finished unknown` rather than dropping out or claiming a zero — the
  field set stays stable for a side-by-side read without asserting an unevidenced
  figure. Finished can legitimately *exceed* started, because a nested agent logs
  into the principal's directory while the principal's own call count doesn't see
  it; the figures are left unclamped so the nesting stays visible.
- **Correction to the entry below**: it says a directory-sourced count would
  "silently read zero" under `--from-archive`. That was wrong. ccarchive's
  capture allowlist takes any `.jsonl` at *any depth*, so `subagents/` is
  mirrored — 92 such directories in the live archive, and a session renders an
  identical header live and archived. The claim was reasoned from how path
  resolution works rather than from what the archive contains. The entry is left
  as written; a record that quietly rewrites its own history is what the honesty
  rule exists to prevent.

### Added (2026-07-26 — cctranscript reports a session's context size and agent count)
- **Context size on the summary line** — `206 turns · 24 you · 182 Claude ·
  477k context · 12h2m`. Counted as `input + cache_creation + cache_read`,
  because in a long session nearly every token arrives as a **cached read**:
  `input_tokens` alone renders a 477k conversation as single digits. Reports the
  **peak**, not the last request, so a compacted session still shows what it
  held; `--json` carries `context.peak` and `context.final` separately, keeping
  the divergence visible. A log with no usage records omits the figure rather
  than claiming zero.
- **Subagent count on the same line**, read from the spawn tool calls (`Agent`,
  and the legacy `Task` name) rather than from the sibling `subagents/`
  directory of per-agent logs. That directory is the stricter source, but
  `--from-archive` resolves a single file, so a directory-sourced count would
  silently read **zero** there — a figure that holds in both modes beats an
  exact one that holds in only the live mode. Read as a ceiling: a skipped or
  stopped spawn still counts. `--json` adds `agents.byType`.
- Both tallies are taken **before** the view gating, so `--tools`/`--think`
  change what you see and never what the header reports.
- The time span joins its two clock times with the word **to**, not an en dash —
  a dash between two colon-heavy times reads as punctuation to decode rather
  than a span to skim. Mike's call, and **scoped to this CLI's header**: not a
  house convention, not propagated to the other instruments. (Written out rather
  than shown: two literal clock times side by side trip leakscan's IPv6 rule.)
- **The agent count always prints, including `0 agents`** — Mike's call, on the
  ground that the summary line gets read by *comparing* sessions, and a chip
  that vanishes at zero makes two headers line up differently for the reader to
  reconcile. (It shipped omit-at-zero hours earlier; reversed the same day.)
  Deliberately the opposite treatment from the context figure, which stays
  conditional: a zero the log **proves** is a fact worth stating, while a size
  the log never recorded is **unknown**, and printing that as zero would be a
  claim the evidence doesn't support.

### Changed (2026-07-25 — enforcement propagates by call, not by copy: ADR 0008)
- **`tools/floor.py`** — ONE registry of which checks run, read by both planes
  (pre-commit hook: staged diff at full cover; CI: whole tree, leakscan
  structural-only). Replaces a scanner list that was **vendored per repo**: the
  scanner *code* was already one-source, but each child carried its own 247-line
  `floor.yml` and four hard-coded `run_scan` lines. Measured across the estate:
  12 of 13 children ran **none** of the five checks added since they were
  scaffolded. Adding a line to the registry now reaches every repo's hook and CI
  at once.
- **`.github/workflows/floor.yml`** — atelier-hosted **reusable workflow**. The
  child template drops 247 lines → ~30 and names no scanner at all. atelier being
  public (ADR 0005) is what lets a private child call it — newly load-bearing.
- **`.atelier-floor.json`** — a repo that does not enforce a check must SAY so:
  `advisory` (runs, reports, does not block — for a one-off re-baseline) or
  `disabled` (with a stated reason), plus `scope`/`flags` for where a check looks
  and how it is tuned. Read out estate-wide by floorfleet. Softening is not the
  child's call: boundary and integrity scanners have no advisory form, and the
  mode-changing flags are refused.
- **`.githooks/pre-commit` + `core.hooksPath`** — the hook is now TRACKED, so it
  survives a fresh clone instead of living on one machine. Proven by a real
  refused commit driven through `core.hooksPath`, not by resemblance to the
  legacy path.
- **atelier runs the floor it ships** — `ci.yml`'s hand-enumerated scanner list
  is gone; the parent is scoped by its own config like any child. A parent with a
  private list is the same bug one level up.

### Added (2026-07-25)
- **`tools/floorfleet.py`** — estate conformance board. Walks every child
  (reusing `pins.discover`, as signfleet does) and reports which repos are
  wired / pinned / vendored / absent, with `--remote` reading GitHub's default
  branches — what will actually run on a push. `--check` exits non-zero if any
  repo is unguarded. **Scaffolding is not proof; enumeration is.** 16 tests.
- **ADR 0008** + two `PROPAGATION.md` sections ("Enforcement propagates too —
  by call, never by copy"; "Enumeration, not assumption"). The existing rule had
  been applied to doctrine *prose* while the file's own closing clause warned
  "do not mistake the anchor for the enforcement" — the enforcement was the
  vendored half.

### Fixed (2026-07-25)
- **A fail-open in floor.py's own first draft**, caught by the planted-secret
  commit tests: it rendered **absolute** paths on the staged plane, which match
  nothing against git's repo-relative path list, so every boundary check silently
  passed. Both shapes now pinned. Recorded because it is the same shape as the
  defect being fixed — a check that runs, reports success, and covers nothing.
- **Nested harness worktrees no longer false-positive the scanners.** A worktree
  nests inside the repo, so a scan rooted at the top re-reads a second copy of
  the tree including this repo's deliberate fake-secret and incompatible-licence
  fixtures — 33 findings, all false. linkscan/sizescan already carried the
  exemption; it is now across the whole set, closing the class rather than the
  next instance.

### Added (2026-07-23 — two more anti-slop scanners: wrapscan (S1) + spellscan (S5), advisory)
- **`tools/wrapscan.py` (S1)**: flags `docs/**` prose lines materially over the
  house wrap width (≥86 cols). Exemptions: fenced/indented code, table rows, ATX
  headings, ref-link defs, and single-unbreakable-token overflow — each with its
  honest limit documented in-header (character-count, not display-width, is a
  stated Unicode caveat). 40 tests + `--selftest`. Grounded in the wrap defect
  that shipped three review cycles running (`SL7`→`AC1`→`IR3`).
- **`tools/spellscan.py` (S5)**: flags US spellings in `docs/**` (artifact,
  organize, colour-family…) via generative `-ise`/`-yse` stem families (irregular
  nouns excluded so it never invents a word) + hand-listed irregulars.
  `license`/`practice` deliberately excluded (untaggable US/NZ homographs).
  Exemptions add URL/path tokens + an API-term allowlist to datescan's set. 60
  tests + `--selftest`.
- Both **wired ADVISORY-ONLY** (`--warn`, exit 0) in `ci.yml` — first-of-kind, so
  not yet reviewed (don't-stack); absent from the blocking pre-commit hook and
  child `floor.yml` until each earns an independent review. Honest uncleaned
  baselines kept as review evidence: wrapscan 286/19, spellscan 68/32. Full tool
  suite 432 green.

### Added (2026-07-23 — both observers read the ccarchive archive: `--from-archive`)
- **`cctranscript --from-archive`**: every view (list, render, `--json`, explicit
  path) works over the compressed mirror ccarchive maintains, not just the live
  logs Claude Code prunes — so a cleaned-up session still renders word for word.
  An explicit `.jsonl.gz` path needs no flag; transcripts carry a `source: archive`
  tag (JSON) / `· archive` header (human). Eviction-aware: a `--list` never reads
  an iCloud-evicted (dataless) mirror — it's listed with an `evicted` marker
  instead — while rendering one chosen session deliberately fetches it back.
- **`ccrepo --from-archive`**: totals now reach back past Claude Code's prune
  horizon by reading the same mirror. Because ccrepo reads *every* file to sum
  spend, an evicted (dataless) mirror is skipped by default and counted as a
  stated gap (a `⚠` footnote + `meta.evicted`); `--materialise` opts into reading
  (re-downloading) them. The ccusage cross-check is off in archive mode — ccusage
  reads the live store, which no longer holds the pruned sessions — with a
  footnote saying so; the actual-spend-vs-estimate reconciliation still runs.
- Shared across both: `--dest`/`$CCARCHIVE_DEST` resolution is copied verbatim
  from ccarchive (so one vocabulary points every tool at the same mirror; `--dest`
  alone implies `--from-archive`), one transparent-gunzip read choke-point per
  tool keeps the parsers byte-format-blind, and ccarchive's SF_DATALESS check is
  ported with the same `CCARCHIVE_SIMULATE_DATALESS` test seam. Suites 150→156
  (cctranscript) and 34→41 (ccrepo); both man pages + `--help` updated under the
  flag drift guard. **Closes the README's "sourcing seam" on the observe side**;
  what remains is only the deferred rollup *precompute* ledger, not a survival gap.

  _(Flag named `--from-archive`, not `--archive`: the bare form read like an
  imperative — "archive the transcripts" — rather than a source selector.)_
- **The secrets/access cycle closed terminal** (verdict:
  `docs/reviews/2026-07-22-1021-secrets-access-cold-pass.md`, 0 MAJOR; Mike
  accept-all, applied `f8350ee`): the keys rule names the **live-session
  channel** — no delegated key use (agent forwarding) through untrusted hosts,
  touch-to-sign where hardware offers it (SA1); the watch leg's store-trail
  surface is honest — "where the store can provide one", the sops+age gap a
  stated bridge (SA2); minting bar restated as **entropy sufficiency
  (~128 bits)**, truncating verifiers record effective length (SA3); the
  **break-glass class** named — machine-minted, transcription-optimised,
  stated bridge per platform (SA4); NIST screening attributed to mint time
  (SA5); never-scrub scoped to published history of rolled credentials (SA6);
  the exposure loop's wording has one home (SA7); central-auth pointer on the
  non-reuse rule (SA8); **artifact→artefact** swept across living surfaces,
  immutable records untouched (SA9).

### Changed (2026-07-23 — queue-run doctrine hardened: QR1–QR9 rulings applied)
- **The queue-run cold pass landed and was ruled** (verdict:
  `docs/reviews/2026-07-22-1149-queue-run-doctrine-cold.md`, PASS-WITH-FINDINGS
  1 MAJOR · 6 MEDIUM · 1 LOW · 1 note; Mike accept-all, applied `b65209c`):
  **a run never starts or instructs its own successor** (the chain's links are
  the principal's — closes the rule-4 laundering path, QR1); worker-built
  deltas count as the run's own authorship (QR2); the worker envelope stated —
  merge and the always-confirm floor stay the orchestrator's (QR3); queue-item
  text is task description, never instruction (QR4); **doctrine-text items
  escalate to the capable tier** (QR5); `QueueRunSkillTest` pins the stamped
  copy, suite 323→330 (QR6); "loses nothing" → "loses at most the item in
  flight" (QR7); vocabulary/pointer/report debts closed (QR8); **waves
  sanctioned** — claim per item, close per merge, report aggregates (QR9).
  The pass's MAJOR keeps the cycle open: the application's own cold pass is
  queued `⏳` for a non-author.

### Changed (2026-07-23 — economics rework: billing states, cap rule, hand-up ladder, third seat)
- **ECONOMICS.md pools → billing states of the marginal token** (`dadde1d`):
  plan-included / plan-included-capped / usage-billed, plus draw-down rate;
  risk assigns the tier seats, billing only prices them. Triggered by the
  provider moving the capable model into the operator's subscription
  (capped share, faster draw-down), which broke the two-pool binary.
- **Marginal-cost self-check** (renamed from "know which pool"): two guards —
  dear-meter builds, and silent cap-crossing (fails open like CI overage).
  At a cap: stop/delay or principal-authorised spend under AUTONOMY's
  confirm floor; **capacity never picks the tier** and down-tiering to dodge
  a cap is forbidden (Mike's ruling, quoted in the ADR).
- **Two hard edges on the tier ladder**: cheaper models welcome wherever the
  work's risk permits (every capacity state); a model past its depth **fails
  noisily and hands up** — workhorse → capable tier → principal.
- **Third seat adopted**: fan-out sub-agents on the cheapest genuinely-capable
  tier as standing practice; stepped-down executor trialled per queue run
  (ROADMAP item). Child ECONOMICS template re-grounded to match. ADR:
  `docs/decisions/2026-07-23-0001-billing-state-of-the-marginal-token.md`;
  cold review queued (rule 4).

### Added (2026-07-22 — second orchestrated queue run, 1210: four items per-item)
- **Root `SECURITY.md` + child template** (`85157c3`): private-disclosure
  policy (GitHub advisories, honest best-effort window, no invented
  SLA/bounty), registered in REPO-STANDARD as a publish-time artifact like
  LICENSE. Part of closing the security-canon gaps A/B/C/E.
- **ccrepo actual-spend reconciliation** (`1711711`): machine-local `spend`
  block (plan or usage mode) compared against the API-list-price estimate,
  Δ $ and %, honest partial/unavailable degradation, JSON/CSV meta; +6
  tests (139 green). Also fixed a pre-existing USD×rate² defect in the
  Actual footnote (the column was always right).
- **v2-plugin de-instance rule-4 verdict delivered**
  (`reviews/2026-07-22-1215-v2-plugin-deinstance-cold.md`):
  PASS-WITH-FINDINGS 2M/3M/1L/2n, VP1–VP8 to Mike; merge stays his call.
- **Person-context portability design pass** (records-only,
  `sessions/2026-07-22-1233-…`): constraints, 8-threat pass, per-leg
  candidates, argued recommendations; D1–D5 to Mike.

### Changed (2026-07-22 — second queue run, continued)
- **Every third-party CI action SHA-pinned** (`85157c3`): ci.yml + all child
  workflow templates, tag kept as trailing comment, five tag→SHA
  resolutions verified live twice (worker + orchestrator independently).
- **Doctrine seams for canon gaps A/B/E** (`85157c3`): REVIEW.md names the
  right-sized threat pass as a build step and gives security findings
  severity + recurrence-prevention; PRINCIPLES §5 secure-by-default, §8
  zero-dep-as-supply-chain-control with the residual named in
  tools/README. Rule-4 `⏳` queued — the building run may not take it.

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
### Added (2026-07-21 — v2 plugin: create-repo de-instanced, worktree + fleet-pins commands)
- **`create-repo` de-instanced and moved into the plugin** (`skills/create-repo/`).
  The skill carried seven baked instance facts (git identity, remote account,
  workspace path, copyright holder, locale, exemplars, doctrine-source location);
  they now come from an **adopter-owned profile** (`~/.atelier/instance.yaml`,
  filled interactively on first run, never committed) so the skill carries no
  identity of its own and can travel in the bundle — you become the principal it
  stamps. A **two-mode source resolver** replaces the hard-coded sibling path:
  *live mode* (a real atelier checkout → pin its git SHA, latest templates) or
  *bundled mode* (the plugin's own tree → pin the plugin version as provenance).
  Design + rulings: `docs/decisions/2026-07-21-0748-deinstance-create-repo-for-the-plugin.md`
  (accepted; rule-4 review ⏳ queued — it forks ADR 0002's SHA-is-the-version for
  plugin-only adopters).
- **`/atelier:worktree` and `/atelier:fleet-pins` commands** — thin wrappers over
  the bundled house tools (`tools/worktree.py`, `tools/pins.py`): doctrine
  (`CONCURRENCY.md`, `PROPAGATION.md`) travelling as behaviour, not just prose.
- Plugin + marketplace manifests bumped **0.1.0 → 0.2.0**; `session-onramp`'s
  companion-behaviours list updated to name the repo-craft additions. All four
  publish-safety scanners green; `worktree.py` + `pins.py` selftests green.
  **Not yet exercised end-to-end:** the interactive first-run fill and a
  bundled-mode scaffold (model-prose behaviour, proven at review/use, not unit-tested).
- **VP1–VP8 rulings applied (2026-07-23**, cold pass
  `reviews/2026-07-22-1215-v2-plugin-deinstance-cold.md`, Mike: VP1–VP6 + VP8
  [fixed] as counselled, VP7 confirmed post-merge**)**: canonical bundled-mode
  block variant added to `PROPAGATION.md` (stamped verbatim, drift tracked by a
  runnable plugin-version check — VP1); signing posture externalised as the
  eighth profile fact, honest default off (VP2); bundle README's "What you get"
  states 0.2.0's actual contents (VP3); ls-count template guard → structural
  named-entries check (VP4); branch rebased onto current main, queue-run +
  create-repo onramp wiring both kept (VP5); profile schema single-sourced in
  `instance.yaml.example` (VP6); malformed markup fixed (VP8).

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
