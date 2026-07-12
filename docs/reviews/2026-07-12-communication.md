# Review — method/COMMUNICATION.md (communication calibration doctrine)

**Scope:** `docs/method/COMMUNICATION.md` (commit `1ca394f`, 2026-07-12,
session 43) plus its wiring (method/README entry, CHANGELOG line, ROADMAP
decline-then-revisit sub-bullet). New doctrine ⇒ cold review owed by
calibration (first-of-kind: the first method/ doc whose worked example is a
scrubbed extract of the principal's *person-level* layer, on a public repo).

**The three lenses, instantiated:**

1. *Approach & assumptions* — is a person-level communication calibration the
   right mechanism, and is the practice/instance split (borrowed from
   TOOLBOX.md) the right frame for it?
2. *Correctness & quality* — does the doc say what session 43 decided, no more
   and no less? Is every "grounded in the live instance" claim carried by a
   concrete specific, or padded? Is it consistent with the rest of `method/` —
   especially RECORD's join rule and the no-personal-data boundary?
3. *Completeness / harvest* — what a calibration doc should cover and doesn't;
   what already exists that it duplicates or ignores; whether maintenance/
   enforcement of the practice is stated honestly (PROPAGATION's enforcement
   clause).

**Specific assumptions to attack:**

- **A1 — the worked example does not leak the personal layer by implication.**
  The doc scrubs the personal context and then *names the categories it
  scrubbed* ("health, workload, household"). On a public repo whose owner is
  identified, is stating which sensitive categories exist behind the scrub
  itself a leak — the same *join* class RECORD's rule regulates (identity ×
  sensitive posture), one layer up (person, not repo)? Judge as a cold public
  reader: what can be inferred about the principal from the scrubbed example
  plus the scrub note plus the grounding anecdotes (the "witty at full dose"
  case, "reduce cognitive load")? **Do not read `~/.claude/` or any
  person-level file** — the question is precisely what a reader *without* that
  layer can reconstruct.
- **A2 — the axes list is grounded, not padded.** Every axis claims grounding
  in the live instance. Which axes carry a dated, specific confirmation (the
  colour-icons case) and which are generic best-practice a heading could have
  invented? An ungrounded axis violates the house's stub-don't-fabricate rule
  and should be named.
- **A3 — the decline-then-revisit history is honest grounding, not
  relitigation.** The doc was declined the same day it was built. Check the
  ROADMAP sub-bullet and the doc's history paragraph against each other: does
  the record show the original call standing (values stay personal) with a
  sharper split resolving it, or does it read as quietly reversing a decision
  the ROADMAP already recorded?
- **A4 — the practice/instance split actually holds structurally.** TOOLBOX's
  split is the claimed precedent — verify the analogy is real, not borrowed
  authority. And test the boundary sentence "the calibration works without the
  reader knowing it": is that true of the worked example as printed, or do
  some lines only make sense *with* the missing motivation?
- **A5 — wiring and duplication.** Verify the claimed wiring exists (method/
  README entry, CHANGELOG, ROADMAP sub-bullet). Sweep for overlap: does any
  other method/ doc (RECORD, EVIDENCE, TOOLBOX, the apex) already carry
  reply-style guidance this duplicates, and does the repo's own CLAUDE.md
  onramp conflict with "person-local, never copied"?

**Reviewer:** cold fresh-context agent (2026-07-12), read-only; fixes applied
by the coordinating session after the verdict. Review deep, not fast. Verdict
below the divider, findings with stable IDs (C1, C2, …).

---

**VERDICT: PASS-WITH-FINDINGS**

