# Cold pass — the PT rulings applied — the fourth guard requirement homed, the copies swept

**Pass type:** doctrine cold pass (with the seven code banners it governs), per
`docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection: this batch's reviewer and orchestrator are both `claude-fable-5-1`.
**Status:** BRIEF WRITTEN 2026-09-25 UTC; the review runs in the same batch
under the orchestration below, by a reviewer that is not the brief-writer.
**Queue pointer:**
`docs/roadmap/300-posture-recover-cheaply-mike-commissioned/040-rule-4-cold-pass-queued-the-posture.md`.
**Why it earns a review:** the fourth requirement says what every guard must
declare; the PT cycle found it had no home a guard could comply with, and this
application is what gives it one — a wrong home leaves every guard non-compliant
with a rule nobody can meet.

## Spawn provenance

- **Author of the work under review:** the session(s) that landed the commits
  named under *What the work is*. This brief-writer was not that session, was
  neither started nor instructed by it, and has edited none of the delta's
  paths.
- **Who wrote this brief:** an atelier session Mike opened on 2026-09-20 and
  re-pointed on 2026-09-24 with the prompt "Please deliver all fable dependent
  work, and work that would be best delivered using fable", on the Fable tier
  (`claude-fable-5-1`), orchestrating this batch of twenty rule-4 passes. It
  wrote this brief from the queue pointer, the landing commits' subjects and
  file lists, and the delta paths' names; it did not open the intent record or
  any prior verdict on these surfaces.
- **Who takes the review:** a fresh Fable subagent (`claude-fable-5-1`) spawned
  by the brief-writer with this brief as its only framing. It is not the
  author's session and was not instructed by the author. The reviewer repeats
  its own provenance in the verdict.
- **Orchestration shape, disclosed per rule 4:** reviewer-plus-orchestrator. The
  orchestrator holds the `.deferred.md` sibling outside the worktree, commits
  the reviewer's phase-1 findings unrevised, then releases the sibling's text by
  message; the reviewer appends a reconcile section; the orchestrator folds the
  sibling in and updates the pointer. The orchestrator forms no finding and
  writes no severity. Both seats are Fable, so the off-tier clause is not
  invoked; the shape is stated anyway so the record is auditable.
- ⚠️ **Brief-writer's exposure, disclosed** (rule-2 material it met before
  writing): the `docs/SESSIONS.md` index entries of 2026-09-11 to 2026-09-19
  (the last three summarise the 2026-09-18 and 2026-09-19 runs in the authors'
  words); the first 30 lines and the last ~3,000 characters of
  `docs/sessions/2026-09-20-1053-queue-run-the-loose-ends.md`, read during an
  interrupted-session sweep on 2026-09-20; every queued `⏳` pointer on the board
  in full, including each pointer's own "lens that matters" paragraph — that
  paragraph is the author's framing and has been moved to this pass's sibling;
  the pass file `docs/reviews/2026-08-17-1000-coldsweep-cold.md` in full (brief
  and verdict) and lines 1–80 of
  `docs/reviews/2026-08-21-0820-pointing-up-cold.md`, both as formatting
  templates; the landing commits' subjects and `--stat` file lists (never the
  diffs); and, as doctrine read at onramp, `docs/method/CONCURRENCY.md` §§ *On a
  split board*, *Claiming at a dirty primary checkout* and *Surviving an
  interrupted session*, `docs/method/REVIEW.md` and `docs/method/00-APEX.md` at
  HEAD. Per-pass additions are marked ⚠️ under *Deferred reading*.

## What the work is

Landing commits (diff these; review the paths at HEAD):

- `3453842` (2026-08-23) — the landing commit

Delta paths:

- `docs/method/GUARDS.md` — the four-requirements preamble; § *The home*
- `docs/method/PRINCIPLES.md` §10 — the two limits carried; the `ACCESS.md` case
  pointer dropped
- `docs/method/SECRETS.md` + `docs/method/DATA-PROTECTION.md` — the up-pointers
  (the ruled stamped-copies half)
- the seven code banner spellings in `tools/` (`leakscan.py`, `secretscan.py`,
  `test_datescan.py`, `test_linkscan.py`, `test_pathscan.py`,
  `test_spellscan.py`, `test_wrapscan.py`)
- `CHANGELOG.md` — the 2026-08-23 entry and the belated note
- board items `docs/roadmap/300-*/010-*.md` (the citation) and
  `docs/roadmap/115-*/120-*.md` (the fold note)

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code,
tests and live behaviour. The lenses organise it; they do not bound it.
Non-goals are the only narrowing and are themselves reviewable.

Whether § *The home* names a surface, a format and a check a guard can actually
comply with — then check every guard in the registry at HEAD against it (count
compliant, non-compliant, and guards added after 2026-08-23 that never met it:
the registry has gained `conflictscan`, `blockscan`, `memprobe`, `coldsweep`
since). Whether the seven banners say the same thing in the same words, and
whether the scanners rewritten on 2026-09-20 kept their banner. Whether the two
up-pointers compress without narrowing. Whether `115/120`'s fold left one
declaration standard or two. **Non-goal:** the PT rulings themselves.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself. The
   home rests on the registry being the one place every guard passes through —
   test whether a tool can be a guard without a registry entry (the instruments
   layer; `coldsweep`), and what the fourth requirement then binds.
2. **Correctness & quality.** Diff `3453842`. Check each pointer resolves; count
   the requirements on every surface; compare the seven banners byte for byte
   and against every other tool's banner at HEAD.
3. **Completeness / harvest.** Search for every other statement of the guard
   requirements: `tools/README.md` header, `CONTRIBUTING.md` and its template,
   `docs/build/REPO-STANDARD.md`, `skills/`. Is the fourth requirement in the
   registry's *schema* or only in prose beside it?
4. **Security & privacy** — mandatory. Doctrine prose plus comment banners; no
   runtime surface. Check the banners carry nothing but the rule. Discharge the
   house scanner by grounds in one line.

## Re-run obligation

Re-run, do not read. A recorded proof is a claim that can be stale at the commit
that recorded it; a proof you have not re-run is not one you can close on. Lift
floor invocations from `.githooks/pre-commit`, `tools/floor.py` and
`.github/workflows/ci.yml` rather than guessing.

- a registry walk: for each `Scanner` in `tools/floor.py` at HEAD, record
  whether its module carries the declared banner and the home's fields
- `linkscan`, `pathscan`, `wrapscan`, `spellscan` over `docs/method` at HEAD;
  the floor on both planes

## House rules for this run

- You work in the shared review worktree
  `/Users/mike/worktrees/atelier-review-batch-0925` (branch
  `review-batch-0925`), read-only except for THIS brief file. Other reviewers
  are working there at the same time on their own briefs; never open another
  `docs/reviews/2026-09-25-0715-*` file — it is another pass's framing.
- Run **no git command that writes** in the worktree (no add, commit, stash,
  checkout, worktree, reset, clean). Read-only git (`log`, `show`, `diff`,
  `blame`, `branch -r`) is fine. Mutation probes, checkouts of older commits,
  scratch children and scratch linked worktrees go in your own clone: `git clone
  <worktree> <scratchpad>/<PREFIX>/probe` under the session scratchpad, named by
  your prefix so parallel reviewers do not collide.
- One heavy process at a time on this machine: run the full Python suite
  (`python3 -m unittest discover -s tools`, in the foreground, ~minutes) at most
  once, never scan any tree outside the worktree or your scratch clone, and
  never point a scanner at the machine's other repos.
- `/security-review` is **discharged by grounds** for this batch: it reads the
  session's pending diff, which in the shared worktree is other passes' unstaged
  drafts, and this is a landed-delta review. State that line in your lens-4
  answer and deliver the code-altitude read by hand, checked against the OWASP
  catalogue where the work has a code surface.
- Dates in your verdict are absolute ISO-8601 from `date -u` (the hook-plane
  `datescan` reds relative words such as "yesterday" or "next week" tree-wide,
  and would block the orchestrator's commit). Wrap prose at ≤ 100 columns. NZ
  English. Never quote a secret, a placeholder token, an email address or any
  personal detail — this repo is PUBLIC; describe, don't quote.
- Review deep, not fast. A finding needs a probe or a re-driven claim behind it,
  not reasoning alone; a clean lens needs the trail that earned it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the deferred material lives in the sibling .deferred.md, held by the orchestrator outside the worktree under the rule-1 split and released only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`,
