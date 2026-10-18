# Cold pass — agreement is not corroboration, minted in EVIDENCE

**Pass type:** doctrine cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at selection by
whoever takes this pass.
**Status:** BRIEF ONLY — the review has NOT run. Written 2026-10-17 UTC by an Opus brief-writer;
the pass waits for a further cold Fable session that neither the delta's author nor this
brief-writer (nor its orchestrator) started or instructed; tier checked at selection (rule 4).
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/780-rule-4-cold-pass-queued-agreement-is-not-corroboration.md`.
**Why it earns a review:** it adds a rule to the evidence ladder every session climbs — what
counts as the *independent corroboration* rung — and promotes it to doctrine under the >2
promotion rule, so every repo that inherits `EVIDENCE.md` inherits the new test.

## Spawn provenance

- **Author of the work under review:** the 2026-10-16 queue run whose intent record is the
  session file dated 2026-10-16 07:03 UTC that the pointer names (not opened by the
  brief-writer). The landing commit's trailer names an Opus model; the run's orchestrator wrote
  this delta itself, not through a worker.
- **Who wrote this brief:** an Opus subagent (`claude-opus-5-5`) dispatched on 2026-10-17 by the
  Mike-opened Fable review session working in the worktree `atelier-review-1017`, on Mike's
  2026-10-16 answer that a fresh Opus session writes these briefs. Neither it nor its
  orchestrator authored the delta or was started or instructed by its author. **Off-tier for
  review, disclosed: it forms no finding and writes no severity**, and stops after this brief and
  its sibling.
- **Who takes the review:** a further cold Fable session, not yet started, passing rule 4's
  criterion. If it runs as reviewer-plus-orchestrator, the off-tier conditions of rule 4 apply and
  are disclosed in the claim, the pointer and the verdict. The reviewer repeats its own provenance
  in the verdict.
- ⚠️ **Brief-writer's exposure, disclosed** (rule-2 material met before writing): the four queue
  pointers it was assigned (160/780–810; refs-only, no claim line yet) and, as a shape example,
  the 160/500 pointer with its claim line; the delta lists of eight neighbouring pointers (160/700,
  720, 730, 760, 820, 830, 850, 860), read to find overlaps; the landing commit's subject,
  `--stat`, diff and **full message body** (the author's account); `docs/method/REVIEW.md` rules
  1–4; three user-local templates — the ask halves of the 2026-10-16 expected-toolbox and
  scanner-rule-gates briefs, and the whole expected-toolbox sibling, seeded questions included
  (another pass's framing, on other surfaces); HEAD text of the delta and of the passages named in
  *Scope*; one or two grep-hit lines from the commissioning item and from `115/060`; filename-level
  greps of `docs/reviews/` (no file there opened); and its harness-loaded memory index and
  instruction files. It did not open the intent record, `docs/SESSIONS.md`, `docs/sessions/`,
  `docs/ROADMAP-DONE.md` or any file under `docs/reviews/`. Its orchestrator passed it an
  instruction set (pointers, templates, staging rules, prefixes already taken) and no evaluative
  content about the delta; what the orchestrator read is its own to disclose in its claim.
  Everything evaluative the brief-writer formed is in the sibling.

## What the work is

Landing commit (diff it on the delta path; review the path at HEAD, `8acfff1` or later):

- `b572594` (2026-10-16 07:16 UTC) — method: mint "agreement is not corroboration" in EVIDENCE
  (200/090)

Delta path (the pointer's own scope): `docs/method/EVIDENCE.md` §13, the one paragraph the commit
adds, headed **A second voice is not a second angle unless it opened the source** (21 added
lines; at HEAD it sits between the ladder's closing paragraph and *Handing the question to the
principal*). No later commit touches `EVIDENCE.md`; confirm that.

The commit also touched board items, the session index, the intent record and another item's
held draft; those are not the delta.

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs and live behaviour. The
lenses organise it; they do not bound it. Non-goals are the only narrowing and are themselves
reviewable.

Probe, at least:

- **What the rung now means.** Read §13's ladder, its *independent corroboration* rung and §4
  ("its own corroboration") against the new paragraph. Build a case table: a second party that
  opened the *same* artefact as the first; one that opened a different artefact derived from the
  first; a tool's output; the principal agreeing; a cold reviewer agreeing with a prior verdict;
  a subagent re-reading text its parent quoted to it; a party that re-ran a probe rather than
  opening a file. For each, what does the paragraph say, and does a reader reach one answer?
- **The grounding, re-driven.** The paragraph cites three instances and where each is kept:
  `CONCURRENCY.md` § *Re-run, don't reason*, the board item `115/060`, and `CONCURRENCY.md`
  § *Orchestrated queue runs*. Open each cited surface and say whether it records what the
  paragraph says it records. (The fourth citation, `200/090`, is the commissioning item, barred
  until phase 2 — check it at reconcile.)
- **The promotion rule, as written.** `PROPAGATION.md` § *When a rule keeps breaking* states the
  >2 promotion rule. Does this minting meet that rule as the rule is worded, and is the rung it
  chose (a doctrine paragraph) the one that section's ladder would pick?
- **One fact, one home.** `CONCURRENCY.md` states the same rule at two places (its *Re-run,
  don't reason* bullets and its *Orchestrated queue runs* account). Which is now the home, does
  each copy point to it, and do the copies still agree in wording and reach (`EVIDENCE` §9,
  `PROPAGATION.md` § *One statement, stamped copies*)?
- **The sibling rule left behind.** The paragraph names a second rule and declines to promote it.
  Is that statement accurate, and is a doctrine paragraph the place for it?
- **Where it reaches.** Which surfaces children and the plugin's skills read restate the evidence
  ladder or its corroboration rung, and do any now disagree?

**Non-goals:** the decision to promote this rule at all (the >2 rule's threshold itself). Whether
the minting meets that rule, the wording, its placement and its consistency are in scope.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself first. Ask whether
   "which artefact did it open" is the right test for independence, and whether a rule about who
   opened what can be followed by a reader who cannot see the other party's reads.
2. **Correctness & quality.** Diff `b572594` on `docs/method/EVIDENCE.md`. Check every
   cross-reference in the new paragraph resolves to a passage that says what is claimed. Record
   the case table from *Scope*.
3. **Completeness / harvest.** Every surface that states the corroboration rung or the rule:
   `EVIDENCE.md` §§2, 4, 13; the two `CONCURRENCY.md` sites; `REVIEW.md`'s independence rules;
   `README.md` and `docs/method/README.md` summaries; the plugin's skills; `CHANGELOG.md`. Is a
   changelog entry or a stamp owed?
4. **Security & privacy** — mandatory. The paragraph cites real episodes in a public repo: check
   it names no private repo, person, host or account beyond the recorded exceptions, and that the
   cited board items carry nothing that should not be public. Describe, never quote, anything
   sensitive. `/security-review` is discharged by grounds (a landed prose delta).

## Re-run obligation

Re-run, do not read. Lift invocations from `.githooks/pre-commit`, `tools/floor.py` and
`.github/workflows/ci.yml` rather than guessing.

- `python3 tools/linkscan.py --root . .` and `python3 tools/pathscan.py --warn --root . docs` —
  the paragraph's links and backtick paths, exit codes read explicitly
- `python3 tools/leakscan.py --root . .`, exit code read explicitly
- `python3 tools/wrapscan.py --root . docs` and `python3 tools/spellscan.py --root . docs`
- `git log --oneline b572594..HEAD -- docs/method/EVIDENCE.md` — empty, or each commit named
- the floor on both planes at HEAD (`python3 tools/floor.py --plane ci --root .`, and
  `--plane hook`)

## House rules for this run

- Name your own review worktree in the verdict; it is read-only to you except for THIS file. Other
  sessions may be live on this machine: touch nothing outside your worktree and your scratch
  clone. Never open another `docs/reviews/2026-10-16-*` or `docs/reviews/2026-10-17-*` file — it
  is another pass's framing.
- No git command that writes in the worktree, beyond committing this one file at the end of each
  phase (or handing it to your orchestrator to commit). Read-only git is fine. Older checkouts and
  scratch trees go in a private clone under your session scratchpad, named by your prefix.
- One heavy process at a time: the full Python suite at most once, in the foreground; never point
  a scanner at another repo on the machine.
- `/security-review` reads the session's pending diff, not this delta. Discharge it by grounds and
  do the code-altitude read by hand against the OWASP catalogue, or keep the tree clean when you
  spawn it — never with this brief or its sibling dirty.
- Absolute ISO 8601 dates from `date -u`; prose wrapped at ≤ 100 columns; NZ English. Never quote
  a secret, a placeholder token, an email address or a personal detail — this repo is PUBLIC.
- Review deep, not fast: a finding needs a probe or a re-driven claim behind it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the deferred material lives in the sibling .deferred.md under the rule-1 split, opened only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`, every
prior verdict in `docs/reviews/`, the queue pointer
`docs/roadmap/160-doctrine-review-owed/780-rule-4-cold-pass-queued-agreement-is-not-corroboration.md`,
the sibling `docs/reviews/2026-10-17-0930-agreement-not-corroboration-cold.deferred.md`, the
landing commit's message body (the author's account; read subject, stat and diff only), and the
commissioning item:

