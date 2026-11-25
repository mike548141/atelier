# 2026-11-25 12:49 UTC — work run: three fixes, a hand-up, and why Fable passes pile up

**Session:** `f8dd3843` (messaging name `atelier-31`), Claude Opus 5.5, principal-opened by
`/atelier:work run` with no brief typed after it, so the run took the prompt's default order.
Orchestrator; two build workers (one Opus, one Sonnet) and one read-only Opus worker, each in
its own worktree or read-only.

## Opening

`ccopen` at 12:49 UTC: the machine was busy (15-minute load 22 on 12 cores), so the run waited
the prompt's 30 minutes and started at about 13:20 once both averages were under 12. A second
work run (`0b4f93ef`) and the `210/620` build session (`b04df0da`) were live; neither held a
claim this run wanted. Mid-wait, a relay from another session (`shed-73`) carried the
principal's words, verbatim: *"Tell all open claude sessions I am going to sleep so no questions
until I wake up, so work on everything you can sensibly until then rather than get stuck waiting
for me"*.

## What was done

- **Hand-up PR #142 landed as-is** (`320/910`, `320/920`, from a private child; no number
  collision), the first act on finding it.
- **`320/910`, inline:** a brief-writing worker runs each of its brief's re-run lines once
  under `nice`; a full-suite line it names for the orchestrator, which runs it before landing
  the brief. In `CONCURRENCY.md`, the dispatch skeleton, `REVIEW.md` and the brief skill.
  Cold pass queued as `160/1830`.
- **`210/580`, an Opus worker:** all fourteen `cctranscript --search` findings settled
  (twelve fixed, CS8 never present, CS13 answered by its pass); 126 tests. Pass `160/1840`.
- **`210/590`, a Sonnet worker:** `publishscan`'s ignore loader folded into `allowmarker` as
  parameters, refusals byte for byte. Pass `160/1850`.
- **`460/010` step 1, a read-only Opus worker:** the queued Fable passes classified; the
  answer and the annex below. Steps 2–4 open; the draft bar goes to him first.
- **`320/900`, an Opus worker:** the plain-tree walk counts what it prunes; `secretscan` and
  `leakscan` print it and warn. Pass `160/1860`; the git-mode twin filed as `115/560`.
- **`320/920`:** read, made `🎯` with a recommendation.
- Full suites before each push: 3,526 then 3,539 Python tests OK, 754 JS tests OK. The hook
  scanners were probed under the primary checkout's Python 3.9 after the fast-forward.

## Learned

- A rebase of the landing branch while its suite ran in the same worktree voided that run;
  the suite was stopped and re-run. Run the suite in a tree nothing else touches.
- A worker stamped a `CHANGELOG.md` heading with the local date; corrected to UTC at landing.
- A worker named the wrong home for a stale figure (`210/080`); it was the frozen archive,
  a record kept as written. Checked before writing it down.

## Left open, for him

- `460/010` step 2: the draft bar changes rule 4 itself, so it is put to him before it is
  written (the annex holds it).
- `320/920`: where a queued brief's held sibling lives (recommendation on the item).
- Four new cold passes queued this run (`160/1830`, `1840`, `1850`, `1860`) wait for his
  Fable approval like every other; under the draft bar `1850` would fold into the next
  scanner pass rather than run alone.

## Stopped on

