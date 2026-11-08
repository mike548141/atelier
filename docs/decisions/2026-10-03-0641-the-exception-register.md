# The exception register: every guard exception in one central file, narrowed to the string

**Status**: draft, reworked 2026-11-09 to the central-file shape on Mike's
answers (`160/650`). Mike rules on acceptance.
• **Date**: 2026-10-03 (first draft); 2026-11-09 (redraft, then this rework)

**Review**: the first draft's rule-4 design cold pass FAILED it, 3 MAJOR
(`docs/reviews/2026-10-04-2215-exception-register-design-cold.md`, findings
XR1–XR16). Every finding is answered below (§ *What changed, and why*). This
rework owes a Fable re-review before acceptance (`160/1130`). That pass is
Fable work and waits for his approval.

## Drafting history

- **2026-10-03.** First draft, by the queue run that did part 1 of `110/100`:
  one central JSONL register per repo, hash locators, every inline marker and
  ignore file retired.
- **2026-10-04.** The cold pass failed it: sound core (required provenance,
  the three-way grant label, string-level narrowness), unsound plumbing (the
  roll-out, staleness, and the claim that every exception fits). XR15 added
  that it was larger than the measured gap, and asked that he be offered two
  sizes.
- **2026-11-09, redraft.** Mike approved a redraft on the reviewer's counsel
  (2026-11-08, `160/650`). It proposed the **small** design: keep every marker
  and ignore file where it is and add who, when and why to each. It
  **recommended small** and put the size to him as Q1.
- **2026-11-09, this rework.** He answered the four questions (answers to
  options offered, not rulings; recorded in `160/650`). On Q1 he chose
  *"Large: one central file"*, the option that was **not** recommended. So
  this draft returns to one central file, and keeps from the redraft
  everything that fixed the first draft's plumbing: the both-forms
  transition, staleness as a fact about the tree, and the shared vocabulary.
  The review's objections to a central file still stand as costs. § 8 prices
  them and says how the design pays each one. The first draft's text and the
  small design are in git history.

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
  2026-11-09 the CI plane reports **136 findings suppressed by marker across 8
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
  binary, and neither guard reads pixels or non-image formats. Reading inside
  binaries is out of this design, on his answer to Q4, and is filed as
  `115/390`.
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

**One central register file per repo is the single home of its exemptions.**
Every inline allow-marker, ignore-file line and binary-manifest line moves into
it, as one self-describing entry. Each entry says what is exempted, as narrowly
as the finding allows (down to one string), and why, who and when, in the
vocabulary `160/980` already put on manifest lines.

Nothing works differently on the day this ships. Both forms are honoured, a
repo with no register behaves exactly as it does now, and the old forms retire
only on a later, dated ruling of his (§ 6).

### 1. What the register holds, and what stays out

**Moves in:** inline allow-markers, lines in the `.<scanner>ignore` files, and
`.leakscanbinaries` lines. The manifest is an ignore file in all but name, and
`leakscan`'s own comment already expects its lines to migrate as they are.

**Stays where it is, gaining the same fields:** the floor's softening entries
in `.atelier-floor.json` (`advisory`, `disabled`, `scope`, `flags`). They are
check-level and repo-level settings, read by the floor before any scanner
starts; the option he picked replaced the markers and ignore files, not these.
They are already one file per repo, and each already states a `why`. `floor.py`
refuses unknown keys, so it learns the new fields before any repo writes one.
The listing in § 7 prints both files, so one command shows every granted
exemption. The things below are not grants and are not in it.

**Out, and why, so nobody reads the register as the whole answer:**

- **A scanner's built-in subtractions** (public-key lines, published URLs,
  truncation, the finding cap). They define the rule and grant nothing; each
  guard already prints their counts (`GUARDS.md` § *Fail noisy*).
- **Registry warn-only wiring and the CI plane's reduced `leakscan` cover.**
  Declarations of the floor registry; changing them is a doctrine change.
- **The hook bypass.** Side-stepping, governed by `GUARDS.md`
  § *Side-stepping*.
- **Three exemptions that need no reason today:** `reviewscan`'s deferral
  substring, `wrapscan` silencing any line that carries a sibling's marker, and
  the retired `sizescan` budget token. Part 3 decides each: carry a record, or
  be written down as part of a rule.

### 2. The file

One file, `.atelier-exceptions.jsonl`, tracked, at the repo root, holding one
JSON object per line. The order of lines carries no meaning. No file means no
entries.