Cold fresh-context review, 2026-07-12, read-only. Scope: `docs/method/COMMUNICATION.md` at commit `1ca394f` (which is HEAD; working tree clean) plus its wiring. I read the brief, REVIEW.md, 00-APEX.md, the doc itself, and the consistency set (TOOLBOX.md, RECORD.md, EVIDENCE.md, PROPAGATION.md, ADR 0005, the repo README and CLAUDE.md, ROADMAP, CHANGELOG, SESSIONS.md, `docs/sessions/2026-07-12-43-communication-doctrine.md`, and the R-review exemplar). Claims re-run: `git show --stat 1ca394f` confirms all six claimed files landed in the one commit (RECORD's lockstep rule held); the method/README entry 12 (`docs/method/README.md:46–50`), CHANGELOG block (`CHANGELOG.md:8–17`), ROADMAP review-owed item (`docs/ROADMAP.md:10–16`) and decline-then-revisit sub-bullet (`docs/ROADMAP.md:111–118`, nested under the untouched original reframe item at :103–110) all exist at HEAD and say what the doc claims; every internal cross-reference resolves (TOOLBOX's "Two things, kept separate" split is real and verbatim-parallel; EVIDENCE §7 is absolute dating; RECORD.md:94–95 is scrub-of-HEAD-is-not-remediation; ADR 0005 is the named-worked-example framing). A duplication grep across `method/`, the root README, and CLAUDE.md found no other home for reply-style guidance. Honesty note on A1: my system context included person-level material I am instructed to ignore; I could not unsee it, so I answered A1 by enumerating only inferences derivable from cited repo text — every step below is checkable against the repo alone.

