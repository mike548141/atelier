# Ruling round — the agenda (prepared 2026-10-03, for the principal)

**What this is.** Everything on the board and in `docs/reviews/` that waits on a
ruling from the principal, sorted into sittings so that each sitting settles the
most with the least reading. Prepared by the Fable session that ran the
2026-10-03 cold passes, from two read-only inventories made the same day:

- [`2026-10-03-0357-ruling-round-agenda-board-inventory.md`](2026-10-03-0357-ruling-round-agenda-board-inventory.md)
  — the 81 open 🎯 board items, grouped by surface, with blast radius and staleness
- [`2026-10-03-0357-ruling-round-agenda-findings-inventory.md`](2026-10-03-0357-ruling-round-agenda-findings-inventory.md)
  — every unruled review finding (15 MAJOR, 101 MODERATE, ~300 minor and note),
  grouped by surface, with the clusters one ruling would settle

Both are snapshots at `306c7c2`; verify an item against the live board before
ruling on it. The six passes run on 2026-10-03 (160/430–480) add their findings
when their verdicts land; they are listed in § *Arrivals* below.

## The shape of the backlog, in one paragraph

Eighty-one board items carry a 🎯. Fifteen of them are only wrappers over review
verdicts; sixty-six are decisions in their own right, and sixty-six of the
eighty-one reach every child repo. About thirteen are already overtaken and need
only a confirmation. Beneath them, forty-one verdict files carry findings nobody
has ruled: fifteen MAJOR (twelve fleet-wide), a hundred and one MODERATE (seven
already moot), and roughly three hundred minor and note. Six MODERATE code-pass
verdicts sit in the queue although nothing in their briefs says the principal
must rule on ordinary code. Two of the principal's own rulings on one finding
(AP1) contradict each other, and three findings ask for a re-brief because the
ruling they review rested on a stale account. The queue is large mostly because
it has never been triaged; the first sitting below is that triage.

## How each sitting runs

- The presenting session prepares, per item: what it is, what it is for, the
  options, the impact of each option on atelier and on the children, and a
  recommendation marked as such. Long context goes in a completed message
  *before* the ask; the ask itself goes in the structured device
  (`COMMUNICATION.md` § *Asking for a ruling*).
- MAJORs and doctrine changes are asked one at a time. Minors and notes are
  batched with the recommendation pre-filled.
- Every ruling is recorded twice in the same commit: in the verdict file under
  `## Rulings — <date>` and on the board item. Application is queued, never done
  in the ruling sitting, and the application's cold pass is queued at landing
  (REVIEW rule 4).
- A ruling that rests on a fact (a ruleset exists, a tool is wired, a file still
  says X) is preceded by a live read of that fact in the sitting. The AP1
  contradiction below is what happens otherwise.

## Sitting 0 — Triage: shrink the queue without new judgement

Confirmations only; each is one yes. Expect the count to fall by roughly a third.

1. **Tick the moot box.** `290/070:49–51` closes CMF2, CMF5, CMF6, CMF8, RG2,
   RG3, RG6, RG8, RG9, BG14 and RP1–RP5 under the 2026-09-18 destroy ruling.
   (RG8's leftover state file still needs removing — an action, not a ruling.)
2. **Confirm overtaken items closed:** 010/100 (ruled in ros 2026-08-17),
   020/020 and 230/020 (harvestscan wired warn-only by HV1), 020/140 (every
   child ruled or done; the only owed piece is at 020/170), 020/170's D1 half,
   GA1 in 160/060 (funded as 115/080), LR2 and LR3 in 020/215 (fixed by
   `c782e14`, `1b46d05`), 310/040 (gate cleared; now an action), 010/030 (only
   nova left), 290/060's BG1 (fixed by `1b3ba12`; BG2's third branch is not).
3. **Drop the 🎯 where no decision is asked:** 020/010, 020/070 (work items),
   210/160 and 210/140's build detail ("whoever builds this decides"), 300/030
   (already ruled "looked at next").
4. **Merge duplicates:** 210/020 = 210/030; 290/060's BG3 ⊂ 160/220; 160/050's
   P6 line = 260/080. Split 160/050 into its five verdicts before any sitting
   walks it.
5. **Class ruling: code findings go back to the builder.** RC, BL, HP, LW, SP,
   FW, SW, CS, FF, and the code halves of BA, SG, FV, CC were reviewed under
   briefs with no rule-3 clause; REVIEW step 4 already lets any session fix or
   `[reject: grounds]` ordinary code. Proposed: the principal rules only the
   MAJORs and anything that changes a guard's posture, exit code or reach; the
   rest is funded as fix items for a queue run, each application earning its
   rule-4 pass. This alone removes about sixty MODERATEs from the queue.
