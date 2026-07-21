# Review brief: the applied REACH batch — A1–A8 into REACH.md, A1's carve-out into AUTONOMY.md

**Scope:** the single application commit (subject `method: apply the REACH
re-review decisions…`, 2026-07-13) — `docs/method/REACH.md` (all eight
findings) and `docs/method/AUTONOMY.md` (the secrets-floor carve-out that is
A1's other half). The decisions applied are Mike's, 2026-07-13: **all eight
[fixed]** (`reviews/2026-07-12-reach-rereview.md`).

**Why this review exists:** REVIEW.md's cycle rule — applying decisions to
doctrine is itself a doctrine edit and earns a cold pass. The applier authored
neither REACH nor the verdict, but it did author the applied wording, so this
brief binds under the independence rules.

**Sequencing (rule-2 residual, named not denied):** review the edited doctrine
at HEAD and commit your findings *first*; open the re-review verdict file and
this commit's hunks only after. The delta unavoidably carries the verdict's
decision stamps.

**Your first act:** name the load-bearing assumptions yourself (lens 1). This
brief's account of the work is itself attackable. The cycle closes on a
no-MAJOR pass (the principal's 2026-07-13 ruling); remainder decided into the
backlog, no further ceremony.

---

## Deferred — author-seeded questions (open only after your own attack surface is committed)

1. A1 was fixed in **both** docs — do REACH's provisioned-store bullet and
   AUTONOMY's secrets carve-out now state *one* rule, or two rules that merely
   sound alike? Try to construct a case that passes one doc and fails the other.
2. A2 scopes riding to retrieval — does the new sentence actually bind rung 4,
   or only rung 5? Is "the exposure the operator deliberately made" resolvable
   by an outside adopter?
3. A4 split the descent rule (shape picks 1–2, block gates 3+) — does the
   ladder's rung-2 charter text still agree with the new rule, and does any
   other sentence still assert the old absolute rule?
4. A5 restricts the isolation axis to rungs 3–5 — does the rung-4 second-axis
   sentence still hang together after the reframe?
5. Did the applied wording drift from what Mike actually decided (all eight as
   the reviewer's stated fixes), and is any drift an improvement honestly owed
   a label, or silent scope-creep?

---

# Verdict — cold pass on the applied REACH batch (commit `5cf1436`)

**Reviewer:** cold-context agent, no prior involvement; findings H1–H8 durably drafted before opening the commit's verdict-file hunks, `reviews/2026-07-12-reach-rereview.md`, `reviews/2026-07-12-reach.md`, or this brief's deferred section. Instance proof re-run per REVIEW.md: `instruments/browser-fetch/test_server.py` via the pre-existing venv interpreter — **11/11 pass, nothing installed**. (The README's live-fetch claims — firefox/webkit, rung-4 CDP — were not re-run: they need real browsers driven; gap stated, not glossed.)

## Verdict: **PASS-WITH-FINDINGS**

The application is faithful: all eight decided fixes are present in the HEAD text, in substance and mostly in the verdicts' own recommended words, and the two docs now state the provisioned-credential rule as one rule from two sides. The doctrine's spine — cheapest-first ladder, purpose-of-storage test, ride-not-mint — survives a fresh hostile read, its cross-references all resolve at HEAD (EVIDENCE §13, SECRETS/ACCESS, ADR 0006 addendum verbatim), and the reproducible proof reproduces. **No MAJOR finding**, so under REVIEW.md's stopping rule the cycle closes here; H1–H8 below are backlog material, four MEDIUM and four LOW, and none unseats an applied decision — the sharpest ones (H2, H3, H7) sit on seams the batch itself tightened but did not fully close.

## Load-bearing assumptions I attacked (my own list)

1. "Operator" and "principal" are the same person — asserted once, defined nowhere.
2. Ride vs mint is operationally distinguishable — in particular that "existing cookies are fair game" cannot be read to license exporting session state.
3. The purpose-of-storage test is the actual governing rule — no later sentence silently overrides it.
4. A "block" is legible — block-gated descent has a detectable trigger.
5. The rung 1–2 equivalence ("clears no new walls") generalises beyond the one worked instance.
6. The only line reach can cross is the principal's credential line — no other party's "no" needs drawing.
7. Cross-references resolve at HEAD — checked; all resolve.
8. The instance proof holds — re-run; it does.

## Findings

### H1 — MEDIUM — operator/principal conflation is an unstated solo-operator assumption
REACH.md uses "operator" throughout the ladder (rungs 4–6) and "principal" throughout the boundary; the only join is the assertion in "Why the two halves are one doc" that "the operator running the browser there is the principal". Neither term is defined, and nothing covers operator ≠ principal — a team adoption where a colleague runs the rung-4/5 browser: whose vault does the boundary guard, and may a non-principal operator's exposure of *their own* session count as a grant only "the principal" can make? The instance README already drifts on exactly this seam — it licenses the line-crossing on "the **operator's** explicit permission" where doctrine says a grant is "the **principal's** alone to make". REVIEW.md sets the house precedent for this class of gap (its rule-3 solo-operator caveat names the degenerate case rather than assuming it). **Fix:** one clause defining the terms or stating the assumption — where operator ≠ principal, the exposed session/vault is the operator's and the grant belongs to whoever owns the store — and align the README's wording.

### H2 — MEDIUM — "existing cookies … are fair game" licenses more than riding
A cookie *is* a minted bearer credential. The doc means "use the session in place, through the ridden browser", but the literal parenthetical also covers reading/exporting the cookie store — e.g. copying the operator's cookie jar into a rung-3 disposable engine, a tempting move that buys rung-5 reach with rung-3 isolation and no operator present. AUTONOMY's secrets floor would catch the export ("reading … moving … any direct handling of a stored value") — but only if the reader classifies a cookie as a stored credential, which REACH's own sentence has just told them is "fair game". A2's applied fix scopes what the agent may *do through* a ridden session; it does not close taking session state *out of* one. **Fix:** "fair game *in place*, driven through the ridden session; reading or exporting session state (cookie stores, tokens) is touching the store — secrets floor."

### H3 — MEDIUM — the categorical browser-store exclusion now contradicts the doc's own two criteria, ungrounded
The boundary's test is explicit: "*why the credential was stored*, not where it sits". The second bullet then overrides it categorically: a browser's saved-credential store is "**never** itself the provisioned path … even a dedicated one stood up for the agent's use." Post-A1, the tension is sharper, not softer: take a dedicated agent profile the principal deliberately provisions with a bot-account login — the purpose test passes, and A1's new "through the resolving machinery" condition is arguably satisfied by autofill (the browser resolves the credential into the form; the agent never sees the value). Both stated criteria pass, yet the sentence says never, with no grounds given. The real grounds presumably exist (a saved login mints unbounded *new* sessions vs a ride the operator implicitly scoped; a browser store has no per-use grant or audit surface) — but unstated, the rule reads as arbitrary, and an agent reasoning from the doc's own criteria could argue past it. (The 2026-07-12 re-reviewer probed this sentence and found it coherent — against the *pre-A1* text, before "resolving machinery" became a stated criterion.) **Fix:** one grounding clause, or scope the test: purpose governs *which stores*; mint-vs-ride governs *which acts*, and saved-login autofill is a mint whatever the store's purpose.

### H4 — MEDIUM — one line is drawn; the other party's line is never named
The title promises "the line you won't cross", and the doc draws exactly one: the principal's credentials. But rungs 3–5 exist specifically to defeat anti-bot walls — some of which are the *resource owner* saying no (ToS, paywalls, rate limits). Public, shareable doctrine reading "escalate until through; the only line is your own credential store" sanctions, to an outside adopter, defeating any wall so long as no credential is touched — and rungs 1–3 the agent walks alone. The repo's own habit is residuals named, not denied. **Fix:** a short residual — whether to defeat a deliberate wall at all is its own judgement with its own floor (AUTONOMY's people/safety, legal, the target's terms); the ladder governs *how* to escalate, never *whether* the target is fair to take.

### H5 — LOW — "blocked" is undefined, and soft blocks are the common case
Descent is "block-gated: step down only when the current rung is actually blocked" — but anti-bot walls usually fail soft (200 with a JS shell, a challenge page, decoy content). A literal reader stalls at a soft-blocked rung; a liberal one treats thin content as licence to descend. A4 split the rule; it didn't define its trigger. **Fix:** one sentence — blocked = the rung cannot return the resource in usable form (hard error, challenge, or demonstrably degraded/empty content).

### H6 — LOW — rung 1–2 equivalence stated as general fact, grounded in one instance
"Same anti-bot profile as rung 1 … clears no new walls" and the intro's "clear the same walls" are true of the worked instance but presented as engine-agnostic doctrine. In other instances rung 1 is a provider-hosted fetch (datacentre IPs, own renderer) whose wall profile differs from a local raw client in both directions. The header's "untested beyond it" hedge doesn't reach these sentences. This challenges the *decided* A4/A5 wording, so it is the principal's to weigh, not a fidelity defect. **Fix:** "in the worked instance" or "typically".

### H7 — LOW — "never a standing grant" (rung-5 ride) vs "temporary or permanent" (credential grant) reads as contradiction
A seam the batch itself created: A2's applied sentence says a rung-5 ride is "never a standing grant" while A6's applied taxonomy, one bullet down, lets the principal grant "temporary or permanent" — the stronger act grantable, the weaker not. The resolution is present (standing access *moves* the credential into the provisioned path) but never connected to the ride sentence, so an adopter can read a flat contradiction. **Fix:** one clause — "standing reach goes through the provisioned path (next bullet), never through a standing ride".

### H8 — LOW (harvest, outside this commit's files) — the instance README lags the doctrine it seeded
`instruments/browser-fetch/README.md`: (a) still frames its credential boundary as "a rule owed to `method/` doctrine — see ROADMAP", though REACH.md now exists and has survived two reviews — the pointer should name it; (b) still states the pre-A4 absolute ("Always start at the top and step down only when the current rung is blocked"), which A4's shape-picks-rungs-1–2 split superseded; (c) carries H1's "operator's explicit permission" drift. **Fix:** a small README alignment pass.

## Fidelity check — 8/8 faithfully applied

| Finding | Applied at HEAD | Fidelity |
|---|---|---|
| A1 | REACH provisioned-store bullet narrowed to provisioned-use-through-resolving-machinery; AUTONOMY secrets bullet gains the matching carve-out | ✅ near-verbatim to the recommended shape; adds a grounding parenthetical (SECRETS right-plane rule) — clarifying, not scope-creep |
| A2 | "riding licenses retrieval… state-changing act… its own action under the AUTONOMY.md floor… rung-5 ride scoped… never a standing grant" | ✅ verbatim in substance; "not a standing grant" → "**never** a standing grant" — immaterially stronger, no label owed |
| A3 | stale instance-status parenthetical deleted; rot-proof pointer sentence added | ✅ |
| A4 | shape picks rungs 1–2; block-gates from rung 3 down | ✅ |
| A5 | isolation axis restricted to engine rungs 3–5; top half named honestly | ✅ "equal wall-clearing power, different request shape" paraphrases the recommended "processing/capability" — same substance |
| A6 | standing grants enrol; temporary grants expire, never enrol; record the grant, never the value | ✅ near-verbatim |
| A7 | EVIDENCE §13 cross-reference ("reach picks the pipe, evidence picks the strength") | ✅; §13 verified present |
| A8 | honesty clause ("generalised from that one worked instance — engine-agnostic by construction, untested beyond it"); third verb realigned | ✅; ADR 0006 addendum wording ("extend what the teammate can *do*") matched verbatim |

**Deviations:** two, both immaterial and labelled above (A2 "never", A5 paraphrase); neither is scope-creep nor owed a drift label. **Cosmetic:** the A2 and A5 splices left two unwrapped over-length lines in REACH.md (the "escalation principle is general" line and the "never a standing grant" line) — rewrap when next touched.

## Reconciliation with the deferred questions

1. **A1 — one rule or two sound-alikes?** Substantially one rule; both docs require *provisioned purpose* + *resolving machinery*, and my constructed cases fail both docs together. One residual edge (found post-reveal, so recorded here, not as a committed finding): machinery-mediated **repurposing** — the tooling resolves the value, agent never touches it, but for an unprovisioned purpose — fails REACH explicitly ("repurposing … stays on the floor") while AUTONOMY's bullet head ("any **direct handling** of a stored value") doesn't literally catch it. An AUTONOMY-alone reader could miss that stop. One-word-class fix when next touched; LOW.
2. **A2 — binds rung 4 or only rung 5?** The retrieval-scoping binds every ridden session ("a ridden session", generic — rung 4 included); only the exposure-scoping clause is rung-5-specific, which is right (rung 4's profile is dedicated by definition). "The exposure the operator deliberately made" is resolvable in the instance (start the browser, bind the port) but its *duration* is unstated, and its resolvability for an outside adopter is the operator/principal question — covered by my H1.
3. **A4 — rung-2 charter agreement; any leftover absolute?** The charter agrees (fit-not-blockage wording matches the new split). No doctrine sentence still asserts the old absolute — but the instance README does, verbatim ("Always start at the top…"): my H8(b).
4. **A5 — does the rung-4 second-axis sentence still hang together?** Yes. It no longer hangs off a whole-ladder single-axis claim; "rungs 1–3 the agent walks alone; 4–6 cost the operator progressively more" stands on its own, and rungs 1–2 are explicitly placed above the isolation trade.
5. **Wording drift?** None owed a label — see the fidelity table; the two deviations are immaterial and the one addition (A1's grounding parenthetical) is the fix's own rationale inlined, an improvement that changes no scope.

My committed pass independently covered questions 3 and 4 (H8, and assumption 5's probe of the reframed axis text); questions 1, 2, and 5 are answered above.

---

**Decision (per the cycle rule, 2026-07-13):** no MAJOR — **cycle CLOSED** on
this pass; H1–H8 + the two reconciliation residuals consolidated onto one
ROADMAP backlog item (doctrine-substantive ones flagged as the principal's
when picked up). No further ceremony spawned, per the rule.

**Addendum 2026-07-21 — the backlog item taken; the principal ruled.** The
2026-07-21-0736 session applied the agent-grade findings (H8 [fixed] — the
README alignment pass, plus the two cosmetic rewraps) and put H1–H7 + the
machinery-mediated-repurposing residual (R1, reconciliation question 1) to
Mike with per-finding counsel. Mike ruled: *"I accept your recommendations on
all of those"* — **H1–H7 [fixed], R1 [fixed]**, applied 2026-07-21
(wt: worktree-reach-rulings-apply) in the reviewer's recommended shapes:
H1 operator/principal defined + team-adoption clause; H2 riding scoped to
in-place use through the ridden session (REACH + the instance README's mirror
sentence); H3 the two tests scoped — purpose governs stores, mint-vs-ride
governs acts, autofill is a mint; H4 the resource-owner residual named; H5
"blocked" defined incl. soft blocks; H6 rung-1/2 equivalence hedged to the
worked instance; H7 standing-reach-through-the-provisioned-path join; R1
AUTONOMY's secrets bullet extended to unprovisioned *use*, machinery-mediated
or not. This applies the rulings of a **no-MAJOR** pass ⇒ terminal
application, no further pointer (the close rule; same shape as `87af9f9`).
