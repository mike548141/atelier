# 2026-07-21 · 0736 UTC · the three review-owed strands taken (Fable)

**Prompt:** "Do the review work… There are parallel sessions so take
precautions and use a worktree" — the three *Doctrine — review-owed* items.
All three claimed on `main` (`8d3fa9f`) before work began; work in
`wt: worktree-review-owed-triple`. A parallel session's claim (`4bc0b52`,
man-page rollout) landed mid-session on a different item — yielded to, lane
respected.

## Strand 1 — fleet re-stamp of the reviews template ✅

nova, numen, shed — the three children carrying the drifted, pre-trigger copy
of `docs/reviews/README.md` — re-stamped from the template at the closed
review-trigger/sizescan cycle's HEAD. Per child: synced, tree verified clean,
`<atelier-path>` filled `../atelier`, no-placeholder grep green, both
`../atelier/docs/method/` pointers verified resolving, committed + pushed
(nova `13f6970`, numen `d271ae0`, shed `118fc69`; each child's own scan hooks
green). ros never carried the file — adding one is that repo's session's call
at pin bump, not this re-stamp's. Item → ROADMAP-DONE.

## Strand 2 — the review-line artefact (closes F6) ✅ ⏳ queued

Delta `fa7a90f`, one reviewable thing: ADR template + decisions README carry
a **Review** field; ROADMAP template states the convention for
direction-setting entries; new `tools/reviewscan.py` (presence-only,
`docs/decisions/` only, boundary 2026-07-21 — frozen records never flagged;
roadmap headings deliberately unlinted on the 0820 record's grounds) wired
into pre-commit.sample, atelier `ci.yml`, child `floor.yml`. Suite 284→293,
selftest + red/green legs bite-proven, live scan green at HEAD. `REVIEW.md`'s
"enforcement is structural" re-stated per surface — mechanical for decision
records, honestly conventional for roadmap sections. Deliberation in
`decisions/2026-07-21-0744-review-line-artefact.md` (dogfoods the field);
0820 ADR addendum appended. Doctrine by function ⇒ **⏳ rule-4 pointer
queued** (refs only); this author spawned nothing.

## Strand 3 — REACH/AUTONOMY backlog (H1–H8 + residuals) ⚠️ split

**Applied (agent-grade — alignment to already-ruled doctrine, cosmetics):**
H8 the browser-fetch README pass — (b) the stale pre-A4 absolute realigned to
the shape-picks-rungs-1–2 split, (a) the credential-boundary paragraph now
names `REACH.md` as canonical instead of "owed to doctrine — see ROADMAP",
(c) "operator's explicit permission" re-anchored to *a grant the principal
alone makes* (the doctrine's decided wording) — plus the two over-length
REACH.md lines rewrapped (no word changes).

**Not applied — 🎯 the principal's rulings owed (REVIEW.md rule 3: these
change doctrine wording; the counsel below is the author's position,
labelled, applied only on ruling):**

1. **H1 (MEDIUM) — operator ≠ principal is nowhere covered.** *What:* add one
   clause to REACH.md's "Why the two halves are one doc": where the operator
   is not the principal, the exposed session/vault is the *operator's own*,
   and a grant belongs to whoever owns the store. *Why:* team adoptions exist;
   the README already drifted on exactly this seam. *Impact:* public doctrine
   stops assuming solo operation; no behaviour change for this estate.
   **Counsel: take.**
2. **H2 (MEDIUM) — "existing cookies … are fair game" licenses cookie
   export.** *What:* scope to "fair game *in place*, driven through the
   ridden session; reading or exporting session state (cookie stores, tokens)
   is touching the store — secrets floor." *Why:* a cookie is a minted bearer
   credential; the literal sentence licenses copying the jar into a
   disposable engine — rung-5 reach with rung-3 isolation, no operator
   present. *Impact:* closes the sharpest gap the batch left; the
   browser-fetch README's mirror sentence gets the same scoping on ruling.
   **Counsel: take.**
3. **H3 (MEDIUM) — the categorical browser-store "never" now argues against
   the doc's own two criteria.** *What:* scope the test — *purpose* governs
   which stores; *mint-vs-ride* governs which acts; saved-login autofill is a
   mint whatever the store's purpose. *Why:* post-A1, a dedicated bot-login
   profile passes both stated criteria yet the sentence says never, with no
   grounds — an agent reasoning from the doc's own test can argue past it.
   *Impact:* the rule becomes derivable instead of arbitrary; no change to
   what's actually allowed. **Counsel: take.**
4. **H4 (MEDIUM) — only the principal's line is drawn.** *What:* add a short
   residual: whether to defeat a deliberate wall at all is its own judgement
   with its own floor (AUTONOMY's people/safety, legal, the target's terms);
   the ladder governs *how* to escalate, never *whether* the target is fair
   to take. *Why:* public doctrine reading "escalate until through" sanctions
   defeating any wall so long as no credential is touched. *Impact:* one
   paragraph; aligns with the repo's residuals-named-not-denied habit.
   **Counsel: take.**
5. **H5 (LOW) — "blocked" undefined; soft blocks are the common case.**
   *What:* one sentence — blocked = the rung cannot return the resource in
   usable form (hard error, challenge, or demonstrably degraded/empty
   content). *Impact:* stops both the stalled-literal and the
   descend-liberal misreads. **Counsel: take.**
6. **H6 (LOW) — rung-1/2 equivalence stated as engine-agnostic fact,
   grounded in one instance.** *What:* hedge the two sentences ("in the
   worked instance" / "typically"). *Why flagged separately:* this challenges
   the decided A4/A5 wording itself, so it is explicitly not the author's to
   soften. *Impact:* honesty hedge only. **Counsel: take.**
7. **H7 (LOW) — "never a standing grant" vs "temporary or permanent" reads
   as contradiction.** *What:* one connecting clause — standing reach goes
   through the provisioned path (next bullet), never through a standing
   ride. *Impact:* joins two already-true sentences. **Counsel: take.**
8. **R1 (LOW, reconciliation residual) — AUTONOMY's "direct handling"
   doesn't literally catch machinery-mediated repurposing.** *What:* extend
   the secrets bullet's head: "any direct handling of a stored value — and
   any *use* of one beyond its provisioned purpose, machinery-mediated or
   not." *Why:* REACH stops it explicitly; an AUTONOMY-alone reader could
   miss the stop. *Impact:* the two docs state one rule again.
   **Counsel: take.**

Application of any taken rulings is itself a doctrine edit — per the applied-
batch precedent it lands with a ⏳ pointer for a non-author pass (or rides
the open review-line cycle's terminal rules if Mike prefers).

## Close state

Worktree merged to `main`; claims released (strand 1 → DONE, strand 2 → ⏳,
strand 3 → rulings-owed item); suite 293 OK; scans green; children pushed.