6. **Class ruling: ratify the sixteen author-disposed files.** Fourteen passes
   from 2026-07-10 to 07-12 predate rule 3 and were dispositioned by their
   authors; every MAJOR among them is `[fixed]` and most were verified by a
   later pass. Proposed: ratify en bloc, recorded once in `160/README`.
7. **Fix the stale lines nobody owns:** `200/README:108` and `:131` still say
   "await Mike's ruling" for passes ruled 2026-08-04; the BS verdict header says
   "REVIEW NOT RUN"; the RP header says "RUNNING"; `290/070:40` is unticked.
   Records hygiene, no ruling.

## Sitting 1 — What is wrong at HEAD on a security surface

Live reads first, then rule. Each of these is a control that is either absent
or lying today.

- **AR1 + AR8 (+ 140/020, 115/180).** ADR 0008's control clause says `main` has
  no ruleset; a ruleset has been live since 2026-08-09. The two prior rulings
  (2026-08-09: ruleset with owner bypass plus a machine check; 2026-08-23: re-word
  to "not enabled") contradict each other because the second was briefed on a
  stale read. Ask: which ruling stands, then amend the ADR to the live state.
  Also fixes AR2, AR4, AR5 by consequence.
- **RC1 (+ RC3, BL2, RC8 — cluster C4).** Two hook-plane guards scan nothing and
  exit 0 under a common per-user git setting. Ask: fund the shared staged-diff
  parser (115/080 part 3) as the recurrence step, and whether to hot-fix the
  prefix flags first. The AM pass on 160/480 (allow-marker grammar, part 2) may
  bear on it — read its verdict before this sitting.
- **RU1 / NP6 + NP1 + 320/330 + PR #92 (cluster C9).** The stamped floor tells a
  private child how to file a hand-up but not the one rule that stops it naming
  itself; the precedence applied on 2026-09-19 was narrowed by the applier from
  "rule 2 wins everywhere" to "no repo token". Two closed PRs and two doctrine
  passages already carry a private child's name, and PR #92 is held on exactly
  this question. One ruling: the floor clause, the widened precedence, and
  whether doctrine prose may name a private child.
- **AB1, LK1, RC2, SP3.** Four scanner regressions from blocking to green:
  the E3 fingerprint carve-out reaches credential-keyed values; a malformed
  scoped allow-marker exempts a whole line (the AM pass tells us whether that is
  now in fourteen guards); a bare token in a URL's userinfo passes; a blocking
  finding can be listed nowhere once the 50,000 cap is hit. Ask each: fix as
  counselled, demote, or accept and pin.
- **Fleet reds the floor is about to produce.** publishscan round 2 (260/040)
  reds three private children at their next CI run — already live, no pin bump
  needed. Draft PR #97 (G3: leakscan blocks unlisted binaries) would red seven
  children's CI; it is held for the principal. Ask: land, land with a grace
  window, or hold. The PL pass on 160/470 informs the first.

## Sitting 2 — Rulings that rested on a stale briefing (cluster C3)

Three findings say the principal was asked to rule on an account that was
wrong or incomplete when it was put. Each is re-briefed from the live facts and
asked again; the prior ruling is not assumed.

- **AR8** — handled in sitting 1.
- **CC1 (+ CC10).** The ccmail delegation route was ruled "stores nothing", but
  the route signs with the cloud CLI's plaintext refresh token and the keyless
  grant still reaches every mailbox in the domain; no route's exposure to a
  compromised session is stated. Also operational: on 2026-09-26 both routes were
  down, so no session could open an attachment — the principal runs
  `ccmail --auth` and refreshes the cloud login.
- **DR1 (+ 420/010, 320/110 — the Asking cluster).** The "reached him" rule
  branches on a display mode the session cannot see; under focus mode the plain
  case reproduces the extracted-approval shape. One branchless rule is
  counselled. Rule it with the two new Asking items: when to ask at all
  (420/010) and establish-that-a-decision-exists-first (320/110).

## Sitting 3 — CONCURRENCY: the shared checkout and who talks to whom

- **Cluster C1: the dirty-sibling stop.** BA1 (MAJOR), SG2, SG3, BA3, SG8,
  SG10, SG12, 010/160, 320/120, 030/140. The twice-ruled sentence was deleted on
  2026-09-20; the relaxation now proposed says "dirty" but is true only for
  unstaged edits. One ruling on 010/160, worded "unstaged", restores the
  sentence into CF3's branch list and closes the rest.
