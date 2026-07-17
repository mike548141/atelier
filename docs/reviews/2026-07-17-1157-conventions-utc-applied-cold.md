# Cold review — CONVENTIONS + UTC-at-rest ADR, the F1–F6 applied batch

**Scope:** the CONVENTIONS/UTC doctrine hunks of application commit `e6a295e`
(2026-07-17) — the rulings of the first cold pass applied:
`docs/method/CONVENTIONS.md` (the Date & time row as the declared three-shape
house profile; label strength), `docs/method/RECORD.md` (UTC minting +
absolute-dating), `docs/method/CONCURRENCY.md`, `docs/method/PROPAGATION.md`,
`docs/build/REPO-STANDARD.md` (the UTC/canonical-block hunks only),
the three child templates (`docs/build/templates/CLAUDE.md`,
`…/templates/docs/decisions/README.md`, `…/templates/docs/reviews/README.md`),
and the dated addendum to
`docs/decisions/2026-07-15-1327-timestamps-utc-at-rest.md`. Review the edited
doctrine **at HEAD** plus those hunks. The core question of an applied-batch
pass: **does the new wording faithfully implement the principal's rulings —
no drift, no overreach, no silent miss — and is it sound doctrine in its own
right at HEAD?** The identifier-minting claim has a definite shape: the six
minting sites are claimed to now say UTC (`date -u`, ADR pointer), templates
via the canonical block with a drift test.

Out of scope: the CLI-docs and ccarchive hunks in the same commit (separate
cycles — one queued for its own pass, one CLOSED). Record hunks (`ROADMAP`,
`SESSIONS`, session/review files) are context, not target — but see
sequencing: the review-file hunks stay closed until your findings are
committed.

**Sequencing (REVIEW.md rules 1–2, application-review form):** (1) read this
brief **only above the first `---` divider** (use a limited read); (2) review
the doctrine at HEAD and the scoped delta, naming and attacking the
load-bearing assumptions yourself, and **write your attack surface and findings
durably into the verdict section of this file first**; (3) only then open the
deferred section below the divider, the prior verdict + `§ Decision` in
`reviews/2026-07-17-1000-conventions-utc-at-rest-cold.md`, and the intent
record `sessions/2026-07-17-0958-three-queued-cold-reviews-taken.md` —
reconcile, never anchor: check the application implements each ruling as
decided. An application review cannot fully honour rule 2 (the delta carries
the prior verdict's decision stamps); that residual exposure is named, not
denied — keep those hunks unopened until your findings are committed.

**Spawn provenance (rule 4, tested against the delta's author — the applier):**
this brief is written by a **non-author** taking session that Mike (the
principal) opened fresh and pointed at the queue ("do any review work queued");
the applier session (Fable, intent record above) neither started nor instructed
the taking session or this reviewer. The reviewer is a cold spawn of the taking
session, which authored neither the doctrine, the prior verdict, nor the
applied delta. Disclosure: the taking session read the intent record (which
includes application highlights) to scope this brief, but not the prior
CONVENTIONS verdict's findings; above-the-divider text is kept to scope and
refs. The verdict must repeat this provenance.

**This is self-authored doctrine (by function):** all findings are the
principal's to decide (rule 3) — record counsel per finding, labelled as the
reviewer's counsel; apply nothing.

**Re-run live proofs in scope:** the application claims 247 tool tests green,
the template/canonical-block drift test green, the scan set clean (secretscan ·
leakscan structural + local · licenscan · linkscan · sizescan), and that the
six minting sites now instruct UTC. Re-run what falls in scope; verify the
minting-site claim by reading each site, and the templates against the
canonical block.

**Run all three lenses** (approach & assumptions · correctness/honesty ·
completeness/harvest), deep not fast; findings get stable IDs (F1…) with
severity MAJOR/MEDIUM/LOW. Append your verdict to this file below the second
`---` divider.

---

## Deferred — refs (open only after your attack surface and findings are committed)

No seed questions were queued this time (the `⏳` pointer was refs-only, per
spec). Refs for the reconcile step:

- Prior verdict + rulings:
  `docs/reviews/2026-07-17-1000-conventions-utc-at-rest-cold.md` (findings
  F1–F5 + the principal's own F6, reviewer's counsel, and `§ Decision` — Mike
  ruled F1–F5 as counselled and F6 "make all the changes as you counselled").
- Intent record: `docs/sessions/2026-07-17-0958-three-queued-cold-reviews-taken.md`
  (the taker/applier's account, including its application highlights — the
  author's claims to test, not settled scope).

---
