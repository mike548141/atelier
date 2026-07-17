# 2026-07-17 · 1340 UTC · the two queued applied-batch cold passes run (Fable)

## Trigger

Mike opened a fresh session: "do any review work queued". Two `⏳` items sat
in *Doctrine — review-owed* — the applied-batch cold passes the applier
session (2026-07-17-0958) queued under rule 4 after applying the CLI-docs
F1–F7 and CONVENTIONS/UTC F1–F6 rulings in commit `e6a295e`. This session is
a valid rule-4 taker for both: the applier session neither started nor
instructed it.

## What happened

1. **Claimed before working** (CONCURRENCY § Claiming work): both `⏳` lines
   stamped in one direct-to-`main` commit (`c10f73e`). Solo session, no
   parallel work live, so trunk-based on `main` per the solo default — no
   worktree.
2. **Two briefs written by the taker** (rule 4), application-review
   sequencing per REVIEW.md: findings committed durably before the prior
   verdict's `§ Decision` stamps, the deferred refs, or the intent record are
   opened; the rule-2 residual exposure named. The `⏳` pointers were
   refs-only this time — no seed questions (the prior batch's disclosure,
   closed). Taker exposure disclosed in each brief: the intent record (and,
   for CLI-docs, the prior verdict) had been read to scope the brief.
3. **Two cold reviewers spawned in parallel** (background agents, Fable —
   cold spawns of the taking session). Both were **cut mid-run by the Claude
   session limit** (reset 0130 Pacific/Auckland = ~1330 UTC) and resumed
   with context intact on Mike's "pick up where you left off": the
   CONVENTIONS reviewer had its verdict durably written through the proofs
   section and owed only the reconcile; the CLI-docs reviewer had run proofs
   but written nothing durable, and wrote attack surface + findings before
   opening any deferred material. Interruption and resume are part of the
   provenance trail; neither reviewer opened deferred material out of
   sequence (each verdict carries its own disclosures).
4. **One taker correction at commit:** the CONVENTIONS verdict heading
   originally stamped the local date as UTC ("2026-07-18 (UTC)") — corrected
   to 2026-07-17 with the correction named in the heading. No reviewer
   judgement was touched.

## Verdicts — both PASS-WITH-FINDINGS, 0 MAJOR, nothing applied

| Review | Result | Sharpest finding |
|---|---|---|
| CLI-docs applied batch (F1–F7) | 0 MAJOR · 2 MEDIUM · 3 LOW; all seven rulings implemented faithfully | F1: the man page's `EXIT STATUS` predates all four new non-zero exit paths — the full-reference register no longer covers what the tool does |
| CONVENTIONS/UTC applied batch (F1–F6) | 0 MAJOR · 1 MEDIUM · 5 LOW; six rulings implemented, one reconcile-stage drift | F1: a seventh identifier-minting site (`REVIEW.md:157`) carries no UTC note — the "six sites" enumeration was asserted, not derived; F6: prior-F6's counselled foreign-formats line was silently dropped |

Verdicts, attack surfaces, provenance, disclosures, and per-finding counsel:
`reviews/2026-07-17-1157-cli-docs-applied-cold.md`,
`reviews/2026-07-17-1157-conventions-utc-applied-cold.md`.

Every recorded proof re-ran green in both reviews: 247 tool tests · 75
instrument tests (incl. the superset drift test) · the template/canonical
drift test (character-for-character) · `mandoc -T lint` clean · the five-scan
set clean on a clean HEAD export (secretscan · leakscan structural **and**
local · licenscan · linkscan · sizescan) · a fresh installer drive in
throwaway XDG dirs (stale owned links removed, foreign links and real files
kept, idempotent) · live `~/.local/bin` residue confirmed gone · the MANPATH
claims verified empirically · the six UTC minting sites read at HEAD.

## Owed

**Both rulings are Mike's (rule 3 — self-authored doctrine):** two 🎯 ROADMAP
items point at the verdicts (CLI-docs F1–F5; CONVENTIONS F1–F6). Nothing was
applied; reviewer's counsel is recorded per finding. **Both passes returned
0 MAJOR, so each cycle closes on Mike's ruling** (close rule) — what he
declines to fix is decided into the backlog, and the terminal application
spawns no further ceremony.

## Housekeeping

The stale `.claude/worktrees/fable-review` worktree (previous session's,
zero unique commits, flagged by both reviewers as working-tree scan noise)
removed; claims released with this landing (`⏳` → 🎯).
