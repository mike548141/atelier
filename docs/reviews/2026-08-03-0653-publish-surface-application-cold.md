# Brief — publish-surface application cold pass (rule 4)

- **Work under review:** the publish-surface application delta — commit
  `62bb1c1` (`docs/build/REPO-STANDARD.md` standardise step 2,
  `docs/method/TOOLBOX.md` residual clause,
  `docs/build/templates/claude/settings.local.json` narrowed), which applied
  Mike's rulings PS1–PS3 from the 2026-08-02 publish-surface delta cold pass.
- **Review shape:** application review (REVIEW.md § *Applying decisions to
  doctrine*). The edited doctrine is reviewed at HEAD and findings committed
  **before** the prior verdict (`2026-08-02-2210-publish-surface-delta-cold.md`)
  is opened; reconcile follows. The residual exposure — the delta's commit
  message carries the author's account of PS1–PS3 — is named, not denied.
- **Spawn provenance (rule 4):** taken from the ROADMAP `⏳` queue by a
  session Mike spawned generically ("do any work that requires Fable,
  including reviews"). This session authored neither the publish-surface
  delta, the verdict, nor this application; the application's author (the
  2026-08-02 taker session) spawned nothing here. Reviewer tier: Fable.
- **Disclosed exposure:** the mandated onramp (SESSIONS.md tail) included the
  author session's addendum summarising this application before the taker
  could choose not to read it. Named for auditability; the file-level detail
  was met cold.
- **Scope:** the doctrine text at HEAD (is it true, coherent with its
  neighbours, and free of the defect class it fixes), the template as
  something `create-repo` stamps into children, and cross-surface coherence —
  the four-places problem PS1 exists because of. Non-goals: re-litigating the
  ⓑ untrack ruling itself.
- **Lenses:** all four. Review deep, not fast.

---

# Verdict — PASS · 0 MAJOR / 0 minor / 2 notes

**Provenance (restated per rule 4):** reviewed by a Fable session Mike
spawned generically; the reviewer authored neither the publish-surface
delta, the 2026-08-02 verdict, nor this application. Findings committed
before the prior verdict was opened; reconcile follows beneath.

**What was verified at HEAD, not read from the delta's account:**

- **PS1** — REPO-STANDARD's standardise step 2 now instructs the *untrack*
  form, and it matches the skill's stamped copy near-verbatim
  (`skills/create-repo/SKILL.md:236`). **The PS1 class is closed at HEAD,
  swept rather than assumed:** a tree-wide sweep of every `.claude/settings`
  mention outside records (REPO-STANDARD ×2, TOOLBOX, SKILL ×2, the gitignore
  template) finds no surviving mandate-site — every surface now states the
  untrack rule or the ignore rule, coherently.
- **PS2** — the TOOLBOX residual clause is *accurate*: the seed template
  (`templates/claude/settings.json`, ~35 grants) is tracked and public, so
  "the estate default remains mapped; untracking hides divergence, not the
  default" is a true statement of the live tree, not an aspiration.
- **PS3** — the published `settings.local.json` template carries
  `defaultMode: acceptEdits` only; no `allow` block survives anywhere — a
  tree-wide grep for a bare `"Bash"` grant outside records returns nothing.
  Both templates parse as JSON.

**Lens 1 (approach).** The application's shape — fix the sentence, name the
residual where the cost is already named, narrow the published grant — is the
minimal faithful form of the three rulings, and the step-2 parenthetical
telling a standardiser *why* pre-2026-07-29 repos will still be tracking the
file is exactly the right context at the point of use.

**Lens 4 (security/privacy).** `/security-review` discharged with grounds:
landed doctrine-text delta; the only pending change is this brief (the SL2
trap). Weighed manually: the delta strictly *reduces* published capability
grants; the one disclosure it leaves is PSA1 below.

## Findings

**PSA1 (note) — the PS2 residual clause says "the seed template", singular;
two templates are published.** Post-PS3, `settings.local.json` still
publishes one fact: the estate's default session mode (`acceptEdits` —
edits apply without per-edit approval). The PS2 residual argument (the
default is mapped; divergence is hidden) extends to it unchanged, but the
clause as written names only the allowlist template. Counsel: one word —
"templates" — plus a parenthetical naming the mode bit, next time TOOLBOX
is open; not worth its own commit.

**PSA2 (note) — nothing verifies a child's seeded ignore file downstream.**
The skill's step 3 already frames copying-both-files as "a check that the
seeded ignore file was not trimmed", but for standardised-not-scaffolded
repos the only guard against a re-tracked allowlist is `publishscan` at the
child's next pin bump — which is the designed answer (P2 exists for exactly
this), recorded here so the dependency is explicit: **PS1's fix propagates
by pin bump, not by this commit.** No action beyond what the board already
tracks.

## Faithfulness to the rulings (written at reconcile, below)

- **PS1 ✅** — the counsel was "delete the clause, add the skill's
  pre-2026-07-29 note to the canonical text"; the application did exactly
  that, and the sweep above confirms no sixth surface survives.
- **PS2 ✅** — the counsel was one sentence in TOOLBOX's named-cost
  paragraph; the application wrote the residual in full, including the
  sharpest form ("a repo whose live allowlist never diverges from seed is
  still described exactly"), which is the prior verdict's own observation
  carried into the doctrine honestly.
- **PS3 ✅** — the counsel offered narrow-or-mark-deliberate; the ruling
  chose narrow, and the applied template keeps `acceptEdits` only. The
  `WebSearch` grant fell with the `allow` block — entailed by the ruling,
  coverage-checked (no `allow` block remains anywhere in the templates).

## Reconcile (prior verdict opened after the findings were committed)

Nothing overturned. PSA1 turns out to sit exactly on the prior PS3's closing
clause (the local template "is outside publishscan's allowlisted-template
reasoning, argued for `settings.json` only") — the application narrowed the
grant but the residual-naming clause still reads singular; PSA1 stands as the
precision residue of that, not a new class. Verified while reconciling:
`publishscan` does not flag the tracked local template
(`templates/claude/` ≠ `.claude/` at any depth), so no fixture change is
owed. PSA2 matches the prior verdict's own pin-bump framing.

**Disposition: terminal.** 0 MAJOR ⇒ the publish-surface cycle **closes**
per REVIEW.md's no-MAJOR rule. PSA1–PSA2 are residue for Mike (rule 3);
counsel recorded, nothing applied by this session.

## Decisions (Mike, 2026-08-03, plain-language walk-through)

- **PSA1 [fixed]** — ruled fix-at-next-TOOLBOX-touch; the rulings-application
  records commit was that touch. The residual clause now says "templates",
  and names the `acceptEdits` mode-bit disclosure the local template
  carries.
- **PSA2 [accepted]** — pin-bump propagation accepted as the designed
  mechanism; the dependency is recorded here and in the roadmap, no new
  work item.
