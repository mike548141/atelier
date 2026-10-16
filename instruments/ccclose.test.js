// Stdlib-only tests for ccclose — node:test + node:assert, zero third-party dep.
// Run:  node --test instruments/*.test.js
//
// Every test builds its own world in a temporary directory: throwaway git repos,
// a fake HOME (so ~/.claude/projects is a fixture, never the real store), an
// isolated git config, synthetic transcripts, and a stub standing in for `gh`
// through $CCCLOSE_GH. No test reads the real ~/.claude, a real repo or the
// network.

const test = require('node:test');
const assert = require('node:assert');
const fs = require('node:fs');
const os = require('node:os');
const path = require('node:path');
const { execFileSync, spawnSync } = require('node:child_process');

const cc = require('./ccclose');

const SCRIPT = path.join(__dirname, 'ccclose');
const CCTRANSCRIPT = path.join(__dirname, 'cctranscript');
const NOW = Date.now();
const MIN = 60000;
// A synthetic identity, spelled so no scanner reads it as a real address.
const EMAIL = 't' + String.fromCharCode(64) + 'x.invalid';

// --- the fixture world ---------------------------------------------------

function world() {
  const base = fs.mkdtempSync(path.join(os.tmpdir(), 'ccclose-test-'));
  const home = path.join(base, 'home');
  fs.mkdirSync(path.join(home, '.claude', 'projects', 'proj'), { recursive: true });
  const gitconfig = path.join(base, 'gitconfig');
  fs.writeFileSync(gitconfig, '');
  const env = {
    PATH: process.env.PATH, HOME: home, TMPDIR: os.tmpdir(),
    GIT_CONFIG_GLOBAL: gitconfig, GIT_CONFIG_NOSYSTEM: '1',
    GIT_AUTHOR_NAME: 'T', GIT_AUTHOR_EMAIL: EMAIL, GIT_COMMITTER_NAME: 'T', GIT_COMMITTER_EMAIL: EMAIL,
    CCCLOSE_GH: path.join(base, 'no-gh-here'),
  };
  return { base, home, env };
}

function sh(w, cwd, args, when) {
  const env = { ...w.env };
  if (when !== undefined) {
    const d = new Date(when).toISOString();
    env.GIT_AUTHOR_DATE = d; env.GIT_COMMITTER_DATE = d;
  }
  return execFileSync('git', args, { cwd, env, encoding: 'utf8', stdio: ['ignore', 'pipe', 'pipe'] }).trim();
}

// A repo on main with one old commit, pushed to a local bare origin.
function repo(w, name = 'repo') {
  const root = path.join(w.base, name);
  const bare = path.join(w.base, `${name}.git`);
  fs.mkdirSync(root);
  sh(w, w.base, ['init', '-q', '--bare', '-b', 'main', bare]);
  sh(w, root, ['init', '-q', '-b', 'main']);
  sh(w, root, ['remote', 'add', 'origin', bare]);
  write(root, 'README.md', 'demo\n');
  commit(w, root, 'init', NOW - 3 * 24 * 60 * MIN);
  sh(w, root, ['push', '-q', '-u', 'origin', 'main']);
  sh(w, root, ['remote', 'set-head', 'origin', 'main']);
  return root;
}

function write(root, rel, text) {
  const p = path.join(root, rel);
  fs.mkdirSync(path.dirname(p), { recursive: true });
  fs.writeFileSync(p, text);
}
function commit(w, root, msg, when) {
  sh(w, root, ['add', '--', '.']);
  sh(w, root, ['commit', '-q', '-m', msg], when);
  return sh(w, root, ['rev-parse', 'HEAD']);
}

