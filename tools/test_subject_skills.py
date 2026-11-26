"""Every /atelier: command is subject, space, action (board 450/020).

The principal, 2026-11-24, verbatim: "I think a space and for the default it
could have a menu or help screen a little like what /atelier does by itself.
We should make all the atelier command like this so its consistent". And:
"So something like /atelier:review by itself would be a help screen, not run
a command by default".

So the plugin ships one skill per subject (`skills/<subject>/SKILL.md`, a
router) and one file per action beside it (`skills/<subject>/<action>.md`,
front matter `action:`). These tests keep the router's table, the action
files and the router's description in step, keep the bare-subject menu wired,
and keep the retired hyphen names (his pick for them, "Nothing": no
forwarder, no signpost) out of the live surfaces.
"""
import hashlib
import json
import re
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
MENU = ROOT / "instruments" / "atelier-menu" / "menu.py"

RETIRED = ("review-brief", "review-drain", "review-plan", "work-run", "work-plan",
           "queue-run", "queue-plan", "fleet-sweep", "fleet-pins", "install-hook",
           "create-repo", "session-onramp", "scan")

# Live surfaces: what a reader is told to run or where a thing lives now.
# Records (sessions, reviews, decisions, board items, census, changelog) keep
# the names they were written with.
LIVE = ["README.md", "CLAUDE.md", "skills", "instruments", "tools",
        "docs/build", "docs/method", ".claude-plugin", ".githooks", ".github"]
RECORDS = ("docs/method/census/",)


ROOT_VAR = "${CLAUDE_PLUGIN_ROOT}"
PROMPT_REF = "docs/method/session-open/session-open-prompt.md"
_GIT_READS = [f'Bash(git -C "{ROOT_VAR}" rev-parse --show-toplevel)',
              f'Bash(git -C "{ROOT_VAR}" show HEAD:{PROMPT_REF})',
              f'Bash(git -C "{ROOT_VAR}" status --porcelain -- {PROMPT_REF})']


def expected_grant(subject: str) -> list:
    """Each router's allowed-tools, pinned (review 2026-11-24: RK29, a grant
    of any python and any git; RK19, a router widened to all of Bash stayed
    green). Reading the plugin's own files (RK1: an action's text is a read
    outside the session's directory; the leading slash makes the filled-in
    root absolute, `//...`, which a live probe showed the harness needs), the
    menu by its exact command, and for session and work the read-only git
    reads of the committed prompt; for session, the close's read-only report."""
    grant = [f"Read(/{ROOT_VAR}/**)",
             f'Bash(python3 "{ROOT_VAR}/instruments/atelier-menu/menu.py" {subject})']
    if subject in ("session", "work"):
        grant += _GIT_READS
    if subject == "session":
        grant += ["Bash(ccclose:*)", f'Bash("{ROOT_VAR}/instruments/ccclose":*)']
    return grant


def split_grant(value: str) -> list:
    """allowed-tools split at the commas between rules, not inside them."""
    out, depth, cur = [], 0, ""
    for ch in value:
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
        if ch == "," and depth == 0:
            out.append(cur.strip())
            cur = ""
        else:
            cur += ch
    if cur.strip():
        out.append(cur.strip())
    return out


def router_shape(d: Path) -> str:
    """A router with what is its own taken out (its name, description,
    argument hint, grant, table rows and the subject's word), so the six can
    be compared: the shared text is one text."""
    text = (d / "SKILL.md").read_text(encoding="utf-8")
    text = re.sub(r"(?m)^(name|description|argument-hint|allowed-tools): .*$", r"\1:", text)
    text = re.sub(r"(?m)^\| `[a-z]+` \| \[`[a-z]+\.md`\].*$\n", "", text)
    s = re.escape(d.name)
    text = re.sub(rf"(?m)^# /atelier:{s}$", "# /atelier:<subject>", text)
    text = re.sub(rf"`/atelier:{s}`", "`/atelier:<subject>`", text)
    return re.sub(rf'menu\.py" {s}$', 'menu.py" <subject>', text, flags=re.M)


# The shared router text, pinned whole (RK19: an added line telling the
# session to start a drain, and the plugin root said to be one level up,
# both stayed green). Change it deliberately: set this in the same commit.
ROUTER_SHAPE_SHA256 = "c1e6e1bdd77f1cd00638d0a85971bf42c15de7e6c588258dcb836d05718632a0"