```
{"id":"20261109-3fa91c07","guard":"leakscan","rule":"email","level":"token","path":"docs/example.md","tok":"v1:9c1f4e2ab07d3165","n":1,"why":"reserved example domain in a worked example","by":"agent","session":"0a1b2c3d","on":"2026-11-09"}
```

**This is literally one file, not a directory of them.** XR8 offered two ways
to survive parallel sessions: one small file per entry, or one file with a
declared union merge and a duplicate-ID check. The first would have been a
stretch of his words: one folder is a central place, but it is not "one
central file". The second keeps his words, so this draft takes it.

- **Append-only.** A commit may only add lines. Changing an entry means adding
  a new one with `supersedes=<old id>`. Withdrawing one means adding an entry
  with `level` `retired` and `supersedes`. The hook refuses a staged change or
  removal of an existing line. The CI pass re-checks each push against its
  base (the floor's checkouts carry full history), so a bypassed hook is
  still caught.
- **Declared merge.** The repo's `.gitattributes` gives this file git's
  built-in union merge, so two branches that each add entries merge with both
  kept. Probed in a throwaway repository on 2026-11-09: a merge and a rebase
  of two concurrent appends were both clean and kept both lines. Without the
  attribute the same merge is an ordinary conflict, which is loud and safe.
- **Why append-only is load-bearing.** The same probe confirmed union's one
  trap: a line deleted on one branch beside another branch's append silently
  **comes back**. In this file a deletion never happens, so nothing can
  return. A retired entry stays retired whichever way a merge falls, because
  retirement is itself a line.
- **Duplicate check.** Two byte-identical lines are harmless. Two lines with
  one `id` and different content block on CI.
- **Why this differs from the board** (ADR `2026-08-15-0610`, one file per
  item). The three incidents behind that decision were sessions overwriting
  each other's edits to a file both were changing. Register lines are never
  changed after they land, and adding lines side by side is the one case union
  merge handles. If the first build shows the merge route failing (§ 9, proof
  4), a directory of entries is the fallback, and that would be put to him.

**Entry IDs** are `<YYYYMMDD>-<8 hex>`, the hex being a digest of the entry's
other fields. An edit in place no longer matches its ID, and is reported.

### 3. The record

The key names are the tokens on `.leakscanbinaries` lines, so a manifest line
moves across with its values unchanged.

| Field | Required | Meaning |
|---|---|---|
| `id` | yes | § 2 |
| `guard` | yes | the scanner; `*` only for the `walk` class |
| `rule` | yes | the rule exempted; `walk` class excepted |
| `level`, `path` and the level's fields | yes | § 4 |
| `why` | yes | the purpose, as a marker's reason says it today |
| `by` | yes | the kind of grant, below |
| `session` | yes | 8-character short session ID, `human`, or `unknown` |
| `on` | yes | `YYYY-MM-DD`, UTC |
| `ref` | for `principal-*` | tracked path of the record holding his words |
| `review-by` | deferments, `unrecorded` | `YYYY-MM-DD` |
| `review-kind` | a fleet-set date | `mandate` or `default` |
| `supersedes` | replacing an entry | the old `id` |
| `notes` | no | anything else useful |

**Kinds of grant (`by`):**

- `principal-ruled` — his own words decided it. `ref` names where they sit.
- `principal-answer` — he picked from options a session offered. `ref` names
  the record of the question and his pick.
- `agent` — a session's own judgement.
- `unrecorded` — migration only, on his answer to Q3: an old exemption whose
  grantor no record shows. It needs `review-by`, its `session` is `unknown`,
  and no helper writes it for a new grant.

**Session (his answer to Q2).** The first 8 characters of the transcript ID,
which is how the records already cite sessions. A subagent shares its parent's
ID, so the field names the top-level session. A helper run with no session ID
never defaults to `human`: it writes `by=CHOOSE`, which every loader refuses
until a person states the kind, as `160/980`'s helper already does.

**Pointer to his words (Q2).** `ref` must name a file tracked in this repo, so
a reader opens his words in one step. His words are pointed at, never copied
in. If they are recorded nowhere in the repo, they get recorded first.

**When.** A date, not a time; the commit that adds the line is the independent
witness of the moment. A check reports an entry whose `on` is later than its
commit. For `unrecorded` entries, `on` is the date the old exemption first
appears in git, the only witness there is.

**Past `review-by`.** It behaves as an expired floor advisory does: red on the
floor line and the fleet board, saying how many days it has stood, and it
blocks nothing. Someone is made to look, and no commit fails on a date set
months earlier. Each repo's migration item sets the dates for its own entries.
A date set for the whole fleet names its kind (`GUARDS.md` § *Who may move a
deferment's date*).

**This is a claim, not proof.** An entry is text anyone who can commit can
write. A session can write `principal-ruled` against its own choice, or point
`ref` at a file that holds no such words. Nothing in a text file can make that
impossible, and no tool compares `ref` with what he said. What the design
gives is checkability: every claim sits in one file, `ref` opens in one step,
the `agent` and `principal-*` entries can be listed and sampled, and an entry
cannot be quietly rewritten afterwards (§ 2).

### 4. Narrowness: how an entry far from the line still hits one word

An entry names no line number, because line numbers move. It names the string
itself, by digest, and how many copies of it the file may hold.

For one finding the levels nest, so "narrowest" has one answer:
**token ⊂ line ⊂ file ⊂ glob.** A guard whose finding is not a string uses
**unit** in place of line.

1. **Token** (`level` `token`; `path`, `tok`, `n`, optional `w` and `ctx`). Exempts
   hits of its rule, in that file, whose *canonical token* has that digest.
   - **Survives a pattern change.** The canonical token is the hit widened to
     whitespace on both sides, so a pattern edit that moves a boundary inside
     a word does not void the entry. `tok` is `v1:` plus the first 16 hex
     characters of SHA-256. The digest is below `secretscan`'s 32-character
     entropy threshold, and `v1` makes any later change of scheme visible. A
     hit of several words is digested with its inner whitespace collapsed, and
     `w` records how many words it spans (default 1), so the rule-free checks
     below can look for it. A hit that spans several lines has no single token,
     so the guard treats it as a unit (level 3).
   - **Survives line moves.** Nothing in the entry depends on where the line
     is, so inserted lines, moved blocks and paragraph reflow leave it good.
   - **Cannot spread.** `n` is how many copies of that token the file may
     hold, set at grant. The count is of whitespace-bounded spans, not of a
     rule's hits, so it needs no rule or term list and gives the same answer
     on every plane. More copies than `n` **blocks** on CI, saying found and
     allowed. Fewer reports "shrink it". This is what makes a string entry
     narrower than a line marker rather than wider: a common word excused
     once is not excused wherever it next appears (XR4).
   - **One word on one line** (`ctx`). When the same string sits elsewhere in
     the file and those copies must stay unexempted, `ctx` adds a digest of
     the rest of that line, with whitespace collapsed. Only the copy on a line
     with that context is exempt. It still survives line moves, but an edit
     to that line voids it, loudly. `ctx` is **required** at grant when the
     file holds more copies than the entry covers. It is otherwise left off,
     so that prose reflow does not void entries for nothing.
2. **Line** (`level` `line`; `path`, `ctx`). For a finding that is the whole
   line, such as `wrapscan`'s, where there is no string to name.
3. **Unit** (`level` `unit`; `path`, `unit`). For `sizescan`, `reviewscan`,
   `licenscan`, `stampscan` and `pointerscan`: the guard's own unit (a header,
   a record, a declaration, a block, a pointer), named as the guard names it.
4. **File** (`level` `file` or `binary`; `path`).
   - *Binary:* `.leakscanbinaries`' digest-bound acceptance moves in unchanged
     (`digest`, plus `set` and `field` for metadata kept per set and per
     field), one entry per manifest line. A changed binary re-blocks. An
     exemption cannot be narrower than what is scanned; inside a binary that
     is image metadata only, and the rest is `115/390`.
   - *Text:* only with a `class`. `fixture` also needs
     `expect=<rule>:<count>[,…]`: more hits than expected **blocks** on CI, so
     a real value landing in a fixture file (the `115/050` near miss) cannot
     hide there; fewer reports "shrink it". Editing the file does not re-block,
     so a test file that changes often costs nothing until its findings
     change. This is wider than his "only that string", and is kept because
     three test files alone hold 229 fixture findings (XR4). `generated` and
     `store` (a frozen record store) need only the `class`.
     His own example fits here: a file where every line is a secret.
5. **Glob** (`level` `glob`; `path` is the pattern). Must name its `class`:
   `generated`, `store`, `fixture` (with `expect`), or `walk` (a walk-scope
   rule such as the nested-worktree pattern, which exempts no finding, names
   no rule, and takes `guard` `*` so it is one entry, not one per guard).

**What is decidable, and so reported on every run:** a token entry without
`ctx` where the file holds more copies than `n`; a fixture whose count has
moved; a file or glob entry with no `class`, which is refused; and every legacy
marker and ignore line still unmigrated, with the findings it covers. No size
threshold is set, because none has been grounded.

### 5. Stale is a fact about the tree, not about one run

"Matched nothing in this run" and "stale" are different facts. A rule the plane
does not run (`local-term` on CI), a path outside a narrowed scope and the
hook's staged-lines view all produce the first without the second.

**Stale means:** a `path` that no longer exists; a glob that matches no tracked
file; a `tok` whose digest matches no whitespace-bounded span of the file; a
`ctx` matching no line of it; an entry whose `id` no longer matches its fields;
a `supersedes` naming no entry; a `ref` that is not a tracked file. None of
these needs a rule or a term list, so each gives the same answer on every
plane.

**Checked by one whole-tree pass on the CI plane**, reading the register and
then each file it names, one file at a time. Stale entries **block**. Over-count
findings (§ 4) block in the same pass. A line too long to check is reported as
unchecked, never as stale.

**On the hook plane**, which sees only staged lines, the check covers what the
staged state can decide: new entries are well formed; no existing line changed
or vanished; and a path this commit deletes or renames leaves no live entry
behind. That last point moves the cost of a rename to the moment it is made.
The hook never judges staleness from what matched, and it does not count
copies, so one beyond `n` passes the hook and blocks on CI. It reads the
register from the staged copy, as `leakscan` already does for
`.leakscanbinaries`, so an uncommitted entry exempts nothing.

### 6. The transition: both forms work, so no child goes red

Children call the floor at `main`, so a scanner change reaches every child at
its next CI run (§ *The constraint* above). The design has to be safe on that
day.

- **T0, the build.** Every scanner reads the register **and** the old forms; a
  finding is exempt if either covers it. A legacy exemption keeps exempting
  exactly what it exempts now, and counts as "unmigrated" without blocking.
  Register checks bind only register entries, which no child has yet. No
  register file means no change at all. A fleet view reports each child's
  unmigrated count, so the blast radius is measured before anything moves.
- **T1, migration, repo by repo.** atelier first, then each child through an
  item on its own board. In each repo the entries land first; a dry run shows
  the register alone covers what the old form covered; only then are the
  markers and ignore lines removed. Provenance is recovered from records where
  it can be found, never invented; otherwise the entry is `unrecorded`. Wide
  globs are narrowed as they move. A marker for a term-list rule is migrated
  on a machine that has the list. Frozen records are never edited: their
  markers stay as text, and their store is covered by one `store` entry.
- **Precondition for T1.** A repo migrates only once the tools its own hook
  runs can read the register. An older tool on a migrated repo cannot see its
  entries and would report the findings: loud, not silent, but avoidable. The
  fleet view shows this before a repo starts.
- **T2, retirement of the old forms.** A separate, dated step that Mike rules,
  taken only when the fleet view shows zero unmigrated. The date names its
  kind, mandate or default. **This ADR does not set it**, and until he rules
  it, a marker that works keeps working.

### 7. Reading the register, and streaming

Each scanner reads the file once, line by line, into a small index: exact
paths mapped to their entries, plus the list of globs (XR13). Its size follows
the number of entries, not the size of the repo. A hit's digest is computed in
process, from the line the scanner already holds, and the hit is never printed.
The stale pass reads one file at a time. No guard holds more than one file's
lines, this index, and its own counts.

**A listing** prints a repo's live exemptions from the register and
`.atelier-floor.json`, by path or for the whole repo, with the current line and
column of each one and the context masked. It stands in for the reason that
used to sit on the line (§ 8).

### 8. What the central choice costs, and how each cost is paid

The review said a central file was the wrong call for several reasons (XR6,
XR8, XR15). He has weighed the size and chosen this. Its costs are stated here
so that they are bought knowingly.

| Cost | Plainly | How the design pays it |
|---|---|---|
| **The reason leaves the line** (XR6) | Someone reading a file sees a suspicious string with nothing beside it. | The listing, by path. A guard's message names the entry when one nearly matches. Residual: reading the file alone no longer explains it. `GUARDS.md`'s "on the line or in the file a reviewer reads" is rewritten at acceptance. |
| **A diff shows a digest, not the string** (XR6) | The reviewer sees path, rule and reason, but not the excused text. | Each CI run prints the entries that push added, resolved to line and column. Residual: the text itself takes one step to see. |
| **Entries do not travel with content** (XR6) | A rename, an archive move or a copy leaves the entry behind; a marker went with its line. | The hook stops a rename that strands a live entry; a superseding entry repairs it. A copy needs its own grant, which is stricter than a marker that travelled unreviewed. `store` entries cover archives. |
| **Scaffolded children** (XR6) | Template content arrives in a child with no entry. | Scaffolding writes the template's seed entries into the child's new register, under the scaffolding session. |
| **One file every grant touches** (XR8) | Parallel sessions all add to it. | Union merge plus append-only (§ 2), and the merge route is a first-build proof. |
| **More to build, and to migrate** (XR15) | It is larger than the gap the audit measured. The small design added fields where each exemption already sat; this moves every one and adds a shared loader, a listing and a migration helper. In atelier alone, 136 findings are suppressed by marker and 36 ignore lines stand. | The smallest first build stays additive (§ 9); T1 runs repo by repo. Residual: this is the real price of the choice. |
| **Two places during transition** (XR1) | Until T2 an exemption may sit in either form. | The fleet view counts what is left. |
| **The register must be read before scanning** | Slightly against "should not load a whole file". | § 7: a small index bounded by the entry count, never by repo or file size. |
| **`ctx` voids on a line edit** (XR4) | Editing that line blocks until a new entry lands. | Used only where the string repeats and only one copy is excused. |

**What it buys:** one place to read everything a repo excuses; every new grant
visible in one file's diff; string-level cover without touching the content;
and no exemption that copies itself along with a pasted line.

### 9. The smallest first build (the reviewer's counsel, XR14)

One guard, one repo, additive: `leakscan` in atelier reads the register beside
its markers, for the token, line and fixture levels. Before anything widens it
must prove five things:

1. the hook plane neither blocks wrongly nor misreports staleness, and honours
   only a staged entry;
2. a CI runner without the term list stays green;
3. a pattern edit does not void a token entry, and a moved line does not;
4. two worktrees granting at once land cleanly through every route work lands
   by, including a pull-request merge on the host, not only a local merge;
5. a tool from before this change, on a migrated repo, fails loudly and never
   passes quietly.

No child is touched until all five hold.

## Rejected

- **Today's markers and ignore files, each with provenance added** (the small
  design). The redraft recommended it, and he chose the central file instead.
  Its record survives here as the register's fields.