// A synthetic transcript spanning [NOW - 60 min, NOW + 10 min]: the window
// covers the "in-window" commits (NOW - 30 min) and any worktree the test adds
// while it runs, and excludes the old commit (three days back).
function transcript(w, id, extra = [], endMin = 10) {
  const at = (m) => new Date(NOW + m * MIN).toISOString();
  const recs = [
    { type: 'user', timestamp: at(-60), message: { role: 'user', content: 'Add a null check to the parser' } },
    { type: 'assistant', timestamp: at(-59), message: { model: 'claude-opus-5-5', content: [{ type: 'text', text: 'On it.' }] } },
    ...extra.map((r) => ({ timestamp: at(-20), ...r })),
    { type: 'assistant', timestamp: at(endMin), message: { model: 'claude-opus-5-5', content: [{ type: 'text', text: 'Done.' }] } },
  ];
  const p = path.join(w.home, '.claude', 'projects', 'proj', `${id}.jsonl`);
  fs.writeFileSync(p, recs.map((r) => JSON.stringify(r)).join('\n') + '\n');
  return p;
}

function ccclose(w, cwd, args = [], envExtra = {}) {
  const r = spawnSync('node', [SCRIPT, ...args], { cwd, env: { ...w.env, ...envExtra }, encoding: 'utf8' });
  return { code: r.status, out: r.stdout, err: r.stderr };
}
function json(w, cwd, args = [], envExtra = {}) {
  const r = ccclose(w, cwd, [...args, '--json'], envExtra);
  const j = JSON.parse(r.out);
  j.code = r.code;
  j.by = Object.fromEntries(j.checks.map((c) => [c.id, c]));
  return j;
}

// A gh stub: answers auth status, and `pr list` / `run list` from JSON files.
// It answers `run list --commit <sha>` only for a FULL 40-hex sha, as the real
// gh effectively does (a short sha silently returns []).
function ghStub(w, { prs = [], runs = [], authOk = true } = {}) {
  const dir = path.join(w.base, 'gh');
  fs.mkdirSync(dir, { recursive: true });
  fs.writeFileSync(path.join(dir, 'prs.json'), JSON.stringify(prs));
  fs.writeFileSync(path.join(dir, 'runs.json'), JSON.stringify(runs));
  const stub = path.join(dir, 'gh');
  fs.writeFileSync(stub, `#!/bin/sh
case "$1 $2" in
  "auth status") ${authOk ? 'exit 0' : 'exit 1'} ;;
  "pr list") cat "${dir}/prs.json" ;;
  "run list")
    sha=""; while [ $# -gt 0 ]; do [ "$1" = "--commit" ] && sha="$2"; shift; done
    if [ \${#sha} -eq 40 ]; then cat "${dir}/runs.json"; else echo "[]"; fi ;;
  *) exit 2 ;;
esac
`);
  fs.chmodSync(stub, 0o755);
  return stub;
}

const ID_ORDER = ['worktrees', 'branches', 'pushed', 'prs', 'session-record', 'board', 'claims',
  'floor', 'reviews', 'bypasses', 'tree'];

// --- pure functions ------------------------------------------------------

test('parseArgs takes the three selectors and refuses anything else', () => {
  assert.deepEqual(cc.parseArgs(['--session', 'abc', '--root', '/x', '--json']),
    { session: 'abc', root: '/x', json: true, help: false });
  assert.match(cc.parseArgs(['--session']).error, /needs a value/);
  assert.match(cc.parseArgs(['--root', '--json']).error, /needs a value/);
  assert.match(cc.parseArgs(['--fix']).error, /unknown argument/);
});

test('askSentences lists close-out-shaped sentences and passes over ordinary ones', () => {
  assert.deepEqual(cc.askSentences('Add a null check to the parser'), []);
  assert.deepEqual(cc.askSentences('Please close out the session.'), ['Please close out the session.']);
  assert.deepEqual(cc.askSentences('Fix the bug. Make sure the roadmap is updated.'), ['Make sure the roadmap is updated.']);
  assert.deepEqual(cc.askSentences('are questions and decisions recorded'), ['are questions and decisions recorded']);
  assert.deepEqual(cc.askSentences('Leave things clean'), ['Leave things clean']);
  // A cue with no object, or an object with no cue, is not an ask.
  assert.deepEqual(cc.askSentences('make sure it compiles'), []);
  assert.deepEqual(cc.askSentences('what is on the roadmap'), []);
});

