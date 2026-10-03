# Cold pass — the mandate-versus-default date rule in GUARDS.md

**Pass type:** doctrine cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection: this pass's reviewer and orchestrator are both `claude-fable-5-1`.
**Status:** BRIEF WRITTEN 2026-10-03 0357 UTC; the review runs under the
orchestration below, by a reviewer that is not the brief-writer.
**Queue pointer:** `docs/roadmap/160-doctrine-review-owed/450-rule-4-cold-pass-queued-the-date-kind-rule.md`.
**Why it earns a review:** a dated deferment is how every guard's allowance expires; a rule about who may move that date decides whether a child can quietly extend an exemption the house set.

## Spawn provenance

- **Author of the work under review:** the 2026-10-03 queue run (an Opus
  orchestrator with dispatched workers) that landed the commits named under
  *What the work is*. This brief-writer was not that session, was neither
  started nor instructed by it, and has edited none of the delta's paths.
- **Who wrote this brief:** an atelier session Mike opened on 2026-10-03 with
  the prompt "Do all cold reviews and any other work dependent on fable", on
  the Fable tier (`claude-fable-5-1`), orchestrating six rule-4 passes queued
  by that run. It wrote this brief from the queue pointer, the landing commits'
  subjects and `--stat` file lists, and the delta paths' names; it did not open
  the intent record.
- **Who takes the review:** a fresh Fable subagent (`claude-fable-5-1`) spawned
  by the brief-writer with this brief as its only framing. It is not the
  author's session and was not instructed by the author. The reviewer repeats
  its own provenance in the verdict.
- **Orchestration shape, disclosed per rule 4:** reviewer-plus-orchestrator. The
  orchestrator holds the `.deferred.md` sibling outside the worktree and
  outside the harness scratchpad (subagents can read the scratchpad), commits
  the reviewer's phase-1 findings unrevised, then releases the sibling's text by
  message; the reviewer appends a reconcile section; the orchestrator folds the
  sibling in and updates the pointer. The orchestrator forms no finding and
  writes no severity. Both seats are Fable, so the off-tier clause is not
  invoked; the shape is stated anyway so the record is auditable.
- ⚠️ **Brief-writer's exposure, disclosed** (rule-2 material it met before
  writing): the authoring run told this session over the cross-session channel
  that the pointer existed and named its subject in a phrase; nothing else from
  that run was read. Earlier in the same sitting this session commissioned
  read-only inventories of the board's open items and of every verdict in
  `docs/reviews/`, for a ruling round; the summaries it received include prior
  findings on the surfaces under review. Those summaries are author-side
  framing this pass must meet cold; every line of them that bears on this delta
  has been moved to the sibling and kept out of this brief. The brief-writer
  also read the 2026-09-25 batch's staged-plane brief as a formatting template,
  the session index entries of 2026-09-19 to 2026-10-01, and, as doctrine at
  onramp, `docs/method/REVIEW.md`, `docs/method/00-APEX.md` and
  `docs/method/COMMUNICATION.md` § *Asking for a ruling* at HEAD.

## What the work is

Landing commits (diff these; review the paths at HEAD, `17c75a9` or later):

- `f54ae72` (2026-10-03) — guards: a fleet date names its kind — mandate binds, default seeds (board `040/010`)

Delta paths:

- `docs/method/GUARDS.md` — the new subsection *Who may move a deferment's date: mandate or default*, under § *Acceptance and deferment are different things*

No tool, template or other doctrine file changed in the landing commit; whether any of them should have is yours to establish.

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code,
tests and live behaviour. The lenses organise it; they do not bound it.
Non-goals are the only narrowing and are themselves reviewable.

