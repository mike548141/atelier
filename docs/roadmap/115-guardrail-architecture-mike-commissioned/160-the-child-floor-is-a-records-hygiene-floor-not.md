- [ ] **The floor a child inherits is a records-hygiene floor, and the children
      are where the real risk lives.** atelier holds text. The children hold the
      credentials, the domain data and the live systems. Yet of the 15 checks a
      child inherits, **3 guard that surface** — the two boundary scanners and
      the publish-surface check. Eight guard record integrity, three guard prose
      style, one guards licensing. The weighting is inverted against where harm
      would actually land.
      **And almost nothing in a child has ever been caught by a guard in the
      child.** Across every recorded child incident, the catcher was Mike
      asking, a cold review, a commissioned sweep, or a live failure — very
      rarely a gate. The one class the gates did catch was found at adoption,
      firing on content that had been sitting there for weeks.
      **Three specific holes, each measured rather than reasoned:**
      **(a) The unsoftenable boundary is softenable after all.** The
      personal-data scanner is declared in code to have no advisory form,
      because the boundary *"is not a re-baselining matter"*. But a path glob
      filters before the rule set runs, so a repo-wide glob retires it entirely
      — and several children carry one. Each is reasoned and cites a decision
      record; the point is architectural, not a criticism of those calls. **The
      ignore file outranks a property the code declares inviolable.** That is
      worth either honouring in the ignore-file loader or striking from the
      code's claim, because right now the code says something untrue.
      **(b) The strongest guard has the weakest reach.** The full personal-data
      cover depends on a machine-local term list that must never reach a CI
      runner — correctly. So the whole-tree plane runs structurally only, and
      the complete cover exists on one laptop. The plane that backstops a
      skipped hook and a fresh clone is the degraded one. This is honestly
      declared in the output; it is still the inverse of where cover is needed.
      **(c) Destructive-operation safety is directive only, everywhere.** The
      verified-restore-point rule has no mechanism in atelier or any child, and
      the doc carrying it says of itself that a rule living only in a session's
      memory protects nothing. No destructive-op incident is on record, so this
      is an unexercised control rather than a demonstrated failure — which is
      the best time to fix it and the reason nobody has.
