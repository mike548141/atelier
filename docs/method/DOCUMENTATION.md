# Documentation — transfer intent and capability, at the reader's altitude

*Documentation exists to transfer intent and capability to a reader at the
moment of need, at that reader's altitude. Everything else — form, depth, tone,
medium — is mechanism that follows from three questions: **who** is asking,
**what** they are asking, and **how** they consume. "Great" is therefore not one
quality; it is the **right artefact for each cell** of a matrix. A docstring, a
man page and an error message do not compete — each answers a different question
for a different reader at a different moment, and each is good exactly when it
serves its cell. (Authored 2026-07-20 off Mike's brief; anchored on Diátaxis +
a consumer axis; tiki is the named exemplar. review-owed — see foot.)*

This binds every child repo. atelier holds the **doctrine**; a child holds its
**application** — `ros`/tiki is the named proving ground (its ROADMAP carries the
application half). Most of what follows is **extraction, not invention**: the
pieces already exist as scattered case-law (`RECORD.md`, `EVIDENCE.md §9`,
`COMMUNICATION.md`, `CONVENTIONS.md`, and `ros` `PRINCIPLES.md §6`), and this
doc's job is to unify them and name the two axes they were missing.

## Two axes

Every documentation artefact sits at the intersection of two independent axes.
Get both right and the artefact — its form, its depth, its tone — picks itself.

### The what/who — anchor on Diátaxis

For "who is asking and what are they asking", we adopt **Diátaxis** rather than
reinvent it: a proven, widely-used framework, and adopting it is the
least-invented path (the house rule is to ground, not to fabricate a private
vocabulary where a good public one exists). Its four modes map onto the
audiences directly:

| Diátaxis mode | Orientation | Serves | The reader's question |
|---|---|---|---|
| **Tutorial** | learning | newbie | "get me started, hold my hand" |
| **How-to** | task | operator | "help me accomplish *this*" |
| **Reference** | information | expert | "give me the exact fact/flag/contract" |
| **Explanation** | understanding | developer | "help me understand *why* it is like this" |

Two audience splits fall out of the four modes: **newbie vs expert** (tutorial
vs reference) and **operator vs developer** (how-to/reference vs explanation).
The developer cell is the one most often dropped: the reader who *extends* the
tool needs `ARCHITECTURE`/`PURPOSE`-class explanation, why-comments, and ADRs —
a distinct need, easily conflated with the *expert user* who only needs deeper
reference. Name it separately.

Extend Diátaxis where it is silent; do not contradict it. The consumer axis
below is the principal extension.

### The how — the consumer axis (what Diátaxis lacks)

Diátaxis assumes a human reader. atelier's readers are not all human, and the
consumer determines **form**:

- **Human** — reads prose, scans structure, wants narrative and the *why*,
  tolerates ambiguity and infers. Served by tutorials, curated `--help`, a
  legible README, worked examples.
