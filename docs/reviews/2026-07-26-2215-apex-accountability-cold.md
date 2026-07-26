# Cold review (rule 4) — apex: the principal's authority is rooted in accountability

**Subject (refs only):** the opening grounding paragraph added to
`docs/method/00-APEX.md` § "The principal's authority is conditioned on being
informed" in commit `4af5f3b` (2026-07-24). Establish the exact hunk with
`git show 4af5f3b` and review it at HEAD, in the context of the whole apex.

**Spawn provenance:** this review was spawned by a non-author taker session the
principal (Mike) opened and pointed at the review queue on 2026-07-26 ("Please
do any review work"); the work's author neither started nor instructed this
review or this reviewer; the taker authored none of the delta and gives the
reviewer refs only, no evaluative account. Session and reviewer tier: Fable
(cold review passes run on Fable — the principal's ruling, 2026-07-26).

**Taker exposure, owned:** the taker read the ROADMAP queue pointer and
SESSIONS index one-liners before writing this stub. Nothing evaluative from
either appears above the divider.

**The reviewer's first acts:** establish what the paragraph claims and why
from the delta and HEAD yourself; name the load-bearing assumptions and attack
surface as your own; run all four lenses at the widest scope
(`docs/method/REVIEW.md`). This is **apex text** — the widest blast radius in
the operating model; every future session and every child repo inherits its
framing. The heavy lenses: 1 — is accountability the right root for the
authority claim, does the RASCI framing hold, and does grounding the
reservation in consequences create any unintended release (if a decision's
consequences somehow didn't land on the principal, would the paragraph read as
licensing the agent to take it?); 3 — coherence with the rest of the apex and
with every in-repo restatement of the informed-principal section. This is a
public, shareable repo — lens 4 includes whether the paragraph's liability
framing (privacy, copyright/IP, licence/contract) says anything an adopter
would inherit wrongly.

**Re-run obligations:** `python3 tools/floor.py --plane ci` ·
`python3 -m unittest discover -s tools` · `node --test instruments/*.test.js`.
Lens 4's scanner: a landed markdown doctrine delta — `/security-review`
reaches only pending diffs and excludes markdown, so discharge it in one
explicit line with grounds.

**Reading discipline (hard):** do not open `docs/ROADMAP.md`,
`docs/SESSIONS.md`, `docs/sessions/**`, any other file in `docs/reviews/`, or
anything under `docs/reviews/withdrawn/`. Do not grep git history for review
commits; confine git archaeology to the delta commit named above. Open the
deferred section below only after your findings are durably written to this
file; then append the reconcile, named as such.

Findings carry stable IDs (**AA1…**) with claim / evidence / counsel; close
with **PASS**, **PASS-WITH-FINDINGS**, or **FAIL** and severity counts.
Self-authored apex doctrine: REVIEW.md rules 3–4 govern — findings are the
principal's to decide; nothing is applied in this pass.

---

## Deferred — open only after your findings are durably written above

*Intent record:* no separate record — the queue pointer states the intent as
the principal's own reading: the principal's authority is born of the
principal's accountability (RASCI *Accountable*) — he funds the work, the
world attributes the product to him, and the liabilities (privacy,
copyright/IP, licence/contract) land on him; the reserved decisions are his
*because their consequences are*. The paragraph is the author-agent's wording
of that reading, at the principal's instruction.

## Reviewer's attack surface (named first, before the deferred section is opened)

*Cold rule-4 reviewer, Fable, worktree at HEAD `9aef298`, 2026-07-26 (UTC).
Established the subject myself from `git show 4af5f3b` and
`docs/method/00-APEX.md` at HEAD (lines 64–75): a new opening paragraph
grounding the principal's reserved authority in accountability (RASCI
*Accountable* — attribution, funding, liability), closing "authority follows
accountability, and an agent that bears none of the outcome holds none of the
final say", plus the follow-on sentence's "absolute above" → "honesty absolute
above" clarification.*

Load-bearing assumptions I will attack, as my own:

1. **Accountability is the right root** — that attribution + funding +
   liability, rather than (say) the honesty absolute itself, ownership, or the
   principal–agent relation as such, is the true source of the reservation; and
   that adding a *second* grounding does not now give the section two competing
   roots (the next paragraph still calls it "the positive face of the honesty
   absolute above, and part of it").
2. **The consequence-conditional does not release** — "reserved to him
   *because their consequences are*" read contrapositively: if a reserved
   decision's consequences did not land on the principal (third-party harm,
   humanity-scale harm, harm landing on the agent's vendor, a safety floor stop
   whose victims are others), would the paragraph license the agent to take it?
   Likewise "bears **none** of the outcome holds **none** of the final say" —
   does the none/none logic invite a partial-bearing ⇒ partial-say reading?
3. **The RASCI framing holds** — the principal is named *Accountable*; the
   agent's letter is unassigned. Does the half-applied framework mislead, and
   is RASCI the frame the rest of the repo actually uses?
4. **The factual predicates are true and stay true** — "he funds it (… CI
   runners, every running cost)" on a public repo with free Actions minutes;
   "tiki is Mike's" as a named example inside canonical, adopter-inherited
   normative text.