- **A marker at the line pointing to its entry** (XR6's hybrid, the redraft's
  `ex=<id>`). It keeps the reason at the point of use, but it keeps the
  scattered notes he chose to replace.
- **One small file per entry, in a directory.** It avoids merge handling
  entirely and is the fallback in § 2, but it is not "one central file".
- **An entry that excuses a string anywhere in a file, with no count.** Every
  future occurrence would be excused too, which is wider than a line marker
  (XR4).
- **A whole-file hash for a text fixture.** Every edit re-blocks it; one test
  file had 16 commits by 2026-10-04.
- **Quoting his words in the record.** It makes the entry unreadable and copies
  his words into a second place.
- **Relying on git alone for who and when.** It cannot name a session or tell
  a ruling from an answer. Git stays as the witness of the moment.

## Consequences

- **Build (part 3)**, priced so it is not a surprise:
  - `allowmarker.py`: the shared register loader beside the marker parser, and
    the helper that prints an entry (generalising the one `160/980` added to
    `leakscan`).
  - Each scanner that honours exemptions: consult the register, and report the
    hit's columns so a digest can be computed in process. Part 3 lists which of
    `publishscan`, `signscan`, `harvestscan` and the board check grant
    exemptions at all, since they do not use `allowmarker.py`.
  - `floor.py`: accept the fields on softening entries; the stale pass; the
    fleet view of unmigrated counts; the listing.
  - The hook: read the register from the staged copy; the append-only and
    stranded-path checks.
  - The migration helper; the `.gitattributes` line; scaffolding's seed
    entries.
