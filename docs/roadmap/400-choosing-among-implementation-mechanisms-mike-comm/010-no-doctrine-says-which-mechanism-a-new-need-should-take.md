- [ ] 🎯 **No doctrine says which mechanism a new need should take — four are
      already in use by precedent, none by rule.**
  - [ ] 🔑 **What's actually in play, named so the question is checkable.**
        At least six mechanisms exist in this estate today: a **policy-as-code
        guard** (a `tools/` scanner wired to the hook + CI floor); a
        **Claude Code Skill** (packaged in the atelier plugin, invoked by
        name or reached for autonomously); a **slash command**
        (`.claude-plugin/commands/`, deliberately invoked, no autonomous
        trigger); a **hook** (`PreToolUse`/`Stop`, intercepts without being
        asked — and `COMMUNICATION.md`'s Stop-hook episode is the one
        recorded lesson about a hook firing at the wrong moment, not a rule
        for choosing one); an **instrument** (`instruments/`, ADR 0006 —
        a read-only or credential-holding CLI a teammate runs directly); and
        a **custom MCP server** — adopted once (`browser-fetch`, third-party)
        but never built in-estate. Doctrine has criteria for choosing among
        **models** (`ECONOMICS.md`) and for one narrow membership question
        (instrument vs estate/infra, ADR 0006) — nothing chooses among these
        six.
  - [ ] 🔎 **`050/010` is the one existing gesture at this, and it stays
        narrow on purpose.** Mike's own captured idea there — handle trust
        failures "with a skill... not doctrine" — reasons from exactly the
        axis a general rule would need (enforced procedure vs. policy the
        agent applies to itself under the same pressure that caused the
        failure), but scopes it to one incident class and leaves even that
        undesigned ("can a skill actually gate anything, or is its value the
        deterministic checklist?"). This item is the general question that
        one is an instance of.
  - [ ] 🤔 **Candidate axes, none chosen, offered because "define when" is
        meaningless without naming what varies:**
    - **Must a violation be mechanically blocked, or is it a judgement call
      a session applies?** — the policy-as-code programme's own premise
      (directive first, enforced second) already answers this for guards
      specifically; the question is whether it generalises to "so build a
      guard" vs "so it's doctrine text" as the first fork.
    - **Does it intercept automatically, or get invoked deliberately?** — a
      hook fires without being asked (and can fire at the wrong moment, per
      the Stop-hook lesson); a slash command and most skills wait to be
      reached for; an MCP server sits available to be queried repeatedly
      mid-reasoning, which none of the others do.
    - **Who needs it — one repo, or the estate?** — a scanner is wired
      per-repo by the floor; a skill ships once in the atelier plugin and
      installs everywhere (when installed at all — see `180/010`, filed
      2026-09-14, on the plugin nobody had actually installed); an
      instrument is a standing binary on one machine.
    - **What does it cost to carry?** — `ECONOMICS.md` already prices skills
      as an episodic context cost; an MCP server carries a standing
      connection/maintenance burden neither a skill nor a scanner does; a
      scanner runs near-free on every commit once built.
  - [ ] 📎 **Not scoped to an answer.** These four axes are read out of
        existing fragments (GUARDS.md's enforcement premise, ECONOMICS.md's
        cost framing, `COMMUNICATION.md`'s hook incident, ADR 0006's
        boundary reasoning) rather than invented — whether they compose into
        one decision tree, and where it would live (`GUARDS.md`? a new
        `build/` doc? an ADR?), is the design work this item asks for and
        does not do.
