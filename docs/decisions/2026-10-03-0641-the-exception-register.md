# The exception register: every guard exception recorded, and narrowed to the string

**Status**: draft, redrafted 2026-11-09 (`160/650`). Mike rules on acceptance.
• **Date**: 2026-10-03 (first draft); 2026-11-09 (redraft)

**Review**: the first draft's rule-4 design cold pass FAILED it, 3 MAJOR
(`docs/reviews/2026-10-04-2215-exception-register-design-cold.md`, findings
XR1–XR16). Mike approved this redraft on the reviewer's counsel on
2026-11-08 (recorded in `160/650`). The redraft owes a Fable re-review
before acceptance. That pass is Fable work and waits for his approval.

## Drafting history

- **2026-10-03.** First draft, by the queue run that did part 1 of `110/100`.
  It proposed one central JSONL register per repo, hash locators, and the
  retirement of every inline marker and ignore file.
- **2026-10-04.** The cold pass failed it: sound core (required provenance,
  the three-way grant label, string-level narrowness), unsound plumbing (the
  roll-out, staleness, and the claim that every exception fits).
- **2026-11-09.** Redrafted on the reviewer's counsel for every finding. The
  first draft's text is in git history and quoted where the review needs it.
  § *What changed, and why* maps each finding to its change.

## Context

Mike, 2026-10-03, verbatim, in full. He said he has had to repeat it "many
many times", and first asked on 2026-09-12 (`roadmap/110-…/100`):

> I want to be clear that I am seeing too larger gaps in the exceptions used
> for things like leakscan, secretscan and the other guards. I've said many
> many times (I've had to repeat myself to you alot on this) that I want any
> exception to be
> * Specified and recorded so that its clear that the exception exists, why
> it is necessary, who created it (e.g. session transcript ID, did I rule or
> did you do it automatically etc), when the exception was granted, and any
> other relevant and useful info
> * As narrow an exception as possible. I gave the example of a particular
> position in the file or string of characters rather than a whole line in a
> file, or the whole file, or a folder of files.
> For example if every line in a file is secrets then an exception for the
> file makes sense, but if it were one string in the file then only that
> string should be excluded.
> This should be true of binaries, files large and small etc
>
> And the guards need to work efficently and effecitvely. For example we have
> had situations were the guards ran for hours and took GBs of memory that
> stalled the laptop and had to be killed. It should not try and load a whole
> file or all results into memory, it needs to continually close work as it
> opens new work so it can deal with big repos (GB or number of files), big
> files etc

And on 2026-09-12: *"just the specific characters in a text file, not the
file, not the line/row. Same for non-text files."*

**Three requirements:** (1) every exception records why, who (the session,
and whether he ruled it or an agent did it), when, and other useful detail;
(2) every exception is as narrow as possible, down to the string, for text
and binaries; (3) every guard streams.

**A fourth, from his 2026-10-03 correction** (`420/020`): a pick from options
a session offered is an *answer*, not a *ruling*. The record must tell them
apart.

### What exists, measured

From the part 1 audit (`110/100`, at `1685fd8`, 2026-10-03), the cold pass
(2026-10-04) and a floor run on the CI plane on 2026-11-09:

- **26 exception mechanisms.** None records the session or whether Mike
  ruled. Only the floor's `advisory` carries an expiry.
- **Inline markers.** 91 live at the audit, 84 unscoped, but nearly all cover
  a single rule, and only about 3 lines hold more than one finding. On
  2026-11-09 the CI plane reports **132 findings suppressed by marker across 8
  guards** (that is findings, not markers). Not every marker is line-level:
  `sizescan`, `reviewscan`, `licenscan`, `stampscan` and `pointerscan` exempt
  their own unit (a header, a record, a declaration, a block, a pointer).
- **Ignore files.** 36 reasoned lines across 9 ignore files on 2026-11-09 (33
  at the audit). About 14 mask a file or folder for a handful of findings.
  With the ignore files emptied, the cold pass measured 96 `secretscan` and
  137 `leakscan` blocking findings, 229 of them in three test files that are
  mostly code.
- **Binaries.** G3 is built (`020/150`): `.leakscanbinaries` accepts a
  binary by a digest of its bytes, and keeps image metadata set by set and,
  for Exif, IPTC, XMP and PNG text, field by field. `160/980`'s application
  adds who and when to each manifest line as
  `by=<kind> session=<id|human> on=<YYYY-MM-DD>`, chosen to map onto this
  register's fields. `secretscan` still skips a file whose first chunk looks
  binary, and neither guard reads pixels or non-image formats.
- **Floor softening** (`.atelier-floor.json`: `advisory`, `disabled`,
  `scope`, `flags`) already carries a `why` per entry. atelier has 3 `scope`
  entries.
- **`GUARDS.md` § *Who, why, when*** says who and when "come from version
  control". `git blame` cannot name a session, or tell a ruling from an
  answer or an agent's choice. This ADR replaces that section.

### The constraint the first draft missed

Children call atelier's floor at `main`
(`docs/build/templates/workflows/floor.yml`; the rationale is in
`.github/workflows/floor.yml`), and every
hook runs atelier's tools from a shared directory. A scanner change reaches
every child at its **next CI run**, not at a pin bump. So any change that
stops honouring an existing exemption turns every child red the same day.

## Decision (proposed)

**Keep each exemption where it lives, and give every one the same record.**
Inline markers, ignore-file lines, binary-manifest lines and floor softening
entries stay. Each gains the provenance fields below, in one vocabulary
shared with `160/980`'s manifest lines. A marker may narrow to one string on
its line. No exemption that works at the build stops working until Mike rules a dated
retirement, and only after a fleet view shows nothing left to migrate.

### 1. What it covers, and what stays out

**Covered (content and check exceptions):** inline allow-markers, ignore-file
lines, `.leakscanbinaries` lines, and the floor's softening entries
(`advisory`, `disabled`, `scope`, `flags`). The floor entries stay in
`.atelier-floor.json`, at the check and repo levels where `GUARDS.md` puts
them. They gain the same fields there. They are not moved.

**Out, and why, so no reader thinks one listing answers "what is this repo
not looking at":**

- **A scanner's built-in subtractions** (public-key lines, published URLs,
  truncation, the finding cap). They are the rule's own definition, not a
  grant, and each guard already prints their counts (`GUARDS.md` § *Fail
  noisy*).
