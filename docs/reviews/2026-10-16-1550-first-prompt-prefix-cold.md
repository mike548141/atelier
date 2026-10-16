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
