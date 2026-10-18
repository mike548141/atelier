# Cold pass — cctranscript's harness classification, shared with ccclose

**Pass type:** code cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection by whoever takes the pass.
**Status:** BRIEF ONLY — the review has NOT run. Written 2026-10-17 UTC by an Opus
brief-writer; the pass waits for a further cold Fable session that neither the
delta's author nor this brief-writer (nor its orchestrator) started or instructed.
Tier is checked at selection (rule 4).
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/880-rule-4-cold-pass-queued-harness-classification.md`.
**Why it earns a review:** it changes who the house's transcript reader says typed what.
Its prompt counts and refs are quoted into records as evidence of the principal's
words, the authorship rule turns on them, and the same classifier now decides which
prompts the close-out checker treats as the principal's asks.

## Spawn provenance

- **Author of the work under review:** the queue run whose intent record is dated
  2026-10-16 15:01 UTC (an Opus orchestrator with dispatched workers; the pointer counts
  the worker's output as the run's authorship; the commit's trailer names a Sonnet
  model). Not opened here.
- **Who wrote this brief:** an Opus subagent (`claude-opus-5-5`) dispatched on 2026-10-17
  by the Mike-opened Fable review session working in worktree `atelier-review-1017`, on
  Mike's 2026-10-16 answer that a fresh Opus session writes these briefs. It authored
  none of the delta. It is **off-tier for review, disclosed: it forms no finding and
  writes no severity**, and it stops after this brief and its sibling.
- **Who takes the review:** a further cold Fable session, not yet started, that passes
  rule 4's criterion. If it runs as reviewer-plus-orchestrator, rule 4's off-tier
  conditions apply and are disclosed in the claim, the pointer and the verdict. The
  reviewer repeats its own provenance in its verdict.
- ⚠️ **Exposure, disclosed** (rule-2 material met before writing). This brief-writer
  read: its instruction file; the four queue pointers it was assigned (160/860–890) in
  full, and 160/500 in full as the shape of an append line (including that item's
  result line); the staging directory's file listing, and the first 50 lines of one
  peer brief of this batch (160/850) and its append, for shape; the landing commit's
  subject, `--stat`, diff on `instruments/cctranscript`, `instruments/ccclose`, the
  README and the design note, **and message body** (the author's own account, with
  counts from a real transcript store), and the merge's message body; grep-hit lines
  for the `'you'` role in the instruments; while writing the sibling pass 160/870's
  brief, `instruments/ccclose.design.md` whole and parts of `instruments/ccclose`;
  three templates in full; `docs/reviews/` filenames and filename-level greps (no prior
  verdict opened); and its harness-loaded memory index, which holds one-line notes on
  transcript authorship. Writing the other briefs of its set, it also read the 160/860
  and 160/890 deltas' diffs and message bodies, and grep-hit lines of a sweep that
  included single lines of board items 115/290 and 115/320. It did not open the intent
  record, the commissioning item,
  `docs/SESSIONS.md`, `docs/sessions/`, `docs/ROADMAP-DONE.md` or
  `docs/method/REVIEW.md`, and did not read the tests' or man page's diffs. What its
  orchestrator read is the orchestrator's to disclose; it passed on an instruction
  file, three templates and a list of taken prefixes, and no evaluative content.
  Everything evaluative is in the sibling.

## What the work is

Landing commit (diff it; review the paths at HEAD, `2f9cfe4` or later):

- `cea247e` (2026-10-16 16:43 UTC) — cctranscript: classify harness text in user records
  instead of counting it as prompts; landed in merge `99f4c2a` (2026-10-16 16:48 UTC,
  "merge: cctranscript stops crediting harness text to the principal (210/250)"), which
  changes none of the delta paths against `cea247e` (checked)

Delta paths (the pointer's own list): `instruments/cctranscript`,
`instruments/cctranscript.test.js`, `instruments/man/cctranscript.1`,
`instruments/ccclose`, `instruments/ccclose.test.js`, `instruments/ccclose.design.md`
(§6) and `instruments/README.md` (the header-line section). In cctranscript the new
surface is `HARNESS_TAGS`, `COMMAND_TAGS`, `JOINED_TAGS`, `stripElements`,
`classifyUserRecord`, the `harness` role and its render, the first-prompt label in
`--list`, search, the header chips and the exports; in ccclose, `stripWrappers` and the
user-record branch of `readTranscript`.

ccclose itself landed twenty minutes earlier (`4eda680`, merged `6ccbc7a`) and is pass
160/870's subject. Review ccclose's use of the shared classifier here; leave ccclose's
other code to that pass. Nothing touches the delta paths after `99f4c2a`.

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code, tests and
live behaviour. The lenses organise it; they do not bound it. Non-goals are the only
narrowing and are themselves reviewable.

Probe, at least:

- **The classifier's decision table.** For `classifyUserRecord` and `stripElements`,
  enumerate inputs and record the verdict: `isMeta` set; wholly one wrapper; several
  wrappers; wrapper plus whitespace; wrapper plus a sentence; a wrapper with attributes,
  upper case, a self-closing form, a nested same-name element, or no closing tag; a
  joined `browser_instruction` before, after and inside a prompt; a principal prompt
  that pastes or quotes a wrapper; content as a string, as text blocks, as image-only
  blocks. Which inputs move a real prompt to `harness`, and which leave harness text as
  `you`?
- **Numbering invariance.** The refs (`N`, `N.M`, `N+K`) are quoted in committed
  records. Re-drive old against new on synthetic transcripts and record any ref that
  moves, including where a record that used to be a prompt now classifies as `null`.
- **Every consumer.** `readTurns`, `numberTurns`, the `--list` first-prompt label,
  `--search` and its table, the header chips (including the total turns figure),
  `--json`, and ccclose. Do they all ask the one classifier, and does any count or
  filter still reach the `you` role by another path? Other `instruments/` files and the
  search design note that describe roles.
- **The JSON contract.** A new role value in `--json` output: who consumes it, and is the
  change documented where a consumer would look?
- **ccclose's side.** Its prompt numbering must still equal cctranscript's refs, and its
  asks list must take only the principal's words. Check both against the shared
  classifier and the slash-command stripping ccclose keeps for itself.
- **The grounding claims in the code.** The comment above `HARNESS_TAGS` says the list
  came from a census of the live store. Re-drive a census on your own machine, read-only,
  recording counts and tag names only.

**Non-goals:** the decision that a harness record keeps its exchange number (the delta
states its reason); whether it should is reviewable only for what it costs a reader.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself first. Among
   them: that harness text is recognisable from its wrapper tags alone; that `isMeta` is
   only ever the harness's; that a census of recent sessions covers the wrapper kinds
   the harness emits; that one shared classifier is safer than two copies.
2. **Correctness & quality.** Read `classifyUserRecord`, `stripElements`, `readTurns`
   and ccclose's `readTranscript` whole; diff `cea247e`. Build the decision table from
   *Scope*. Check whether the tests' cases came from the regex or from the same reading
   that wrote it.
3. **Completeness / harvest.** The man page, the README header-line section, the design
   note's §6, `cctranscript.search.design.md`, the CHANGELOG, and any doctrine or memory
   that cites prompt counts or the authorship rule this changes.
4. **Security & privacy** — mandatory. The census and any live check read real
   transcripts: never quote one, never commit a count that identifies a person or a
   repo outside this one. Can a crafted record (a pasted wrapper, an injected
   instruction block) make the principal's words read as harness text, or harness text
   read as the principal's? The regex is built from a tag list at call time: check its
   cost on long or adversarial records. `/security-review` is discharged by grounds (a
   landed delta; the pending diff is not the work) — say so, and do the code-altitude
   read by hand against the OWASP catalogue.

## Re-run obligation

Re-run, do not read. Lift invocations from `.github/workflows/ci.yml` (the instruments
job) rather than guessing.

- `node --test instruments/cctranscript.test.js instruments/ccclose.test.js`, then the
  whole instruments suite once as CI runs it (`node --test instruments/*.test.js`),
  foreground
- `mandoc -T lint instruments/man/cctranscript.1`; `node instruments/cctranscript --help`
  by path
- the decision table, driven through `require` of the module at HEAD from a scratch
  script
- numbering invariance: in a scratch clone, `cea247e^` against `cea247e` over the same
  synthetic transcripts (and, read-only, a sample of your own machine's), comparing refs
  and per-role counts; record numbers only
- the floor on both planes at HEAD (`python3 tools/floor.py --plane ci --root .`, and
  the hook plane as `.githooks/pre-commit` invokes it)

## House rules for this run

- Name the worktree you work in. Run no git command that writes there; read-only git is
  fine. Probes, fixtures and older checkouts go in a private clone under your session
  scratchpad, named by your prefix.
- One heavy process at a time on a shared machine: the instruments suite at most once
  whole, in the foreground; a transcript census sized to finish in minutes, under
  `nice`. Never run an installed tool by bare name from `PATH`; instruments are
  symlinked onto it from another checkout. Never run anything with a side effect.
- `/security-review` reads the session's pending diff: discharge it by grounds for this
  landed delta, or keep the tree clean whenever you spawn it — never with this brief or
  its sibling dirty.
- Dates absolute ISO 8601 from `date -u`. Prose wrapped at ≤ 100 columns. NZ English.
  Never quote a secret, placeholder token, email address, personal detail or real
  transcript text — this repo is PUBLIC; describe and locate instead.
- Review deep, not fast: a finding needs a probe or a re-driven claim behind it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the deferred material lives in the sibling .deferred.md, held apart under the rule-1 split and opened only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`,
`docs/sessions/`, every prior verdict in `docs/reviews/`, the queue pointer, this
brief's sibling `docs/reviews/2026-10-17-1010-harness-classification-cold.deferred.md`,
the landing commit's and the merge's message bodies (the author's account; read
subjects, stats and diffs only), and the commissioning and neighbouring items:

- `docs/roadmap/210-instruments-open-features/250-cctranscript-counts-harness-text-as-prompts.md`
- `docs/roadmap/210-instruments-open-features/260-notification-records-read-two-ways.md`

Sweep with `python3 tools/coldsweep.py --root <your worktree> --also-exclude
docs/roadmap/160-doctrine-review-owed/880-rule-4-cold-pass-queued-harness-classification.md
--also-exclude docs/reviews/2026-10-17-1010-harness-classification-cold.deferred.md
--also-exclude
docs/roadmap/210-instruments-open-features/250-cctranscript-counts-harness-text-as-prompts.md
--also-exclude
docs/roadmap/210-instruments-open-features/260-notification-records-read-two-ways.md
<pattern>`; `--include-barred` only with disclosure in the verdict. Reading the delta is
never barred.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list. Then append
your verdict below a `---` divider in THIS file: provenance repeated (how you were
spawned, your tier, what you read), per-lens answers, the standing checklist V1–V7 each
answered or discharged with grounds, the decision table, findings with stable IDs
(prefix `HC`: `HC1`, `HC2`, …) and severities (MAJOR / MODERATE / minor / note), an
overall PASS / PASS-WITH-FINDINGS / FAIL line with counts, a re-run ledger, and a
follow-up checklist. Then STOP and commit phase 1 unrevised before opening the sibling.
Edit no other file.

**Phase 2.** Open the sibling; append `### Reconcile` beneath your verdict: per-finding
notes against the seeded questions and the intent record, any finding formed at
reconcile marked as such, and the overall line restated. Never revise phase-1 text.
Then fold the sibling in below the reconcile and delete it.

Findings are the principal's to decide (rule 3): record all, apply nothing; counsel per
finding is welcome, labelled and kept beneath it.

---

## Verdict — phase 1, cold pass on Fable, 2026-10-18 00:21 UTC

### Provenance, repeated

- **Reviewer.** This verdict — every lens answer, severity and the reconcile to come — was
  formed by a Claude Code subagent running as **Fable 5.1 (`claude-fable-5-1`)**, the tier
  rule 4 names (ruling 2026-08-04), checked at selection.
- **Spawn.** Dispatched by a Mike-opened Claude Code **cloud** session (`claude-fable-5-1`,
  orchestrating; it opened on `claude-opus-5` and Mike switched it to Fable before any claim
  or pass). That session authored none of the delta or the brief and was not started or
  instructed by their authors. It forms no finding and writes no severity; it holds the
  `.deferred.md` sibling outside the checkout at a path not given to me, commits this phase-1
  text before releasing the sibling, and received one operational note from Mike's watching
  session (model, queue scope, container facts, merge instruction — nothing evaluative about
  any delta). The claim line in the queue pointer discloses the same shape; I have not opened
  the pointer.
- **Where.** The shared checkout `/home/user/atelier`, branch `claude/review-work-briefs-adj6ad`
  at `c9d8a0d`, which adds only this run's review commits over `main`. No worktree: a cloud
  container holds one full clone, no worktrees, no sibling repos, no estate root, no
  `~/.claude/` and no transcript store; `gh` is on PATH with an invalid token (not needed).
  The checkout's `origin/main` ref is `fe020b16`, one board commit past the `0aff4d8` the
  orchestrator named; `git diff fe020b16 HEAD -- instruments/` is empty, so the delta under
  review is as it stands on `main`. Probes, fixtures and the older checkout live only under
  `/home/user/scratch/HC/` (a private clone at `cea247e^`). No git command that writes was
  run in the checkout; this file is the only one edited.
- **What I read, in order.** `docs/method/REVIEW.md`; this brief; `docs/method/00-APEX.md`
  (and the repo `CLAUDE.md`, injected by the harness). Then the delta as `git diff cea247e^
  cea247e -- <delta paths>` and `git show --stat --format=%s` of `cea247e` and `99f4c2a`
  — subjects and stats only, **no message body opened** — plus `git diff cea247e 99f4c2a --
  instruments/cctranscript` and `git diff 99f4c2a^1 99f4c2a -- CHANGELOG.md`; the seven
  delta files whole at HEAD; `instruments/cctranscript.search.design.md`;
  `.github/workflows/ci.yml`; `.githooks/pre-commit`; the scope block of
  `.atelier-floor.json`; grep-hit lines of `tools/reviewscan.py`; `tools/coldsweep.py
  --help` and `--list-barred`; board items `310/080`, `320/070` and `220/060` whole,
  `020/180` lines 100–139, grep hits in `210/100`; grep hits for `cctranscript` in
  `docs/method/session-open/session-open-prompt.md` and ADR 0006, and for "authorship" in
  `docs/method/`.
- **Exposure, disclosed.** `git log --oneline -3` on the branch printed three other passes'
  verdict-commit *subjects* (DM, HX, SX — none opened). The merge's `--stat` and the
  coldsweep summary lines printed the *filenames* of the queue pointer, items `210/250` and
  `210/260`, one `docs/sessions/` file and four other `160/` pointers (none opened). I did
  not open the pointer, the sibling, `docs/SESSIONS.md`, `docs/sessions/`,
  `docs/ROADMAP-DONE.md`, any other file under `docs/reviews/`, or either commit body. All
  sweeps ran through `tools/coldsweep.py` with the brief's four `--also-exclude` paths;
  `--include-barred` was not used. `/security-review` was not run (discharged by grounds,
  lens 4).

### Lens 1 — approach and assumptions

Load-bearing assumptions, named first and then attacked (table rows refer to the decision
table below; "invariance" to the re-run ledger's item 6):

- **A1 — harness text is recognisable from its wrapper tags alone, plus `isMeta`.** Holds
  for every shape the harness is known to emit (rows 6–14, 17–18, 40–42, 47, 50): attributes,
  an attribute value containing `>`, CRLF and nested *different* wrappers are all handled.
  It fails in the *attributing* direction on anything malformed: an upper-case, self-closing,
  unclosed, closing-only or unknown-named wrapper is the principal's (rows 19–28). The repo's
  own fixture for the attachment-channel form of `<cross-session-message …>` (`peerMsg` in
  `instruments/cctranscript.test.js`) has **no closing tag**; if the `type:"user"` form is
  ever shaped the same way and not `isMeta`, the classifier calls it a prompt. Not
  re-drivable here (no store); recorded under HC5's test gap.
- **A2 — `isMeta` is only ever the harness's.** The code's earlier census (2026-09-18, in
  `isHumanQueuedCommand`) saw peer messages `isMeta:true`; the delta adds skill bodies.
  Nothing in the repo contradicts it; I cannot re-drive it. Relayed.
- **A3 — the only element that rides on a real prompt is `<browser_instruction>`.** This is
  what `JOINED_TAGS` encodes and the assumption with the most resting on it. If any other
  harness block is logged inside a prompt's own record — a separate text block or inline —
  cctranscript shows it as the principal's words (rows 15, 16, 45, 46), the `--list` label
  leads with it (invariance, transcript D), and a `--search` hit in it reports role `you`;
  only ccclose is immune, because it strips every wrapper. The census behind the claim is
  40 recent sessions of one repo, and the comment does not say it looked for mixed records;
  board `320/070` (2026-08-21) records that system reminders "arrive in both records". → HC2.
- **A4 — one shared classifier is safer than two copies.** Agreed and re-driven: the two
  tools agree turn for turn on every synthetic transcript. But a *prompt's text* still
  differs between them — ccclose strips every wrapper, cctranscript only the browser block —
  so the comment's "so they cannot disagree" is true of classification and false of text.
  → HC3.
- **A5 — the slash-command wrappers "hold no sentences of the principal's".** False for
  `<command-args>`, which holds exactly what the principal typed after the command name.
  → HC1.

**The brief's framing** is accurate on what the work is and why it earns review, with one
"checked" claim wrong: the merge did change a delta path (HC6). The non-goal — a harness
record keeps its exchange number — fences off no risk; its cost to a reader is HC8 and is
acceptable, because `310/080` is a committed record that quotes a cctranscript "turn 6",
which is exactly why refs must not move.

### Lens 2 — correctness and quality

- **Numbering invariance — re-driven, holds.** Old (`cea247e^`) against HEAD over four
  synthetic transcripts (45 turns covering every decision-table shape): **0 refs moved**;
  every `claude` ref byte-identical; `--json` refs identical; 9 records relabelled
  `you`→`harness` at the same ref; one prompt text shortened (its joined browser block);
  ccclose's `turn`, `midTurn` and asks identical old and new; every ccclose ask ref present
  as a `you`/`you-mid` ref in cctranscript's `--json`. No record moves from numbered to
  `null`: the classifier returns `null` exactly where the old code skipped (empty text), and
  a prompt whose remainder after the browser block would be empty is caught first as harness
  (`HARNESS_TAGS` ⊇ `JOINED_TAGS`).
- **Every consumer asks the one classifier.** `readTurns`; `firstPromptInLines` (the
  `--list` label, harness-first sessions now labelled by the first real prompt); `--search`
  (harness searched, role reported, `ROLE_W` widened — which also fixes the one-column
  overflow `you-mid` already had); the header chips (`count('you')` excludes harness, the
  `turns` total includes it, the chip is conditional like mid-turn); `--json`; ccclose's
  `readTranscript`. No count or filter reaches `you` by another path; `side` puts harness on
  the left and `exchangeRule` prints the hollow glyph. ✓
- **JSON contract.** The new `harness` role is documented in the man page's `--json`
  paragraph. No in-repo consumer reads cctranscript's `--json`: ccclose requires the module,
  and skills, commands, tools and templates mention neither tool. Discharged.
- **The record's own claims.** The `HARNESS_TAGS` comment at HEAD carries the UTC census date
  only because the merge corrected the landing commit's NZ-local date (HC6). The CHANGELOG
  adds a second live-store figure ("181 → 56 over 12 recent sessions"). Neither is
  re-drivable here; both are relayed, not weighed.
- **Tests.** 447 run, 431 pass, 16 darwin-only skips, 0 fail. The harness tests pin the
  shapes the author designed for and none the design's assumptions turn on (HC5).
- The man page's `.TH` date stays `2026-08-09` through this and two earlier content edits:
  evidently not bumped by house practice, so no finding.

### Lens 3 — completeness and harvest

Swept with `coldsweep` (barred set excluded): the man page, the README header-line section,
`ccclose.design.md` §6 and CHANGELOG all carry the change. Missed: the search design note
(HC4). Doctrine citing prompt counts or the authorship rule: none in `docs/method/` — the
two `cctranscript` mentions in `session-open-prompt.md` concern timestamps and the session
id. The board holds the class in `310/080`, `320/070` and `210/100`, all consistent with the
delta; `220/060` (nothing watches the ask channel) is the natural home for HC1's
consequence and is otherwise unaffected. Nothing was duplicated: ccclose's own wrapper list
was removed in favour of the exports.

### Lens 4 — security and privacy

- **`/security-review`:** discharged by grounds — it reads the session's pending diff, which
  here is this brief and nothing of the landed delta; the tree was otherwise clean.
- **Design altitude.** The threat enumeration lives in code comments (a pasted wrapper; a
  joined block) rather than as a written step. The two directions: (i) the principal's words
  read as harness — a prompt that is *wholly* a pasted wrapper (rows 33, 47) vanishes from
  `you`, from the `--list` label and from ccclose's asks; (ii) harness text read as the
  principal's — a malformed wrapper (rows 19–28), or a harness block riding on a prompt
  (A3 → HC2). Direction (ii) is the class `310/080` names — a record credited to the
  principal is quoted forward carrying his authority — and it survives in cctranscript's
  render, `--json` and `--list` for anything the census did not see; ccclose is the safer
  consumer. An injected instruction block inside a prompt record would be shown as the
  principal's by cctranscript and dropped by ccclose.
- **Code altitude**, by hand against the OWASP catalogue classes from memory (the catalogue
  hosts have not resolved from this container for earlier reviewers; I did not attempt the
  network): local file input only; no shell, no network, no credential handling in the
  delta; the regex is built from constant tag lists, never from input (no pattern
  injection); every input path is the same `JSON.parse`-per-line the tool always had. ReDoS:
  measured (HC7) — linear on benign and HTML-ish 848 KB records, O(opens × tail) on an
  adversarial record of unclosed opens. Output: control sequences in any role's text reach
  the terminal unstripped (pre-existing, every role; HC9).
- **Privacy of this pass.** No real transcript exists or was read here; every fixture is
  synthetic; no count identifying a person or a repo is recorded.

### Standing checklist V1–V7

- **V1 — no claim stronger than its evidence.** Bites: HC1 (a grounding claim false for
  `<command-args>`), HC3 ("cannot disagree"; the man page's "prepends" when any quoted
  browser block is removed too), HC6 (the brief's "checked"). The census and the CHANGELOG
  figure are relayed, not weighed.
- **V2 — re-run every live-proven claim.** Tests, man lint, `--help`, both floor planes, the
  decision table and numbering invariance re-driven (ledger). Three claims **not re-driven
  here (relayed)**: the 40-session census, the 12-session 181→56 figure, and
  `isMeta`-is-harness — this container has no transcript store.
- **V3 — swept to every mirror.** The search design note was not (HC4); every other mirror
  was.
- **V4 — one fact, one home.** Tag lists single-sourced ✓. The kept-number rationale is
  restated eight times, unstamped (HC10).
- **V5 — no internal contradiction.** Design note §6 against `stripWrappers` (HC3); README's
  "the field set never varies" beside two conditional chips (HC11).
- **V6 — security and privacy.** Lens 4 above; `/security-review` discharged by grounds.
- **V7 — provenance.** In the brief ✓ and repeated above ✓.

### Decision table

Driven through `require` of `instruments/cctranscript` and `instruments/ccclose` at HEAD
(`/home/user/scratch/HC/table.js`, 60 synthetic records). *TN* = a closed
`<task-notification>` element, *SR* = `<system-reminder>`, *BI* = `<browser_instruction>`.
"cct text" is what cctranscript renders or carries in `--json`; "ccclose" is whether
`readTranscript` would count the record as the principal's, with the text its asks heuristic
would see when that differs. Old behaviour (`cea247e^`) on every non-`null` row was `you`.

| # | input | class | cct text | ccclose |
|---|---|---|---|---|
| 1 | `isMeta` + plain sentence | harness | sentence, whole | no |
| 2 | `isMeta` + TN | harness | raw | no |
| 3 | `isMeta` + empty string | null | — | — |
| 4 | `isMeta` + whitespace | null | — | — |
| 5 | `isMeta:false` + plain | prompt | plain | yes |
| 6 | wholly TN | harness | raw | no |
| 7 | wholly SR | harness | raw | no |
| 8 | wholly `<local-command-stdout>` | harness | raw | no |
| 9 | wholly `<local-command-stderr>` | harness | raw | no |
| 10 | wholly `<local-command-caveat>` | harness | raw | no |
| 11 | wholly `<cross-session-message …>` with attrs | harness | raw | no |
| 12 | wholly BI | harness | raw | no |
| 13 | SR then TN | harness | raw | no |
| 14 | TN inside surrounding whitespace | harness | raw | no |
| 15 | TN then a sentence | prompt | **TN kept** + sentence | yes; sentence only |
| 16 | a sentence then TN | prompt | sentence + **TN kept** | yes; sentence only |
| 17 | TN with attributes | harness | raw | no |
| 18 | attribute value containing `>` | harness | raw | no |
| 19 | UPPER-CASE TN | **prompt** | raw | yes; raw |
| 20 | Mixed-Case TN | **prompt** | raw | yes; raw |
| 21 | `<task-notification/>` | **prompt** | raw | yes; raw |
| 22 | `<task-notification />` | **prompt** | raw | yes; raw |
| 23 | nested same-name SR | **prompt** | raw | yes; `c</system-reminder>` |
| 24 | unclosed TN (truncated) | **prompt** | raw | yes; raw |
| 25 | closing tag only | **prompt** | raw | yes; raw |
| 26 | `<task-notification-x>…</task-notification-x>` | **prompt** | raw | yes; raw |
| 27 | `<task-notification-x>…</task-notification>` | harness | raw | no |
| 28 | `<task-notificationx>…</task-notificationx>` | **prompt** | raw | yes; raw |
| 29 | BI before prompt | prompt | prompt only | yes |
| 30 | BI after prompt | prompt | prompt only | yes |
| 31 | BI inside prompt | prompt | prompt, three spaces | yes |
| 32 | two BI + prompt | prompt | prompt only | yes |
| 33 | lone pasted SR, no other words | **harness** | raw | **no** |
| 34 | TN inside a code fence | prompt | fence + TN kept | yes; fences only |
| 35 | quotes SR with words | prompt | **quote kept** | yes; **quote removed** |
| 36 | quotes BI with words | prompt | **quote removed** | yes; quote removed |
| 37 | HTML-escaped wrapper | prompt | kept | yes |
| 38 | bare open tag as a word | prompt | raw | yes |
| 39 | TN open, SR close | prompt | raw | yes; raw |
| 40 | two sequential TN | harness | raw | no |
| 41 | TN nesting SR | harness | raw | no |
| 42 | TN with CRLF | harness | raw | no |
| 43 | content as string | prompt | as typed | yes |
| 44 | two text blocks | prompt | joined with `\n` | yes |
| 45 | text block SR + text block ask | prompt | **SR kept** + ask | yes; ask only |
| 46 | ask + appended SR block | prompt | ask + **SR kept** | yes; ask only |
| 47 | two SR text blocks only | harness | raw | no |
| 48 | image-only blocks | null | — | — |
| 49 | image + text | prompt | text | yes |
| 50 | image + TN | harness | raw | no |
| 51 | empty content array | null | — | — |
| 52 | `content` missing | null | — | — |
| 53 | `message` missing | null | — | — |
| 54 | `message` missing + `isMeta` | null | — | — |
| 55 | null record | null | — | — |
| 56 | whitespace only | null | — | — |
| 57 | `<command-name>/clear…`, empty args | prompt | raw XML | no (text empty) |
| 58 | command with `<command-args>` carrying an ask | prompt | raw XML | **no — ask dropped** |
| 59 | `<command-name>` + `<local-command-stdout>` | prompt | raw XML | no |
| 60 | `toolUseResult` record (callers filter it) | prompt | text | yes (never reached) |

Which inputs move a real prompt to `harness`: a prompt that is wholly pasted wrapper(s) —
rows 33 and 47. Which leave harness text as `you`: any malformed wrapper — rows 19–26, 28 —
and any non-browser harness block riding on a prompt — rows 15, 16, 45, 46 — if the live
store holds such records (not re-driven here). Rows 57–59 are the principal's own commands by
design, shown as raw XML; row 58 is HC1.

### Findings

**HC1 — MODERATE — `<command-args>` holds the principal's words, and ccclose drops them.**
The delta's grounding comment above `COMMAND_TAGS` (and `ccclose.design.md` §6) says the
slash-command wrappers "hold no sentences of the principal's", so a consumer hunting for
asks strips them. `<command-name>` and `<command-message>` hold none; `<command-args>` holds
exactly the text the principal typed after a command. Probe: table row 58 — a record of the
shape the repo's own fixtures use (`ccclose.test.js`, the `/clear` record) with an ask in its
args classifies `prompt`, ccclose strips it to the empty string, `principal` is false, the
turn is not counted and the ask is never listed; cctranscript shows the record as `you` with
the raw XML as its text. The stripping predates the delta (ccclose's old `WRAPPERS` held
`command-args`), but the delta re-grounds it with a false rationale and moves it into the
shared module both tools now trust. Whether the principal types close-out asks as command
arguments is not re-drivable here. *Counsel (reviewer's, for the principal):* strip
`command-name`/`command-message` only and unwrap `command-args` for the asks list; have
cctranscript render such a record as `/name args` rather than raw XML; correct the comment
and §6; add row 58 as a test. Recurrence-prevention: a test that asserts principal text
survives every wrapper strip.

**HC2 — MODERATE, conditional and not re-driven here — the "only `browser_instruction`
rides on a real prompt" census claim is the design's load-bearing assumption, and if it is
wrong cctranscript credits harness text to the principal.** `JOINED_TAGS` strips one
element from a prompt's text; every other harness block is stripped only to decide whether
a record is *wholly* harness. Probe: rows 15, 16, 45 and 46 — a TN or SR riding on a prompt
as prefix, suffix or a separate text block stays in cctranscript's `you` text, in `--json`,
and leads the `--list` label (invariance transcript D: the label opens with the reminder
body, not the ask), while ccclose strips it. The claim rests on a census of 40 recent
sessions of one repo whose comment does not say it looked for mixed records; `320/070`
records that system reminders "arrive in both records" (2026-08-21). This container has no
store, so the claim is relayed: **re-drive it** — count `type:"user"` non-tool records whose
text holds a `HARNESS_TAGS` element *and* non-wrapper text, per tag. If any exist beyond the
browser block, the attribution class `310/080` names is live in cctranscript's render and
label. *Counsel:* classify per text block rather than per record — a block that is wholly a
wrapper is harness and leaves the prompt's text; an inline quote inside a block stays — which
also removes the quoted-wrapper trade-off in HC3; failing that, widen `JOINED_TAGS` with the
trade-off stated. Add rows 15/45 as tests in whichever direction the census decides.

**HC3 — minor — the two tools agree on the ref and disagree on the text, and the design
note understates ccclose's own filter.** `ccclose.design.md` §6: "One filter remains
ccclose's own, for the asks list only: the slash-command wrappers." In fact `stripWrappers`
removes every `HARNESS_TAGS` element from a prompt's text as well, which cctranscript keeps:
row 35 — a prompt quoting a system reminder renders whole in cctranscript and as "why does
show up?" in ccclose; row 36 — a prompt *quoting* a browser block loses the quote in both,
though the man page says only a block "a browser extension prepends" is removed. The code
comment "so they cannot disagree" is true of classification only. The header `N you` and
ccclose's `N turn` also differ by the slash-command records (invariance A: 7 against 5) —
§6's last clause does allow for that. *Counsel:* state the text asymmetry in §6 and the man
page, or resolve it per HC2's counsel.

**HC4 — minor — a mirror not swept: `cctranscript.search.design.md`.** Its banner records
each departure of the build from the design and got a bullet for `you-mid` on 2026-09-18;
nothing for `harness`. §4 still says `numberTurns` "numbers only `you` (N) and `claude`
(N.M) turns" and §5 that the default searches "prompts and replies". Related: `--search`'s
layer vocabulary (`searched prompts+replies`, `meta.layersSearched`) has no name for the
harness layer whose hits it now returns, so a harness hit arrives under a summary that does
not say it was searched. *Counsel:* one banner bullet; either name the layer or state that
harness rides in the prompts layer.

**HC5 — minor — the tests pin the regex's own happy path.** Every harness fixture is a
lowercase, closed, well-formed wrapper; the cases the design's assumptions turn on are
asserted in neither direction: a non-browser wrapper riding on a prompt (rows 15/16/45/46), a
lone pasted wrapper (33), an unclosed, self-closing or upper-case wrapper (19–25, and the
repo's own unclosed `peerMsg` shape), a `<command-args>` ask (58). ccclose's
`'hi   there'` assertion pins three spaces rather than meaning. A test that asserts *current*
behaviour on each would at least make the trade-offs visible when the harness's shapes move.

**HC6 — minor — the brief's "checked" merge claim is false, and the one line it missed is a
convention fix.** The brief: merge `99f4c2a` "changes none of the delta paths against
`cea247e` (checked)". `git diff cea247e 99f4c2a --stat -- instruments/` shows one line in
`instruments/cctranscript`: the `HARNESS_TAGS` census date, `2026-10-17` at the landing
commit (NZ-local; the commit is 2026-10-16 16:43 UTC) corrected to `2026-10-16` at the merge
(`CONVENTIONS.md`: UTC at rest). HEAD is right; the brief's instruction to diff `cea247e`
would have had a reviewer read a comment HEAD does not carry. Rule 1: the brief's account of
the work is attackable, and this one was wrong on a point it marked verified.

**HC7 — note — regex cost, measured.** `stripElements` on 848 KB records: benign prose
1.2 ms, every character a `<` 1.8 ms, HTML-ish 1.5 ms, one unclosed open at the start 1.3 ms;
50 000 closed wrappers (2 MB) 8 ms. Adversarial — N unclosed `<system-reminder>` opens
before a 400 KB tail: 100 → 15 ms, 300 → 43 ms, 1 000 → 150 ms, 3 000 → 456 ms, i.e.
O(N × tail), from the lazy `[\s\S]*?` scanning to the end once per open. It runs on every
non-tool user record in a render, the `--list` label and every gate-passing file of a
`--search`. Not a practical risk — only a pasted blob of unclosed opens reaches it — and a
single `<`-anchored pass or a cap on opens would close it. The `new RegExp` per call is
negligible.

**HC8 — note — the kept exchange number, costed for a reader (the non-goal).** `N you` no
longer equals the last exchange number; grey `◦ N` rules interleave with cyan `▸ N`; an
"exchange 7" quoted in a record may be harness-opened. The man page says all of this. The
alternative would move every ref already quoted — `310/080` quotes a cctranscript "turn 6"
as evidence — so the cost is the right one to pay.

**HC9 — note, pre-existing — control sequences in any role's text reach the terminal
unstripped.** `renderBody` and `harnessLine` collapse whitespace but do not strip ESC; a
record carrying terminal escapes would restyle the render. Every role, before and after the
delta; recorded under lens 4, not charged to this change.

**HC10 — note — V4.** The rationale "harness keeps its exchange number because quoted refs
must not move" is restated in the file header, the `classifyUserRecord` block, `readTurns`,
`numberTurns`, the man page, the README, `ccclose.design.md` §6 and CHANGELOG — eight homes,
none stamped. Drift risk only.

**HC11 — note — V5.** `instruments/README.md` says the header is designed so "the *field
set* never varies between runs" and, in the same breath, now describes two chips that appear
only when non-zero (mid-turn, harness). The sentence predates the delta; the delta extends
the exception without reconciling it. The agents chips are what the rule was written for.

### Overall

**PASS-WITH-FINDINGS — 0 MAJOR · 2 MODERATE · 4 minor · 5 note.** The change does what it
claims where it can be re-driven here: refs are invariant, the two tools agree turn for
turn, every consumer asks the one classifier, and the floor, the suites and the man lint
are green. What it rests on — two grounding claims about what the harness writes into a
prompt's own record — could not be re-driven in this container, and one of them is false on
the repo's own fixtures.

### Re-run ledger

| # | claim / check | how | result |
|---|---|---|---|
| 1 | delta tests | `node --test instruments/cctranscript.test.js instruments/ccclose.test.js` | 119 run · 117 pass · 2 darwin-only skips · 0 fail · 5.9 s |
| 2 | instruments suite, once, as CI runs it | `node --test instruments/*.test.js` | 447 run · 431 pass · 16 darwin-only skips · 0 fail · 23.3 s |
| 3 | man page | `mandoc -T lint instruments/man/cctranscript.1` | clean, exit 0 |
| 4 | help digest | `node /home/user/atelier/instruments/cctranscript --help` | prints, exit 0 |
| 5 | decision table | `/home/user/scratch/HC/table.js`, `require` of both modules at HEAD | 60 rows above |
| 6 | numbering invariance | `/home/user/scratch/HC/invariance.js`: `cea247e^` (private clone) against HEAD, module and CLI `--json`, 4 synthetic transcripts, 45 turns, plus old/new ccclose | 0 refs moved · claude refs identical · 9 relabelled at the same ref · ccclose counts and ask refs identical |
| 6b | same, on a sample of a real store | — | **not re-driven here (relayed):** no store in the container |
| 7 | floor, CI plane | `python3 tools/floor.py --plane ci --root .` | every enforced check ✅; warn-only pathscan 1 finding unrelated to the delta (an ADR's `tools/exception.py`); 23 pre-existing secretscan advisories; 11.9 s |
| 8 | floor, hook plane | `python3 tools/floor.py --plane hook --root … --tools …/tools` as `.githooks/pre-commit` invokes it | leakscan ❌ by design (no user-local term list; board `115/350`), every other check ✅, exit 1 as expected |
| 9 | census behind `HARNESS_TAGS` (40 sessions, one repo) | — | **not re-driven here (relayed)** |
| 10 | CHANGELOG "181 → 56 over 12 recent sessions" | — | **not re-driven here (relayed)** |
| 11 | "`isMeta` is only ever the harness's" | — | **not re-driven here (relayed)** |
| 12 | regex cost | `/home/user/scratch/HC/cost.js` under `timeout` | HC7 figures |
| 13 | merge changes no delta path | `git diff cea247e 99f4c2a --stat -- instruments/` | **false**: one line (HC6) |
| 14 | nothing touches delta paths after the merge | `git diff 99f4c2a HEAD --stat -- <paths>` | empty ✓ |
| 15 | `/security-review` | — | discharged by grounds (landed delta; pending diff is this brief) |
| 16 | Python tool suite | — | not run: the delta is Node-only and the brief's re-run list does not name it; the CI-plane floor ran |

### Follow-up checklist (the principal's to decide — nothing applied)

- [ ] HC1 — decide whether `<command-args>` text is the principal's for the asks list and
      the render; correct the `COMMAND_TAGS` comment and design note §6 either way.
- [ ] HC2 — re-drive the census for mixed records (wrapper + non-wrapper text in one
      `type:"user"` record), per tag; decide per-block classification or a wider
      `JOINED_TAGS`.
- [ ] HC3 — state or resolve the prompt-text asymmetry between the tools; fix the man
      page's "prepends".
- [ ] HC4 — one departure bullet in `cctranscript.search.design.md`; name the harness layer
      in `--search`'s summary or say where it rides.
- [ ] HC5 — add the assumption-bearing rows (15/45, 33, 24, 58) as tests in whichever
      direction HC1/HC2 are decided.
- [ ] HC6 — brief-writer's note: diff the merge against the landing commit before writing
      "checked".
- [ ] HC7–HC11 — notes; no action owed unless the principal wants the regex anchored.

### Reconcile — phase 2, 2026-10-18 00:28 UTC

Phase-1 text above is unrevised. Opened at phase 2, after the orchestrator committed phase 1
as `87cb7c6`: the sibling (folded in below), the queue pointer `160/880`, the intent record
`docs/sessions/2026-10-16-1501-queue-run-briefs-and-guard-builds.md`, the commissioning
item `210/250`, its neighbour `210/260`, and both commit bodies (`cea247e`, `99f4c2a`).
Reconcile-step reading of prior verdicts, disclosed: three passages of
`docs/reviews/2026-10-16-1550-first-prompt-prefix-cold.md` that name `cea247e` (its FP8), one
grep hit in `docs/reviews/2026-08-15-1032-cctranscript-search-cold.md` not pursued, and the
counts only from one line of `docs/SESSIONS.md` (for seeded question 7). The
`2026-10-16-1551` pass the sibling names was not opened. One further probe ran
(`/home/user/scratch/HC/harnessonly.js`, for seeded question 6).

**Against the intent record and the commit bodies.** The author's account matches the code
I read: one classifier, harness keeps its number, ccclose takes the exported lists. Its two
live-store claims — "181 → 56 on the 12 most recent sessions" with "last-exchange numbers
match old and new on all 12", and the intent record's own session going from 13 `you` to
the one Mike typed with 12 notifications shown as harness — are consistent with the
synthetic invariance I re-drove (0 refs moved) and stay **relayed**, not weighed (ledger 6b,
9, 10). The body's "so they cannot disagree" is the claim HC3 narrows. The merge body's "one
NZ-local date corrected" is the line HC6 found; the brief-writer read that body and still
wrote "changes none of the delta paths (checked)". `210/250`'s "dropping the number is a
one-place change" is not quite so: `numberTurns` and ccclose's own `n++` both carry it — an
instance of HC10's drift risk already in a record, no new finding.

**Against the seeded questions.**

1. HC6 answers the date: NZ-local at rest in the landing commit, UTC after the merge. Two
   censuses ground two different things — the 40-session one the tag list, the 12-session
   one the before/after count and the last-exchange check. Consistent; neither re-drivable
   here.
2. Yes: `turns.length` counts harness turns and the `you` chip excludes them — probed
   ("4 turns · 0 you · 2 Claude · 2 harness"; invariance A: "28 turns · 7 you · … ·
   6 harness"). The README's new sentence about `you` reads true; its "field set never
   varies" is HC11.
3. Yes — HC2 and HC3 are exactly this. The shared classifier ended disagreement on *whose
   record it is*; the two tools still disagree on *what the prompt's text is*.
4. A slash command's expansion and a skill body are `isMeta` and classify harness, which is
   right for their text (the harness wrote it). The principal's authorship of the
   invocation survives only in the `<command-…>` record, shown as `you` with raw XML (rows
   57–59), and the typed arguments are dropped by ccclose — HC1. Whether any principal-typed
   sentence is itself logged `isMeta` is relayed (A2).
5. Yes: `isHumanQueuedCommand` rejects `commandMode:"task-notification"`, so the same
   notification is a numbered grey turn as a user record and invisible as an attachment.
   The author filed it (`210/260`), and its text is accurate: neither shape credits the
   principal. One design note for that item, not a finding here: a turn given to the
   attachment shape must not bump `N` — the mid-turn `N+K` precedent is the only shape that
   keeps every quoted ref.
6. Probed. A session whose only user records are harness text: `--list` labels it with the
   empty string (the row shows id and time, blank label; `--json` `firstPrompt: ""`); the
   header reads `4 turns · 0 you · 2 Claude · 2 harness`; `--json` refs are `1, 1.1, 2,
   2.1`, harness-opened; ccclose counts `turn=0 mid=0 asks=0` with the window known. Honest
   on every surface; no finding.
7. Yes, and nothing but the CHANGELOG marks the break — **HC12, below, formed at
   reconcile.**
8. HC7.

**Against the prior verdicts named.** FP8 of the first-prompt-prefix pass already records
that `cea247e` overtook its brief within the hour and that the `firstPromptInLines` rewrite
keeps the predicate shared by the prefix and whole-file paths — consistent with my lens 2
(the `--list` label asks the classifier on both paths). Nothing in the search cold pass's
one hit bears on the delta. Overlap with `160/870`: ccclose's `stripWrappers` and the user
branch of `readTranscript` are reviewed here (HC1, HC3); its other code is that pass's.

**HC12 — note, formed at reconcile — `you` counts quoted before 2026-10-16 are not
comparable with the new reader's, and only the CHANGELOG says so.** Seeded question 7 asked
whether old figures were quoted and whether anything flags the break. Probe: `docs/SESSIONS.md`
carries at least one header line from the old reader ("206 turns · 24 you · 182 Claude",
counts only); the old `you` figure is an upper bound that included harness records, so a
reader comparing it with a fresh run of the same session will see a drop and nothing in the
tool, the man page or the record says why. Records are frozen and correct for their date;
the CHANGELOG entry is the one flag. *Counsel:* one NOTES line in the man page — counts of
`you` taken before 2026-10-16 include what is now `harness` — or nothing, if the CHANGELOG is
judged enough.

**Overall, restated: PASS-WITH-FINDINGS — 0 MAJOR · 2 MODERATE · 4 minor · 6 note.**
HC1–HC11 stand as written; HC12 is the one finding formed at reconcile.

## Deferred material — folded in at the verdict

*The sibling `docs/reviews/2026-10-17-1010-harness-classification-cold.deferred.md`,
folded in verbatim at phase 2 and deleted, per `REVIEW.md` rule 1 (split for the duration,
merged at rest).*

# Sibling to the harness-classification cold pass — held under rule 1's split

Sibling of `docs/reviews/2026-10-17-1010-harness-classification-cold.md`, held under
`docs/method/REVIEW.md` rule 1's split. **Open only after the phase-1 findings in the
brief are committed.** Written 2026-10-17 UTC by the Opus brief-writer named in the
brief's provenance; it forms no finding. Fold this file in below the reconcile and
delete it at phase 2.

## Intent and commissioning records

- Intent record: `docs/sessions/2026-10-16-1501-queue-run-briefs-and-guard-builds.md` —
  **not opened by the brief-writer**.
- Commissioning board item (name only, never opened): `210/250` (cctranscript counts
  harness text as prompts), filed by the merge that landed ccclose. Neighbouring item
  filed by this delta's merge: `210/260` (notification records read two ways).
- The landing commit's message body (read by the brief-writer), in summary:
  `readTurns` treated every non-tool-result user record as the principal's, so task
  notifications, `isMeta` records and slash-command output echoes took role "you", and
  a prepended browser-instruction block showed as part of a real prompt; "on the 12
  most recent sessions of one repo that read 181 'you' turns where 56 are the
  principal's". One shared classifier now serves `readTurns`, the `--list` label and
  ccclose "so they cannot disagree"; harness text keeps its exchange number so quoted
  refs do not move, and "last-exchange numbers match old and new on all 12 sessions
  checked". Trailer: a Sonnet model.
- The merge's body: read by the orchestrator before the merge; "one NZ-local date
  corrected"; closes 210/250, files 210/260, queues 160/880.

## Prior verdicts on these surfaces (named by filename grep, not opened, not exhaustive)

- `docs/reviews/2026-08-15-1032-cctranscript-search-cold.md` — the search surface
- `docs/reviews/2026-10-16-1550-first-prompt-prefix-cold.md` — the `--list` first-prompt
  label this delta changes (`firstPromptInLines`)
- `docs/reviews/2026-10-16-1551-git-quoted-paths-cold.md` — names ccclose

## The pointer's own lens hints

None. The pointer is refs-only.

## Overlap with sibling passes of this batch

- 160/870 (ccclose's build) shares `instruments/ccclose`, its tests, the design note and
  the README. This delta rewrote ccclose's own classification twenty minutes after that
  one merged. The 160/870 brief tells its runner to leave this delta's hunks here.
- The first-prompt-prefix pass (2026-10-16) reviewed the `--list` label code before this
  delta changed its record test.

## Seeded questions (the brief-writer's suspicions, a floor not a fence)

1. The comment above `HARNESS_TAGS` dates its census 2026-10-17 and counts 40 sessions;
   the commit was made 2026-10-16 16:43 UTC and its body counts 12. Is the comment's date
   NZ-local at rest, and which census grounds the tag list?
2. The header's first chip is `${turns.length} turns`. Does that total now include
   harness turns while the `you` chip excludes them, and does the README's account of
   the header still read true?
3. Only `browser_instruction` is removed from a real prompt. A `system-reminder` joined
   to a real prompt stays in the text cctranscript shows as the principal's, while
   ccclose strips it for the asks. Is that the disagreement the shared classifier was
   meant to end?
4. `isMeta` records are harness "whatever they contain". Does any principal action (a
   slash command's expansion, a skill invoked by the principal) log as `isMeta` and so
   lose its authorship?
5. 210/260's title says notification records are read two ways. Do task notifications
   ever arrive as `queued_command` attachments, where `isHumanQueuedCommand` and not this
   classifier decides, so the two shapes disagree?
6. A transcript whose only user records are harness text: what does `--list` label it,
   and what does ccclose number?
7. Prompt-share figures computed before this change have been quoted in records and
   memory. Does anything flag that counts from the old reader are not comparable with
   counts from the new?
8. `stripElements` builds a fresh lazy-match regex per call over the whole record text.
   With kilobyte-scale notifications and an unclosed tag, what is its cost?