- `docs/roadmap/200-anti-slop-invariant-registry-promote-rec/090-two-corroboration-failures-worth-minting-from.md`

Sweep with `python3 tools/coldsweep.py --root <your-worktree> --also-exclude
docs/roadmap/160-doctrine-review-owed/780-rule-4-cold-pass-queued-agreement-is-not-corroboration.md
--also-exclude docs/reviews/2026-10-17-0930-agreement-not-corroboration-cold.deferred.md
--also-exclude
docs/roadmap/200-anti-slop-invariant-registry-promote-rec/090-two-corroboration-failures-worth-minting-from.md
<pattern>`; `--include-barred` only with disclosure in the verdict. Reading the delta is never
barred; the author's narrative of why, and the verdicts that recorded it, are.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list. Append your verdict
below a `---` divider in THIS file: provenance repeated (how you were spawned, your tier, what you
read), per-lens answers, findings with stable IDs (prefix `EC`: `EC1`, `EC2`, …) and severities
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

# Verdict — phase 1 (prefix `EC`)

**Reviewer tier:** Fable 5.1 (`claude-fable-5-1`), checked at selection: it is the tier the
principal named (ruling 2026-08-04), so rule 4's stop clause did not fire. Phase 1 begun
2026-10-17 23:38 UTC; completion time is the last line of the re-run ledger.

## Provenance, repeated

- **Spawn.** This reviewer was spawned by a Mike-opened Claude Code **cloud** session running
  `claude-fable-5-1` as orchestrator (it opened on `claude-opus-5` and Mike switched it to Fable
  before any claim or pass). That session authored none of the delta or the brief and was not
  started or instructed by their authors. The orchestrator forms no finding and writes no
  severity; it holds the `.deferred.md` sibling outside the checkout at a path not given to me,
  commits this phase-1 file before releasing the sibling, and received one operational note from
  Mike's watching session (model, queue scope, container facts, merge instruction — no evaluative
  content about any delta). The queue pointer's claim line discloses the same shape; I have not
  opened the pointer. The brief's own provenance (an Opus brief-writer, off-tier, forming no
  finding) stands as written above and is not contradicted by anything I read.
- **Container.** One checkout at `/home/user/atelier`, branch `claude/review-work-briefs-adj6ad`,
  HEAD `0aff4d8`; the orchestrator states HEAD equals `origin/main` and I could not re-drive that
  (no network git here) — *relayed*. No worktrees, no sibling repos, no estate root, no
  `~/.claude/`, no `gh`, no GitHub API. The clone is **shallow**: `.git/shallow` names `c824287`
  (committed 2026-10-17 09:40 UTC) as the graft root; 52 commits are reachable from HEAD; the
  landing commit `b572594` is present as an object with its parent, but is not an ancestor of
  HEAD in the local graph. This bears on one re-run (EC9). Scratch directory
  `/home/user/scratch/EC/` was created; nothing was written to it in phase 1 — every probe ran
  read-only in place. No git command that writes was run; no file other than this one was edited.
- **Read, in order.** `docs/method/REVIEW.md`; this brief; `docs/method/00-APEX.md` once; the
  delta by `git show --stat --format=%s b572594` and `git diff b572594^ b572594 --
  docs/method/EVIDENCE.md` (subject, stat and diff only — the body is unread); `EVIDENCE.md`,
  `CONCURRENCY.md` and `PROPAGATION.md` whole at HEAD; `docs/method/README.md`; board items
  `115/060` whole and `020/390` lines 30–74; `.githooks/pre-commit`; `.github/workflows/ci.yml`;
  `.atelier-floor.json`; `tools/datescan.py` lines 239–268; `CHANGELOG.md` head plus greps;
  `README.md`, `skills/*/SKILL.md` and `commands/*.md` by grep.
