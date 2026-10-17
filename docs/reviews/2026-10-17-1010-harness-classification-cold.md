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
