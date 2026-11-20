- [x] **DOCUMENTATION doctrine — what great documentation is, per audience and
      consumer (Mike, 2026-07-20, raised in ros off the tiki CLI-UX review).**
      (**claimed 2026-07-20 1423 UTC** — Mike ruled "1–3 I accept your
      recommendations"; the taker applies DD1–DD4, wt: `atelier-rulings-apply`.)
      **Cold pass RAN 2026-07-20**
      (`reviews/2026-07-20-1355-documentation-draft-cold.md`): **PASS — 0 MAJOR
      · 2 MEDIUM · 2 LOW**; every grounding claim re-ran true at ros `806eb10`.
      🎯 **Mike's rulings owed:** DD1 (table drops the developer cell) · DD2
      ("map directly" overclaim) · DD3 (inventory misses tests / commit
      messages / diagrams) · DD4 (no competing draft exists — decide whether
      this cold pass discharges the reconcile intent). No-MAJOR ⇒ closes
      terminal on ruling. tiki application half still owed (ros's lane).
      Mike: *"be clear on what great documentation looks like, and its
      purpose"* — for **audiences** developer vs operator × newbie vs expert,
      and **consumers** human · AI · orchestrating software — covering
      *"everything from docstrings to the --help screen on a CLI app … to the
      man file and a wiki. And any other form of documentation you can think
      of."* Belongs HERE because it binds every child repo; **tiki (ros) is
      the named exemplar / real-world proving ground** (its ROADMAP carries
      the application half, same day). Scope for the method doc
      (`method/DOCUMENTATION.md` when authored): the audience×consumer
      matrix and what "great" means per cell · the artefact inventory
      (docstrings · CLI --help · man pages · README · canon docs
      (PURPOSE/ARCHITECTURE/GLOSSARY-class) · wiki/tutorials/examples ·
      error messages as documentation · the machine contract (--json
      schemas, exit codes) as documentation-for-software · changelogs ·
      session/decision records) · the single-source/pointer rule (a fact
      lives once; everything else points) · same-commit currency (docs
      change in the commit that changes the behaviour — the man-page rule
      generalised) · honesty in docs (claims carry their proving rung) · and
      the **third-party-docs seam**: a child's docs state its own intent +
      live-proven deltas/quirks, and POINT to vendor docs (RouterOS,
      VirtualBox, …) — never mirror them. Existing part-truths to absorb,
      not duplicate: RECORD.md (records), the CLI-docs standard cycle
      (ROADMAP-DONE), CONVENTIONS.md, ros PRINCIPLES §6 legibility.
      *review: WARRANTED — doctrine; author, Fable-review, THEN propagate
      (mechanism-before-content). The tiki application pass is the review's
      evidence base.*
      **Decisions to date (Mike, 2026-07-20):** (1) **anchor on Diátaxis**
      (tutorial · how-to · reference · explanation) and extend as needed —
      the least-invented path; (2) the **consumer axis** (human · AI ·
      orchestrating software) is the extension Diátaxis lacks; (3) fold the
      independently-surfaced deltas — the **developer** audience is a distinct
      cell Diátaxis's *explanation* mode serves, easy to conflate with
      expert-*user*; atelier's **record doctrine already IS the AI-reading
      standard** (resume-cold, one-fact-one-home, grounding, absolute dating —
      so that cell is *extraction*, not invention); **version-pin the vendor
      pointer** ("verified against RouterOS 7.x", not a bare link).
      **Draft authored 2026-07-20 (Opus) at `method/DOCUMENTATION.md`** —
      registered in `method/README.md` (15), grounded read-only against
      ros @ `806eb10` (tiki.1 MACHINE OUTPUT/CAVEATS/SEE ALSO, PRINCIPLES §6,
      EVIDENCE §9, RECORD). Mike commissioned this as **one candidate**, to be
      **cold-reviewed against any competing draft and reconciled** — so unlike
      the earlier note, a competing draft *is* deliberately open. *review
      state: `⏳` queued — a non-author session takes it (REVIEW.md rule 4),
      reconciles the drafts, and applies. Author does not self-review. tiki
      application (ros half) still owed and is the review's evidence base.*
      **CYCLE CLOSED 2026-07-20** — Mike ruled all counsel accepted; applied `87af9f9` (terminal, no-MAJOR). Verdict + decisions: `reviews/2026-07-20-1355-documentation-draft-cold.md`.
