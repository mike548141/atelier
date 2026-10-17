# Cold pass — the concurrency cue count

**Pass type:** doctrine cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at selection by
whoever takes this pass.
**Status:** BRIEF ONLY — the review has NOT run. Written 2026-10-16 UTC by an Opus brief-writer;
the pass waits for a further cold Fable session that neither the delta's author nor this
brief-writer (nor its orchestrator) started or instructed; tier checked at selection (rule 4).
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/560-rule-4-cold-pass-queued-three-cues.md`.
**Why it earns a review:** § *The trigger* is how a session learns it may not be alone; the
delta changes the count of its firing cues and so every claim the paragraph makes about "the
cues" as a set. A small delta: keep the review proportionate, but test every predicate.

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

Landing commit (diff it on the delta path; review at HEAD, `2e2da81` or later):

- `df0820e` (2026-10-03) — concurrency: three cues, not two (200/100 C5)

Delta path: `docs/method/CONCURRENCY.md`, § *The trigger*: the paragraph introducing the firing
cues and the line that heads their list. Read the whole section; the delta's meaning depends on
the sentences around the two edited words.

## Scope

Widest the work admits; the lenses organise it, they do not bound it. Non-goals are the only
narrowing and are themselves reviewable.

Probe, at least:

- **Every predicate over the set.** The paragraph and the list say the cues are cheap, need no
  locking machinery, are ways to *discover* concurrency, and that their silence licenses nothing;
  the third cue's own text calls the other two "discoveries you make by accident". Test each
  predicate against each of the three cues and record a cue-by-predicate table.
- **What a cue is.** The paragraph opens "The substrate rule still needs a firing cue". For each
  cue, does it end in the substrate action (move to a worktree), or only in knowledge? Is each a
  cue in the paragraph's own sense?
- **The section's opening.** Its first paragraph speaks of "a blind spot in the cues below" and
  names one cue's limit. Does it still read true over three?
- **History.** Find when the third cue and § *The channel* landed (`git log -S`), and whether
  that landing left other set-level claims or mirror sites un-updated besides the count.
- **Mirror sites.** Any other place that counts, lists or summarises the cues: the PROPAGATION
  floor region and its stamped template copy, this repo's `CLAUDE.md`, the `session-onramp` and
  `queue-run` skills, `docs/method/GLOSSARY.md`, § *The channel* itself.

**Non-goal:** the cues themselves (already doctrine); the paragraph's claims about them, and its
agreement with its mirrors, are the subject.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself first. Ask whether
   correcting a count was the whole of what the mismatch signalled.
2. **Correctness & quality.** Diff `df0820e`. Produce the predicate table above.
3. **Completeness / harvest.** The mirror sweep above; say which sites agree at HEAD.
4. **Security & privacy** — mandatory. The paragraph guards the shared working tree, an integrity
   surface. Check whether any reading lets a session treat a silent or unavailable channel as
   evidence it is alone. Otherwise discharge in one line with grounds. `/security-review` is
   discharged by grounds.

## Re-run obligation

Re-run, do not read. Lift invocations from `.githooks/pre-commit`, `tools/floor.py` and
`.github/workflows/ci.yml` rather than guessing.

- `git log -S 'two cues' --oneline` and `git log -S 'Ask, when a channel exists' --oneline`
- `python3 tools/stampscan.py --warn --root . .` for the stamped floor region
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
`docs/roadmap/160-doctrine-review-owed/560-rule-4-cold-pass-queued-three-cues.md`, the sibling
`docs/reviews/2026-10-16-1510-three-cues-cold.deferred.md`, the landing commit's message body
(the author's account; read subject, stat and diff only), and the commissioning item
`docs/roadmap/200-anti-slop-invariant-registry-promote-rec/100-r2-found-eleven-live-contradictions.md`.

Sweep with `python3 tools/coldsweep.py --root <your-worktree> --also-exclude
docs/roadmap/160-doctrine-review-owed/560-rule-4-cold-pass-queued-three-cues.md --also-exclude
docs/reviews/2026-10-16-1510-three-cues-cold.deferred.md --also-exclude
docs/roadmap/200-anti-slop-invariant-registry-promote-rec/100-r2-found-eleven-live-contradictions.md
<pattern>`; `--include-barred` only with disclosure in the verdict. Reading the delta is never
barred; the author's narrative of why, and the verdicts that recorded it, are.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list. Append your verdict
below a `---` divider in THIS file: provenance repeated (how you were spawned, your tier, what you
read), per-lens answers, findings with stable IDs (prefix `TC`: `TC1`, `TC2`, …) and severities
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

## Verdict — phase 1 (2026-10-17 UTC)

### Provenance, repeated

- **Reviewer:** a fresh `claude-fable-5-1` subagent (the principal-named review tier), spawned
  2026-10-17 by a Fable orchestrator that authored neither the delta nor this brief and holds
  the deferred sibling outside the reviewer's reach until these findings are committed. Neither
  the reviewer nor its orchestrator was started or instructed by the delta's author (the
  2026-10-03 queue run) or by the brief-writer. Rule 4's criterion is met; the orchestrator
  forms no finding and writes no severity. Every severity below is the reviewer's.
- **Worktree:** `/Users/mike/worktrees/atelier-review-1017`, branch `review-1017`, HEAD `b0f88bd`
  (carries `8acfff1`, verified with `merge-base --is-ancestor`). Read-only to the reviewer except
  this file. `git status` showed the orchestrator's context partition (deleted
  `2026-10-16-15*.deferred.md` siblings) and, part-way through, another pass's staged close-out;
  neither was touched.
- **Read:** the brief; `docs/method/CONCURRENCY.md` in full at HEAD; `docs/method/REVIEW.md`
  (rules 1–4, the re-run rule, the V1–V7 checklist); the landing commit's subject, `--stat` and
  diff on the delta path (message body unread); the trigger-region diffs of `295d94a`, `b0f202d`
  and the pre-flip text of `91ce0a7`; the mirror sites named in *Scope*; `tools/coldsweep.py`,
  `tools/board.py` (title rule), the hook, `ci.yml` and `tools/floor.py` for invocations.
- ⚠️ **Rule-2 exposure, disclosed.** The reviewer's first tree sweep was a hand-written
  `grep -rn` with a text-prefix exclusion (`^\./docs/sessions/` …) that assumed a `./` prefix
  `grep -r <dir>` does not emit — the exact defect `coldsweep.py` exists for, and the
  behaviour `REVIEW.md` rule 2 names. The sweep ran wide open. Single grep-hit lines were seen
  from: `docs/SESSIONS.md` (five index entries, among them the 2026-07-20 triple-pass summary
  naming CF1–CF7 by gist, and the two 2026-08-17 entries on the channel doctrine and its cold
  run, one of which states the gist of prior finding **CH2**); `docs/sessions/` (six files, one
  line each, including a 2026-10-03 ruling-round agenda row for CH2 with its proposed
  disposition); `docs/ROADMAP-DONE.md` (seven lines); the prior verdict
  `docs/reviews/2026-08-17-1000-channel-doctrine-cold.md` (seven lines, stating the gist of
  **CH2** — the ask cue overclaims — and **CH7** — "The two cues:" followed by three bullets,
  and "discoveries you make by accident" misdescribing the say-so cue); two unrelated prior
  verdicts (pathscan lines); the barred queue pointer's first lines (refs only); the
  commissioning item `200/100` (two lines: C5 as filed and as closed); and `280/030`'s CH2
  line. No file was opened; no body read beyond those lines. The correct sweep
  (`coldsweep.py`, exclusions as the brief lists) was then run and its exclusion set is in the
  ledger. **Consequence:** findings TC2 and TC4 below coincide in subject with CH2 and CH7 as
  exposed; each was re-derived from the HEAD text with its own probe, but the reviewer cannot
  claim they were formed unanchored, and says so at each. TC1, TC3, TC5 and TC6 touch nothing
  the exposure carried. The ruling state of CH2/CH7 is unknown to the reviewer and is phase-2
  work.
- `/security-review` discharged by grounds: the session's pending diff is other reviewers'
  drafts and a sibling pass's close-out, not this delta; the delta is two words of prose with
  no code surface. The security read was done by hand (lens 4).

### Lens 1 — approach and assumptions

Load-bearing assumptions named first: (a) the three bullets are peers — each is "a firing cue"
in the paragraph's sense, so one count and one set of predicates can describe them; (b) the
count was the only thing the 2026-08-17 landing (`b0f202d`) left stale when it added the third
bullet; (c) no mirror site carries the count, so the fix has one home. (c) holds (lens 3).
(a) does not hold cleanly: the third bullet is not wired to the substrate action (TC1), and its
"fact" sentence pulls against the paragraph's own silence rule (TC2). (b) is nearly true — the
same landing wrote a second count over the same backstop that the section's opening already
contradicts (TC3). So correcting the count was *most* of what the mismatch signalled, not all:
the mismatch was a sign the third bullet had been appended to a paragraph written for two
without the paragraph being re-read as a set.

### Lens 2 — correctness and quality

`df0820e` is correct as far as it goes: both "two" tokens on the delta path became "three", the
"both cheap" quantifier became "all cheap", and no other numeral in the paragraph needed the
edit ("the other two" inside the third bullet is right). The predicate table:

| Predicate (where stated) | Say so at open | Dirty-tree backstop | Ask, when a channel exists |
| --- | --- | --- | --- |
| cheap (para.) | ✅ one sentence from the principal | ✅ `git status` | ⚠️ conditional: needs a channel to exist and a reply to wait for; § The channel's own cost clause (TC5) |
| no locking machinery (para.) | ✅ | ✅ | ✅ § The channel: "It is not a lock" |
| a way to *discover* concurrency (para.) | ⚠️ you are told, not discovering — but a way to learn | ✅ | ✅ |
| silence licenses nothing (para.) | ✅ absent say-so ≠ alone; § The solo default agrees | ✅ the opening paragraph is this rule | ❌ "turns the flipped prior into a *fact*" admits the reverse reading (TC2) |
| ends in the substrate action (para.: "a firing cue") | ✅ "works in a worktree from its first action" | ✅ "moves itself to a worktree" | ❌ "enumerates its live peers … and asks" — no consequence clause (TC1) |
| "discoveries you make by accident" (3rd bullet) | ❌ a deliberate act by the principal (TC4) | ✅ | n/a (the claim is about the other two) |
| opening: "a blind spot in the cues below" | — | ✅ named there; also a third blind spot by line 81's own description (TC3) | — |

Reading the section's opening over three: it still reads true. Its stated reason for the flip
is the backstop's clean-tree blind spot, which the third cue does not remove, and "the cues
below" is count-free. It does not acknowledge that one cue can confirm the prior in the
positive direction — not a defect, noted for the counsel under TC2.

### Lens 3 — completeness and harvest

History (re-run, not read): the trigger and its two cues landed `91ce0a7`; the flipped prior and
the opening paragraph landed `295d94a` (2026-07-20); the third cue, § The channel and the
"two blind spots" paragraph landed together in `b0f202d` (2026-08-17); "two cues" ×2 stayed
until `df0820e` (2026-10-03). `git log -S` for "two cues" lists `b0f202d` nowhere, confirming the
landing that added the bullet never touched the count. What else that landing left: the second
stale count (TC3) and the unwired third bullet (TC1); it did re-stamp the floor region (verified
by `stampscan`, identical) and did point the floor's index rule at § The trigger (correct at
HEAD, `PROPAGATION.md:162`).

Mirror sweep at HEAD — **no mirror states a count**, so all agree with the delta:

| Site | Says | Count? | Agrees |
| --- | --- | --- | --- |
| `PROPAGATION.md` floor bullet (145–162) | clean tree ≠ alone; `git status` first; dirty ⇒ move; worktree by default; announce file set + answer peers | no | ✅ |
| `docs/build/templates/CLAUDE.md` 57–74 | stamped copy, byte-identical (`stampscan`) | no | ✅ |
| this repo's `CLAUDE.md` read-order 1 | clean tree ≠ alone; dirty ⇒ worktree; worktree by default | no (omits the ask cue — the repo has no channel) | ✅ |
| `skills/queue-run/SKILL.md` step 2 | `git status` first; dirty ⇒ worktree; clean tree ≠ alone | no | ✅ |
| `skills/session-onramp/SKILL.md` | names concurrency as a doctrine area only; no cue content | no | ✅ |
| `docs/method/GLOSSARY.md` | no entry for cue, trigger, flipped prior or channel | no | ✅ (TC5 note) |
| § The channel, *Hello* class | "enumerate its live peers and ask, rather than inferring solitude from a clean tree" | no | ⚠️ same reverse reading as TC2 |
| `CHANGELOG.md:2046` | "the cues are discovery-only, silence licenses nothing (CF2)" | no | ✅ |

### Lens 4 — security and privacy

The guarded surface is the shared uncommitted tree. One reading does let a session treat a
silent or empty channel as evidence it is alone: the third bullet's "the only cue that turns the
flipped prior into a *fact*" plus § The channel's "rather than inferring solitude from a clean
tree" read together as "enumerate peers; an empty list is the checked fact". § The solo default
closes it two sections away ("an affirmative statement or record, never an absence"), but the
cue's own sentence does not, and a reader at § The trigger need never reach it (TC2). An
*unavailable* channel is safe: the bullet is conditioned on "where sessions can message each
other", and the paragraph's silence rule covers the rest. No secret, identity or personal
detail is on the delta path. `/security-review` discharged by grounds (provenance).

### Findings

**TC1 — MODERATE — the third cue is not wired to the substrate action.** The paragraph
defines the set by function: "The substrate rule still needs a firing cue". The first two
bullets each end in the action — "works in a worktree from its first action", "moves itself
to a worktree". The third ends in knowledge: "enumerates its live peers at open and asks
(§ The channel)", and § The channel's *Hello* class adds no consequence either. The delta's
count now vouches for the three as peers ("there are three — all cheap") while the third is a
cue in a weaker sense than the paragraph's own. *Counsel:* one clause on the bullet — a peer's
answer that names this repo is the dirty-tree case without the dirt: move to a worktree, and
announce the file set as § Claiming work already requires.

**TC2 — MODERATE — "turns the flipped prior into a *fact*" admits a silent channel as
evidence of solitude.** (Coincides in subject with prior finding CH2 as exposed; re-derived
from HEAD text — see provenance.) The paragraph says "their silence licenses nothing"; the
third bullet says the ask is "the only cue that turns the flipped prior into a *fact* rather
than a posture", and § The channel says it lets a session "enumerate its live peers and ask,
rather than inferring solitude from a clean tree". The fact runs one way only — a peer who
answers proves company; an empty enumeration or no reply is an absence, which § The solo
default says never counts. The bullet does not say which way, and it sits where a session
decides whether to take a worktree. Security lens finding (the tree is the integrity surface).
*Counsel:* "turns the flipped prior into a fact **when a peer answers**; no answer is silence
and licenses nothing" — one clause, and the § The channel *Hello* sentence carries the same.

**TC3 — minor — "The backstop has two blind spots" is a second stale count in the same
section.** The opening paragraph names a blind spot of the dirty-tree backstop (a disciplined
peer leaves a clean tree between commits). Line 81, written in `b0f202d`, says the backstop has
*two* blind spots, scoped as "both bite in the shared primary checkout" and "neither shows in
`git status` as anything that reads as 'stop'". The opening's blind spot meets both halves of
that description. The two at line 81 are hazards present without a signal; the opening's is an
absence over time — different in kind, which is why this is minor and not the C5 class
restated — but a reader counting the section's blind spots gets three, and the delta's fix was
count-only. *Counsel:* "two **more** blind spots" or "two blind spots the opening paragraph
does not cover".

**TC4 — minor — "the other two are discoveries you make by accident" misdescribes the say-so
cue.** (Coincides in subject with prior finding CH7 as exposed; re-derived — see provenance.)
Say-so at open is a deliberate act by the principal, told to the session; nothing accidental
occurs. The sentence is true of the dirty-tree backstop alone. *Counsel:* "the other two reach
you by being told or by stumbling on the evidence".

**TC5 — note — "all cheap" is conditional for the third cue, and the vocabulary has no
glossary home.** Asking costs a channel that may not exist and a wait for replies, and
§ The channel's cost clause records four rounds of which two corrected the first two. The claim
is defensible for the act of asking; it is the one cue with a cost paragraph of its own. Also
`GLOSSARY.md` (a seed, 2026-07-23) has no entry for cue, trigger, flipped prior or channel;
no action owed by this delta.

**TC6 — note — the landing commit's generated index line truncates the pointer's title
mid-parenthesis.** `docs/ROADMAP.md:278` reads "… the concurrency cue count (200/100" because
`board.py` cuts titles at `TITLE_MAX = 70` on a word boundary; eleven other index lines show the
same shape. Standing board behaviour, not the delta's defect; recorded because the hunk is in
the delta's `--stat`.

**Overall: PASS-WITH-FINDINGS · 0 MAJOR · 2 MODERATE · 2 minor · 2 note.**

The two-word correction is right and complete on its own terms. The findings are about the
paragraph the correction now vouches for: a set of three described with predicates written for
two, one member of which is not wired to the action the set exists to fire.

### Standing checklist V1–V7

- V1 — "the only cue that turns the flipped prior into a *fact*" is stronger than its evidence
  (TC2). Nothing else in the delta claims more than it shows.
- V2 — every re-runnable claim in scope re-run (ledger below); the commit body's and the
  commissioning item's accounts are barred and were not relied on.
- V3 — swept to every mirror site named and to `CHANGELOG.md`; none carries the count; the
  stamped copy verified identical.
- V4 — the cue list has one home; the floor bullet is a stamped compression that points up.
  Discharged.
- V5 — three internal tensions recorded: TC2 (fact vs silence), TC3 (two vs three blind
  spots), TC4 (accident vs say-so).
- V6 — lens 4 run by hand; `/security-review` discharged by grounds.
- V7 — provenance in the brief (§ Spawn provenance) and repeated above, exposure included.

### Re-run ledger

| Command (from the worktree root) | Result |
| --- | --- |
| `git merge-base --is-ancestor 8acfff1 HEAD` | true; HEAD `b0f88bd` |
| `git show --stat df0820e` + diff on `docs/method/CONCURRENCY.md` | 4 files, +16/−3; two hunks on the delta path, as described |
| `git log -S 'two cues' --oneline` | `88f9925`, `df0820e`, `f88bace`, `b7e0da5`, `9991ad3`, `295d94a` — `b0f202d` absent |
| `git log -S 'Ask, when a channel exists' --oneline` | `88f9925`, `b0f202d` |
| `git log -S 'three cues'` / `-S 'both cheap'` / `-S 'blind spot in the cues'` / `-S 'discoveries you make by accident'` | `df0820e`+`88f9925` / `df0820e`+`91ce0a7` / `295d94a` / `b0f202d` |
| `python3 tools/coldsweep.py --root <wt> --also-exclude <pointer> --also-exclude <sibling> --also-exclude <200/100> -i 'cues'` | exit 0; 10 hits over 641 files; 396 excluded as rule-2 barred (`docs/SESSIONS.md`, `docs/sessions`, `docs/ROADMAP-DONE.md`, `docs/reviews`, plus the three `--also-exclude` paths) |
| `nice -n 10 python3 tools/stampscan.py --warn --root . .` | exit 0; 1 stamped block verified, `docs/build/templates/CLAUDE.md:18` identical to canonical `floor` (93 lines) |
| `nice -n 10 python3 tools/floor.py --plane ci --root .` | exit 0; all enforced checks green; advisories: secretscan 23 low-variety-entropy (standing), pathscan 2 missing-path (warn-only, neither on the delta path) |
| `nice -n 10 python3 tools/floor.py --plane hook --root .` | exit 0; all green (index held a sibling pass's staged close-out, content unread) |
| `grep -rlE '\bTC[0-9]\b' docs/reviews docs/roadmap` (filenames only) | no other file; prefix free |

Not run: the Python suite and the node suite — the brief's re-run list does not name them and
the delta is prose; machine load averaged 8–11 throughout.

### Follow-up checklist

- [ ] TC1 — the principal rules whether the third bullet gains its consequence clause.
- [ ] TC2 — the principal rules on the one-way-fact clause here and in § The channel *Hello*;
      phase 2 checks CH2's ruling state before anything is proposed twice.
- [ ] TC3 — the principal rules on the blind-spot count wording.
- [ ] TC4 — the principal rules on the "by accident" wording; phase 2 checks CH7's state.
- [ ] TC5 / TC6 — notes; no action owed by this delta. TC6 is the board's, if anyone's.
- [ ] Process — this reviewer's wide sweep was a rule-2 breach of the kind `coldsweep.py`
      was built to make unnecessary; it happened because the sweep was run by hand *before*
      the brief's sweep instruction was reached. Phase 2 and the orchestrator weigh whether
      TC2/TC4 stand as independent; the reviewer's own view is that they stand on their
      probes but not on their independence.

### Reconcile

Phase 1 committed at `9e45243`; the sibling was received from the orchestrator as text after
that commit (2026-10-17 UTC). Opened at reconcile, and nothing else: the landing commit's message
body; the intent record `docs/sessions/2026-10-03-0144-queue-run-handups-and-tool-defects.md`
(its `200/040` and close sections); the commissioning item `200/100` (C5 as filed and closed);
the two prior verdicts the sibling names, read for their cue findings and decision state; the
pointer `280/030`; the 2026-10-03 ruling inventory's CH rows. Phase-1 text above is unrevised.

**Against the seeded questions.**

- *Q1 (predicates not re-checked; "all cheap" over a channel; "by accident" vs say-so).*
  Anticipated TC4 (the say-so misdescription) and TC5 (cheapness conditional). Both formed in
  phase 1; the predicate table answers the question cue by cue. Nothing changes.
- *Q2 (the third cue asks but does not say what to do with the answer — cue or fact-finding
  step?).* Anticipated TC1 exactly. Phase-1 severity stands at MODERATE; the sibling's framing
  ("belongs beside the cues") is one of two shapes the counsel under TC1 allows for, and the
  choice is the principal's.
- *Q3 (the opening written for two — does it describe three?).* Answered in lens 2: it still
  reads true, being count-free and grounded in the backstop's blind spot. The adjacent count it
  led the reviewer to is TC3. Nothing changes.

**Against the intent record and the commissioning item.** The landing commit's body says what
the diff shows and no more: two "two cues" over three bullets, the third having come with
§ The channel. `200/100` C5 is filed as "internal" with file:line evidence and is closed with
the same two-word description. The intent record carries no evaluative account of C5 beyond
"each fixed separately with its own pass", and records the principal's "fix the contradictions
one by one" as an answer, not a ruling. The brief's account of the work is accurate; nothing in
the author's narrative was relied on in phase 1 and nothing in it moves a severity.

**Against the two prior verdicts — the finding this reconcile forms.**

- `2026-07-20-1355-concurrency-flip-cold.md`: CF2 `[fixed]` wrote "their silence licenses
  nothing" into the paragraph so that cue-silence could never license relaxing; CF6 `[fixed]`
  dropped "(primary)" from the say-so cue. TC2 is the CF2 principle re-opened by the third
  bullet's "fact" sentence — the same observation the channel verdict made at its reconcile.
- `2026-08-17-1000-channel-doctrine-cold.md`: **CH2** (MODERATE) is TC2 in substance, with
  the same repro lines and the same counsel; **CH7** (minor) is two findings in one — the
  "two cues" count over three bullets, *and* the "by accident" misdescription — of which the
  first half is what `df0820e` fixed and the second half is TC4. Decision state at HEAD, read
  from `280/030` and the 2026-10-03 ruling inventory: the channel cycle is closed at 0 MAJOR
  and **CH1–CH16 await the principal's ruling round**; CH2 sits in the inventory as unruled
  with no overtaking change; CH7 is listed as open wording. So TC2 and TC4 are not new: they
  are open findings re-found, and the exposure disclosed in the provenance is why the reviewer
  cannot claim to have re-found them cold. They stand on their probes; their severities are
  unchanged; the principal should rule them *once*, under whichever ID the ruling round reaches
  first.

**TC7 — minor — formed at reconcile — the delta discharged half of an open finding without
citing it, and the record still shows that half open.** CH7 named the "two cues" count on
2026-08-17; it sat unapplied for 47 days until R2's survey re-found the same defect as C5 and
`df0820e` fixed it, with neither the commit body, the commissioning item nor the 2026-10-03
run's record mentioning CH7. At HEAD the channel pointer `280/030` still lists CH7 among the
open wording findings, and the verdict file carries no `[fixed]` against it. Two consequences:
the ruling round will present a count defect that no longer exists, and the record cannot show
that the open-verdict route failed to deliver a fix the survey route then delivered — which is
the datum § *When a rule keeps breaking* would want. *Counsel:* a one-line `[fixed: df0820e —
count half only]` note against CH7 at the ruling round, and the same cross-check (grep the
finding IDs on the delta path before filing) when `200/100`'s remaining fixes are closed, since
C1–C11 were surveyed over surfaces that carry open verdicts.

**Overlap with sibling passes of this batch.** The worktree-venv pass (§ *The substrate*) and
the harvest pass (the closing-litany bullet) closed on `main` at `07c62ea` and `825880b`; both
are on `docs/method/CONCURRENCY.md` but neither touches § *The trigger*, and neither verdict was
opened. No sequencing conflict with this pass's findings.

**Overall, restated: PASS-WITH-FINDINGS · 0 MAJOR · 2 MODERATE · 3 minor · 2 note** (TC7
added at reconcile; no phase-1 severity amended).

## Deferred material — folded in at reconcile

# Sibling to the three-cues cold pass — held under rule 1's split

Sibling of `docs/reviews/2026-10-16-1510-three-cues-cold.md`, held under
`docs/method/REVIEW.md` rule 1's split. **Open only after the phase-1 findings in the brief are
committed.** Written 2026-10-16 UTC by the Opus brief-writer named in the brief's provenance; it
forms no finding. Fold this file in below the reconcile and delete it at phase 2.

## Intent and commissioning records

- Intent record: `docs/sessions/2026-10-03-0144-queue-run-handups-and-tool-defects.md` —
  **not opened by the brief-writer**.
- Commissioning item: `200/100` C5, in
  `docs/roadmap/200-anti-slop-invariant-registry-promote-rec/100-r2-found-eleven-live-contradictions.md`
  — **not opened by the brief-writer**.
- The landing commit's message body (read by the brief-writer): it says the section said "two
  cues" twice over a list of three, the third having arrived with § *The channel* without the
  count being updated.

## Prior verdicts on these surfaces (named by filename grep, not opened, not exhaustive)

- `docs/reviews/2026-07-20-1355-concurrency-flip-cold.md`
- `docs/reviews/2026-08-17-1000-channel-doctrine-cold.md` — by its name alone, possibly the pass
  on the channel doctrine that brought the third cue (unverified; not opened)

## The pointer's own lens hints

None. The pointer is refs-only; its last sub-bullet is the brief-writer's orchestrator's claim.

## Overlap with sibling passes of this batch

`docs/method/CONCURRENCY.md` is also the subject of the worktree-venv pass (§ *The substrate*,
a few lines above) and the harvest pass (the closing-litany bullet). Sequence them if one runner
takes several.

## Seeded questions (the brief-writer's suspicions, a floor not a fence)

1. The count was fixed, but the predicates were not re-checked: "all cheap, no locking
   machinery" now covers a messaging channel, and the third cue says "the other two are
   discoveries you make by accident" when one of them is the principal saying so at open.
2. The third cue enumerates peers and asks. It does not say what to do with the answer. Is it a
   firing cue for the substrate rule, or a fact-finding step that belongs beside the cues?
3. The section's opening names "a blind spot in the cues below" and describes only the
   dirty-tree cue's blind spot. Written for two, does it still describe three?