test('stripWrappers removes harness wrappers so wrapper-only text is empty', () => {
  assert.equal(cc.stripWrappers('<task-notification>agent done, close out</task-notification>'), '');
  assert.equal(cc.stripWrappers('<command-name>/clear</command-name>\n<command-args></command-args>'), '');
  assert.equal(cc.stripWrappers('hi <system-reminder>x</system-reminder> there'), 'hi   there');
  // A browser extension's instructions ride in the prompt's own record; only the typed text is the principal's.
  assert.equal(cc.stripWrappers('<browser_instruction>record them for review</browser_instruction>\nShip it'), 'Ship it');
});

test('bypassesIn names workaround-shaped commands and leaves ordinary ones alone', () => {
  assert.deepEqual(cc.bypassesIn('git commit --no-verify -m x'), ['hooks skipped']);
  assert.deepEqual(cc.bypassesIn('git -c commit.gpgsign=false commit -m x'), ['signing switched off']);
  assert.deepEqual(cc.bypassesIn('git push --force origin main'), ['force push']);
  assert.deepEqual(cc.bypassesIn('git reset --hard origin/main'), ['hard reset']);
  assert.deepEqual(cc.bypassesIn('git stash'), ['bare stash']);
  assert.deepEqual(cc.bypassesIn('git stash pop'), ['bare stash']);
  assert.deepEqual(cc.bypassesIn('git add -A'), ['stage everything']);
  assert.deepEqual(cc.bypassesIn('rm -f .git/index.lock'), ['lock file removed']);
  assert.deepEqual(cc.bypassesIn('gh pr merge 12 --admin'), ['protection bypassed']);
  for (const ok of ['git push origin main', 'git stash push -u -m tag-1', 'git stash apply abc123',
    'git add instruments/ccclose', 'git commit -m "fix"', 'git reset --soft HEAD~1']) {
    assert.deepEqual(cc.bypassesIn(ok), [], ok);
  }
});

// --- the transcript ------------------------------------------------------

test('readTranscript streams the window, the principal\'s prompts, asks and bypasses', async () => {
  const w = world();
  const p = transcript(w, 'sess-a', [
    { type: 'user', message: { role: 'user', content: 'Before you finish, update the session log.' } },
    { type: 'attachment', attachment: { type: 'queued_command', commandMode: 'prompt', origin: { kind: 'human' }, prompt: 'Are the decisions recorded?' } },
    // Not the principal: a peer's message, a harness notice, a meta record, a wrapper-only prompt.
    { type: 'attachment', attachment: { type: 'queued_command', commandMode: 'prompt', origin: { kind: 'peer' }, prompt: 'close out now' } },
    { type: 'attachment', attachment: { type: 'queued_command', commandMode: 'task-notification', prompt: 'close out now' } },
    { type: 'user', isMeta: true, message: { role: 'user', content: 'Make sure the roadmap is updated.' } },
    { type: 'user', message: { role: 'user', content: '<task-notification>worker done; close out</task-notification>' } },
    { type: 'assistant', message: { model: 'claude-sonnet-5-5', content: [{ type: 'tool_use', name: 'Bash', input: { command: 'git commit --no-verify -m wip' } }] } },
  ]);
  const t = await cc.readTranscript(p);
  assert.equal(t.first, NOW - 60 * MIN);
  assert.equal(t.last, NOW + 10 * MIN);
  assert.equal(t.turn, 2);       // the first prompt and the session-log ask; meta and wrapper-only excluded
  assert.equal(t.midTurn, 1);    // the human queued_command only
  assert.equal(t.asksTotal, 2);
  assert.deepEqual(t.asks.map((a) => [a.channel, a.ref]), [['turn', '2'], ['mid-turn', '2+1']]);
  assert.deepEqual(t.models.sort(), ['Opus 5.5', 'Sonnet 5.5']);
  assert.equal(t.bypassesTotal, 1);
  assert.deepEqual(t.bypasses[0].kinds, ['hooks skipped']);
});

