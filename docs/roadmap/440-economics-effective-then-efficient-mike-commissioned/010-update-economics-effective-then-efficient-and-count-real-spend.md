- [ ] 🎯 **Update the doctrine's economics so "the right model for the job"
      means effective first, then efficient, with every real-money cost
      counted, not only the plan's** `[M][doctrine]`. Mike commissioned this,
      2026-11-12. Verbatim:

      > I need to update the doctrine economics to take Claude budgets vs
      > actual expenditure over and above plan costs into account more. This
      > principle is still the same, we use the right model for the job and to
      > be right the model must be effective which means capable of
      > understanding and delivering the quality required that the specific
      > job requires. There is a big difference between capabilities to do
      > research, to develop code, to test code, to provide insights, and to
      > write great papers (advice, reports, presentations etc).
      > Secondly to be right it must be the most efficient model for the job,
      > and that does not always mean the cheapest per token which is where we
      > need to consider are we using Claude's weekly budget, platform API and
      > other things that cost real money over and above my Claude plan at the
      > time. That includes costs outside Claude like GitHub actions minutes
      > etc. Sometimes a "more expensive" model like fable will deliver a job
      > cheaper and to the same or better quality than "cheaper" models like
      > opus, sonnet, and haiku.

      **The filing session's reading, beneath his words and not a
      substitute for them.** Two tests, in order. (1) *Effective*: the model
      can understand the job and deliver the quality that job needs. Job
      kinds differ in what they need (he names research, writing code,
      testing code, producing insight, writing papers such as advice,
      reports and presentations). (2) *Efficient*: among the models that
      pass test 1, the one that costs least **for the whole job**, which is
      not the same as the least per token. His principle is unchanged; this
      sharpens what "right" means.
      **What the house says today, and where it pulls the other way.**
      - `ECONOMICS.md` § *Match the model to the job* quotes his 2026-09-19
        ruling, *"the cheapest model that can do a good job is the one that
        should be used for every job including orchestration"*, and then
        prices by **billing state per marginal token** (plan-included,
        capped, usage-billed). Read at face value, "cheapest" can be taken
        as cheapest per token. His new words say it is not, so the two need
        reconciling in his words, not the filing session's.
      - The same section says building belongs on the cheapest-drawing
        tier and review on the capable tier. That splits seats by *kind of
        work* in two (build, review). He names at least five kinds of work
        with different capability needs, so the two-way split is coarser
        than his point.
      - The billing states describe the Claude plan. His words add costs
        the states do not cover by name: the weekly allowance as a budget
        to be spent well, the platform API, and non-Claude metered spend
        such as GitHub Actions minutes. `ECONOMICS.md` § *The compute pool
        — CI minutes* sits "beside the model spend" and does not tie the
        two into one choice. § *Cost is the lowest precedence* says cost is
        optimised last and never against correctness; it does not say what
        counts as cost.
      **Owed, not built:**
      - (a) 🎯 the wording and its home, quoting him. Candidates:
        `ECONOMICS.md` § *Match the model to the job* (the rule and the
        billing states) and § *The compute pool — CI minutes* (so minutes and model choice are
        weighed together), plus a pointer from `session-onramp` where a
        session picks a model.
      - (b) a statement of what "effective" is per kind of work: capable of
        the understanding and the quality **that job requires**. The
        doctrine stays general; which exact model clears which bar is
        person-local and lives in the operator's private repo, never here.
      - (c) a statement of what "efficient" counts: tokens, the weekly
        allowance, platform-API spend, and other metered services, summed
        over the job (retries, rework and review included), against what the
        operator actually pays beyond the plan at the time.
      - (d) **evidence for "sometimes the dearer model is cheaper".** His
        sentence is a claim about outcomes. The doctrine should not state
        it as a rule until a measured case supports it. The repo's own
        usage tool can give per-job spend by model; the job-level
        comparison (same job, two models, cost and quality) is not yet
        measured.
      - (e) how a session decides in the moment: what it checks, what it
        records, and when the choice is the principal's. A rule that
        raises spend beyond the plan is a spend question (the floor's
        "spending money") and stays his.
      **Review.** Doctrine about spend and model choice, written by
      sessions that spend it: its wording earns a rule-4 pass before it
      binds.