Read the subsection against the whole of `GUARDS.md` and every surface that carries a `review-by` or expiry date: `tools/floor.py`'s handling of declared dates, the scanners' allow-marker expiry if any, `.atelier-floor.json`, `PROPAGATION.md`'s floor block, the child `CLAUDE.md` template, and the board legend. Where the rule quotes the principal, check that the quoted words and the surrounding paraphrase say the same thing. Find a live dated allowance in this repo and walk it through the rule: which kind is it, who may move it, and does any tool enforce that. **Non-goal:** whether the principal's rule is right.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself. The rule presumes every fleet date can be classed as one of two kinds: find the date that is neither, or both. It presumes a child can tell which kind a date is: find where that is undeclared.
2. **Correctness & quality.** Read the subsection and the section it sits under in full. Does the new text contradict, duplicate or silently narrow anything else in `GUARDS.md` or in the docs it points at? Does it name a home for the declaration it requires?
3. **Completeness / harvest.** Every surface that states date semantics for allowances and deferments: list them and check each at HEAD against the new rule. Does `CHANGELOG.md` carry it? Does any guard read the kind?
4. **Security & privacy** — mandatory. A rule about who may extend an exemption is a security control. Check the failure direction: if a child mis-classes a mandate as a default, what guard notices? The house scanner is discharged by grounds (landed delta; the pending diff is this brief) — say so, and deliver the read by hand.

## Re-run obligation

Re-run, do not read. A recorded proof is a claim that can be stale at the commit
that recorded it; a proof you have not re-run is not one you can close on. Lift
floor invocations from `.githooks/pre-commit`, `tools/floor.py` and
`.github/workflows/ci.yml` rather than guessing.

- the floor on both planes at HEAD (doctrine delta; no code to drive)
- `python3 tools/floor.py --selftest` and a grep of `tools/` for date and expiry handling, to ground the sweep in lens 3

## House rules for this run

- You work in the shared review worktree `/Users/mike/worktrees/atelier-review-430`
  (branch `review-430-1003`), read-only except for THIS brief file. Other
  reviewers are working there at the same time on their own briefs; never open
  another `docs/reviews/2026-10-03-*` file — it is another pass's framing. Run
  **no git command that writes** there (no add, commit, stash, checkout,
  worktree, reset, clean). Read-only git (`log`, `show`, `diff`, `blame`) is
  fine. Mutation probes, scratch children and checkouts of older commits go in
  your own clone: `git clone /Users/mike/worktrees/atelier-review-430
  <scratchpad>/DK/probe` under the session scratchpad, named by your
  prefix so parallel reviewers do not collide.
- One heavy process at a time on this machine: run the full suite at most once,
  in the foreground with a long timeout; if a memory-probe test times out, note
  it as environmental and re-run that test file alone before recording it.
  Never scan any tree outside the worktree or your scratch clone, and never
  point a scanner at the machine's other repos. Other sessions are live on this
  machine and in this repo's primary checkout; touch nothing there.
- `/security-review` is **discharged by grounds**: it reads the session's
  pending diff, which here is other passes' drafts and this brief, and this is a
  landed-delta review. State that line in your lens-4 answer and deliver the
  code-altitude read by hand.
- Dates in your verdict are absolute ISO-8601 from `date -u` (the hook-plane
  `datescan` reds relative words such as "yesterday" or "next week" and would
  block the orchestrator's commit). Wrap prose at ≤ 100 columns. NZ English.
  Never quote a secret, a placeholder token, an email address, a private
  repo's name or any personal detail — this repo is PUBLIC; describe, don't
  quote.
- Review deep, not fast. A finding needs a probe or a re-driven claim behind it,
  not reasoning alone; a clean lens needs the trail that earned it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the deferred material lives in the sibling .deferred.md, held by the orchestrator outside the worktree under the rule-1 split and released only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`,
`docs/sessions/`, every prior verdict in `docs/reviews/`, the queue pointer
`docs/roadmap/160-doctrine-review-owed/450-rule-4-cold-pass-queued-the-date-kind-rule.md`
(it carries the author's framing and this pass's claim line), and:

- `docs/sessions/2026-10-03-0144-queue-run-handups-and-tool-defects.md` (the
  intent record)
- the board item `docs/roadmap/040-*/010-*.md` (the commission, carrying the principal's words in context)
- `docs/roadmap/020-*/170-*.md` and `docs/roadmap/115-*/120-*.md` (prior GUARDS.md rulings' outcome lines)

Sweep with `python3 tools/coldsweep.py --root
/Users/mike/worktrees/atelier-review-430 --also-exclude
docs/roadmap/160-doctrine-review-owed/450-rule-4-cold-pass-queued-the-date-kind-rule.md
--also-exclude docs/roadmap/040-review-validation-policy-mike-2026-07-05 --also-exclude docs/roadmap/020-policy-as-code-programme-five-tracks-mik --also-exclude docs/roadmap/115-guardrail-architecture-mike-commissioned <pattern>` — rule 2's
default bar plus the items above; `--include-barred` only with disclosure in
the verdict. Reading the *delta* is never barred: the code, its tests, the
README entries and the registry are the subject. What is barred is the author's
narrative of why, and the verdicts that recorded it.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list.
Then append your verdict below a `---` divider in THIS file: provenance repeated
(how you were spawned, your tier, what you read), per-lens answers, findings
with stable IDs (prefix `DK`: `DK1`, `DK2`, …) and severities
(MAJOR / MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL
line with counts, a re-run ledger with the commands and their results, and a
follow-up checklist. Then STOP and report to the orchestrator that phase 1 is
written. Do not open the sibling (it is not in the tree); do not edit the queue
pointer, the board, or any file but this one.

**Phase 2.** On receipt of the sibling's text, append `### Reconcile` beneath
your verdict: per-finding notes against the seeded questions and the intent
record, any finding formed at reconcile marked as such, and the overall line
restated. Never revise phase-1 text. The orchestrator folds the sibling in below
your reconcile.

Findings are the principal's to decide (rule 3): record all, apply nothing;
your counsel per finding is welcome, labelled as counsel and kept beneath the
finding.

---

## Verdict — DK, phase 1

**Provenance.** Reviewer: `claude-fable-5-1` (Fable tier), a fresh subagent spawned by the
brief-writer with this brief as its only framing. Not the author's session (the 2026-10-03
queue run) and not instructed by it. Orchestration shape as the brief states:
reviewer-plus-orchestrator, both seats Fable, so the off-tier clause is not invoked. Written
2026-10-03 04:27 UTC.