- **Exposure, disclosed.** `tools/coldsweep.py` with the brief's three `--also-exclude` paths and
  never `--include-barred`; its hits included two index lines of `docs/ROADMAP.md` that print the
  *titles* of the barred pointer (160/780) and the barred commissioning item (200/090) — title
  words only, neither file opened. `git log --graph -12` printed other passes' commit *subjects*
  (TB, PF) — subjects only; no verdict file opened. `git show --stat --format=%s c824287` printed
  a whole-tree stat (the graft root) including file names under `docs/reviews/` and
  `docs/sessions/` — names only. Nothing under `docs/reviews/2026-10-16-*`, `2026-10-17-*`
  (other than this file), `drafts/`, `withdrawn/`, `docs/SESSIONS.md`, `docs/sessions/`,
  `docs/ROADMAP-DONE.md`, the queue pointer or `200/090` was opened. The sibling was not looked
  for.

## Lens 1 — Approach & assumptions

Load-bearing assumptions, named by me before reading the brief's probes as questions:

- **A.** The defect in the three episodes is in the *agreement* — a second party endorsing a
  claim it never checked — rather than in the first party's claim being unsourced.
- **B.** "Which artefact did it open" is a test the receiving party can apply.
- **C.** `EVIDENCE.md` §13 is the point of use, where a session grades an agreement.
- **D.** Three recorded instances of one pattern exist, and counting them satisfies the >2 rule.
- **E.** A doctrine paragraph is the right remedy, as against a mechanism or a record field.

Attacked:

- **A** holds as far as it goes. In all three episodes the *first* claim already sat at the
  recall/inference rung — a reading of a doctrine clause reasoned from a summary, a coined
  paraphrase, a three-signal inference — and §2 already tiers an unsourced agreement as
  `ai-inference`, §4 already says one unconfirmed source is a lead. The paragraph's novelty is
  operational (what to *ask*), not epistemic. The operational part is where the defect is (EC1).
- **B** is followable as "ask" and not closable by the asker: the answer is a peer's claim, which
  `CONCURRENCY.md § Re-run, don't reason` calls a hypothesis, and a past record cannot be asked.
  The checkable half is the asserter's, in §1's durable register; the paragraph does not reach
  for it (EC3).
- **C** is reasonable — the rung's definition is where a reader decides whether an agreement
  counts — but a third statement placed there without being made the home is the V4 defect the
  house names (EC2).
- **D**: episodes 1 and 3 are two parties agreeing with neither having opened the source; episode
  2 is one record citing another record's coinage. The paragraph's closing sentence bridges them
  by definition ("repetition is the cheapest agreement"); the heading is framed for the narrower
  class (EC8).
- **E**: `PROPAGATION.md § When a rule keeps breaking` requires the chosen rung to be tested
  against the recorded occurrences. The 2026-09-20 recurrence happened in a session editing the
  very file that already carried the rule, so findability was not the failure, and a third
  statement elsewhere would not have prevented it by the section's own criterion. The test is not
  on the record (EC4).

The brief's framing, attacked: its non-goal (the >2 threshold itself) is a legitimate narrowing —
it fences the threshold, not the counting or the placement, both of which it keeps in scope. Its
"No later commit touches `EVIDENCE.md`; confirm that" is true of the file's *content* and false of
the prescribed *command* in this container (EC9). Its account of what the work is — one paragraph
of 21 lines at the stated position — is accurate (diff reproduced).

## Lens 2 — Correctness & quality

**Diff reproduced.** `git diff b572594^ b572594 -- docs/method/EVIDENCE.md`: one hunk, 21 added
lines (20 of text, one blank), inserted after the ladder's closing paragraph and before *Handing
the question to the principal*; identical at HEAD (`git diff --stat b572594 HEAD -- docs/method/
EVIDENCE.md` is empty). Lines 191–210 at HEAD; the longest line is 79 columns.

**Cross-references, each opened:**

