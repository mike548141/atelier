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

## Verdict — cold reviewer, 2026-07-17 (UTC; the heading originally read 2026-07-18 — the local date mis-stamped as UTC, corrected by the taker at commit)

**PASS-WITH-FINDINGS — 0 MAJOR · 1 MEDIUM · 5 LOW** *(amended at reconcile:
originally written as 4 LOW before the deferred refs were opened; F6 below was
found by the reconcile step and added transparently — no pre-reconcile finding
was altered)*. The applied wording is
sound doctrine at HEAD and every recorded proof re-ran green. Findings are the
principal's to decide (rule 3); counsel per finding is labelled as the
reviewer's counsel. Written before the deferred refs' targets, the prior
verdict, or the intent record were opened; the reconcile section below was
added after.

### Provenance (repeated per the brief) and disclosures

Provenance: this reviewer is a cold spawn of the taking session, which Mike
opened fresh and pointed at the queue; the taking session authored neither the
doctrine, the prior verdict, nor the applied delta, and the applier session
neither started nor instructed the taking session or this reviewer.

Disclosures, in the order they happened:

1. **Brief overshoot** — the limited read ran to line 70, four lines past the
   first `---` (line 66): I saw the deferred heading and the partial sentence
   stating no seed questions were queued. Nothing else below the divider was
   read at that point.
2. **Commit-message exposure** — scoping the delta required `git show e6a295e`,
   whose message carries the applier's own application highlights. Unavoidable
   for an applied-batch pass; treated as claims to test, not scope.
3. **SESSIONS.md tail exposure** — checking whether practice matches the
   declared prose-stamp shape meant reading the index tail, whose entries
   summarise the prior verdict's finding counts and the rulings. This happened
   *after* the attack surface and findings F1–F5 below were formed (the tool-call
   sequence evidences it); no finding below originates there.
4. **Deferred-refs exposure** — locating the append point for this verdict
   meant reading the file tail (lines 70–81), i.e. the deferred section. It is
   refs-only (both paths were already named above the divider) plus a one-line
   rulings summary; no seed questions. Findings were fully formed first.

### Attack surface — the load-bearing assumptions, named

1. **The six-site enumeration is complete** — every doc that instructs minting
   a record identifier now says UTC. (Attacked by an independent sweep for
   `HHMM`/`<date>-`/slug minting instructions across `docs/`, `skills/`,
   `commands/`, `instruments/`, root files. Result: F1 — a seventh site.)
2. **The recorded proofs are re-runnable at HEAD** — 247 tool tests, the
   template/canonical drift test, the five-scan set. (All re-ran green; see
   proofs below.)
3. **The three-shape house profile is internally coherent, consistent with the
   Time row and the ADR, and matches practice at HEAD.** (Holds: the strict-ISO
   claim about zone-less stamps meaning local time is correct per ISO 8601; the
   key-shape rationale — hyphen for `T`, colon dropped as filename-hostile — is
   accurate; SESSIONS.md's own entries use the labelled `YYYY-MM-DD · HHMM UTC`
   shape.)
4. **The ADR addendum's two worked cases are factually right.** (Both hold:
   the ADR self-documents its `1327` as UTC minted while the wall clock read
   07-16, so a UTC key genuinely can sort before a local afternoon key minted
   earlier in real time; the bare-prose-date-is-UTC consequence matches
   RECORD's new absolute-dating sentence.)
5. **The canonical block and the template stamp are character-identical and
   mechanically pinned.** (Holds: `test_stamped_block_matches_canonical` green;
   block text at PROPAGATION.md:83–122 and templates/CLAUDE.md verified.)
6. **Post-ruling practice lives the doctrine.** (Holds: the taker's own records
   — briefs `2026-07-17-1157-*` committed 2026-07-17T11:57:56Z, claim commit
   at 11:56Z, session log `0958` — are UTC-minted within a minute of their
   identifiers; the prose stamps in the index tail are date + `HHMM UTC`.)

### Findings

- **F1 (MEDIUM) — a seventh minting site exists, unannotated:
  `docs/method/REVIEW.md:157`.** The lifecycle's step 1 instructs writing a
  brief to `docs/reviews/<date>-<HHMM>-<slug>.md` with no zone note — and it is
  the one minting instruction reviewers actually follow when opening a cycle.
  The applied claim ("the six identifier-minting sites now say UTC") is true of
  the six it names, but the enumeration itself is what a reader will trust, and
  the same logic that got `RECORD.md`'s session-file site annotated (it too
  merely referenced CONCURRENCY's rule) applies here unchanged. Mitigation:
  REVIEW.md states no zone at all, so a reader who follows CONCURRENCY gets
  UTC — this is a completeness miss, not a contradiction, hence MEDIUM not
  MAJOR. *Counsel: add the same `in UTC (`date -u`)` clause to REVIEW.md:157,
  and stop counting — sweep with `grep -rn 'HHMM' docs/` whenever the claim is
  "all minting sites", so the number is derived, not asserted.*