What I read: this brief; the landing commit `f54ae72` (`git show` — subject, body, `--stat`,
the GUARDS.md hunk); `docs/method/GUARDS.md` in full; `tools/floor.py` (module docstring
§§ advisory and board marks, `Advisory`/`Scope`/`Flags`, `_load_advisory`, the floor-line
renderer); `tools/floorfleet.py` (advisory rendering); `.atelier-floor.json`;
`.githooks/pre-commit`; `.github/workflows/ci.yml`; `docs/method/PROPAGATION.md` (floor block,
§ The layer-override rule, § Who is a child, § Pointing up steps 3–4 and *Closing the loop*);
`docs/build/REPO-STANDARD.md` (the `.atelier-floor.json` bullet);
`docs/build/templates/CONTRIBUTING.md` and `templates/workflows/floor.yml` (advisory passages);
`docs/roadmap/README.md` (board legend); `CHANGELOG.md` (headings and horizon hits);
`tools/README.md` (advisory hits); `docs/ROADMAP.md` (index lines only); and three unbarred
board items that mention the horizon — `110/060`, `110/070`, `230/010` — plus
`030/README.md`'s `review-by` paragraph. Not opened: anything the brief bars, the sibling, any
other `2026-10-03-*` review.

⚠️ **Exposure disclosed, two items.**

1. The shared worktree at `4ff8de5` (branch `review-430-1003`, forked at `2c8c3b0`) did not
   contain the delta: `f54ae72` was not an ancestor, and GUARDS.md there had no such
   subsection. I reviewed `main` at `ca61feb` through the scratch clone the brief allows. The
   orchestrator merged `origin/main` (`e5b44fe`) into the worktree mid-pass (HEAD `0a669e7`
   after the merge); I confirmed `f54ae72` is an ancestor there and that every surface named
   above is byte-identical between `ca61feb` and `0a669e7` (`git diff --stat` empty). Every read
   below is at `ca61feb`, which equals `0a669e7` for those paths.
2. The brief's sweep command bars `docs/roadmap/040-review-validation-policy-mike-2026-07-05`,
   a directory that does not exist; the commission item lives under
   `docs/roadmap/040-principal-set-dates-mandate-vs-default-m/`. My first `coldsweep` (pattern
   `mandate`) therefore printed two part-lines of the barred `040/010` item as grep hits before
   I added the real path to every later sweep. I did not open the file. Seen: a fragment
   restating that a mandate binds the class and children may only tighten it, and a fragment
   saying the item holds the principal's words verbatim. Neither formed a finding; both are
   already in the GUARDS.md text under review.

### Lens answers

