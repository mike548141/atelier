# Cold pass — "harvest" scoped to monolithic boards across the close lists

**Pass type:** doctrine cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at selection by
whoever takes this pass.
**Status:** BRIEF ONLY — the review has NOT run. Written 2026-10-16 UTC by an Opus brief-writer;
the pass waits for a further cold Fable session that neither the delta's author nor this
brief-writer (nor its orchestrator) started or instructed; tier checked at selection (rule 4).
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/540-rule-4-cold-pass-queued-harvest-only-on-a-monolithic-board.md`.
**Why it earns a review:** it edits what every session does at close — in the record doctrine,
the queue-run pattern, the queue-run skill and the principal's own session-open prompt — and
narrows a word that more than one rule uses.

## Spawn provenance

- **Author of the work under review:** the 2026-10-03 queue run that landed the commit below; its
  intent record is the session file dated 2026-10-03 0144 UTC that the pointer names (not opened
  by the brief-writer). The commit's trailer names an Opus model.
- **Who wrote this brief:** an Opus subagent (`claude-opus-5-5`) dispatched by the Mike-opened
  Opus queue-run session `abe96d8d` on 2026-10-16, on Mike's answer of that date that a fresh Opus
  session writes these briefs. Neither it nor its orchestrator authored the delta or was started
  or instructed by its author. **Off-tier for review, disclosed: it forms no finding and writes no
  severity**, and stops after this brief and its sibling.
- **Who takes the review:** a further cold Fable session, not yet started, passing rule 4's
  criterion. If it runs as reviewer-plus-orchestrator, the off-tier conditions of rule 4 apply and
  are disclosed in the claim, the pointer and the verdict. The reviewer repeats its own provenance
  in the verdict.
- ⚠️ **Brief-writer's exposure, disclosed** (rule-2 material met before writing): the seven queue
  pointers it was assigned (160/500, 520–570; refs-only, each ending in the orchestrator's claim
  line); the seven landing commits' subjects, `--stat` lists, full message bodies (the author's
  account) and diffs on the delta paths; `docs/method/REVIEW.md` in full; the ask halves of two
  2026-10-04 briefs as templates; HEAD text of the neighbouring surfaces named in *Scope*; single
  grep-hit lines from unrelated board items and old `CHANGELOG.md` entries; filenames (not
  contents) of prior verdicts; and its own cross-session memory index. It did not open the intent
  record, the commissioning board item, `docs/SESSIONS.md`, `docs/sessions/`,
  `docs/ROADMAP-DONE.md` or any prior verdict. Its orchestrator read the `docs/SESSIONS.md` index
  tail (entries through 2026-10-16, including the authoring run's one-paragraph summary) and the
  2026-10-16 session record's close section, and passed no evaluative content beyond the pointer
  list. Everything evaluative the brief-writer formed is in the sibling.

## What the work is

Landing commit (diff it on the delta paths; review at HEAD, `2e2da81` or later):

- `b218f1e` (2026-10-03) — record: harvest is a monolithic-board step, everywhere it is named
  (200/100 C3)

Delta paths (the pointer's own list):

- `docs/method/RECORD.md` — the harvest trigger, at the end of the harvest-integrity paragraph
- `docs/method/CONCURRENCY.md` — the closing-litany bullet in § *Orchestrated queue runs*
- `docs/method/session-open/session-open-prompt.md` — *Ending the session*
- `skills/queue-run/SKILL.md` — step 6, *Per-item close*

## Scope

Widest the work admits; the lenses organise it, they do not bound it. Non-goals are the only
narrowing and are themselves reviewable.

Probe, at least:

- **What "harvest" means.** Collect every sense the live doctrine gives the word: RECORD's
  (collapsing closed items to pointers, moving detail to the archive store), `GLOSSARY.md`'s
  (extracting what a piece of work taught into durable records), the apex's "Harvest, then
  encode", REVIEW's lens 3 *Completeness / harvest*. Say which sense each delta site meant before
  the edit and after it, and whether narrowing one sense dropped another from a close list.
- **RECORD agrees with itself.** The split-board rule (a completed item flips `[x]` in its own
  file and "there is no harvest step") against the edited trigger; and whether "the session-close
  tidy-up (above)" still resolves to the passage it means.
- **The new term.** "Roadmap close" appears in two delta sites. Is it defined anywhere a session
  would look, and does each site's parenthetical parse for a split board, a monolithic board, and a
  repo mid-migration?
- **The tools agree.** `tools/harvestscan.py`, `tools/sizescan.py`'s archive gate and
  `tools/board.py`, as documented in `tools/README.md`: do they treat split and monolithic boards
  the way the edited text says?
- **Children.** The template `docs/build/templates/docs/ROADMAP.md` stamps a monolithic board.
  Does a child reading its stamped close rule now know what to do at close?

**Non-goal:** the split-board design itself (already doctrine). The close lists' consistency with
it is the subject.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself first. Ask whether
   scoping the word was the right fix, against defining it once and pointing at the definition.
2. **Correctness & quality.** Diff `b218f1e` on the four paths. Record, per delta site, the text
   before and after and which board shapes it now covers.
3. **Completeness / harvest.** Every other close list that names the roadmap step: the template
   `CLAUDE.md` *Session rhythm* bullet, this repo's `CLAUDE.md`, the `session-onramp` skill, the
   PROPAGATION floor region, other files under `docs/method/session-open/`. Which were left as
   they were, and does each still agree?
4. **Security & privacy** — mandatory. Harvest moves or deletes record content; RECORD makes bulk
   deletion from a record store a show-first action. Say whether the scoping changes when that
   deletion happens or whether it is shown first. No code surface: `/security-review` is
   discharged by grounds.

## Re-run obligation

Re-run, do not read. Lift invocations from `.githooks/pre-commit`, `tools/floor.py` and
`.github/workflows/ci.yml` rather than guessing.

- `python3 tools/harvestscan.py --root . .`, `python3 tools/sizescan.py --check --root . .` and
  `python3 tools/board.py --check --root .`, exit codes read explicitly
- `python3 tools/pathscan.py --root . .` and `python3 tools/linkscan.py --root . .` over the
  delta sites' cross-references
- the floor on both planes at HEAD (`python3 tools/floor.py --plane ci --root .`)

## House rules for this run

- Name your own review worktree in the verdict; it is read-only to you except for THIS file. Other
  sessions may be live on this machine: touch nothing outside your worktree and your scratch
  clone. Never open another `docs/reviews/2026-10-16-1510-*` file — it is another pass's framing.
- No git command that writes in the worktree, beyond committing this one file at the end of each
  phase (or handing it to your orchestrator to commit). Read-only git is fine. Older checkouts go
  in a private clone under your session scratchpad, named by your prefix.
- One heavy process at a time: the full Python suite at most once, in the foreground; never point
  a scanner at another repo on the machine.
- `/security-review` reads the session's pending diff, not this delta. Discharge it by grounds, or
  keep the tree clean when you spawn it — never with this brief or its sibling dirty.
- Absolute ISO 8601 dates from `date -u`; prose wrapped at ≤ 100 columns; NZ English. Never quote
  a secret, a placeholder token, an email address or a personal detail — this repo is PUBLIC.
- Review deep, not fast: a finding needs a probe or a re-driven claim behind it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the deferred material lives in the sibling .deferred.md under the rule-1 split, opened only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`, every
prior verdict in `docs/reviews/`, the queue pointer
`docs/roadmap/160-doctrine-review-owed/540-rule-4-cold-pass-queued-harvest-only-on-a-monolithic-board.md`,
the sibling `docs/reviews/2026-10-16-1510-harvest-monolithic-board-cold.deferred.md`, the landing
commit's message body (the author's account; read subject, stat and diff only), and the
commissioning item
`docs/roadmap/200-anti-slop-invariant-registry-promote-rec/100-r2-found-eleven-live-contradictions.md`.