- **F2 (LOW) — the change that redefined a declared default is not dated where
  the doc's own rule demands.** CONVENTIONS' maintenance bullet says "when a
  default changes, date the change here"; the Date & time format row was
  materially re-declared (bare "ISO 8601" → the three-shape house profile) with
  no date in the doc, and the CHANGELOG's newest dated entry is 2026-07-14 —
  the 2026-07-17 doctrine change is recorded only in the ADR addendum, the
  verdict files, and git history. *Counsel: either add a dated parenthetical to
  the row (or a CHANGELOG entry for the applied batch), or soften the
  maintenance bullet to name the ADR/addendum as the sanctioned dating home —
  as written, the doc's first material change broke its own rule.*
- **F3 (LOW) — the ingestion aside is an estate-wide absence claim the repo
  cannot verify.** "(No live ingestion surface exists in the estate yet…)" is
  true only while private facts stay a particular shape, and nothing will
  prompt this line's update when the first surface appears. *Counsel: scope it
  to what the doctrine can see — e.g. "none of the repos under this doctrine
  has one yet" — or accept it deliberately as a dated proving-ground marker.*
- **F4 (LOW) — mechanical insertion left ragged wrapping at two sites.**
  `docs/method/RECORD.md:67–68` ("in UTC (`date -u`) — ADR 2026-07-15; the")
  and `docs/build/REPO-STANDARD.md:111–112` break mid-clause with short
  orphan lines — the UTC clause was spliced in without reflowing the
  paragraph. Cosmetic. *Counsel: reflow the two paragraphs.*
- **F5 (LOW) — CONCURRENCY's "same-day records keep their order" is now a
  steady-state claim with an unnamed exception.** Across the boundary era the
  ADR addendum accepts sort inversion, but a CONCURRENCY reader sees the
  ordering claim with no pointer to the exception. *Counsel: acceptable as-is
  (forward-only, all-UTC keys do keep order); a three-word pointer to the ADR's
  addendum would close it if wanted.*

### Proofs re-run — all green

- **247 tool tests**: `python3 -m unittest discover -s tools -p 'test_*.py'` →
  `Ran 247 tests … OK`.
- **Template/canonical drift test**: `tools.test_templates` → 12/12 OK,
  including `test_stamped_block_matches_canonical` (character-for-character).
- **Scan set on a clean HEAD export** (git archive to scratchpad): secretscan
  clean · leakscan clean (**structural + local** — the machine-local term list
  loaded) · licenscan clean (Apache-2.0, all declarations agree) · linkscan
  clean · sizescan clean. Note: run against the *working tree* the scans flag
  only the untracked stale `.claude/worktrees/fable-review/` copy (scanner
  fixtures at unignored paths) — environmental residue, not repo content; the
  committed tree is clean. The six scanner selftests also pass.
- **The six minting sites read at HEAD, each instructing UTC**:
  `docs/method/RECORD.md:67–68` · `docs/method/CONCURRENCY.md:108` ·
  `docs/build/REPO-STANDARD.md:111–112` · `docs/build/templates/CLAUDE.md:39`
  (via the canonical block, whose source `docs/method/PROPAGATION.md:107` also
  says it) · `templates/docs/decisions/README.md:12–13` ·
  `templates/docs/reviews/README.md:24–25`.

### Reconcile — written after opening the prior verdict, `§ Decision`, and the intent record

Checked ruling by ruling: does the application implement each as decided?

