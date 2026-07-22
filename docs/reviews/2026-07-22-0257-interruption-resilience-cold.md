# Cold pass — interruption-resilience doctrine (delta `9c11525`)

- **Date/time**: 2026-07-22 0257 UTC
- **Spawn provenance (rule 4)**: taken from the ROADMAP `⏳` queue by the
  session Mike opened with "please do any review work" (continued after it
  closed the scope/lens-4 cycle). The delta's author was a sibling session,
  now closed, which neither started nor instructed this one; this session
  authored none of `9c11525` or its records. Claim `e0450ee` on `main`
  first; brief taker-written.
- **Named exposure**: before claiming, this taker had read (a) the claim
  commit `f59b1da`'s body — which names the three gaps as ratified ("the
  resume-state carrier missing at the cut, decision-limbo, and lifting the
  cmd+Q recovery procedure into method") — and (b) the tail of the ROADMAP
  gap-analysis section (Gap 3's full text), both incidentally while
  resolving mid-pass concurrency during the prior review. That is author
  framing this reviewer cannot un-read: the *problem statement* arrived
  warm. Mitigation: the framing names the gaps, not the encoding — the
  review attacks how the delta encodes them, where the author's account has
  not been read (the intent record, the commit body, and Gaps 1–2's
  analysis stay deferred until findings are committed). The diff is read
  via `git show --format=` so the body stays unseen.

## What the work is (refs only)

Delta `9c11525` (2026-07-22), at HEAD:

- `docs/method/CONCURRENCY.md` — a new section on surviving an interrupted
  session (+61 lines)
- `CLAUDE.md` — an onramp firing pointer to it (+5/−1)

Method doctrine by function — governs every future session's behaviour at
and after a cut — so the full rule-4 ceremony applies, and rule 3 puts all
decisions with Mike.

## Ask

Run all four lenses; scope is the whole commitment.

1. **Approach & assumptions** — name the load-bearing assumptions first.
   Is per-cut resilience the right frame, and is doctrine prose the right
   mechanism (vs a tool/checklist artefact)? Does the new section overlap,
   contradict, or duplicate what CONCURRENCY, RECORD, or the onramp already
   require? Is the firing condition actually findable at the moment it
   must fire — by a *resumer* session that doesn't know a cut happened?
2. **Correctness & quality** — does the text do what it claims; is every
   grounded claim real (the section will cite incidents/sessions — re-run
   or re-verify what is re-runnable, e.g. any commands the recovery
   procedure prescribes, against a live repo state); honest about what is
   doctrine vs hope.
3. **Completeness / harvest** — the pointer's flagged sub-question: should
   the template CLAUDE.md onramp carry the same died-mid-flight→sweep
   pointer so the firing condition propagates to children? Also: does the
   new section reach the surfaces that already describe session close
   (RECORD, the session-onramp skill, templates), or does it create a
   second telling that will drift?
4. **Security & privacy** — reach per shape: landed-delta, markdown-only —
   the harness scanner cannot genuinely be aimed at it; discharged on
   those grounds, per REVIEW.md lens 4. Manual pass: does the recovery
   procedure it prescribes (reflog sweeps, stash inspection, orphan
   worktrees) risk exposing or publishing another lane's in-flight
   content, and does the text guard that?

Live proofs: the repo floors at HEAD; any command sequence the section
prescribes, executed against this repo where safe; the CLAUDE.md pointer's
link target resolving (linkscan) and its firing grammar tested against the
reader who needs it.

Cycle context: first cold pass of this cycle — findings get IDs (IR1, …)
with severities; decisions are Mike's (rule 3); MAJORs present would keep
the cycle open past application.

---

## Deferred material (open only after findings are committed)

- `docs/sessions/2026-07-22-0245-interruption-resilience-doctrine.md`
  (intent record, incl. its addendum re the gitlink incident)
- The ROADMAP gap-analysis section (Gaps 1–2 unread portions)
- Commit bodies of `9c11525`, `b4b5142`, `c258451`
- The author seeded no questions beyond the pointer's flagged sub-question,
  which is carried in the Ask above; everything here is taker-written.

---

## Verdict — PASS-WITH-FINDINGS, 0 MAJOR · 2 MEDIUM · 2 LOW (committed before any deferred material was opened)

**Provenance restated (rule 4):** the Mike-spawned taker session; authored
none of `9c11525` or its records; the intent record, Gaps 1–2's analysis,
and all commit bodies remain unread at this point. Diff read via
`git show --format=`. Subject pinned at `9c11525` on ref `e0450ee`.

### Attack surface (named as the first act)

- **A1 — the onramp tell licenses the right conclusion.** FALSIFIED in the
  live case — see IR1. The tell's *mechanics* are sound (clean closes do
  leave closing entries here — verified against the session log's recent
  history); its stated *inference* is not.
