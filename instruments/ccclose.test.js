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
function ghStub(w, { prs = [], runs = [], authOk = true, views = {} } = {}) {
  const dir = path.join(w.base, 'gh');
  fs.mkdirSync(dir, { recursive: true });
  fs.writeFileSync(path.join(dir, 'prs.json'), JSON.stringify(prs));
  fs.writeFileSync(path.join(dir, 'runs.json'), JSON.stringify(runs));
  for (const [n, state] of Object.entries(views)) fs.writeFileSync(path.join(dir, `view-${n}.json`), JSON.stringify({ state, title: `pr ${n}` }));
  const stub = path.join(dir, 'gh');
  fs.writeFileSync(stub, `#!/bin/sh
case "$1 $2" in
  "auth status") ${authOk ? 'exit 0' : 'exit 1'} ;;
  "pr list") cat "${dir}/prs.json" ;;
  "pr view") if [ -f "${dir}/view-$3.json" ]; then cat "${dir}/view-$3.json"; else exit 1; fi ;;
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
  'floor', 'reviews', 'bypasses', 'tree', 'subagents'];


// --- subagent fixtures ---------------------------------------------------
//
// The agents of a session sit beside its transcript:
//   <project>/<session-id>/subagents/agent-<id>.jsonl + agent-<id>.meta.json
// Ids, descriptions and tool-use ids here are synthetic.

const at = (m) => new Date(NOW + m * MIN).toISOString();
const asst = (m, stop, blocks) => ({ type: 'assistant', timestamp: at(m), message: { stop_reason: stop, content: blocks.map((b) => ({ type: b })) } });
// Finished: streamed partials (stop_reason null) and then the final end_turn.
const finishedTurns = [asst(-50, null, ['thinking']), asst(-49, null, ['tool_use']),
  { type: 'user', timestamp: at(-48), message: { role: 'user', content: [{ type: 'tool_result', tool_use_id: 'x' }] } },
  asst(-47, 'end_turn', ['text'])];
// Cut: the last assistant record is a tool_use with no result after it.
const cutTurns = [asst(-50, null, ['thinking']), asst(-49, null, ['tool_use'])];

function agent(w, sid, id, { turns, description = `job ${id}`, shape = 'background', toolUseId = `toolu_${id}` }) {
  const dir = path.join(w.home, '.claude', 'projects', 'proj', sid, 'subagents');
  fs.mkdirSync(dir, { recursive: true });
  fs.writeFileSync(path.join(dir, `agent-${id}.jsonl`), turns.map((r) => JSON.stringify(r)).join('\n') + '\n');
  fs.writeFileSync(path.join(dir, `agent-${id}.meta.json`), JSON.stringify({ agentType: 'general-purpose', description, toolUseId, requestShape: shape, model: 'sonnet' }));
}

// The three shapes a background agent's end takes in the parent transcript.
const noteText = (id, status) => `<task-notification>\n<task-id>${id}</task-id>\n<tool-use-id>toolu_${id}</tool-use-id>\n<status>${status}</status>\n<summary>Agent done</summary>\n</task-notification>`;
const viaAttachment = (id, status) => ({ type: 'attachment', attachment: { type: 'queued_command', commandMode: 'task-notification', prompt: noteText(id, status) } });
const viaQueue = (id, status) => ({ type: 'queue-operation', operation: 'enqueue', content: noteText(id, status) });
const viaUser = (id, status) => ({ type: 'user', message: { role: 'user', content: noteText(id, status) } });
const toolResult = (toolUseId) => ({ type: 'user', message: { role: 'user', content: [{ type: 'tool_result', tool_use_id: toolUseId, content: 'done' }] } });

const agentLines = (j) => Object.fromEntries(j.by.subagents.agents.map((a) => [a.id, a]));

// --- pure functions ------------------------------------------------------

test('parseArgs takes the three selectors and refuses anything else', () => {
  assert.deepEqual(cc.parseArgs(['--session', 'abc', '--root', '/x', '--json']),
    { session: 'abc', root: '/x', json: true, identifiers: false, help: false });
  assert.equal(cc.parseArgs(['--identifiers']).identifiers, true);
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

test('harness text and ccclose agree turn for turn: cctranscript calls it harness, ccclose numbers it and does not ask from it', async () => {
  const w = world();
  const p = transcript(w, 'sess-harness', [
    { type: 'user', message: { role: 'user', content: '<task-notification><summary>make sure the roadmap is updated</summary></task-notification>' } },
    { type: 'user', isMeta: true, message: { role: 'user', content: [{ type: 'text', text: 'Close out: update the session log.' }] } },
    { type: 'user', message: { role: 'user', content: '<browser_instruction>record the board for review</browser_instruction>\nBefore you finish, update the session log.' } },
  ]);
  const t = await cc.readTranscript(p);
  const ct = JSON.parse(execFileSync('node', [CCTRANSCRIPT, '--json', p], { encoding: 'utf8', env: w.env }));
  // cctranscript: only the fixture's own opening prompt and the last record are the
  // principal's; the two between are harness, numbered 2 and 3.
  assert.deepEqual(ct.turns.filter((x) => x.role !== 'claude').map((x) => [x.role, x.ref]),
    [['you', '1'], ['harness', '2'], ['harness', '3'], ['you', '4']]);
  assert.equal(ct.turns.find((x) => x.ref === '4').text, 'Before you finish, update the session log.');
  // ccclose: the same refs, and the principal's prompt count excludes the harness records.
  assert.equal(t.turn, 2);
  assert.equal(t.asksTotal, 1);
  assert.equal(t.asks[0].ref, '4');
  assert.equal(t.asks[0].quote, 'Before you finish, update the session log.');
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
    board: 'na', claims: 'na', floor: 'na', reviews: 'na', bypasses: 'pass', tree: 'pass', subagents: 'na' };
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

// --- check 12: subagents finished ---------------------------------------

test('taskNotifications reads the id and status of each block, and only a text that opens with the tag', () => {
  assert.deepEqual(cc.taskNotifications(noteText('a1', 'completed')), [{ id: 'a1', status: 'completed' }]);
  assert.deepEqual(cc.taskNotifications(`${noteText('a1', 'killed')}\n${noteText('b2', 'stopped')}`),
    [{ id: 'a1', status: 'killed' }, { id: 'b2', status: 'stopped' }]);
  assert.deepEqual(cc.taskNotifications('I saw ' + noteText('a1', 'completed')), []);   // a mention, not a notification
  assert.deepEqual(cc.taskNotifications('<task-notification>\n<task-id>a1</task-id>\n</task-notification>'), []);  // no status
  assert.deepEqual(cc.taskNotifications(''), []);
});

test('readTranscript records a notification from each of its three carrier shapes, and ignores a mention', async () => {
  const w = world();
  const p = transcript(w, 'sess-carriers', [
    viaAttachment('aaa1', 'completed'), viaQueue('bbb2', 'killed'), viaUser('ccc3', 'stopped'),
    // Not carriers: an assistant quoting the tag, and a tool_result (a record with toolUseResult) carrying it.
    { type: 'assistant', message: { content: [{ type: 'text', text: noteText('ddd4', 'completed') }] } },
    { type: 'user', toolUseResult: {}, message: { role: 'user', content: noteText('eee5', 'completed') } },
    // A dequeue is not an arrival.
    { type: 'queue-operation', operation: 'remove', content: noteText('fff6', 'completed') },
  ]);
  const t = await cc.readTranscript(p);
  assert.deepEqual([...t.notes.keys()].sort(), ['aaa1', 'bbb2', 'ccc3']);
  assert.equal(t.notes.get('bbb2').status, 'killed');
});

test('check 12 sorts every agent into its state, with each carrier and the foreground tool_result', () => {
  const w = world();
  const root = repo(w);
  const sid = 'sess-agents';
  // ✅ finished, notified: one agent per carrier shape.
  agent(w, sid, 'a1111111', { turns: finishedTurns, description: 'via attachment' });
  agent(w, sid, 'b2222222', { turns: finishedTurns, description: 'via queue enqueue' });
  agent(w, sid, 'c3333333', { turns: finishedTurns, description: 'via user record' });
  // ✅ stopped on purpose: cut mid-turn, but the parent saw it stopped.
  agent(w, sid, 'd4444444', { turns: cutTurns, description: 'duplicate, stopped' });
  // ✅ foreground: ended by the tool_result on its launch.
  agent(w, sid, 'e5555555', { turns: finishedTurns, description: 'foreground job', shape: 'foreground', toolUseId: 'toolu_fg' });
  // ⚠️ finished, never notified. Its launch's tool_result must not count as its end.
  agent(w, sid, 'f6666666', { turns: finishedTurns, description: 'result never read' });
  // ❌ cut mid-flight, no notification.
  agent(w, sid, 'a7777777', { turns: cutTurns, description: 'cut by a closed tab' });
  transcript(w, sid, [
    viaAttachment('a1111111', 'completed'), viaQueue('b2222222', 'completed'), viaUser('c3333333', 'completed'),
    viaQueue('d4444444', 'stopped'), toolResult('toolu_fg'), toolResult('toolu_f6666666'),
  ]);
  const j = json(w, root, ['--session', sid]);
  const c = j.by.subagents;
  assert.equal(c.status, 'fail', c.summary);
  assert.equal(j.code, 1);
  assert.deepEqual(c.counts, { agents: 7, reported: 4, stopped: 1, unconsumed: 1, cut: 1 });
  assert.match(c.summary, /7 agent\(s\) · 4 reported · 1 stopped on purpose · 1 finished, result never consumed · 1 cut mid-flight/);
  const a = agentLines(j);
  for (const id of ['a1111111', 'b2222222', 'c3333333']) {
    assert.equal(a[id].status, 'pass', id);
    assert.match(a[id].end, /completed notification/);
  }
  assert.equal(a.d4444444.status, 'pass');
  assert.match(a.d4444444.end, /stopped on purpose \(stopped notification\)/);
  assert.equal(a.e5555555.status, 'pass');
  assert.match(a.e5555555.end, /tool_result/);
  assert.equal(a.f6666666.status, 'warn');
  assert.match(a.f6666666.end, /never consumed/);
  assert.equal(a.a7777777.status, 'fail');
  assert.match(a.a7777777.end, /cut mid-flight: last turn is a tool_use with no result/);
  assert.equal(a.a7777777.short, 'a777777');
  assert.equal(a.a7777777.description, 'cut by a closed tab');
  // Problems list first, then each agent by short id, description and end.
  assert.match(c.items[0], /^❌ a777777 cut by a closed tab — cut mid-flight/);
  assert.match(c.items[1], /^⚠️ f666666 result never read — finished, but the parent has no notification/);
  assert.ok(c.items.some((x) => /^✅ d444444 duplicate, stopped — stopped on purpose/.test(x)));
  const text = ccclose(w, root, ['--session', sid]).out;
  assert.match(text, /❌ Subagents finished +7 agent\(s\)/);
  assert.match(text, /- ✅ e555555 foreground job — reported \(tool_result/);
});

test('check 12 passes when every agent was reported or stopped on purpose', () => {
  const w = world();
  const root = repo(w);
  agent(w, 'sess-agents-ok', 'a1111111', { turns: finishedTurns });
  agent(w, 'sess-agents-ok', 'd4444444', { turns: cutTurns });
  transcript(w, 'sess-agents-ok', [viaAttachment('a1111111', 'completed'), viaUser('d4444444', 'killed')]);
  const j = json(w, root, ['--session', 'sess-agents-ok']);
  assert.equal(j.by.subagents.status, 'pass', j.by.subagents.summary);
  assert.deepEqual(j.by.subagents.counts, { agents: 2, reported: 1, stopped: 1, unconsumed: 0, cut: 0 });
  assert.match(j.by.subagents.items.join('\n'), /stopped on purpose \(killed notification\)/);
});

test('check 12 warns, and does not fail the close, for a finished agent whose result was never consumed', () => {
  const w = world();
  const root = repo(w);
  write(root, 'docs/SESSIONS.md', '# Sessions\n- [today](sessions/today.md)\n');
  write(root, 'docs/sessions/today.md', '# today\n');
  commit(w, root, 'records: session close', NOW - 30 * MIN);
  sh(w, root, ['push', '-q', 'origin', 'main']);
  agent(w, 'sess-agents-warn', 'a1111111', { turns: finishedTurns });
  transcript(w, 'sess-agents-warn');
  const j = json(w, root, ['--session', 'sess-agents-warn']);
  assert.equal(j.by.subagents.status, 'warn');
  assert.deepEqual(j.by.subagents.counts, { agents: 1, reported: 0, stopped: 0, unconsumed: 1, cut: 0 });
  assert.equal(j.code, 0);
  assert.equal(j.verdict.status, 'warn');
});

test('a mention of the notification is not one: an agent only talked about stays unconsumed', () => {
  const w = world();
  const root = repo(w);
  agent(w, 'sess-agents-mention', 'a1111111', { turns: finishedTurns });
  transcript(w, 'sess-agents-mention', [
    { type: 'assistant', message: { content: [{ type: 'text', text: noteText('a1111111', 'completed') }] } },
  ]);
  const j = json(w, root, ['--session', 'sess-agents-mention']);
  assert.equal(j.by.subagents.status, 'warn');
});

test('an agent resumed after its completed notification and cut again is a fail, not a pass', () => {
  const w = world();
  const root = repo(w);
  // Notified at -20 min (transcript() stamps extras there); the agent worked on at -10.
  agent(w, 'sess-agents-resume', 'a1111111', { turns: [...finishedTurns, asst(-10, null, ['tool_use'])] });
  transcript(w, 'sess-agents-resume', [viaAttachment('a1111111', 'completed')]);
  const j = json(w, root, ['--session', 'sess-agents-resume']);
  assert.equal(j.by.subagents.status, 'fail');
  assert.match(j.by.subagents.items[0], /resumed after its completed notification and cut mid-flight/);
});

test('a resumed agent that finished again is judged by its LAST turn', () => {
  const w = world();
  const root = repo(w);
  agent(w, 'sess-agents-resume2', 'a1111111', { turns: [...cutTurns, asst(-40, null, ['thinking']), asst(-39, 'end_turn', ['text'])] });
  transcript(w, 'sess-agents-resume2', [viaQueue('a1111111', 'completed')]);
  assert.equal(json(w, root, ['--session', 'sess-agents-resume2']).by.subagents.status, 'pass');
});

test('check 12 is not applicable with no subagents/ directory, and says so rather than pass', () => {
  const w = world();
  const root = repo(w);
  transcript(w, 'sess-no-agents');
  const j = json(w, root, ['--session', 'sess-no-agents']);
  assert.equal(j.by.subagents.status, 'na');
  assert.match(j.by.subagents.summary, /^not applicable — no subagents\/ directory/);
  assert.deepEqual(j.by.subagents.counts, { agents: 0, reported: 0, stopped: 0, unconsumed: 0, cut: 0 });  // known zeros print
  assert.match(ccclose(w, root, ['--session', 'sess-no-agents']).out, /➖ Subagents finished +not applicable/);
  // With no transcript at all it is also not applicable, and the counts are unknown rather than zero.
  const none = json(w, root, ['--session', 'nothing-here']);
  assert.equal(none.by.subagents.status, 'na');
  assert.equal(none.by.subagents.counts, null);
});

test('an empty subagents/ directory is a known zero, not a skipped check', () => {
  const w = world();
  const root = repo(w);
  transcript(w, 'sess-empty-agents');
  fs.mkdirSync(path.join(w.home, '.claude', 'projects', 'proj', 'sess-empty-agents', 'subagents'), { recursive: true });
  const j = json(w, root, ['--session', 'sess-empty-agents']);
  assert.equal(j.by.subagents.status, 'pass');
  assert.match(j.by.subagents.summary, /^0 agent\(s\) · 0 reported · 0 stopped on purpose · 0 finished, result never consumed · 0 cut mid-flight/);
});

test('check 12 list is capped and the cut counted, with problems listed first', () => {
  const w = world();
  const root = repo(w);
  const n = cc.CAP + 4;
  for (let i = 0; i < n; i++) agent(w, 'sess-many-agents', `aa${String(i).padStart(6, '0')}`, { turns: finishedTurns });
  agent(w, 'sess-many-agents', 'zz999999', { turns: cutTurns, description: 'the one that matters' });
  transcript(w, 'sess-many-agents', Array.from({ length: n }, (_, i) => viaAttachment(`aa${String(i).padStart(6, '0')}`, 'completed')));
  const j = json(w, root, ['--session', 'sess-many-agents']);
  assert.equal(j.by.subagents.items.length, cc.CAP);
  assert.equal(j.by.subagents.itemsTotal, n + 1);
  assert.equal(j.by.subagents.counts.agents, n + 1);
  assert.match(j.by.subagents.items[0], /^❌ zz99999 the one that matters/);
  assert.match(ccclose(w, root, ['--session', 'sess-many-agents']).out, /… and 5 more/);
});

// --- documentation convention (REPO-STANDARD: concise --help + a man page) --

test('--help is a concise digest that points at the man page', () => {
  const help = execFileSync('node', [SCRIPT, '-h'], { encoding: 'utf8' });
  assert.ok(help.trimEnd().split('\n').length <= 24, '--help should stay a one-screen digest');
  assert.match(help, /man ccclose/);
  for (const opt of ['--session', '--root', '--json', '--identifiers']) assert.ok(help.includes(opt));
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

// --- --identifiers: the paste-ready block (RECORD.md) ----------------------

const idRun = (w, cwd, sid, env = {}) => ccclose(w, cwd, ['--session', sid, '--identifiers'], env);
const FIELDS = ['Session', 'Commits', 'Pull requests', 'Board', 'Worktrees and branches', 'Agents', 'Other repos'];
// The field headings, in order, as they appear in the block.
const headings = (out) => out.split('\n').filter((l) => l.startsWith('- **')).map((l) => l.match(/^- \*\*([^*]+)\*\*/)[1]);

const bashUse = (id, command, cwd) => ({ type: 'assistant', cwd, message: { model: 'claude-opus-5-5', content: [{ type: 'tool_use', id, name: 'Bash', input: { command } }] } });
const useResult = (id, text, isError = false) => ({ type: 'user', message: { role: 'user', content: [{ type: 'tool_result', tool_use_id: id, content: text, is_error: isError }] }, toolUseResult: { stdout: text } });

function boardWorld() {
  const w = world();
  const root = repo(w);
  write(root, 'docs/ROADMAP.md', '<!-- GENERATED by board.py -->\n# Roadmap\n');
  const item = (sec, n, first) => write(root, `docs/roadmap/${sec}-demo-section/${n}-item.md`, `${first}\n      body of the item\n`);
  // Before the window: 040 is claimed already.
  item('010', '040', '- [~] (claimed earlier)');
  commit(w, root, 'board: seed', NOW - 2 * 24 * 60 * MIN);
  // In the window, oldest first.
  item('010', '010', '- [ ] **a** filed');
  item('010', '020', '- [~] (claimed now) b');
  item('010', '030', '- [ ] **c** filed');
  item('010', '060', '- [ ] **f** filed');
  commit(w, root, 'board: file a, b, c, f', NOW - 40 * MIN);
  item('010', '030', '- [~] (claimed now) c');
  item('010', '040', '- [x] **DONE** d');
  item('010', '060', '- [~] (claimed now) f');
  commit(w, root, 'board: claim c and f; close d', NOW - 35 * MIN);
  item('010', '020', '- [x] **DONE** b');
  item('010', '060', '- [ ] **f** released');
  write(root, 'docs/roadmap/010-demo-section/010-item.md', '- [ ] **a** filed\n      body of the item\n      ⏳ cold review queued\n');
  commit(w, root, 'board: close b; release f; queue review on a', NOW - 30 * MIN);
  return { w, root };
}

test('--identifiers prints only the block, in RECORD order, with every field (the stable field set)', () => {
  const { w, root } = boardWorld();
  transcript(w, 'sess-id-1');
  const r = idRun(w, root, 'sess-id-1');
  assert.equal(r.code, 0);
  assert.ok(r.out.startsWith('## Identifiers\n'));
  assert.deepEqual(headings(r.out), FIELDS);
  assert.doesNotMatch(r.out, /close-out check|Checks\n|verdict/);
  assert.match(r.out, /- \*\*Session\*\*: sess-id-1 · Opus 5\.5 · \d{4}-\d\d-\d\d \d\d:\d\d to \d{4}-\d\d-\d\d \d\d:\d\d UTC\n/);
  assert.match(r.out, /- \*\*Other repos\*\*: not read by ccclose — fill in by hand\n/);
  assert.match(r.out.trimEnd().split('\n').pop(), /^\*Attribution: "this session's" = dated inside the window/);
});

test('a plain run ends with the identifiers block after the verdict; --json keeps the checks alone (210/300)', () => {
  const { w, root } = boardWorld();
  transcript(w, 'sess-id-1');
  const r = ccclose(w, root, ['--session', 'sess-id-1']);
  const at = r.out.indexOf('\n## Identifiers\n');
  assert.ok(at > 0, 'the block is printed');
  assert.match(r.out.slice(0, at), /(ready to close|not ready to close|some need a look)/);
  assert.deepEqual(headings(r.out.slice(at + 1)), FIELDS);
  const j = ccclose(w, root, ['--session', 'sess-id-1', '--json']);
  assert.doesNotMatch(j.out, /## Identifiers/);
  assert.ok(Array.isArray(JSON.parse(j.out).checks));
});

test('--identifiers commits: oldest first, short shas, and first^..last when unbroken', () => {
  const { w, root } = boardWorld();
  transcript(w, 'sess-id-2');
  const log = sh(w, root, ['log', '--reverse', '--format=%h', '-3']).split('\n');
  const j = JSON.parse(ccclose(w, root, ['--session', 'sess-id-2', '--identifiers', '--json']).out);
  assert.equal(j.commits.total, 3);
  assert.deepEqual(j.commits.items.map((x) => x.short), log);
  assert.equal(j.commits.unbroken, true);
  assert.equal(j.commits.range, `${log[0]}^..${log[2]}`);
  const out = idRun(w, root, 'sess-id-2').out;
  assert.match(out, new RegExp(`- \\*\\*Commits\\*\\* \\(3\\): ${log.join(' ')} · unbroken, \`${log[0]}\\^\\.\\.${log[2]}\``));
  // The range is a real git range over exactly these commits.
  assert.equal(sh(w, root, ['rev-list', '--count', `${log[0]}^..${log[2]}`]), '3');
});