| Prior finding | Ruled | Applied as decided? |
|---|---|---|
| F1 (MAJOR) — six minting sites stale | fixed as counselled | ✅ **Faithful.** All six sites verified at HEAD saying UTC (`date -u`); RECORD/CONCURRENCY/REPO-STANDARD and both README templates carry the ADR pointer. One recorded, sensible narrowing: the canonical block (`templates/CLAUDE.md` via PROPAGATION) carries zone + `date -u` but no ADR pointer — `§ Decision` names the canonical-block route, the counsel itself noted a child never reads atelier's ADRs, and an ADR path in a child block would dangle. Not drift. |
| F2 (LOW) — label-strength mismatch | fixed as counselled | ✅ Row reads exactly the counselled "local on presentation, labelled where doubtable". |
| F3 (LOW) — prose-date corollary unstated | fixed as counselled | ✅ Landed as a dated ADR addendum rather than an edit to Consequences — the *more* correct shape (append-only ADR lifecycle), and `§ Decision` records it. RECORD's absolute-dating sentence carries the ADR pointer. |
| F4 (LOW) — ingestion clause instance-less, unmarked | fixed as counselled | ⚠️ **Substantially faithful, one residual.** The counselled half-line is in CONVENTIONS clause 3 verbatim, matching `§ Decision`'s record. But the sentence the finding actually quoted — the ADR consequence "Foreign-data ingestion must carry a zone-metadata field", operational present tense — remains unmarked in the ADR. Within the ruling's letter as recorded; noted, no severity. |
| F5 (LOW) — sort inversion implied, unstated | fixed as counselled | ✅ Addendum names it; I verified the worked case independently before opening the refs (the ADR's `1327` is self-documented UTC; the inversion arithmetic holds). |
| F6 (LOW, principal-raised) — ISO row undeclared profile | fixed as counselled | ⚠️ **Three of the four counselled lines applied; the fourth dropped, unrecorded** — see new finding F6 below. |

Reconciliation with my own findings: my F1 (the REVIEW.md:157 seventh site) is
*not* an application-fidelity failure — the prior verdict's F1 enumerated
exactly six sites and the application implemented exactly those six faithfully;
the miss lives in the enumeration both passes inherited, which sharpens my F1's
counsel (derive the list by sweep, don't assert a count). My F3 critiques the
wording of a *ruled* insertion ("the estate" scope is the applier's choice, not
Mike's — the counsel specified the half-line's content, not that phrase); it
stands as counsel on the applied wording. My F2, F4, F5 were not raised in the
prior pass and stand unchanged. Nothing in the refs caused any pre-reconcile
finding to be withdrawn or reworded.

**F6 (LOW) — application drift on prior-F6: the counselled foreign-formats
line was dropped without a record.** Mike ruled prior-F6 "make all the changes
as you counselled", and the taker's counsel had four elements: the three
shapes *plus* "foreign formats (ssh-keygen) kept as-is under clause 3". The
applied row declares "Three declared shapes" and never mentions foreign
formats; `§ Decision`'s F6 entry likewise records only the three shapes, so
the narrowing is silent — neither a recorded decision nor a stated deferral.
Consequence at HEAD: SIGNING's `valid-after="20260711Z"` — the very example
prior-F6 named — is again a deviation from the declared profile with no named
home in the row, the exact anti-pattern class the row was rewritten to close
(rule 3 covers it generically, which is why this is LOW, not MEDIUM).
*Reviewer's counsel: either add the counselled fourth line to the row ("foreign
formats — e.g. ssh-keygen's own syntax — kept as received under rule 3"), or
record the narrowing in the prior verdict's `§ Decision` with grounds. The
class matters more than the instance: an applied-batch record that silently
implements less than the ruling is the drift this pass exists to catch.*

*Reconcile written 2026-07-17 (UTC; originally mis-stamped 2026-07-18 — the
local date — corrected by the taker at commit) by the same cold reviewer; files touched:
this brief only (appended + the headline count amended transparently). No
commits, no pushes.*

---

## Decision — 2026-07-17, ruled by Mike (principal)

Mike ruled **F1–F6 all [fixed] as counselled** ("agreed — apply as
counselled", 2026-07-17). Applied the same day by the taking session (authored
neither the doctrine nor this verdict; the reviewer was its cold spawn). What
was applied:

- **F1** — the seventh minting site annotated: `REVIEW.md` lifecycle step 1 now
  carries `(`HHMM` in UTC — `date -u`, ADR 2026-07-15)`. The counsel's
  derive-don't-assert rule holds for any future "all minting sites" claim
  (sweep `grep -rn 'HHMM' docs/`).
- **F2** — the Date & time row now dates its own re-declaration ("re-declared
  2026-07-17 from a bare 'ISO 8601' — the ADR's addendum records why"),
  satisfying CONVENTIONS' own maintenance rule in-doc.
- **F3** — the ingestion aside scoped to what the doctrine can see: "No repo
  under this doctrine has a live ingestion surface yet".
- **F4** — both spliced paragraphs reflowed (`RECORD.md`, `REPO-STANDARD.md`).
- **F5** — CONCURRENCY's ordering claim now points at the accepted boundary-era
  inversion in the ADR's addendum.
- **F6** — the dropped fourth line restored to the row: foreign formats (e.g.
  ssh-keygen's `YYYYMMDDZ`) kept as received under rule 3, frame recorded
  alongside — closing the silent narrowing this pass caught.

Also corrected by the taker, named in place: the verdict heading and reconcile
footer had stamped the local date (2026-07-18) as UTC.

Verified after applying: 247 tool tests (incl. the template drift test) · 75
instrument tests · sizescan · linkscan all green.

**0 MAJOR at the pass ⇒ CYCLE CLOSED** (close rule): this terminal
application queues no further pointer.
