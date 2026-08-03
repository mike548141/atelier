# Orchestrated queue run — seven workers, eight claims (2026-08-03)

Fable 5 orchestrator (Mike's per-run tier call), seven Opus workers in
isolated agent worktrees, per CONCURRENCY § Orchestrated queue runs: workers
committed code and method-doc deltas only, the orchestrator reviewed every
diff against its merge-base, owned all records (claims, harvests, `⏳`
pointers, CHANGELOG), merged per-item and pushed per-merge. Claims were
committed and pushed before dispatch (`6650b4f`); every claim closed in the
commit that landed its work. One stamp correction caught at start: the
context date read 2026-08-04 (NZ local) while `date -u` said 2026-08-03 — all
at-rest stamps use the latter.

## Landed, in merge order

- **Landing-equals-bookkeeping preamble doctrine** (`0f36356`, inline on the
  orchestrator): the `[x]`/harvest single-commit clause and the inline-claim
  close, written into the ROADMAP preamble by a session that did not author
  the candidate; enacted by its own landing commit. Rule-4 `⏳` queued.
- **E6a** (`75f52df`): the boundary posture into `SECRETS.md` — Mike's stated
  intent as the bar both scans answer to, over-flag as fail-safe, the
  leakscan/secretscan asymmetry as found-and-decided, EI5's
  rotation-presupposes-detection grounding, narrowing as the principal's
  decision, the advisory dial decided-not-built with EI1's precondition.
- **ER1–ER4 + the mid-tier promotion** (`958e59b`): the pre-flip scrub into
  AUTONOMY's making-public entry; the local-path convention's home named; the
  soft figure made approximate; RECORD's addendum-pointer convention. Plus
  ECONOMICS writes the mid tier in as standing executor (well-floored
  known-pattern builds + prescriptively-reviewed fixes; discriminator floor
  density) off the concluded third-seat trial — trial detail harvested.
- **E7, the leakscan PII-half sweep** (`bafcf93`): discharged on its fourth
  carry. Verdict: partial, materially behind the credential half — no
  label-context layer, no placeholder suppression, paths never scanned,
  binaries skipped silently; G1–G7 fix shapes ranked with cry-wolf risk,
  D1–D6 defects (D1: an allow-marker silences the term list on its line),
  and a deliberate don't-add list. All queued for Mike.
- **E6c + SF residue** (`47709df`): low variety is not innocence in
  credential-key context — the ruled six-shape probe went 2/6 → 6/6, the
  blocking set only widened, the 16-shape canary suite pins the gate. The one
  new live-tree finding (the SF verdict quoting its own specimen) was
  allow-markered with the reason in the same merge; the triage record's
  entropy aside carries its dated correction at source.
- **FS1–FS5 on floorfleet** (`10b71b6`): discovery authority beside the
  answer, three-outcome remote reads (`unknown` reds `--check`; only 404
  means "not enrolled"), token spec on every surface atelier carries, zeros
  print. Plus an out-of-scope crash fix: a repo with no floor config felled
  the board that exists to report it. Application `⏳` queued (FS1's MAJOR
  keeps the cycle open).
- **TAA + C1F residues** (`200f80b`): joined notes (the `elif` is gone),
  days-over on the floor line, C0 controls stripped at both ruled parse
  seams (floor whole-document; publishscan globs + output), the LS1 security
  test honestly rewritten for the layered guard. Terminal applications of
  closed cycles. Residue found at application and recorded live: floorfleet
  parses child configs through its own seam — a third open surface of the
  C1F3 class.
- **pointerscan + B4 wiring** (`1fbfc2e`): the FUNDED grammar build and the
  HV rulings as one build. Both detectors advisory-first and registry-wired;
  scope settled on four measured specimens; pass type ruled a lawful fourth
  pointer field (FG6 specimen clean); instance 2 located; the recorded
  counts corrected in both directions (five stale residues were seven — two
  live at HEAD; three grammar instances were 19 across history). Day-one
  proof honoured: the live findings it warned on (the ADR 0008 agenda +
  stale cycle state, the seam entry's stale state, P6's `⏳`-for-decision
  marker misuse) were fixed in the landing merge, and the scan reads clean
  at HEAD. The warn-renders-`✅ enforced` fork was handed up, recorded beside
  EP3's class, not decided.

## Numbers

Test suite 830 → **933**, all green at every merge. Floor: ten scanners →
**twelve**, all enforced, hook + CI planes green (the ROADMAP size advisory
stands, as designed). ROADMAP 2,873 → ~2,665 lines with five harvest
sections moved to ROADMAP-DONE. Four rule-4 `⏳` pointers queued (E6
application E6a+E6c · mid-tier doctrine · FS application · pointer-grammar
build + B4 wiring — all tier Fable, all refs-only, written under the new
guard's eye). No `--no-verify` anywhere in the run.

## Honest notes

- Worker reports were verified at merge: diffs read, suites re-run at the
  merged state, live scans re-run where the change widened a gate. The one
  security-test rewrite (LS1) was read line-by-line before accepting.
- ER4's two broken pointer instances live in closed/append-only records and
  stay unrewritten by design; the convention now stops the recurrence.
- The estate root still owes itself the consumer workflow's one-line
  token-spec comment (recorded as a Track B item, generic).
- E6b/E6d were deliberately not claimed: EI1/EI3 make them a
  bring-proposals-to-Mike pickup, queued for the session's question round.
- W6's changelog stamps arrived as 2026-08-04 (local-date drift, the same
  trap this session dodged at start) and were corrected to UTC at merge.