test('--identifiers commits: a broken chain lists the shas and shows no range', () => {
  const w = world();
  const root = repo(w);
  write(root, 'a.txt', 'a'); commit(w, root, 'on main', NOW - 40 * MIN);
  sh(w, root, ['checkout', '-q', '-b', 'side']);
  write(root, 'b.txt', 'b'); commit(w, root, 'on side', NOW - 35 * MIN);
  sh(w, root, ['checkout', '-q', 'main']);
  write(root, 'c.txt', 'c'); commit(w, root, 'on main again', NOW - 30 * MIN);
  transcript(w, 'sess-id-3');
  const j = JSON.parse(ccclose(w, root, ['--session', 'sess-id-3', '--identifiers', '--json']).out);
  assert.equal(j.commits.total, 3);
  assert.equal(j.commits.unbroken, false);
  assert.equal(j.commits.range, null);
  assert.doesNotMatch(idRun(w, root, 'sess-id-3').out, /unbroken/);
});

test('--identifiers with no commits in the window prints zeros and none, not absence', () => {
  const w = world();
  const root = repo(w);
  write(root, 'docs/ROADMAP.md', '<!-- GENERATED by board.py -->\n');
  write(root, 'docs/roadmap/010-s/010-i.md', '- [ ] i\n');
  commit(w, root, 'old board', NOW - 2 * 24 * 60 * MIN);
  transcript(w, 'sess-id-4');
  const out = idRun(w, root, 'sess-id-4').out;
  assert.deepEqual(headings(out), FIELDS);
  assert.match(out, /- \*\*Commits\*\* \(0\): none\n/);
  assert.match(out, /- \*\*Pull requests\*\*: none/);
  assert.match(out, /  - completed: none\n  - created: none\n  - claimed \(still open\): none\n  - ⏳ review items created: none\n/);
  assert.match(out, /- \*\*Worktrees and branches\*\*: none\n/);
  assert.match(out, /- \*\*Agents\*\*: 0 · none launched\n/);
});

