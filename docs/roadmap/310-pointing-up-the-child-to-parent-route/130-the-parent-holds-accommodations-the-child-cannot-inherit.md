- [ ] 🎯 **CLASS — the parent holds accommodations its children cannot inherit,
      and neither side can see the asymmetry from where it stands.** Three
      independent instances in one evening, 2026-09-20, none of them looked for:
      two reported by private children over the peer channel and one found here
      by getting it wrong. Filed as the class rather than three defects, because
      the three fixes are unrelated and the pattern is not.

      ## The three instances

      **(1) Scope declarations.** Atelier narrows `wrapscan` to the doctrine
      surface in `.atelier-floor.json` (WS1, Mike's option A, 2026-07-23), so
      `docs/roadmap/` is outside the gate **here, by ruling**. A child with no
      such declaration runs the scanner unscoped over `docs/**`. Measured in
      one: `wrapscan` absent from its `scope` block, and **237 of 324 board
      item files carrying a `wrapscan:allow` marker — 73%**. The child pays a
      hand-written marker per item where the parent pays one line of config.
      *And the substitute is worse than the accommodation:* each marker carries
      a written reason, is edited by hand on every new item, and that child has
      a recorded instance of `secretscan` reading a long allow-reason as a
      secret. The parent's declaration has no such failure mode.
      ⚠️ *The reporting child's own caveat, carried:* it counted the markers,
      it did not judge them. A ruling that turns on the number should sample
      them.

      **(2) Naming freedom.** Atelier is public, so a private child filing a
      hand-up here must file **class-only** — no repo name, no paths from its
      own tree — because a private child naming itself in a public parent is
      the same disclosure as a public parent naming a private root, read from
      the other end. Both children that filed today reached this independently
      and neither was asked to. The parent can name itself in its own records
      at no cost; the child pays anonymity, and a finding stripped of its
      repo is a finding harder to act on.

      **(3) Instrumentation — the sharpest of the three, and a child's
      framing.** `stampscan` cannot check a child at all (`320/160`):
      `source=` may not resolve outside `--root`, and a compliant child's copy
      reds by construction anyway because the mandatory placeholder fills are
      not obtainable by deletion. So **the parent's guards can see the parent;
      a child's guards can see everything except the one thing that binds it
      to the house.** Its only compliant move is a hand check it must remember
      to run — and on 2026-09-20 that hand check, in one child, caught two
      absent floor bullets and a stale recipe that was *actively wrong* across
      a 288-commit delta. No tool would have caught it, because no tool can
      run there.

      ## Why it is a class and not three items

      Each instance is a parent-local accommodation — a config narrowing, a
      posture, a working instrument — that is **invisible from both ends**.
      The parent cannot reproduce the child's pain: atelier is *immune by
      declaration* to instance (1), which is precisely why `010/130` spent
      weeks reasoning about the wrong mechanism (`wrapscan`'s exemption logic)
      before a child measured the real one. And the child cannot see that the
      parent has an accommodation at all — it experiences only a rule that
      costs more than the doctrine says it should, which reads as its own
      failure to comply cleanly.

      🔑 **The diagnostic that generalises:** when a child reports a house rule
      as expensive and the parent cannot reproduce the expense, **suspect an
      accommodation the parent holds and has not propagated** — before
      suspecting the child. That inversion is the finding.

      ## The ask

      Decide whether `PROPAGATION.md` owes a rule here, and of what shape.
      Candidates, not a design, and deliberately not chosen:
      **(a)** parent-local narrowings are declared where children can read
      them, so a child can adopt or refuse deliberately rather than never
      learn they exist; **(b)** a parent may not hold an accommodation it has
      not offered downstream — strict, and probably too strict, since some are
      genuinely local; **(c)** nothing changes but the diagnostic above is
      written down, so the next instance is recognised in one read instead of
      several sessions.

      ⚠️ **Not established:** how many *other* accommodations exist. Nobody has
      enumerated the parent's local config against what children carry —
      `.atelier-floor.json`'s `scope` block alone narrows three scanners, and
      only one of the three surfaced today. A census would turn this from three
      anecdotes into a count, and has not been run.