**1. Approach & assumptions.** Load-bearing assumptions, named: (a) every fleet date is one of
two kinds; (b) a child can tell which kind a date is; (c) a `review-by` is something children
*inherit*. (c) is false as a mechanism: nothing in the tree carries a fleet-wide `review-by` to
children. `.atelier-floor.json` is per repo; atelier's own has never held an `advisory` key
(`git log -S'review-by' -- .atelier-floor.json` is empty); and the only "inherited" date in the
tree is the example `2026-09-01` at `templates/CONTRIBUTING.md:65` and `floor.py:104,806`. The
C1b horizon reached children as a board instruction. (b) fails at the same point — DK1. For (a),
dates that are neither: a child's own self-set `review-by` with no fleet date behind it (the
template example is one; the rule is silent on who may move it), and PROPAGATION's
pending-upstream line, a deferment whose expiry is an *event* (the next pin bump), not a date —
DK3. The grounding instance itself is covered: `110/070` records the 2026-09-01 horizon as the
principal's, so it is a principal-set date ruled before the rule, which the retro clause reaches.

**2. Correctness & quality.** Read against the whole of GUARDS.md and the docs it points at. No
contradiction found. Two quiet widenings of the quote (DK4) and one missing cross-link (DK5):
PROPAGATION's layer-override rule says a child rule looser than the house's is a defect unless
the principal rules an exemption *recorded in the child*; a later date on a default is exactly a
ruled looseness, and neither doc says so to the other's reader. The subsection does not name a
home for the declaration it requires — DK1. Placement under § Acceptance and deferment is right:
a `review-by` is the deferment expiry that section defines. The floor's prose gates pass on the
new text (wrapscan at 85 columns, spellscan, datescan all clean — ledger).

**3. Completeness / harvest.** Surfaces stating date semantics for allowances and deferments,
each checked at `ca61feb`: GUARDS.md (rule present); `tools/floor.py` docstring and
`_load_advisory` (`why` + `review-by` only, no kind, example date 2026-09-01 — already passed);
`tools/floorfleet.py:1323–1334` (🔴 expired / ⚠️ until / 🟡 pre-C1; no kind, no house-date
comparison); `templates/CONTRIBUTING.md:59–70` (same example, passed date, no kind — DK6);
`templates/workflows/floor.yml:20–25` (advisory described; no date semantics beyond "reason");
`PROPAGATION.md` floor block (no allowance-date semantics — nothing to update); § Pointing up
step 3 and *Closing the loop* (event-expiring deferment — DK3); `REPO-STANDARD.md:125–135`
(narrow, never contradict — DK5); board legend `docs/roadmap/README.md` (dates only on `[~]`
claims; nothing to update); `tools/README.md` (secretscan's advisory *tier*, not deferments;
nothing to update); `CHANGELOG.md` — does **not** carry the rule; latest entry 2026-09-20
(DK7). Does any guard read the kind? No: a grep for `mandate`, `kind`, `ceiling`, `house date`
over `floor.py` and `floorfleet.py` finds only two unrelated uses of "kind".