test('--identifiers board: completed, created and claimed groups, and the ⏳ items', () => {
  const { w, root } = boardWorld();
  transcript(w, 'sess-id-5');
  const j = JSON.parse(ccclose(w, root, ['--session', 'sess-id-5', '--identifiers', '--json']).out);
  assert.equal(j.board.known, true);
  // 020 (created claimed, then closed) and 040 (claimed before the window, closed in it).
  assert.deepEqual(j.board.completed, ['010/020', '010/040']);
  // Filed in the window: not 040, which pre-dates it.
  assert.deepEqual(j.board.created, ['010/010', '010/020', '010/030', '010/060']);
  // 030 is claimed and still open; 060 was claimed then released; 020 closed.
  assert.deepEqual(j.board.claimed, ['010/030']);
  assert.deepEqual(j.board.review, ['010/010']);
  const out = idRun(w, root, 'sess-id-5').out;
  assert.match(out, /  - completed: 010\/020, 010\/040\n/);
  assert.match(out, /  - created: 010\/010, 010\/020, 010\/030, 010\/060\n/);
  assert.match(out, /  - claimed \(still open\): 010\/030\n/);
  assert.match(out, /  - ⏳ review items created: 010\/010\n/);
});

test('--identifiers board: no board, or a hand-kept one, is marked by hand', () => {
  const w = world();
  const root = repo(w);
  transcript(w, 'sess-id-6');
  assert.match(idRun(w, root, 'sess-id-6').out, /- \*\*Board\*\*: by hand — this repo has no board\n/);
  write(root, 'ROADMAP.md', '# Roadmap (hand-kept)\n- [ ] one\n');
  commit(w, root, 'hand board', NOW - 30 * MIN);
  assert.match(idRun(w, root, 'sess-id-6').out, /- \*\*Board\*\*: by hand — ROADMAP\.md is hand-kept/);
});