5. **The liability sentence exports safely (lens 4)** — "a privacy breach, a
   copyright or IP infringement, a broken commercial licence or contract fall
   on the principal, not the agent" read by a public adopter as a *legal*
   allocation rather than a governance one; whether an adopter inherits a
   wrong or falsely comforting claim about where liability actually lands.
6. **Coherence with every in-repo restatement** — REVIEW.md rule 3's citation
   of this section, AUTONOMY.md, PROPAGATION.md's floor, the build templates'
   inlined apex floor, and the Laws section (obedience's ground vs
   accountability's ground): does any restatement now assert a different or
   pre-widening source for the authority?

Reading discipline honoured: no ROADMAP.md, no SESSIONS.md, no
`docs/sessions/**`, no other `docs/reviews/*`, nothing under
`docs/reviews/withdrawn/`, no git-history greps; archaeology confined to
`git show 4af5f3b`. The delta commit's own ROADMAP hunk appeared inside that
sanctioned `git show` output; nothing evaluative from it is used here. The
deferred section below the divider remains unread at this point.

---

## Verdict — cold rule-4 pass (Fable, 2026-07-26 UTC, worktree at HEAD `9aef298`)

**Spawn provenance, repeated:** reviewed in a session the work's author neither
started nor instructed — a worktree opened by the taker session the principal
pointed at the queue; the reviewer received refs only (the brief above the
divider) and established the subject from `git show 4af5f3b` and HEAD itself.
Reviewer tier Fable, per the principal's 2026-07-26 ruling.

### Re-run obligations — all green, exit codes checked explicitly

- `python3 tools/floor.py --plane ci` → exit 0; all nine scanners ✅ enforced.
  One size-advisory on `docs/ROADMAP.md` (advisory never fails; file not
  opened).
- `python3 -m unittest discover -s tools` → exit 0, "selftest OK".
- `node --test instruments/*.test.js` → 207 pass / 0 fail, exit 0.
- **Lens 4 scanner, discharged with grounds:** `/security-review` reaches only
  pending diffs and excludes markdown; this subject is a *landed markdown*
  doctrine delta, so the scanner has nothing it can read — and running it here
  would scan the dirty review brief itself (the documented SL2 hazard,
  `REVIEW.md` lens 4). Not run; its absence weighed as nothing either way.

### Findings

**AA1 — the consequence-conditional leaves a narrow release surface, and the
none/none phrasing invites a proportional-say misreading.** *(MINOR)*
*Claim:* `00-APEX.md:70–72` grounds the reservation as "reserved to him
*because their consequences are*: authority follows accountability, and an
agent that bears none of the outcome holds none of the final say." Read
contrapositively, a reserved decision whose consequences land chiefly on a
third party (a safety floor stop whose victims are others; the Zeroth-Law
domain) could be argued out of the reservation on the paragraph's own logic;
and "bears **none** … holds **none**" invites, by denying the antecedent, a
partial-bearing ⇒ partial-say reading — live for the one floor item whose
outcome the agent *does* bear, "a lockout-class change that could sever your
own access" (`AUTONOMY.md`, restated in the floor block,
`docs/build/templates/CLAUDE.md:35–36`).
*Evidence:* the operative text blocks the exploit twice — "reserved … to no
one else … The rule binds them all" (`00-APEX.md:75–82`) is unconditional,
and third-party harm converts to principal liability by the paragraph's own
list (`00-APEX.md:67–69`), with the Laws (`00-APEX.md:202–221`) covering the
rest. So the release requires a wilful misreading — but this is apex text with
the widest inheritance, where a grounds-clause read as a licence test by one
future optimising session propagates fleet-wide.
*Counsel:* one guard clause — mark the sentence as grounds, not a test; e.g.
"grounds, not a gate: a consequence that lands on a third party lands on the
principal as liability, and the reservation binds regardless of who else is
touched". The none/none sentence could add "and bearing a share buys no
share" or equivalent.

