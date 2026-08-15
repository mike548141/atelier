- [ ] 🤔 **Per-transcript topic capture — idea to consider (Mike, 2026-08-02;
      no design pass yet).** Capture the themes/topics discussed in each
      transcript, so a specific one can be found later without rereading them.
      Companion to the search strand, not a duplicate of it: the designed
      search ([`cctranscript.search.design.md`](../../../instruments/cctranscript.search.design.md))
      answers *"which transcripts contain this literal term/regex"* — it needs
      you to already know a string; topics would answer *"which session was
      the one about X"* when only the subject is remembered. Recall vs grep.
      **One grounding check taken before capture (2026-08-02): there is no
      existing field to lift.** The live store carries **zero**
      `"type":"summary"` records across every project's logs, so a topic
      layer must be *derived* from the transcript, not read off it.
      **Open questions for the design pass (not answered here):**
      - Source: a model pass per transcript (real token cost, real quality)
        vs log-derived heuristics — first user prompt, repo, files touched,
        tool mix — free but shallow. Measure what the cheap version actually
        retrieves before paying for the expensive one.
      - Owner and shape: ccarchive stamping a topics sidecar at archive time
        (the transcript is stable by then, and the shape rhymes with the
        `.meta.json` capture class above) vs cctranscript deriving on demand.
      - Consumption: how search and `--list` use it — a `--topic` filter, a
        line in the header, or both.
      Nothing designed or decided; capture only.