test('--identifiers agents: present are counted and listed, absent print zero', () => {
  const w = world();
  const root = repo(w);
  agent(w, 'sess-id-7', 'aa111111', { turns: finishedTurns, description: 'Build the thing' });
  agent(w, 'sess-id-7', 'bb222222', { turns: cutTurns, description: 'The cut one' });
  transcript(w, 'sess-id-7', [viaAttachment('aa111111', 'completed')]);
  const out = idRun(w, root, 'sess-id-7').out;
  assert.match(out, /- \*\*Agents\*\*: 2 · 1 reported · 0 stopped on purpose · 0 result never consumed · 1 cut mid-flight\n/);
  assert.match(out, /  - aa11111 Build the thing — reported \(completed notification\)\n/);
  assert.match(out, /  - bb22222 The cut one — cut mid-flight/);
  transcript(w, 'sess-id-8');
  assert.match(idRun(w, root, 'sess-id-8').out, /- \*\*Agents\*\*: 0 · none launched\n/);
});

test('--identifiers agents: more than the checks cap are all listed', () => {
  const w = world();
  const root = repo(w);
  const n = cc.CAP + 3;
  for (let i = 0; i < n; i++) agent(w, 'sess-id-9', `aa${String(i).padStart(6, '0')}`, { turns: finishedTurns });
  transcript(w, 'sess-id-9', Array.from({ length: n }, (_, i) => viaAttachment(`aa${String(i).padStart(6, '0')}`, 'completed')));
  const j = JSON.parse(ccclose(w, root, ['--session', 'sess-id-9', '--identifiers', '--json']).out);
  assert.equal(j.agents.items.length, n);
});