**A1 — does the worked example leak the personal layer by implication? No — it sits on the sanctioned side of RECORD's own line.** What a cold public reader can reconstruct from the doc: the principal (identified — accepted knowingly in ADR 0005) keeps a calibration older than atelier; several of its lines are motivated by personal context in three categories (`COMMUNICATION.md:92`, "health, workload, household"); he carries a load (:47, :26 "why the person carries the load they do"); something exists he must not be nagged about (:26); a previous assistant overdid wit (:63–64). The join this creates is *identity × category-existence*, with zero specifics — no condition, person, figure, or entity is inferable. RECORD's redrafted rule (the R1 fix) regulates the join and resolves it by "either the name or the posture goes generic" — here the name is irreducibly present (ADR 0005) and the posture *is* generic: three category nouns. Decisively: the repo already publishes those very categories as its boundary statement (`README.md:111–112` "No personal, health, family, or financial context ever enters this repo"; CLAUDE.md's hard constraint) — so "health, workload, household" discloses only that the categories the boundary already names have content behind them, which is true of any human principal and was already implied. The sharpest available inference — join "must not be nagged about" to "health" — yields a fact with no content ("something health-adjacent, unspecified"). Below the harm line. The scrub note is also apex-required: stating *that* material was removed, and what class, is what keeps the example honest rather than passing as complete.

**A2 — axes grounded or padded? Qualified yes — grounded, unevenly evidenced.** No axis reads as heading-filler; each carries instance-specific phrasing rather than textbook generalities. But the evidence tiers differ. Repo-corroborated *before* this commit (the pre-existing ROADMAP reframe item, `docs/ROADMAP.md:107–110`, lists what was written into the person layer): ordering ("outcome-first-then-evidence"), density ("watch volume, let structure replace length"), visual structure ("visual reader → iconography/tables"). Carrying a concrete specific: visual structure (colour vs monochrome icons — the doc's own "specifics matter more than the category" case, dated 2026-07-12 in the session file but *undated in the doc*, see C3) and tone (the overdone-wit anecdote — concrete, undated, and a genuine grounding case: preference real, recitation the defect). Locale is grounded by the house's own conventions. The two weakest — cognitive-load stance and what-personal-context-is-for — rest solely on this commit's self-attestation; a cold reader cannot corroborate them anywhere in the pre-existing record, and the instance is unreachable by design. That is inherent to the split, and the bearing (:97–99) states the provenance honestly, so it is not fabrication — but it is the difference between "grounded" and "checkably grounded", and the doc could close it cheaply (C3's dating fix does half of it).

**A3 — decline-then-revisit: honest grounding, not relitigation. Yes.** The original reframe item stands untouched at `docs/ROADMAP.md:103–110` (the 1ca394f diff only *adds* — 7 review-owed lines, 8 sub-bullet lines); the revisit is an appended sub-bullet, not an edit. The three accounts agree with each other and with the facts: the boundary half of the original call (values are personal, `~/.claude/` only) genuinely stands; the artefact half ("the clean call was *not* to build `method/REPORTING.md`") genuinely was reversed — by the principal, same day, openly, with the resolving distinction (pattern ≠ values) recorded in all three places. The doc's parenthetical (:29–32) says exactly this and hides nothing. One calibration note, no finding: a call reversed within hours is by definition re-litigable, which is RECORD's ADR test — but the ADR test is whether *forgetting the reasoning* would cost a future argument, and the reasoning is durably recorded in three joined places, so an ADR would be ceremony here.

**A4 — does the practice/instance split hold structurally? Yes, with the precedent honestly layered.** The TOOLBOX analogy is real, not borrowed authority: same heading ("Two things, kept separate"), same shape (shareable rules / person-local values, `TOOLBOX.md:9–23`), same `~/.claude/` home, same never-in-a-shareable-repo boundary. Where COMMUNICATION *exceeds* TOOLBOX — including a scrubbed instance excerpt, which TOOLBOX never does — it correctly cites ADR 0005 for that extension, not TOOLBOX (:26–27), and the move has in-repo precedent (the ROADMAP's AUTONOMY/STORAGE practice/instance-restructure item treats person-local specifics as marked worked examples). The boundary sentence "the calibration works without the reader knowing it" (:94–95) is true at the directive level — I tested each worked-example line and every one is executable as printed; none dangles on missing motivation ("keep the wit light-touch" even carries its why via the meta-rule's anecdote). But it is only true at the *compliance* level, and the doc's own first meta-rule says compliance isn't the purpose — see C4.

**A5 — wiring and duplication. Wiring complete; no duplication; one real cross-record tension.** All claimed wiring verified at HEAD (citations in the scope paragraph); the SESSIONS.md session-43 line and detail file also landed in the same commit. The root README's method list (`README.md:57–71`) is a selective highlight (it omits ten other method docs), so COMMUNICATION's absence there is not a gap. No other method/ doc carries reply-style guidance (grep clean). The repo's own CLAUDE.md ("NZ English; macrons") does **not** conflict with "person-local, never copied" — the doc explicitly sanctions repo-convention locale in a repo CLAUDE.md (:68–70), and the conventions there govern the repo's artefacts, not a person. The tension that *does* exist is C2: "not even a private one" (:71) is stricter than both its claimed precedent and the ROADMAP north star, unreconciled.

**Findings**

- **C1 [Minor]** — `docs/method/COMMUNICATION.md:66–67`: "Maintain it like a record" names no enforcement, and this practice is the extreme case of the R4 class RECORD was already corrected for — the instance lives in the person-level layer, where *no* control in the house can reach it: no scanner (EVIDENCE §12's floor is unavailable), no CI, and no review sweep either, because a cold reviewer is barred from reading `~/.claude/` *by design* — this review's own brief is the proof. The only enforcement is the agent's write-back discipline at the moment a reply lands well or badly. PROPAGATION's enforcement clause requires saying that plainly; silence implies a protection the practice can't deliver. *Fix*: one sentence in the meta-rules — maintenance binds through write-time discipline alone; the instance sits outside the reach of every mechanical floor and every review sweep, and the house's reviews are barred from it on purpose.
- **C2 [Minor]** — `docs/method/COMMUNICATION.md:68–72`: "never copy it into a repo — not even a private one" silently out-narrows the record it claims to align with. TOOLBOX (:21–22) says never in a *shareable* repo; the ROADMAP north star (`docs/ROADMAP.md:631–643`) explicitly designs a two-tier scheme in which the lighter instance/identity tier "may tolerate a private store/repo", reserving never-a-repo for crown-jewels. Calibration *values* (colour icons, outcome-first) are the lighter tier; only the motivators are crown-jewels. Stricter is a permitted narrowing, but the house's own layer-override discipline says a divergence is surfaced, never silent — and here both readings now sit in the public record for a future session to trip over. *Fix*: either scope the not-even-private clause to the motivating personal context (matching the north star's tiers), or keep the blanket rule and add the reconciling sentence ("deliberately stricter than the portability north star's lighter tier, because a calibration travels *with* its motivators") — one way, so record and doctrine agree.
- **C3 [Minor]** — the doc violates its own dating rule twice, both cheaply fixable without leaking anything. (i) `:74–77`: the worked example is a *copy* of a living, still-accumulating document (the bearing, :97–99, says so) with no date and no staleness posture — EVIDENCE §7 (absolute dating), §9 (two copies drift silently), §10 (no refresh trigger named); and the meta-rule six lines above it says "never copied" with no stated carve-out for the exception sitting in the same file. (ii) `:44–46`: "the live instance prefers *colour* icons" is a confirmation the session record dates (2026-07-12) but the doctrine doc leaves undated, in the very doc that mandates dated confirmations. *Fix*: head the example "snapshot of the live instance, 2026-07-12 — the instance moves; this illustrates the shape" ; add "(confirmed 2026-07-12)" to the colour-icons specific; add "(the scrubbed snapshot below is the one sanctioned exception — ADR 0005's framing, replaced wholesale by an adopter)" to the never-copied bullet.
- **C4 [Low]** — `docs/method/COMMUNICATION.md:94–95`: "the calibration works without the reader knowing it" is true as printed at the directive level (verified line-by-line) but overclaims against the doc's own first meta-rule, which says mechanical compliance is precisely not the point — the scrub removes exactly the understanding that :61–62 declares the purpose. Harmless for the adopter (who replaces the example wholesale) but the sentence hands a hostile reader a self-contradiction. *Fix*: sharpen — "the calibration *functions* without it: every line above is executable as printed; the understanding that turns rules into judgement stays person-local, which is why the instance, not this snapshot, is what the agent actually serves."

**Close.** The doc survives its own sharpest question. The brief feared the first person-level scrub on a public repo would leak by implication; judged strictly from the repo, it doesn't — the scrub note discloses category names the repo's boundary statement already published, and the join it creates carries no content, landing exactly on the sanctioned side of the line RECORD's redraft drew one layer down. The split is structurally sound, honestly layered on its two real precedents (TOOLBOX for the shape, ADR 0005 for the excerpt), and the decline-then-revisit is a model of append-only honesty — the original call is still readable, unedited, above its own reversal. What the findings share is one theme: the doc holds the *boundary* rigorously but is looser on itself than the house is on everything else — unenforceable maintenance unstated (C1), a silent out-narrowing of the portability record (C2), an undated copy of a living document under a rule that forbids copies (C3). All are one-to-three-sentence fixes; none touches the design. Fix the four and this is the clean, small pattern doc it set out to be — and the first proof that the named-worked-example framing can reach one layer further up than the estate, into the person, without dragging the person along.

---

## Disposition — 2026-07-12, coordinating session

All four findings **[fixed]** same day, one commit:

- **C1 [fixed]** — enforcement named in the maintain-like-a-record meta-rule:
  write-time discipline is the only control; the instance sits outside every
  mechanical floor and every review sweep, reviews barred from the person
  layer by design.
- **C2 [fixed]** — resolved ONE way, the strict way: the blanket
  not-even-private rule stays, with the reconciling sentence — deliberately
  stricter than the portability north star's lighter tier, because a
  calibration travels *with* its motivators and gets crown-jewel handling
  whole. Doctrine and record now agree, divergence surfaced not silent.
- **C3 [fixed]** — worked example headed as a dated snapshot (2026-07-12,
  "the instance moves; this illustrates the shape, it does not track the
  original"); colour-icons confirmation dated in the doc; the never-copied
  bullet now names the snapshot as the one sanctioned exception (ADR 0005
  framing, replaced wholesale by an adopter).
- **C4 [fixed]** — the boundary sentence sharpened to the reviewer's wording:
  the calibration *functions* without the personal context; the understanding
  that turns rules into judgement stays person-local, which is why the
  instance, not the snapshot, is what the agent serves.

Reviewer honesty note, kept load-bearing: the reviewer disclosed it could not
unsee system-injected person-level context and answered A1 from repo-citable
inference chains only — every A1 step checks against the repo alone. A future
re-run of this review would be cleaner with a context-stripped reviewer
harness; noted, not blocking.