test('the refs ccclose prints are the refs cctranscript prints for the same turns', async () => {
  const w = world();
  const p = transcript(w, 'sess-refs', [
    { type: 'user', isMeta: true, message: { role: 'user', content: 'skill text' } },
    { type: 'user', message: { role: 'user', content: 'Then close out cleanly.' } },
    { type: 'attachment', attachment: { type: 'queued_command', commandMode: 'prompt', prompt: 'and update the roadmap' } },
  ]);
  const t = await cc.readTranscript(p);
  const ct = JSON.parse(execFileSync('node', [CCTRANSCRIPT, '--json', p], { encoding: 'utf8', env: w.env }));
  const byText = new Map(ct.turns.filter((x) => x.role === 'you' || x.role === 'you-mid').map((x) => [x.text, x.ref]));
  for (const a of t.asks) {
    const src = a.quote.startsWith('Then') ? 'Then close out cleanly.' : 'and update the roadmap';
    assert.equal(a.ref, byText.get(src), `ref for "${src}"`);
  }
  assert.equal(t.asks.length, 2);
});

// --- whole runs over throwaway repos -------------------------------------

test('a tidy close passes every check that applies and exits 0', () => {
  const w = world();
  const root = repo(w);
  write(root, 'docs/SESSIONS.md', '# Sessions\n- [today](sessions/today.md)\n');
  write(root, 'docs/sessions/today.md', '# today\n');
  commit(w, root, 'records: session close', NOW - 30 * MIN);
  sh(w, root, ['push', '-q', 'origin', 'main']);
  transcript(w, 'sess-tidy');
  const j = json(w, root, ['--session', 'sess-tidy']);
  assert.deepEqual(j.checks.map((c) => c.id), ID_ORDER);
  const want = { worktrees: 'pass', branches: 'pass', pushed: 'pass', prs: 'na', 'session-record': 'pass',
    board: 'na', claims: 'na', floor: 'na', reviews: 'na', bypasses: 'pass', tree: 'pass' };
  for (const [id, st] of Object.entries(want)) assert.equal(j.by[id].status, st, `${id}: ${j.by[id].summary}`);
  assert.equal(j.code, 0);
  assert.equal(j.verdict.status, 'pass');
  assert.equal(j.commits.inWindow, 1);
  assert.equal(j.commits.notOnRemote, 0);
  assert.equal(j.session.found, true);
  assert.equal(j.window.known, true);
  assert.match(j.window.heuristic, /overlapped/);
});

