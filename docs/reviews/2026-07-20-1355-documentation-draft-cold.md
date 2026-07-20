# Cold pass — DOCUMENTATION doctrine, first draft (delta `62fe96a`)

- **Date/time**: 2026-07-20 1440 UTC (brief; claim stamped 1355)
- **Spawn provenance (rule 4)**: same taker as the sibling passes — Mike-
  spawned ("do any reviews waiting"), claim on `main` (`69b8de0`), authored
  none of the draft, its records, or the ros artefacts it grounds against.
  Taker-written brief.
- **The reconcile clause is vacuous — stated up front.** Mike commissioned
  this draft as *one candidate*, "cold-review my work against any competing
  drafts to reconcile". **No competing draft exists at HEAD**: no second
  file, no draft branch (`git branch -a` swept), and the ROADMAP records
  "a second session did not open a competing draft." So this pass runs as a
  cold adversarial review of the single draft — the review itself is the
  counterweight the competing draft would have been. If it emerges a draft
  exists elsewhere (scratchpad, another machine), reconciliation is owed and
  this verdict says so rather than pretending to have done it.
- **Named exposure**: the ROADMAP item (Mike's commission, his three
  recorded decisions, and the author's scope summary); `62fe96a`'s commit
  message; the SESSIONS.md entry for the draft (read in full during this
  session's early queue-scan grep — it carries the author's evaluative
  account including "honest gaps stated in-doc"; every claim in it is
  treated as a claim to re-run); one line of the draft itself (line 228,
  surfaced by the same grep). All named; the author's account of what the
  doc achieves is attackable, not settled scope.
- **Deferred material (opened only after findings are committed)**: nothing
  substantive remains beyond what is named above — there is no separate
  intent record for this draft (the SESSIONS entry is its record) and no
  prior verdict. The reconcile step is therefore: re-check the named
  exposure's claims against the findings, and state the seed↔finding
  overlap against Mike's three recorded decisions (which function as seeds:
  Diátaxis anchor, consumer axis, three folded deltas).

## What the work is (refs only)

Commit `62fe96a` — new file `docs/method/DOCUMENTATION.md`; registration in
`docs/method/README.md` (entry 15). Grounding target named by the delta:
`ros` @ `806eb10` (read-only). In-scope at HEAD: the draft, its README
registration, its fit against the sibling method docs it claims to absorb
rather than duplicate (RECORD, EVIDENCE §9, CONVENTIONS, COMMUNICATION,
APEX), and the ros artefacts its grounding claims cite.

## Lenses and the taker's attack surface