def front_matter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    out = {}
    for line in text[4:end].splitlines():
        m = re.match(r"^([A-Za-z][\w-]*):\s*(.*)$", line)
        if m:
            out[m.group(1)] = m.group(2).strip().strip('"')
    return out


def subjects():
    return sorted(d for d in SKILLS.iterdir() if (d / "SKILL.md").is_file())


def action_files(d: Path):
    return {p.stem: p for p in sorted(d.glob("*.md"))
            if p.name != "SKILL.md" and front_matter(p).get("action")}


def unquoted(text: str) -> str:
    """The text with the principal's quoted words removed: an italic quote
    (*"..."*) keeps the names he used, verbatim, and is not a live use."""
    return re.sub(r'\*"[^"]*"\*', "", text, flags=re.S)


class SubjectSkills(unittest.TestCase):
    def test_the_six_subjects(self):
        self.assertEqual([d.name for d in subjects()],
                         ["fleet", "repo", "review", "session", "work", "worktree"])

    def test_no_commands_directory(self):
        self.assertFalse((ROOT / "commands").exists(),
                         "commands/ is retired: each command is a subject's action")

    def test_every_skill_dir_is_a_subject(self):
        for d in SKILLS.iterdir():
            if d.is_dir():
                self.assertTrue((d / "SKILL.md").is_file(), f"{d} has no router")
                self.assertTrue(action_files(d), f"{d.name} has no action files")

    def test_router_front_matter(self):
        for d in subjects():
            fm = front_matter(d / "SKILL.md")
            self.assertEqual(fm.get("name"), d.name)
            desc = fm.get("description", "")
            self.assertLessEqual(len(desc), 1024, f"{d.name}: description too long")
            self.assertIn("Pass the action as the first argument", desc)
            self.assertIn(f"bare /atelier:{d.name} shows this menu", desc)

    def test_description_carries_every_action(self):
        """One description does the work of several, so it must carry every
        action's word, or a request for that action never finds the skill."""
        for d in subjects():
            desc = front_matter(d / "SKILL.md")["description"]
            for a in action_files(d):
                self.assertRegex(desc, rf"\b{re.escape(a)}\b", f"{d.name}: {a}")

    def test_action_names_match_files(self):
        for d in subjects():
            for stem, p in action_files(d).items():
                self.assertEqual(front_matter(p)["action"], stem, str(p))
                self.assertTrue(front_matter(p).get("description"), str(p))
                self.assertNotIn("name", front_matter(p),
                                 f"{p}: an action file is not a skill; no name:")

    def test_router_table_matches_action_files(self):
        for d in subjects():
            body = (d / "SKILL.md").read_text(encoding="utf-8")
            rows = re.findall(r"^\| `([a-z]+)` \| \[`([a-z]+)\.md`\]", body, re.M)
            self.assertEqual(sorted(a for a, _ in rows), sorted(action_files(d)), d.name)
            for a, f in rows:
                self.assertEqual(a, f, d.name)
            self.assertEqual(front_matter(d / "SKILL.md")["argument-hint"],
                             " | ".join(a for a, _ in rows))

    def test_bare_subject_shows_its_menu(self):
        for d in subjects():
            body = (d / "SKILL.md").read_text(encoding="utf-8")
            self.assertIn(f"instruments/atelier-menu/menu.py\" {d.name}", body)
            self.assertIn("and do nothing else", body)
            # A headless run of "/atelier:review drain the reviews now" read
            # run.md and plan.md, taking "drain" for "run" (2026-11-24): the
            # router must say the word is exact and gates every read.
            self.assertIn("exactly one of the", body)
            self.assertIn("Read no action file and run nothing until", body)
            out = subprocess.run([sys.executable, str(MENU), "--root", str(ROOT), d.name],
                                 capture_output=True, text=True, timeout=30).stdout
            for a in action_files(d):
                self.assertIn(f"`/atelier:{d.name} {a}`", out)

    def test_router_holds_no_harness_placeholder(self):
        """Claude Code fills the arguments and plugin-root placeholders in a
        skill file as it loads it, so a router that wrote them literally to
        explain them read, as loaded, "wherever the action's file says ``"
        (found 2026-11-24 on a bare /atelier:session). Action files are read
        with Read and keep them; the router names them in words, and uses the
        plugin root only where its filled-in value is wanted: the grant, the
        line that states the root, and the menu command."""
        for d in subjects():
            body = (d / "SKILL.md").read_text(encoding="utf-8")
            self.assertNotIn("$ARGUMENTS", body, d.name)
            for line in body.splitlines():
                if ROOT_VAR in line:
                    self.assertTrue(
                        line.startswith("allowed-tools: ")
                        or line == f"`{ROOT_VAR}`"
                        or line == f'python3 "{ROOT_VAR}/instruments/atelier-menu/menu.py" {d.name}',
                        f"{d.name}: the plugin root in an unexpected line: {line[:80]}")

    def test_router_grant_is_pinned(self):
        for d in subjects():
            grant = front_matter(d / "SKILL.md").get("allowed-tools", "")
            self.assertEqual(split_grant(grant), expected_grant(d.name),
                             f"{d.name}: allowed-tools differs from the pinned grant")

    def test_action_files_carry_no_grant(self):
        """An action file is read, not loaded as a skill, so the harness never
        applies an allowed-tools there; one would read as a grant it is not."""
        for d in subjects():
            for p in action_files(d).values():
                self.assertNotIn("allowed-tools", front_matter(p), str(p))

    def test_routers_share_one_text(self):
        shapes = {d.name: router_shape(d) for d in subjects()}
        first = shapes["review"]
        for name, shape in shapes.items():
            self.assertEqual(shape, first, f"{name}: its router text differs from review's")
        digest = hashlib.sha256(first.encode("utf-8")).hexdigest()
        self.assertEqual(digest, ROUTER_SHAPE_SHA256,
                         "the routers' shared text changed: if deliberate, set "
                         "ROUTER_SHAPE_SHA256 to the new digest in the same commit")

    def test_router_states_the_root_and_the_first_word_rule(self):
        for d in subjects():
            body = (d / "SKILL.md").read_text(encoding="utf-8")
            self.assertIn(f"\n`{ROOT_VAR}`\n", body, d.name)
            self.assertNotRegex(body, r"levels? above|base directory>/\.\.", d.name)
            self.assertIn("the first of them is not an action here", body, d.name)

    def test_retired_names_are_gone_from_live_surfaces(self):
        names = "|".join(re.escape(n) for n in RETIRED)
        # A user-level path (`~/.claude/skills/<name>`) is the adopter's own,
        # not the plugin's layout, so it is not a use of a retired name.
        rx = re.compile(rf"/atelier:(?:{names})\b|(?<!\.claude/)\b(?:skills|commands)/(?:{names})\b")
        files = subprocess.run(["git", "-C", str(ROOT), "ls-files", "--", *LIVE],
                               capture_output=True, text=True).stdout.split()
        hits = []
        for f in files:
            if f.startswith(RECORDS) or f == "tools/test_subject_skills.py":
                continue
            p = ROOT / f
            if not p.is_file():
                continue
            try:
                text = unquoted(p.read_text(encoding="utf-8"))
            except UnicodeDecodeError:
                continue
            for n, line in enumerate(text.splitlines(), 1):
                if rx.search(line):
                    hits.append(f"{f}:{n}: {line.strip()[:100]}")
        self.assertEqual(hits, [], "retired command names in live files:\n" + "\n".join(hits))

    def live_files(self):
        files = subprocess.run(["git", "-C", str(ROOT), "ls-files", "--", *LIVE],
                               capture_output=True, text=True).stdout.split()
        for f in files:
            if f.startswith(RECORDS) or f == "tools/test_subject_skills.py":
                continue
            p = ROOT / f
            if not p.is_file():
                continue
            try:
                yield f, unquoted(p.read_text(encoding="utf-8"))
            except UnicodeDecodeError:
                continue

    def test_no_bare_retired_name_in_live_files(self):
        """RK22: the sweep saw a retired name only after /atelier: or skills/.
        A hyphenated old name standing alone in backticks is the same use."""
        names = "|".join(re.escape(n) for n in RETIRED if "-" in n)
        # A finding id from a review series named for an old skill
        # (`create-repo C3`) is a record's name, not a command.
        rx = re.compile(rf"`/?(?:{names})(?:`(?!\s+[A-Z]{{1,4}}\d)| (?![A-Z]{{1,4}}\d)[^`]*`)")
        hits = [f"{f}:{n}: {line.strip()[:100]}"
                for f, text in self.live_files()
                for n, line in enumerate(text.splitlines(), 1) if rx.search(line)]
        self.assertEqual(hits, [], "retired command names in live files:\n" + "\n".join(hits))

    def test_every_new_form_command_names_a_real_action(self):
        """RK22: a command written `/atelier:<subject> <word>` whose word is
        not one of the subject's actions points a reader at nothing."""
        known = {d.name: set(action_files(d)) for d in subjects()}
        rx = re.compile(r"`/atelier:([a-z]+) ([a-z|]+)")
        hits = []
        for f, text in self.live_files():
            # An author's note may name an option that was turned down.
            text = re.sub(r"<!--.*?-->", lambda m: "\n" * m.group(0).count("\n"),
                          text, flags=re.S)
            for n, line in enumerate(text.splitlines(), 1):
                for subject, words in rx.findall(line):
                    if subject not in known:
                        continue
                    bad = [w for w in words.split("|") if w not in known[subject]]
                    if bad:
                        hits.append(f"{f}:{n}: /atelier:{subject} {words}")
        self.assertEqual(hits, [], "commands naming no action:\n" + "\n".join(hits))


