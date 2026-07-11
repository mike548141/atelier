# Review — RECORD "The record is public — keep private repos generic"

**Scope:** the new RECORD.md section (commit `dfd5aec`, 2026-07-11) plus the
scrub commit it grounds in (`d6963ec`). Review-owed by its own flag: the section
came out of a **live incident** (session-record posture-prose leaked into public
atelier, scrubbed same day) rather than the usual grounded-extraction, so it has
had no cold read at all — incident-born doctrine risks over-fitting the one case
that hurt.

**The three lenses, instantiated:**

1. *Approach & assumptions* — is prose-description-of-secrets the right class to
   regulate, and is a naming rule the right mechanism?
2. *Correctness & quality* — does the rule as written say what the incident
   taught, no more and no less? Is it consistent with the rest of `method/` and
   with the repo's own current records?
3. *Completeness / harvest* — what records already on `main` violate it; what
   adjacent failure modes it silently omits.

**Specific assumptions to attack:**

- **A1 — the worked-example carve-out is drawn in the right place.** The rule:
  name a private repo only when the name carries *doctrinal weight as a worked
  example* ("ros, faves"); "a repo merely standardised or worked on that session
  gets no name". But the repo's own records — including the session-39 fleet-
  adoption entry written the *same day* — name every fleet child (numen,
  docker-heap, rpi, nova, homenetwork, ec2_builder, hitchbots_guide, FoodTracker,
  Baby Brain). Either those records are all in violation of the new rule, or the
  rule is written stricter than the practice it claims to codify. Which is it?
  Is the harmful class the *name*, or the *name joined to secret-posture prose*?
- **A2 — the rule catches the incident's failure mode.** Reconstruct the
  incident from `d6963ec`: would this section, had it existed, have named the
  leaked prose as a violation *before* commit? Or does it only describe the
  cleanup after?
- **A3 — over-restriction.** Doctrine must sometimes cite a real repo to stay
  grounded (grounding is a hard constraint in this house). Does the rule as
  written block legitimate grounding, and does the carve-out's parenthetical
  "(ros, faves)" read as an exhaustive whitelist when it shouldn't (or should)?
- **A4 — the older records.** The ROADMAP item explicitly asks: sweep records
  that predate the rule (SESSIONS index + `docs/sessions/` detail files +
  ROADMAP + CHANGELOG + reviews) for prose that records *which private repo
  holds which secret, where, or its exposure history*. Anything found is a
  scrub candidate — list each with file:line.
- **A5 — enforceability.** The section itself concedes a scanner can't catch a
  sentence. Is review-cadence the stated enforcement, and is that stated
  honestly (PROPAGATION's enforcement clause), or does the section imply a
  protection it can't deliver?

**Reviewer:** cold fresh-context agent (2026-07-12), read-only; fixes applied by
the coordinating session after the verdict. Review deep, not fast. Verdict below
the divider, findings with stable IDs (R1, R2, …).

---

**VERDICT: PASS-WITH-FINDINGS**

Cold fresh-context review, 2026-07-12, read-only. Scope: RECORD.md "The record
is public — keep private repos generic" (commit `dfd5aec`) plus the incident
scrub it grounds in (`d6963ec`). I read the brief, REVIEW.md, 00-APEX.md,
RECORD.md whole, both commits in full, and swept the entire record (SESSIONS
index, all session detail files, ROADMAP, CHANGELOG, reviews, decisions, and
`tools/pins.py`) for violations. Live claims re-run per REVIEW.md:
`gh repo view mike548141/atelier --json visibility` returns PUBLIC, and the
pre-scrub commit `77adbc7` (session-39 record with service-level posture
detail) is an ancestor of public `main` — the scrub's "details remain in pushed
public history" caveat holds, honestly stated.

The section's central clause is correct and earns its keep. Its naming clause
is mis-drawn, and the rule as written is violated by the repo's own current
records — including by the scrub commit that grounds it.

**A1 — is the carve-out drawn in the right place? No.** The harmful class is
the *join* — a private repo's name coupled to secret-posture prose — not the
name. The evidence is decisive: (i) the same-day scrub `d6963ec` deliberately
*kept* every fleet child's name (session-39 index and detail, session-38
heading) while removing only the posture detail — the scrub's own judgement
contradicts the rule's "a repo merely standardised or worked on that session
gets no name"; (ii) the record pervasively and legitimately names children with
no harm (numen as first keeper repo and the child-CI-floor test child across
sessions 21–30; faves/rpi in the foundation review; the adoption inventory
itself); (iii) `pins.py` names ros/faves in a public comment. Under the rule as
written, most of `main` is in violation, which means the rule does not codify
practice — it over-writes it. The rule should regulate class (b): never join a
private repo's identity to which secrets it holds, where, or its exposure
history (and generalise "secrets" to sensitive posture — client-confidentiality
content is the same class). Name-only mentions are unregulated; the record's
resumability depends on them.

