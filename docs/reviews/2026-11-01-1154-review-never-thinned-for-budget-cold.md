# Cold pass — the commission that a review is never cut down to fit a budget (`430/010`)

**Pass type:** design cold pass on a captured feature, per `docs/method/REVIEW.md` § *Review
the design, not only the build* (a captured feature earns a review in its own right, cheapest at
the moment it is written), with rule 4's provenance discipline: the subject is doctrine about
review, filed by a session that runs reviews.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at selection by
whoever takes this pass. A session not on that tier stops here and takes nothing.
**Fable-gated:** the principal's standing ruling of 2026-10-26 is that no Fable work runs without
his explicit approval, and that such work waits for it rather than running on a lesser tier. This
pass runs **only on his explicit approval**.
**Status:** BRIEF ONLY — the review has NOT run. Written 2026-11-01 UTC by an Opus 5.5
brief-writer subagent; the pass waits for a cold Fable session that neither the item's author nor
this brief-writer (nor its orchestrator) started or instructed.
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/990-design-cold-pass-queued-review-never-thinned-for-budget.md`.
**Why it earns a review:** the item is the house's record of what the principal's rule means and
of the work owed to make it bind. Whatever it says the rule covers, and whatever it leaves out,
becomes the frame for the doctrine wording and the guards built from it. A reading that is
narrower than his words, or an options list that misses the case that actually recurs, is
inherited by every brief-writer and reviewer the rule is meant to protect, and nothing downstream
would notice: a guard built to a narrow reading passes green.

## Spawn provenance

- **Author of the work under review:** a Mike-opened Fable 5.1 orchestrating session on
  2026-10-04/05 UTC (the session that ran six cold passes that night), which filed the item in
  commit `323ff19`. Git cannot name a session; the item's own text names its filer as the session
  that made the offer it records.
- **Who wrote this brief:** an Opus 5.5 subagent (`claude-opus-5-5`) dispatched on 2026-11-01 UTC
  by a Mike-opened Opus 5.5 orchestrating session (`2be3482c`), on the principal's instruction of
  2026-11-02 NZDT: *"Write briefs for anything that needs a review in any of the repos, where a
  brief is not ready"*. Neither authored any of the subject, and neither was started or instructed
  by its author. **Off-tier for review, disclosed: the brief-writer forms no finding and writes no
  severity**, and stops after this brief and its sibling.
- **Who takes the review:** a further cold Fable session, not yet started, that passes rule 4's
  criterion. If it runs as reviewer-plus-orchestrator, rule 4's conditions apply and are disclosed
  in the claim, the pointer and the verdict. The reviewer repeats its own provenance in its verdict.
- **Barred from taking this pass:** the authoring session and its subagents; session `2be3482c`
  and its subagents, this brief-writer included.
- ⚠️ **Brief-writer's exposure, disclosed** (rule-2 material met before writing):
  - its dispatch prompt and a common-rules file from `2be3482c` (form and house rules, plus a
    candidate list naming this item and the phrase that matched it);
  - the item `430/010` whole and the section narrative `430/README.md` whole; the one
    `docs/ROADMAP.md` line for it; a `git grep` for `430/010` that printed **one
    `docs/SESSIONS.md` index line** (the intent record's summary line, which describes the
    filing night and the offer the item records) and one table row in item `300/020`;
  - `skills/review-brief/SKILL.md` whole; `REVIEW.md` lines 12–24 and 468–508 and its heading
    list; `ECONOMICS.md` lines 125–140 and 350–372, and a grep of it for budget words;
  - as shape examples: `docs/reviews/2026-10-26-0917-identifiers-credit-on-evidence-cold.md` whole
    and the head of its sibling (another pass, on other surfaces); the heads of several older
    briefs and verdict lines while triaging other candidates;
  - its harness also loaded user-level instruction files that hold the principal's later rulings
    on review spend. They are private and are not quoted here; what bears on the subject is
    named, by count only, in the sibling.

  It did **not** open the intent record (`docs/sessions/2026-10-04-2210-six-fable-cold-passes-and-the-budget-rule.md`)
  or any verdict on it. Everything evaluative it formed is in the sibling, by count in its header.

## The acceptance test

The principal's words, verbatim, are in the subject and are the test (`430/README.md` and the
item's opening quote):

> Remember that review work / sessions are never allowed to down grade the integrity or quality
> of the review process to meet a budget. Quality is more important than cost.
> If we run out of budget then we will resume the work when the budget replenishes

and the commission: *"Add a job to the board to reinforce the following point in the doctrine and
make it policy as code if we can find a way to do so e.g. how to write a brief and the review
process in macro and micro"*. Judge the item against those words, never against its own reading
of them.

## What the work is

One commit on `main`, `323ff19` (2026-10-04 22:29 UTC): *roadmap: file Mike's rule that a review
is never cut down to fit a budget (430/010)*. Paths:

- `docs/roadmap/430-review-quality-is-never-traded-for-budget-mike-commissioned/README.md`
- `docs/roadmap/430-review-quality-is-never-traded-for-budget-mike-commissioned/010-reinforce-the-rule-in-doctrine-and-guard-it-in-code.md`
- the generated `docs/ROADMAP.md` lines for both.

No later commit touches either file at `7bd98ce`; confirm at your HEAD. Nothing the item owes has
been built. The subject is the captured feature: the reading, the account of the house, the
evidence, the owed list (a)–(d) and the candidates under (c). The item's own review line names a
later rule-4 pass on the doctrine **wording** once written; that pass is a separate one and is
not this one.

## Claims the item makes, extracted (not evaluated)

- C1. **The reading:** budget may decide how many reviews run and when; it never decides how a
  review is run; when the allowance runs out, the work pauses and resumes after it replenishes.
- C2. `ECONOMICS.md` § the self-check (the cap never moves work down-tier; at the cap the choice
  is delay or pay) covers the reviewer's tier and does not cover a review's shape, depth or brief.
- C3. `ECONOMICS.md` § *Match the ceremony to the risk* can be read by a session under a tight
  allowance as licence to thin a review, and the two need reconciling: risk sets whether a review
  is owed and of what kind; once owed, budget does not shrink it.
- C4. `REVIEW.md` has no sentence on budget.
- C5. Without a stated whole, "downgrade" has nothing to be measured against, so a definition of
  the undecayable process is owed at two scales. Macro: one fresh reviewer per pass, the named
  tier, the brief-and-sibling split, both phases, every re-run on the list. Micro: what a brief
  must contain.
- C6. Guard candidates (none chosen): `reviewscan` requiring a brief's fixed parts (the four
  lenses, a re-run list, the deferred-reading bar, spawn provenance with the tier); one brief per
  queue pointer and one verdict per brief; a verdict's re-run ledger covering every re-run line;
  a paused pass recorded as paused, never closed.
- C7. What a guard cannot see is an offer made in conversation, so that half stays with the
  wording at the point of use; the candidate homes are `REVIEW.md` (beside rule 4),
  `ECONOMICS.md` (both sections) and the review-brief skill.
- C8. A resume path is owed, so that pausing at the cap is the easy route.
- C9. Evidence: one instance measured (the filing session's own offer to share one reviewer
  across several passes); the principal's report of several sessions doing the same is recorded
  as unmeasured.

## Scope

Widest the work admits: intent, the reading, the assumptions, the options, the account of the
house today, and what the item should own and does not. The lenses organise it; they do not
bound it. Probe, at least:

- **The reading against the words.** Take the verbatim text alone and write down, before reading
  C1, what it forbids and permits. Then compare. Every gap in either direction is a candidate
  finding.
- **The house today.** Read `REVIEW.md`, `ECONOMICS.md`, `AUTONOMY.md` (spend), the review-brief
  skill and the queue-run skill at HEAD for every sentence that already says, or contradicts,
  what the principal said. Test C2, C3 and C4 against that read, not against the item's
  summary. The doctrine has moved since `323ff19`; account for anything that landed after it.
- **The macro/micro list (C5).** Is it the whole process? Construct the ways a session under a
  low allowance could thin a pass that the list does not name (in the brief, in the run, in the
  verdict, in the reconcile, in what is claimed afterwards), and say which ones occur in the
  house's own record.
- **The guard candidates (C6).** For each, establish what `reviewscan`, `pointerscan` and the
  floor check today, and whether the candidate could be built without false positives on the
  ~200 existing briefs. Say which part of the rule no candidate reaches.
- **The pause (C8).** How does the house record a pass stopped at the cap today? Find instances
  in the board and the briefs, and whether any was recorded as closed, thinned or re-scoped.
- **Homing.** Apply `GUARDS.md`'s rule that a rule with no home is not a rule to the candidate
  homes in C7: which surface does a brief-writer or a reviewer actually read at the moment the
  temptation arises?

**Non-goals:** the doctrine wording itself (not written; its own pass is owed when it is), and the
principal's rule (his to make; reviewable only for how the item reads and carries it).

## The four lenses

1. **Approach & assumptions** — the most important. Name the load-bearing assumptions yourself
   first, then attack the ones below. Ask whether "reinforce in doctrine and guard in code" is
   the right shape for a rule whose breaches the item says happen in conversation.
2. **Correctness & quality.** Every factual claim about the house (C2–C4, C7) checked against the
   files at HEAD, with line numbers. Every overclaim or underclaim recorded against its text.
3. **Completeness / harvest.** What the item should have named and did not: surfaces, prior
   rulings in the house's own text, related open items, children that inherit the rule.
4. **Security & privacy** — mandatory. The subject is a board item in a public repo that quotes
   the principal. Check it carries nothing about his plan, spend or private context beyond what a
   public repo may hold (`docs/build/REPO-STANDARD.md`, the purpose-based rule), and whether the
   rule as read would push future records to publish spend detail. `/security-review` has nothing
   to reach: the subject is landed markdown, which its exclusions bar; discharge it in one line
   with those grounds, and never run it with this brief or its sibling dirty.

## Load-bearing assumptions to attack

Each is a falsifiable claim; damage it with a probe or confirm it by re-driving.

- A1. The reading (C1) is the principal's rule, no narrower and no wider.
- A2. The house has no sentence today that already states the rule (C2, C4).
- A3. `ECONOMICS.md`'s proportionality section is the source of the temptation (C3).
- A4. The macro/micro list (C5) is the whole of what may not be decayed.
- A5. A guard over brief and verdict shape (C6) would catch the breach the evidence shows.
- A6. One measured instance (C9) is enough to set the item's shape.

## Re-run obligation

Re-run, do not read. The brief-writer ran each line once, from a worktree root at `7bd98ce` plus
one records-only commit, in the foreground; its results are held in the sibling, not offered here.
Read exit codes explicitly.

- `git log --oneline -- docs/roadmap/430-review-quality-is-never-traded-for-budget-mike-commissioned/`
- `grep -n -i -E 'budget|allowance|replenish|tank|\bcap\b' docs/method/REVIEW.md skills/review-brief/SKILL.md`
  (C4), and the same pattern over `docs/method/ECONOMICS.md` (C2, C3)
- `python3 tools/reviewscan.py --help` and `python3 tools/reviewscan.py --root .`
- `python3 tools/pointerscan.py --root .`
- `nice -n 10 python3 tools/floor.py --plane ci --root .`

## House rules for this run

- Claim the pointer first (`[~]` with a stamp generated by `date -u` in the same command), on
  `main`, pushed before any review work starts.
- Work in a worktree; read-only except for this file. Scratch goes under your session scratchpad.
- This repo is PUBLIC: every byte of the verdict is published when pushed. Quote the principal
  only where the house already does; name no private repo; carry no plan, price or spend figure.
- This pass is pending while you run it: anything you write to the session log, the pointer or a
  commit subject before phase 2 names the sibling by file and count only.
- Absolute ISO 8601 dates from `date -u`; prose wrapped at ≤ 100 columns; NZ English.
- Review deep, not fast: a finding needs a probe or a re-driven claim behind it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the deferred material lives in the sibling .deferred.md, held apart under the rule-1 split and opened only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/` (the
intent record `docs/sessions/2026-10-04-2210-six-fable-cold-passes-and-the-budget-rule.md`
among them), every prior verdict in `docs/reviews/`, the queue pointer named above, `323ff19`'s
message body, and this brief's sibling
`docs/reviews/2026-11-01-1154-review-never-thinned-for-budget-cold.deferred.md` (2 sections:
re-run results, and 9 brief-writer questions).