- **`160/980` compatibility.** Its `by`, `session`, `on` are this vocabulary,
  and `.leakscanbinaries` lines move in with their values. Two additive changes
  at the build: its kinds gain `unrecorded` (his answer to Q3), and its helper
  writes the 8-character session form. `unknown` is already a valid session
  token by its pattern.
- **Doctrine, rewritten at acceptance, not before:** `GUARDS.md` § *Who, why,
  when* (git is the witness of when; the record carries who and the kind) and
  § *Granularity* (token and unit levels); `REPO-STANDARD.md`; the scanners'
  help text that tells a reader to add a marker; `commands/scan.md`.
- **Templates and scaffolded children.** Files that ship into a child or teach
  the form (`commands/scan.md`, `docs/build/REPO-STANDARD.md`, the child floor
  workflow template, the create-repo instance example) move to the register
  form at T1, with the seed entries of § 8.
- **The register is scanned like any other file.** It holds digests under the
  entropy threshold (XR9), and needs no exemption for itself. A `why` that trips
  a guard is rewritten. That no self-exemption is needed is checked in the first
  build rather than assumed.
- **Privacy (his answer to Q2).** Short session IDs and `ref` paths appear in
  public repos. `why` follows `method/RECORD.md`'s rule for public records, and
  the draft ADR of 2026-08-05 on estate-internal context in public records
  governs the same class (XR10).