Sweep with `python3 tools/coldsweep.py --root <your-worktree> --also-exclude
docs/roadmap/160-doctrine-review-owed/540-rule-4-cold-pass-queued-harvest-only-on-a-monolithic-board.md
--also-exclude docs/reviews/2026-10-16-1510-harvest-monolithic-board-cold.deferred.md
--also-exclude
docs/roadmap/200-anti-slop-invariant-registry-promote-rec/100-r2-found-eleven-live-contradictions.md
<pattern>`; `--include-barred` only with disclosure in the verdict. Reading the delta is never
barred; the author's narrative of why, and the verdicts that recorded it, are.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list. Append your verdict
below a `---` divider in THIS file: provenance repeated (how you were spawned, your tier, what you
read), per-lens answers, findings with stable IDs (prefix `HM`: `HM1`, `HM2`, …) and severities
(MAJOR / MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL line with counts, a
re-run ledger (commands and results) and a follow-up checklist. Then STOP and commit this file
before opening the sibling. Edit no other file.

**Phase 2.** Open the sibling. Append `### Reconcile` beneath your verdict: per-finding notes
against its seeded questions and the intent record, any finding formed at reconcile marked as
such, and the overall line restated. Never revise phase-1 text. Fold the sibling in below the
reconcile and delete it.

Findings on doctrine are the principal's to decide (rule 3): record all, apply nothing; counsel
per finding is welcome, labelled as counsel.

---

# Verdict — phase 1 (2026-10-17 UTC)

## Provenance, repeated

- **Reviewer:** a fresh `claude-fable-5-1` subagent (the principal-named review tier), spawned
  2026-10-17 by a Fable orchestrator that authored neither the delta nor this brief and holds
  the deferred sibling outside the reviewer's reach until these findings are committed. The
  orchestrator forms no finding and writes no severity. Neither party was started or
  instructed by the 2026-10-03 queue run that landed `b218f1e` (rule 4's criterion, met).
- **Worktree:** `/Users/mike/worktrees/atelier-review-1017`, branch `review-1017`, HEAD
  `92ca3de` (`8acfff1` is an ancestor; `b218f1e` is an ancestor). Read-only to this reviewer
  except for this file; no git command that writes was run.
- **What was read:** the landing commit's subject, `--stat` and diff on the four delta paths
  (never its message body); the four delta files at HEAD; `REVIEW.md` (rules 1–4, lenses, the
  standing checklist); `RECORD.md` in full; `GLOSSARY.md` § *Process*; `00-APEX.md` the
  "Harvest, then encode" bullet; `CONCURRENCY.md` § *Orchestrated queue runs*;
  `PRINCIPLES.md` §6; `PROPAGATION.md` § *The standard child doctrine block*; the template
  `CLAUDE.md` and `docs/ROADMAP.md`; `REPO-STANDARD.md` line 147–148; the `session-onramp`,
  `queue-run` and `review-brief` skills; `tools/README.md` § sizescan and § harvestscan; the
  heads of `tools/harvestscan.py`, `tools/sizescan.py`, `tools/board.py` and the scanner
  registry in `tools/floor.py`; `git log` subjects on each delta path and the subject, stat
  and diff of the two later commits on the session-open path (`4d80321`, `6a0ac93`) plus
  `6a0ac93`'s message body, which is not a barred commit; two unbarred board items that the
  sweep surfaced (`010/040`, `320/670`).
- **Exposure, disclosed:** both sweeps ran with the brief's three `--also-exclude` paths and
  **without** `--include-barred`. No prior verdict, `docs/SESSIONS.md`, `docs/sessions/`,
  `docs/ROADMAP-DONE.md`, the queue pointer, the commissioning item or the sibling was opened.
  `/security-review` was not run (grounds under lens 4). The generated index
  `docs/ROADMAP.md` was touched only through sweep hit-lines.

## Load-bearing assumptions, named first (lens 1)

1. *"Harvest" names one thing, so scoping it at each site is enough.* **False** — the live
   doctrine gives the word at least two senses (HM2).
2. *The four delta sites are the only close lists that name the roadmap step.* **Mostly
   true** for the word; **false** for the step — the child template names it without the word
   (HM4).
3. *A word-led edit at four sites stays landed.* **False** at HEAD — one site was reverted by
   a later restore (HM1).
4. *The tools already treat the two board shapes the way the edited text says.* **True**:
   `board.py` renders done items as ✅ so `sizescan`'s cold-content gate cannot fire on the
   generated index; `harvestscan` watches the board directory; both re-ran clean.

**Was scoping the word the right fix, against defining it once and pointing at it?** The
weaker of the two. Scoping at each site produced three phrasings for one step (HM3) and left the
word's other sense, in `GLOSSARY.md` and the apex, pointing at the one passage where the word
now means something else (HM2). A single definition would have fixed the contradiction C3 named
once, and left each close list free to say "roadmap close" and point.

## Per-lens answers

**Lens 2 — correctness, per delta site (before → after, and which shapes it now covers):**

- `RECORD.md` trigger — before: "harvesting is part of the session-close tidy-up"; after:
  "on a **monolithic** board, harvesting is part of…; a split board has no harvest step: a
  closed item flips `[x]` in its own file". At HEAD: as landed. Covers both shapes explicitly.
- `CONCURRENCY.md` litany — before: "the roadmap harvest"; after: "the roadmap close (a
  harvest on a monolithic board)". At HEAD: as landed. Covers both; a repo mid-migration is
  resolved by RECORD's "keeps the monolithic form", not by the site.
- `session-open-prompt.md` — before: "roadmap harvested"; after: "roadmap items closed
  (harvested, on a monolithic board)". At HEAD: **reverted to "roadmap harvested"** (HM1). On
  a split board that is a wrong instruction again.
- `queue-run/SKILL.md` step 6 — before: "roadmap harvest"; after: "roadmap close". At HEAD:
  as landed. Covers both by pointing at RECORD; the term is undefined (HM3).

`RECORD.md` agrees with itself at the two passages the brief named: the split-board rule
(line 230–236, "there is no harvest step") and the edited trigger (278–282) say the same thing,
and "the session-close tidy-up (above)" resolves to § *The session log*'s "Finish the sequence,
then *declare* the close" bullet, which is shape-neutral ("update the roadmap / changelog /
follow-ups"). A third passage in the same file does not agree (HM5).

**Lens 3 — completeness / every other close list:** the template `CLAUDE.md` *Session rhythm*
bullet and its `PROPAGATION.md` floor copy name put-away plus an evidence-based all-clear and
point at `RECORD.md` — shape-neutral, still agree. This repo's `CLAUDE.md` names only the
`SESSIONS.md` entry — agrees. The `session-onramp` skill carries no close list — nothing to
agree. `docs/method/session-open/` holds one file — the reverted site (HM1). `docs/roadmap/
README.md` line 17 states the split-board rule — agrees. The child template `docs/ROADMAP.md`
and `REPO-STANDARD.md` name the step without the word, with a trigger neither the gate nor
RECORD recognises (HM4). The commit's own subject, "everywhere it is named", is re-driven false
by HM4 and HM5 (one site named without the word; one unscoped mention in the delta's own file).

**Lens 4 — security & privacy:** the delta is prose in four markdown files; there is no code,
input or credential surface. `/security-review` is discharged by grounds: it reads this
session's pending diff, which is other reviewers' drafts, and its own exclusions bar markdown,
so a run would be both an exposure and definitionally empty. Read by hand against the OWASP
Top 10 classes: none applies to a doctrine edit. The lens's live question — whether the scoping
changes when record content is deleted or whether it is shown first — is answered in HM7: no.

**Lens 5 (the brief's "Children"):** a child reading its stamped header is told to spill
completed detail "once it grows"; its floor reds on the first `[x]` it leaves inline. It does
not know what to do at close (HM4).

## Standing checklist

- **V1** — the commit subject's "everywhere it is named" runs past its evidence (HM4, HM5);
  CONCURRENCY's "binds in … the child `CLAUDE.md` block" likewise (HM6).
- **V2** — every re-run in the brief's list was run (ledger below); the floor is green at
  HEAD; `pathscan`'s warn-only findings recorded (HM9).
- **V3** — swept to mirror sites: one site reverted (HM1), one mirror missed because it does
  not use the word (HM4), one in-file mention unscoped (HM5).
- **V4** — three phrasings for one step, none stamped (HM3).
- **V5** — RECORD lines 120–130 vs 230–236 (HM5); GLOSSARY vs RECORD on the word (HM2).
- **V6** — lens 4 above; HM7.
- **V7** — provenance stated in the brief and repeated above.

## Findings

Findings on doctrine are the principal's to decide (rule 3): recorded, nothing applied.
Counsel is labelled.

**HM1 — MAJOR — one of the four delta sites is reverted at HEAD, and the board under-reads
it.** `docs/method/session-open/session-open-prompt.md` line 122 reads the pre-delta "roadmap
harvested". Probe: `git log` on the path shows `b218f1e` (2026-10-03), then `4d80321`
("the missed intermediate version, inserted late"; author and committer dates both
2026-09-14), then `6a0ac93` (2026-10-17, "restore current content after inserting the missed
historical commit"). `4d80321`'s diff replaces the delta's line with the old one; `6a0ac93`'s
diff does not touch that line, so the restore was taken from a snapshot older than `b218f1e`.
`git blame -L 122,122` now attributes the line to 2026-09-14. Effect: the prompt the principal
opens sessions with tells every session on this split-board repo to harvest the roadmap, the
exact contradiction C3 fixed, while `RECORD.md` says there is no harvest step. Board item
`320/670` (a child's hand-up, 2026-10-17) has the regression but reads this hunk as "smaller,
and maybe intended" — it was not intended: it undoes a landed, review-queued ruling (this
pass's own delta). *Counsel:* restore the `b218f1e` wording under `320/670`'s remedy, and
correct that item's text so hunk 2 is recorded as a reversal, not a possible intent. Class
lesson for the record: a "restore" takes its base from the last commit on the path, checked
with `git log -- <path>`, never from a remembered version.

**HM2 — MODERATE — "harvest" has two live senses and the delta scoped one without saying
which.** `GLOSSARY.md` line 73: *closing a piece of work by extracting what it taught into the
records that outlive it; integrity rules in RECORD.md*. `00-APEX.md` line 242, "Harvest, then
encode", uses that sense. `RECORD.md` § *The roadmap* uses a different one: the mechanical move
of completed detail to the archive store. `REVIEW.md` lens 3 and the `review-brief` skill use
a third, the reviewer's "Completeness / harvest". The delta's "A split board has no harvest
step" is true in RECORD's sense and false in GLOSSARY's — a split-board session still extracts
what the work taught at close, as the apex demands — and a reader who follows GLOSSARY's pointer
to RECORD lands on the one passage where the word means the other thing. Nothing in any of the
four sites says which sense is scoped. *Counsel:* give the mechanical sense its own word in
RECORD (relocation, archive move) and leave "harvest" to GLOSSARY's sense; or add the second
sense to the GLOSSARY entry with the board-shape qualifier. Either is one edit; the choice is
the principal's.

**HM3 — minor — "roadmap close" is a new, undefined term, and the step now has three
phrasings.** `CONCURRENCY.md` line 918: "the roadmap close (a harvest on a monolithic
board)"; `skills/queue-run/SKILL.md` line 78: bare "roadmap close", pointing at `RECORD.md`
for the contents — where the phrase does not occur (the reader finds the concept at lines
230 and 279, not the term); the session-open site as landed: "roadmap items closed
(harvested, on a monolithic board)". No GLOSSARY entry. The CONCURRENCY parenthetical parses
for a split board (flip `[x]` in the item file) and a monolithic one (collapse to pointers);
a repo mid-migration is resolved by RECORD's "a repo that has not adopted the split keeps the
monolithic form" rather than by the sites themselves. V4: one fact, three homes, no stamp.
*Counsel:* one GLOSSARY entry for "roadmap close" naming both shapes; the sites say the term
and point.

**HM4 — MODERATE — the child's stamped close rule names a trigger neither the gate nor RECORD
recognises.** `docs/build/templates/docs/ROADMAP.md` line 5 and `docs/build/REPO-STANDARD.md`
line 147–148: move completed detail to `ROADMAP-DONE.md` "once it grows". The gate every child
runs — `sizescan --check`, enforced on the ci plane in `tools/floor.py`'s registry and reached
through `floor.yml` — fires on the first `[x]` left inline on a `ROADMAP.md` and never on
length (`tools/README.md` § sizescan; the module docstring). RECORD's trigger, the delta, says
at session close. So a child following its own header reds its floor on its first pushed `[x]`
— the 2026-07-23 case `RECORD.md` lines 120–130 grounds. The delta's "everywhere it is named"
missed it because the template never uses the word "harvest"; the 2026-09-18 sweep (`010/040`)
passed the same header as "current for the children" on the same word-led basis. *Counsel:*
"once it grows" → "in the commit that closes the item — the floor's `sizescan` gate reds on a
`[x]` left inline", at both sites.

**HM5 — minor — monolith-era wording survives unscoped in the delta's own file.** `RECORD.md`
lines 120–130: "CI runs checks a local scan does not — reviewscan…, the harvest gate a pushed
`[x]` trips". On this split board the generated `ROADMAP.md` renders done items as ✅, never
`[x]` (`tools/board.py` line 52–53, 226–227), so the gate cannot trip; and since 2026-09-20 the
hook plane runs `sizescan --check` too (`floor.py` registry), so a pushed `[x]` is no longer a
thing only CI sees. The sentence holds for a child on a monolithic board with no hook installed
and is stated as a general present-tense rule. *Counsel:* scope it ("on a monolithic board,
where the hook is not installed") or fold the claim into the dated grounding parenthesis as
history.

**HM6 — note — a small overclaim the delta edited around.** `CONCURRENCY.md` line 920: the
litany "already binds in `RECORD.md` and the child `CLAUDE.md` block". The block's
session-rhythm bullet (`PROPAGATION.md` line 163–169; template `CLAUDE.md` line 75–82) carries
put-away plus an evidence-based all-clear and points at RECORD; it does not carry the litany's
contents. *Counsel:* "binds in `RECORD.md`, which the child `CLAUDE.md` block points at".

**HM7 — note — lens 4 answer: the scoping changes neither when record content is deleted nor
whether it is shown first.** On a split board the harvest step is removed outright, so no
relocation happens at close; on a monolithic board the move at close is as it was, and both
the show-first rule (`RECORD.md` 238–255) and `harvestscan`'s ≥ 50-net-line warn are untouched
by the delta. One ambiguity pre-exists and is recorded for the principal: the show-first rule's
letter, "removing a block from a record store", covers a routine lossless harvest move as much
as a deletion; whether a move counts as removal is unstated.

**HM8 — note — a backdated commit makes the path's history read backwards.** `4d80321` carries
author and committer dates of 2026-09-14 yet sits after `b218f1e` (2026-10-03) in the history;
`git blame` dates line 122 to 2026-09-14 although it became live on 2026-10-17, and a
date-sorted log on the path tells the story in the wrong order. Found tracing HM1; outside the
delta.

**HM9 — note — re-run residue, none the delta's.** `pathscan` (warn-only on both planes)
reports one stale path on the repo-plane run (`tools/README.md` line 1509, a sessions-archive
directory that does not exist) and two on the ci plane (a 2026-10-03 decision record naming a
tool file that does not exist; the session-open prompt's line 15 relative path, which is
written from a child's perspective by design). Recorded so the reds are not lost.

## Overall

**PASS-WITH-FINDINGS — 1 MAJOR · 2 MODERATE · 2 minor · 4 note.** The delta did what it
claimed at the three sites that are still as landed, and `RECORD.md` agrees with itself at the
two passages the brief named. The MAJOR is the live state, not the author's edit: a later
restore reverted the principal's own session-open prompt to the contradictory wording, and the
board item that noticed reads it as possibly intended. The MODERATEs are the two things a
word-led scoping could not reach: the word's other sense, and the one mirror that names the
step without the word.

## Re-run ledger

All from the worktree root, each under `nice -n 10`, in the foreground, one at a time.

- `date -u` → 2026-10-17 10:10 UTC.
- `git merge-base --is-ancestor` for `8acfff1`→HEAD, `b218f1e`→`6a0ac93`, `6a0ac93`→`8acfff1`
  → all true.
- `python3 tools/harvestscan.py --root . .` → exit 0, clean.
- `python3 tools/sizescan.py --check --root . .` → exit 0, clean; 0 suppressed, 0 inert
  hatches.
- `python3 tools/board.py --check --root .` → exit 0, index current.
- `python3 tools/pathscan.py --root . .` → exit 1, 1 finding (HM9); 395 record files excluded
  by default.
- `python3 tools/linkscan.py --root . .` → exit 0, clean; 4 suppressed by allow-marker.
- `python3 tools/floor.py --plane ci --root .` → exit 0, floor green at HEAD; `harvestscan`,
  `pointerscan`, `pathscan` and `indexscan` warn-only; `pathscan` 2 findings (HM9);
  `secretscan` 23 advisory; `leakscan` enforced without `--require-terms` on this plane.
- `python3 tools/coldsweep.py --root . <the brief's three --also-exclude> -i 'harvest'` →
  385 hits over 641 files, 396 barred files excluded; no `--include-barred`.
- the same sweep with the pattern for "roadmap close", "roadmap items closed", "roadmap
  harvest" and "close(s) roadmap" → 8 hits; same exclusions.

Not run, by the brief's and the run's rules: the full Python suite and the node suite (not in
the re-run list; machine load averaged above 10 throughout); `/security-review` (grounds in
lens 4). The dirty tree the floor saw was the orchestrator's context partition (deleted
`.deferred.md` siblings), which is why `harvestscan` reported a −14 net-line change.

## Follow-up checklist (for the principal's ruling; the reviewer applies nothing)

- [ ] HM1 — restore the `b218f1e` wording at the session-open site; correct `320/670`'s
      reading of hunk 2 (MAJOR)
- [ ] HM2 — one definition of "harvest", or a second word for the mechanical sense (MODERATE)
- [ ] HM4 — the child template and `REPO-STANDARD.md`: "once it grows" → at the item's close
      (MODERATE)
- [ ] HM3 — a GLOSSARY entry for "roadmap close"; the three sites point at it (minor)
- [ ] HM5 — scope or historicise `RECORD.md` lines 120–130 (minor)
- [ ] HM6, HM7, HM8, HM9 — notes; HM9's stale paths are ordinary hygiene for any session