Lens 1 — approach & assumptions (named first, taker's own):

- **A1 — the matrix must be a tool, not a decoration.** Two axes (Diátaxis
  mode × consumer) implies up to 12 cells. Test: pick real artefacts (a
  `--help` screen, a man page, an error message, a `--json` schema, a
  changelog) and see whether the doc's matrix actually *decides* something
  about each — form, altitude, what "great" means — or whether the artefact
  inventory and the matrix run past each other.
- **A2 — every grounding claim is re-run against ros @ `806eb10`.** The
  draft claims tiki.1 carries MACHINE OUTPUT / CAVEATS sections, that
  PRINCIPLES §6 holds "the principal may be a machine", and — the honest-gap
  claim — that tiki.1's SEE ALSO does *not* yet point at vendor docs. All
  three verified at that exact commit, not at ros HEAD.
- **A3 — absorb-don't-duplicate is testable.** The scope rule says existing
  part-truths (RECORD, EVIDENCE §9, CONVENTIONS, ros PRINCIPLES §6) are
  absorbed by *pointer*, not restated. Any restated fact that can drift
  from its home is a finding against the doc's own single-source principle.
- **A4 — "ship the harvester not the harvest" must be honest about what
  exists.** If no harvester exists anywhere in the fleet, the doc may state
  the principle but must not imply one is running. Check for aspiration
  wearing present tense.
- **A5 — the third axis nobody named.** Diátaxis modes × consumers is the
  commissioned frame; audience (developer vs operator, newbie vs expert)
  was Mike's original ask and is *not* one of the two axes. Test whether
  the draft loses the audience dimension in the two-axis reduction, or
  handles it deliberately.
- **A6 — seam with COMMUNICATION.md.** Two method docs now own "how words
  reach a reader". Check the boundary is stated, not left to collide.

Lens 2 — correctness & quality: full read at HEAD; contradiction sweep
against sibling method docs; the in-doc review-state line (the 07-18
"omission is the bug" remedy); sizescan class of the new file.

Lens 3 — completeness / harvest: Mike's commission enumerated artefacts
("everything from docstrings to the --help screen … man file and a wiki …
any other form"); check the inventory against that list and against what a
real repo ships (tests-as-docs? commit messages? ADRs? README badges?
tutorials?) — a silently missing artefact class is a finding.

---

# Verdict — 2026-07-20 ~1500 UTC

**Provenance repeated (rule 4):** the taker named in the brief; author of
none of the draft, its records, or the ros artefacts cited. No deferred
material remained unread beyond what the brief names (no intent record
exists separate from the SESSIONS entry; no prior verdict exists), so
findings and reconcile land in one commit.

## Lens 2 first — every grounding claim re-ran TRUE at `ros` @ `806eb10`

This is the draft's strongest property and it is verified, not taken:

- `tiki.1` **MACHINE OUTPUT**: "byte-stable", "Machine mode never prompts",
  per-verb schemas — present as claimed.
- `tiki.1` **CAVEATS**: the flash-floor quirk (free-hdd exactly 20480,
  RAM-only silent revert, "run tiki health before trusting an apply to
  stick") — verbatim as the draft renders it.
- `tiki.1` **SEE ALSO**: points only to ARCHITECTURE/CHANGELOG/README — the
  draft's *honest-gap* claim (no vendor pointer yet) is **true**, and
  correctly assigned to ros's application half.
- `ros PRINCIPLES §6`: "the principal may be a machine" (Mike, 2026-07-15),
  the tier-1/tier-2 split (2026-07-17), "entire result, never a lossy
  subset", "the human view is a rendering of the machine truth", and
  `fleet.json schema_version` as the worked instance — all present; the
  draft's Grounding paragraph is a faithful lift.
- **"Ship the harvester, not the harvest"**: a real, Mike-ratified ruling
  (ros model-datasheet catalogue, 2026-07-18, three independent grounds) —
  the draft's copyright-question cross-reference is accurate.
- Principle 2's pointer: `RECORD.md` does carry the docs-as-code /
  man-page-in-the-same-commit rule at its head — the pointer resolves.
- Registration: `method/README.md` entry 15 present; sizescan does not flag
  the new file (232 lines, judgement-class); the in-doc `*review:*` foot
  line complies with the 07-18 "omission is the bug" remedy; the
  COMMUNICATION.md seam claim ("working with me" calibration) matches that
  doc's actual text.

## Findings

- **DD1 (MEDIUM, lens 1/2 — the table drops the cell the doc says is most
  often dropped).** § *What "great" means per cell* promises "the two axes
  together", but its table columns are **Human newbie · Human expert · AI
  operator · Orchestrator** — a four-persona strip, not a matrix. Missing:
  the **developer** cell (and the human *operator*, arguably). The draft
  itself warns, three sections earlier, "The developer cell is the one most
  often dropped… Name it separately" — and then its own great-per-cell table
  drops it. The persona set also disagrees with the artefact inventory's
  (which uses operator/expert/developer). The irony aside, the defect is
  real: the table is where a child session will look up "what does great
  mean for X", and the extend-the-tool reader has no column. *Taker's
  counsel: add the developer column (needs: the why + extension seams;
  served by: ARCHITECTURE/PURPOSE-class docs, why-comments, ADRs; fails
  when: only reference exists), or retitle the table "the four
  highest-traffic cells" and say where the others live.*
- **DD2 (LOW, lens 2 — the mapping overclaims "directly").** "Its four
  modes map onto the audiences directly" is stronger than Diátaxis itself
  licenses — modes serve *needs of the moment*, not user types (an expert
  is a newbie in a new tool; newbies read how-tos). Mike's decision 3
  deliberately folds developer↔explanation, so the mapping is ruled — but
  "directly" flattens a known-rough correspondence into a clean one. One
  qualifying clause ("map roughly, by centre of gravity") keeps the anchor
  honest without weakening it.
- **DD3 (MEDIUM, lens 3 — inventory gaps against the commission's "any
  other form you can think of").** Three artefact classes the estate
  demonstrably uses are absent from the inventory: (a) **tests as
  documentation** — executable how-to/reference whose staleness is caught
  mechanically, the natural bridge to `EVIDENCE.md` (fixtures and
  snapshot-replay *are* worked examples); (b) **commit messages** — the
  house's own "why-dense body" convention is a documentation artefact, and
  the AI consumer leans on it constantly (this review reconstructed intent
  from commit messages throughout); (c) **diagrams** (architecture /
  executive-audience) — a form the estate's own practice names. *Counsel:
  add rows, or state the exclusion and where each lives instead.*
- **DD4 (LOW, process — the reconcile clause is vacuous).** Mike
  commissioned "cold-review against any competing drafts to reconcile"; no
  competing draft exists at HEAD (no file, no branch; the ROADMAP records
  that the second session did not open one). Not a defect of the draft —
  recorded so the `⏳` item's "reconciles the drafts and applies" is not
  ticked as done by implication. **Mike decides**: accept this adversarial
  cold pass as the counterweight the second draft would have been, or
  commission a genuine competing draft before ratifying.

## Reconcile — named exposure re-checked against findings

Mike's three recorded decisions function as the seeds, and all three are
honoured in the draft: Diátaxis anchor ✓ (with DD2's one-word overclaim),
consumer axis ✓ (faithful §6 lift, verified), the three folded deltas ✓ —
though decision 3's *warning* (developer ≠ expert-user, easy to conflate) is
exactly what DD1's table then does by omission, which is the strongest sign
this pass found something the seeds pointed *at* rather than away from. The
SESSIONS entry's evaluative claims ("honest gaps stated in-doc", "grounded
read-only against ros @ 806eb10") both re-ran true. Beyond the seeds: DD3
(inventory gaps), DD4 (vacuous reconcile).

## Result

**PASS with findings — 0 MAJOR · 2 MEDIUM · 2 LOW.** The draft is strong:
genuinely grounded (every citation re-ran true at the pin — rare and worth
saying), honest about its gaps, single-sourced by pointer, and the two-axis
frame with the consumer extension is the right shape. The MEDIUMs are the
dropped developer column (DD1) and the inventory gaps (DD3); both are
additive fixes, not rework. Doctrine, self-authored — **decisions are
Mike's**, including the standing one DD4 surfaces: whether this cold pass
discharges the "competing draft" intent. The tiki application pass (ros's
half) remains owed and is unaffected. No-MAJOR ⇒ on Mike's rulings the
cycle closes terminal per the close rule.