- **The digest is not secrecy.** A short string is guessable from its digest.
  The string already sits in the tracked file the entry names, so the digest
  adds little exposure; it is there to locate, not to hide.

## Open questions for Mike

None at present. What remains his: accepting this design once its re-review has
run, approving the Fable re-review itself (`160/1130`), and the dated ruling
that retires the old forms (T2). His four answers are folded in above: Q1 is
the whole of the design, Q2 § 3, Q3 § 3 and § 6, Q4 Context and § 4.

## What changed, and why

| Finding | Where it is met under the central shape |
|---|---|
| XR1 MAJOR, retiring markers reds every child | Both forms honoured from T0; T2 is a later dated ruling of his, only at zero unmigrated; fleet count first; T1 precondition on the hook's tools (§ 6). |
| XR2 MAJOR, "matched nothing blocks" | Stale is a fact about the files, rule-free, checked once on CI; the hook decides only what staged state can (§ 5). |
| XR3 MAJOR, "every exception lives there" | Claim narrowed and the exclusions named; floor keys gain the fields in place and the listing prints both; unit level for non-string findings (§ 1, § 4, § 7). |
| XR4 MODERATE, not a ladder | Levels nest; the count `n` stops a string entry spreading; `ctx` isolates one copy; `file` is decidable by `class` and `expect`; sizes stated (§ 4, § 8). |
| XR5 MODERATE, provenance is asserted | Said plainly. `ref`, content-hash IDs, append-only and supersede, commit-date cross-check, `by=CHOOSE` and no `human` default (§ 2, § 3). |
| XR6 MODERATE, reason leaves the line | Cost accepted on his choice and stated. Paid by the listing, CI's print of added entries, the stranded-path check, scaffolding seeds. The hybrid is rejected, with its reason (§ 7, § 8, Rejected). |
| XR7 MODERATE, hash tied to match text | Canonical whitespace-bounded token, versioned scheme, `n` counted over spans; per-scanner plumbing priced (§ 4, Consequences). |
| XR8 MODERATE, one append-only file | XR8's second counsel: one file, union merge, duplicate-ID check; append-only closes union's resurrection trap, probed; the merge route is first-build proof 4; directory is the named fallback (§ 2, § 9). |
| XR9 minor, "never stored" | Claim withdrawn; 16-hex digests avoid the entropy advisory; no self-exemption, checked at first build (§ 4, Consequences). |
| XR10 minor, publishing IDs and rulings | His answer to Q2: 8-character ID and a pointer. His words are pointed at, not copied (§ 3, Rejected). |
| XR11 MODERATE, binaries | G3 moves in unchanged, field-level metadata intact; the rest is out of this design on his answer to Q4, filed as `115/390` (Context, § 4). |
| XR12 minor, facts | Corrected: findings vs markers, unit-level markers, scanners not using `allowmarker.py` (Context, Consequences). |
| XR13 note, small points | Index is paths plus a glob list; `walk` needs no rule and takes `guard` `*`; `unrecorded` defined; review-kind added; the unbuilt helper is not named by path (§ 3, § 4, § 7). |
| XR14 note, first build | Adopted; proof 4 extended to the host's merge; proof 5 rewritten, because an old tool cannot read a register (§ 9). |
| XR15 MODERATE, larger than the gap | Stands as a cost. The small design was recommended and put to him; he chose the central file (Drafting history, § 8). |
| XR16 note, cut quotation | His words quoted whole (Context). |

Not taken: none. One part of XR13 (the nested-worktree glob may already be
dead since `110/110`) is left to the part 3 migration to probe, not assumed.
