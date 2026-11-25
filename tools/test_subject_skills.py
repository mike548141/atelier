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


if __name__ == "__main__":
    unittest.main()