- **A2 — the sweep is executable and correct.** CONFIRMED by running it
  live on this repo mid-review: tree clean, stash list empty, every
  worktree accounted to a live lane, reflog legible against the last
  logged close. All five rows are checkable with plain git; none requires
  state a cut would have destroyed.
- **A3 — every § cross-reference resolves.** CONFIRMED by heading grep:
  Integration hygiene, Claiming work, Orphan claims (bold run-in),
  Stay in your lane, Every branch ends put away, RECORD.md § Why this is
  doctrine — all real anchors at HEAD.
- **A4 — the decision-limbo move contradicts nothing.** CONFIRMED: writing
  the open question to the claim/roadmap line before blocking is the same
  durability RECORD already demands of session close; chat-asks/record-
  remembers adds a rule where none stood.
- **A5 — no second telling to drift.** CONFIRMED: the session-onramp skill
  does not restate the read-order (no parity surface); RECORD and
  CONCURRENCY are cited, not copied. The one surface that *does* restate
  the read-order — the child CLAUDE.md template — is IR2.

### Lens 4 — security & privacy (scanner discharged with grounds)

Landed-delta, markdown-only: `/security-review` cannot genuinely be aimed
at it — discharged per REVIEW.md lens 4. Manual pass: the sweep is
read-first by construction and lane-guarded ("another session's recovery
is not yours to run"); it prescribes no command that publishes, and
recovery-committing a stranger's stranded work — the real exposure in this
territory — is explicitly barred by the change-nothing rule. The pre-commit
scanner floor still covers anything a recovery session does choose to
commit. No new surface.

### Findings

- **IR1 (MEDIUM, correctness at the point of use)** — `CLAUDE.md` step 4:
  "A last commit then silence with **no closing entry** means the last
  session died mid-flight, not closed clean." The inference is wrong by
  this doctrine's own flipped prior: a **live parallel session** produces
  the identical signature — and did, during this review (claim `e0450ee` +
  brief `d9c140d` landed after this session's last closing entry, session
  very much alive). CONCURRENCY's own text hedges correctly ("a
  live-*looking* branch with no closing log entry" → *possible*
  interruption residue → read-first sweep); the onramp compression
  escalates "possible" to "means", teaching a resumer to conclude *death*
  where the evidence supports *death or live sibling* — and a resumer who
  believes "died" is primed to reclaim claims or tidy "orphan" state that
  belongs to a live lane. Mitigation already present: the sweep is
  read-first and the reclaim-on-evidence rule guards the worst act. Same
  family as SL1/F3 — the point-of-use copy diverging from the parent —
  but as overclaim, not omission. *Counsel: one-line reword — "means the
  last session either died mid-flight or is still live — run the
  read-first sweep… before assuming either".*