- **Registry warn-only wiring and the CI plane's reduced `leakscan` cover.**
  These are the floor registry's declarations. Changing them is a doctrine
  change with its own review, not an exception.
- **The hook bypass.** It is side-stepping, governed by `GUARDS.md`
  § *Side-stepping*.
- **Three exemptions that need no reason today:** `reviewscan`'s deferral
  substring, `wrapscan` silencing any line that carries a sibling's marker,
  and the retired `sizescan` budget token. Part 3 decides each one: carry a
  record, or be written down as part of a rule.

### 2. The record

| Field | Token | Required | Meaning |
|---|---|---|---|
| reason | (the marker's or line's reason) | yes | the purpose, as today |
| rule | (the marker's scope) | yes, new form | the rule exempted; `walk` class excepted (below) |
| who | `by=` | yes | kind of grant, below |
| session | `session=` | yes | session ID, `human`, or `unknown` |
| when | `on=` | yes | `YYYY-MM-DD`, UTC |
| where his words are | `ref=` | for `principal-*` | repo path of the record holding his ruling, or the options and his answer |
| review-by | `review-by=` | deferments | `YYYY-MM-DD`; a fleet date also names its kind, `review-kind=mandate` or `default` |
| narrowing | `tok=`, `class=`, `expect=` | per level | § 3 |
| entry | `ex=` | optional | points at an entry file, § 4 |
| notes | (entry file only) | no | anything else useful |

**Kinds of grant (`by=`):**

- `principal-ruled` — his own words decided it. `ref=` names where they sit.
- `principal-answer` — he picked from options a session offered. `ref=` names
  the record of the question and his pick.
- `agent` — a session's own judgement.
- `unrecorded` — migration only, for a legacy exemption whose grantor no
  record shows. It requires `review-by=`, and no helper writes it for a new
  grant. It is the open question Q3.

**Session.** The transcript ID (`$CLAUDE_CODE_SESSION_ID`), `human` when a
person writes the line, or `unknown` (migration only). A subagent shares its
parent's ID, so the field names the top-level session, which is the one a
transcript tool can open. A helper run with no session ID never defaults to
`human`. It writes `by=CHOOSE`, which every loader refuses until a person
states the kind (as `160/980`'s helper already does).

**When.** A date, not a time: the commit that adds the line is the
independent witness of the exact moment. A check reports a line whose
`on=` is later than its commit.

**This is a claim, not proof.** The record is text anyone who can commit can
write. A session can write `principal-ruled` against its own choice, or
quote words he never said. Nothing in a text file can make that impossible.
What the design does is make it checkable: `ref=` must name a tracked file,
so a reader can open his words in one step; and an in-place edit is visible
(§ 4).

### 3. Narrowness: four nested levels, plus the guard's unit

For one finding the levels nest, so "narrowest" has one answer:
**token ⊂ line ⊂ file ⊂ glob.** A guard whose finding is not a string uses
**unit** in place of line.

1. **Token.** A marker carrying `tok=v1:<digest>` exempts only the hit of its
   rule whose *canonical token* has that digest, on that line. The canonical
   token is the hit widened to whitespace on both sides, so a pattern change
   that moves a boundary inside a word does not void it. The digest is the
   first 16 hex characters of SHA-256, as `.leakscanbinaries` uses (below
   `secretscan`'s 32-character entropy threshold, so no advisory noise). The
   `v1` names the scheme, so a later change of scheme is visible. **Required
   when the line holds two or more hits of the marker's rule at grant time**;
   optional otherwise.
2. **Line.** A rule-scoped marker. The new form must name its rule; an
   unscoped legacy marker is reported as "scope it".
3. **Unit.** For `sizescan`, `reviewscan`, `licenscan`, `stampscan` and
   `pointerscan`: the guard's own unit, as today, with the record added.
4. **File.** An ignore line naming one path, or a `.leakscanbinaries` line.
   - *Binary:* G3's digest-bound line, with metadata kept per set and per
     field. The digest re-blocks a changed file.
   - *Text that cannot hold a marker* (JSON, generated output): allowed as is.
   - *Text that can:* only with `class=fixture` and
     `expect=<rule>:<count>[,…]`. More hits under it than expected
     **blocks** on the CI plane: a real value landing in a fixture file (the
     `115/050` near miss) can no longer hide there. Fewer reports "shrink it".
     Editing the file does not re-block, so a test file that changes often
     costs nothing until its findings change.
5. **Glob.** Must name its `class=`: `generated`, `store` (a frozen record
   store), `fixture` (with `expect=`), or `walk` (a walk-scope rule such as
   the nested-worktree pattern, which exempts no finding and so names no
   rule).

**What is decidable, and so reported on every run:** an unscoped marker; a
line marker without `tok=` on a line with two or more hits of its rule; a
fixture entry whose count has moved; and every legacy ignore line, with the
number of findings it covers. No size threshold is set, because none has
been grounded. A file-level entry over a large file stays visible by count.

### 4. Where the fields sit

- **Declaration files** (ignore files, `.leakscanbinaries`): the tokens go in
  the line's reason comment, exactly as `160/980` writes them.
- **Floor softening entries:** the same fields as object keys. `floor.py`
  refuses unknown keys, so it learns them before any repo writes one.
- **Inline markers:** the tokens follow the reason. Where they will not fit
  (a prose line under the wrap limit) or notes are wanted, the marker carries
  `ex=<id>` and the fields sit in an **entry file**: one small JSON file per
  entry, named by its ID, in a directory `.atelier-exceptions` at the repo
  root.

**Entry IDs** are `<YYYYMMDD>-<8 hex>`, the hex being a digest of the
entry's own content. An edit in place no longer matches its ID and is
reported. A change is made by a new entry with `supersedes=<old id>`. One
file per entry means two worktrees granting at once never touch the same
file (the board's 2026-08-15 lesson). A declaration line has no ID, so
the CI pass reports any line whose tokens a push changed rather than added.

The reason stays at the line the reader sees, and a marker moves with its
content through a rename, a copy or an archive move. A path-keyed line
(ignore file, manifest) goes stale on a rename and says so.

**Forward compatibility.** The tokens and `ex=` ride in the reason text. A
scanner that predates this change reads a new-form marker or line as an
ordinary reasoned one. Old tools never refuse new records.

### 5. Stale is a fact about the tree, not about one run

"Matched nothing in this run" and "stale" are different facts. A rule the
plane does not run (`local-term` on CI), a path outside a narrowed scope and
the hook's staged-lines view all produce the first without the second.

**Stale means:** an `ex=` naming no entry file; an entry file no marker
names; a path that no longer exists; a `tok=` whose digest matches no
whitespace-bounded span of its line (this needs no rule and no term list, so
it gives the same answer on every plane); an entry edited in place; a
fixture count exceeded.

**Checked by one whole-tree pass on the CI plane**, reading the declarations,
the marked lines and the entry files, one file at a time. New-form records
that are stale **block**. Legacy forms only report. A marked line too long to
check is reported as unchecked, never as stale.

**On the hook plane**, which sees only staged lines, the check is limited to
what it can decide: a staged new-form marker or line is well formed, and its
`ex=` entry exists. It never reports staleness.

### 6. The transition: both forms work, so no child goes red

- **T0, the build.** Every scanner reads both forms. A legacy exemption
  (no `by=`) keeps exempting exactly what it exempts today, and is counted
  as "unmigrated" without blocking. New-form checks bind only new-form
  records, which no child has yet. A fleet view reports each child's
  unmigrated count: the blast radius is measured before anything moves.
- **T1, migration, repo by repo.** atelier first, then each child through an
  item on its own board. Provenance is recovered from records where it can
  be found, never invented. Over-wide globs are narrowed. Markers inside
  frozen records are never edited: their store is covered by one `store`
  glob that carries a record.
- **T2, retirement of the legacy form.** A separate, dated step that Mike
  rules, taken only when the fleet view shows zero unmigrated. The date names
  its kind, mandate or default (`GUARDS.md` § *Who may move a deferment's
  date*). This ADR does not set it.

### 7. Streaming

No central index is built. Markers are read in the line the scanner already
holds. An `ex=` entry is read on first use and cached, bounded by the number
of markers met. The stale pass reads one file at a time. No guard holds more
than one file's lines plus its own counts.

### 8. The smallest first build (the reviewer's counsel, XR14)

One guard, one repo, additive: `leakscan` in atelier reads the new form
beside the old, for the line, token and fixture levels. Before anything
widens it must prove five things:

1. the hook plane neither blocks nor misreports staleness;
2. a CI runner without the term list stays green;
3. a pattern edit does not void a `tok=` entry;
4. two worktrees granting at once merge cleanly;
5. a scanner from before the change honours a new-form marker.

No child is touched until all five hold.

## Rejected

- **One central register that replaces every marker and ignore file** (the
  2026-10-03 draft). It buys one file to list and string-level cover inside
  fixture files. This design gets the first from each guard's listing of its
  live exemptions and the second from `expect=`. Its costs: a both-forms
  transition anyway (XR1), reasons moved away from the line (XR6), hashes
  that a pattern change voids estate-wide (XR7), and one shared file that
  every grant edits (XR8). It is put to Mike as Q1, because the size is his
  call.
- **A hash of the matched string, anywhere in the file.** It exempts every
  present and future occurrence of a common string, which is wider than
  today's line marker (XR4).
- **A whole-file hash for a text fixture.** Every edit re-blocks it; one test
  file had 16 commits by 2026-10-04.
- **Quoting his words in the record.** A long quote makes the line
  unreadable and copies his words into a second place. `ref=` points at the
  one place they sit.
- **Relying on git alone for who and when.** It cannot name a session or tell
  a ruling from an answer. Git stays as the witness of the moment.

## Consequences

- **Build (part 3)**, priced so it is not a surprise:
  - `allowmarker.py`: parse the tokens and `ex=` from a reason, and the
    shared helper that prints a record (generalising the one `160/980`
    added to `leakscan`).
  - Each scanner that honours markers: report the hit's columns so `tok=` can
    be computed; the boundary scanners compute the digest in process and
    never print the hit.
  - `floor.py`: accept the fields on softening entries; the stale pass and
    the fleet view of unmigrated counts.
  - `publishscan`, `signscan`, `harvestscan` and the board check do not use
    `allowmarker.py`; part 3 lists which of them grant exemptions at all.
- **`160/980` compatibility.** Its `by=`, `session=`, `on=` tokens are this
  vocabulary. Two additive changes follow at the build: its kinds gain
  `unrecorded` (if Q3 is answered yes), and `unknown` is already a valid
  session token by its pattern.
- **Doctrine, rewritten at acceptance, not before:** `GUARDS.md` § *Who, why,
  when* (git is the witness of when; the record carries who and the kind)
  and § *Granularity* (token and unit levels); `REPO-STANDARD.md`; the
  scanners' help text that tells a reader to add a marker; `commands/scan.md`.
- **Templates and scaffolded children.** Files that ship into a child or
  teach the form (outside `tools/`: `commands/scan.md`,
  `docs/build/REPO-STANDARD.md`, the child floor workflow template, the
  create-repo instance example) use inline tokens, never `ex=`, so a
  scaffolded child gets the record with the content.
- **Privacy.** The `why` follows `method/RECORD.md`'s rule for public records
  (no private repo's name joined to its posture). Session IDs and `ref=`
  paths in a public repo are Q2; the draft ADR of 2026-08-05 on
  estate-internal context in public records governs the same class.
- **The digest is not secrecy.** A short string is guessable from its
  digest. The string already sits in the tracked file the record names, so
  the digest adds little exposure; it is there to locate, not to hide.

## Open questions for Mike

Not decided here. Each is for him, in plain words, with a recommendation.

- **Q1 (XR15). How big should this be?** *Small:* keep today's markers and
  ignore files, add who, when and why to each, let a marker narrow to one
  string, and narrow the wide folder exceptions. *Large:* one central file
  that replaces them all. **Recommended: small**, as drafted above. It meets
  all three requirements, nothing goes red, and the large one adds little.
- **Q2 (XR10). In a public repo, may each exception show the session ID and
  point to where your words are recorded?** *Yes, both* (the session logs
  and board already publish short session IDs and those records); *short
  session ID only, no pointer*; or *kind and date only, the session kept
  private*. **Recommended: yes, both, with the 8-character short session
  ID**, which is how the records already cite sessions.
- **Q3 (first draft's open question; XR13). Old exceptions with no record of
  who granted them:** mark them *unrecorded*, with a review-by date that
  forces someone to look; or *re-grant each one* by a session or by you
  before the old form retires. **Recommended: unrecorded with a review-by
  date.** It is honest and does not invent who granted them.
- **Q4 (XR11). Binary files are only partly checked.** The guards check a
  binary's name, whether it changed, and the metadata of three image
  formats, field by field. Nothing reads the pixels, other formats' insides,
  or (for `secretscan`) a binary's bytes at all. An exception cannot be
  narrower than what is scanned. *Open a separate investigation into
  scanning binary contents*; or *accept and write down the gap*.
  **Recommended: a separate, scoped investigation**, kept out of this
  register so it does not hold the rest up.

## What changed, and why

| Finding | Change in this redraft |
|---|---|
| XR1 MAJOR, retiring markers reds every child | Markers and ignore files stay; both forms honoured; T0–T2 with a fleet count first and retirement a later ruled step (§ 6). |
| XR2 MAJOR, "matched nothing blocks" | Stale redefined as tree facts, checked by one CI pass; the hook checks form only (§ 5). |
| XR3 MAJOR, "every exception lives there" | Claim narrowed and the exclusions named; floor keys gain the fields in place; unit level for non-string findings (§ 1, § 3). |
| XR4 MODERATE, not a ladder | Levels nest per finding; match-anywhere dropped; `file` for fixtures made decidable by `expect=`; sizes stated (§ 3, Context). |
| XR5 MODERATE, provenance is asserted | Said plainly; `ref=`, content-hash IDs, supersede-not-edit, commit-date cross-check, `by=CHOOSE` and no `human` default (§ 2, § 4). |
| XR6 MODERATE, reason leaves the line | Hybrid adopted: the record sits at the line or names its entry; markers travel; templates carry inline tokens (§ 4, Consequences). |
| XR7 MODERATE, hash tied to match text | Canonical whitespace-bounded token, versioned scheme; the per-scanner plumbing priced (§ 3, Consequences). |
| XR8 MODERATE, one append-only file | One entry file per ID; declaration lines stay where they were (§ 4). |
| XR9 minor, "never stored" | Claim withdrawn; 16-hex digests avoid the entropy advisory (§ 3, Consequences). |
| XR10 minor, publishing IDs and rulings | Not decided: Q2. His words are pointed at, not copied (Rejected). |
| XR11 MODERATE, binaries | Updated for G3 as built (field-level metadata); the remaining gap stated as Q4. |
| XR12 minor, facts | Corrected: findings vs markers, unit-level markers, scanners not using `allowmarker.py` (Context, Consequences). |
| XR13 note, small points | No central index; `walk` class needs no rule; `unrecorded` kind defined; review-by kind added; the unbuilt helper is not named by path. |
| XR14 note, first build | Adopted, plus a fifth proof, forward compatibility (§ 8). |
| XR15 MODERATE, larger than the gap | The small design is the proposal; the large one is rejected here and put to him as Q1. |
| XR16 note, cut quotation | His words now quoted whole (Context). |

Not taken: none. One part of XR13 (the nested-worktree glob may already be
dead since `110/110`) is left to the part 3 migration to probe, not assumed.
