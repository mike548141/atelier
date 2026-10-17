# Cold pass — cctranscript reads a bounded prefix for the first-prompt column

**Pass type:** code cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection by whoever takes this pass; a session that cannot honour it stops.
**Status:** BRIEF ONLY — the review has NOT run. Written 2026-10-16 UTC by an Opus
brief-writer; the pass waits for a further cold Fable session that neither the
delta's author nor this brief-writer (nor its orchestrator) started or
instructed; tier checked at selection (rule 4).
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/680-rule-4-cold-pass-queued-first-prompt-prefix.md`.
**Why it earns a review:** the change is a speed path whose safety rests on one
claim — that a prefix can never change the answer the whole-file read gave. If
the claim is false, the session list silently shows the wrong first prompt, and
a session picked from that list is the wrong session.

## Spawn provenance

- **Author of the work under review:** the queue run whose intent record is
  dated 2026-10-05 11:20 UTC (path in the sibling; not opened by this writer).
  The code commit carries a model-unnamed co-author trailer (a dispatched worker,
  which the pointer counts as the run's authorship); the follow-up carries an
  Opus trailer.
- **Who wrote this brief:** an Opus subagent (`claude-opus-5-5`) dispatched by the
  Mike-opened Opus queue-run session `abe96d8d` on 2026-10-16 UTC, on Mike's
  answer that day that a fresh Opus session writes these briefs. Neither it nor
  its orchestrator authored, started or instructed the authoring run, and
  neither edited the delta. It is **off-tier for review, disclosed: it forms no
  finding and writes no severity**, and it stopped after this brief and its
  sibling.
- **Who takes the review:** a further cold Fable session, not yet started, that
  passes rule 4's criterion. It repeats its own provenance in its verdict and, if
  it runs under an orchestrator, discloses that shape as rule 4 requires.
- ⚠️ **Exposure, disclosed** (rule-2 material met before writing). This writer
  read: the queue pointer in full; both commits' subjects, `--stat` and message
  bodies (the author's account, including a census and timings taken on the
  principal's real archive); the code diff of `83d9b0b` and the one-line
  instrument hunk of `72bc6d3`; `gunzipHead`, `cwdFromLog` and the `--list` call
  sites at HEAD; `REVIEW.md` down to § *Whether work earns a review*; the ask
  halves of two 2026-10-04 briefs as format models; filename listings of
  `docs/reviews/` and `docs/roadmap/`, and path greps over `docs/reviews/` that
  name prior verdicts without reading them; and its auto-loaded cross-session
  memory index. Its orchestrator read the `docs/SESSIONS.md` index tail (entries
  through 2026-10-16, including the authoring runs' one-paragraph summaries) and
  the 2026-10-16 session record's close section, and passed this writer nothing
  evaluative beyond the pointer list. What this writer suspects is in the sibling.

## What the work is

Landing commits (diff these; review the paths at HEAD):

- `83d9b0b` (2026-10-05 UTC) — cctranscript: read a bounded prefix of each mirror
  for the first-prompt column; landed in merge `89a7539` (210/180)
- `72bc6d3` (2026-10-05 UTC) — the commit after the merge; for these paths, one
  comment line in `instruments/cctranscript` (the census date); its other files
  are board and records

Delta paths: `instruments/cctranscript` (`firstUserPromptText`, the new
`firstPromptInLines`, `FIRST_PROMPT_PREFIX`, the export list) and
`instruments/cctranscript.test.js`. No later commit has touched either path.

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code,
tests and live behaviour. The lenses organise it; they do not bound it.
Non-goals are the only narrowing and are themselves reviewable.

Whether `firstUserPromptText` returns, for every input, exactly what the parent
commit's whole-file read returned — and where it does not, whether the
difference is disclosed, intended and documented. Build synthetic `.gz` mirrors
in your clone and compare old (`83d9b0b^`) against new, function and full
`--list --from-archive` output (text and `--json`): the first prompt well inside
64 KB; straddling the 64 KB decompressed boundary; after the boundary; a first
line longer than 64 KB; a log with no prompt; tool-result carriers before the
prompt; CRLF line ends; multi-byte UTF-8 at the cut; a multi-member gzip; a gzip
with trailing bytes; a truncated gzip whose prefix is intact; a zero-byte `.gz`;
a plain-text file named `.gz`; a highly compressible log (a small compressed read
that inflates to megabytes); a mirror that changes between the prefix read and
the fallback read. Check `gunzipHead`'s doubling loop on each: bytes read,
memory peak, number of inflates. Check the evicted-mirror guard still keeps every
path from reading an offloaded file.

**Non-goals:** `--search` (the commit says it is untouched — verify that, then
leave it); `gunzipHead` itself as introduced by an earlier change (read it, since
the delta now depends on it, but judge only how the delta uses it).

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself first —
   among them, what must be true of the decompressed prefix for "the first match
   among complete leading lines is the first match in the file" to hold, and
   whether a bound chosen from one archive's census can matter to correctness.
2. **Correctness & quality.** Read the delta and its tests whole. Run the case
   matrix above, old against new, and record a table. Do the new tests fail
   against the parent? Do they pin the dropped partial line, the fallback, and
   the disclosed corrupt-mirror change?
3. **Completeness / harvest.** Is the corrupt-mirror behaviour change stated in
   `--help`, `instruments/man/cctranscript.1`, `instruments/README.md` and
   `CHANGELOG.md`? Do `ccrepo` or any other instrument still read whole mirrors
   for a first-lines question that the same helper would answer?
4. **Security & privacy** — mandatory. Code altitude, against the OWASP
   catalogue: decompression-bomb resource use through the prefix path; terminal
   control sequences in a prompt printed raw to the list (does the delta widen
   which bytes reach the terminal?); file-descriptor handling on throw. Design
   altitude: the input is the principal's private transcripts. `/security-review`:
   discharge by grounds (landed delta; the pending diff is other passes' drafts)
   and do this read by hand, or aim it only at a clean tree.

## Re-run obligation

Re-run, do not read. Lift invocations from `.githooks/pre-commit`,
`tools/floor.py` and `.github/workflows/ci.yml` rather than guessing.

- `node --test instruments/cctranscript.test.js`, at HEAD and with the delta's
  tests run against `83d9b0b^`'s code; then `node --test instruments/*.test.js`
  once, foreground, from your clone
- `mandoc -T lint instruments/man/cctranscript.1`
- the case matrix in *Scope*, old against new, on synthetic mirrors
- the commit's real-archive claims (byte-identical listings, CPU before and
  after): reproduce the *shape* of the timing on a synthetic corpus; if you
  judge the real archive necessary, follow the privacy rule below, else
  discharge the claim with grounds in the ledger
- the floor on both planes at HEAD, exit codes read explicitly

## House rules for this run

- **The tool's default input is the principal's private history.** Never run
  `cctranscript` by bare name (the installed copy resolves to the primary
  checkout); run it by absolute path from your clone with `HOME` pointed at a
  scratch tree of synthetic logs. If you run it against the real archive at all,
  write both outputs to files and compare them by hash only — never display a
  listing: its first-prompt column would show you the principal's prompts,
  including those of the sessions that authored this work (rule-2 material).
- Name your own worktree in the verdict. Run **no git command that writes** there;
  read-only git is fine. Probes and older checkouts go in a private clone under
  your scratchpad, named by your prefix.
- One heavy process at a time on a shared machine: each suite at most once,
  foreground. Never point a scanner at another repository on the machine.
- Absolute ISO-8601 dates from `date -u`. Prose wrapped at ≤ 100 columns. NZ
  English. Never quote a secret, placeholder token, email address, transcript
  text or personal detail — the repo is public; describe and locate instead.
- Review deep, not fast: a finding needs a probe or a re-driven claim behind it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the deferred material lives in the sibling .deferred.md beside this brief under the rule-1 split, opened only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`,
`docs/sessions/`, every prior verdict in `docs/reviews/`, the queue pointer named
above, this brief's sibling (same path, `.deferred.md`), and the commissioning
items `180-first-prompt-column-gunzips-every-mirror.md` and
`050-archive-mode-pool-construction-dominates-every.md` under
`docs/roadmap/210-instruments-open-features/`.

Sweep with rule 2's default bar plus these (`<root>` is your worktree):

```sh
Q=docs/roadmap/160-doctrine-review-owed
W=docs/roadmap/210-instruments-open-features
python3 tools/coldsweep.py --root <root> \
  --also-exclude $Q/680-rule-4-cold-pass-queued-first-prompt-prefix.md \
  --also-exclude docs/reviews/2026-10-16-1550-first-prompt-prefix-cold.deferred.md \
  --also-exclude $W/180-first-prompt-column-gunzips-every-mirror.md \
  --also-exclude $W/050-archive-mode-pool-construction-dominates-every.md \
  <pattern>
```

`--include-barred` only with disclosure in the verdict. The delta is never barred.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list. Then
append your verdict below a `---` divider in THIS file: provenance repeated (how
you were spawned, your tier, what you read), per-lens answers, findings with
stable IDs (prefix `FP`: `FP1`, `FP2`, …) and severities (MAJOR / MODERATE /
minor / note), a security finding also carrying a recurrence-prevention step, an
overall PASS / PASS-WITH-FINDINGS / FAIL line with counts, a re-run ledger with
commands and results, and a follow-up checklist. Commit it before opening the
sibling. If an orchestrator holds the sibling outside the tree, it releases it on
your committed findings.

**Phase 2.** Open the sibling; append `### Reconcile` beneath your verdict:
per-finding notes against its seeded questions and the intent record, any finding
formed at reconcile marked as such, and the overall line restated. Never revise
phase-1 text. Fold the sibling in below the reconcile and delete it.

The author is not the taker, so record every finding and apply nothing; counsel
on fixes is welcome, labelled as counsel.

---

# Verdict — phase 1 (2026-10-17 UTC)

## Provenance

- **Who ran this:** a cold Fable subagent (`claude-fable-5-1`), spawned 2026-10-17 UTC by a
  Fable orchestrator that authored neither the delta nor this brief and passed only the
  spawn prompt (process rules, prefix `FP`, the brief's path). Rule 4's criterion holds: no
  session in this chain started or instructed the authoring run. Tier checked at claim:
  Fable, as the brief requires. The orchestrator forms no finding; every finding and
  severity below is this reviewer's.
- **Tree:** worktree `/Users/mike/worktrees/atelier-review-1017`, branch `review-1017`,
  HEAD `ac88dc4` (descends from `8acfff1`; `instruments/` identical to `main`). No git
  write was run there. Probes ran in a private clone under this session's scratchpad
  (`FP/clone` at `ac88dc4`; `FP/old` holds `83d9b0b^`'s instrument with ONE scratch-only
  edit, an export of `firstUserPromptText`, so old and new could be called side by side).
- **What was read:** this brief; the two landing commits' diffs for the instrument paths;
  `instruments/cctranscript` at HEAD (`gunzipHead`, `cwdFromLog`, `sessionRecord`,
  `archiveSessions`, `runList`, the first-prompt pair, the argv parser, `--help`);
  `instruments/cctranscript.test.js` whole; `instruments/ccrepo` lines 684–700 and
  826–834; `instruments/man/cctranscript.1` lines 360–380; `instruments/README.md`
  lines 60–66 and 572–578; `CHANGELOG.md` lines 154–159; `docs/method/REVIEW.md`
  V1–V7; `.githooks/pre-commit`, `tools/floor.py` and `.github/workflows/ci.yml` for the
  invocations; `docs/roadmap/210-instruments-open-features/240-ccarchive-design-charter.md`
  lines 28–36 (a coldsweep hit; not a barred item). Nothing under `docs/reviews/` except
  this file; no `docs/SESSIONS.md`, `docs/sessions/`, `docs/ROADMAP-DONE.md`, pointer,
  sibling, or the two barred 210 items. No real transcript or archive was read: every
  probe used synthetic mirrors with `HOME` pointed at an empty scratch directory.
- ⚠️ **Exposure, disclosed.** The first `git show` of this pass printed both landing
  commits' message bodies before the orchestrator's bar on them had been registered. They
  hold the author's account (the census, the timings, the disclosed difference). Every
  claim in them was re-driven below rather than taken on trust, and none shaped a
  severity; but the reviewer saw the author's framing before forming findings.
- The brief's line "No later commit has touched either path" was true when written and
  stale an hour later: `cea247e` (2026-10-16 16:43 UTC, item 210/250, merged `99f4c2a`)
  rewrote the body of `firstPromptInLines`. Reviewed at HEAD as the brief directs; the
  rewrite keeps the one predicate shared by the prefix path and the whole-file path, so
  the delta's invariant is unaffected (FP8).

## Lens answers

**1 — Approach & assumptions.** The load-bearing assumptions, named first:

- (a) The bytes `gunzipHead` returns are a byte-exact prefix of what the whole-file
  inflate would return. True for an intact stream (inflate is sequential). **Not
  checked** for a damaged one: gzip's only integrity check (CRC-32 and length) is in the
  trailer, which the prefix path never reaches, so a corrupted-but-still-decodable prefix
  yields bytes the whole-file read would have rejected. This is where "cannot change an
  answer" fails (FP1).
- (b) Line boundaries are the byte `0x0a`, and a cut at the last `0x0a` leaves only
  complete lines. True, and UTF-8-safe: `0x0a` never occurs inside a multi-byte sequence,
  so decoding complete lines from the prefix equals decoding them from the whole.
- (c) The per-line predicate is pure and identical in both paths. True: both call
  `firstPromptInLines`, and `cea247e` changed that one function, not either caller.
- (d) The whole-file split tolerates whatever the prefix split tolerates (CRLF, blank
  lines, unparsable lines). True: same function, same `split('\n')`.
- (e) Nothing changes the file between the prefix read and the fallback read. Driven
  (matrix row "race"): a hit answers from the prefix alone and a miss discards it, so the
  answer always comes wholly from one version; the window cannot produce a mixed answer.
- The 64 KB bound cannot matter to correctness given the fallback, only to speed; the
  census is therefore a tuning claim, not a safety claim, and the shape of its benefit
  reproduces (ledger). Picking it from one archive is fine for a speed path.

**2 — Correctness & quality.** Delta and tests read whole. Matrix below, old (`83d9b0b^`)
against new (HEAD), function-level, bytes read and inflates counted by wrapping `fs` and
`zlib` in the probe process. Every intact case is equal; every divergence is a damaged
mirror, and one divergence is a silently wrong answer (FP1). The new tests do not fail
against the parent's code for any behavioural reason (FP2).

| case | gz bytes | old → new | read old/new | inflates | note |
|---|---|---|---|---|---|
| inside | 814 275 | equal | 1.6 MB / 64 KB | 1/1 | prompt line 3 |
| straddle | 232 420 | equal | 465 KB / 530 KB | 1/2 | prompt line spans the cut |
| after | 1 083 946 | equal | 2.2 MB / 2.2 MB | 1/2 | fallback answered |
| longline-incomp | 162 720 | equal | 325 KB / 391 KB | 1/2 | no `0x0a` in head |
| longline-comp | 424 | equal | 848 B / 424 B | 1/1 | 300 KB line in head |
| noprompt-big | 542 660 | equal (`''`) | 1.1 MB / 1.2 MB | 1/2 | |
| noprompt-tiny | 53 | equal (`''`) | 106 B / 159 B | 1/2 | strict read twice |
| carriers-first | 303 690 | equal | 607 KB / 64 KB | 1/1 | 3 carriers then prompt |
| crlf | 218 208 | equal | 436 KB / 64 KB | 1/1 | `\r\n` ends |
| multibyte-straddle | 235 461 | equal | 471 KB / 536 KB | 1/2 | 3-byte chars at the cut |
| multibyte-later | 66 906 | equal | 134 KB / 64 KB | 1/1 | |
| multimember-m2 | 217 138 | equal | 434 KB / 64 KB | 1/1 | prompt in member 2 |
| multimember-m1 | 217 132 | equal | 434 KB / 64 KB | 1/1 | |
| trailing junk | 108 637 | old throws / new answers | 217 KB / 64 KB | 1/1 | correct text |
| trailing-small | 109 | both throw | | 1/2 | |
| truncated-in | 300 000 | old throws / new answers | 600 KB / 64 KB | 1/1 | the disclosed case |
| truncated-after | 300 000 | both throw | | 1/2 | |
| truncated-small | 40 | both throw | | 1/2 | |
| zero-byte | 0 | both throw | | 1/2 | |
| plain-text-small | 107 | both throw | | 1/2 | |
| plain-text-big | 200 212 | both throw | | 1/2 | |
| bomb-after | 83 369 | equal | 167 KB / 232 KB | 1/2 | 80 MB zeros, prompt last |
| bomb-before | 83 380 | equal | 167 KB / 64 KB | 1/1 | 63 MB inflated for line 2 |
| corrupt-stored | 202 381 | old throws / **new WRONG** | 405 KB / 192 KB | 1/2 | flip in prompt |
| corrupt-huffman | 109 706 | old throws / new lists | 219 KB / 64 KB | 1/1 | flip after prompt |
| corrupt-crc-only | 109 722 | old throws / new lists | 219 KB / 64 KB | 1/1 | trailer bad only |
| corrupt-late | 2 000 560 | old throws / new lists | 4.0 MB / 192 KB | 1/2 | flip at 1.5 MB |

`gunzipHead`'s doubling loop: one read and one inflate on every default-level case (64 KB
compressed inflates past the 64 KB want); the two stored-block (level 0) cases took the
doubling branch — 64 KB then 128 KB read, two inflates — and returned on the hit. Memory
proxy (inflated output bytes): equal to or below the old path on every case except the
highly compressible late-prompt one (FP5). The evicted-mirror guard: `firstUserPromptText`
is reached only from `runList` (both the text and `--json` branches test `s.evicted`
first) and `cwdFromLog` only from `sessionRecord` (guarded); `--search` reads mirrors
through `readTurns` behind its own `evicted && !materialise` skip. No path reads an
offloaded file for a listing. `--search` is untouched by the delta: its diff touches no
line of `runSearch`/`readTurns`, verified by the commit diff and by the HEAD read.

Full CLI listing, old against new, over the clean synthetic pool (the 19 intact mirrors):
text and `--json` byte-identical (SHA-256 equal). Over the dirty pool both abort with an
uncaught zlib error and a raw stack trace, as before; the rows new printed before aborting
include the silently altered prompt from `corrupt-stored`.

**3 — Completeness / harvest.** The behaviour change is in `CHANGELOG.md` and the commit;
not in `--help` (a digest, fine), not in `instruments/man/cctranscript.1`, not in
`instruments/README.md` (FP3). `ccrepo`'s `cwdFromLog` still gunzips every mirror whole for
a 64 KB sniff, under a comment that says a cheap partial read does not exist; the ccarchive
charter item still says cctranscript gunzips every mirror for one column (FP4).

**4 — Security & privacy.** `/security-review` discharged by grounds: it reads this
session's pending diff, which is other reviewers' draft verdicts, not the landed delta; the
read was done by hand against the OWASP Top 10. A01/A02/A05/A07/A10: nothing to bite on
(no auth, no crypto, no config, no network). A03 injection: paths come from `readdir` of
the archive root and reach only `fs` calls; the one spawn (`stat -f`) is pre-existing and
array-argumented. A04 design: the input is the principal's private transcripts; the delta
reads fewer bytes of each and adds no output surface. A06 components: `node:zlib` only.
**A08 integrity: FP1** — the prefix path has no integrity check, so damaged bytes can be
listed as a prompt where the old path refused. A09 logging: a damaged mirror still aborts
the whole listing with a raw zlib stack trace that names the mirror's path (pre-existing,
out of scope, noted under FP1's counsel). Resource use: the prefix inflate is bounded by
what 64 KB of deflate can hold (about 66 MB at the 1032:1 ceiling; 63 MB measured on
zeros), so not a bomb, but FP5. Terminal control sequences: for an intact mirror the
prefix path returns the identical string, and for a damaged one any bytes must still parse
as a JSON string inside a record, so the set of bytes that can reach the terminal is not
widened; `runList` clips at 70 characters and strips nothing, as before. File descriptors:
`gunzipHead` closes in `finally`; the fallback uses `readFileSync`; `cwdFromLog`'s live
branch closes before returning. Privacy of this pass: no real archive read; synthetic
mirrors only; `HOME` pointed at an empty scratch directory for every CLI run.

## Findings

Severities are this reviewer's. Doctrine and design are the principal's to decide; the
work is recorded, nothing applied. Counsel is labelled.

**FP1 — MODERATE (A08 integrity).** The delta's safety claim — "a hit is final … the
prefix … can never change an answer" (code comment, commit, CHANGELOG) — is false for a
damaged mirror, and the disclosed difference understates it. gzip verifies data only in
the trailer; the prefix path never reads the trailer, so a corrupted prefix that still
decodes is trusted. Probe: a level-0 mirror with one byte flipped inside the prompt text
lists the altered text (old: throws); a sweep of 400 single-bit flips across the first
2.4 KB of a default-level mirror's compressed bytes gave 175 both-throw, 187 new-correct
where old threw, and **38 (9.5 %) where new listed wrong text** where old threw. The
commit discloses "a corrupt mirror whose first prompt sits in the intact prefix now
lists" — but the code cannot tell an intact prefix from a damaged one, and the row it
prints can be wrong, which is exactly the harm the brief's "why it earns a review" names.
Mitigants, which hold the severity below MAJOR: it needs a damaged mirror; ccarchive keeps
a SHA-256 manifest and `--verify` for integrity; the listing is a navigation aid and the
chosen session renders through the strict whole-file read, which still throws. *Counsel:*
(i) state the honest contract where the claim now sits — comment, CHANGELOG, man page: the
prefix path reads bytes the trailer never checked, so on a damaged mirror it may list a
wrong or partial first prompt where the whole read refused, and integrity is `ccarchive
--verify`'s job; (ii) pin it with a test built like the probe (level 0, one byte flipped,
assert the altered text is returned, so the contract is explicit rather than accidental);
(iii) optionally, catch the fallback's throw in `runList` and print a marked row (as the
evicted row does) instead of aborting the listing with a stack trace — pre-existing, but
the delta's disclosure leans on that abort as the "before". *Recurrence prevention:* a
partial inflate is unverified data; any consumer that acts on one says so at the point of
use, and the claim "cannot change an answer" is reserved for paths that re-check.

**FP2 — minor.** The five new tests do not distinguish the delta from its parent. Run
against `83d9b0b^`'s code with only the missing export added, all five pass (the parent's
whole-file read satisfies every assertion); without the export they fail on `TypeError`,
not behaviour. They pin the invariant the delta promises, which is worth having, but none
pins the one place behaviour differs (the disclosed truncated-in-prefix case now listing),
and nothing pins the dropped partial line as a behaviour — the comment's rationale ("could
parse as a different, shorter object") is inert for JSONL, since a cut object never parses;
the drop is still right, but for a different reason (a whole-file strict read whose last
line lacks `0x0a` is otherwise re-read, which the `nonl` test shows). *Counsel:* add the
FP1 test and a truncated-in-prefix test; reword the comment to the real reason.

**FP3 — minor (V3).** The behaviour change and the prefix read are stated in `CHANGELOG.md`
and the commit only. `instruments/man/cctranscript.1` (`--from-archive`, `--list`) and
`instruments/README.md` describe listing as peeking each candidate for its first prompt and
say nothing about what a damaged mirror now does. *Counsel:* one sentence in the man page
beside the evicted-marker sentence, carrying FP1's honest contract.

**FP4 — minor (V5, harvest).** Two live statements now contradict the delta.
`instruments/ccrepo` lines 693–695 gunzip every mirror whole for the 64 KB cwd sniff under
"gzip has no cheap partial read", while `cctranscript`'s `gunzipHead` is that read
(ccrepo's rollup cache makes the cost small on warm runs, so the stale comment is the
defect, the harvest a nicety). `docs/roadmap/210-instruments-open-features/240-…` line 33
still says cctranscript's "archive pool still gunzips every mirror for one column
(`210/180`)". *Counsel:* fix the comment (and share the helper if ccrepo ever wants it);
tick the charter line.

**FP5 — note (resource).** `gunzipHead` inflates the whole 64 KB compressed chunk whatever
`want` is (no output cap), and `firstUserPromptText` keeps `head` in scope while the
fallback inflates the whole file, so on a highly compressible mirror whose prompt is late
the new path holds about 1.8× the old peak (143 MB vs 80 MB inflated on the 80 MB-of-zeros
case; 63 MB inflated to read line 2 on the prompt-first case). Bounded, so not a bomb, and
real logs inflate nearer 5–10×. *Counsel:* `head = null` before the fallback, or scope it.

**FP6 — note (speed only).** Two double reads: when the file is at most 64 KB compressed,
`gunzipHead` already did the strict whole inflate, and a miss then re-reads and re-inflates
the same bytes (noprompt-tiny: two inflates); and for every mirror `sessionRecord` and
`runList` each inflate the same 64 KB prefix (cwd sniff, then first prompt), two prefix
inflates per mirror. Neither changes an answer. *Counsel:* carry the sniffed head on the
session record, or return it from `gunzipHead` with a flag saying "this was the whole file".

**FP7 — note (V4).** The 64 KB bound lives as four literals — `FIRST_PROMPT_PREFIX`,
two `65536`s in `cwdFromLog`, the floor in `gunzipHead` — with a comment asserting they
agree instead of one named constant.

**FP8 — note (provenance).** The brief's "no later commit has touched either path" was
overtaken by `cea247e` within the hour; the rewrite of `firstPromptInLines` keeps the
shared-predicate symmetry (assumption c) and the matrix ran at HEAD, so no finding on the
delta — recorded so the next reader of this brief does not take the line as current. Also
noted: `firstUserPromptText` is now exported without the evicted guard its callers apply,
so a future caller must remember it.

## Overall

**PASS-WITH-FINDINGS · 0 MAJOR · 1 MODERATE · 3 minor · 4 note**

The speed path is correct on every intact input the matrix could construct, the listing is
byte-identical over an intact pool, and the CPU shape reproduces. The one claim it rests
on is over-stated for damaged mirrors, and that is a disclosure-and-test gap, not a design
fault.

## Re-run ledger

All from the scratch clone at `ac88dc4` (tests, floors, CLI) or the worktree (sweeps,
lint), foreground, under `nice -n 10`, one heavy process at a time; exit codes read
explicitly. Load averages at the time ran 8–20 (other sessions' suites).

| step | command (abridged) | result |
|---|---|---|
| node suite | `node --test instruments/*.test.js` (once, clone) | 447/447 pass, exit 0 |
| delta tests vs parent | the five `first prompt` tests on `83d9b0b^` + shim | 5/5 pass (FP2) |
| same, no shim | as above without the export | 5 fail, all `TypeError` |
| man lint | `mandoc -T lint instruments/man/cctranscript.1` | silent, exit 0 |
| matrix | `matrix.js` (27 cases, old vs new, counters) | table above; FP1, FP5, FP6 |
| flip sweep | `flips.js` (400 single-bit flips) | 175 / 187 / 38 (FP1) |
| CLI listing | `--list --all --from-archive --dest <clean> [--json]`, old/new | SHA-256 equal |
| CLI listing, dirty pool | same over the damaged mirrors | both exit 1, raw zlib trace |
| timing shape | `timing.js`: 300 mirrors, 111.5 MB gz, 9 late prompts, 3 runs | see below; equal |
| real-archive claims | not run (privacy rule; shape reproduced) | discharged by grounds |
| floor, hook plane | `floor.py --plane hook --root <clone> --tools <clone>/tools` | exit 0 ✅ |
| floor, ci plane | `floor.py --plane ci --root .` (clone) | exit 0, all ✅ |
| Python suite | not in this brief's re-run list | not run |
| coldsweep | delta's names; rule-2 bar + the four `--also-exclude`s | 34 hits, exit 0; not wide |

Timing shape: old 2.33–2.46 s CPU per run of the function over the corpus, new 0.54–0.57 s
(about 4.3×); answers equal on all 300.

The real-archive timing (about 27 s to 7 s for the listing; 24 s to 4 s for the function)
is discharged on grounds: the brief's privacy rule bars displaying a listing, the function
ratio reproduces at about 4.3× on a synthetic corpus of similar shape, and the
byte-identical claim reproduces on the synthetic pool. The census numbers (983 mirrors,
24 beyond 64 KB) are the author's and were not re-counted; they tune speed only.

## Standing checklist V1–V7

- V1 — FP1 (claim stronger than its evidence); the timing and byte-identical claims hold
  in shape.
- V2 — every "measured"/"byte-identical" claim re-driven (ledger); the census discharged
  as a tuning claim.
- V3 — FP3 (man page, README not swept); CHANGELOG is.
- V4 — FP7.
- V5 — FP4 (ccrepo comment; charter line).
- V6 — lens 4 by hand; `/security-review` discharged by grounds; FP1 carries the
  recurrence step.
- V7 — provenance above, including the exposure.

## Follow-up checklist (for the principal / the taker; nothing applied here)

- [ ] FP1 — decide the contract for a damaged mirror and state it in comment, CHANGELOG,
  man page; add the corrupt-prefix test; consider a marked row instead of an abort.
- [ ] FP2 — add the discriminating tests; reword the partial-line comment.
- [ ] FP3 — one man-page sentence beside the evicted marker.
- [ ] FP4 — fix ccrepo's stale comment; tick the charter line.
- [ ] FP5/FP6/FP7 — speed and tidiness counsel, take or leave.
- [ ] FP8 — refresh the brief's "no later commit" line if the brief is reused.

### Reconcile (phase 2, 2026-10-17 UTC)

Opened after the phase-1 commit `6f01de8`, on the orchestrator's release: the sibling's text
(sent verbatim), the queue pointer, the intent record's `210/180` section, and the three prior
verdicts the sibling names (the 2026-10-03 archive-pool pass `CP`, the 2026-08-15 search pass
`CS`, the 2026-08-17 plain-reply design pass). The two commissioning 210 items stay unopened:
the release did not name them. Phase-1 text above is unrevised. No suite re-run; no new probe.

**Seeded question 1 — the comment's "can never change an answer" against the commit's
disclosed difference.** Both cannot be true as written, and the comment is the overclaim (V1):
FP1 stands and is sharper than the seed, because the probe shows the difference is not only
"lists instead of aborting" but "can list wrong text" where the old read refused. On whether
the new behaviour is the one the tool wants: the direction is the one two prior passes
counselled — `CP4` (2026-10-03) and `CS11` (2026-08-15) both found `firstUserPromptText`
aborting the whole listing with a raw stack on an unreadable or damaged mirror and asked for a
per-row guard with a marker, as `--search` does. Neither was taken, and the delta's disclosure
now leans on that still-open abort as its "before". FP1's counsel (iii) is `CP4`, not a new
ask; the honest contract (i) and the pinning test (ii) are this pass's additions.

**Seeded question 2 — how large is the decoded buffer, and is it ever worse than the whole
read?** FP5 answers it: `gunzipHead` returns the whole inflate of 64 KB compressed, so on a
1000:1 body it returns about 63–67 MB (this pass measured 63 MB on zeros; `CP` measured 67 MB
and a 129 MB RSS delta on the same shape). It is worse than the old path only when the prompt
is beyond the prefix on a highly compressible mirror, where the retained `head` plus the
fallback's whole inflate peaks at about 1.8× the old (143 MB against 80 MB inflated). `CP7`
recorded that the listing's memory peak sat in `firstUserPromptText`; the delta lowers it for
every prompt-early mirror and can raise it for a late-prompt compressible one. Note-level, as
phase 1 rated it.

**Seeded question 3 — is a `Z_SYNC_FLUSH` partial inflate always a byte-exact prefix of the
full decompression, including multi-member files and trailing bytes?** For an intact stream,
yes: this pass's matrix (two multi-member shapes, two trailing-bytes shapes, a straddling
multi-byte line) and `CP`'s eight shapes (a member cut inside the next member's header, trailing
garbage beyond the prefix, a long `FNAME` header) agree, with no counter-example found. For a
damaged stream, no — and that is FP1: nothing in the prefix path can know the stream is intact,
because gzip's check is in the trailer. The "first match is final" argument therefore holds
exactly as far as the mirror is intact; on trailing junk the prefix is exact and the whole read
refuses anyway, which is the disclosed class.

**Seeded question 4 — a bound fitted to one machine's data, and what the comment publishes.**
Soundness: for a speed-only bound with a whole-file fallback, a census of one archive is an
adequate basis (lens 1); the number tunes cost and cannot change an answer for an intact
mirror. Publication: this pass had not weighed the second half, so it is formed here.

**FP9 — note (formed at reconcile; privacy, the principal's call).** The code comment, the
CHANGELOG entry, the commit body and the intent record all state the principal's archive's
shape — 983 mirrors, the first-prompt distribution out to a 2.9 MB tail, listing CPU before and
after — in a public repository. It is aggregate and names no session, path or text, and the
repo's changelog already carries timings "on one real archive", so the sensitivity is low; but
the public comment carries more of the archive than its justification needs. *Counsel:* the
comment can say "a census of one archive: nearly every first prompt within 16 KB, a flat tail
beyond", and the counts can stay in the session record, if the principal wants the archive's
size kept out of the code.

**Seeded question 5 — do the new tests fail against the parent?** No: FP2. With only the
missing export added to the parent, all five pass; without it they fail on `TypeError`. They
pin output equality, which the parent had, and not the one place behaviour differs.

**Against the intent record.** Its `210/180` section states what the commit states (three
byte-identical listings, 983 equal answers, about 27 s to 7 s, Node 411 pass) and adds that
the worker measured `--search` and left it alone because a prefix cannot be output-identical
there — consistent with the non-goal and with this pass's HEAD read. The record names a Sonnet
worker as builder; the pointer counts that as the run's authorship, and rule 4's criterion is
unaffected. Nothing in the record alters a finding or a severity.

**Against the pointer.** Refs-only, as the sibling says. The pointer was added by `78cc660`,
after the close commit, and says so itself: queuing followed landing by one commit rather than
riding it. Recorded for V7's count; no finding, since the lag is disclosed in the pointer and
cost the review nothing.

**Against the prior verdicts.** `CP7` proposed exactly this change, with the caveat that the
first user line is not guaranteed inside 64 KB so a fall-through is needed; the delta honours
the caveat. `CP4` and `CS11` remain open and FP1's counsel (iii) folds into them. `CP6`
(no CHANGELOG entry at the 2026-10-03 landing) does not recur: this delta's entry exists. The
2026-08-17 design pass touches `firstUserPromptText` only as a name in a list; nothing to
reconcile.

**Overall line, restated:** PASS-WITH-FINDINGS · 0 MAJOR · 1 MODERATE · 3 minor · 5 note
(FP9 added at reconcile; phase-1 severities unchanged).

## Deferred material — folded in at reconcile

# Deferred sibling — cctranscript's first-prompt prefix read

**Held under rule 1's split** (`docs/method/REVIEW.md`). Open only after your
phase-1 findings are committed to the brief
`docs/reviews/2026-10-16-1550-first-prompt-prefix-cold.md`. At verdict, fold this
file in below your reconcile and delete it.

Written 2026-10-16 UTC by the Opus brief-writer named in the brief, which authored
none of the delta and forms no finding: the questions below are seeds, a floor
and never a fence.

## Intent record

- `docs/sessions/2026-10-05-1120-queue-run-closes-and-builds.md` — **not opened
  by the brief-writer**. The follow-up commit `72bc6d3` appended to it.

## Prior verdicts on the same surface (named, not opened)

Path greps over `docs/reviews/` for `instruments/cctranscript` name these; none
was opened by the brief-writer:

- `docs/reviews/2026-08-15-1032-cctranscript-search-cold.md`
- `docs/reviews/2026-08-17-1321-plain-reply-repurpose-design.md`
- `docs/reviews/2026-10-03-0357-archive-pool-speedup-cold.md` — by its name, the
  likeliest review of the change that introduced `gunzipHead`

## The pointer's own lens hints

None. The pointer is refs-only (delta, intent record, tier, pass type). Note for
V7 and rule 4's landing = queuing: the pointer was added by `78cc660`, after the
close commit `72bc6d3`, not in the commit that landed the work; that commit's
message says so itself.

## Seeded questions

1. The code comment says the bound "can never change an answer"; the commit
   message discloses that a corrupt mirror whose prompt sits in the intact prefix
   now lists instead of aborting the listing. Both cannot be true as written. Is
   the comment an overclaim (V1), and is the new behaviour the one the tool
   wants?
2. `gunzipHead` inflates with `Z_SYNC_FLUSH` and returns as soon as it has at
   least `want` bytes — it can return far more. For a highly compressible log, how
   large is the buffer the prefix path decodes and then converts to a string, and
   is that ever worse than the whole-file read it replaced?
3. Is a `Z_SYNC_FLUSH` partial inflate always a byte-exact prefix of the full
   decompression — including multi-member files and files with trailing bytes —
   which the "first match is final" argument needs?
4. The 64 KB bound and its justification come from a census of the principal's
   own archive, recorded in a code comment. Is a number fitted to one machine's
   current data a sound basis even for a speed-only bound, and does the comment
   publish anything about the private archive (its size, its shape) that should
   not be in a public file?
5. Do the new tests actually fail against the parent, or do they pass on both
   (pinning only output equality, which the parent already had)?