test('an untidy close fails on worktrees, branches, pushes, record and claims, and exits 1', () => {
  const w = world();
  const root = repo(w);
  write(root, 'docs/SESSIONS.md', '# Sessions\n');
  write(root, 'docs/ROADMAP.md', '# Roadmap\n- [~] build the widget (claimed by queue run sess-unt)\n- [~] older (claimed 2020-01-01-0000 UTC)\n');
  commit(w, root, 'records: old', NOW - 3 * 24 * 60 * MIN);
  sh(w, root, ['push', '-q', 'origin', 'main']);
  // A branch with an in-window tip, and a linked worktree, both left behind.
  sh(w, root, ['checkout', '-q', '-b', 'feature']);
  write(root, 'src/a.txt', 'a\n');
  commit(w, root, 'feature work', NOW - 30 * MIN);
  sh(w, root, ['checkout', '-q', 'main']);
  sh(w, root, ['worktree', 'add', '-q', path.join(w.base, 'wt'), '-b', 'wt-branch']);
  transcript(w, 'sess-untidy-1');
  const j = json(w, root, ['--session', 'sess-untidy-1']);
  // A filesystem that records no birth time leaves the worktree's age unknown:
  // then the honest answer is a warning, never a pass.
  const born = fs.statSync(path.join(root, '.git', 'worktrees')).birthtimeMs > 0;
  assert.equal(j.by.worktrees.status, born ? 'fail' : 'warn', j.by.worktrees.summary);
  assert.equal(j.by.branches.status, 'fail');
  assert.ok(j.by.branches.items.some((s) => s.startsWith('feature (not merged)')), j.by.branches.items.join('|'));
  assert.equal(j.by.pushed.status, 'fail');
  assert.equal(j.by.pushed.itemsTotal, 1);
  assert.equal(j.by['session-record'].status, 'fail');
  // The claim naming the session's 8-char id prefix is this session's, whatever its date.
  assert.equal(j.by.claims.status, 'fail');
  assert.equal(j.by.claims.itemsTotal, 1);
  assert.match(j.by.claims.summary, /1 other/);
  assert.equal(j.by.board.status, 'na');        // hand-kept board: nothing to rebuild
  assert.equal(j.code, 1);
  assert.equal(j.verdict.status, 'fail');
  const text = ccclose(w, root, ['--session', 'sess-untidy-1']);
  assert.equal(text.code, 1);
  assert.match(text.out, /❌ Branches put away/);
  assert.match(text.out, /❌ not ready to close/);
});

test('a merged branch that was not deleted is still not put away', () => {
  const w = world();
  const root = repo(w);
  sh(w, root, ['checkout', '-q', '-b', 'done-work']);
  write(root, 'x.txt', 'x\n');
  commit(w, root, 'work', NOW - 30 * MIN);
  sh(w, root, ['checkout', '-q', 'main']);
  sh(w, root, ['merge', '-q', '--ff-only', 'done-work']);
  sh(w, root, ['push', '-q', 'origin', 'main']);
  transcript(w, 'sess-merged');
  const j = json(w, root, ['--session', 'sess-merged']);
  assert.equal(j.by.branches.status, 'fail');
  assert.deepEqual(j.by.branches.items, ['done-work (merged, not deleted)']);
  assert.equal(j.by.pushed.status, 'pass');
});

test('the session record is "written but not committed" when the log is only dirty', () => {
  const w = world();
  const root = repo(w);
  write(root, 'SESSIONS.md', '# Sessions\n');
  commit(w, root, 'old log', NOW - 3 * 24 * 60 * MIN);
  sh(w, root, ['push', '-q', 'origin', 'main']);
  fs.appendFileSync(path.join(root, 'SESSIONS.md'), '- today\n');
  transcript(w, 'sess-dirty');
  const j = json(w, root, ['--session', 'sess-dirty']);
  assert.equal(j.by['session-record'].status, 'fail');
  assert.match(j.by['session-record'].summary, /written but not committed/);
  assert.equal(j.by.tree.status, 'warn');      // dirty, but not attributable: warn, never fail
});