**Everything left is blocked, with economics close behind**: of the board's remaining open
items not waiting on him, the ones read this run were either unruled choices (`115/210`,
`320/010` classes B and C, `320/770`'s reach, `010/130`), idea-only, or dated after this run
(`010/250`, `010/290`, on 2026-12-04).

## Annex — `460/010` step 1: the sample of queued passes

Written by the read-only worker against `origin/main` at `edcff979`; checked by this session.

### Clauses used (today's text)

- **D** — "doctrine text" earns the full ceremony (REVIEW.md § *Whether work earns a review*,
  ECONOMICS.md § *Match the ceremony*); rule 4: self-authored doctrine always earns a cold spawn.
  Rule 3 defines doctrine **by function**: "any rule that governs future agent behaviour, whether
  it lives in prose, an ADR, a schema, a validator, a CI gate, or a template or skill".
- **F** — first-of-kind or structural work. **S** — silent-failure mode ("a gate that can report
  green while not actually checking"). **I** — irreversible or public-facing. **P** — the
  principal's own order on the item.
- **SV** — the exemption: "tests and dogfooding exercise it end-to-end over already-reviewed
  machinery … wiring an already-reviewed tool into a gate, a refactor its suite fully covers, a
  records-only edit".
- `meets*` = meets only by the letter: a wording/correction edit counts as "doctrine text"
  because the text has no materiality test.

"Grounds" = the pointer says *why this work's failure would matter* (a risk class, a blast
radius), beyond "per `method/REVIEW.md` rule 4". "Principal" = y only where his words or his
picked option on the item ask for the review; approvals to *run* or *schedule* an already-queued
pass are noted but are not an order.

### Table

| id | subject (≤8 words) | class | clause | grounds | principal ordered |
|---|---|---|---|---|---|
| 985 | board index claimed-line fit, bracket neutralising | **fails** | SV (format fix, reviewed generator, wrapscan reds a miss) | y (reach: every child) | n |
| 986 | orchestrator writes the review pointer | meets | D (new CONCURRENCY rule) | y | n |
| 987 | board.py sorts numbers as numbers | **fails** | SV (sort order; visible; tested; 75-line commit) | y (reach) | n |
| 988 | datescan blockquotes report instead of block | meets | S (a blocking guard stops blocking a class) | y | n (built to his dial answers) |
| 989 | ccapple, private Apple-store search | meets | F + I (others' private content) + P | y | **y** ("Merge it now, review after") |
| 991 | cctranscript reads notifications one way | **fails** | SV (one record class, reviewed instrument, tested) | y (refs quoted) | n |
| 992 | scanner selftests print only verdict | **fails** | SV (output shape; verdict still printed) | y (reach: every child CI) | n |
| 1240 | floor bars, rollback check, membership, rule-copy | meets | D (00-APEX, AUTONOMY, GUARDS edits) + S | n | n |
| 1450 [x] | ccfleet, fleet-sweep, review-drain, modelguard | meets | F (headless sessions, permission mode, deny hook) | y | n (approved one run) |
| 1460 | verdict records its method and reasoning | meets | D (new rule from his words) | n | n (scheduled: "next … fable drain") |
| 1470 | floor Asking bullet: "same turn" | meets* | D (sync to an already-written rule, itself queued as 1440) | n | n (approved: API if parity) |
| 1480 | EVIDENCE §18 extended, §19–21 new | meets | D | n | n (approved: API if parity) |
| 1490 | three REVIEW.md paragraphs | meets | D | n | n (approved: API if parity) |
| 1500 | two PRINCIPLES bullets (interruption, SHA-2) | meets | D | n | n (approved: API if parity) |
| 1510 | guard own-work invariant; point-of-use wording | meets | D | n | n (approved: API if parity) |
| 1520 | relay rule, worker test bound, hygiene rewording | meets | D (two new rules; one rewording) | n | n (approved: API if parity) |
| 1530 | floor.py refuses bare-list spelling | **cannot say** | D-by-function (CI gate) vs SV (reviewed tool, tightening, 0 users) | y (reach) | n (approved: API if parity) |
| 1540 | floor drift check by setting; rotation trigger | meets | D (floor region copied into every child) | y | n (approved: API if parity) |
| 1550 | allow-marker scope without reason exempts nothing | **cannot say** | D-by-function vs SV (tightening, census 0 changed) | y (reach) | n (approved: API if parity) |
| 1560 | ccclose check 14 + floorhook SessionStart | meets | F (hook in every child session) + D (close verdict policy) | y | n (approved: API if parity) |
| 1570 | flipcheck, AUTONOMY sentence, quotescan advisory | meets | D (always-confirm floor's own doc) | y | n (approved: API if parity) |
| 1580 | PRINCIPLES §11 first-principles evaluation | meets | D | y | n (approved: API if parity) |
| 1590 | floor bundle: visibility slots, estate-root duty | meets | D (floor copied verbatim; widened duty) | y | n (approved: API if parity) |
| 1600 | leakscan G3 reads Office/PDF metadata | meets | F (untrusted-bytes parser in a blocking guard) | y | **y** (his pick "Build the reader"; the option named the review) |
| 1610 | /atelier menu, ccstatusline, prefixhook, MECHANISMS | meets | D + F (hook at every session open) | y | n (priority set: low) |
| 1620 | secretguard, deadhook, stashscan, treeline, pins | meets | F (Bash-denying hook; new verdict mode) | y | n (priority set: low) |
| 1630 | review never thinned, slice 2 | meets | D | n | n |
| 1640 | leakscan ipv4 skips UA version; graces removed | meets | S (narrowed detection; stated) — grace removal half is SV | y | n |
| 1650 | three doctrine corrections (PROPAGATION, EVIDENCE §17) | meets | D (new paragraphs + a corrected premise) | n | n |
| 1670 | board index: summary + unfinished only | meets | D (RECORD.md) + S (items can drop from index) | y | n |
| 1680 | archivecut tool and atelier's archive cut | meets | F + I-ish (deletes a file, re-points links) | n | n (scheduled: next drain) |
| 1690 | template scaffolds per-item board | meets | D-by-function (template stamped into children) | n | n |
| 1700 | session index retired into docs/sessions/ | meets | F + D (302 files written, RECORD.md) | n | n |
| 1710 | ccclose check 15, close listings, idhook | meets | D (blocking close policy) + F (text injected every session) | y | n (scheduled: next drain) |
| 1720 | ccopen, session-open twin | meets | F | y | n |
| 1730 | licenscan reads CC0, 0BSD vs ISC, Zlib | **cannot say** | S? (misread) vs SV (93-line table change, reviewed guard, tested) | y | n (scheduled: next drain) |
| 1740 [x] | ccfleet whole grant; UNLANDED verdict | meets | S (permission narrowing, claim release) | y | n (folded into RK by his pick) |
| 1750 | slice-5 census corrections, signscan coverage line | meets* | D (statements corrected to match the tree) | y | n (scheduled: next drain) |
| 1760 | CI template least privilege; slice-6 corrections | meets* | D-by-function (template) + corrections | y | n (scheduled: next drain) |
| 1770 | decision statuses accepted; scan wording; skill lists | meets | D (what binds changed) | y | n (scheduled: next drain) |
| 1780 | run start gates, parked mark, rename (partly withdrawn) | meets | D (session-open prompt, two rule files) | y | n (scheduled: next drain) |
| 1820 | DV and PK fixes re-check | meets | P (his pick "Before, plus re-check") | y | **y** |

### Counts

- **meets 35** (of which **meets\* 3**: 1470, 1750, 1760 — wording or factual corrections that
  qualify only because "doctrine text" has no materiality test)
- **fails 4** (985, 987, 991, 992 — all one queue run's batch of 2026-11-03)
- **text cannot say 3** (1530, 1550, 1730)
- **grounds stated: 29 y / 13 n.** All 4 "fails" stated grounds — and the grounds was *reach*
  ("every child runs it at `@main`"), which is not one of the text's triggers.
- **principal ordered: 3 y / 39 n.** Of the 39: 15 he later approved to run (14 on the API lane,
  1450), 9 he scheduled for "next drain" or folded, 2 he prioritised low, the rest have no word.

### Patterns

1. **Repeated passes on one instrument, one pointer per landing.** ccclose 8 (2 ⏳ + 6 🎯/🛑);
   ccfleet 4 (1450, 1660 folded, 1740, 1820); board.py 4 (985, 987, 1670, part of 1240); leakscan
   2 ⏳ + 2 🎯 (990, 994); floor.py 3. Rule 4 says "landing = queuing", in the landing commit, so
   pass count scales with commits, not risk. Folding into one pass happened only ad hoc, by the
   principal's pick (1660→1450, 1740→RK).
2. **Re-checks of re-checks.** 1450 FAIL → RK re-check (1790) → DV/PK fixes → 1820 re-check. All
   principal-approved; the text says nothing on when a re-check is owed or when it stops.
3. **Wording-only / correction passes.** 1470 (a sync to a rule already queued as 1440), 1750,
   1760, part of 1520; 1780 now reviews a round that was withdrawn the same day.
4. **Run-sized batches.** One queue run (78ca9153) queued 14 passes in a day; 608d8123 queued 4;
   4c65083c/deeac927 queued 7 (985–992). Each landing → its own pass.
5. **The exemption is dead letter.** "Self-verifying" appears once in `docs/method/` and on the
   board only in two archived items; no live pointer weighs it. Rule 3 makes any validator, CI gate,
   template or skill "doctrine by function", and rule 4 makes self-authored doctrine "always" earn a
   cold spawn — so for anything in `tools/`, `instruments/` gates, templates or skills, rule 4
   overrides SV and a session following the text queues.
6. **Lopsided review line, confirmed:** the 18 `not warranted — <grounds>` lines on the board are
   all on hand-ups and queued build items; none is on a landed tool or doctrine change. Queuing
   needs no grounds (13 pointers give none); declining needs written grounds.
7. **"Reach" is the commonest stated grounds** and is not a criterion: the text never says whether
   blast radius alone, with tests and a fail-loud failure, earns a pass.

### Verdict on his question

**Both, mostly weak doctrine.** By count: 4 of 42 (10%) are sessions queuing what today's text
exempts (ignored doctrine — though even these cite rule 3's "doctrine by function" reading, which
the text supports); 3 the text cannot decide; 35 are what the text requires — including passes he
may judge unqualified (corrections, syncs, per-commit passes on one tool). The text is the main
cause: "doctrine text" has no materiality floor, rule 3+4 overrides the self-verifying exemption
for any rule-encoding code, nothing groups successive changes to one subject, and nothing asks for
grounds at queue time or checks them.

### Draft bar for step 2 (DRAFT — not doctrine, not ruled)

> **Before queuing a cold pass, the pointer answers three questions; a pointer that cannot answer
> the third does not queue — it carries `review: not warranted — <grounds>` instead.**
> 1. **Commitment:** what will rest on this once trusted (a rule others follow, a gate that blocks,
>    a privacy or permission boundary, an irreversible action)?
> 2. **Worst failure:** the single worst way it can be wrong.
> 3. **Why the floor misses it:** why the tests, the floor and normal use would not surface that
>    failure (it fails silent, it reads untrusted input, it narrows a grant or a detection, it
>    changes what binds). "Every child runs it" is reach, not an answer.
>
> **Never on its own:** a fix whose failure is loud (a sort, a format, an output shape, a
> tightening that reds on misuse) to an already-reviewed tool its tests cover; a wording or factual
> correction that adds no rule; a sync of a copy to a source already reviewed or queued. These
> carry `not warranted` or **fold** into the subject's next open pass.
> **One open pass per subject:** a change to an instrument or doc with an unrun ⏳ widens that
> pointer's delta instead of opening a new one.
> **Rule 3's function test decides who rules on findings, not whether a pass is owed.**