**A2 — does the rule catch the incident's failure mode? The central clause,
yes; the section as a whole, incompletely.** "Never records *which private repo
holds which secret, where, or its exposure history*" is nearly a transcription
of what `d6963ec` removed (service-level credential names, config line numbers,
a live secret seed, was-public history, an archive path) — had it existed, it
names sessions 38–39's prose as violations before commit. But it is rule-text
only, with no mechanical gate (see A5), and the strongest evidence it doesn't
fully transmit the class is that the scrub session itself — rule in hand,
editing the very file — left a name-to-posture join standing (R2 below). The
section describes the incident accurately; it does not yet describe the
*residual* failure mode, the coarse-grained join that survives genericisation.

**A3 — over-restriction? Yes, as written.** Grounding is a hard constraint in
this house; doctrine must sometimes cite real repos. The "(ros, faves)"
parenthetical reads as a whitelist and is contradicted *within the same
commit*: the ROADMAP review-owed item says "ros/faves/numen are intended
examples". numen carries genuine doctrinal weight across the record (first
scaffold, first real child-CI run). The carve-out needs to be a test, not a
list: name a private repo when the name is load-bearing for the lesson; the
parenthetical becomes "e.g. ros, faves, numen".

**A4 — the sweep.** No residual service names, secret types, locations, or
exposure history anywhere in the record (grep for the scrubbed incident's
vocabulary: zero hits outside ADR 0005's atelier-about-itself addendum). What
remains is joins:

- `docs/sessions/2026-07-11-39-fleet-adoption.md:15–16` — "`ec2_builder`,
  `homenetwork`, `hitchbots_guide` — the ones carrying secrets/client content
  (below)." **Class (b), the worst survivor**: it tells a reader exactly which
  three of eleven private repos hold secrets and which holds client material.
  Scrub candidate under any reading of the rule.
- `docs/sessions/2026-07-11-38-….md:39` (heading "docker-heap standardised —
  and a live-secret discovery handled honestly"), `:41–54` ("real committed
  credentials the private repo already tracks… pre-public blocker"), `:64–65`
  and `:80` ("floor red on the tracked secret"). **Class (b), coarse-grained**
  — no service names, but docker-heap is identified and its posture (committed
  credentials, rotation pending, intends to go public) described.
- `docs/SESSIONS.md:48` — same join in the session-38 index line ("the scan
  surfaced real committed secrets already tracked as the repo's own pre-public
  blocker… floor CI correctly red on the tracked secret").
- `docs/ROADMAP.md` (open questions) — item headed "`docker-heap` is
  unstandardised — DONE" joined to "inline-credential debt already tracked as
  the repo's own pre-public blocker… CI correctly red on the tracked secret
  until it's rotated."
- Borderline, acceptable under the redrafted rule: `docs/SESSIONS.md:50` (all
  eleven names listed, with "surfaced real secret debt in a few repos" — a
  diluted few-of-eleven join) and `2026-07-11-39-fleet-adoption.md:37` ("the
  docker-heap policy" cited inside a credentials bullet — mild reinforcement of
  the session-38 join).
- Name-only, fine: every other hit (numen scaffolding/CI runs, pin bumps,
  faves/rpi in the foundation review, CHANGELOG's "moved in from
  `homenetwork/bin`").

**Position taken**: the rule should regulate class (b) only. Class (a) naming
is woven through the record's machinery and the scrub's own choices; outlawing
it makes the doctrine a dead letter on arrival.

**A5 — enforceability. Stated dishonestly by omission.** The section concedes
a scanner can't catch a sentence, then names *no* compensating control — it
just states the rule. PROPAGATION's enforcement clause is explicit that
documents inform and review enforces; EVIDENCE §12's machine floor is exactly
what's unavailable here, and the section should say so and name what remains:
write-time author discipline plus review-cadence sweeps of the record. The
incident's own arc proves the point — the author, same session, with the rule
freshly written, missed the R2 join in the file being scrubbed. A rule whose
only enforcement is the discipline of the writer it just failed must say that
plainly, or it implies a protection it can't deliver.

**Findings**

- **R1 [Blocking]** — RECORD.md:100–102: "a repo merely standardised or worked
  on that session gets no name" outlaws the repo's own records and contradicts
  the grounding scrub's kept names. *Fix*: redraft to regulate the join — a
  private repo's name may appear (adoption lists, worked examples); what never
  appears is its name coupled to secret/exposure/confidentiality posture; when
  recording security work, either the name or the posture goes generic. Extend
  "secrets" to sensitive posture generally (client content included).
- **R2 [Blocking]** — `docs/sessions/2026-07-11-39-fleet-adoption.md:15–16`
  joins three named private repos to "carrying secrets/client content" on
  public `main`. *Fix*: scrub — fold the three into the plain adoption list and
  let the generic "Security debt surfaced" section carry the posture,
  unattributed.
- **R3 [Minor]** — the docker-heap coarse join survives in four places
  (`docs/SESSIONS.md:48`; session-38 detail heading, §3, :64–65, :80;
  `docs/ROADMAP.md` open-questions item), including the "pre-public blocker"
  intent leak (announces that a repo with secret-bearing history will be
  published). *Fix*: either genericise the name in the posture sentences ("an
  infra child") or have the R1 redraft explicitly sanction coarse joins with
  stated rationale — but resolve it one way; doctrine and record must agree.
- **R4 [Minor]** — RECORD.md section names no enforcement. *Fix*: one
  sentence: the mechanical floor cannot hold this rule (EVIDENCE §12
  unavailable by the section's own admission); enforcement is write-time
  discipline plus periodic review sweeps of the record (PROPAGATION's
  enforcement clause), and this review is the first such sweep.
- **R5 [Minor]** — carve-out list inconsistency: section says "(ros, faves)";
  the same commit's ROADMAP item says ros/faves/numen. *Fix*: "e.g. ros,
  faves, numen" plus the load-bearing-name test from A3.
- **R6 [Low]** — `docs/sessions/2026-07-11-38-….md:44` "see the covenant note
  below" dangles; the scrub never added the referent. *Fix*: point it at the
  RECORD.md section or delete the aside.
- **R7 [Low]** — the section omits the incident's sharpest lesson: on a public
  repo, scrubbing HEAD is not remediation — the posture prose is still
  reachable at `77adbc7` on public `main` (re-verified live). *Fix*: add the
  sentence; it is also the honest justification for R4's write-time emphasis.

**Close.** The section's core insight is sound and well-grounded: the
personal-data boundary covers description, not just pattern, and the scanner's
blindness to a sentence is real — I re-proved the residue it can't see sitting
on `main` right now. But incident-born doctrine over-fitted exactly as the
brief feared, just in an unexpected direction: it banned the harmless thing
(names) the scrub itself kept, while the harmful thing (the name-to-posture
join) survived the scrub in four places, one of them precise enough to serve as
targeting data. Redraft the one sentence (R1), scrub the survivors (R2, R3),
state the enforcement honestly (R4, R7), and the section becomes what it set
out to be — a rule the next session can actually apply at write-time, which,
on a public repo where every push is irrevocable, is the only moment the rule
can ever bind.

---

## Disposition — 2026-07-12, coordinating session

All seven findings **[fixed]** same day, one commit:

- **R1 [fixed]** — RECORD.md section redrafted: the regulated class is now the
  **join** (name × sensitive posture, publication intent and client content
  included); name-only mentions sanctioned explicitly with the
  load-bearing-name test.
- **R2 [fixed]** — the three-named-repos-to-posture join scrubbed from the
  fleet-adoption detail; the generic section carries the posture unattributed.
- **R3 [fixed]** — resolved ONE way, the strict way: coarse joins also go
  generic at HEAD. All four places rewritten ("findings the repo's own records
  already track"); the "pre-public blocker" intent leak removed everywhere; the
  session-38 §3 heading de-joined. Doctrine and record now agree.
- **R4 [fixed]** — enforcement named in the section: write-time discipline +
  periodic review sweeps, nothing stronger; mechanical floor unavailable by the
  rule's own premise.
- **R5 [fixed]** — carve-out is now "e.g. ros, faves, numen" behind the
  load-bearing-name test, not a whitelist.
- **R6 [fixed]** — dangling "covenant note below" now points at RECORD's "the
  record is public" rule.
- **R7 [fixed]** — the section now opens with scrub-of-HEAD-is-not-remediation
  and closes grounded in both the incident and this review's four-place
  survivor find.

Residual, stated: the pre-scrub prose remains reachable in public history
(`77adbc7` and earlier) — irrevocable by design of git; the write-time rule is
the only control that exists. The RECORD.md redraft is itself doctrine text and
per its own calibration would be review-owed — judged covered by *this* review
(the redraft implements this verdict's R1/R4/R5/R7 wording, reviewed here),
not a fresh unreviewed idea.
