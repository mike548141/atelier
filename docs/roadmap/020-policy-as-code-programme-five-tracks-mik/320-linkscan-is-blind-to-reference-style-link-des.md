- [ ] 🔥 **`linkscan` is blind to reference-style link destinations, and says
      "every internal link resolves" anyway.** Handed up from a child session
      under the queue-never-deliver rule, and **re-verified here by
      reproduction 2026-08-16** rather than accepted. The `_LINK` regex is
      anchored on the literal `](` of an inline destination, so the whole
      CommonMark reference family is never *extracted* — not merely left
      unresolved.
      **The probe.** One file, one broken inline link plus five broken
      reference-style links — full `[t][ref]`, collapsed `[ref][]`, shortcut
      `[ref]`, image `![alt][ref]`, and a reference to a real file with a
      non-existent anchor. Result: **exactly one finding**, the inline one.
      Delete the inline link and the same file reports
      `✓ linkscan clean — every internal link resolves.` at **exit 0**, with
      five broken links present. Both finding kinds — `missing-file` and
      `missing-anchor` — go through the same hole.
      **Why this is the sharpest instance of a class already queued.** It is
      not silence; it is an *affirmative claim naming the exact property it
      did not check*. That is the vacuity shape filed at
      [`115/130`](../115-guardrail-architecture-mike-commissioned/130-a-guard-reports-whether-its-rule-fired-at-all.md)
      — "clean" and "never looked" rendering identically — and this is the
      first instance found in an **enforced** guard rather than an advisory
      one. A broken record pointer in reference form cannot fail a commit.
      **A correction to the report as received, and it makes the gap worse.**
      The child's account said `pathscan` catches these. Partly. Probed here:
      `pathscan` **does** flag a reference definition whose destination
      carries a slash, and **does not** flag one that is a bare filename —
      while the control in the same probe (a bare path mention) fired
      correctly, so its silence is a real miss and not a scope artefact. So
      the compensating cover is partial, and on at least one child's hook
      plane it is warn-only besides.
      **Suggested shape, from the child, and it is a good one:** validate the
      **definitions** rather than the usages. `^ {0,3}\[label\]:\s+<dest>`
      already yields a destination that can go straight through the existing
      resolve path. It needs no bracket matching, and it dodges the real
      hazard of the obvious alternative — a shortcut-form matcher fires on
      ordinary prose (`[square brackets]`, `arr[0]`, a citation `[1]`).
      Confirmed in the same probe that those three shapes carry no definition
      and stay correctly silent. The residue a definition-only fix leaves is
      the *undefined label*, a lower-stakes class better named in the
      docstring than chased.
      **Also a docstring defect.** The module names the inline forms as in
      scope and rules `[[wiki]]` links out **by design**, and says nothing
      about reference style — so the omission reads as coverage rather than
      as a stated limit.
      **Exposure, as reported and not verified here** (the child owns its own
      tree, work-locality): 36 reference definitions in that repo, 11 of them
      in its roadmap's ADR pointers, none currently broken. Exposure, not
      damage.