- **SK1 + SK2 + SK3.** REVIEW rule 1 calls orchestrator-held deferral
  "structural"; on this harness a subagent can read the orchestrator's
  scratchpad. Practice has already moved (siblings held outside the scratchpad
  since 2026-09-26, including for this session's six passes); the doctrine has
  not. Ask: downgrade "structural" to "strong default with an audit trail", and
  name the read surface.
- **Cluster C15: the off-tier orchestrator.** RR2, RR5, TR1, TR2, TR3,
  320/320. Rule 4's off-tier clause is attestable but not checkable, two run-open
  surfaces omit it, and the session-open prompt has one stop where doctrine has
  two.
- **Talk first and beyond the repo.** 280/050, 360/010 (rules 1 and 2 only),
  360/020, 320/390, CH1 (280/040), CH2, CH3, CH5, HF1. The channel findings
  (CH1–CH16) have waited since 2026-08-17; 280/050 is the principal's own idea
  and its cheapest answer to 360/020.
- **200/100 (filed 2026-10-03 by the queue run):** eleven places where a doctrine
  copy contradicts its source, the sharpest being the queue-run skill telling a
  run to `pull --rebase --autostash` with no status-first gate while CONCURRENCY
  says to stop if the dirty work is a peer's. Ride with HF3 (the drift and sync
  fix never reached the skills or `pins.py`).

## Sitting 4 — The guard programme: how much, and what a guard must declare

- **115/170 first.** Is three-quarters of open work on guards the right spend?
  115/220 waits on it explicitly; 115/100, 115/120, 020/220, 320/060, 320/080,
  320/310, 020/120 and 260/050 all take their appetite from it.
- **020/240 → 020/220 → 020/230.** Does the rule-breaking ladder gain a floor
  (framing never optional; a check wherever one can see the moment), and is the
  census of which rules have a forcing function commissioned?
- **One GUARDS.md sitting:** 115/010 (evidence window), 115/120 (four-field
  declaration; carries PT1 and PW1), 320/020, 320/050, 320/030, 110/100, 400/010
  (which mechanism a new need takes), FV2 (may an allow marker reach the floor
  block). The DK pass on 160/450 (the mandate-versus-default date rule) lands
  here too.

## Sitting 5 — Visibility and naming in public trees

- **260/080 (P6) first:** the ADR on estate-internal context in public records
  has Decision and Rejected sections still empty. It frames everything below.
- **020/030 (C5) with 020/050 as one ruling**, per C5R5/C5R6; C5R1–C5R4 correct
  the item's own account before the options are put (rule on classes, not the
  frozen numbers).
- **320/380, 260/050 (P3), 390/020**, and the classes-only sweep (cluster C14:
  FF4, C5R1, CM7, CM8, BS10, BG11) under 030/070.

## Sitting 6 — PROPAGATION: membership, pointing up, the stamped floor

- **CM1–CM3**: "every repo the principal works an agent in" annexes repos he
  does not own; exclusions have no home or register.
- **The parent's half (cluster C10):** RU3, RU4, RU12 — merge-not-rebase for a
  DIRTY hand-up, an open-PR check at session start, provisional item numbers.
  RU4 was proven again on 2026-10-03: eleven PRs stood open until asked about.
- **Cluster C11, restatement drift:** DR2, AK1, AK2, RR1, RR12, RR8/AA9, PW3,
  HF2. One ruling: pointer-ise the floor's restated duties to the apex, and
  stamp or point the onramp skill, in one commit. Note DR2 and AK4 disagree on
  whether blockscan's red on the shared apex section is a defect or a false
  positive; the CU pass on 160/430 bears on it.
- **Routes beyond atelier:** 310/120, 310/140 (the key fork: a PR files an idea
  or carries a fix), 310/130, 310/020, 410/010, 390/010.
- **Board vocabulary:** 310/060 (also settles 010/100 and 310/070), BG3 (the
  generated index and wrapscan — "needs Mike's own answer"), BS3, BS5.

## Sitting 7 — How we work: one-liners, records, the apex

- **"Does this earn a line, and where?"** 330/010, 350/010, 370/010, 380/010
  (rule with 350), 340/010, 220/010, 220/020, 320/070 → 320/080 (same commit),
  320/100, 115/020, 200/030, TD1.