**4. Security & privacy.** `/security-review` is discharged by grounds: it reads the session's
pending diff, which here is other passes' drafts and this brief, and this is a landed-delta
review. Read by hand: the subsection adds no secret, token, address or private repo name; the
two migrated repos are unnamed; the principal is named by first name as the rest of the doc
already does. Failure direction (the brief's question): a child mis-classes a mandate as a
default and sets a later date. **No guard notices.** `floor.py` accepts any valid ISO date
(probe B parsed, exit 0); `floorfleet` prints `⚠️ advisory until <date>` and goes 🔴 only when
the *child's* date passes; nothing holds a house date to compare against; nothing reads history
to see a date move later (`floor.py` and `floorfleet.py` contain no `git log`, `blame` or
`rev-list`). The control the rule describes is a convention with no check — DK2.

### Findings

**DK1 — MAJOR. The kind the rule requires has no home a child reads, and the one structured
home refuses it.** The subsection says a fleet date-setting ruling "names its kind", that the
answer is recorded "beside the date", and that "a child reading the date knows what it may
do". The date a child reads is `advisory.<check>.review-by` in its own `.atelier-floor.json`.
Probe A (a `kind` key beside `review-by`): `floor: .atelier-floor.json: advisory.wrapscan has
unknown 'kind' (known: 'why', 'review-by')`, exit 1. Probe B (the kind written into `why`):
parses, exit 0, read by nothing. The ruling itself lives in a board item and a session record —
the surfaces GUARDS.md § *A rule with no home is not a rule* says a cold session does not load.
By this doc's own homing test, the kind is declared nowhere a child's session or tool reads it,
and the premise "a `review-by` the children inherit" names a mechanism that does not exist
(lens 1). *Counsel:* either (i) give the kind a structured home — a house-dates declaration in
atelier (`{check, date, kind}`) that `floorfleet` reads, and/or an optional `kind` key that
`_load_advisory` accepts — or (ii) have the subsection say honestly that the kind's only homes
as the tree stands are the ruling's board item and the child's `why` text, and queue (i). Either
way, "a child reading the date knows what it may do" should not stand until one of them lands.

**DK2 — MODERATE. A rule about who may extend an exemption is a security control, and no check
enforces it.** DK1's companion from the enforcement side. A later date on a mandate is
indistinguishable, to every tool on both planes, from a later date on a default or from a
child's own date: `floor.py` validates shape only; `floorfleet` compares the date to the current
day, never to a house date; no tool reads a repo's history, so a `review-by` that moved later
between commits is invisible. The brief's own "why it earns a review" — a child quietly extending
an exemption the house set — is exactly the unguarded case. *Counsel:* the cheapest check is
hook-plane and local: `floor.py --plane hook` already sees the staged `.atelier-floor.json`
beside HEAD's, so "review-by moved later" can be an advisory line at the commit that does it;
the house-date comparison for mandates belongs in `floorfleet` once DK1 gives it a value.

**DK3 — MODERATE. Dates that are neither kind.** (a) A deferment a child sets for itself with no
fleet date behind it — in practice the common case, since every live `review-by` is a per-repo
declaration — is outside the rule, which classes only dates "set by the principal for the whole
fleet". Who may move a self-set date, and how far, is unsaid, and that is where quiet extension
actually happens. (b) PROPAGATION.md § Pointing up step 3: a pending-upstream line is a
deferment "dated, addressed, and removable at the next pin bump" whose expiry is an event; the
subsection's "a deferment's expiry" does not reach it. (c) A fleet horizon set by a *session* in
a board item, not by the principal, is neither a mandate nor a default and is not "a date ruled
before this rule was written"; the retro clause does not reach it. *Counsel:* one sentence
scoping the rule to principal-set fleet dates and pointing self-set dates at § Provenance
(declared, reasoned, principal-visible), plus a line for (c): a date no principal set has no kind
until one is asked for.

**DK4 — minor. The paraphrase widens the quote in two places.** The quoted words say a child may
"argue for an exemption to something that should not apply to them"; the bullet says "through
its parent" — routing the quote does not contain (defensible via PROPAGATION § Pointing up, but
an addition). The quote says under a default a child "could set an alternative date"; the bullet
says a later date "stands as of right" — the quote grants the move, not freedom from every
condition, and § Provenance's four conditions still bind every deferment. "A deferment's expiry
is *often* set by the principal for the whole fleet" rests on one instance. The quote's source is
the barred commission item, so "near-verbatim" is checked at phase 2, not here. *Counsel:* mark
the two additions as the house's reading, or replace "as of right" with "needs no ruling, and
carries the reason every deferment carries".

**DK5 — minor. Missing cross-link with the layer-override rule.** PROPAGATION.md § Who is a
child: a child rule looser than the house's is "forbidden unless the principal rules a specific
exemption, and the exemption is recorded in the child". A later date on a default is a ruled
looseness; a reader of PROPAGATION alone reads it as drift, and a reader of GUARDS alone does
not learn that an exemption argued from a *mandate* must be recorded in the child.
`REPO-STANDARD.md:135` ("narrow but never contradict") has the same gap. *Counsel:* one pointer
each way; no restatement.

**DK6 — minor. Template and docstring examples carry a passed date with no kind.**
`docs/build/templates/CONTRIBUTING.md:65` and `tools/floor.py:104,806` show
`"review-by": "2026-09-01"` — the C1b horizon, already behind the calendar. A child that copies
the template example verbatim gets `[review by 2026-09-01 — PASSED, N days]` on its first floor
run, and the example says nothing of the date's kind, which is the rule's own ask. *Counsel:* a
visible placeholder (`YYYY-MM-DD`) in the template, and a kind named in the example's `why`.