- `PROPAGATION.md § When a rule keeps breaking` — resolves; states the >2 promotion rule ("act at
  the third instance") at line 811. Holds.
- `CONCURRENCY.md § Re-run, don't reason` — resolves. Records the *class* (lines 542–544: the
  bolded bullet, "two-of-three agreement … one unread claim with an echo") and that a party
  "re-read a doctrine passage and withdrew its own assertion". It does **not** record the
  narrative the paragraph gives — a child *mistranslated* a doctrine clause; a *third* read the
  doctrine and found *both* wrong. That narrative's primary source is the kept transcript under
  `docs/sessions/` (the section's *Bearing* links it) and/or `200/090` — both barred until
  phase 2. **Not re-driven in phase 1**; reconcile checks it (EC7).
- `115/060` — resolves; records exactly what the paragraph says: a coined paraphrase in quotation
  marks had become a citable source for a second board item (found by a 2026-08-09 cold pass;
  verified still live 2026-08-15). Holds.
- `CONCURRENCY.md § Orchestrated queue runs` — resolves; the ⚠️ provenance paragraph records
  the 2026-09-20 attribution, two sessions agreeing on it, and a transcript check "the next
  hour" falsifying it. Holds; `020/390` lines 40–56 corroborate in the same words ("neither
  had looked").
- `200/090` — barred; reconcile.

**The case table.** The paragraph carries two tests. **T-lead** (sentences 1 and 3): did the
second party open *the source*? **T-count** (sentence 5, the one phrased as the counting rule):
did it open *something the first party did not*? For each of the brief's cases:

- *Opened the same artefact as the first* — T-lead: a second angle. T-count: not corroboration.
  **Diverge.**
- *Opened a different artefact derived from the first* (a generated index, a rendered copy) —
  T-lead: unclear whether a derivative is "the source". T-count: corroboration. **Diverge** — and
  a derivative shares the source's error by construction, which "an independent route to the
  fact" forbids.
- *A tool's output, the second party ran it* — both: counts ("the API answer"). One answer.
- *A tool's output, the second party read the first's paste of it* — T-lead: no. T-count: yes,
  because the paste or transcript is something the first party did not "open". **Diverge.**
- *The principal agreeing without opening* — both: no. One answer. (§13's *Handing the question
  to the principal* already keeps authority and evidence apart; nothing new is needed.)
- *A cold reviewer agreeing with a prior verdict after its own read of the same delta* — T-lead:
  a second angle. T-count: not corroboration. **Diverge** — and this is the independence
  `REVIEW.md` rule 2 is built to buy (the REACH case).
- *A subagent re-reading text its parent quoted to it* — T-lead: no. T-count: yes — "the
  transcript" is on the paragraph's own list of artefacts. **Diverge**, and T-count admits the
  paradigm echo.
- *A party that re-ran a probe rather than opening a file* — T-lead's verb "opened" does not
  literally cover a reproduction; the example list does. T-count: yes. One answer by example,
  not by rule.

Four of eight rows diverge and one is unclear. A reader does not reach one answer (EC1).

**Done vs stubbed.** The paragraph claims nothing beyond itself. "Grounded three times": two of
three re-driven against the cited surfaces in phase 1, the first's narrative deferred. "Has one
recorded instance" (the sibling rule): true on the unbarred tree — `coldsweep` finds the phrase
only at its CONCURRENCY home (line 545) and in this paragraph — but see EC6 on its form.

## Lens 3 — Completeness / harvest

Every surface that states the rung or the rule, at HEAD:

- `EVIDENCE.md` §2, §4, §13. §4's "its own corroboration" (one direct observation settles a
  reported fact) and §13's "primary + corroboration" for high stakes are in a pre-existing mild
  tension; the paragraph neither worsens nor resolves it, and does not cite §2 or §4 where either
  would anchor it.
- `CONCURRENCY.md` lines 542–544 and 816–817 — two bolded statements of the rule, differing in
  reach ("the second party never opened" / "neither party opened"); neither points at
  `EVIDENCE.md`; `EVIDENCE.md` cites both as grounding, which is not a pointer to a home (EC2).
- `REVIEW.md` — never uses the word; its independence model treats two independent reads of one
  delta as the independence worth buying, which T-count denies (under EC1).
- `README.md` — no mention of the ladder (grep). `docs/method/README.md` — its `EVIDENCE.md`
  summary lists §§1–10 topics and no §13; pre-existing staleness, not this delta's.
- Plugin skills (`skills/*/SKILL.md`) and `commands/*.md` — zero hits for the rung, the rule,
  `EVIDENCE.md` or §13. Nothing disagrees; nothing to stamp.
- `PROPAGATION.md`'s floor block — does not carry the ladder; nothing owed there.
- `CHANGELOG.md` — no line for the minting, where house practice carries doctrine lines (EC5).

Duplicated or ignored: §2 + §4 already imply the rule; the paragraph's distinct value is the
operational test — the part with the defect.

## Lens 4 — Security & privacy

*Design altitude.* The paragraph names no repo, person, host, account or filesystem path beyond
two board-item refs and two method files; the three episodes are described by class ("a child's
sessions", "two sessions", "some escaped scratch files"). The cited surfaces: `115/060`
describes rather than quotes and names no child; `CONCURRENCY.md § Orchestrated queue runs`
names two generic `/tmp` filenames and a per-project scratch parent — pre-existing and already
public; the § *Re-run* bearing names the public child `faves`, public by its own record. Nothing
the paragraph adds should not be public. *Code altitude.* No code in the delta; the OWASP
catalogue has nothing to bite on prose — the one applicable class, sensitive-data exposure, is
checked by the hand read above and by `leakscan` (structural) clean at HEAD on the tree and on
the file. **`/security-review` not run — discharged by grounds:** it reads this session's pending
diff (this brief), its own exclusions bar markdown so its pass would be definitionally empty, and
aiming it at a dirty brief is the SL2 hazard REVIEW.md records. **Hook-plane leakscan with the
term list: not re-driven here (relayed)** — the container has no local term list and the hook
plane refused by design (115/350); the CI plane is the honest plane here and is clean.

## Findings

**EC1 — MAJOR — The paragraph states its test two ways, and they disagree on the paradigm
cases.** Sentences 1 and 3 test whether the second party *opened the source*; sentence 5 counts
corroboration only if it *opened something the first party did not*. Probe: the case table above
— four of eight rows diverge. Two rows carry the weight. (a) A second party that independently
opened the *same* artefact is "a second angle" by the lead and "not corroboration" by the count,
and that case is the independence `REVIEW.md` rule 2 exists to buy. (b) A subagent re-reading its
parent's quote, or a session reading a peer's pasted tool output, has opened "the transcript" —
on the paragraph's own list — which the first party did not open, so the counting sentence
admits the exact echo the paragraph exists to refuse. The sentence phrased as the rule is the one
that misfires. V5, inside a 21-line rule inherited by every child. *Counsel (labelled; the
decision is the principal's):* state the test in the ladder's own vocabulary — an agreeing party
contributes the rung *it* stands on, never the rung it agrees with; a party at recall, or at a
quote of the first party's claim, adds nothing; a party that opened the same primary is a second
fetch — strong against misreading, still one route; the corroboration rung is reached by a
*different* route, another artefact or a reproduction. One sentence resolves every row and keeps
the heading true.

**EC2 — MODERATE — Three originals and no home.** `CONCURRENCY.md` carries two bolded statements
of the rule (542–544; 816–817); the minting adds a third in `EVIDENCE.md` (191–198) and
touches neither CONCURRENCY site — `EVIDENCE.md` is the only method file in `b572594`'s stat.
None is stamped; none points at another as canonical; the three already differ in reach
(second party / neither party / a different artefact). `PROPAGATION.md § One statement, stamped
copies`: "Three independent statements of one rule is the defect"; `EVIDENCE.md` §9. V4 and V3.
*Counsel:* make §13 the home once EC1 is settled, and reduce the two CONCURRENCY statements to
the instance records they already are — both sit inside bearings — pointing up at §13, or stamp
them.

**EC3 — MODERATE — The duty sits on the receiver alone, and the receiver's question returns
testimony.** The operative verb is *ask*. A reader who cannot see the other party's reads can
ask; the answer is a peer's claim (a hypothesis, per `CONCURRENCY.md § Re-run, don't reason`),
and a past record cannot be asked. In all three grounding episodes the corrective act was not a
question put to the agreeing party but someone *opening the artefact*; none of the three records
a receiver asking and being answered. The checkable half is the asserter's — a claim of agreement
names the artefact it rests on, in the record (`EVIDENCE.md` §1's durable register, §12's
enforce-by-machine) — and the paragraph does not reach for §1, so what it adds is honour-system
on both sides. *Counsel:* one sentence of writer's duty pointing at §1; keep the receiver's rule
as the fallback when the record is silent — treat the agreement as absent and climb yourself,
which §13 already says.

**EC4 — MODERATE — The grounding note claims the ladder's authority for the count and skips its
test for the rung.** `PROPAGATION.md § When a rule keeps breaking` requires testing a rung against
the recorded occurrences before stopping on it (RL1) and says a wording change "reliably is not"
progress. Run the test the paragraph did not record: the rule was written into `CONCURRENCY.md`
on 2026-08-17; the third occurrence (2026-09-20) was produced by a session editing that file's
own § *Orchestrated queue runs* — findability was not what failed, so a third statement in
another file would not have prevented it. Rung 2 (a record field "artefact opened:", lintable as
absent) and rung 3 (make the artefact check the first step of an attribution, as the 2026-09-20
fix did for scratch paths) are not considered on the record. PROPAGATION gives the author a
defensible reading — promotion into doctrine is "a separate act" from climbing (RL3) — so the
finding is that the test was owed and not shown, not that promotion was wrong; the threshold is
the brief's non-goal. *Counsel:* record the rung test in `200/090`; if a paragraph is still the
pick, say why rungs 2 and 3 do not fit these three incidents.

**EC5 — minor — A CHANGELOG line is owed.** `PROPAGATION.md § The mechanism` point 1: the
CHANGELOG carries one line per doctrine change, and a child's drift check reads it. The minting
has none — no 2026-10-16 entry mentions corroboration or `200/090`; all seven 2026-10-16 entries
are tool changes. House practice does carry doctrine lines: `EVIDENCE.md` §15 (CHANGELOG line
140), the §13 ladder (2923), the 2026-08-23 scanner-delta sentence (353). Mitigated: `git log`
shows the subject plainly and point 1 names it as the other route. V3.

**EC6 — minor — A stored derived value, and a decision of record, inside doctrine.** "Has one
recorded instance" is a count that rots the moment a second instance is recorded — `EVIDENCE.md`
§8's own rule, broken inside `EVIDENCE.md`. The two closing sentences record a decision *not* to
promote a rule that lives in another file: a record-of-decision whose home is the commissioning
item or the session record, not §13. A reader of the ladder gains nothing from them. *Counsel:*
drop both sentences; reconcile will check whether `200/090` already holds the decision.

**EC7 — minor — Two citation imprecisions in the grounding.** (i) "the kept exchange in
`CONCURRENCY.md § Re-run, don't reason`": the exchange is kept under `docs/sessions/` (the
section's *Bearing* links it); CONCURRENCY holds the extraction, so a reader following the
citation finds a summary and one more hop. (ii) The first episode's narrative — a mistranslated
clause; a third read the doctrine and found both wrong — is not in the cited section, which
records the class and that one party re-read a passage and withdrew its assertion. **Not
re-driven in phase 1**; reconcile checks it against the transcript and `200/090`. Also: "a
child's sessions agreed that a child had mistranslated" reads as two children; if one is meant,
say so.

**EC8 — note — The second instance is of a neighbouring class.** Episodes 1 and 3 are two
parties agreeing with neither having opened the source. Episode 2 (`115/060`) is one record
citing another record's coinage as a quoted source — no second voice agreed; a claim was
repeated. The closing sentence bridges them by definition. The class that covers all three is
"a claim gains standing from a party that did not open the source", one level above the
heading's "second voice". This feeds EC1: name the class at that level and the heading, the
count and the three episodes line up.

**EC9 — note — The brief's confirm-step and prescribed re-run misfire in this container.** "No
later commit touches `EVIDENCE.md`; confirm that" and `git log --oneline b572594..HEAD --
docs/method/EVIDENCE.md — empty, or each commit named`: on this shallow clone the log names
`c824287`, the graft root, which "adds" every file — a false positive a reviewer could record as
a later touch. The honest confirmation is blob identity: `git diff --stat b572594 HEAD --
docs/method/EVIDENCE.md` is empty, so no commit between the landing and HEAD changed the file's
content. *Counsel for the brief template, not the delta:* prescribe the blob comparison, which is
depth-independent, or say what a shallow clone prints.

*Observed, out of scope, not a finding:* `pathscan` (warn-only) reports one pre-existing stale
path in `docs/decisions/2026-10-03-0641-the-exception-register.md` line 84 (`tools/exception.py`
does not exist). It is visible on every CI run and is not this delta's.

## Standing checklist V1–V7

- **V1** — "Grounded three times": two of three re-driven against the cited surfaces; the first's
  narrative deferred (EC7). "Minted at the third under the >2 rule": the count holds if episode 2
  is accepted as the same class (EC8). No other claim stronger than its evidence found.
- **V2** — ledger below; one prescribed re-run misfires here (EC9).
- **V3** — mirror sites swept: `CONCURRENCY.md` ×2 (EC2), `CHANGELOG.md` (EC5), skills, commands
  and both READMEs (nothing restates the rung).
- **V4** — EC2.
- **V5** — EC1 within the paragraph; the §4/§13 tension pre-exists and is not worsened;
  `REVIEW.md`'s independence model cuts against T-count (under EC1).
- **V6** — lens 4 above; `/security-review` discharged by grounds.
- **V7** — provenance stated in the brief and repeated above; both disclose the orchestrator
  arrangement.

## Overall

**PASS-WITH-FINDINGS — 1 MAJOR · 3 MODERATE · 3 minor · 2 note.** The rule is right in intent
and its three instances are recorded where the paragraph says; its operative sentence is not yet
one rule (EC1), and it was minted as a third original rather than a home (EC2). Rule 3: every
finding recorded, nothing applied; counsel is labelled.

## Re-run ledger

All commands run from `/home/user/atelier` at HEAD `0aff4d8`; exit codes read explicitly.

- `date -u` → `Sat Oct 17 23:38:00 UTC 2026` at open.
- `git status --short` → empty (clean). `git log --oneline -1` → `0aff4d8 review: claim the 12
  briefed rule-4 passes …` on `claude/review-work-briefs-adj6ad`.
- `git show --stat --format=%s b572594` → subject `method: mint "agreement is not corroboration"
  in EVIDENCE (200/090)`; 7 files, `docs/method/EVIDENCE.md | 21 ++++`; author date
  2026-10-16 07:16 UTC (`%aI`). Body not printed.
- `git diff b572594^ b572594 -- docs/method/EVIDENCE.md` → one hunk, 21 added lines (reproduced
  under lens 2).
- `git log --oneline b572594..HEAD -- docs/method/EVIDENCE.md` → **one line, `c824287`** — not
  empty. `git log --format='%h parents=[%p]' -1 c824287` → no parents; `.git/shallow` →
  `c824287`; `git rev-list --count HEAD` → 52; `git merge-base --is-ancestor b572594 HEAD` →
  **no**. So the listed commit is the shallow graft root, not a later edit (EC9).
- `git diff --stat b572594 HEAD -- docs/method/EVIDENCE.md` → **empty** (content identical).
  Also empty: `b572594` vs `c824287`, and `c824287` vs HEAD.
- `git merge-base --is-ancestor 8acfff1 HEAD` → yes (the brief's "8acfff1 or later" holds).
- `python3 tools/floor.py --list --plane ci --root .` and `--plane hook` → 16 checks each; plans
  identical.
- **`python3 tools/floor.py --plane ci --root .` → exit 0.** 11 enforced green; secretscan 🟡 23
  advisory (pre-existing, none in the delta); leakscan 🟡 structural-only (the plane does not pass
  `--require-terms`); pathscan warn-only 1 finding (pre-existing, `docs/decisions/2026-10-03-…`
  line 84); harvestscan, pointerscan, indexscan clean. **This is the plane I ran as the floor.**
- **`python3 tools/floor.py --plane hook --root .` → exit 1, BLOCKED by leakscan** — "--require-
  terms set but no local term list found … refusing to report it as a pass". Expected in this
  container (115/350); every other check on the hook plane green or as on CI.
- `python3 tools/linkscan.py --root . docs/method/EVIDENCE.md` → exit 0, clean.
- `python3 tools/pathscan.py --warn --root . docs/method/EVIDENCE.md` → exit 0, clean (1
  pre-existing allow-marker suppressed).
- `python3 tools/leakscan.py --root . docs/method/EVIDENCE.md` → exit 0, clean, structural only.
- `python3 tools/wrapscan.py --root . docs/method` → exit 0, clean (85-column budget; the
  paragraph's longest line is 79: `awk 'NR>=191 && NR<=210 {print length}'`).
- `python3 tools/spellscan.py --root . docs/method` → exit 0, clean.
- `python3 tools/datescan.py --root . docs/method/EVIDENCE.md` → exit 0, clean.
- `python3 tools/coldsweep.py --root . <three --also-exclude as the brief> -i '<pattern>'`, 645
  files swept, 409 excluded as barred, exit 0 each: `corroborat` → 45 hits (rule statements at
  `CONCURRENCY.md` 542, 816; `EVIDENCE.md` 177–196; the rest board items and `SECRETS.md` using
  the word in its ordinary sense); `symptom count` → 2 hits (`CONCURRENCY.md` 545, `EVIDENCE.md`
  209); `second angle` → 3 (all `EVIDENCE.md`); `unread claim|with an echo` → 2
  (`CONCURRENCY.md` 544, `EVIDENCE.md` 194); `>2 promotion` → 3 (`EVIDENCE.md` 200, 304;
  `PROPAGATION.md` 811).
- `grep -n -i -E 'corroborat|200/090|b572594|2026-10-16' CHANGELOG.md` → no entry for the
  minting; the three `corroborat` hits are 2026-07 lines. `grep -n 'EVIDENCE' CHANGELOG.md` → 13
  lines, including §15 (140) and §13 (2923).
- `grep -n -i -E 'corroborat|evidence ladder|EVIDENCE\.md|§13' skills/*/SKILL.md commands/*.md`
  → exit 1 (no hits). `grep -n -i -E 'EVIDENCE|ladder|corroborat' README.md` → one hit, the
  PRINCIPLES precedence ladder; nothing on EVIDENCE.
- **Not run, with grounds:** the full Python suite, `node --test instruments/*.test.js` and the
  `mandoc` lint — the delta is prose with no code surface any of them reaches, and the container's
  four CPUs are shared with up to five concurrent reviewers; `/security-review` — lens 4 above;
  hook-plane leakscan with terms, and any check needing another repo, the estate root or a live
  platform read — impossible in this container, relayed, never faked.
- `python3 tools/floor.py --plane ci --root .` re-run after this verdict was written → exit 0,
  same board as above; `python3 tools/reviewscan.py --root . docs/reviews` → exit 0, 182 briefs
  clean; `python3 tools/datescan.py --root . <this file>` → exit 0. `git status --short` → only
  this file modified.
- Phase 1 complete: `date -u` → `Sat Oct 17 23:52:45 UTC 2026` (2026-10-17 23:52 UTC).

## Follow-up checklist

- [ ] **EC1** — the principal rules on the test's wording; one sentence carries the rule.
- [ ] **EC2** — choose the home; reduce or stamp the two `CONCURRENCY.md` statements.
- [ ] **EC3** — writer-side duty, one sentence, pointing at §1.
- [ ] **EC4** — the rung test recorded in `200/090`.
- [ ] **EC5** — a CHANGELOG line.
- [ ] **EC6** — move the sibling-rule sentences to the record.
- [ ] **EC7** — citation precision; reconcile verifies the first episode's narrative.
- [ ] **EC8** — feeds EC1; no separate action.
- [ ] **EC9** — for the brief template, not the delta.
- [ ] **Phase 2** — open the sibling, `200/090`, the queue pointer, the landing commit's body and
      the kept transcript; reconcile beneath this verdict; fold the sibling in; delete it.

### Reconcile

**Written:** begun 2026-10-17 23:57 UTC, completed 2026-10-17 23:59 UTC, at HEAD `994176f`
(phase 1 committed unrevised; the delta still identical at HEAD). Nothing above this heading was
edited. The sibling was removed with `rm` at 23:59 UTC; the floor (CI plane), `reviewscan` and
`datescan` were re-run on the folded file after that and are clean.

**Provenance of this step.** The orchestrator committed phase 1 as `994176f`, pushed, placed the
sibling in the tree and released it by message; it formed no finding. It also reported a
`git fetch --unshallow` on the checkout — verified: `.git/shallow` absent, `git rev-list --count
HEAD` → 1779, `b572594` now an ordinary ancestor of HEAD. Opened, in this order and nothing else:
the sibling; the queue pointer `160/780`; the commissioning item `200/090`; the landing commit's
body (`git show -s --format=%B b572594`); the intent record
`docs/sessions/2026-10-16-0703-queue-run-after-the-sizescan-ruling.md`; the kept transcript
`docs/sessions/2026-08-17-0343-cross-session-channel-transcript.md`; the two prior verdicts the
sibling names for these surfaces — `docs/reviews/2026-08-17-1000-channel-doctrine-cold.md` and
`docs/reviews/2026-07-26-2215-evidence-escalation-rung-cold.md` (rule 2's reconcile step, to
reconcile and never to anchor); `git blame` on `CONCURRENCY.md` lines 542–544 and 816–817; and
CHANGELOG and board greps for the class EC10 names. Not opened: the 2026-10-16 brief the sibling
names (another pass's framing, barred by the house rule in both phases), the three older
concurrency verdicts (they predate and do not touch this paragraph), `docs/SESSIONS.md`,
`docs/ROADMAP-DONE.md`. Still no git write command; still only this file edited; the scratch
directory still empty.

#### Per-finding notes

- **EC1 (MAJOR — stands; strengthened).** Seeded question 1 is the same observation, reached
  independently — the context partition held (the sibling's bytes reached me after `994176f`).
  Against the record: `200/090` (a) states the rule as "when a second voice agrees, ask which
  artefact it opened", and the transcript § 3 as "when the second never opened the source";
  neither carries the counting clause "only if it opened something the first party did not".
  That sentence was added at `b572594` and has no grounding instance behind it — none of the
  three episodes involved a same-artefact or derived-artefact case. The intent record says only
  "minted … beside the corroboration rung, with all three instances cited". Seeded question 2 (a
  re-run) is my case-table row 8: covered by the example list ("the API answer"), not by the
  rule's verb; the ladder's top rung already names reproduction, and one clause could say so.
  The prior §13 verdict (EE2) reads the rungs as ordered by evidential strength — the vocabulary
  the counsel uses. Severity unchanged.
- **EC2 (MODERATE — stands; sharpened).** Seeded question 4 is the same. `git blame`: line 542
  landed in `b0f202d` (2026-08-17, the channel extraction); line 816 in `df2d4e7` (2026-09-20,
  "correct the scratchpad clause — the attribution was wrong") — the second statement was
  written by the session that made the error, inside its own correction, so the rule was
  restated at the point of its breach before it was minted. The intent record says both rules
  "were already written, but only in `CONCURRENCY.md` § *The channel*" — inexact: the second
  statement sits in § *Orchestrated queue runs*, which the same record cites as the third
  instance. The 2026-08-17 channel verdict reviewed line 542 when it was the only statement; it
  was not a second original then. Severity unchanged.
- **EC3 (MODERATE — stands; grounded).** Not anticipated by the sibling, the intent record or
  `200/090`. The transcript shows the corrective in the first episode as "a peer went and re-read
  your source rather than taking my claim on trust" — someone opened the artefact; the
  receiver-side "ask which artefact it opened" is `200/090`'s framing (the filing session's
  words, not the child's). Severity unchanged.
- **EC4 (MODERATE → minor — corrected at reconcile).** Phase 1 said the rung test was "not on
  the record" and that rungs 2 and 3 were "not considered on the record". The barred
  commissioning item shows otherwise: `200/090` lines 25–31 place the rule on rung 1 with a
  reason — "the prose scanners cannot see either — this is a reasoning defect, not a text
  defect — so if anything catches it, it is framing at the point of use rather than a check" —
  which considers and rejects rung 2. Written 2026-08-17 by the filing session, before the third
  instance. My phase-1 argument that findability "was not what failed" is also weaker than
  written: the point of use for this rule is where a session grades an agreement (§13), and on
  2026-09-20 the rule lived only in the channel section, so a rung-1 move to §13 is coherent
  with that occurrence. What survives: the would-have-prevented test was not re-run at minting
  after the third instance (the ✅ note counts and stops); rung 3 was never considered; the
  paragraph does not point at the rung reasoning, so a reader of §13 sees a count where the
  record holds an argument; and the rung-1 fix "framing at the point of use" was executed as a
  third original rather than as the home with pointers — which is EC2. Phase-1 text stands as
  written; this note records the error and the re-grade. The counsel narrows to: point the
  grounding note at `200/090`'s rung reasoning, and record the post-third-instance test there.
- **EC5 (minor — stands; confirmed).** The intent record says CHANGELOG entries "were written
  for all three guard changes" and names none for the minting; the omission is an omission, not
  a policy.
- **EC6 (minor — stands; confirmed).** `200/090`'s ✅ note already holds the sibling-rule
  decision in full ("(b) has one instance. It stays in `CONCURRENCY.md` § *Re-run, don't
  reason*, not promoted. Its second instance is the trigger to re-open it."). The two EVIDENCE
  sentences duplicate a decision already in its proper home.
- **EC7 (minor — stands; narrowed).** Seeded question 3 is the same probe. (ii) is now verified
  against the transcript § 3: "I asserted `faves` had mistranslated CF3. A second session backed
  it and added supporting evidence. A third read `CONCURRENCY.md` and found we were both
  wrong." The narrative holds; `200/090` (a) carries it, so the citation is right in aggregate,
  with the CONCURRENCY half holding the class only. One wording defect is confirmed rather than
  suspected: the asserting sessions and the child alleged to have mistranslated were the
  **same** child — the paragraph's "a child's sessions agreed that a child had mistranslated"
  reads as two. (i) stands.
- **EC8 (note — stands; strengthened).** Seeded question 5 is the same. `200/090` itself
  classifies `115/060` as "same mechanism, different surface — a claim gaining authority from
  repetition rather than from anyone re-opening the source". That is the class stated at the
  level that covers all three; the paragraph's heading narrows it to "a second voice".
- **EC9 (note — stands; confirmed by the unshallow).** After `git fetch --unshallow`:
  `.git/shallow` absent, 1779 commits, `git log --oneline b572594..HEAD --
  docs/method/EVIDENCE.md` empty. The brief's confirm-step is correct on a full clone and
  misfires on the shallow clone this container shipped with.

#### Seeded question 6 — answered, no finding

The grounding bracket runs 12 of the paragraph's 20 lines; the rule's test precedes it (lines
191–198), so a reader finds the test without reading the grounding. `EVIDENCE.md` §15 uses the
identical shape (an 11-line bracketed grounding), so the convention has precedent in the same
file. EC6 names the part of the bracket that does not belong in doctrine at all.

#### Formed at reconcile

- **EC10 — note (formed at reconcile) — the CHANGELOG-omission class has a second noticed
  occurrence.** The 2026-08-17 channel verdict's CH12 recorded no CHANGELOG entry for a
  ~155-line doctrine section; EC5 records none for this minting. `PROPAGATION.md § When a rule
  keeps breaking`: "treat a *second* occurrence you *happen* to notice as the trigger" for the
  ladder. Rung 2 is plausible — a co-change check that a commit touching `docs/method/*.md`
  also touches `CHANGELOG.md`, the shape `blockscan --against HEAD^` already runs in CI,
  advisory. By my greps no board item proposes it, and the channel section still has no entry
  (`grep -n -i 'the channel' CHANGELOG.md` returns one unrelated line). *Counsel:* a board
  item, not a doctrine edit.

#### Prior verdicts' standing claims, checked

- `2026-07-26-2215` (EE1–EE6, the §13 ladder): EE2's reading — the rungs are ordered by
  evidential strength and the principal's recollection is reported-tier — is consistent with my
  case-table row on the principal and with EC1's counsel. EE3 (the rule may not bind where the
  choice is faced) is the same point-of-use argument `200/090` makes for rung 1. Nothing in EE
  conflicts with EC1–EC9.
- `2026-08-17-1000` (CH1–CH16, the channel section): CH12 feeds EC10. The verdict carries no
  decisions section I could find; its findings' status is not this pass's to establish.

#### Overall after reconcile

**PASS-WITH-FINDINGS — 1 MAJOR · 2 MODERATE · 4 minor · 3 note** (EC4 re-graded MODERATE →
minor at reconcile; EC10 added at note; phase-1 counts left as written above). The headline is
unchanged and sharper: the paragraph's operative counting sentence was added at minting with no
grounding instance behind it and contradicts its own lead on the paradigm cases. Findings remain
the principal's to decide (rule 3); nothing applied.

## Deferred material — folded in at the verdict

# Sibling to the agreement-is-not-corroboration cold pass — held under rule 1's split

Sibling of `docs/reviews/2026-10-17-0930-agreement-not-corroboration-cold.md`, held under
`docs/method/REVIEW.md` rule 1's split. **Open only after the phase-1 findings in the brief are
committed.** Written 2026-10-17 UTC by the Opus brief-writer named in the brief's provenance; it
forms no finding. Fold this file in below the reconcile and delete it at phase 2.

## Intent and commissioning records

- Intent record: `docs/sessions/2026-10-16-0703-queue-run-after-the-sizescan-ruling.md` —
  **not opened by the brief-writer**.
- Commissioning board item (head lines and one grep line seen, never read whole): `200/090`
  (two corroboration failures worth minting, offered upward by a child session as method; now
  `[x]`). Its grep line says the episode, `115/060` and a third instance meet the >2 promotion
  rule.
- The landing commit's message body (read by the brief-writer): it counts three recorded
  instances (a child's episode, a coined paraphrase cited as a source, a 2026-09-20 attribution
  two sessions agreed on and a transcript falsified), says the rule "lived only as a lesson of
  the channel" until now, and says the sibling rule (a symptom count locates existence, not site)
  has one instance and stays unpromoted. The same commit released another item's claim
  (`140/020`) and held a drafted re-wording there, unlanded; that part is not this delta.

## Prior verdicts on these surfaces (named by filename grep, not opened, not exhaustive)

- `docs/reviews/2026-07-26-2215-evidence-escalation-rung-cold.md` — the §13 ladder itself
- `docs/reviews/2026-08-17-1000-channel-doctrine-cold.md` — the `CONCURRENCY.md` channel passage
- `docs/reviews/2026-07-11-concurrency-put-away.md`,
  `docs/reviews/2026-07-13-concurrency-claiming-work.md`,
  `docs/reviews/2026-07-20-1355-concurrency-flip-cold.md` — older `CONCURRENCY.md` passes
- `docs/reviews/2026-10-16-1551-standing-checklist-test-rule-cold.md` — an unrun 2026-10-16 brief
  whose delta includes earlier `EVIDENCE.md` commits (another pass's framing)

## The pointer's own lens hints

None. The pointer is refs-only.

## Overlap with sibling passes of this batch

No other pass in the 2026-10-16 or 2026-10-17 batches has this paragraph as its delta. The
160/710 pass (checklist and test rule) has `EVIDENCE.md` in its delta, from `90c42ec` to
`be9a3ae` (which added §15), all before `b572594`. The 160/820 pass shares this pass's intent
record and authoring run.

## Seeded questions (the brief-writer's suspicions, a floor not a fence)

1. "Count the agreement as corroboration only if it opened something the first party did not."
   Read literally, two parties who each opened the *same* primary file are not corroboration.
   Is that intended, or does "independent route" (the paragraph's own first sentence) mean
   something else? The two sentences may set different tests.
2. The ladder already put *reproduce it yourself* above *independent corroboration*. A party
   that re-runs a probe opens no artefact in the paragraph's sense (file, transcript, API
   answer). Does the new test classify a re-run as corroboration, or leave it out?
3. The first grounding instance cites `200/090` "and the kept exchange in `CONCURRENCY.md`
   § *Re-run, don't reason*". At HEAD that section records the agreement failure as "two-of-three
   agreement felt like confirmation"; check the paragraph's retelling ("a third read the doctrine
   and found both wrong") against it.
4. `CONCURRENCY.md` keeps its two statements of the rule, with slightly different wording ("the
   second party never opened" vs "neither party opened"). Was a pointer from those sites to the
   new home owed under one-fact-one-home, and is "a lesson of the channel" now a second original?
5. Is a three-instance count that includes one item from a child (`200/090`) and one coined
   paraphrase (`115/060`, itself a quotation defect rather than an agreement failure) three
   instances of *this* rule, or of a neighbouring one? The >2 rule's threshold is a non-goal;
   whether these instances meet it is not.
6. The paragraph is a long parenthetical (16 lines inside brackets) carrying the grounding. Does
   that shape meet the house's prose conventions, and would a reader find the rule's test without
   reading the grounding?
