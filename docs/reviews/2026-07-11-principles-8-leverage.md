# Review — PRINCIPLES §8 "Leverage — invest now to stop paying later"

**Scope:** the §8 doctrine addition (commit `cf447fb`, 2026-07-11, session 33),
review-owed by the ceremony-calibration rule (doctrine text; flagged, not
self-certified). The ROADMAP brief asked for a light, fresh-context read:
placement/consistency (appended-not-renumbered; the §7 "numbered last" note vs
a new §8; the ties to §2 DRY / §7 codify / EVIDENCE §14) and whether the
"not a licence to gold-plate" discipline genuinely bounds the principle.

**Reviewer:** Fable, cold fresh-context session (2026-07-11), read-only; fixes
applied by the coordinating session after the verdict. Verdict below verbatim.

---

**VERDICT: PASS-WITH-FINDINGS**

Reviewer: cold, fresh-context, read-only. Scope: PRINCIPLES.md §8 (commit
`cf447fb`, 2026-07-11), per the ROADMAP review-owed brief.

**Placement — appended-not-renumbered is correct.** Verified against the
pre-change text (`git show cf447fb~1:docs/method/PRINCIPLES.md`): §7 was
genuinely the last numbered principle before this commit, §7 does
cross-reference §5 ("Mechanism in §5"), and external `PRINCIPLES §N` citations
exist (e.g. ros bearings, the 2026-07-10 method-layer review brief cites
"§1–7" repeatedly). Inserting mid-list would have broken real references;
appending was the right call. §8 is also correctly *not* added to the
precedence ladder — it is bounded by rule 6 and operationalised by the
"One-off or recurring?" situation test, which is the right mechanism.

**Findings:**

1. **[Minor] Stale header claim — PRINCIPLES.md intro.** "What follows
   resolves collisions *among* the design principles §1–7." False since this
   commit: §8 exists and participates in collisions — the new "One-off or
   recurring?" situation test resolves a §8-vs-KISS collision by name. This is
   §6's own cautionary case ("when a learning is refined, sweep the stale
   claims in the *same* commit") violated by the commit that sits two sections
   below it. Fix: change to "§1–8". One-line edit.

2. **[Minor] §7's "Numbered last" opener now false.** "Numbered last for
   stability, logically first: the axiom the rest serves." §8 is now numbered
   last. The irony is that this sentence's own rationale (positions are
   stable, so numbers can be cited) is exactly *why* §8 was appended rather
   than inserted — the decision honours the sentence while falsifying it.
   Fix: rephrase to something position-independent. Do not renumber anything.

3. **[Low, optional hardening] "Real recurrence" carries no evidence bar.**
   The discipline paragraph demands "*real* recurrence or a *real* avoided
   class... never an imagined future need", and the precedent pair (codified
   verb vs throwaway migration script) anchors it. But "real" is asserted, not
   tested: a motivated builder can promote predicted recurrence to "real" in
   prose. §6 already holds that every claim carries its test; one clause
   applying that here would close the gap — e.g. "the strong case is
   *observed* recurrence (it has already recurred); a predicted recurrence is
   a claim like any other and carries its test." Genuinely optional — the
   existing text plus the situation test's bidirectional-waste framing already
   bounds the principle adequately; this is a hardening, not a hole.

**Ties — all verified to hold.** §2 DRY: "one-source is this principle applied
to facts" is coherent with §2's own framing of DRY as the EVIDENCE §9 /
PROPAGATION one-source rule. §7 codify: the codified-removal-verb case §8
cites is §7's own case, correctly marked "(§7)" as a generalisation, not a
duplication. EVIDENCE.md §14 ("An instrument you built is a source — it must
not lie for you"): §8's paraphrase — build it tested and honest, not a fragile
script that moves the cost to debugging — matches §14's substance exactly.
PROPAGATION.md's thin-anchor-fat-pointer pattern exists as cited.

**The gold-plate discipline genuinely bounds the principle.** It names the
failure mode in both directions (over-build = KISS/rule-6 waste; hand-repeat =
§8 waste), refuses imagined need, and explicitly denies §8 any shortcut
through §0–§2 — so it cannot be read as blanket permission to build tooling.
Finding 3 is the only softness, and it is low-severity. Premise-attack not
warranted: the principle is real, decided practice, not doctrine invented for
a heading.

**Grounding.** Strong, as the brief predicted, and verified rather than
taken: the scan instruments exist in `tools/` (leakscan, licenscan,
secretscan, linkscan, pins — each with a test file), and I re-ran
`python3 tools/leakscan.py --selftest` live: "selftest OK", exit 0. The
thin-anchor-fat-pointer mechanism is a real, documented pattern, and the
codified-removal-verb case pre-existed §8 in §7 (extracted from ros practice,
per the method-layer review). The session record
(`../sessions/2026-07-11-33-leverage-principle.md`) is honest about provenance
(Mike stated the principle) and about its own review-owed status. Not
verified: I did not run the full CI floor or the other scanners' selftests
(one representative live run per the light-review scope), and I did not check
ros-side inheritance — the session record defers that to the children's next
pin bump, which is out of scope here.

---

**Disposition (2026-07-11, same day):** all three findings **[fixed]** — intro
now reads "§1–8"; §7 opener rephrased position-independent ("Last of the
original seven — positions here are stable so §N citations hold — but
logically first"); the observed-vs-predicted recurrence clause added to the §8
discipline paragraph (finding 3's optional hardening, taken). Gate cleared.