**DK7 — minor. `CHANGELOG.md` does not carry the rule.** Latest entry 2026-09-20; no entry for
the 2026-10-03 doctrine change. Prior doctrine rulings of this size each have one.

**DK8 — MODERATE (pass integrity, not the delta). The brief framed the pass at a HEAD the
worktree did not have.** Detail under *Exposure disclosed*, item 1. A reviewer following
"review the paths at HEAD" literally in the named worktree would have read a GUARDS.md with no
subsection and formed findings against the wrong tree. Recovered via the scratch clone, then
confirmed identical after the orchestrator's merge. *Counsel:* one house-rule line in the brief
template — confirm the landing commit is an ancestor of the worktree HEAD before reading — and
the orchestrator merges `origin/main` into the review branch before spawning.

**DK9 — minor (brief, not the delta). The sweep's bar names a directory that does not exist**
(`040-review-validation-policy-mike-2026-07-05` where the item lives under
`040-principal-set-dates-mandate-vs-default-m`), so `coldsweep` did not enforce the bar the prose
declares. Detail under *Exposure disclosed*, item 2. *Counsel:* `coldsweep --also-exclude` warns
when a given path matches nothing.

### Overall

**PASS-WITH-FINDINGS** — 1 MAJOR (DK1) · 3 MODERATE (DK2, DK3, DK8) · 5 minor (DK4, DK5, DK6,
DK7, DK9) · 0 notes. The rule says what the principal ruled and sits in the right section; what
it asks for — a declared kind a child can read — has no surface and no check, and the doc's own
homing test says that makes it not yet a rule.

### Re-run ledger

All runs at `ca61feb` in the scratch clone `<scratchpad>/DK/probe` (cloned from the worktree,
`main` fetched from origin), later confirmed byte-identical to worktree HEAD `0a669e7` for every
surface read. UTC, 2026-10-03.