- **AI** (a coding agent, an LLM operator) — reads prose *at scale*, and rewards
  density, self-containment, single-source (no conflicting facts to reconcile),
  tight linking, and grounding (so it can trust a claim's strength). A hybrid:
  consumes prose, but rewards machine-legibility. This consumer is an
  intelligent **tier-1** principal — it holds intent and can answer elicitation.
- **Orchestrating software** — does not read prose at all. Its documentation
  **is the contract**: `--json` schemas, exit codes, stable flag names, error
  codes. A **tier-2** consumer — served by the *same* machine contract as the
  AI, kept complete/stable/versioned, but with no ability to ask a follow-up
  question. For software, **backward-compatibility is documentation currency**:
  a broken schema is a documentation failure even if every prose word is
  perfect.

*Grounding.* This axis is a generalisation of `ros` `PRINCIPLES.md §6`
(legibility — "the principal may be a machine", Mike, 2026-07-15; the tier-1/
tier-2 split, 2026-07-17): the machine contract carries the **entire** result
(findings, provenance, what-would-prove-it-wrong, what was skipped), never a
lossy subset of the human render, and **the human view is a *rendering* of the
machine truth, never the reverse.** tiki's `fleet.json schema_version` is the
worked instance. This doc lifts that from one tool's design principle to
house-wide documentation doctrine.

## What "great" means per cell

The two axes together; "great" is the artefact that serves the cell, nothing
grander.

| | **Human newbie** | **Human expert** | **AI operator** (tier 1) | **Orchestrator** (tier 2) |
|---|---|---|---|---|
| **Needs** | a guided path, examples first | fast reference, zero ceremony | accurate one-liners, predictable grammar | stable schemas + exit codes |
| **Served by** | tutorials, curated `--help`, README | man page, full per-command help | docstrings/help as index, GLOSSARY, grounded canon docs | `--json` contract + exit codes, versioned |
| **Fails when** | drops them into reference | pads with ceremony | facts conflict across sources | the schema changes silently |

## The artefact inventory

Every form of documentation is one of the cells above; there is no artefact that
serves "everyone". Map each to its mode and its consumer:

| Artefact | Diátaxis mode | Primary consumer |
|---|---|---|
| Docstring | reference (+ *why* at the site) | AI + human (developer) |
| Inline comment | explanation (the *why*) | human + AI |
| CLI `--help` (terse) / help examples | reference / how-to | human + AI (operator) |
| man page | reference (full) | human (operator/expert) |
| README | tutorial onramp + map | human + AI (newbie) |
| Canon docs (PURPOSE / ARCHITECTURE / GLOSSARY) | explanation | human + AI (developer) |
| Wiki / tutorials / examples | tutorial + how-to | human (newbie → operator) |
| **Error messages** | how-to, *in situ* | human + software |
| **Machine contract** (`--json` schemas, exit codes) | *the contract* | **software** |
| Changelog | reference (history) | human + AI |
| ADR / session / decision records | explanation (why-history) | human + AI |

Two cells earn emphasis because they are the ones most often left out of "the
docs":

- **Error messages are documentation** — read at the highest-stress moment of
  need, when the reader is stuck. A good one states *what is wrong, why, and what
  to do*, as data where a machine consumes it (named cause + evidence + remedy,
  not a bare stack trace). They deserve the design attention the wiki nobody
  reads gets. (This is `ros`'s diagnose discriminator applied to prose: an error
  that guesses is worse than one that says "I don't know, here's what I checked".)
- **The machine contract is documentation-for-software** — `--json` shapes and
  exit codes are documented and **versioned like an API**, because the
  orchestrator cannot ask a follow-up question. tiki's man page carries a
  dedicated `MACHINE OUTPUT` section — byte-stable JSON, "machine mode never
  prompts", per-verb schemas — which is the exemplar of this cell done right.

## The principles the doctrine rests on

Several already exist elsewhere; this doc unifies them and points, rather than
restating (principle 1, applied to itself).

1. **One fact, one home; everything else points.** A fact lives once and is
   cross-referenced by a stable identifier. Duplicated docs do not merely cost
   maintenance — they **diverge silently**, and a divergent doc is worse than
   none (the update lands in one copy, the reader trusts the other). This is
   `EVIDENCE.md §9` and `PROPAGATION.md`'s one-source rule, applied to every
   documentation artefact.
2. **Same-commit currency.** The doc that governs a thing changes in the *same
   commit* as the thing — the man-page rule (`RECORD.md`, docs-as-code)
   generalised to every artefact. Currency is **structural, not aspirational**;
   a stale doc is a lie the moment it merges. For the software consumer this
   becomes the contract's version discipline (schema_version moves with the
   schema).
3. **Docs are claims, and claims carry their proving rung.** "fixtured /
   real-kernel / live-proven" applies to a sentence exactly as to code. Honest
   docs say what is *known* versus *believed*, and a not-yet-built thing is
   *labelled a stub*, never written in the present tense (`00-APEX.md`;
   `EVIDENCE.md`). A stale or over-strong doc is an over-strong claim about the
   code — an apex violation, not a tidiness lapse.
4. **The consumer sets the form; the fact still lives once.** The same fact may
   render three ways — narrative for the human, dense-and-linked for the AI, a
   schema for software — but per principle 1 the renderings **point to one
   source**; they do not re-state it. Form varies; truth does not fork.
5. **Meet the reader at the point of need, at their altitude.** The highest-
   leverage documentation reaches the reader where they already are (the error
   at the failure site, the docstring at the call site, the `--help` at the
   prompt), pitched at their level — not a level-up in a wiki they must go find.