test('worktreeAdds reads path and branch from the common forms of git worktree add', () => {
  assert.deepEqual(cc.worktreeAdds('git worktree add -b qr-1 /w/a-qr-1 origin/main', '/r'),
    [{ path: '/w/a-qr-1', branch: 'qr-1' }]);
  assert.deepEqual(cc.worktreeAdds('git -C /r worktree add ../w/two', '/elsewhere'),
    [{ path: '/w/two', branch: 'two' }]);
  assert.deepEqual(cc.worktreeAdds('cd /r && git worktree add "wt dir" topic', '/x'),
    [{ path: '/r/wt dir', branch: 'topic' }]);
  assert.deepEqual(cc.worktreeAdds('git worktree add --detach /w/d HEAD', '/r'), [{ path: '/w/d', branch: null }]);
  assert.deepEqual(cc.worktreeAdds('git worktree add -B again /w/e && echo hi', '/r'), [{ path: '/w/e', branch: 'again' }]);
  assert.deepEqual(cc.worktreeAdds('git worktree list', '/r'), []);
});

test('ghPrCommands reads merge numbers and ignores other repos, flag values and quoted mentions', () => {
  assert.deepEqual(cc.ghPrCommands('gh pr merge 12 --squash'), { creates: 0, merges: [12] });
  assert.deepEqual(cc.ghPrCommands('gh pr merge --squash --body 5 #13'), { creates: 0, merges: [13] });
  assert.deepEqual(cc.ghPrCommands('gh pr merge https://github.com/o/r/pull/14'), { creates: 0, merges: [14] });
  assert.deepEqual(cc.ghPrCommands('git push && gh pr create --fill && gh pr merge 15'), { creates: 1, merges: [15] });
  assert.deepEqual(cc.ghPrCommands('gh pr merge --squash'), { creates: 0, merges: [] });
  assert.deepEqual(cc.ghPrCommands('gh pr merge 16 -R other/repo'), { creates: 0, merges: [] });
  assert.deepEqual(cc.ghPrCommands('echo "then gh pr merge 17"'), { creates: 0, merges: [] });
});