| Command | Result |
|---|---|
| `git merge-base --is-ancestor f54ae72 HEAD`, worktree at `4ff8de5` | exit 1 — delta absent (DK8) |
| same, worktree at `0a669e7` after the orchestrator's merge | exit 0 |
| `git diff --stat ca61feb 0a669e7 -- <the reviewed paths>` | empty — identical |
| `python3 tools/floor.py --selftest` | `ok (15 scanners, 0 failure(s))`, exit 0 |
| `floor.py --plane hook --root <clone> --tools <clone>/tools` (lifted from `.githooks/pre-commit`) | exit 0; 12 ✅ enforced, 3 👁️ warn-only; the warn-only findings are pre-existing and off-delta (pointerscan grammar on `160/380`, pathscan missing-path in `session-open-prompt.md`, sizescan on ROADMAP.md and SESSIONS.md) |
| `floor.py --plane ci --root .` (lifted from `ci.yml`) | exit 0; same board plus 22 secretscan advisory (entropy) findings, all pre-existing, none in the delta; datescan, wrapscan, spellscan clean over GUARDS.md |
| `python3 -m unittest discover -s tools -p 'test_*.py'` (once, foreground; exceeded the 600 s limit and the harness moved it to the background; a sibling pass's suite ran concurrently) | ran to completion at 04:26 UTC; **result UNREAD** — the summary line was outside the captured tail and the pipe's exit code is `tail`'s, so no pass is claimed; the delta has no code, and the floor's own selftest and both planes above are the re-runs the brief lists |
| probe A: `floor.py --list --root kind-key` (`kind` key beside `review-by`) | ConfigError `unknown 'kind' (known: 'why', 'review-by')`, exit 1 |
| probe B: `floor.py --list --root kind-in-why` (kind in `why`, `review-by` 2027-01-01) | parses, exit 0; nothing reads the text |
| `git log -S'review-by' -- .atelier-floor.json` | empty — atelier has never declared a dated advisory |
| grep `mandate` / `kind` / `ceiling` / `house date` over `floor.py`, `floorfleet.py` | no kind handling |
| grep `git log` / `blame` / `rev-list` / `HEAD^` over the two floor tools | no history read |
| `coldsweep` ×4 (`mandate`; `2026-09-01`; dated-deferment regex; `review-by` family) | 423–425 files barred per run; the first run leaked two part-lines of `040/010` (DK9); hits are the lens-3 surface list |

### Follow-up checklist

- [ ] DK1, DK2 → one board item (a home for the kind and the check that reads it); the
      principal's call between counsel (i) and (ii)
- [ ] DK3 → wording ruling: scope sentence, self-set dates, event-expiring deferments
- [ ] DK4, DK5 → wording and cross-links in one commit, after a ruling on "as of right"
- [ ] DK6 → template and docstring example dates (mechanical)
- [ ] DK7 → `CHANGELOG.md` entry for the 2026-10-03 doctrine change
- [ ] DK8, DK9 → brief-template line, orchestrator pre-spawn merge, `coldsweep` no-match warning
- [ ] Phase 2 reconcile on receipt of the sibling: check "near-verbatim" against the commission
      item's quoted words

### Reconcile

Same reviewer (`claude-fable-5-1`), 2026-10-03, after phase 1 was committed unrevised. The
orchestrator disclosed that a blocked commit left another pass's staged files in the index, so
the phase-1 text landed inside `4ff5f81` ("close the CP pass") rather than under its own
subject; the content is mine byte-for-byte (worktree clean against HEAD when checked). Opened
for this section: the sibling's text; the intent record
`docs/sessions/2026-10-03-0144-queue-run-handups-and-tool-defects.md` (§ `040/010` and the
close); board items `040/010`, `040/README.md`, `160/450`, and the outcome lines of `020/170`
and `115/120`. Phase-1 text above is unrevised.

**Against the seeded questions.**

1. *Quoted verbatim? Paraphrase adds or drops a condition?* The GUARDS.md quotation matches the
   board capture in `040/010` word for word. The board item itself says it holds Mike's words
   "near-verbatim", and the original utterance is not in the tree, so verbatim-to-the-board is
   what can be shown. The paraphrase drops nothing; it adds two things (DK4 stands). Both
   additions trace to the run's gloss rather than the quote: "stand as of right" is the board
   item's own phrase for the two later dates, carried into doctrine as a general rule; "through
   its parent" appears nowhere in the item or the intent record and is the run's routing.
2. *Does any tool read a date's kind?* No, on either plane — DK1 and DK2 stand as written. The
   intent record confirms the run changed no tool and names GUARDS.md as "the home the item
   named"; the item's "likely doctrine home" was a guess at a prose home, and nothing in the
   record weighs where a child reads the kind.
3. *Does the rule say what an unnamed date is, and does that default fail safe?* It says a
   pre-rule date "has no kind on record" and to ask when it matters. It does not say what binds
   in the meantime, so the default is undefined rather than safe. PROPAGATION.md § The
   layer-override rule already supplies the safe reading — on a live collision the stricter
   reading wins until resolved upward, which here means treat an unnamed date as a mandate until
   the principal says otherwise. DK11 below.
4. *Placement?* Under § Acceptance and deferment is right and the item's own reasoning agrees:
   a `review-by` is the deferment expiry that section defines. The fourth requirement governs
   what a guard declares about itself, a different subject. The orchestrator's PT1/PW1 context
   is the apt comparison for DK1, though: PW1 found the fourth requirement's registry home
   reaches registry guards only; the kind's homelessness is the same class one level down — the
   per-repo floor config, where a child's date actually lives, has no slot for it.

**Per finding, against the intent record and the item.**

- DK1, DK2 — unchanged; neither record considers a machine-readable home or a check.
- DK3 — unchanged. The item's grounding ("the two self-migrated repos' later review-by dates")
  is the principal-set case; the self-set and event-expiring cases are not discussed anywhere.
- DK4 — attribution sharpened as in question 1; severity unchanged.
- DK5, DK6, DK7 — unchanged; the intent record's close lists no CHANGELOG entry for the run.
- DK8 — unchanged. The intent record confirms the run queued `160/450` and did not spawn the
  pass; the fork of the review branch before the delta is the review run's, not the author's.
- DK9 — checked against the live tree as asked: `docs/roadmap/` holds exactly one `040-`
  section, `040-principal-set-dates-mandate-vs-default-m/` (files `010-capture-doctrine-when-
  the-principal-sets-a-dat.md`, `README.md`), and `git log --all` over the path the brief named
  (`040-review-validation-policy-mike-2026-07-05`) is empty — that directory has never existed.
  The brief's bar was a typo'd path, not a renamed section; the deferred-reading list's glob
  (`040-*/010-*.md`) was correct and is what I followed.

**Formed at reconcile (marked as such).**

**DK10 — minor, formed at reconcile. The run's own clause is not marked as the run's in the
doctrine.** The commit message and the board item both say the retro clause ("A date ruled
before this rule was written has no kind on record…") is the run's addition "and is marked as
such". It is marked in the item and the intent record, not in GUARDS.md, where it follows
"Mike's rule (2026-08-09)" with no change of voice. A reader of the doctrine surface — the only
one a cold session loads — attributes it to the principal. *Counsel:* one attribution clause,
as the doc already does for its own tests elsewhere ("the run's addition, 2026-10-03").

**DK11 — minor, formed at reconcile. An unnamed date has no stated meaning until asked.**
Question 3 above. *Counsel:* one sentence pointing at PROPAGATION's stricter-reading rule, so
the meantime reads as mandate; this also answers the orchestrator's C5R9 context in part — the
answer, when recorded "beside the date", should carry the date it was ruled.

**Overall, restated: PASS-WITH-FINDINGS** — 1 MAJOR (DK1) · 3 MODERATE (DK2, DK3, DK8) ·
7 minor (DK4, DK5, DK6, DK7, DK9, DK10, DK11) · 0 notes. No phase-1 severity moved.

## Folded sibling — released after the phase-1 findings were committed

The `.deferred.md` sibling the orchestrator held outside the worktree, folded in
verbatim at close; the reviewer met it only in phase 2.

# Deferred sibling — the mandate-versus-default date rule in GUARDS.md (DK)

Held by the orchestrator outside the worktree and outside the harness
scratchpad. Released to the reviewer only after its phase-1 findings are
committed. Folded into the verdict file at close.

## 1. The queue pointer's own framing (author's words)

> - ⏳ **Rule-4 cold pass queued: the mandate-versus-default date rule
> (`040/010`).** The run authored the wording itself. The rule is Mike's
> and is quoted, and the placement and surrounding prose are the run's.
> It was queued at landing, and the run neither takes it nor spawns a
> reviewer for it. *Tier:* Fable, the principal-named review tier,
> checked at selection. *Pass type:* doctrine cold pass, per
> `method/REVIEW.md` rule 4. *Delta, scoped to paths:*
> `docs/method/GUARDS.md` (the new subsection under § *Acceptance and
> deferment are different things*). It landed on `main` on 2026-10-03.
> *Intent record:*
> `docs/sessions/2026-10-03-0144-queue-run-handups-and-tool-defects.md`.

## 2. Intent record and commissioning item (read in phase 2)

- `docs/sessions/2026-10-03-0144-queue-run-handups-and-tool-defects.md`
- the board item named in the pointer

## 3. What the authoring run said to the orchestrator (channel, verbatim)

> a third refs-only pointer of mine is on main, docs/roadmap/160-doctrine-review-owed/450-rule-4-cold-pass-queued-the-date-kind-rule.md. It covers a doctrine pass on a GUARDS.md addition. No detail beyond the file.

Nothing else from that run was read by the orchestrator.

## 4. Prior findings and seeded questions (the orchestrator's, labelled)

Context the orchestrator holds (from inventories, not from the intent record):

- The mandate-versus-default question has been open on the estate since the
  2026-08-09 floor sweep ("the mandate-vs-default date ruling" is named as an open
  ruling in the user-local estate-floor memory of that date).
- GUARDS.md's fourth requirement ("declared") was ruled 2026-08-23 (PT1) to be
  homed in the floor registry beside `why`; PW1 (2026-09-25, unruled MODERATE) found
  that home reaches registry guards only, not off-registry guards or child-local
  checks. A date-kind declaration may have the same homelessness.
- FG2 (2026-08-03, ruled) adopted "provenance, not direction" as the invariant: a
  declared, reasoned, expiring, principal-visible act may lower a response. The
  expiring part is what a date kind governs.
- C5R9 (2026-08-09, unruled minor): GUARDS lacks a grant-date requirement.

Seeded questions (the orchestrator's): (1) Is the principal's rule quoted verbatim,
and does the paraphrase around it add or drop a condition? (2) Does any tool read a
date's kind, or is the rule prose-only on every plane? (3) Does the rule say what an
unnamed date is, and does that default fail safe? (4) Does the subsection's placement
under *Acceptance and deferment* fit, or does it belong with the fourth requirement?
