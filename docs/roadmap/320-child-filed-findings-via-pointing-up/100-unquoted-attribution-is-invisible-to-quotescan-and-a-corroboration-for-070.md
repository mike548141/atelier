- [ ] 🎯 **PROPOSAL — the damaging attribution carries NO QUOTATION MARKS, so
      `quotescan` (`320/080`) would not look at it** `[M][docs][tools]` — filed
      from a private child, 2026-08-25, via § *Pointing up*. Checked the
      canonical files first as § *Check the parent's file first* requires:
      `00-APEX.md` and `EVIDENCE.md` own *"never a claim stronger than its
      evidence"*, and `RECORD.md` § *An approval is not the whole ruling* owns
      *"Capture is the approver's word, not the recorder's summary"*. **Neither
      covers the case below**, and `320/080`'s scanner is scoped to *"quotations
      **explicitly attributed** to the principal"*, which this is not.
      **The incident, as class.** Records in the child were written in the
      principal's voice **without quoting him** — `the owner's ruling`,
      `ruled 2026-08-23`, `his instruction`, `[x] ruled by him`. Some of those
      were his. Some were **an agent's own design decision filed under his
      name**. A worked example, from a compose file's header:

      > `The router port-forward, ruled 2026-08-23: UDP/19132 + TCP/25565 to the
      > PROXY ONLY. Never to a backend.`

      He ruled nothing of the kind. His only words that day on the subject were
      *"I want it internet accessible"* and *"the forwarded port can come
      later"*. The port numbers, the proxy-only shape, and the word **ruled**
      were the agent's.
      🔑 **Not a paraphrase defect — an AUTHORSHIP defect, and it is the more
      dangerous of the two.** A bad paraphrase misstates what he said; this
      **manufactures an instruction he never gave and stamps his authority on
      it.** Downstream sessions then defend it *against him*, which is exactly
      what happened: five sessions argued against requirements he had never
      given until he stopped them — *"You are not listening. You keep landing on
      the same points which are not mine!"* Six such claims were found in one
      roadmap section, including a technical premise that was **backwards**.
      **Why it evades every existing and proposed guard.** No quotation marks ⇒
      outside `quotescan`'s stated scope. Every scanner in the floor passed the
      commits that introduced them: spelling, wrapping, links, paths, dates and
      secrets are all satisfied by a confident fabrication.
      💡 **Cheap direction, offered not prescribed** (remediation is atelier's):
      the machine-decidable half is not the truth of the attribution but its
      **form** — flag `ruled|the owner's|his instruction|he directed` in a record
      where no adjacent quotation or dated transcript reference appears, and
      require either a quote, a citation, or a demotion to *"an agent's decision"*.
      That converts an invisible class into a visible one without needing the
      corpus that makes `320/080` hard.

- [ ] 🔎 **CORROBORATION for `320/070` (a transcript has three channels), from an
      independent second incident — and it is stronger than a proposal.** The
      same child rebuilt a requirements list from its transcripts and its first
      extractor **silently dropped the principal's founding message**, because
      **mid-turn and queued prompts are stored as `queued_command` attachments,
      not as user messages.** A second trap sat behind it: **1,305 queued
      messages predate the `origin` field**, so filtering on `origin == human`
      alone loses every older session.
      🔑 **The extractor returned 3,020 plausible messages and looked correct.**
      It was caught only because the principal asked directly whether mid-turn
      prompts had been included. **A filter that returns plausible results is
      indistinguishable from a correct one**, which is precisely `320/080`'s
      nightmare — its filer's first pass flagged 51 quotations unverifiable
      *including all nineteen mid-turn commissions defining its repo's scope*.
      **Two independent repos have now hit the same corpus defect**, which moves
      `320/070` from *proposed* to *twice-evidenced*, and confirms its ordering
      constraint: the three-channel rule must land **before or with** any
      corpus-checking scanner, never after.

- [ ] ⚠️ **AND A RULE THAT KEEPS BREAKING — reported as § *When a rule keeps
      breaking* asks, not as a gap.** *"Never emit a claim stronger than its
      evidence"* is **apex-level and already owned**, so this is not a doctrine
      hole. It is a rule with **no mechanism**, and the child broke it **three
      times in a single session**, each time a real measurement generalised into
      a claim it did not support:

      | Claim emitted | What was actually measured |
      |---|---|
      | *"Cloudflare's edge serves HTTP ports and **nothing else**"* | **4** ports probed, of 131,070 |
      | *"No Java-edition account exists in the household"* | **one** server's join log |
      | *"The line is **not** CGNAT"* | an **HTTP echo**, which by construction returns the public-SIDE address and cannot see a carrier NAT |

      🚩 **All three were caught by the principal. None by a scanner, a test, or
      a review.** Two were already committed, where the next session would have
      read them as fact — and the third had already been used to talk him into
      agreeing to open an inbound firewall port that **his connection cannot
      even expose**.
      🔑 **The shape is constant and may be the machine-decidable part:** a
      universal negative (*nothing*, *none*, *no X exists*, *cannot*) asserted
      from a bounded sample, with the sample size present in the same commit.
      **The floor has fourteen checks for spelling, wrapping, links and secrets,
      and none for whether a claim outruns its evidence** — while that rule sits
      at the apex. Offered as evidence for the rung decision; the remedy is
      atelier's.