- **IR2 (MEDIUM, completeness — the author's own flagged sub-question)** —
  the child CLAUDE.md template carries the same onramp step ("Tail of
  `docs/SESSIONS.md` — where the last session left off") with no firing
  pointer, so children inherit the onramp without the tell — the firing
  condition doesn't propagate. *Counsel: yes, propagate — one sentence in
  the template pointing at `<atelier-path>/docs/method/CONCURRENCY.md`
  § Surviving an interrupted session (the doctrine is reachable via the
  pinned path), worded per IR1's corrected inference; lands at next pin
  bump like every template change.*
- **IR3 (LOW, wrap hygiene)** — two lines materially over the 80-col
  house wrap: the claim-breadcrumb aside at `CONCURRENCY.md:197`
  (~153 cols) and the orphan-worktrees table row (~109 cols). Ambient
  tolerance runs 81–85; these are the third shipping of the wrap class in
  three cycles (SL7, AC1, IR3). *Counsel: rewrap the aside; the table row
  can split its parenthetical to a footnote line — or accept table rows as
  a named exception if Mike prefers.*
- **IR4 (LOW, grammar propagation)** — the resume breadcrumb
  (`· at: export path unverified`) extends the claim-line grammar, but the
  ROADMAP header legend — the point-of-use surface that defines claim-line
  grammar — still shows only `(claimed <date>-<HHMM>, wt: <branch>)`.
  *Counsel: extend the legend by half a line, or leave and accept the
  breadcrumb as free-form; either is coherent, but say which.*

### Live proofs

Sweep exercised end-to-end on this repo (A2). Suite + floors re-run at
HEAD: recorded below after the run. The onramp pointer's link target
resolves (linkscan green on every commit this pass made).

No MAJOR. Rule 3: IR1–IR4 are Mike's to decide; counsel recorded per
finding. Per the close rule a no-MAJOR pass closes the cycle — the
decided fixes apply without another full ceremony.

### Finding added at the floor re-run (still pre-deferred)

- **IR5 (MEDIUM, records hygiene — the shared floor is red on `main`)** —
  the authoring session's records marked its ROADMAP item `[x]` and closed
  without harvesting it, so `sizescan --check` fails at HEAD
  (1 cold-content item) and the **floor workflow on `main` has failed on
  every push since** (verified: last three runs red, cause reproduced
  locally, rc=1). A standing red on the shared floor is worse than its
  trigger: it masks real reds for every session until cleared. The fix is
  the gate's own lossless move — harvest the `[x]` byte-verbatim to
  `ROADMAP-DONE.md` — mechanical records hygiene, not doctrine, so this
  pass will apply it in its records close and re-prove the floor green.
  *Counsel for the doctrine itself: none — the gate worked exactly as
  designed; the miss was the close litany, which RECORD already owns.*

### Reconcile — what the deferred material changed

Nothing overturned; two nuances. Opened after findings committed
(`85e7eac`): the intent record, Gaps 1–2's analysis, and the commit bodies.

- The author's account matches the encoding reviewed at HEAD: the ~80%
  grounding claim, the three-gap structure, the deliberate template
  non-propagation (IR2 answers the author's own flagged question), and the
  two grounded recoveries. IR1's overclaim exists in the author's account
  too ("silence with no closing entry = died mid-flight") — the finding
  attacks the encoding and stands unchanged.
- **The gitlink incident is honestly recorded and verified fixed**: the
  `b4b5142` `git add -A` sweep of the sibling worktree's gitlink is
  disclosed as an apex note, fixed forward (`3961404`: untracked +
  `.claude/worktrees/` gitignored — this pass's own worktree confirms the
  ignore holds), lesson saved to memory. No finding — the record did the
  right thing loudly.
- **IR5 nuance**: the close claim "all three pre-commit scanners green" was
  *honest* — sizescan is a CI-side gate, not a pre-commit hook, so the
  session verified exactly what it named. The miss is a close-litany blind
  spot (hooks checked, workflow not), which RECORD's close rules own; the
  finding stands as records hygiene, severity unchanged.

**Final: PASS-WITH-FINDINGS — 0 MAJOR · 3 MEDIUM (IR1, IR2, IR5) ·
2 LOW (IR3, IR4). No MAJOR ⇒ the cycle closes** (close rule); IR1–IR4 to
the backlog for the principal's ruling with counsel recorded per finding;
IR5's harvest is mechanical records hygiene, applied by this pass's records
close and re-proven green there.