test('a generated board runs the repo\'s board.py --check; claims and review pointers are read from its items', () => {
  const w = world();
  const root = repo(w);
  write(root, 'docs/ROADMAP.md', '<!-- GENERATED by board.py — do not hand-edit; edit docs/roadmap/ -->\n# Board\n');
  write(root, 'docs/roadmap/010-a/010-item.md', '- [ ] an item\n');
  write(root, 'tools/board.py', 'import sys\nprint("stale: docs/ROADMAP.md")\nsys.exit(1)\n');
  commit(w, root, 'board', NOW - 3 * 24 * 60 * MIN);
  sh(w, root, ['push', '-q', 'origin', 'main']);
  // In the window: a tool path changes and a claim is dated inside the window.
  const iso = new Date(NOW - 40 * MIN).toISOString();
  const stamp = `${iso.slice(0, 10)}-${iso.slice(11, 13)}${iso.slice(14, 16)}`;   // the claim form: 2026-10-16-1554
  write(root, 'docs/roadmap/010-a/010-item.md', `- [~] an item (claimed ${stamp} UTC)\n`);
  write(root, 'tools/x.py', 'print(1)\n');
  commit(w, root, 'tool change + claim', NOW - 30 * MIN);
  sh(w, root, ['push', '-q', 'origin', 'main']);
  transcript(w, 'sess-board');
  let j = json(w, root, ['--session', 'sess-board']);
  assert.equal(j.by.board.status, 'fail');
  assert.deepEqual(j.by.board.items, ['stale: docs/ROADMAP.md']);
  assert.equal(j.by.claims.status, 'fail', j.by.claims.summary);
  assert.equal(j.by.reviews.status, 'warn');
  assert.ok(j.by.reviews.items.includes('tools/x.py'));
  // The board passes, the claim is released and a ⏳ pointer lands: all three clear.
  write(root, 'tools/board.py', 'import sys\nsys.exit(0)\n');
  write(root, 'docs/roadmap/010-a/010-item.md', '- [ ] an item\n  - ⏳ review queued\n');
  commit(w, root, 'close records', NOW - 20 * MIN);
  sh(w, root, ['push', '-q', 'origin', 'main']);
  j = json(w, root, ['--session', 'sess-board']);
  assert.equal(j.by.board.status, 'pass', j.by.board.summary);
  assert.equal(j.by.claims.status, 'pass');
  assert.equal(j.by.reviews.status, 'pass', j.by.reviews.summary);
});

test('GitHub checks read gh: a green floor passes, cancelled fails, pending warns, an open PR fails', () => {
  const w = world();
  const root = repo(w);
  write(root, '.github/workflows/floor.yml', 'on: push\n');
  const sha = commit(w, root, 'work', NOW - 30 * MIN);
  sh(w, root, ['push', '-q', 'origin', 'main']);
  sh(w, root, ['remote', 'set-url', 'origin', 'https://github.com/example/demo.git']);
  transcript(w, 'sess-gh');
  const runs = (conclusion, status = 'completed') => [
    { databaseId: 1, workflowName: 'floor', status: 'completed', conclusion: 'failure' },  // superseded
    { databaseId: 2, workflowName: 'floor', status, conclusion },
  ];
  let j = json(w, root, ['--session', 'sess-gh'], { CCCLOSE_GH: ghStub(w, { runs: runs('success') }) });
  assert.equal(j.by.floor.status, 'pass', j.by.floor.summary);
  assert.ok(j.by.floor.summary.startsWith(sha.slice(0, 12)));
  assert.equal(j.by.prs.status, 'pass');
  j = json(w, root, ['--session', 'sess-gh'], { CCCLOSE_GH: ghStub(w, { runs: runs('cancelled') }) });
  assert.equal(j.by.floor.status, 'fail');
  assert.match(j.by.floor.summary, /cancelled is not a pass/);
  j = json(w, root, ['--session', 'sess-gh'], { CCCLOSE_GH: ghStub(w, { runs: runs(null, 'in_progress') }) });
  assert.equal(j.by.floor.status, 'warn');
  j = json(w, root, ['--session', 'sess-gh'], { CCCLOSE_GH: ghStub(w, { runs: [] }) });
  assert.equal(j.by.floor.status, 'warn');
  assert.match(j.by.floor.summary, /no run reported/);
  const prs = [
    { number: 7, title: 'mine', headRefName: 'x', createdAt: new Date(NOW - 10 * MIN).toISOString() },
    { number: 3, title: 'old', headRefName: 'y', createdAt: new Date(NOW - 9 * 24 * 60 * MIN).toISOString() },
  ];
  j = json(w, root, ['--session', 'sess-gh'], { CCCLOSE_GH: ghStub(w, { prs, runs: runs('success') }) });
  assert.equal(j.by.prs.status, 'fail');
  assert.deepEqual(j.by.prs.items, ['#7 mine (x)']);
  // gh absent or not signed in: unknown, never a pass.
  j = json(w, root, ['--session', 'sess-gh']);
  assert.equal(j.by.prs.status, 'warn');
  assert.equal(j.by.floor.status, 'warn');
  assert.match(j.by.prs.summary, /not installed/);
  j = json(w, root, ['--session', 'sess-gh'], { CCCLOSE_GH: ghStub(w, { authOk: false }) });
  assert.match(j.by.floor.summary, /not authenticated/);
});