**AA2 — RASCI is invoked halfway: the principal gets the A, the agent no
letter.** *(MINOR)*
*Claim:* `00-APEX.md:64–65` names the principal "the one *Accountable*" and
stops; RASCI appears nowhere else in the doctrine (repo-wide grep: sole
occurrence) and the agent's obvious letter — *Responsible*, the executing
party — is unassigned.
*Evidence:* the inline gloss ("the party on whom the outcome finally lands")
covers the A for a reader who has never met RASCI, so plain-over-jargon is
technically discharged — but the half-application leaves the framework's
strongest support unused: RASCI's own single-A convention is precisely the
claim being made (final say sits in exactly one place), and naming the agent
*Responsible* would state the R-executes-under-A asymmetry the closing
sentence gropes for.
*Counsel:* one clause completing the frame — "the agent is *Responsible* — it
executes — and R works under A's final say, never beside it" — or drop the
RASCI name and keep only the gloss; half a framework is weaker than either
whole choice.

**AA3 — the section now states two roots for the reservation with the join
unstated.** *(MINOR)*
*Claim:* paragraph one grounds the reservation in accountability
(`00-APEX.md:64–72`); paragraph two still opens "The positive face of the
honesty absolute above, **and part of it**: the doctrine reserves certain
decisions to the principal" (`00-APEX.md:74–75`) — syntactically attaching the
*reservation itself* to the honesty absolute. The delta sharpened the
referent ("absolute" → "honesty absolute") but did not reconcile the two
groundings.
*Evidence:* a consistent reading exists — accountability sources the
*authority*; honesty sources the *informed condition* on exercising it — but
the reader must construct it; the text as written says the reservation is
both born of accountability and part of honesty, and in canonical apex text
the join should not be homework.
*Counsel:* rebind paragraph two to the condition, not the reservation — e.g.
"The positive face of the honesty absolute above, and part of it, is the
*condition*: that authority is real, but not exercisable uninformed…" —
leaving the reservation's source solely with the new paragraph.

**AA4 — "every running cost" is a totalising factual claim with a visible
counterexample.** *(NIT)*
*Claim:* `00-APEX.md:67` — "he funds it (model spend, CI runners, every
running cost)". Actions minutes on public repos (this one included) are
GitHub-funded; "every" overstates.
*Evidence:* the claim is true in substance — wherever a running cost exists it
is the principal's — and true of the private fleet; but the apex's own first
rule is "never a claim stronger than its evidence" (`00-APEX.md:20`), and
this is the apex.
*Counsel:* soften to "every running cost the work incurs is his to fund" or
drop "CI runners" from the parenthesis.

**AA5 — the liability sentence reads as a legal allocation; it errs safe, and
one clause would pin it.** *(NIT — lens 4's adopter-inheritance question,
answered)*
*Claim:* `00-APEX.md:68–69` — "a privacy breach, a copyright or IP
infringement, a broken commercial licence or contract fall on the principal,
not the agent" — will be read by public adopters as a statement about where
liability legally lands.
*Evidence:* no *wrong* inheritance: as between the two named parties the
claim is sound (the agent is not a liability-bearing person), and the error
direction is cautious — an adopter over-owning liability is the safe failure.
The only shading it hides is that model vendors can carry contractual
indemnities for some of these classes, which the sentence neither needs nor
contradicts.
*Counsel:* optionally pin the register with "as between principal and agent"
so no adopter mistakes a governance allocation for legal advice. Acceptable
as-is.