NUMBERS = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6,
           "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11,
           "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15,
           "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19,
           "twenty": 20}


def manifest_actions(desc: str):
    """The (subject, action) pairs a manifest description lists, as
    "(review: brief, plan and run; work: run and plan; ...)"."""
    m = re.search(r"\(([a-z]+: [^)]*)\)", desc)
    pairs = set()
    for part in m.group(1).split(";"):
        subject, _, words = part.strip().partition(": ")
        for w in re.split(r",\s*|\s+and\s+", words):
            if w.strip():
                pairs.add((subject, w.strip()))
    return pairs


class TheActionsTextsAndManifests(unittest.TestCase):
    """RK19: the plan, the run and the manifests were pinned by nothing."""

    def flat(self, rel):
        return re.sub(r"\s+", " ", (ROOT / rel).read_text(encoding="utf-8"))

    def test_review_plan_is_read_only(self):
        flat = self.flat("skills/review/plan.md")
        self.assertIn("Read-only from start to finish: no claim, no worktree, no "
                      "session started, no commit, no seal. A plan is never a seal.", flat)
        self.assertIn("never into a brief", flat)
        self.assertIn("review candidates", flat)

    def test_review_run_plans_every_run(self):
        flat = self.flat("skills/review/run.md")
        self.assertIn("Every run, before any pass starts, run `/atelier:review plan`", flat)
        self.assertIn("It is a gate, not a habit.", flat)
        self.assertIn("The words typed after `/atelier:review run` are the "
                      "principal's words for this run.", flat)

    def test_manifests_list_every_action_and_count_them(self):
        actual = {(d.name, a) for d in subjects() for a in action_files(d)}
        for rel, path in ((".claude-plugin/marketplace.json", ("plugins", 0, "description")),
                          (".claude-plugin/plugin.json", ("description",))):
            data = json.loads((ROOT / rel).read_text(encoding="utf-8"))
            for k in path:
                data = data[k]
            self.assertEqual(manifest_actions(data), actual, rel)
            m = re.search(r"\b(\w+) subjects holding (\w+) actions", data)
            self.assertTrue(m, rel)
            self.assertEqual(NUMBERS.get(m.group(1)), len(subjects()), rel)
            self.assertEqual(NUMBERS.get(m.group(2)), len(actual), rel)