test('with no transcript the window is unknown, and attribution checks say so rather than pass', () => {
  const w = world();
  const root = repo(w);
  sh(w, root, ['checkout', '-q', '-b', 'stray']);
  sh(w, root, ['checkout', '-q', 'main']);
  const j = json(w, root, ['--session', 'no-such-session']);
  assert.equal(j.session.found, false);
  assert.match(j.session.why, /no transcript found/);
  assert.equal(j.window.known, false);
  assert.equal(j.by.branches.status, 'warn');
  assert.equal(j.by.pushed.status, 'warn');
  assert.equal(j.by.bypasses.status, 'na');
  assert.equal(j.asked.total, null);
  assert.equal(j.commits.inWindow, null);       // unknown is not zero
  assert.equal(j.prompts.turn, null);
  const text = ccclose(w, root, ['--session', 'no-such-session']);
  assert.match(text.out, /Commits {5}unknown in the window/);
  assert.match(text.out, /asks unknown/);
});

test('the session defaults to $CLAUDE_CODE_SESSION_ID and resolves in any project folder', () => {
  const w = world();
  const root = repo(w);
  fs.mkdirSync(path.join(w.home, '.claude', 'projects', 'other'), { recursive: true });
  transcript(w, 'sess-env');
  fs.renameSync(path.join(w.home, '.claude', 'projects', 'proj', 'sess-env.jsonl'),
    path.join(w.home, '.claude', 'projects', 'other', 'sess-env.jsonl'));
  const j = json(w, root, [], { CLAUDE_CODE_SESSION_ID: 'sess-env' });
  assert.equal(j.session.id, 'sess-env');
  assert.equal(j.session.source, '$CLAUDE_CODE_SESSION_ID');
  assert.equal(j.session.found, true);
  const none = json(w, root, []);
  assert.equal(none.session.id, null);
  assert.match(none.session.why, /no session id/);
});

test('a live session\'s window runs to now; a past session keeps its transcript\'s end', () => {
  const w = world();
  const root = repo(w);
  // The log's last line is 40 minutes old; a branch was committed 5 minutes ago.
  transcript(w, 'sess-live', [], -40);
  sh(w, root, ['checkout', '-q', '-b', 'late']);
  write(root, 'late.txt', 'l\n');
  commit(w, root, 'late work', NOW - 5 * MIN);
  sh(w, root, ['checkout', '-q', 'main']);
  const past = json(w, root, ['--session', 'sess-live']);
  assert.equal(past.window.toNow, false);
  assert.equal(past.by.branches.status, 'pass');
  const live = json(w, root, [], { CLAUDE_CODE_SESSION_ID: 'sess-live' });
  assert.equal(live.window.toNow, true);
  assert.equal(live.by.branches.status, 'fail');
  assert.match(ccclose(w, root, [], { CLAUDE_CODE_SESSION_ID: 'sess-live' }).out, /live session: runs to now/);
});

test('outside a git repo every repo check is not applicable and nothing crashes', () => {
  const w = world();
  const plain = path.join(w.base, 'plain');
  fs.mkdirSync(plain);
  transcript(w, 'sess-plain');
  const j = json(w, plain, ['--session', 'sess-plain']);
  for (const id of ID_ORDER.filter((x) => x !== 'bypasses')) assert.equal(j.by[id].status, 'na', id);
  assert.equal(j.code, 0);
  assert.equal(j.repo.isGit, false);
});