### What held

- **The root itself (lens 1, the heavy question):** accountability —
  attribution + funding + liability — is a sound and well-chosen source for
  the reservation; no stronger candidate root exists in the doctrine
  (honesty grounds the *condition*, not the authority — AA3 is a wording
  seam, not a wrong root). The commit's own claim ("stated the condition but
  never its source") verified true against the pre-image in
  `git show 4af5f3b`.
- **No authority-sense collision:** "authority follows accountability"
  coexists cleanly with "capability scopes authority" (`00-APEX.md:234–241`,
  `AUTONOMY.md:124–129`) because the glossary already chains them — the
  principal is "the grantor of all authority the agent exercises"
  (`GLOSSARY.md:21–23`); capability scopes how much is *delegated*, and the
  new paragraph reserves only the *final say*.
- **Every in-repo restatement coheres (lens 3, the other heavy work):**
  `RECORD.md:139`, `REVIEW.md:88–90`, `AUTONOMY.md:108–109`,
  `CONCURRENCY.md:516–517`, and the child floor block
  (`docs/build/templates/CLAUDE.md:32–41`) each restate the *informed
  condition* only; none asserts a source for the authority, so none now
  contradicts the grounding — and the floor block's silence is by design
  (children inline a short floor and point up, `00-APEX.md:243–249`).
- **Lens 4 substance:** no secrets, no new personal-data class — the
  principal's name and tiki's attribution have apex precedent
  (`00-APEX.md:10`, `00-APEX.md:243–249`); leakscan clean at HEAD; the
  funding parenthesis carries no amounts.
- **Lens 2 craft:** NZ spelling ("licence"), ISO attribution date, wrap,
  and house attribution style all clean (floor scanners green at HEAD).

### Discipline deviations, owned

- The sanctioned `git show 4af5f3b` necessarily displayed the delta's own
  ROADMAP hunk (the queue pointer landed in the same commit); nothing
  evaluative from it is used above.
- One phrase-echo grep swept `docs/` too broadly and printed a single matched
  line each from `docs/ROADMAP.md` and one `docs/sessions/` file; both lines
  merely mirror the paragraph's own wording. Neither file was opened; nothing
  evaluative was absorbed. Owned as a brush against the reading ban.
- `docs/reviews/withdrawn/` untouched; no other review files read; no
  git-history greps run.

### Close

**PASS-WITH-FINDINGS** — 0 MAJOR · 3 MINOR (AA1, AA2, AA3) · 2 NIT (AA4,
AA5). Self-authored apex doctrine: every finding above is counsel under
REVIEW.md rules 3–4 — the decisions are the principal's; nothing was applied
in this pass. A no-MAJOR pass is cycle-closing under REVIEW.md's
diminishing-returns rule, subject to the principal's decisions on the
findings.

## Reconciliation — deferred section opened after the verdict was durable

The deferred section carries no seeded questions — only the intent record:
the paragraph is the author-agent's wording of the principal's own reading
(accountability → RASCI *Accountable* → reservation), given at the
principal's instruction.

- **Findings added:** none.
- **Findings withdrawn:** none — every finding above targets the *wording*'s
  precision and inheritance behaviour, not the intent, and the intent record
  confirms the paragraph renders that intent faithfully (lens 2 held).
- **Findings sharpened:**
  - **AA2** — the RASCI frame is the *principal's own* reading, not the
    author-agent's imported jargon. The finding stands (the frame is still
    half-applied), but its counsel now weights the first option: *complete*
    the frame by assigning the agent *Responsible*, rather than dropping the
    RASCI name — dropping it would edit out the principal's chosen framing.
  - **AA1** — the "because their consequences are" conditional is likewise
    the principal's own phrasing per the intent record; the counsel is
    unchanged (a guard clause marking grounds-not-gate) but is now explicitly
    a wording guard around the principal's reading, not a challenge to it.

Withdrawn-directory ban held through this phase; no further files opened.
Verdict unchanged: **PASS-WITH-FINDINGS — 0 MAJOR · 3 MINOR · 2 NIT.**