class TheReviewTextsStayInStep(unittest.TestCase):
    """The pass prompts and run.md rule what an unattended drain does, and the
    two cold passes of 2026-11-25 found most of their sentences pinned by
    nothing (DV7, PK16: 13 and 12 mutants survived). Each test below names the
    finding it keeps and was seen to fail on the unfixed text."""

    def flat(self, rel):
        return re.sub(r"\s+", " ", (ROOT / rel).read_text(encoding="utf-8"))

    def test_the_pass_prompts_name_no_skill_path(self):
        """DV7 M10, M12: a pass runs in another repo, where a path into this
        skill does not resolve."""
        for name in ("orchestrator-prompt", "fold-prompt", "resume-prompt"):
            text = (SKILLS / "review" / f"{name}.md").read_text(encoding="utf-8")
            self.assertNotIn("skills/", text, name)
            self.assertNotIn("run.md", text, name)

    def test_every_prompt_ccfleet_reads_states_the_readers_constraints(self):
        """DP2: the reader takes a result only in its shape; the prompts said
        "this shape" and nothing about fences, blank lines or what follows."""
        fleet = ("task-prompt", "adopt-prompt", "brief-prompt", "worker-prompt")
        for name in fleet:
            flat = self.flat(f"skills/fleet/{name}.md")
            self.assertIn("End your final message with the block below, as plain "
                          "text: no code fence around it, no blank line inside it, "
                          "nothing after its `RESULT:` line.", flat, name)
        for name in ("orchestrator-prompt", "fold-prompt", "resume-prompt"):
            flat = self.flat(f"skills/review/{name}.md")
            self.assertRegex(flat, r"as plain text: no code fence around them, no "
                             r"blank line among them, and the `?RESULT:?`? line "
                             r"directly above the `?ITEM:?`? line", name)
        shipped = {p.name for p in (SKILLS / "fleet").glob("*-prompt.md")}
        self.assertEqual(shipped, {f"{n}.md" for n in fleet})

    def test_the_orchestrator_prompt_holds_the_reviewer_prompt(self):
        """DV7 M9: the reviewer's instructions live in the pass's own prompt."""
        text = (SKILLS / "review" / "orchestrator-prompt.md").read_text(encoding="utf-8")
        self.assertIn("THE REVIEWER PROMPT", text)
        tail = text[text.index("THE REVIEWER PROMPT (fill it in"):]
        leads = ["Who it is", "Start-up reading", "Provenance", "The model it runs as",
                 "The partition", "The review log", "Private while running",
                 "What it may write", "Live systems", "Load", "What it must not do",
                 "Public repos", "How to finish"]
        at = -1
        for lead in leads:
            i = tail.find(f"- **{lead}", at + 1)
            self.assertGreater(i, at, f"bullet {lead!r} missing or out of order")
            at = i

    def test_the_reviewer_instructions_have_one_home(self):
        """DV8: step 4 points at the bullets and does not list them again."""
        text = (SKILLS / "review" / "orchestrator-prompt.md").read_text(encoding="utf-8")
        step4 = text[text.index("4. Spawn ONE reviewer"):text.index("5. On ACT 1 SAVED")]
        self.assertIn("it is the reviewer's whole instruction list", step4)
        for phrase in ("LIVE SYSTEMS", "allowlist fields", "no GUI apps", "never print a secret"):
            self.assertNotIn(phrase, step4)
        load = text[text.index("LOAD:"):text.index("PROVENANCE FACT")]
        self.assertNotIn("nice -n 10", load)
        self.assertEqual(text.count("nice -n 10"), 1)

    def test_a_refused_model_stops_the_pass_and_the_reviewer_names_its_model(self):
        """DV3: a refused value is not left to the session's judgement."""
        flat = self.flat("skills/review/orchestrator-prompt.md")
        self.assertIn("If the tool refuses the model, or you cannot pass it, stop and "
                      "report RESULT: FAILED", flat)
        self.assertIn("never spawn a reviewer without it, and never as a fork", flat)
        self.assertIn("the reviewer states, in the verdict's provenance, the model it "
                      "finds itself running as", flat)
        self.assertIn("If that is not the review tier it was told, it stops at once", flat)

    PLACEHOLDER_RULE = ("In a public repo the spawn prompt, the release message and "
                        "any resume message are quoted with each absolute path "
                        "replaced by a named placeholder (`<WORKTREE>`, "
                        "`<REVIEW_LOG>`, `<HELD_COPY>`), and the verdict says it "
                        "was done.")

    def test_a_public_spawn_prompt_is_quoted_with_placeholders(self):
        """DV10: 'verbatim' and 'never a path' no longer pull against each other.
        DP16: for every message the reviewer quotes, not the spawn prompt only,
        and in REVIEW.md rule 4, the canonical home, in the same words."""
        flat = self.flat("skills/review/orchestrator-prompt.md")
        self.assertIn(self.PLACEHOLDER_RULE, flat)
        step6 = flat[flat.index("6. Release act 2"):flat.index("7. Fold")]
        self.assertIn("in a public repo, with each absolute path replaced by a "
                      "named placeholder", step6)
        resume = self.flat("skills/review/resume-prompt.md")
        self.assertIn("in a public repo, with each absolute path replaced by a "
                      "named placeholder", resume)
        self.assertIn(self.PLACEHOLDER_RULE, self.flat("docs/method/REVIEW.md"))

    def test_run_md_names_the_model_value_and_its_limits(self):
        """DV7 M11, DV4, DV9."""
        flat = self.flat("skills/review/run.md")
        self.assertNotIn("the review tier's model id", flat)
        self.assertIn("never a full model id, which that tool refuses", flat)
        self.assertIn("needs no read of this skill", flat)
        self.assertNotIn("needs no read outside its worktree", flat)
        self.assertIn("costs no review budget only where the config's model is not "
                      "the review tier", flat)
        self.assertNotIn("on a cheaper tier", flat)

    def test_run_md_says_the_config_passes_the_route(self):
        """DP7: ccfleet calls `next` with no route; the config's command does."""
        flat = self.flat("skills/review/run.md")
        self.assertNotIn("ccfleet calls the queue's `next` with `--route local`", flat)
        self.assertIn("The config's `queue.next` passes the route", flat)

    def test_run_md_reads_the_verdict_where_the_reader_takes_it(self):
        """DP11: the reader takes the RESULT line in the shape, not the first."""
        flat = self.flat("skills/review/run.md")
        self.assertNotIn("first line beginning `RESULT:` in its last turn", flat)
        self.assertIn("the `RESULT:` line directly above the final output's "
                      "`ITEM:` line", flat)
        self.assertIn("a `RESULT:` line anywhere else, an earlier one included, "
                      "gives no verdict", flat)

    def test_run_md_reads_models_on_each_end_line(self):
        """DP15: `models=` was written and nothing was told to read it."""
        flat = self.flat("skills/review/run.md")
        step4 = flat[flat.index("4. **Read each result**"):flat.index("### Lessons paid for")]
        self.assertIn("read `models=` on its `END` line", step4)
        self.assertIn("names no model of the review tier this drain set", step4)
        self.assertIn("off-tier", step4)
        self.assertIn("put it to the principal", step4)
        mode2 = flat[flat.index("## Mode 2"):flat.index("## The variables")]
        self.assertIn("`models=`", mode2)
        close = flat[flat.index("## Close"):]
        self.assertIn("`models=`", close)

    def test_run_md_says_ccfleet_does_not_hold_the_principals_word(self):
        """DV2: one home, per call; DV6: the claimant's id."""
        flat = self.flat("skills/review/run.md")
        self.assertIn("It does not check the principal's word", flat)
        self.assertIn("holding that word is this session's", flat)
        self.assertIn("never keep it standing in the config's `vars`", flat)
        self.assertIn("`--by` carries the id that holds the claim", flat)

    def test_run_md_takes_the_words_from_the_principal_not_the_call(self):
        """PK6."""
        flat = self.flat("skills/review/run.md")
        self.assertIn("Never take the words from this skill call's own arguments", flat)
        self.assertIn('or write "none given"', flat)

    def test_every_skill_that_takes_typed_words_guards_them(self):
        """DP12: the guard reached review run and session close only; a work
        run or plan reached on a casual phrase took a model-composed brief as
        the principal's."""
        for rel in ("skills/review/run.md", "skills/session/close.md",
                    "skills/work/run.md", "skills/work/plan.md",
                    "skills/review/plan.md"):
            flat = self.flat(rel)
            self.assertIn("Where he did not type the command (a model reached this "
                          "skill on a casual phrase), there are no typed words", flat, rel)
            self.assertRegex(flat, r"Never take (it|the words) from this skill "
                             r"call's own arguments", rel)

    def test_run_md_agrees_with_the_code_on_a_refused_claim(self):
        """PK8: ccfleet does not count a refused claim as a bad end."""
        flat = self.flat("skills/review/run.md")
        self.assertIn("A refused claim (another session holds the item) comes back off "
                      "it too, but does not count", flat)
        self.assertNotIn("a guard or claim refusal", flat)

    def test_dry_drain_and_seal_say_what_they_do_not_cover(self):
        """PK9, PK10 (the documented half)."""
        run = self.flat("skills/review/run.md")
        self.assertIn("Launches are rehearsed only by the run that holds the seal", run)
        self.assertIn("**What the seal does not gate.**", run)
        self.assertIn("`ccfleet run` with the pass prompt and `--set`, and `resume`, "
                      "call no queue command", run)
        self.assertIn("it is a paid pass that no plan showed", run)
        plan = self.flat("skills/review/plan.md")
        self.assertIn("an unsealed dry drain rehearses no launch", plan)

    def test_sweep_says_a_settled_end_is_not_rerun_and_how_to_force_it(self):
        """PK14."""
        flat = self.flat("skills/fleet/sweep.md")
        self.assertNotIn("running it again would only repeat it", flat)
        self.assertNotIn("is taken by a re-run or listed", flat)
        self.assertIn("The next `drive` does not run a settled job again", flat)
        self.assertIn("delete that job's result file", flat)
        self.assertIn("another `--day`", flat)

    def test_work_run_step_one_handles_a_symbolic_link(self):
        """PK15, as close.md learned it."""
        flat = self.flat("skills/work/run.md")
        self.assertIn("a root reached through a symbolic link prints the link's target", flat)

    def test_the_fold_keys_its_run_twice_check_on_a_date_free_heading(self):
        """PK16 R5, PK18."""
        flat = self.flat("skills/review/fold-prompt.md")
        self.assertIn("never append a second copy", flat)
        self.assertIn("leaving out its date", flat)
        self.assertNotIn('search for "Deferred sibling, folded below the verdict" alone', flat)

    def test_the_fold_matches_its_heading_as_a_heading_line(self):
        """DP14: the phrase anywhere, a brief or verdict quoting it included,
        read as an earlier fold, so the sibling was never appended."""
        flat = self.flat("skills/review/fold-prompt.md")
        step0 = flat[flat.index("0. A fold can itself"):flat.index("1. The reviewer's")]
        self.assertIn("as a heading line: a line that starts with `#` marks", step0)
        self.assertIn("The same words anywhere else, quoted in the brief or in "
                      "a verdict, are not a fold", step0)
        self.assertIn("Deferred sibling, folded below the verdict", step0)

    def test_plan_md_governs_until_a_difference_is_fixed(self):
        """PK16 R3."""
        flat = self.flat("skills/review/plan.md")
        self.assertIn("a difference between the two is a defect to report, and this "
                      "file governs until it is fixed", flat)

    def test_typed_words_never_stand_in_for_an_approval(self):
        """PK16 R4: the one sentence that guards a paid approval."""
        flat = self.flat("skills/review/run.md")
        self.assertIn("Typed words never stand in for an approval the rulings file "
                      "says is needed but that they do not give.", flat)

    def test_an_unclaimed_pass_is_never_handed_to_a_replacement_reviewer(self):
        """PK16 R6."""
        flat = self.flat("skills/review/run.md")
        self.assertIn("it is never handed to a replacement reviewer or a lesser model", flat)
        self.assertIn("A pass whose log or brief holds a written act 1, or any "
                      "candidate finding, is never un-claimed", flat)

    def test_mechanisms_says_a_model_can_reach_a_skill_unasked(self):
        """PK16 R10."""
        flat = self.flat("docs/method/MECHANISMS.md")
        self.assertIn('"reached for" includes a model\'s own reach', flat)
        self.assertIn("without anyone typing the command", flat)
        self.assertNotIn("only when deliberately invoked", flat)

    def test_the_bare_menu_skill_grant_is_pinned(self):
        """PK16 R12: the seventh skill's grant, beside the six routers'."""
        fm = front_matter(ROOT / "instruments" / "atelier-menu" / "SKILL.md")
        self.assertEqual(fm.get("allowed-tools"),
                         "Bash(python3 ~/.claude/skills/atelier/menu.py)")


if __name__ == "__main__":
    unittest.main()