test('--root selects the repo; a bad --root or flag is a usage error (exit 2)', () => {
  const w = world();
  const root = repo(w);
  transcript(w, 'sess-root');
  const j = json(w, w.base, ['--session', 'sess-root', '--root', root]);
  assert.equal(j.repo.root, fs.realpathSync(root));
  assert.equal(ccclose(w, w.base, ['--root', path.join(w.base, 'nope')]).code, 2);
  assert.equal(ccclose(w, w.base, ['--fix']).code, 2);
});

test('listed items are capped and the cut is counted, never silent', () => {
  const w = world();
  const root = repo(w);
  const many = Array.from({ length: cc.CAP + 7 }, (_, i) => `- [~] item ${i} (claimed by sess-cap)`).join('\n');
  write(root, 'ROADMAP.md', `# Roadmap\n${many}\n`);
  commit(w, root, 'claims', NOW - 3 * 24 * 60 * MIN);
  sh(w, root, ['push', '-q', 'origin', 'main']);
  transcript(w, 'sess-cap-1');
  const j = json(w, root, ['--session', 'sess-cap-1']);
  assert.equal(j.by.claims.items.length, cc.CAP);
  assert.equal(j.by.claims.itemsTotal, cc.CAP + 7);
  assert.match(ccclose(w, root, ['--session', 'sess-cap-1']).out, /… and 7 more/);
});

test('the field set is stable: every check prints on every run, in one order', () => {
  const w = world();
  const root = repo(w);
  transcript(w, 'sess-stable');
  const a = json(w, root, ['--session', 'sess-stable']);
  const b = json(w, path.join(w.base), ['--session', 'nothing']);
  assert.deepEqual(a.checks.map((c) => c.id), ID_ORDER);
  assert.deepEqual(b.checks.map((c) => c.id), ID_ORDER);
  for (const k of ['tool', 'session', 'window', 'repo', 'commits', 'prompts', 'models', 'checks', 'asked', 'verdict']) {
    assert.ok(k in a && k in b, k);
  }
  const text = ccclose(w, root, ['--session', 'sess-stable']).out;
  assert.match(text, /Asked of this close — answer each/);
  assert.match(text, /keyword heuristic/);
  assert.match(text, /Heuristic +"this session's" = dated inside the window/);
});

// --- documentation convention (REPO-STANDARD: concise --help + a man page) --

test('--help is a concise digest that points at the man page', () => {
  const help = execFileSync('node', [SCRIPT, '-h'], { encoding: 'utf8' });
  assert.ok(help.trimEnd().split('\n').length <= 24, '--help should stay a one-screen digest');
  assert.match(help, /man ccclose/);
  for (const opt of ['--session', '--root', '--json']) assert.ok(help.includes(opt));
});

test('a man page ships and is well-formed roff', () => {
  const page = path.join(__dirname, 'man', 'ccclose.1');
  assert.ok(fs.existsSync(page), 'instruments/man/ccclose.1 must exist');
  const roff = fs.readFileSync(page, 'utf8');
  assert.match(roff, /^\.TH CCCLOSE 1 /m);
  for (const sec of ['NAME', 'SYNOPSIS', 'DESCRIPTION', 'OPTIONS', 'EXAMPLES', 'EXIT STATUS', 'SEE ALSO']) {
    assert.match(roff, new RegExp(`^\\.SH ${sec}`, 'm'), `a ${sec} section`);
  }
});

test('drift guard: every flag --help prints appears in the man page (superset relation)', () => {
  const help = execFileSync('node', [SCRIPT, '-h'], { encoding: 'utf8' });
  const page = fs.readFileSync(path.join(__dirname, 'man', 'ccclose.1'), 'utf8').replace(/\\-/g, '-');
  const flags = [...new Set(help.match(/--[\w-]+/g))];
  assert.ok(flags.length >= 4, `expected a real flag list, got ${flags.length}`);
  for (const flag of flags) assert.ok(page.includes(flag), `man page must document ${flag}`);
});