- **RECORD (cluster C16):** RF1 (MAJOR, open since 2026-07-26: the reason given
  for the pushed-floor all-clear is wrong), RF2–RF5, CR1, CR2 (the prescribed
  re-run can cancel a peer's run).
- **Apex wording (cluster C18):** AA1–AA5, AA8–AA13, RR1, RR12, LR5.
- **COMMUNICATION after plainscan (cluster C12):** HF4, CMF3, CMF4, RG1, RC12,
  DR4 — one history-recasting sweep.
- **160/120:** the glossary ratify pass, the principal reading `GLOSSARY.md` end
  to end.

## Sitting 8 — Tools and instruments that survive sitting 0's class ruling

- BG3 (above), 020/350 (bidi characters in a board `why`), 020/040 (a third
  scanner verdict state), 020/120 (flip signscan to blocking; pairs with key
  rotation), 320/060, 320/310 (waits on 320/010), 115/220 (waits on 115/170).
  (Pull request 96, pathscan class C, was ruled and merged on 2026-10-03; its
  cold pass is PX.)
- Instruments: 210/030 (ccarchive encryption: counsel is `age` with in-process
  decrypt), CC2–CC4, CS1–CS3, FF1, and the MC and CP passes on 160/460 and
  160/440 when they land.

## Arrivals — the six passes run on 2026-10-03

Verdicts are under `docs/reviews/2026-10-03-*-cold.md`. Four new MAJORs; three
cycles stay open.

| Pass | Item | Overall | Cycle | Joins sitting |
| --- | --- | --- | --- | --- |
| CU | 160/430 stampscan cover switch, blockscan unmapped headings | 0 MAJOR · 1 MODERATE · 6 minor · 3 note | closed | 6 (with FV1–FV3, ST3) |
| CP | 160/440 cctranscript archive-pool speedup | 0 MAJOR · 1 MODERATE · 3 minor · 6 note | closed | 8 (CP9 = CS2, CP4 ⊃ CS11: rule once) |
| DK | 160/450 the mandate-versus-default date rule | 1 MAJOR · 3 MODERATE · 7 minor | OPEN | 4 |
| MC | 160/460 ccarchive manifest checkpoints | 2 MAJOR · 2 MODERATE · 4 minor · 2 note | OPEN | 1 |
| PL | 160/470 publishscan round 2 | 1 MAJOR · 5 MODERATE · 4 minor · 6 note | OPEN | 1 |
| AM | 160/480 shared allow-marker grammar | 0 MAJOR · 5 MODERATE · 4 minor · 4 note | closed | 1 (AM2 = LK1) |
| PX | 160/490 pathscan brace expansion | running at this file's last edit | — | 8 |

The four MAJORs, one line each:

- **MC1** — ccarchive's new heal refreshes the manifest from the source, not the
  mirror: a truncate-then-append with a preserved mtime slips the 2026-07-17
  shrink guard and overwrites the good archive copy with `--verify` green. The
  ruled F1 re-opened by a side door. Sitting 1, first: this is the only durable
  copy of the transcripts.
- **MC2** — pre-existing, surfaced by a real hard kill: mirrors are written in
  place, so a torn archive gets a newer mtime, is never re-archived, and makes
  `--verify` crash.
- **PL1** — pre-existing: git's default path quoting hides any listed file
  under a folder with a non-ASCII name from publishscan on both planes. The
  third sighting of one seam (BA2, SG1 on `board`); one shared NUL-delimited
  listing helper closes all three.
- **DK1** — the date-kind rule asks for a kind a child can read beside the
  date, but the floor config parser refuses any key beside `why` and
  `review-by`; by GUARDS.md's own homing test it is not yet a rule.

Severity handed up: **AM2** — LK1's fail-open on a malformed scoped marker is
now one shared function in seven scanners, both boundary guards among them; the
reviewer held MODERATE and says the case for MAJOR is stronger than when LK1
was filed.

A process finding four of the six passes recorded independently (CP1, DK8,
MC8, PL5, AM11): the review worktree was cut one commit before four of the
deltas landed, so reviewers met pre-delta code until the orchestrator merged
`main` in. Each recovered and disclosed. The seventh brief tells its reviewer to
confirm the delta is present first; the rule-shaped version of that is a
candidate line for REVIEW.md's lifecycle (sitting 3 or 7).

## Things with a clock on them

- ⏳ **FLOORFLEET_TOKEN expires 2026-10-27.** Renewing it is a human step
  (`030/README:149`).
- ⏳ **ccmail had both routes down on 2026-09-26** (CC10). Until the principal
  re-authorises, no session can open a mail attachment.
- 🚩 **Three private children go red on publishscan at their next CI run**
  (260/040). That is the floor working; it will look like breakage.
- 🚩 **PR #92 is held** on a privacy question; **PR #97** (leakscan blocks
  unlisted binaries) **is a draft held for a ruling** — landing it reds seven
  children's CI.