test('--identifiers worktrees: created ones are read from the commands, put away or still present', () => {
  const w = world();
  const root = repo(w);
  const wt = path.join(w.base, 'wt-live');
  sh(w, root, ['worktree', 'add', '-q', '-b', 'live-branch', wt]);
  const gone = path.join(w.base, 'wt-gone');           // never on disk: put away
  transcript(w, 'sess-id-10', [
    bashUse('t1', `git worktree add -b gone-branch ${gone}`, root), useResult('t1', 'Preparing worktree'),
    bashUse('t2', `git worktree add -b live-branch ${wt}`, root), useResult('t2', 'Preparing worktree'),
    bashUse('t3', 'git worktree add -b failed-branch wt-failed', root), useResult('t3', 'fatal: no', true),
    { type: 'assistant', message: { content: [{ type: 'tool_use', id: 't4', name: 'EnterWorktree', input: { name: 'entered' } }] } },
    { type: 'user', message: { role: 'user', content: [{ type: 'tool_result', tool_use_id: 't4',
      content: `Created worktree at ${path.join(w.base, 'wt-entered')} on branch worktree-entered. The session is now working in the worktree.` }] },
    toolUseResult: { worktreePath: path.join(w.base, 'wt-entered'), worktreeBranch: 'worktree-entered' } },
    { type: 'assistant', message: { content: [{ type: 'tool_use', id: 't5', name: 'EnterWorktree', input: { path: wt } }] } },
    { type: 'user', message: { role: 'user', content: [{ type: 'tool_result', tool_use_id: 't5', content: `Entered existing worktree at ${wt}.` }] } },
  ]);
  const j = JSON.parse(ccclose(w, root, ['--session', 'sess-id-10', '--identifiers', '--json']).out);
  const by = Object.fromEntries(j.worktrees.items.map((x) => [x.branch, x]));
  assert.equal(j.worktrees.items.length, 3);                // failed add and entering an existing one are not creations
  assert.equal(by['gone-branch'].worktree, 'put away');
  assert.equal(by['gone-branch'].branchState, 'deleted');
  assert.equal(by['live-branch'].worktree, 'still present');
  assert.match(by['live-branch'].branchState, /^kept/);
  assert.equal(by['worktree-entered'].via, 'EnterWorktree');
  assert.equal(by['worktree-entered'].worktree, 'put away');
  const out = idRun(w, root, 'sess-id-10').out;
  assert.match(out, /- \*\*Worktrees and branches\*\* \(3\):\n/);
  assert.match(out, new RegExp(`  - ${gone.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')} \\(branch gone-branch\\) — worktree put away; branch deleted\n`));
  assert.match(out, /\(branch live-branch\) — worktree still present; branch kept/);
});

