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