The doctrine files and the subject itself are not barred. Sweep with `python3 tools/coldsweep.py
--root <your-worktree> --also-exclude
docs/roadmap/160-doctrine-review-owed/990-design-cold-pass-queued-review-never-thinned-for-budget.md
--also-exclude docs/reviews/2026-11-01-1154-review-never-thinned-for-budget-cold.deferred.md
<pattern>`; `--include-barred` only with disclosure in the verdict. Read `323ff19`
body-free with `python3 tools/coldsweep.py --root . --commit 323ff19`: plain `git show` prints the
body before the diff, and reading is atomic (rule 1).

## Process

**Phase 1.** Reproduce the floor first; work the lenses, the scope probes, the assumptions and the
re-run list; run the standing checklist V1–V7 unasked, each answered or discharged with grounds.
Append your verdict below a `---` divider in THIS file: provenance repeated (how you were spawned,
your tier, what you read), per-lens answers, the per-assumption result (A1–A6), findings with
stable IDs (prefix `RQ`: `RQ1`, `RQ2`, …) and severities (MAJOR / MODERATE / minor / note), an
overall PASS / PASS-WITH-FINDINGS / FAIL line with counts, a re-run ledger, and a follow-up
checklist. Then STOP and commit phase 1 unrevised before opening the sibling. Edit no other file.

**Phase 2.** Open the sibling and the intent record. Append `### Reconcile` beneath your verdict:
per-finding notes against the sibling's questions and the author's account, any finding formed at
reconcile marked as such, and the overall line restated. Never revise phase-1 text. Then fold the
sibling in below the reconcile and delete it.

The subject is doctrine-shaping text about review: record all findings and apply nothing (rule 3);
the principal decides, after a plain-language account. Counsel per finding is welcome, labelled as
counsel and kept beneath it.