test('--identifiers worktrees: a relative path resolves against the record cwd', () => {
  const w = world();
  const root = repo(w);
  transcript(w, 'sess-id-11', [bashUse('r1', 'git worktree add -b rel-branch ../rel-wt', root), useResult('r1', 'ok')]);
  const j = JSON.parse(ccclose(w, root, ['--session', 'sess-id-11', '--identifiers', '--json']).out);
  assert.equal(j.worktrees.items[0].path, path.join(w.base, 'rel-wt'));
});

test('--identifiers worktrees: branches with a tip in the window and no command are still listed', () => {
  const w = world();
  const root = repo(w);
  sh(w, root, ['checkout', '-q', '-b', 'side-work']);
  write(root, 's.txt', 's'); commit(w, root, 'side', NOW - 30 * MIN);
  sh(w, root, ['checkout', '-q', 'main']);
  transcript(w, 'sess-id-12');
  const out = idRun(w, root, 'sess-id-12').out;
  assert.match(out, /  - branch side-work — branch kept, not merged\n/);
});

test('--identifiers PRs: opened, merged, still-open and other-repo PRs, with state from gh', () => {
  const w = world();
  const root = repo(w);
  sh(w, root, ['remote', 'set-url', 'origin', 'https://github.com/example/demo.git']);
  const stub = ghStub(w, {
    views: { 7: 'MERGED', 9: 'MERGED' },
    prs: [{ number: 11, title: 'still open', headRefName: 'topic', createdAt: new Date(NOW - 30 * MIN).toISOString(), url: 'u' },
      { number: 99, title: 'someone else', headRefName: 'old', createdAt: new Date(NOW - 5 * 24 * 60 * MIN).toISOString(), url: 'u' }],
  });
  transcript(w, 'sess-id-13', [
    bashUse('p1', 'gh pr create --fill', root), useResult('p1', 'https://github.com/example/demo/pull/7'),
    bashUse('p2', 'gh pr merge 7 --squash', root), useResult('p2', 'merged'),
    bashUse('p3', 'gh pr merge 9 --squash', root), useResult('p3', 'merged'),
    bashUse('p4', 'gh pr create --fill', root), useResult('p4', 'https://github.com/other/thing/pull/3'),
    bashUse('p5', 'gh pr merge 8', root), useResult('p5', 'not mergeable', true),
  ]);
  const j = JSON.parse(ccclose(w, root, ['--session', 'sess-id-13', '--identifiers', '--json'], { CCCLOSE_GH: stub }).out);
  const by = Object.fromEntries(j.pullRequests.items.map((x) => [x.number, x]));
  assert.deepEqual(Object.keys(by).sort(), ['11', '7', '9']);   // not 8 (failed), 3 (other repo) or 99 (not this session's)
  assert.deepEqual(by[7].did, ['opened', 'merge run']);
  assert.equal(by[7].state, 'merged');
  assert.deepEqual(by[9].did, ['merge run']);
  assert.equal(by[11].state, 'open');
  assert.equal(j.pullRequests.elsewhere, 1);
  const out = idRun(w, root, 'sess-id-13', { CCCLOSE_GH: stub }).out;
  assert.match(out, /- \*\*Pull requests\*\* \(3\):\n/);
  assert.match(out, /  - #7 opened \+ merge run — now merged\n/);
  assert.match(out, /  - #9 merge run — now merged\n/);
  assert.match(out, /  - #11 open, credited by the window — now open\n/);
  assert.match(out, /  - 1 more in another repo, listed by hand\n/);
});

test('--identifiers PRs: without gh the numbers still print, with the state marked unknown', () => {
  const w = world();
  const root = repo(w);
  sh(w, root, ['remote', 'set-url', 'origin', 'https://github.com/example/demo.git']);
  transcript(w, 'sess-id-14', [
    bashUse('p1', 'gh pr create --fill', root), useResult('p1', 'https://github.com/example/demo/pull/21'),
  ]);
  const out = idRun(w, root, 'sess-id-14').out;   // CCCLOSE_GH points at nothing
  assert.match(out, /  - #21 opened — state unknown\n/);
  assert.match(out, /gh is not installed, so states and open PRs are unknown/);
});

test('--identifiers with no transcript marks what it cannot derive by hand and still exits 0', () => {
  const w = world();
  const root = repo(w);
  const r = ccclose(w, root, ['--identifiers'], { CLAUDE_CODE_SESSION_ID: '' });
  assert.equal(r.code, 0);
  assert.deepEqual(headings(r.out), FIELDS);
  assert.match(r.out, /- \*\*Session\*\*: by hand — no session id · by hand — model unknown · by hand — window unknown/);
  assert.match(r.out, /- \*\*Commits\*\*: by hand — /);
  assert.match(r.out, /- \*\*Worktrees and branches\*\*: by hand — /);
  assert.match(r.out, /- \*\*Agents\*\*: by hand — /);
});

test('--identifiers --json carries the same fields', () => {
  const { w, root } = boardWorld();
  transcript(w, 'sess-id-15');
  const j = JSON.parse(ccclose(w, root, ['--session', 'sess-id-15', '--identifiers', '--json']).out);
  assert.equal(j.form, 'identifiers');
  assert.deepEqual(Object.keys(j), ['tool', 'form', 'session', 'commits', 'pullRequests', 'board', 'worktrees', 'agents', 'otherRepos', 'heuristic']);
  assert.equal(j.session.id, 'sess-id-15');
});