`docs/sessions/`, every prior verdict in `docs/reviews/`, the queue pointer
`docs/roadmap/300-posture-recover-cheaply-mike-commissioned/040-rule-4-cold-pass-queued-the-posture.md`
(it carries the author's own lens hints), and:

- the verdict `docs/reviews/2026-08-17-1321-posture-cold.md` (PT; its § *Rulings
  — 2026-08-23* is this delta's intent record)
- `docs/sessions/2026-08-17-0900-posture-recover-cheaply.md`

Sweep with `python3 tools/coldsweep.py --root
/Users/mike/worktrees/atelier-review-batch-0925 --also-exclude
docs/roadmap/300-posture-recover-cheaply-mike-commissioned/040-rule-4-cold-pass-queued-the-posture.md
<pattern>` — rule 2's default bar, plus `--also-exclude` for the items above;
`--include-barred` only with disclosure in the verdict. Reading the *delta* is
never barred: the code, its tests, the doctrine text and the catalogue entries
are the subject. What is barred is the author's narrative of why, and the
verdicts that recorded it.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list.
Then append your verdict below a `---` divider in THIS file: provenance repeated
(how you were spawned, your tier, what you read), per-lens answers, findings
with stable IDs (prefix `PW`: `PW1`, `PW2`, …) and severities (MAJOR / MODERATE
/ minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL line with counts, a
re-run ledger with the commands and their results, and a follow-up checklist.
Then STOP and report to the orchestrator that phase 1 is written. Do not open
the sibling (it is not in the tree); do not edit the queue pointer, the board,
or any file but this one.

**Phase 2.** On receipt of the sibling's text, append `### Reconcile` beneath
your verdict: per-finding notes against the seeded questions and the intent
records, any finding formed at reconcile marked as such, and the overall line
restated. Never revise phase-1 text. The orchestrator folds the sibling in below
your reconcile.

Findings on doctrine are the principal's to decide (rule 3): record all, apply
nothing; your counsel per finding is welcome, labelled as counsel and kept
beneath the finding.

---

## Verdict — phase 1 (written 2026-09-25T07:30Z)

### Provenance, repeated

- **Reviewer:** a fresh subagent on `claude-fable-5-1` (the tier REVIEW.md rule 4
  names), spawned by the batch orchestrator with this brief as its only framing.
  Not the author's session; neither started nor instructed by the author of
  `3453842`. Reviewer-plus-orchestrator shape as the brief discloses; both seats
  Fable, so the off-tier clause is not invoked.
- **Worktree:** `/Users/mike/worktrees/atelier-review-batch-0925`, read-only
  except this file; no writing git command run. HEAD was `c4b9cd0` at spawn and
  advanced to `60225c1` during the pass (three other passes' phase-1 commits);
  `git diff --stat c4b9cd0 HEAD` over every delta path is empty, so the subject
  did not move. I did not open those three commits' files.
- **What I read:** this brief; `docs/method/REVIEW.md` and `00-APEX.md` in full;
  `docs/method/GUARDS.md` in full; `PRINCIPLES.md` §10 and the situation tests
  (lines 412–552) plus its heading list; `SECRETS.md` lines 1–20;
  `DATA-PROTECTION.md` via the diff; the `CHANGELOG.md` 2026-08-23 entry; board
  items `115/120`, `300/010`, `300/020` in full and `docs/ROADMAP.md` index lines
  surfaced by sweeps; `docs/method/README.md` lines 80–92; `tools/floor.py`
  lines 340–730 and the registry; `tools/leakscan.py` 55–100;
  `tools/secretscan.py` 88–125; `tools/coldsweep.py` 1–45;
  `.github/workflows/ci.yml`; `.githooks/pre-commit`; `.atelier-floor.json`;
  grep hits only from `tools/README.md`, `docs/build/REPO-STANDARD.md`,
  `docs/decisions/README.md`, `docs/build/templates/`, `skills/`,
  `docs/method/ACCESS.md`, and board items `320/200`, `320/300`, `020/370`,
  `020/380`. Delta diff via `git show 3453842 -- <paths>` with the queue pointer
  path excluded.
- ⚠️ **Exposure, disclosed:** (1) the commit *body* of `3453842` names the
  PT1–PT9 rulings in the author's words — intent-adjacent prose, met through
  `git show --stat`, which prints the body before the stat; (2) the CI-plane
  floor's secretscan advisory list printed the *path* of one prior verdict
  (`docs/reviews/2026-08-09-0822-…`) — path only, no content; (3) the tree-wide
  sweeps ran through `tools/coldsweep.py` with the default bar plus
  `--also-exclude` on the queue pointer, never `--include-barred`. The deferred
  sibling is not in the tree and was not opened; the queue pointer `300/040` was
  not opened.

### Lens answers

**1. Approach & assumptions.** Load-bearing assumptions, named by me and tested:

- *The floor registry is the one place every guard passes through.* **False at
  HEAD.** `tools/floor.py --list` on both planes prints 15 entries; `.github/
  workflows/ci.yml` wires three further guards as bespoke steps — `stampscan`,
  `blockscan`, `signscan` — each with a comment saying it is *deliberately* not
  in the registry, and board item `020/380` itself calls two of them "guards
  outside the floor registry". A child's `local` check is a fourth route: it is
  built into a `Scanner` from `.atelier-floor.json`, whose admitted keys
  (`LOCAL_KEYS`) are `run, why, planes, args, scope` and nothing beside `why`.
  What the fourth requirement binds for those guards is undefined → **PW1**.
- *The seven banners are the complete copy set.* **False by one** — the
  doctrine index `docs/method/README.md:87` still says three → **PW3**.
- *The home is buildable where it is homed.* **True.** `Scanner` is a frozen
  dataclass with `why: str`; a sibling field is a one-line addition, though the
  build must also reach `LOCAL_KEYS`, the config parser and `--list` rendering.
- *The interim clause is honest.* **True.** GUARDS.md lines 30–31 say "funded
  and not yet built"; the registry confirms nothing is built.
- *The fold leaves one standard.* **True on the board.** `115/120` is `[ ]`, its
  fold note names one slot with the wider fields, and a sweep for "beside the
  `why`" / "`why` field" finds no competing funding (5 hits, all this delta or
  the `115` README).
- *`coldsweep` and `memprobe` are guards.* **False.** `coldsweep`'s docstring
  says "Not a floor check … gates no commit and has no verdict"; `memprobe` is a
  measurement harness. The brief's "the registry has gained `conflictscan`,
  `blockscan`, `memprobe`, `coldsweep` since" is wrong on three of four — only
  `conflictscan` (2026-09-18) entered the registry; `blockscan` (2026-09-20) is
  CI-only; the other two are instruments. Brief framing attacked as rule 1 asks.

**2. Correctness & quality.** Diff of `3453842` read in full. Every pointer
resolves: linkscan clean over `docs/method` and over the whole tree on both
planes; the `300/010` link to `115/120` resolves; `ACCESS.md` at HEAD carries no
device-joining, BYOD or hotspot content (grep), so "no home doc yet" is true at
HEAD. Requirement counts per surface: GUARDS.md preamble **4**; `CHANGELOG.md`
**4**; `300/010` three-plus-fourth; seven banners **4** in the header — but the
two scanner banners' *bodies* still carry **3** bullets (NARROW, REASONED,
NOISY) and neither declares → **PW2**; `docs/method/README.md:87` **3** →
**PW3**; `PRINCIPLES.md` §10 gives no count. Banners byte-for-byte: the five
test docstrings share `GUARDS.md — narrow, noisy, reasoned, declared.` exactly
(`test_pathscan` continues into a paragraph); the two scanner headers share
`GOVERNED BY \`method/GUARDS.md\` — narrow, noisy, reasoned, declared` and then
diverge (`:` / `. Same contract as`). Every other tool at HEAD cites GUARDS.md
by rule letter only (12 modules, 4 further `Allowances` classes) — no other
three-word or four-word banner exists to drift. The 2026-09-20 rewrites
(`020/380` series, `c1a2f12` file-walk single-sourcing) kept all seven: 21
commits touched the delta files after landing and the banner survives each.
The two up-pointers compress without narrowing: each names its case, points at
§10, and says "carries the case, not the rule". The two limits are carried in
§10 — but in a second spelling that differs from the canonical one → **PW7**.
`CHANGELOG` present tense overclaims the slot → **PW8**.

**3. Completeness / harvest.** Other statements of the requirements: none in
`tools/README.md`, `docs/build/REPO-STANDARD.md`, the `CONTRIBUTING.md`
template or `skills/` (grep for narrow/noisy/reasoned/GUARDS — no hits beyond
unrelated uses of the words). One missed: `docs/method/README.md:87` (**PW3**).
Schema or prose: **prose only** — no field on `Scanner`, no key in `LOCAL_KEYS`,
nothing printed by `--list` beside `why`; GUARDS.md says so. Guards landed after
the ruling carry no declaration on any durable surface (**PW4**). The
`review:`-line homing for non-guard designs points at a surface whose own
documentation does not carry the choice (**PW6**). "Declared" is now two terms
in one doc (**PW5**).

**4. Security & privacy.** `/security-review` is **discharged by grounds**: it
reads the session's pending diff, which in this shared worktree is other
passes' unstaged drafts, and this is a landed-delta review. Hand read at code
altitude: the seven `tools/` hunks are one comment or docstring line each
(`git show` shows only `#`/`"""` lines changed); no runtime path, input, output
or secret handling moves, so no OWASP Top 10 / ASVS vector has a surface here.
The banners carry the rule and nothing else — both scanner banner bodies and
all five docstrings read in full. At design altitude the doctrine prose adds no
personal detail: rulings are attributed by the principal's first name and date,
the repo's established convention; no email, address, family or health detail
enters. Lens clean.

### Findings

**PW1 — MODERATE — The home reaches registry guards only; three guards at HEAD
and every child-local check sit outside it.** GUARDS.md § *The home* says the
declaration "lives in the floor registry, beside the `why` field" and that all
four requirements bind "every guard in the estate". It says what a non-*guard*
design does (the `review:` line) and nothing about a non-*registry* guard.
Probe: `floor.py --list` (15 entries, both planes); `ci.yml` wires `stampscan`,
`blockscan`, `signscan` as bespoke steps, each commented as deliberately
off-registry; `LOCAL_KEYS` admits no declaration key, so a child's `local` guard
could not comply even after `115/120` lands unless that build reaches the config
schema. By this doc's own § *A rule with no home is not a rule*, the fourth
requirement is homeless for those guards. Not MAJOR because the interim clause
("binds new guard work as a review question") is registry-agnostic and covers
them until the build.
*Counsel:* one sentence in § *The home* — an off-registry guard declares in its
module docstring beside the wiring note a reader already meets there — and a
line in `115/120` that the slot reaches `LOCAL_KEYS` and the `local` parser.

**PW2 — MODERATE — Two banners say four and deliver three.** `tools/
leakscan.py:71` and `tools/secretscan.py:99` now read "narrow, noisy, reasoned,
declared" and are followed by exactly three bullets — NARROW, REASONED, NOISY —
with no DECLARED bullet and no statement, anywhere in either module, of which of
the two things the guard does (tree-wide sweep of the declaration vocabulary:
zero hits in `tools/`). The header was widened; the body was not. That is a
claim in the module that the module visibly does not meet, and on this delta's
own reading these two are the estate's clearest "forbids the act" guards
(`advisory=None`, "a burned secret is burned whatever the repo's visibility"),
so the missing bullet was one line each. The five test docstrings are one-word
labels on an `Allowances` class and read as citations, not claims.
*Counsel:* add the fourth bullet to both (each forbids the act; say why), or
hold the header at three until the home lands. The former is cheaper and is the
interim clause honoured in place.

**PW3 — minor — An eighth copy, unswept, on the surface loaded at onramp.**
`docs/method/README.md:87` (the doctrine index): "Carries the estate's standing
requirement on every allowance: **narrow, noisy, reasoned**" — three, dated
2026-08-05 (`git log -S`), untouched by the 2026-08-17 landing and by this
sweep. Two drifts in one line: the count, and "on every allowance" where
GUARDS.md says "on every guard".
*Counsel:* sweep it to four and to "guard"; the `(rule-4 review queued,
2026-08-05)` tail on the same line is a separate staleness for whoever owns the
index.

**PW4 — minor — Guards landed after the ruling carry no declaration on any
durable surface.** `conflictscan` (registry, 2026-09-18) and `blockscan`
(CI-only, 2026-09-20) state neither cheap-failure nor forbids-the-act in their
docstrings or in their board items (`320/200`, `320/300` — grep). The one
post-ruling guard *proposal* that does declare is `320/080` ("it forbids the
act"). The interim clause makes the declaration a review question; I cannot
read those reviews before phase 2, but the question's answer is not on any
surface a future session reads, which is the shape § *A rule with no home*
names. Severity minor because `300/020` is the queued census that will ask it
of every guard, and both guards are plainly "forbids the act".
*Counsel:* fold `conflictscan` and `blockscan` into `300/020`'s list by name.

**PW5 — minor — "Declared" now names two different things in GUARDS.md.**
§ *Provenance, not direction* (2026-08-05) lists "Four conditions … 1.
**Declared** — written down in the repo"; the preamble (this delta) lists
"narrow, noisy, reasoned, **declared**" meaning cheap-failure-or-forbids. The
README index (line 85) glosses the provenance list as "a declared/reasoned/
visible act". "Reasoned" sits in both lists too but maps to the same rule (c);
"declared" does not. A reader meeting the four conditions after the four
requirements will pair them. The name was chosen 2026-08-17; this delta carried
it to the preamble and seven banners.
*Counsel:* rename one — "written" for the provenance condition costs least.

**PW6 — minor — The `review:`-line homing names a surface that does not carry
it.** § *The home*: for non-guard designs "say which you chose" homes "in the
existing `review:` line". At HEAD every documentation of that line —
`docs/decisions/README.md`, the ADR template, `docs/build/templates/docs/
ROADMAP.md:15`, `tools/reviewscan.py` — admits two spellings, `queued (<file>)`
and `not warranted — <grounds>`, and none mentions prevention or cheap failure
(grep across those surfaces and `skills/`: no hits). A design author reading
the line's own contract is not told to say which they chose; the "home" is a
pointer to a surface, not a rule on it.
*Counsel:* one clause in the template's `review:` description, or drop the
claim and leave the situation test as the home.

**PW7 — minor — Two spellings of the two limits, and they differ.** §10 now
carries "a test arriving after the work is grounds to declare, never to
unwire" — GUARDS.md's canonical text is "never grounds to unwire a working gate
*on the author's own judgement* — a guard that fails this test is a *finding
for the principal*, not a revert". The §10 compression drops the qualifier, so
read alone it bars the principal too. And §10's own sentence says the cases
"point up here rather than restating" — then restates GUARDS.md downward.
*Counsel:* §10 keeps "carried with its two limits (`GUARDS.md`)" and drops the
paraphrase.

**PW8 — note — CHANGELOG present tense overclaims the slot.** `CHANGELOG.md:
126–128`: "the declaration lives in the floor registry beside `why`". No such
field exists at HEAD (`Scanner`, `LOCAL_KEYS`, `--list`). GUARDS.md's matching
sentence self-corrects two sentences on ("Until that lands"); the CHANGELOG
entry does not.

**PW9 — note — `tools/secretscan.py:99` is 88 columns after the edit** (the
leakscan line is 71); the module wraps at ~80 elsewhere. Cosmetic; wrapscan is
scoped to docs and does not gate it.

### Overall

**PASS-WITH-FINDINGS** — 0 MAJOR · 2 MODERATE · 5 minor · 2 note.

Counsel on cycle state (REVIEW.md, *when the cycle stops*): no MAJOR, so the
cycle on this delta closes on the principal's decisions and the findings are
decided into the backlog; the natural home for PW1, PW2 and PW4 is `115/120` /
`300/020`, which are already open.

### Re-run ledger

| Command (from the worktree root) | Result |
|---|---|
| `git show --stat 3453842` · `git show 3453842 -- <delta paths, pointer excluded>` | 15 files, +88/−16; read in full |
| `git diff --stat c4b9cd0 HEAD -- CHANGELOG.md docs/method/ tools/ docs/roadmap/ .atelier-floor.json` | empty — delta unchanged under the advancing HEAD |
| `python3 tools/floor.py --list --plane hook` / `--plane ci` | 15 entries each, identical; `why` printed, nothing beside it |
| Registry walk (each `Scanner` vs its module at HEAD) | banner: `leakscan` ✅ `secretscan` ✅, the other 13 cite GUARDS.md by rule letter or not at all (`board`, `harvestscan`, `publishscan` none); home's field: **0 of 15** — the field does not exist; declaration prose: 0 of 15 |
| Off-registry guards at HEAD | `stampscan` (2026-07-23), `signscan` (2026-07-12), `blockscan` (2026-09-20) — wired in `ci.yml` only; declaration prose: 0 of 3 |
| `python3 tools/linkscan.py --root <wt> docs/method` | ✅ exit 0, 0 suppressed |
| `python3 tools/pathscan.py --root <wt> docs/method` | ✗ exit 1, 1 finding — `docs/method/session-open/session-open-prompt.md:15`, the `../atelier/…` shape (`320/010`'s class); file last touched 2026-09-20, outside this delta; warn-only on the floor |
| `python3 tools/wrapscan.py --root <wt> docs/method` | ✅ exit 0 |
| `python3 tools/spellscan.py --root <wt> docs/method` | ✅ exit 0 |
| `python3 tools/floor.py --plane hook --root <wt> --tools <wt>/tools` | exit 0; 11 ✅ 3 👁️; the five `--staged` checks scanned an empty index ("0 staged path(s)") so their clean is over nothing; sizescan 2 size-advisories (ROADMAP, SESSIONS); pointerscan 1 grammar warn (`160/380`, not this delta); pathscan 1 warn (as above) |
| `python3 tools/floor.py --plane ci --root <wt> --tools <wt>/tools` | exit 0; whole tree; secretscan 22 advisory entropy findings (🟡, design), leakscan structural-only (🟡, design); same three warns as the hook plane |
| `python3 -m unittest discover -s tools -p 'test_*.py'` (once) | ran; **summary line not captured** — my own pipe lost it (`tail` cut the unittest summary behind a test's subprocess output; zsh spells `pipestatus` in lower case). Not re-run per the one-run house rule |
| `python3 -m unittest tools.test_{datescan,linkscan,pathscan,spellscan,wrapscan,leakscan,secretscan,floor}` → scratch log | 673 ran, 671 OK, 2 *load* errors — `test_datescan` and `test_linkscan` import siblings bare and need `discover`'s path; an invocation-shape error, not a code one |
| `python3 -m unittest discover -s tools -p 'test_datescan.py'` | 68 tests OK, exit 0 |
| `python3 -m unittest discover -s tools -p 'test_linkscan.py'` | 73 tests OK, exit 0 |
| `python3 tools/coldsweep.py --root <wt> --also-exclude <pointer> <pattern>` | `narrow, noisy, reasoned` 9 hits; `GOVERNED BY` 2; `fourth requirement` 13; `cheap-failure\|forbids-the-act\|…` 8 (all doctrine/board); `GUARDS\.md` 128; variant spellings (`three/four requirements`, `narrow…noisy`) 14; `beside the \`why\`…` 5 — every run: 510 files searched, 347 barred |
| `gh run list --branch review-batch-0925` | `[]` — the branch is unpushed; no CI floor exists for this SHA, so the full-suite result stands unverified by me |
| Interpreter | Python 3.14.6 on this machine (the spawn note said 3.9) |

### Follow-up checklist

- [ ] PW1 — ruling: a home sentence for off-registry guards; `115/120` reaches
      `LOCAL_KEYS` and the `local` parser
- [ ] PW2 — ruling: fourth bullet in both scanner banners, or header back to
      three until the home lands
- [ ] PW3 — sweep `docs/method/README.md:87` (count and "allowance"→"guard")
- [ ] PW4 — name `conflictscan` and `blockscan` in `300/020`'s census
- [ ] PW5 — ruling: disambiguate "declared" (rename the provenance condition)
- [ ] PW6 — ruling: template clause on the `review:` line, or drop the claim
- [ ] PW7 — §10 points at the two limits instead of paraphrasing them
- [ ] PW8 — CHANGELOG tense ("is funded to live", or the interim clause)
- [ ] PW9 — cosmetic rewrap of `secretscan.py:99`
- [ ] Orchestrator: the full Python suite's exit on the pushed SHA (CI floor)
      is owed — my one local run's summary was lost to my own pipe
- [ ] Phase 2: reconcile against the sibling and the `2026-08-17-1321` verdict's
      § *Rulings — 2026-08-23*
