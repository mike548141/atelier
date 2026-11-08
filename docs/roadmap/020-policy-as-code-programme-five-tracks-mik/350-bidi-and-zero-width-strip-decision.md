- [~] (claimed 2026-11-09-0330, wt: atelier-rr-722a-d1)
      🎯 **The bidi / zero-width spoofing set — strip, escape, or accept
      (FR3's named follow-on, ruled queued 2026-08-23).** The parse-seam
      strip now covers C0 + DEL + C1 (U+009B CSI alias included). Bidi
      overrides (U+202E and family) and zero-width characters can still
      visually reorder or disguise a board line on any Unicode terminal —
      but a blanket strip would also mangle legitimate RTL text in a
      child's `why`, so this is a decision with a real trade-off, not a
      widening to fold in silently: strip the override set only, escape it
      visibly, or accept and record. Mike's call when it comes up.
      review: not warranted — a queued decision item; the decision gets
      its account when put.
  - [ ] 💬 **Mike's answer, 2026-11-09 (to options queue run 722ac2e2 offered,
        after reading a one-line summary of each of twenty; an answer, not a
        ruling):** *"Approve all 20"* — the recommendation on this item
        stands approved: escape visibly the bidi override and isolate set (U+202A–202E, U+2066–2069); leave joiners alone.