## The AI consumer — the record doctrine is already this standard

The disciplines that make documentation good for an AI consumer are the ones
atelier *already* wrote for its own record: **resume-cold** (self-contained
enough to reconstruct the *why* from the repo alone), **one-fact-one-home**,
**grounding** (claims tied to evidence), **absolute dating**, **dense linking**.
`RECORD.md` and `EVIDENCE.md` wrote the AI-reading spec without naming the
consumer. So the "AI operator" cell is largely **extraction, not new work**:
point to those docs; do not re-derive them here.

## The vendor-docs seam — point, never mirror

A child's docs cover **its own intent and its live-proven deltas** from the
platform it wraps. For the platform's own semantics, they **point** to the
vendor's docs; they never mirror them.

- **Why not mirror.** Mirrored vendor docs (a) rot the day the vendor changes,
  (b) make you the maintainer of someone else's documentation, (c) break
  one-fact-one-home across an org boundary, and (d) re-tread the model-catalogue
  copyright question — same answer as there: **ship the harvester, not the
  harvest.**
- **What the child *does* own — the seam.** The quirks, version-specific
  behaviours, and API gotchas it has *live-proven* against the platform — the
  places the vendor docs are wrong, silent, or surprising. This is earned,
  grounded knowledge: exactly the class atelier prizes, and precisely what a
  vendor cannot document for you.
- **Version-pin the pointer.** Vendor docs move underneath you, so a pointer
  carries its own proving rung: "verified against RouterOS 7.x", not a bare
  link (principle 3, applied to the seam itself).

*Exemplar — tiki ↔ RouterOS/MikroTik.* tiki's man page `CAVEATS` documents a
live-proven delta the vendor does not surface: boards at the flash floor
(free-hdd exactly 20480) take changes **RAM-only and silently revert** — "run
`tiki health` before trusting an apply to stick." That is the seam done right: a
grounded, tiki-owned quirk, not a re-explanation of what a RouterOS bridge is.
The pattern generalises across the fleet — a container repo ↔ Traefik/Authentik
docs, an image repo ↔ its base-OS docs: **the wrapper documents the wrapping,
never the wrapped.** (Honest gap, for the application pass to close: tiki.1's
`SEE ALSO` currently points only to its own sibling docs, not to MikroTik's —
adding the version-pinned vendor pointer is exactly what this doctrine drives,
and it lives in ros's half, not here.)

## Relationship to COMMUNICATION.md

`COMMUNICATION.md` and this doc share one root — *calibrate to the reader* — and
split on durability and audience-knowledge:

- **COMMUNICATION** is the *ephemeral, in-conversation* channel to **one known
  person**, calibrated from that person's dated "working with me" profile.
- **DOCUMENTATION** is the *durable, in-repo* artefact read **cold by unknown
  future consumers** — human, AI, or software — none of whom are in the room to
  clarify. So it cannot lean on a known reader; it must declare its altitude and
  carry its own context.

## Why this is doctrine, and how it propagates

A stale or mis-aimed doc is not untidiness — it is an over-strong claim about the
code (principle 3), which the apex forbids. And the whole operating model assumes
a session resumes **cold**, which is only true if the documentation carries the
state at the altitude each consumer needs. This doc is **canonical here** and
binds every child; children apply and prove it (tiki first), append their own
deltas, and never silently contradict it (`PROPAGATION.md`). Per house
sequencing, **mechanism before content**: this doctrine is authored and reviewed
before it is stamped across the fleet, and the tiki application pass is the
review's evidence base.

---

*review: **WARRANTED** — doctrine that binds every child repo, and it reverses/
unifies scattered case-law. Author (this session, Opus) does **not** self-review
(`REVIEW.md` rule 3/4, review-brief independence). Mike has commissioned a cold
review of this draft **against any competing draft, to reconcile** — so this is
one candidate, deliberately not the only one. Queued `⏳` on the ROADMAP.
Grounding read this session (read-only, ros @ `806eb10`): `tiki/docs/tiki.1`
(MACHINE OUTPUT, CAVEATS, SEE ALSO), `ros PRINCIPLES.md §6`,
`EVIDENCE.md §9`, `RECORD.md`.*
