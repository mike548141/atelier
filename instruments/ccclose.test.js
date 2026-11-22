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
    // The process table is a fixture too (check 15): a stub that prints
    // <base>/ps.txt, empty unless a test writes it. No test reads the real one.
    CCCLOSE_PS: path.join(base, 'ps-stub'),
  };
  fs.writeFileSync(path.join(base, 'ps.txt'), '');
  fs.writeFileSync(env.CCCLOSE_PS, `#!/bin/sh\ncat "${path.join(base, 'ps.txt')}"\n`);
  fs.chmodSync(env.CCCLOSE_PS, 0o755);
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
// Every commit made through the fixture is remembered by message, with its
// committer time and the repo it was made in, so a transcript can carry the
// command that made it at the time it ran (160/960: a command confirms a commit
// only by subject, repo, result and time).
const CT = new Map();
function commit(w, root, msg, when) {
  sh(w, root, ['add', '--', '.']);
  sh(w, root, ['commit', '-q', '-m', msg], when);
  if (when !== undefined) CT.set(msg, { when, root });
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
  'floor', 'reviews', 'bypasses', 'tree', 'subagents', 'scratch', 'pin', 'launched'];


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

test('stripWrappers unwraps <command-args>: an ask typed as a command argument is read (160/880 HC1)', () => {
  const cmd = '<command-message>wrap</command-message>\n<command-name>/wrap</command-name>\n<command-args>make sure the roadmap is updated</command-args>';
  assert.equal(cc.stripWrappers(cmd), 'make sure the roadmap is updated');
  assert.deepEqual(cc.askSentences(cc.stripWrappers(cmd)), ['make sure the roadmap is updated']);
  // The name and the message hold none of the principal's sentences; empty arguments leave nothing.
  assert.equal(cc.stripWrappers('<command-name>/clear</command-name><command-message>clear</command-message><command-args></command-args>'), '');
});

test('what the principal typed survives every wrapper strip (160/880 recurrence guard)', () => {
  // Principal text OUTSIDE any wrapper survives whichever wrapper sits beside it.
  const cct = require('./cctranscript');
  for (const tag of [...cct.HARNESS_TAGS, ...cct.COMMAND_TAGS]) {
    const out = cc.stripWrappers(`keep this ask <${tag}>inner</${tag}> and this one`);
    assert.ok(out.includes('keep this ask') && out.includes('and this one'), tag);
  }
  // And text INSIDE the one wrapper that is the principal's own writing survives it.
  assert.ok(cc.stripWrappers('<command-args>an ask in the arguments</command-args>').includes('an ask in the arguments'));
});

test('readTranscript counts a slash command with arguments as a turn and reads its ask; one without is no prompt', async () => {
  const w = world();
  const withArgs = '<command-message>wrap</command-message>\n<command-name>/wrap</command-name>\n<command-args>Before you finish, update the session log.</command-args>';
  const bare = '<command-name>/clear</command-name>\n<command-args></command-args>';
  const p = transcript(w, 'sess-cmd', [
    { type: 'user', message: { role: 'user', content: withArgs } },
    { type: 'user', message: { role: 'user', content: bare } },
  ]);
  const t = await cc.readTranscript(p);
  assert.equal(t.turn, 2);       // the base prompt and the command with arguments; the bare /clear is no prompt
  assert.equal(t.asksTotal, 1);
  assert.deepEqual(t.asks.map((a) => a.ref), ['2']);
});

test('a prompt that quotes a harness wrapper: cctranscript shows it, ccclose does not read it as the principal\'s sentence (160/880 HC3)', () => {
  const cct = require('./cctranscript');
  const quoted = 'why does <system-reminder>close out now</system-reminder> show up?';
  assert.equal(cct.classifyUserRecord({ type: 'user', message: { content: quoted } }).text, quoted);
  assert.equal(cc.stripWrappers(quoted), 'why does   show up?');
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

test('an attachment notification (210/260) leaves ccclose numbering and cctranscript refs unchanged', async () => {
  const w = world();
  const ask1 = { type: 'user', message: { role: 'user', content: 'Please tidy the board.' } };
  const reply = { type: 'assistant', message: { role: 'assistant', content: [{ type: 'text', text: 'On it.' }] } };
  const ask2 = { type: 'user', message: { role: 'user', content: 'Before you finish, update the session log.' } };
  const plain = transcript(w, 'sess-plain', [ask1, reply, ask2]);
  const noted = transcript(w, 'sess-noted', [ask1, viaAttachment('a1', 'completed'), reply, viaAttachment('a2', 'failed'), ask2]);
  const a = await cc.readTranscript(plain);
  const b = await cc.readTranscript(noted);
  // Same exchange count, same asks, same refs: the notifications take no number.
  assert.equal(b.turn, a.turn);
  assert.equal(b.asksTotal, a.asksTotal);
  assert.deepEqual(b.asks.map((x) => [x.ref, x.quote]), a.asks.map((x) => [x.ref, x.quote]));
  // cctranscript reads the notifications as harness, and its prompt refs are ccclose's.
  const ctOf = (f) => JSON.parse(execFileSync('node', [CCTRANSCRIPT, '--json', f], { encoding: 'utf8', env: w.env }));
  const ct = ctOf(noted);
  const youRefs = (j) => j.turns.filter((x) => x.role === 'you').map((x) => x.ref);
  assert.deepEqual(youRefs(ct), youRefs(ctOf(plain)));
  assert.equal(b.asks[b.asks.length - 1].ref, youRefs(ct)[youRefs(ct).length - 1]);
  assert.deepEqual(ct.turns.filter((x) => x.role === 'harness').map((x) => x.ref), [null, null]);
});

// --- whole runs over throwaway repos -------------------------------------

test('a tidy close passes every check that applies and exits 0', () => {
  const w = world();
  const root = repo(w);
  write(root, 'docs/sessions/2020-01-01-0000-today.md', '# today\n');
  commit(w, root, 'records: session close', NOW - 30 * MIN);
  sh(w, root, ['push', '-q', 'origin', 'main']);
  transcript(w, 'sess-tidy');
  const j = json(w, root, ['--session', 'sess-tidy']);
  assert.deepEqual(j.checks.map((c) => c.id), ID_ORDER);
  const want = { worktrees: 'pass', branches: 'pass', pushed: 'pass', prs: 'na', 'session-record': 'pass',
    board: 'na', claims: 'na', floor: 'na', reviews: 'na', bypasses: 'pass', tree: 'pass', subagents: 'na', scratch: 'na', pin: 'na', launched: 'pass' };
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

// Board 010/270: the folder is the log. A repo not yet swept may keep the
// retired one-file index, which counts as before until the grace date.
test('the session record is the folder: a session file passes, the retired index is named', () => {
  const w = world();
  const root = repo(w);
  write(root, 'docs/SESSIONS.md', '# Sessions\n');
  write(root, 'docs/sessions/old.md', '# old\n');
  commit(w, root, 'old log', NOW - 3 * 24 * 60 * MIN);
  write(root, 'docs/sessions/today.md', '# today\n');
  commit(w, root, 'records: session close', NOW - 30 * MIN);
  transcript(w, 'sess-folder');
  const j = json(w, root, ['--session', 'sess-folder']);
  assert.equal(j.by['session-record'].status, 'pass', j.by['session-record'].summary);
  assert.match(j.by['session-record'].summary, /1 commit\(s\) to docs\/sessions\/ in the window/);
  assert.match(j.by['session-record'].summary, /docs\/SESSIONS.md is retired/);
});

test('an index line alone counts until the grace date, and fails from it', () => {
  const w = world();
  const root = repo(w);
  write(root, 'SESSIONS.md', '# Sessions\n');
  commit(w, root, 'old log', NOW - 3 * 24 * 60 * MIN);
  fs.appendFileSync(path.join(root, 'SESSIONS.md'), '- today\n');
  commit(w, root, 'records: session close', NOW - 30 * MIN);
  transcript(w, 'sess-grace');
  let j = json(w, root, ['--session', 'sess-grace'], { CCCLOSE_TODAY: '2026-12-03' });
  assert.equal(j.by['session-record'].status, 'pass', j.by['session-record'].summary);
  assert.match(j.by['session-record'].summary, /retired index SESSIONS.md .* accepted until 2026-12-04/);
  j = json(w, root, ['--session', 'sess-grace'], { CCCLOSE_TODAY: '2026-12-04' });
  assert.equal(j.by['session-record'].status, 'fail', j.by['session-record'].summary);
  assert.match(j.by['session-record'].summary, /only the retired index SESSIONS.md was written/);
  // Beside a folder, an index line with no session file warns while the grace holds.
  const w2 = world();
  const root2 = repo(w2);
  write(root2, 'SESSIONS.md', '# Sessions\n');
  write(root2, 'sessions/old.md', '# old\n');
  commit(w2, root2, 'old log', NOW - 3 * 24 * 60 * MIN);
  fs.appendFileSync(path.join(root2, 'SESSIONS.md'), '- today\n');
  commit(w2, root2, 'records: session close', NOW - 30 * MIN);
  transcript(w2, 'sess-grace-2');
  j = json(w2, root2, ['--session', 'sess-grace-2'], { CCCLOSE_TODAY: '2026-12-03' });
  assert.equal(j.by['session-record'].status, 'warn', j.by['session-record'].summary);
  assert.match(j.by['session-record'].summary, /no session file under sessions\//);
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
  assert.match(text.out, /prompts unknown/);
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
  // Bypasses and launched work read the transcript and the host, not the repo.
  for (const id of ID_ORDER.filter((x) => x !== 'bypasses' && x !== 'launched')) assert.equal(j.by[id].status, 'na', id);
  assert.equal(j.by.launched.status, 'pass');
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
  for (const k of ['tool', 'session', 'window', 'repo', 'commits', 'prompts', 'models', 'checks', 'asked', 'askedAll', 'questions', 'otherRepos', 'liveSessions', 'verdict']) {
    assert.ok(k in a && k in b, k);
  }
  const text = ccclose(w, root, ['--session', 'sess-stable']).out;
  assert.match(text, /Asked in this session — answer each: done \/ queued \(item\) \/ not done/);
  assert.match(text, /keyword heuristic/);
  for (const head of ['Questions put to the principal', 'Other repos touched', 'Other live sessions in these repos']) assert.match(text, new RegExp(head));
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
  assert.deepEqual(c.counts, { agents: 7, reported: 4, stopped: 1, unconsumed: 1, running: 0, cut: 1, failed: 0 });
  assert.match(c.summary, /7 agent\(s\) · 4 reported · 1 stopped on purpose · 1 finished, result never consumed · 0 still running · 1 cut mid-flight · 0 failed/);
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

test('check 12 names a failed notification as its own state: a fail, counted apart from cut and unknown (210/400)', () => {
  const w = world();
  const root = repo(w);
  const sid = 'sess-agents-failed';
  // A background agent the parent was told failed; its own log stops mid-turn.
  agent(w, sid, 'a1111111', { turns: cutTurns, description: 'died on a tool error' });
  // A foreground agent that failed still returns a tool_result on its launch: the failure governs.
  agent(w, sid, 'b2222222', { turns: cutTurns, description: 'foreground, failed', shape: 'foreground', toolUseId: 'toolu_fgfail' });
  // A status the tool does not know stays an unknown: a warn, not a failure.
  agent(w, sid, 'c3333333', { turns: finishedTurns, description: 'odd status' });
  transcript(w, sid, [viaAttachment('a1111111', 'failed'), viaQueue('b2222222', 'failed'), toolResult('toolu_fgfail'),
    viaUser('c3333333', 'weird')]);
  const j = json(w, root, ['--session', sid]);
  const c = j.by.subagents;
  assert.equal(c.status, 'fail', c.summary);
  assert.deepEqual(c.counts, { agents: 3, reported: 0, stopped: 0, unconsumed: 1, running: 0, cut: 0, failed: 2 });
  assert.match(c.summary, /1 finished, result never consumed · 0 still running · 0 cut mid-flight · 2 failed/);
  const a = agentLines(j);
  assert.equal(a.a1111111.status, 'fail');
  assert.match(a.a1111111.end, /^failed \(the parent recorded a failed notification\)/);
  assert.equal(a.b2222222.status, 'fail');
  assert.match(a.b2222222.end, /^failed/);
  assert.match(a.c3333333.end, /status "weird", which ccclose does not know/);
  assert.match(c.items[0], /^❌ (a111111|b222222) /);
  assert.doesNotMatch(c.items.join('\n'), /cut mid-flight:/);
  // It reaches the --identifiers block too, as a known count.
  const out = idRun(w, root, sid).out;
  assert.match(out, /- \*\*Agents\*\*: 3 · 0 reported · 0 stopped on purpose · 1 result never consumed · 0 still running · 0 cut mid-flight · 2 failed\n/);
});

test('judgeAgent: a failed notification is failed whatever the transcript ends on, and a later completed one supersedes it', () => {
  const T = Date.now();
  const mk = (status) => ({ ...{ last: T, notes: new Map([['z1', { status, ts: T }]]), toolResults: new Map() } });
  const ag = (o = {}) => ({ id: 'z1', meta: {}, stop: null, blocks: ['tool_use'], lastTs: T - 1000, assistants: 1, ...o });
  assert.equal(cc.judgeAgent(ag(), mk('failed'), T).state, 'failed');
  assert.equal(cc.judgeAgent(ag({ stop: 'end_turn', blocks: ['text'] }), mk('failed'), T).state, 'failed');
  assert.equal(cc.judgeAgent(ag({ stop: 'end_turn', blocks: ['text'] }), mk('completed'), T).state, 'reported');
});

test('check 12 passes when every agent was reported or stopped on purpose', () => {
  const w = world();
  const root = repo(w);
  agent(w, 'sess-agents-ok', 'a1111111', { turns: finishedTurns });
  agent(w, 'sess-agents-ok', 'd4444444', { turns: cutTurns });
  transcript(w, 'sess-agents-ok', [viaAttachment('a1111111', 'completed'), viaUser('d4444444', 'killed')]);
  const j = json(w, root, ['--session', 'sess-agents-ok']);
  assert.equal(j.by.subagents.status, 'pass', j.by.subagents.summary);
  assert.deepEqual(j.by.subagents.counts, { agents: 2, reported: 1, stopped: 1, unconsumed: 0, running: 0, cut: 0, failed: 0 });
  assert.match(j.by.subagents.items.join('\n'), /stopped on purpose \(killed notification\)/);
});

test('check 12 warns, and does not fail the close, for a finished agent whose result was never consumed', () => {
  const w = world();
  const root = repo(w);
  write(root, 'docs/sessions/2020-01-01-0000-today.md', '# today\n');
  commit(w, root, 'records: session close', NOW - 30 * MIN);
  sh(w, root, ['push', '-q', 'origin', 'main']);
  agent(w, 'sess-agents-warn', 'a1111111', { turns: finishedTurns });
  transcript(w, 'sess-agents-warn');
  const j = json(w, root, ['--session', 'sess-agents-warn']);
  assert.equal(j.by.subagents.status, 'warn');
  assert.deepEqual(j.by.subagents.counts, { agents: 1, reported: 0, stopped: 0, unconsumed: 1, running: 0, cut: 0, failed: 0 });
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

// --- check 12: a running agent is not a cut one (210/380) ------------------
//
// An agent with no end recorded is "running" while its own transcript is still
// growing, and "cut" once it has been silent past FRESH_MS. NOW is fixed when
// the module loads and a loaded machine can run a test minutes later, so a
// "just now" record is stamped from the wall clock at the call: rel(s) is s
// seconds ago, in the minutes-from-NOW frame asst() and transcript() use.
const rel = (secs) => (Date.now() - NOW) / MIN - secs / 60;

test('check 12 reads an agent whose transcript is still growing as running, not cut', () => {
  const w = world();
  const root = repo(w);
  // Last record 20 s ago; the parent's own last record is just now.
  agent(w, 'sess-run', 'a1111111', { turns: [asst(rel(60), null, ['thinking']), asst(rel(20), null, ['tool_use'])], description: 'still at it' });
  // The same shape, long silent: the old cut.
  agent(w, 'sess-run', 'b2222222', { turns: cutTurns, description: 'long silent' });
  transcript(w, 'sess-run', [], rel(0));
  const j = json(w, root, ['--session', 'sess-run']);
  const c = j.by.subagents;
  assert.deepEqual(c.counts, { agents: 2, reported: 0, stopped: 0, unconsumed: 0, running: 1, cut: 1, failed: 0 });
  assert.match(c.summary, /1 still running · 1 cut mid-flight/);
  const a = agentLines(j);
  assert.equal(a.a1111111.state, 'running');
  assert.match(a.a1111111.end, /^still running: its transcript last grew \d+ (s|min) ago/);
  assert.doesNotMatch(a.a1111111.end, /cut/);
  assert.equal(a.b2222222.state, 'cut');
  // A running agent still holds the close: the check fails and the exit is 1.
  assert.equal(c.status, 'fail');
  assert.equal(j.code, 1);
  const text = ccclose(w, root, ['--session', 'sess-run']).out;
  assert.match(text, /- ❌ a111111 still at it — still running: its transcript last grew/);
});

test('a running agent alone fails the check but is never called cut', () => {
  const w = world();
  const root = repo(w);
  agent(w, 'sess-run1', 'a1111111', { turns: [asst(rel(6), null, ['tool_use'])] });
  transcript(w, 'sess-run1', [], rel(0));
  const c = json(w, root, ['--session', 'sess-run1']).by.subagents;
  assert.equal(c.status, 'fail');
  assert.deepEqual(c.counts, { agents: 1, reported: 0, stopped: 0, unconsumed: 0, running: 1, cut: 0, failed: 0 });
  assert.doesNotMatch(c.items.join('\n'), /cut mid-flight:/);
});

test('judgeAgent: the freshness test reads the agent clock and the parent clock, and a boundary is fresh', () => {
  const T = Date.parse('2026-01-01T00:00:00Z');
  const agentAt = (lastTs, extra = {}) => ({ id: 'z1', meta: {}, stop: null, blocks: ['tool_use'], assistants: 1, lastTs, ...extra });
  const parent = (last) => ({ notes: new Map(), toolResults: new Map(), last });
  const F = cc.FRESH_MS;
  // Exactly FRESH_MS silent is still running; a millisecond more is cut.
  assert.equal(cc.judgeAgent(agentAt(T - F), parent(T), T).state, 'running');
  assert.equal(cc.judgeAgent(agentAt(T - F - 1), parent(T), T).state, 'cut');
  // The parent carried on for more than FRESH_MS after the agent's last record: stalled, though the clock is near.
  assert.equal(cc.judgeAgent(agentAt(T - 1000), parent(T + F), T).state, 'cut');
  // A parent idle while its agent works (parent last long before the agent's) is no evidence against it.
  assert.equal(cc.judgeAgent(agentAt(T - 1000), parent(T - 3 * F), T).state, 'running');
  // No record time at all is no evidence of growth.
  assert.equal(cc.judgeAgent(agentAt(null), parent(T), T).state, 'cut');
  // A finished agent, or one the parent has an end for, is never running.
  assert.equal(cc.judgeAgent(agentAt(T, { stop: 'end_turn', blocks: ['text'] }), parent(T), T).state, 'unconsumed');
  const stopped = { ...parent(T), notes: new Map([['z1', { status: 'killed', ts: T }]]) };
  assert.equal(cc.judgeAgent(agentAt(T), stopped, T).state, 'stopped');
});

test('an agent resumed after its completed notification is running while it grows, cut once it goes quiet', () => {
  const w = world();
  const root = repo(w);
  // Notified at -20 min (transcript() stamps extras there); the agent is working on, a record 10 s ago.
  agent(w, 'sess-run2', 'a1111111', { turns: [...finishedTurns, asst(rel(10), null, ['tool_use'])] });
  transcript(w, 'sess-run2', [viaAttachment('a1111111', 'completed')], rel(0));
  const j = json(w, root, ['--session', 'sess-run2']);
  assert.equal(agentLines(j).a1111111.state, 'running');
  assert.equal(j.by.subagents.status, 'fail');
  // The same agent, last record at -10 min, is the resumed-and-cut case again.
  agent(w, 'sess-run3', 'a1111111', { turns: [...finishedTurns, asst(-10, null, ['tool_use'])] });
  transcript(w, 'sess-run3', [viaAttachment('a1111111', 'completed')]);
  assert.equal(agentLines(json(w, root, ['--session', 'sess-run3'])).a1111111.state, 'cut');
});

test('check 12 is not applicable with no subagents/ directory, and says so rather than pass', () => {
  const w = world();
  const root = repo(w);
  transcript(w, 'sess-no-agents');
  const j = json(w, root, ['--session', 'sess-no-agents']);
  assert.equal(j.by.subagents.status, 'na');
  assert.match(j.by.subagents.summary, /^not applicable — no subagents\/ directory/);
  assert.deepEqual(j.by.subagents.counts, { agents: 0, reported: 0, stopped: 0, unconsumed: 0, running: 0, cut: 0, failed: 0 });  // known zeros print
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
  assert.match(j.by.subagents.summary, /^0 agent\(s\) · 0 reported · 0 stopped on purpose · 0 finished, result never consumed · 0 still running · 0 cut mid-flight · 0 failed/);
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

// --- a refused delete re-routed (180/180) ---------------------------------

test('deleteRoutes names each delete route and leaves look-alikes alone', () => {
  assert.deepEqual(cc.deleteRoutes('rm -rf /tmp/x'), ['rm']);
  assert.deepEqual(cc.deleteRoutes('ls; rm a'), ['rm']);
  assert.deepEqual(cc.deleteRoutes('find . -name "*.tmp" -exec rm {} +'), ['rm']);
  assert.deepEqual(cc.deleteRoutes('rmdir empty'), ['rmdir']);
  assert.deepEqual(cc.deleteRoutes('unlink f'), ['unlink']);
  assert.deepEqual(cc.deleteRoutes('find /tmp/s -type f -delete'), ['find -delete']);
  assert.deepEqual(cc.deleteRoutes('python3 -c "import shutil; shutil.rmtree(p)"'), ['python rmtree']);
  assert.deepEqual(cc.deleteRoutes('python3 -c "import os; os.remove(p)"'), ['python os delete']);
  assert.deepEqual(cc.deleteRoutes('python3 -c "os.unlink(p)"'), ['python os delete']);
  assert.deepEqual(cc.deleteRoutes('python3 -c "p.unlink(missing_ok=True)"'), ['python pathlib delete']);
  assert.deepEqual(cc.deleteRoutes('node -e "fs.rmSync(d, {recursive: true})"'), ['node fs delete']);
  for (const ok of ['git rm --cached f', 'docker run --rm img', 'ls form', 'cat rm.txt', 'git worktree remove wt',
    'grep -n unlinked f', 'echo confirm']) {
    assert.deepEqual(cc.deleteRoutes(ok), [], ok);
  }
});

test('isRefusal reads the harness\'s refusal wordings and nothing else', () => {
  const err = (content) => ({ type: 'tool_result', is_error: true, content });
  for (const c of [
    'Permission to use Bash with command rm -rf /tmp/x has been denied.',
    'Permission for this action was denied by the Claude Code auto mode classifier. Reason: x',
    'The user doesn\'t want to proceed with this tool use. The tool use was rejected.',
    'Auto mode could not evaluate this action and is blocking it for safety.',
    'This Bash command contains multiple operations. The following parts require approval: rm -rf x',
  ]) assert.equal(cc.isRefusal(err(c)), true, c);
  assert.equal(cc.isRefusal(err([{ type: 'text', text: 'Permission to use Bash has been denied.' }])), true);
  assert.equal(cc.isRefusal(err('Exit code 1\nrm: x: No such file or directory')), false);
  assert.equal(cc.isRefusal({ type: 'tool_result', content: 'Permission to use Bash has been denied.' }), false);
});

// A Bash tool_use and its result, as the parent transcript records them.
const delUse = (id, command, m) => ({ type: 'assistant', timestamp: at(m), message: { model: 'claude-opus-5-5',
  content: [{ type: 'tool_use', id, name: 'Bash', input: { command } }] } });
const delResult = (id, content, m, isError = false) => ({ type: 'user', timestamp: at(m), toolUseResult: 'x',
  message: { role: 'user', content: [{ type: 'tool_result', tool_use_id: id, content, ...(isError ? { is_error: true } : {}) }] } });
const DENIED = (cmd) => `Permission to use Bash with command ${cmd} has been denied.`;
const rerouted = (t) => t.bypasses.filter((b) => b.kinds.some((k) => k.startsWith('refused delete re-routed')));

test('a delete by another route after a refused rm is flagged; a retry by rm is not', async () => {
  const w = world();
  const p = transcript(w, 'sess-reroute', [
    delUse('t1', 'rm -rf /tmp/s/old', -40), delResult('t1', DENIED('rm -rf /tmp/s/old'), -40, true),
    delUse('t2', 'python3 -I -c "import shutil; shutil.rmtree(\'/tmp/s/old\')"', -30), delResult('t2', '', -30),
    delUse('t3', 'find /tmp/s -type f -delete', -25), delResult('t3', '', -25),
    delUse('t4', 'rm -rf /tmp/s/old', -10), delResult('t4', '', -10),
    delUse('t5', 'rm -f /tmp/s/a && rmdir /tmp/s', -5), delResult('t5', '', -5),
  ]);
  const t = await cc.readTranscript(p);
  const hits = rerouted(t);
  assert.equal(hits.length, 2);
  assert.match(hits[0].kinds[0], /^refused delete re-routed \(refused: rm at \d{4}-\d\d-\d\d \d\d:\d\d UTC; now: python rmtree\)$/);
  assert.match(hits[1].kinds[0], /now: find -delete\)$/);
  assert.equal(t.bypassesTotal, 2);
});

test('no re-route without a refusal: a failed rm, a delete before the refusal landed, an unrefused session', async () => {
  const w = world();
  const failed = transcript(w, 'sess-failed-rm', [
    delUse('f1', 'rm /tmp/s/x', -40), delResult('f1', 'Exit code 1\nrm: /tmp/s/x: No such file or directory', -40, true),
    delUse('f2', 'python3 -c "import os; os.remove(\'/tmp/s/y\')"', -30), delResult('f2', '', -30),
  ]);
  assert.equal(rerouted(await cc.readTranscript(failed)).length, 0);
  // Two calls in one turn: the second was issued before the first's refusal came back.
  const parallel = transcript(w, 'sess-parallel', [
    delUse('p1', 'rm -rf /tmp/s/old', -40), delUse('p2', 'find /tmp/s -delete', -40),
    delResult('p1', DENIED('rm -rf /tmp/s/old'), -39, true), delResult('p2', '', -39),
  ]);
  assert.equal(rerouted(await cc.readTranscript(parallel)).length, 0);
  const plain = transcript(w, 'sess-plain-delete', [
    delUse('n1', 'python3 -c "import shutil; shutil.rmtree(\'/tmp/s\')"', -30), delResult('n1', '', -30),
  ]);
  assert.equal(rerouted(await cc.readTranscript(plain)).length, 0);
});

test('a refused Python delete re-routed to rm is flagged in the workaround check of a whole run', () => {
  const w = world();
  const root = repo(w);
  transcript(w, 'sess-reroute-run', [
    delUse('r1', 'python3 -c "import os; os.remove(\'/tmp/s/x\')"', -40),
    delResult('r1', 'The user doesn\'t want to proceed with this tool use. The tool use was rejected.', -40, true),
    delUse('r2', 'rm /tmp/s/x', -30), delResult('r2', '', -30),
  ]);
  const j = json(w, root, ['--session', 'sess-reroute-run']);
  assert.equal(j.by.bypasses.status, 'warn');
  assert.equal(j.by.bypasses.itemsTotal, 1);
  assert.match(j.by.bypasses.items[0], /\[refused delete re-routed \(refused: python os delete at .+; now: rm\)\] rm \/tmp\/s\/x/);
});

// --- check 13: the scratch folder (180/170) --------------------------------

const envRecord = (dir) => ({ type: 'attachment', attachment: { type: 'environment', snapshot: { workingDirectory: '/x', scratchpadDirectory: dir } } });

test('check 13 counts the files and folders left in the scratch folder the transcript records', () => {
  const w = world();
  const root = repo(w);
  const scratch = path.join(w.base, 'scratch');
  write(scratch, 'notes.txt', 'n');
  write(scratch, 'w-one/out.log', 'o');
  write(scratch, 'w-one/deep/exit.txt', 'exit=0');
  fs.mkdirSync(path.join(scratch, 'empty'));
  transcript(w, 'sess-scratch', [envRecord(path.join(w.base, 'gone')), envRecord(scratch)]);
  const j = json(w, root, ['--session', 'sess-scratch']);
  assert.equal(j.by.scratch.status, 'warn');
  assert.equal(j.by.scratch.summary, `3 file(s) and 3 folder(s) left in ${scratch} — clear them, or name each as a loose end`);
  assert.deepEqual(j.by.scratch.items, ['notes.txt', 'w-one/deep/exit.txt', 'w-one/out.log']);
  assert.equal(j.by.scratch.itemsTotal, 3);
  assert.equal(j.code, 0);   // a look, not a fail
  assert.equal(j.verdict.status, 'warn');
  assert.match(ccclose(w, root, ['--session', 'sess-scratch']).out, /⚠️ Scratch folder empty +3 file\(s\) and 3 folder\(s\) left in/);
});

test('check 13 passes on an empty or removed scratch folder, and is not applicable with none recorded', () => {
  const w = world();
  const root = repo(w);
  const empty = path.join(w.base, 'empty-scratch');
  fs.mkdirSync(empty);
  transcript(w, 'sess-scratch-empty', [envRecord(empty)]);
  const e = json(w, root, ['--session', 'sess-scratch-empty']);
  assert.equal(e.by.scratch.status, 'pass');
  assert.equal(e.by.scratch.summary, `${empty} is empty`);
  transcript(w, 'sess-scratch-gone', [envRecord(path.join(w.base, 'nope'))]);
  const g = json(w, root, ['--session', 'sess-scratch-gone']);
  assert.equal(g.by.scratch.status, 'pass');
  assert.match(g.by.scratch.summary, /no longer exists$/);
  transcript(w, 'sess-scratch-none');
  const n = json(w, root, ['--session', 'sess-scratch-none']);
  assert.equal(n.by.scratch.status, 'na');
  assert.equal(n.by.scratch.summary, 'the transcript records no scratch folder');
  assert.equal(json(w, root, ['--session', 'no-such']).by.scratch.status, 'na');
});

test('check 13 lists only folders when no file is left, and caps the file list', () => {
  const w = world();
  const root = repo(w);
  const dirsOnly = path.join(w.base, 'dirs-only');
  fs.mkdirSync(path.join(dirsOnly, 'a', 'b'), { recursive: true });
  transcript(w, 'sess-scratch-dirs', [envRecord(dirsOnly)]);
  const d = json(w, root, ['--session', 'sess-scratch-dirs']);
  assert.equal(d.by.scratch.status, 'warn');
  assert.match(d.by.scratch.summary, /^0 file\(s\) and 2 folder\(s\) left in/);
  assert.deepEqual(d.by.scratch.items, ['a', 'a/b']);
  const many = path.join(w.base, 'many');
  for (let i = 0; i < cc.CAP + 3; i++) write(many, `f${String(i).padStart(3, '0')}.txt`, 'x');
  transcript(w, 'sess-scratch-many', [envRecord(many)]);
  const m = json(w, root, ['--session', 'sess-scratch-many']);
  assert.equal(m.by.scratch.items.length, cc.CAP);
  assert.equal(m.by.scratch.itemsTotal, cc.CAP + 3);
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

// The session's own `git commit` commands, one per message: the house form
// (`git commit -q -m`), so the transcript carries the message and never a SHA.
const iso = (ms) => new Date(ms).toISOString();
// A Bash call and its result, timed around `ms` (the moment the commit was made).
const ran = (id, command, ms, cwd, isError = false) => [
  { ...bashUse(id, command, cwd), timestamp: iso(ms - 500) },
  { ...useResult(id, isError ? 'error: exit 1' : 'ok', isError), timestamp: iso(ms + 500) },
];
const commitCmd = (id, msg, over = {}) => {
  const c = CT.get(msg);
  return ran(id, `git add -- x && git commit -q -m ${JSON.stringify(msg)}`, over.when === undefined ? c.when : over.when, over.cwd === undefined ? c.root : over.cwd, !!over.error);
};
const committed = (...msgs) => msgs.flatMap((m, i) => commitCmd(`c${i}-${m.length}`, m));
// A commit command for `msg` with its own text, run in the repo where the fixture made it.
const ranFor = (id, command, msg, extra = {}) => ran(id, command, CT.get(msg).when, extra.cwd === undefined ? CT.get(msg).root : extra.cwd, !!extra.error);
// (The seed commit is days old, before the window: the session ran no command for it.)
const BOARD_MSGS = ['board: file a, b, c, f', 'board: claim c and f; close d', 'board: close b; release f; queue review on a'];

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
  write(root, 'docs/roadmap/010-demo-section/010-item.md', '- [ ] ⏳ **a** filed\n      body of the item\n');
  commit(w, root, 'board: close b; release f; queue review on a', NOW - 30 * MIN);
  return { w, root };
}

test('--identifiers prints only the block, in RECORD order, with every field (the stable field set)', () => {
  const { w, root } = boardWorld();
  transcript(w, 'sess-id-1', committed(...BOARD_MSGS));
  const r = idRun(w, root, 'sess-id-1');
  assert.equal(r.code, 0);
  assert.ok(r.out.startsWith('## Identifiers\n'));
  assert.deepEqual(headings(r.out), FIELDS);
  assert.doesNotMatch(r.out, /close-out check|Checks\n|verdict/);
  assert.match(r.out, /- \*\*Session\*\*: sess-id-1 · Opus 5\.5 · \d{4}-\d\d-\d\d \d\d:\d\d to \d{4}-\d\d-\d\d \d\d:\d\d UTC\n/);
  assert.match(r.out, /- \*\*Other repos\*\*: none found\n/);
  assert.match(r.out.trimEnd().split('\n').pop(), /^\*Attribution: commits and board movement above the unconfirmed lines are matched to commit commands/);
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
  transcript(w, 'sess-id-2', committed(...BOARD_MSGS));
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
  transcript(w, 'sess-id-3', committed('on main', 'on side', 'on main again'));
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
  assert.match(out, /  - completed: none\n  - created: none\n  - claimed \(still open\): none\n  - claimed, then closed or released by an unconfirmed commit: none\n  - ⏳ review items created: none\n/);
  assert.match(out, /  - unconfirmed, only through a squash merge this session did not run: none\n/);
  assert.match(out, /- \*\*Worktrees and branches\*\*: none\n/);
  assert.match(out, /- \*\*Agents\*\*: 0 · none launched\n/);
});

test('--identifiers board: completed, created and claimed groups, and the ⏳ items', () => {
  const { w, root } = boardWorld();
  transcript(w, 'sess-id-5', committed(...BOARD_MSGS));
  const j = JSON.parse(ccclose(w, root, ['--session', 'sess-id-5', '--identifiers', '--json']).out);
  assert.equal(j.board.known, true);
  // 020 (created claimed, then closed) and 040 (claimed before the window, closed in it).
  assert.deepEqual(j.board.completed, ['010/020', '010/040']);
  // Filed in the window: not 040, which pre-dates it.
  assert.deepEqual(j.board.created, ['010/010', '010/020', '010/030', '010/060']);
  // 030 is claimed and still open; 060 was claimed then released; 020 closed.
  assert.deepEqual(j.board.claimed, ['010/030']);
  assert.deepEqual(j.board.review, ['010/010']);
  assert.deepEqual(j.board.unconfirmed, { completed: [], created: [], claimed: [], review: [], reviewElsewhere: [] });
  assert.deepEqual(j.board.viaSquash, { completed: [], created: [], claimed: [], review: [], reviewElsewhere: [] });
  const out = idRun(w, root, 'sess-id-5').out;
  assert.match(out, /  - unconfirmed, from window-only commits: none\n/);
  assert.match(out, /  - completed: 010\/020, 010\/040\n/);
  assert.match(out, /  - created: 010\/010, 010\/020, 010\/030, 010\/060\n/);
  assert.match(out, /  - claimed \(still open\): 010\/030\n/);
  assert.match(out, /  - ⏳ review items created: 010\/010\n/);
  assert.deepEqual(j.board.claimedMoved, []);
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
  assert.match(out, /- \*\*Agents\*\*: 2 · 1 reported · 0 stopped on purpose · 0 result never consumed · 0 still running · 1 cut mid-flight · 0 failed\n/);
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

// 210/330: a shell variable in the path is read from a literal assignment, and a
// path that cannot be resolved is dropped, never listed under a made-up name.
test('worktreeAdds expands a variable from a literal assignment in the same command', () => {
  assert.deepEqual(cc.worktreeAdds('W=/w/var-one && git worktree add --detach $W origin/main', '/r'),
    [{ path: '/w/var-one', branch: null }]);
  assert.deepEqual(cc.worktreeAdds('W="/w/var two"; git worktree add -b br ${W}/sub', '/r'),
    [{ path: '/w/var two/sub', branch: 'br' }]);
  assert.deepEqual(cc.worktreeAdds('R=/repo && cd $R && git worktree add -b b2 ../rel', '/x'),
    [{ path: '/rel', branch: 'b2' }]);
  assert.deepEqual(cc.worktreeAdds('A=/w/a && A=/w/b && git worktree add $A', '/r'), [{ path: '/w/b', branch: 'b' }]);
});

test('worktreeAdds expands a variable assigned earlier in the transcript', () => {
  const vars = new Map([['W', '/w/earlier']]);
  assert.deepEqual(cc.worktreeAdds('git worktree add --detach $W origin/main', '/r', vars),
    [{ path: '/w/earlier', branch: null }]);
  // A later assignment in the command wins over the transcript's.
  assert.deepEqual(cc.worktreeAdds('W=/w/later && git worktree add --detach $W', '/r', vars),
    [{ path: '/w/later', branch: null }]);
});

test('worktreeAdds drops a path it cannot resolve rather than invent one', () => {
  assert.deepEqual(cc.worktreeAdds('git worktree add --detach $W origin/main', '/r'), []);
  assert.deepEqual(cc.worktreeAdds('git worktree add --detach "${NOPE}/x"', '/r'), []);
  assert.deepEqual(cc.worktreeAdds('git worktree add -b b "$(mktemp -d)"', '/r'), []);
  assert.deepEqual(cc.worktreeAdds('git worktree add -b b `mktemp -d`', '/r'), []);
  // A prefix assignment is not seen by the same command's own expansion.
  assert.deepEqual(cc.worktreeAdds('W=/w/prefix git worktree add --detach $W', '/r'), []);
  // An unknown directory only matters to a relative path.
  assert.deepEqual(cc.worktreeAdds('cd $UNSET && git worktree add -b b rel', '/r'), []);
  assert.deepEqual(cc.worktreeAdds('cd $UNSET && git worktree add -b b /w/abs', '/r'), [{ path: '/w/abs', branch: 'b' }]);
  // The other adds in the same command survive.
  assert.deepEqual(cc.worktreeAdds('git worktree add --detach $W && git worktree add -b ok /w/ok', '/r'),
    [{ path: '/w/ok', branch: 'ok' }]);
});

test('worktreeAdds leaves a plain literal path as it was', () => {
  assert.deepEqual(cc.worktreeAdds('git worktree add -b plain /w/plain origin/main', '/r'), [{ path: '/w/plain', branch: 'plain' }]);
  assert.deepEqual(cc.worktreeAdds('git worktree add "/w/with space" topic', '/r'), [{ path: '/w/with space', branch: 'topic' }]);
});

test('--identifiers worktrees: a $VAR path is listed as resolved, and an unresolvable one is not listed at all (210/330)', () => {
  const w = world();
  const root = repo(w);
  const good = path.join(w.base, 'wt-var-good');
  const early = path.join(w.base, 'wt-var-early');
  transcript(w, 'sess-id-13', [
    bashUse('v1', `W=${good} && git worktree add --detach $W origin/main`, root), useResult('v1', 'Preparing worktree'),
    bashUse('v2', `E=${early}`, root), useResult('v2', ''),
    bashUse('v3', 'git worktree add --detach $E origin/main', root), useResult('v3', 'Preparing worktree'),
    bashUse('v4', 'git worktree add --detach $NEVER_SET origin/main', root), useResult('v4', 'Preparing worktree'),
  ]);
  const j = JSON.parse(ccclose(w, root, ['--session', 'sess-id-13', '--identifiers', '--json']).out);
  assert.deepEqual(j.worktrees.items.map((x) => x.path).sort(), [early, good].sort());
  const out = idRun(w, root, 'sess-id-13').out;
  assert.doesNotMatch(out, /\$W|\$E|NEVER_SET/);
});

// 210/360: a `for` loop over plain words is expanded once per word; any add left
// unresolved is counted, so the block says it under-lists instead of staying silent.
test('worktreeAdds expands a for loop over a literal word list, once per word', () => {
  assert.deepEqual(cc.worktreeAdds('for n in a b c; do git worktree add -b qr-$n /w/qr-$n origin/main; done', '/r'),
    [{ path: '/w/qr-a', branch: 'qr-a' }, { path: '/w/qr-b', branch: 'qr-b' }, { path: '/w/qr-c', branch: 'qr-c' }]);
  assert.deepEqual(cc.worktreeAdds('for n in a b\ndo\n  git worktree add --detach "/w/wt-${n}" origin/main\ndone', '/r'),
    [{ path: '/w/wt-a', branch: null }, { path: '/w/wt-b', branch: null }]);
  // Nested literal loops multiply; a word list may be quoted.
  assert.deepEqual(cc.worktreeAdds('for r in x y; do for n in 1 2; do git worktree add --detach /w/$r-$n; done; done', '/r').map((a) => a.path),
    ['/w/x-1', '/w/x-2', '/w/y-1', '/w/y-2']);
  assert.deepEqual(cc.worktreeAdds("for n in 'a' \"b\"; do git worktree add --detach /w/$n; done", '/r').map((a) => a.path), ['/w/a', '/w/b']);
  // An add after the loop is not inside it, and a loop's variable is not known there.
  const st = { unresolved: 0 };
  assert.deepEqual(cc.worktreeAdds('for n in a b; do echo $n; done; git worktree add --detach /w/$n', '/r', new Map(), st), []);
  assert.equal(st.unresolved, 1);
  // A relative path resolves against the cwd, per word.
  assert.deepEqual(cc.worktreeAdds('for n in a b; do git worktree add -b $n ../$n; done', '/r/sub').map((a) => a.path), ['/r/a', '/r/b']);
});

test('worktreeAdds counts an add it cannot resolve and never guesses its path', () => {
  const count = (cmd, vars) => {
    const st = { unresolved: 0 };
    const got = cc.worktreeAdds(cmd, '/r', vars || new Map(), st);
    return [got, st.unresolved];
  };
  assert.deepEqual(count('for n in $(ls); do git worktree add --detach /w/$n; done'), [[], 1]);
  assert.deepEqual(count('for n in /src/*; do git worktree add --detach /w/$n; done'), [[], 1]);
  assert.deepEqual(count('for n in {a,b}; do git worktree add --detach /w/$n; done'), [[], 1]);
  assert.deepEqual(count('for n in $LIST; do git worktree add --detach /w/$n; done'), [[], 1]);
  assert.deepEqual(count('git worktree add --detach $W'), [[], 1]);
  assert.deepEqual(count('git worktree add -b "$(mktemp -u)" /w/x'), [[], 1]);
  // A literal loop alongside an unresolved add: the first is listed, the second counted.
  assert.deepEqual(count('for n in a; do git worktree add --detach /w/$n; done && git worktree add --detach $Q'),
    [[{ path: '/w/a', branch: null }], 1]);
  // A loop over something unknown, whose variable the path does not use, still resolves.
  assert.deepEqual(count('for n in $(ls); do git worktree add --detach /w/fixed; done'), [[{ path: '/w/fixed', branch: null }], 0]);
  // Everything resolved: nothing counted.
  assert.deepEqual(count('git worktree add -b ok /w/ok')[1], 0);
  assert.deepEqual(count('git worktree add --detach $W', new Map([['W', '/w/w']])), [[{ path: '/w/w', branch: null }], 0]);
});

test('--identifiers worktrees: loop adds are listed and unresolved adds are counted in one line (210/360)', () => {
  const w = world();
  const root = repo(w);
  const lit = path.join(w.base, 'wt-loop');
  transcript(w, 'sess-id-14', [
    bashUse('l1', `for n in a b; do git worktree add --detach ${lit}-$n origin/main; done`, root), useResult('l1', 'Preparing worktree'),
    bashUse('l2', 'for n in $(ls); do git worktree add --detach /nowhere/$n origin/main; done', root), useResult('l2', 'Preparing worktree'),
    bashUse('l3', 'git worktree add --detach $NEVER_SET origin/main', root), useResult('l3', 'Preparing worktree'),
    bashUse('l4', 'git worktree add --detach $ALSO_UNSET origin/main', root), useResult('l4', '', true),
  ]);
  const j = JSON.parse(ccclose(w, root, ['--session', 'sess-id-14', '--identifiers', '--json']).out);
  assert.deepEqual(j.worktrees.items.map((x) => x.path).sort(), [`${lit}-a`, `${lit}-b`]);
  assert.equal(j.worktrees.unresolved, 2);
  const out = idRun(w, root, 'sess-id-14').out;
  const lines = out.split('\n').filter((l) => /worktree adds? not resolved/.test(l));
  assert.equal(lines.length, 1);
  assert.match(lines[0], /^ {2}- 2 worktree adds not resolved \(a variable with no literal assignment/);
  assert.doesNotMatch(out, /NEVER_SET|ALSO_UNSET|nowhere/);
});

test('--identifiers worktrees: no count line when every add resolved (210/360)', () => {
  const w = world();
  const root = repo(w);
  const good = path.join(w.base, 'wt-all-good');
  transcript(w, 'sess-id-15', [
    bashUse('g1', `for n in a b; do git worktree add --detach ${good}-$n origin/main; done`, root), useResult('g1', 'Preparing worktree'),
  ]);
  const j = JSON.parse(ccclose(w, root, ['--session', 'sess-id-15', '--identifiers', '--json']).out);
  assert.equal(j.worktrees.items.length, 2);
  assert.equal(j.worktrees.unresolved, 0);
  assert.doesNotMatch(idRun(w, root, 'sess-id-15').out, /not resolved/);
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
  assert.deepEqual(Object.keys(j.commits), ['known', 'total', 'items', 'unbroken', 'range', 'unconfirmed', 'leftOut', 'evidenceUnreadable']);
  assert.deepEqual(Object.keys(j), ['tool', 'form', 'session', 'commits', 'pullRequests', 'board', 'worktrees', 'agents', 'launched', 'otherRepos', 'touched', 'heuristic']);
  assert.equal(j.session.id, 'sess-id-15');
});

// --- --identifiers: who made the commits (210/290) -------------------------

const parseId = (w, root, sid, env = {}) => JSON.parse(ccclose(w, root, ['--session', sid, '--identifiers', '--json'], env).out);
const subjectsOf = (xs) => xs.map((x) => x.subject);
const item = (root, sec, n, text) => write(root, `docs/roadmap/${sec}-demo-section/${n}-item.md`, text);

test('commitSubjectsIn reads -m, a -m heredoc and -F - from the command, and nothing it cannot read', () => {
  const f = cc.commitSubjectsIn;
  assert.deepEqual(f('git commit -q -m "tools: add the thing"'), ['tools: add the thing']);
  assert.deepEqual(f("git -C /x commit -qm 'a: b' -m 'body line'"), ['a: b']);
  assert.deepEqual(f('git commit --message="c: d"'), ['c: d']);
  assert.deepEqual(f('git add -- x && git commit -q -m "one" && git commit -q -m "two"'), ['one', 'two']);
  assert.deepEqual(f('git commit -q -m "$(cat <<\'EOF\'\nheredoc: subject\n\nbody\n\nCo-Authored-By: T\nEOF\n)"'), ['heredoc: subject']);
  assert.deepEqual(f('git commit -q -F - <<\'EOF\'\nstdin: subject\n\nbody\nEOF'), ['stdin: subject']);
  assert.deepEqual(f('git merge --no-ff side -m "merge: side"'), ['merge: side']);
  // Unreadable forms are missed, never guessed.
  assert.deepEqual(f('git commit -q -F /tmp/msg.txt'), []);
  assert.deepEqual(f('git commit -q -m "$MSG"').length, 1);   // the variable's name, which no commit will carry
  assert.deepEqual(f('git status && git log -3'), []);
});

test('--identifiers commits: the session\'s own commit commands confirm its commits, heredocs and subagents included', () => {
  const w = world();
  const root = repo(w);
  write(root, 'a.txt', 'a'); commit(w, root, 'plain: own commit', NOW - 40 * MIN);
  write(root, 'b.txt', 'b'); commit(w, root, 'heredoc: own commit', NOW - 35 * MIN);
  write(root, 'c.txt', 'c'); commit(w, root, 'agent: made by a subagent', NOW - 30 * MIN);
  agent(w, 'sess-id-20', 'aa111111', { turns: [
    ...ranFor('g1', 'git commit -q -m "agent: made by a subagent"', 'agent: made by a subagent'),
    ...finishedTurns] });
  transcript(w, 'sess-id-20', [
    ...commitCmd('k1', 'plain: own commit'),
    ...ranFor('k2', 'git commit -q -m "$(cat <<\'EOF\'\nheredoc: own commit\n\nwhy\nEOF\n)"', 'heredoc: own commit'),
    viaAttachment('aa111111', 'completed'),
  ]);
  const j = parseId(w, root, 'sess-id-20');
  assert.deepEqual(subjectsOf(j.commits.items), ['plain: own commit', 'heredoc: own commit', 'agent: made by a subagent']);
  assert.equal(j.commits.total, 3);
  assert.equal(j.commits.unbroken, true);
  assert.equal(j.commits.unconfirmed.total, 0);
  assert.equal(j.commits.leftOut.total, 0);
  const out = idRun(w, root, 'sess-id-20').out;
  assert.match(out, /- \*\*Commits\*\* \(3\): \w+ \w+ \w+ · unbroken, `\w+\^\.\.\w+`\n  - unconfirmed, dated in the window only \(0\): none\n  - left out \(0\): none\n/);
});

// A commit message read from a file (210/310): the file must have been written
// by the session itself, at a path that resolves.
const writeUse = (id, file_path, content, cwd) => ({ type: 'assistant', cwd, message: { model: 'claude-opus-5-5', content: [{ type: 'tool_use', id, name: 'Write', input: { file_path, content } }] } });

function fileWorld(subjects) {
  const w = world();
  const root = repo(w);
  subjects.forEach(([s, min], i) => { write(root, `f${i}.txt`, String(i)); commit(w, root, s, NOW - min * MIN); });
  return { w, root };
}

test('messageFilesIn and heredocWritesIn read the file forms, and only the literal-path ones they can use', () => {
  assert.deepEqual(cc.messageFilesIn('git commit -q -F /t/m.txt').map((x) => x.word), ['/t/m.txt']);
  assert.deepEqual(cc.messageFilesIn('git commit --file=/t/m.txt').map((x) => x.word), ['/t/m.txt']);
  assert.deepEqual(cc.messageFilesIn('git -C /r commit -qF "$S/m.txt"').map((x) => [x.word, x.dir]), [['$S/m.txt', '/r']]);
  assert.deepEqual(cc.messageFilesIn('git commit -q -F - <<\'EOF\'\nx\nEOF'), []);
  assert.deepEqual(cc.messageFilesIn('git commit -q -m "a: b"'), []);
  const h = (c) => cc.heredocWritesIn(c).map((x) => [x.word, x.subject]);
  assert.deepEqual(h("cat > /t/m <<'EOF'\n\nhd: one\n\nbody\nEOF"), [['/t/m', 'hd: one']]);
  assert.deepEqual(h('cat <<EOF > /t/m\nhd: two\nEOF'), [['/t/m', 'hd: two']]);
  assert.deepEqual(h('tee /t/m <<EOF\nhd: three\nEOF'), [['/t/m', 'hd: three']]);
  // An append leaves the file's first line unknown; a non-file heredoc writes nothing.
  assert.deepEqual(h('cat >> /t/m <<EOF\nhd: four\nEOF'), []);
  assert.deepEqual(h('tee -a /t/m <<EOF\nhd: five\nEOF'), []);
  assert.deepEqual(h('git commit -q -F - <<EOF\nhd: six\nEOF'), []);
});

test('--identifiers commits: -F path is credited when the session Wrote that file, by absolute or cwd-relative path', () => {
  const { w, root } = fileWorld([['file: written with Write', 40], ['file: relative path', 35], ['peer: unrelated', 30]]);
  transcript(w, 'sess-id-30', [
    writeUse('w1', '/work/msg/one.txt', '\nfile: written with Write\n\nwhy it matters\n'),
    ...ranFor('c1', 'git commit -q -F /work/msg/one.txt', 'file: written with Write'),
    writeUse('w2', 'msg/two.txt', 'file: relative path\n', root),
    ...ranFor('c2', 'git commit -q --file=msg/two.txt', 'file: relative path'),
  ]);
  const j = parseId(w, root, 'sess-id-30');
  assert.deepEqual(subjectsOf(j.commits.items), ['file: written with Write', 'file: relative path']);
  assert.deepEqual(subjectsOf(j.commits.unconfirmed.items), ['peer: unrelated']);
});

test('--identifiers commits: -F path is credited when an earlier heredoc wrote it, and the latest write wins', () => {
  const { w, root } = fileWorld([['hd: first message', 40], ['hd: second message', 35], ['hd: tee message', 30]]);
  transcript(w, 'sess-id-31', [
    bashUse('h1', "cat > /work/m.txt <<'EOF'\nhd: stale draft\nEOF"),
    ...ranFor('h2', "cat > /work/m.txt <<'EOF'\nhd: first message\n\nbody\nEOF\ngit commit -q -F /work/m.txt", 'hd: first message'),
    bashUse('h3', 'cat <<EOF > /work/m.txt\nhd: second message\nEOF'),
    ...ranFor('c3', 'git commit -q -F /work/m.txt', 'hd: second message'),
    ...ranFor('h4', 'tee /work/t.txt <<EOF\nhd: tee message\nEOF\ngit commit -q -F /work/t.txt', 'hd: tee message'),
  ]);
  const j = parseId(w, root, 'sess-id-31');
  assert.deepEqual(subjectsOf(j.commits.items), ['hd: first message', 'hd: second message', 'hd: tee message']);
  assert.equal(j.commits.unconfirmed.total, 0);
});

test('--identifiers commits: a file written after the commit that names it does not credit it', () => {
  const { w, root } = fileWorld([['late: written after', 40]]);
  transcript(w, 'sess-id-32', [
    ...ranFor('c1', 'git commit -q -F /work/late.txt', 'late: written after'),
    writeUse('w1', '/work/late.txt', 'late: written after\n'),
  ]);
  const j = parseId(w, root, 'sess-id-32');
  assert.equal(j.commits.total, 0);
  assert.deepEqual(subjectsOf(j.commits.unconfirmed.items), ['late: written after']);
});

test('--identifiers commits: a $VAR path is credited only when the variable was assigned a literal', () => {
  const { w, root } = fileWorld([['var: assigned in the same command', 41], ['var: same line', 39], ['var: assigned earlier, braces', 35], ['var: never assigned', 30], ['var: assigned from a command', 25]]);
  transcript(w, 'sess-id-33', [
    ...ranFor('v1', "S=/work/msgs\ncat > $S/a.txt <<'EOF'\nvar: assigned in the same command\nEOF\ngit commit -q -F \"$S/a.txt\"", 'var: assigned in the same command'),
    // The assignment and the heredoc on one line, before other commands.
    ...ranFor('v1b', `cd ${root} && S=/work/msgs && cat > $S/e.txt <<'EOF'\nvar: same line\nEOF\ngit commit -q -F $S/e.txt`, 'var: same line'),
    bashUse('v2', 'export DIR=/work/other'),
    writeUse('w2', '/work/other/b.txt', 'var: assigned earlier, braces\n'),
    ...ranFor('v3', 'git commit -q -F ${DIR}/b.txt', 'var: assigned earlier, braces'),
    // Written by a heredoc under an unassigned variable, then committed from it.
    ...ranFor('v4', "cat > $NOPE/c.txt <<'EOF'\nvar: never assigned\nEOF\ngit commit -q -F $NOPE/c.txt", 'var: never assigned'),
    // Assigned from a command: not a literal, so not resolvable.
    ...ranFor('v5', "T=$(mktemp -d)\ncat > $T/d.txt <<'EOF'\nvar: assigned from a command\nEOF\ngit commit -q -F $T/d.txt", 'var: assigned from a command'),
  ]);
  const j = parseId(w, root, 'sess-id-33');
  assert.deepEqual(subjectsOf(j.commits.items), ['var: assigned in the same command', 'var: same line', 'var: assigned earlier, braces']);
  assert.deepEqual(subjectsOf(j.commits.unconfirmed.items), ['var: never assigned', 'var: assigned from a command']);
  assert.match(idRun(w, root, 'sess-id-33').out, /matched only when the session wrote that file at a path that resolves/);
});

test('--identifiers commits: a peer\'s message file is not the session\'s, even when the subject matches', () => {
  const { w, root } = fileWorld([['peer: wrote this one', 40], ['mine: wrote my own', 35]]);
  // The peer (a subagent-less other session) wrote /work/peer.txt; this session only
  // commits from it and from a basename-alike path of its own.
  transcript(w, 'sess-id-34', [
    writeUse('w1', '/work/mine/msg.txt', 'mine: wrote my own\n'),
    ...ranFor('c1', 'git commit -q -F /work/peer/msg.txt', 'peer: wrote this one'),
    ...ranFor('c2', 'git commit -q -F /work/peer.txt', 'peer: wrote this one'),
    ...ranFor('c3', 'git commit -q -F /work/mine/msg.txt', 'mine: wrote my own'),
  ]);
  const j = parseId(w, root, 'sess-id-34');
  assert.deepEqual(subjectsOf(j.commits.items), ['mine: wrote my own']);
  assert.deepEqual(subjectsOf(j.commits.unconfirmed.items), ['peer: wrote this one']);
});

test('--identifiers commits: a subagent\'s Write credits the subagent\'s -F commit, and the parent\'s unordered use of it', () => {
  const { w, root } = fileWorld([['agent: own file', 40], ['agent: parent commits it', 35]]);
  const at = (m) => new Date(NOW + m * MIN).toISOString();
  agent(w, 'sess-id-35', 'bb222222', { turns: [
    { ...writeUse('a1', '/work/a/m1.txt', 'agent: own file\n'), timestamp: at(-41) },
    ...ranFor('a2', 'git commit -q -F /work/a/m1.txt', 'agent: own file'),
    { ...writeUse('a3', '/work/a/m2.txt', 'agent: parent commits it\n'), timestamp: at(-36) },
    ...finishedTurns] });
  transcript(w, 'sess-id-35', [...ranFor('p1', 'git commit -q -F /work/a/m2.txt', 'agent: parent commits it'), viaAttachment('bb222222', 'completed')]);
  const j = parseId(w, root, 'sess-id-35');
  assert.deepEqual(subjectsOf(j.commits.items), ['agent: own file', 'agent: parent commits it']);
});

// 210/320: membership in the window is the COMMITTER date (when the session
// made the commit), never the author date a history rewrite or a backdated
// import may have set months earlier.
function commitBackdated(w, root, msg, authorWhen, committerWhen) {
  sh(w, root, ['add', '--', '.']);
  const env = { ...w.env,
    GIT_AUTHOR_DATE: new Date(authorWhen).toISOString(), GIT_COMMITTER_DATE: new Date(committerWhen).toISOString() };
  execFileSync('git', ['commit', '-q', '-m', msg], { cwd: root, env, encoding: 'utf8', stdio: ['ignore', 'pipe', 'pipe'] });
  CT.set(msg, { when: committerWhen, root });
}

test('--identifiers commits: a commit whose author date predates the window counts by its committer date (210/320)', () => {
  const w = world();
  const root = repo(w);
  write(root, 'a.txt', 'a'); commit(w, root, 'plain: ordinary', NOW - 40 * MIN);
  write(root, 'b.txt', 'b'); commitBackdated(w, root, 'history: backdated author', NOW - 90 * 24 * 60 * MIN, NOW - 35 * MIN);
  write(root, 'c.txt', 'c'); commit(w, root, 'plain: after', NOW - 30 * MIN);
  // Control: the author date really is outside the window, the committer date inside it.
  const [aT, cT] = sh(w, root, ['log', '-1', '--skip=1', '--format=%at %ct']).split(' ').map(Number);
  assert.ok(aT * 1000 < NOW - 60 * MIN && cT * 1000 > NOW - 60 * MIN);
  transcript(w, 'sess-id-22', committed('plain: ordinary', 'history: backdated author', 'plain: after'));
  const j = parseId(w, root, 'sess-id-22');
  assert.deepEqual(subjectsOf(j.commits.items), ['plain: ordinary', 'history: backdated author', 'plain: after']);
  assert.equal(j.commits.total, 3);
  assert.equal(j.commits.unbroken, true);
  assert.equal(j.commits.unconfirmed.total, 0);
  // A backdated commit no command of the session names is not lost: it is dated
  // in the window by its committer date, so it prints as unconfirmed.
  write(root, 'd.txt', 'd'); commitBackdated(w, root, 'history: scripted, no command', NOW - 80 * 24 * 60 * MIN, NOW - 25 * MIN);
  const k = parseId(w, root, 'sess-id-22');
  assert.deepEqual(subjectsOf(k.commits.unconfirmed.items), ['history: scripted, no command']);
});

test('--identifiers commits: a peer\'s commits in the window are unconfirmed, not credited, and break the range', () => {
  const w = world();
  const root = repo(w);
  write(root, 'a.txt', 'a'); commit(w, root, 'mine: first', NOW - 40 * MIN);
  write(root, 'p.txt', 'p'); commit(w, root, 'peer: on main', NOW - 38 * MIN);
  write(root, 'b.txt', 'b'); commit(w, root, 'mine: second', NOW - 36 * MIN);
  sh(w, root, ['checkout', '-q', '-b', 'peer-branch']);
  write(root, 'q.txt', 'q'); commit(w, root, 'peer: on a branch', NOW - 34 * MIN);
  sh(w, root, ['checkout', '-q', 'main']);
  transcript(w, 'sess-id-21', committed('mine: first', 'mine: second'));
  const j = parseId(w, root, 'sess-id-21');
  assert.deepEqual(subjectsOf(j.commits.items), ['mine: first', 'mine: second']);
  assert.deepEqual(subjectsOf(j.commits.unconfirmed.items).sort(), ['peer: on a branch', 'peer: on main']);
  // The peer's commit sits between the two, so first^..last would name three.
  assert.equal(j.commits.unbroken, false);
  assert.equal(j.commits.range, null);
  const out = idRun(w, root, 'sess-id-21').out;
  assert.match(out, /- \*\*Commits\*\* \(2\): \w+ \w+\n  - unconfirmed, dated in the window only \(2\): .* — no commit command of the session matches them by subject, repo, result and time; check before pasting as fact\n/);
});

test('--identifiers commits: a squash merge the session did not run is left out; one it ran is counted', () => {
  const w = world();
  const root = repo(w);
  write(root, 'a.txt', 'a'); commit(w, root, 'mine: change', NOW - 40 * MIN);
  write(root, 'b.txt', 'b'); commit(w, root, 'Add widget (#12)', NOW - 38 * MIN);
  write(root, 'c.txt', 'c'); commit(w, root, 'Add gadget (#13)', NOW - 36 * MIN);
  write(root, 'd.txt', 'd'); commit(w, root, 'Merge pull request #14 from peer/topic', NOW - 35 * MIN);
  // A "(#15)" subject off the integration line is not a merge into it.
  sh(w, root, ['checkout', '-q', '-b', 'topic']);
  write(root, 'e.txt', 'e'); commit(w, root, 'Topic work (#15)', NOW - 34 * MIN);
  sh(w, root, ['checkout', '-q', 'main']);
  sh(w, root, ['remote', 'set-url', 'origin', 'https://github.com/example/demo.git']);
  transcript(w, 'sess-id-22', [
    ...committed('mine: change'),
    bashUse('m1', 'gh pr merge 13 --squash', root), useResult('m1', 'merged'),
    bashUse('m2', 'gh pr merge 14 --squash', root), useResult('m2', 'not mergeable', true),
  ]);
  const j = parseId(w, root, 'sess-id-22', { CCCLOSE_GH: ghStub(w, { views: { 13: 'MERGED' } }) });
  assert.deepEqual(subjectsOf(j.commits.items), ['mine: change', 'Add gadget (#13)']);
  assert.deepEqual(j.commits.leftOut.items.map((x) => [x.subject, x.pr]), [['Add widget (#12)', 12], ['Merge pull request #14 from peer/topic', 14]]);
  assert.match(j.commits.leftOut.items[0].reason, /first-parent line with a PR number \(#12\); this session ran no numbered gh pr merge for it/);
  assert.deepEqual(subjectsOf(j.commits.unconfirmed.items), ['Topic work (#15)']);
  const out = idRun(w, root, 'sess-id-22').out;
  assert.match(out, /  - left out \(2\): \w+ \(PR #12: a squash merge on the first-parent line, and this session ran no numbered gh pr merge for it\), \w+ \(PR #14: a squash merge/);
  assert.match(out, /a heuristic; add by hand any that this session merged another way/);
});

test('--identifiers board: items from a peer\'s commits are unconfirmed, and a left-out squash merge is listed apart (IE14)', () => {
  const w = world();
  const root = repo(w);
  write(root, 'docs/ROADMAP.md', '<!-- GENERATED by board.py -->\n');
  item(root, '010', '010', '- [ ] **mine** filed\n');
  commit(w, root, 'board: file mine', NOW - 40 * MIN);
  item(root, '010', '020', '- [ ] **peer** filed\n');
  commit(w, root, 'board: file the peer item', NOW - 38 * MIN);
  item(root, '010', '030', '- [x] **peer merge** filed and done\n');
  commit(w, root, 'Peer feature (#30)', NOW - 36 * MIN);
  item(root, '010', '010', '- [x] **mine** done\n');
  commit(w, root, 'board: close mine', NOW - 34 * MIN);
  transcript(w, 'sess-id-23', committed('board: file mine', 'board: close mine'));
  const j = parseId(w, root, 'sess-id-23');
  assert.deepEqual(j.board.created, ['010/010']);
  assert.deepEqual(j.board.completed, ['010/010']);
  // The peer's item shows only as unconfirmed. The squash merge is the only
  // carrier of 030, so it is listed, on its own line, as coming through a merge
  // the session did not run (IE14): never as the session's own.
  assert.deepEqual(j.board.unconfirmed.created, ['010/020']);
  assert.deepEqual(j.board.unconfirmed.completed, []);
  assert.deepEqual(j.board.viaSquash.created, ['010/030']);
  const out = idRun(w, root, 'sess-id-23').out;
  assert.match(out, /  - created: 010\/010\n/);
  assert.match(out, /  - unconfirmed, from window-only commits: created 010\/020 — check before pasting as fact\n/);
  assert.match(out, /  - unconfirmed, only through a squash merge this session did not run: completed 010\/030; created 010\/030 — check before pasting as fact\n/);
});

test('--identifiers board: the ⏳ marker counts on an item\'s state line only, never in its body', () => {
  const w = world();
  const root = repo(w);
  write(root, 'docs/ROADMAP.md', '<!-- GENERATED by board.py -->\n');
  item(root, '010', '010', '- [ ] ⏳ **flagged** on the state line\n      body\n');
  item(root, '010', '020', '- [ ] **plain**\n      ⏳ only the body mentions it\n');
  item(root, '010', '030', '- [x] **closed**\n      Close note: the ⏳ pointer was taken.\n');
  item(root, '010', '040', '- [ ] **about the `⏳` glyph** in a code span\n');
  item(root, '010', '050', '- ⏳ **pointer form** with no checkbox\n');
  commit(w, root, 'board: file five items', NOW - 40 * MIN);
  // Touching a body afterwards, or adding a mention there, changes nothing.
  item(root, '010', '010', '- [~] ⏳ **flagged** on the state line\n      body\n      ⏳ again in the body\n');
  item(root, '010', '020', '- [ ] **plain**\n      ⏳ only the body mentions it\n      ⏳ a second mention\n');
  commit(w, root, 'board: touch bodies', NOW - 35 * MIN);
  transcript(w, 'sess-id-24', committed('board: file five items', 'board: touch bodies'));
  const j = parseId(w, root, 'sess-id-24');
  assert.deepEqual(j.board.review, ['010/010', '010/050']);
  assert.deepEqual(j.board.created, ['010/010', '010/020', '010/030', '010/040', '010/050']);
  assert.match(idRun(w, root, 'sess-id-24').out, /  - ⏳ review items created: 010\/010, 010\/050\n/);
});

test('board ids sort as numbers, so a four-digit pointer follows 999 (210/370)', () => {
  assert.deepEqual(['160/1000', '160/986', '010/200', '160/1010', '210/370'].sort(cc.boardOrder),
    ['010/200', '160/986', '160/1000', '160/1010', '210/370']);
});

// --- 160/960: a commit is credited only where the session's own command made it

const own = (root) => ({ cwd: root });

test('IE1/IE11: a peer\'s commit with the session\'s own subject, made at another time, is unconfirmed and breaks the range', () => {
  const w = world();
  const root = repo(w);
  write(root, 'a.txt', 'a'); commit(w, root, 'board: rebuild index', NOW - 40 * MIN);
  const mine = CT.get('board: rebuild index').when;
  write(root, 'p.txt', 'p'); commit(w, root, 'board: rebuild index', NOW - 38 * MIN);   // the peer's, same subject
  write(root, 'b.txt', 'b'); commit(w, root, 'mine: next', NOW - 36 * MIN);
  transcript(w, 'sess-ie1', [...commitCmd('k1', 'board: rebuild index', { when: mine }), ...committed('mine: next')]);
  const j = parseId(w, root, 'sess-ie1');
  assert.equal(j.commits.total, 2);
  assert.deepEqual(j.commits.unconfirmed.items.map((x) => [x.subject, x.note && /does not fit/.test(x.note)]), [['board: rebuild index', true]]);
  // The peer's commit sits between the two, so first^..last would name three.
  assert.equal(j.commits.unbroken, false);
  assert.equal(j.commits.range, null);
  assert.match(idRun(w, root, 'sess-ie1').out, /  - [0-9a-f]+: its subject matches a command of the session that does not fit \(failed, another repo, or another time\)\n/);
});

test('IE1: one command confirms at most one commit, even when two commits fall in its span with that subject', () => {
  const w = world();
  const root = repo(w);
  write(root, 'a.txt', 'a'); commit(w, root, 'board: rebuild index', NOW - 40 * MIN);
  const first = CT.get('board: rebuild index').when;
  write(root, 'p.txt', 'p'); commit(w, root, 'board: rebuild index', NOW - 40 * MIN + 1500);
  // One long-running command whose span covers both commits.
  transcript(w, 'sess-ie1b', ran('long', 'git commit -q -m "board: rebuild index"', first + 800, root));
  const j = parseId(w, root, 'sess-ie1b');
  assert.equal(j.commits.total, 1);
  assert.equal(j.commits.unconfirmed.total, 1);
});

test('IE2: a commit command that failed confirms nothing, even when a peer made a commit with its subject', () => {
  const w = world();
  const root = repo(w);
  write(root, 'p.txt', 'p'); commit(w, root, 'docs: one subject', NOW - 40 * MIN);
  transcript(w, 'sess-ie2', commitCmd('k1', 'docs: one subject', { error: true }));
  const j = parseId(w, root, 'sess-ie2');
  assert.equal(j.commits.total, 0);
  assert.deepEqual(subjectsOf(j.commits.unconfirmed.items), ['docs: one subject']);
});

test('IE3: a commit command run in another repo confirms nothing here; one run in a linked worktree of this repo does', () => {
  const w = world();
  const root = repo(w);
  const other = repo(w, 'other');
  write(root, 'a.txt', 'a'); commit(w, root, 'tools: made in this repo', NOW - 40 * MIN);
  const wt = path.join(w.base, 'wt-linked');
  sh(w, root, ['worktree', 'add', '-q', '-b', 'side', wt]);
  write(wt, 'b.txt', 'b'); commit(w, wt, 'tools: made in a worktree', NOW - 35 * MIN);
  write(root, 'c.txt', 'c'); commit(w, root, 'tools: peer, same subject as a command elsewhere', NOW - 30 * MIN);
  transcript(w, 'sess-ie3', [
    ...commitCmd('k1', 'tools: made in this repo'),
    ...commitCmd('k2', 'tools: made in a worktree', { cwd: wt }),
    // Same subject and time as the peer's commit, but run in the other repo.
    ...commitCmd('k3', 'tools: peer, same subject as a command elsewhere', { cwd: other }),
  ]);
  const j = parseId(w, root, 'sess-ie3');
  assert.deepEqual(subjectsOf(j.commits.items), ['tools: made in this repo', 'tools: made in a worktree']);
  assert.deepEqual(subjectsOf(j.commits.unconfirmed.items), ['tools: peer, same subject as a command elsewhere']);
});

test('IE3: a `git -C other commit` and a `cd other && git commit` are read as running there', () => {
  const w = world();
  const root = repo(w);
  const other = repo(w, 'other');
  write(root, 'a.txt', 'a'); commit(w, root, 'x: via -C other', NOW - 40 * MIN);
  write(root, 'b.txt', 'b'); commit(w, root, 'x: via cd other', NOW - 35 * MIN);
  write(root, 'c.txt', 'c'); commit(w, root, 'x: via -C here', NOW - 30 * MIN);
  transcript(w, 'sess-ie3b', [
    ...ranFor('k1', `git -C ${other} commit -q -m "x: via -C other"`, 'x: via -C other', own(root)),
    ...ranFor('k2', `cd ${other} && git commit -q -m "x: via cd other"`, 'x: via cd other', own(root)),
    ...ranFor('k3', `cd ${other} && git -C ${root} commit -q -m "x: via -C here"`, 'x: via -C here', own(other)),
  ]);
  const j = parseId(w, root, 'sess-ie3b');
  assert.deepEqual(subjectsOf(j.commits.items), ['x: via -C here']);
  assert.deepEqual(subjectsOf(j.commits.unconfirmed.items), ['x: via -C other', 'x: via cd other']);
});

test('IE4: commit text that runs nothing is no evidence (heredoc body, grep pattern, echo, quoted script)', () => {
  const f = cc.commitSubjectsIn;
  assert.deepEqual(f('cat > notes.md <<\'EOF\'\ngit commit -q -m "docs: quoted in a heredoc"\nEOF'), []);
  assert.deepEqual(f('grep -n \'git commit -m "docs: a grep pattern"\' notes.md'), []);
  assert.deepEqual(f('echo "git commit -q -m \'docs: an echo\'"'), []);
  assert.deepEqual(f('bash -c \'git commit -q -m "docs: wrapped in sh -c"\''), []);
  // In command position it still counts: after a line start, ;, &&, ||, a pipe, then/do.
  assert.deepEqual(f('true\ngit commit -q -m "a: new line"'), ['a: new line']);
  assert.deepEqual(f('false || git commit -q -m "a: after or"'), ['a: after or']);
  assert.deepEqual(f('if true; then git commit -q -m "a: after then"; fi'), ['a: after then']);
  assert.deepEqual(f('GIT_EDITOR=true git commit -q -m "a: env prefix"'), ['a: env prefix']);
  // A heredoc that carries the commit's own message still counts, and a later real commit too.
  assert.deepEqual(f('cat > n <<\'EOF\'\ngit commit -m "no: quoted"\nEOF\ngit commit -q -m "yes: real"'), ['yes: real']);
});

test('IE4: a heredoc that quotes a commit command does not confirm a peer\'s commit with that subject', () => {
  const w = world();
  const root = repo(w);
  write(root, 'p.txt', 'p'); commit(w, root, 'docs: example subject', NOW - 40 * MIN);
  transcript(w, 'sess-ie4', ranFor('k1', 'cat > notes.md <<\'EOF\'\ngit commit -q -m "docs: example subject"\nEOF', 'docs: example subject'));
  const j = parseId(w, root, 'sess-ie4');
  assert.equal(j.commits.total, 0);
  assert.deepEqual(subjectsOf(j.commits.unconfirmed.items), ['docs: example subject']);
});

test('IE5: a subagent\'s failed `gh pr merge` confirms nothing; its successful one does', () => {
  const w = world();
  const root = repo(w);
  write(root, 'a.txt', 'a'); commit(w, root, 'Peer work (#14)', NOW - 40 * MIN);
  write(root, 'b.txt', 'b'); commit(w, root, 'Own work (#15)', NOW - 35 * MIN);
  sh(w, root, ['remote', 'set-url', 'origin', 'https://github.com/example/demo.git']);
  agent(w, 'sess-ie5', 'cc333333', { turns: [
    { ...bashUse('m1', 'gh pr merge 14 --squash', root), timestamp: at(-41) },
    { ...useResult('m1', 'not mergeable', true), timestamp: at(-40) },
    { ...bashUse('m2', 'gh pr merge 15 --squash', root), timestamp: at(-36) },
    { ...useResult('m2', 'merged'), timestamp: at(-35) },
    ...finishedTurns] });
  transcript(w, 'sess-ie5', [viaAttachment('cc333333', 'completed')]);
  const j = parseId(w, root, 'sess-ie5');
  assert.deepEqual(subjectsOf(j.commits.items), ['Own work (#15)']);
  assert.deepEqual(j.commits.leftOut.items.map((x) => x.pr), [14]);
});

test('IE6: a squash titled like a commit the session made is unconfirmed, never left out as someone else\'s', () => {
  const w = world();
  const root = repo(w);
  write(root, 'a.txt', 'a'); commit(w, root, 'tools: add the thing', NOW - 40 * MIN);
  write(root, 'b.txt', 'b'); commit(w, root, 'tools: add the thing (#21)', NOW - 35 * MIN);   // a peer squashed the session's branch
  write(root, 'c.txt', 'c'); commit(w, root, 'peer: their own change (#22)', NOW - 30 * MIN);
  sh(w, root, ['reset', '-q', '--hard', 'HEAD']);
  // The session's own branch commit is no longer on any ref in real life; here it
  // stays, which does not matter: the squash is what is under test.
  transcript(w, 'sess-ie6', committed('tools: add the thing'));
  const j = parseId(w, root, 'sess-ie6');
  assert.deepEqual(subjectsOf(j.commits.items), ['tools: add the thing']);
  assert.deepEqual(subjectsOf(j.commits.unconfirmed.items), ['tools: add the thing (#21)']);
  assert.match(j.commits.unconfirmed.items[0].note, /squash merge of PR #21 titled like a commit of this session/);
  assert.deepEqual(subjectsOf(j.commits.leftOut.items), ['peer: their own change (#22)']);
  assert.doesNotMatch(j.commits.leftOut.items[0].reason, /merge not run by this session/);
});

test('IE7: a claim a peer\'s commit closed is not "still open", and has its own line', () => {
  const w = world();
  const root = repo(w);
  write(root, 'docs/ROADMAP.md', '<!-- GENERATED by board.py -->\n');
  item(root, '010', '010', '- [ ] **a** filed\n');
  item(root, '010', '020', '- [ ] **b** filed\n');
  commit(w, root, 'board: file a and b', NOW - 50 * MIN);
  item(root, '010', '010', '- [~] (claimed) **a**\n');
  item(root, '010', '020', '- [~] (claimed) **b**\n');
  commit(w, root, 'board: claim a and b', NOW - 45 * MIN);
  item(root, '010', '010', '- [x] **a** done\n');   // closed by a commit the session did not make
  commit(w, root, 'board: close a (the orchestrator)', NOW - 40 * MIN);
  transcript(w, 'sess-ie7', committed('board: file a and b', 'board: claim a and b'));
  const j = parseId(w, root, 'sess-ie7');
  assert.deepEqual(j.board.claimed, ['010/020']);
  assert.deepEqual(j.board.claimedMoved, ['010/010']);
  assert.deepEqual(j.board.unconfirmed.completed, ['010/010']);
  const out = idRun(w, root, 'sess-ie7').out;
  assert.match(out, /  - claimed \(still open\): 010\/020\n  - claimed, then closed or released by an unconfirmed commit: 010\/010\n/);
});

test('IE8: the block says a separately dispatched worker session\'s commits are expected to print as unconfirmed', () => {
  const { w, root } = boardWorld();
  transcript(w, 'sess-ie8');
  const out = idRun(w, root, 'sess-ie8').out;
  assert.match(out, /a worker dispatched as its own session has its own transcript, which is not read, so its commits print as unconfirmed/);
});

test('IE9: an unreadable subagent transcript is counted beside the unconfirmed line, not swallowed', () => {
  const w = world();
  const root = repo(w);
  write(root, 'a.txt', 'a'); commit(w, root, 'agent: lost with its transcript', NOW - 40 * MIN);
  // A directory where the transcript file should be: reading it fails (EISDIR).
  const dir = path.join(w.home, '.claude', 'projects', 'proj', 'sess-ie9', 'subagents');
  fs.mkdirSync(path.join(dir, 'agent-dd444444.jsonl'), { recursive: true });
  transcript(w, 'sess-ie9');
  const j = parseId(w, root, 'sess-ie9');
  assert.equal(j.commits.evidenceUnreadable, 1);
  assert.match(idRun(w, root, 'sess-ie9').out, /  - evidence incomplete: 1 subagent transcript\(s\) could not be read/);
});

test('IE10: a message\'s first paragraph is folded as git folds it; a quoted -C path with spaces is read', () => {
  const f = cc.commitSubjectsIn;
  assert.deepEqual(f('git commit -q -m "tools: a long subject\nthat git folds\n\nbody here"'), ['tools: a long subject that git folds']);
  assert.deepEqual(f('git commit -q -m "$(cat <<\'EOF\'\ntools: folded\nin a heredoc\n\nbody\nEOF\n)"'), ['tools: folded in a heredoc']);
  const w = world();
  const base = path.join(w.base, 'a dir with spaces');
  fs.mkdirSync(base);
  const root = repo(w, 'a dir with spaces/repo');
  assert.ok(root.includes(' '));
  write(root, 'a.txt', 'a'); commit(w, root, 'x: in a path with spaces', NOW - 40 * MIN);
  transcript(w, 'sess-ie10', ranFor('k1', `git -C "${root}" commit -q -m "x: in a path with spaces"`, 'x: in a path with spaces', { cwd: w.base }));
  assert.deepEqual(subjectsOf(parseId(w, root, 'sess-ie10').commits.items), ['x: in a path with spaces']);
});

test('a rebase, a pull --rebase or a message-less amend rewrites the session\'s own commits: the copies are confirmed; a peer\'s are not', () => {
  const w = world();
  const root = repo(w);
  write(root, 'a.txt', 'a'); commit(w, root, 'mine: first', NOW - 40 * MIN);
  const t1 = CT.get('mine: first').when;
  write(root, 'p.txt', 'p'); commit(w, root, 'peer: untouched', NOW - 25 * MIN);
  // The rebase (at NOW - 20 min) re-commits 'mine: first' as a new commit.
  write(root, 'c.txt', 'c'); commit(w, root, 'mine: first', NOW - 20 * MIN);
  const t2 = NOW - 20 * MIN;
  transcript(w, 'sess-rb', [
    ...commitCmd('k1', 'mine: first', { when: t1, cwd: root }),
    ...ran('rb', 'git rebase origin/main', t2, root),
  ]);
  const j = parseId(w, root, 'sess-rb');
  assert.deepEqual(j.commits.items.map((x) => x.subject), ['mine: first', 'mine: first']);
  assert.deepEqual(subjectsOf(j.commits.unconfirmed.items), ['peer: untouched']);
  // Without the rebase command the second copy is unconfirmed.
  transcript(w, 'sess-rb2', commitCmd('k1', 'mine: first', { when: t1, cwd: root }));
  const k = parseId(w, root, 'sess-rb2');
  assert.equal(k.commits.total, 1);
});

test('a commit command with no end (a record cut before its result) confirms nothing', () => {
  const w = world();
  const root = repo(w);
  write(root, 'a.txt', 'a'); commit(w, root, 'cut: no result', NOW - 40 * MIN);
  transcript(w, 'sess-cut', [{ ...bashUse('k1', 'git commit -q -m "cut: no result"', root), timestamp: iso(NOW - 40 * MIN - 500) }]);
  const j = parseId(w, root, 'sess-cut');
  assert.equal(j.commits.total, 0);
  assert.equal(j.commits.unconfirmed.total, 1);
});

test('commitCommandsIn marks a rebase, a pull --rebase and a message-less amend as rewrites, and a plain pull as nothing', () => {
  const k = (c) => cc.commitCommandsIn(c, '/r').map((x) => [x.sub, x.rewrite, x.subject, x.dir]);
  assert.deepEqual(k('git rebase origin/main'), [['rebase', true, null, '/r']]);
  assert.deepEqual(k('git pull --rebase'), [['pull', true, null, '/r']]);
  assert.deepEqual(k('git pull'), []);
  assert.deepEqual(k('git commit --amend --no-edit'), [['commit', true, null, '/r']]);
  assert.deepEqual(k('git commit --amend -m "a: new"'), [['commit', false, 'a: new', '/r']]);
  assert.deepEqual(k('cd /elsewhere && git commit -q -m "a: b"'), [['commit', false, 'a: b', '/elsewhere']]);
  assert.deepEqual(k('git -C sub commit -q -m "a: b"'), [['commit', false, 'a: b', '/r/sub']]);
  assert.deepEqual(k('git -C "$D" commit -q -m "a: b"'), [['commit', false, 'a: b', null]]);
});


// --- check 14: the atelier pin and floor copy (020/470) ---------------------
//
// Synthetic only: a throwaway "atelier" (a git repo with a local bare origin,
// atelier's own pins.py and its helpers copied in, and a PROPAGATION.md with a
// floor region) and a throwaway child stamped with that floor. Nothing here
// reads a real sibling repo or the network. $CCCLOSE_ATELIER points the check at
// the fixture; the pins.py that runs is the repo's real one.

const TOOLS = path.join(__dirname, '..', 'tools');
const PINS_FILES = ['pins.py', 'estate.py', 'stampscan.py', 'filewalk.py', 'allowmarker.py', 'report.py'];
const FLOOR = [
  '## Doctrine — inherited from atelier (pinned `atelier@<SHA>`)',
  '',
  '- **Rule one:** keep the safety rule verbatim.',
  '- **Source & drift:** canonical doctrine is `<atelier-path>/docs/method/`.',
  '- **This repo\'s visibility:** <visibility fact>.',
];
const propagation = (region) => `# PROPAGATION\n\nprose\n\n<!-- floor:begin -->\n\`\`\`markdown\n${region.join('\n')}\n\`\`\`\n<!-- floor:end -->\n\ntail\n`;
const filledFloor = (region, sha) => region.join('\n').replace('<SHA>', sha.slice(0, 7))
  .replace('<atelier-path>', '../atelier').replace('<visibility fact>', 'PRIVATE by design');
const stampedClaude = (body) => `# child\n\n<!-- stamp:begin source=docs/method/PROPAGATION.md region=floor -->\n${body}\n<!-- stamp:end -->\n`;

// An atelier fixture with one commit holding FLOOR; returns { dir, sha }.
function atelierFixture(w, name = 'atelier') {
  const dir = path.join(w.base, name);
  const bare = path.join(w.base, `${name}.git`);
  fs.mkdirSync(path.join(dir, 'tools'), { recursive: true });
  for (const f of PINS_FILES) fs.copyFileSync(path.join(TOOLS, f), path.join(dir, 'tools', f));
  write(dir, 'docs/method/PROPAGATION.md', propagation(FLOOR));
  sh(w, w.base, ['init', '-q', '--bare', '-b', 'main', bare]);
  sh(w, dir, ['init', '-q', '-b', 'main']);
  sh(w, dir, ['remote', 'add', 'origin', bare]);
  commit(w, dir, 'floor v1', NOW - 3 * 24 * 60 * MIN);
  sh(w, dir, ['push', '-q', '-u', 'origin', 'main']);
  return { dir, bare, sha: sh(w, dir, ['rev-parse', 'HEAD']) };
}
// A child pinned at `sha`, its floor copy `body`.
function childFixture(w, sha, body, name = 'child') {
  const root = repo(w, name);
  write(root, 'CLAUDE.md', stampedClaude(body));
  commit(w, root, 'claude', NOW - 3 * 24 * 60 * MIN + MIN);
  return root;
}
const pinEnv = (a, extra = {}) => ({ CCCLOSE_ATELIER: a.dir, ...extra });
const pinCheck = (w, root, a, extra) => json(w, root, [], pinEnv(a, extra));

test('check 14: a current pin with an identical floor copy passes, and says so', () => {
  const w = world();
  const a = atelierFixture(w);
  const root = childFixture(w, a.sha, filledFloor(FLOOR, a.sha));
  const j = pinCheck(w, root, a);
  assert.equal(j.by.pin.status, 'pass', j.by.pin.summary);
  assert.match(j.by.pin.summary, new RegExp(`pin ${a.sha.slice(0, 7)} is current with origin/main; floor copy identical`));
  assert.equal(j.by.pin.label, 'Atelier pin and floor copy current');
});

// Two commits on atelier's mainline that leave the floor region alone.
function advanceUnrelated(w, a) {
  write(a.dir, 'docs/method/other.md', 'x\n');
  commit(w, a.dir, 'unrelated change one', NOW - 2 * 24 * 60 * MIN);
  write(a.dir, 'docs/method/other.md', 'y\n');
  commit(w, a.dir, 'unrelated change two', NOW - 24 * 60 * MIN);
  sh(w, a.dir, ['push', '-q', 'origin', 'main']);
}

test('check 14: a pin behind with the floor unchanged only warns, with the commits listed, and exits 0', () => {
  const w = world();
  const a = atelierFixture(w);
  const root = childFixture(w, a.sha, filledFloor(FLOOR, a.sha));
  advanceUnrelated(w, a);
  const j = pinCheck(w, root, a);
  assert.equal(j.by.pin.status, 'warn', j.by.pin.summary);
  assert.match(j.by.pin.summary, new RegExp(`pin ${a.sha.slice(0, 7)} is 2 commit\\(s\\) behind origin/main; floor unchanged since the pin; read the delta when convenient`));
  assert.ok(j.by.pin.items.some((l) => /unrelated change two/.test(l)), 'lists the commits the child would inspect');
  assert.doesNotMatch(j.by.pin.summary, /current with/);
  assert.equal(j.code, 0);
  assert.match(ccclose(w, root, [], pinEnv(a)).out, /⚠️ Atelier pin and floor copy current +pin [0-9a-f]{7} is 2 commit/);
});

test('check 14: a pin behind AND the floor changed since the pin fails, and exits non-zero', () => {
  const w = world();
  const a = atelierFixture(w);
  const root = childFixture(w, a.sha, filledFloor(FLOOR, a.sha));
  advanceUnrelated(w, a);
  const moved = FLOOR.map((l) => l.replace('verbatim', 'verbatim, always'));
  write(a.dir, 'docs/method/PROPAGATION.md', propagation(moved));
  commit(w, a.dir, 'floor v2', NOW - 60 * MIN);
  sh(w, a.dir, ['push', '-q', 'origin', 'main']);
  const j = pinCheck(w, root, a);
  assert.equal(j.by.pin.status, 'fail', j.by.pin.summary);
  assert.match(j.by.pin.summary, /is 3 commit\(s\) behind origin\/main, and the safety floor has changed since the pin: read the delta and bump the pin to pick it up/);
  assert.doesNotMatch(j.by.pin.summary, /differs/, 'the copy still matches the floor at ITS pin');
  assert.equal(j.code, 1);
  assert.match(ccclose(w, root, [], pinEnv(a)).out, /❌ Atelier pin and floor copy current +pin [0-9a-f]{7} is 3 commit/);
});

test('check 14: it measures the published mainline, so a local-only atelier commit is not drift', () => {
  const w = world();
  const a = atelierFixture(w);
  const root = childFixture(w, a.sha, filledFloor(FLOOR, a.sha));
  write(a.dir, 'docs/method/other.md', 'unpushed\n');
  commit(w, a.dir, 'not yet pushed', NOW - 60 * MIN);
  assert.equal(pinCheck(w, root, a).by.pin.status, 'pass');
});

test('check 14: a floor copy that differs from atelier\'s floor fails even with a current pin', () => {
  const w = world();
  const a = atelierFixture(w);
  const drifted = filledFloor(FLOOR, a.sha).replace('keep the safety rule verbatim', 'keep the safety rule, roughly');
  const root = childFixture(w, a.sha, drifted);
  const j = pinCheck(w, root, a);
  assert.equal(j.by.pin.status, 'fail', j.by.pin.summary);
  assert.match(j.by.pin.summary, /floor copy differs from atelier's floor at the pin/);
  assert.doesNotMatch(j.by.pin.summary, /stale/);
  assert.equal(j.code, 1);
});

test('check 14: a pin that is not a commit atelier knows fails, naming the checkout', () => {
  const w = world();
  const a = atelierFixture(w);
  const root = childFixture(w, a.sha, filledFloor(FLOOR, 'abcdef0123456789'));
  const j = pinCheck(w, root, a);
  assert.equal(j.by.pin.status, 'fail', j.by.pin.summary);
  assert.match(j.by.pin.summary, /pin abcdef0 is not a commit in the atelier checkout/);
});

test('check 14: atelier itself, and a repo that pins nothing, are not children and do not fail', () => {
  const w = world();
  const a = atelierFixture(w);
  const own = json(w, a.dir, [], pinEnv(a));
  assert.equal(own.by.pin.status, 'na');
  assert.match(own.by.pin.summary, /^not a child — this is atelier itself/);
  const plain = repo(w, 'plain');
  write(plain, 'CLAUDE.md', '# plain\n\nno pin here\n');
  commit(w, plain, 'claude', NOW - 3 * 24 * 60 * MIN + MIN);
  const p = json(w, plain, [], pinEnv(a));
  assert.equal(p.by.pin.status, 'na');
  assert.match(p.by.pin.summary, /^not a child — CLAUDE\.md carries no atelier pin or floor stamp/);
  assert.equal(p.code, 0);
});

test('check 14: no atelier checkout is "no result" with the reason, never "current"', () => {
  const w = world();
  const a = atelierFixture(w);
  const root = childFixture(w, a.sha, filledFloor(FLOOR, a.sha));
  const j = json(w, root, [], { CCCLOSE_ATELIER: path.join(w.base, 'nowhere') });
  assert.equal(j.by.pin.status, 'warn');
  assert.match(j.by.pin.summary, /^no result — \$CCCLOSE_ATELIER \(.*nowhere\) has no tools\/pins\.py/);
  assert.doesNotMatch(j.by.pin.summary, /current/);
  assert.equal(j.code, 0);    // unknown is a look, not a verdict of drift
  assert.equal(j.verdict.status, 'warn');
});

test('check 14: a failed fetch is "no result" with pins.py\'s own reason, never "current"', () => {
  const w = world();
  const a = atelierFixture(w);
  const root = childFixture(w, a.sha, filledFloor(FLOOR, a.sha));
  sh(w, a.dir, ['remote', 'set-url', 'origin', path.join(w.base, 'gone.git')]);
  const j = pinCheck(w, root, a);
  assert.equal(j.by.pin.status, 'warn', j.by.pin.summary);
  assert.match(j.by.pin.summary, /^no result — pins\.py exited 2: .*could not fetch origin/);
  assert.doesNotMatch(j.by.pin.summary, /current with/);
});

// A fixture atelier whose pins.py is a stand-in script: the check's handling of
// a hang and of unreadable output, without depending on how the real one fails.
function standInPins(w, body, name = 'atelier-standin') {
  const a = atelierFixture(w, name);
  fs.writeFileSync(path.join(a.dir, 'tools', 'pins.py'), body);
  return a;
}

test('check 14: a pins.py that outruns the time limit is "no result", not a hang or a pass', () => {
  const w = world();
  const a = standInPins(w, 'import time\ntime.sleep(30)\n');
  const root = childFixture(w, a.sha, filledFloor(FLOOR, a.sha));
  const t0 = Date.now();
  const j = pinCheck(w, root, a, { CCCLOSE_PINS_TIMEOUT: '1' });
  assert.ok(Date.now() - t0 < 15000, 'the limit is enforced');
  assert.equal(j.by.pin.status, 'warn');
  assert.match(j.by.pin.summary, /^no result — pins\.py did not finish within 1 s/);
});

test('check 14: output that does not parse, or a status ccclose does not know, is "no result"', () => {
  const w = world();
  const a = standInPins(w, 'print("all is well")\n');
  const root = childFixture(w, a.sha, filledFloor(FLOOR, a.sha));
  const j = pinCheck(w, root, a);
  assert.equal(j.by.pin.status, 'warn');
  assert.match(j.by.pin.summary, /^no result — pins\.py printed nothing readable/);
  const b = standInPins(w, 'import json\nprint(json.dumps({"children":[{"name":"child","status":"fresh-as-a-daisy","copy":"identical"}]}))\n', 'atelier-standin-b');
  const k = pinCheck(w, root, b);
  assert.equal(k.by.pin.status, 'warn');
  assert.match(k.by.pin.summary, /^no result — pins\.py reported a status ccclose does not know/);
});

test('check 14: the checkout this script lives in is used when nothing names one', () => {
  const w = world();
  const root = childFixture(w, 'abcdef0123456789', filledFloor(FLOOR, 'abcdef0123456789'));
  const at = cc.locateAtelier({ commonDir: path.join(root, '.git'), root }, { ATELIER_ESTATE_ROOT: path.join(w.base, 'estate-root') });
  // This test file runs from atelier or one of its worktrees, so the first
  // candidate is its main checkout: it carries tools/pins.py.
  assert.ok(at.dir && fs.existsSync(path.join(at.dir, 'tools', 'pins.py')), JSON.stringify(at));
});

// --- check 15: launched work finished (210/460) -----------------------------
//
// The process table is a fixture: <base>/ps.txt, printed by the CCCLOSE_PS stub
// that world() installs. A line is `pid ppid etime argv... ENV=...`, as
// `ps -Eww -axo pid=,ppid=,etime=,command=` prints it.

const psLines = (w, lines) => fs.writeFileSync(path.join(w.base, 'ps.txt'), lines.join('\n') + '\n');
const carrying = (sid, harness = 900) => `CLAUDE_CODE_SESSION_ID=${sid} CLAUDE_PID=${harness} HOME=/h`;
const proc = (pid, ppid, etime, argv, sid, harness) => `${pid} ${ppid} ${etime} ${argv} ${carrying(sid, harness)}`;
const useOf = (id, name, input, extra = {}) => ({ type: 'assistant', cwd: '/x', message: { model: 'claude-opus-5-5', content: [{ type: 'tool_use', id, name, input }] }, ...extra });
const resultOf = (id, text, tur, isError = false) => ({ type: 'user', message: { role: 'user', content: [{ type: 'tool_result', tool_use_id: id, content: text, is_error: isError }] }, toolUseResult: tur || { stdout: text } });
const bgRun = (id, command, taskId, over = {}) => [
  useOf(id, 'Bash', { command, run_in_background: true }),
  resultOf(id, `Command running in background with ID: ${taskId}. Output is being written to: /x/${taskId}.output.`, { backgroundTaskId: taskId, ...over }),
];
const lw = (j) => j.by.launched;

test('check 15 is the last of fifteen, with every count printed and zeros included', () => {
  const w = world();
  const root = repo(w);
  transcript(w, 'sess-l0');
  const j = json(w, root, ['--session', 'sess-l0']);
  assert.equal(j.checks[j.checks.length - 1].id, 'launched');
  assert.equal(lw(j).label, 'Launched work finished');
  assert.equal(lw(j).status, 'pass');
  assert.deepEqual(lw(j).counts, { processes: 0, background: 0, launches: 0, harness: 0, scheduled: 0, ended: 0, excluded: 0 });
  assert.match(lw(j).summary, /^0 live process\(es\) · 0 background command\(s\) not ended · 0 detached launch\(es\) not shown finished · 0 harness-started item\(s\) not ended · 0 schedule\(s\) pending · 0 ended or stopped · 0 harness\/own process\(es\) excluded$/);
  assert.deepEqual(Object.keys(lw(j).legs), ['processes', 'background', 'launches', 'harness']);
  assert.equal(lw(j).allItems, undefined, 'the uncapped list stays out of --json');
});

test('check 15 leg 1: a process carrying the session id blocks, printed by pid, age and a few words of argv, never whole', () => {
  const w = world();
  const root = repo(w);
  transcript(w, 'sess-l1');
  psLines(w, [
    proc(4321, 1, '01:02:03', '/opt/venv/bin/python3 worker.py --token=SECRETVALUE --mode fast extra-arg-after-limit', 'sess-l1'),
    proc(4400, 1, '00:30', '/bin/other thing', 'another-session'),
  ]);
  const j = json(w, root, ['--session', 'sess-l1']);
  assert.equal(lw(j).status, 'fail');
  assert.equal(lw(j).counts.processes, 1);
  assert.match(lw(j).items[0], /^❌ live process: pid 4321 · 62m · python3 worker\.py --token=…/);
  const text = JSON.stringify(j);
  assert.doesNotMatch(text, /SECRETVALUE|extra-arg-after-limit|HOME=/, 'the command line is never printed whole');
  assert.equal(j.code, 1);
  assert.match(ccclose(w, root, ['--session', 'sess-l1']).out, /❌ Launched work finished +1 live process\(es\)/);
});

test('check 15 leg 1: the harness, its early MCP servers and its MCP-named helpers are not flagged; a later helper is', () => {
  const w = world();
  const root = repo(w);
  transcript(w, 'sess-l2');   // the first prompt is 60 minutes back
  psLines(w, [
    proc(900, 1, '03:00:00', '/usr/local/bin/claude', 'sess-l2'),                     // the harness itself
    proc(901, 900, '02:59:50', 'node /srv/some-server/dist/index.js', 'sess-l2'),     // started before the first prompt
    proc(902, 900, '00:10:00', 'npx -y @modelcontextprotocol/server-x', 'sess-l2'),   // started later, named as MCP
    proc(903, 900, '00:10:00', '/bin/zsh -c sleep 600', 'sess-l2'),                   // a shell the session started: blocks
  ]);
  const j = json(w, root, ['--session', 'sess-l2']);
  assert.equal(lw(j).counts.processes, 1);
  assert.equal(lw(j).counts.excluded, 3);
  assert.match(lw(j).items[0], /pid 903 · 10m · zsh -c sleep/);
});

test('check 15 leg 1: ccclose\'s own chain (itself, its ancestors, its children) is excluded', () => {
  const sid = 'sess-own';
  const table = new Map([
    [900, { pid: 900, ppid: 1, ageSec: 7200, rest: `/usr/local/bin/claude ${carrying(sid)}` }],
    [910, { pid: 910, ppid: 900, ageSec: 5, rest: `/bin/zsh -c node ccclose ${carrying(sid)}` }],
    [process.pid, { pid: process.pid, ppid: 910, ageSec: 4, rest: `node ccclose ${carrying(sid)}` }],
    [7777, { pid: 7777, ppid: process.pid, ageSec: 1, rest: `ps -Eww ${carrying(sid)}` }],
    [8888, { pid: 8888, ppid: 900, ageSec: 3000, rest: `sleep 999 ${carrying(sid)}` }],
  ]);
  const live = cc.checkLaunched(null, sid, { ok: true, table }, NOW);
  assert.equal(live.counts.processes, 1);
  assert.match(live.items[0], /pid 8888/);
  assert.equal(live.counts.excluded, 4);
});

test('check 15 leg 1: an unreadable process table is unknown, never a pass', () => {
  const w = world();
  const root = repo(w);
  transcript(w, 'sess-l3');
  const j = json(w, root, ['--session', 'sess-l3'], { CCCLOSE_PS: path.join(w.base, 'no-such-ps') });
  assert.equal(lw(j).status, 'warn');
  assert.match(lw(j).summary, /unknown: process table not read \(ps could not run/);
  assert.equal(j.code, 0);
  // With no transcript the other legs are unread, and the line says so.
  const k = json(w, root, ['--session', 'no-such-session']);
  assert.equal(lw(k).status, 'warn');
  assert.match(lw(k).summary, /unknown: no transcript/);
});

test('check 15 is not applicable with no session at all', () => {
  const w = world();
  const root = repo(w);
  const j = json(w, root, [], { CLAUDE_CODE_SESSION_ID: '' });
  assert.equal(lw(j).status, 'na');
});

test('check 15 leg 2: a background command blocks until a terminal notification, or a stop, ends it', () => {
  const w = world();
  const root = repo(w);
  transcript(w, 'sess-l4', [
    ...bgRun('b1', 'make build', 'task1'),
    viaAttachment('task1', 'completed'),
    ...bgRun('b2', 'make slow', 'task2'),
    viaAttachment('task2', 'killed'),
    ...bgRun('b3', 'make forever', 'task3'),
    ...bgRun('b4', 'make stopped-by-me', 'task4'),
    useOf('s4', 'TaskStop', { task_id: 'task4' }), resultOf('s4', 'Successfully stopped task: task4', { task_id: 'task4' }),
    ...bgRun('b5', 'make failed', 'task5'),
    viaAttachment('task5', 'failed'),
    // A launch whose call failed started nothing; one with no task id cannot be matched.
    useOf('b6', 'Bash', { command: 'make never', run_in_background: true }), resultOf('b6', 'bad', { stdout: 'bad' }, true),
    useOf('b7', 'Bash', { command: 'make idless', run_in_background: true }), resultOf('b7', 'started', { stdout: '' }),
  ]);
  const j = json(w, root, ['--session', 'sess-l4']);
  assert.equal(lw(j).status, 'fail');
  assert.equal(lw(j).counts.background, 2);
  assert.equal(lw(j).counts.ended, 4);
  const lines = lw(j).items.filter((x) => x.startsWith('❌'));
  assert.equal(lines.length, 2);
  assert.ok(lines.some((x) => /make forever — task task3: no terminal notification/.test(x)));
  assert.ok(lines.some((x) => /make idless — no task id in its result/.test(x)));
  assert.ok(lw(j).items.some((x) => /make stopped-by-me — stopped \(TaskStop\)/.test(x)));
  assert.equal(lw(j).legs.background.length, 6);
});

test('check 15 leg 3: a command that lets go of work blocks, named by its command, unless shown finished', () => {
  const w = world();
  const root = repo(w);
  const run = (id, command, text = '', over = {}) => [useOf(id, 'Bash', { command }), resultOf(id, text, { stdout: text }, !!over.error)];
  transcript(w, 'sess-l5', [
    ...run('c1', 'nohup python3 serve.py > serve.log 2>&1 &'),
    ...run('c2', 'sleep 5 & wait'),
    ...run('c3', 'tmux new-session -d -s w "claude -p hi"'),
    ...run('c4', 'launchctl load ~/Library/LaunchAgents/x.plist'),
    ...run('c5', 'launchctl unload ~/Library/LaunchAgents/x.plist'),
    ...run('c6', 'git log --oneline'),
    ...run('c7', 'echo "nohup is only a word here" && ls'),
    ...run('c8', 'claude -p "a foreground run"'),
    ...run('c9', 'nohup failing-thing &', '', { error: true }),
    ...run('c10', 'setsid claude -p "go" > run.log 2>&1 < /dev/null & disown'),
  ]);
  const j = json(w, root, ['--session', 'sess-l5']);
  assert.equal(lw(j).status, 'fail');
  const bad = lw(j).items.filter((x) => x.startsWith('❌'));
  assert.equal(bad.length, 3, bad.join('\n'));
  assert.equal(lw(j).counts.launches, 3);
  assert.ok(bad.some((x) => /nohup python3 serve\.py.* — & \+ nohup: the command let go of it and nothing shows it finished/.test(x)));
  assert.ok(bad.some((x) => /tmux new-session -d -s w "claude -p hi" — tmux:/.test(x)));
  assert.ok(bad.some((x) => /setsid claude -p "go".* — & \+ setsid \+ disown \+ headless claude:/.test(x)));
  // Awaited in the same command, and launchctl removed by a later command: not blockers.
  assert.ok(lw(j).items.some((x) => /sleep 5 & wait — the command waited/.test(x)));
  assert.ok(lw(j).items.some((x) => /launchctl load .* — launchctl removed by a later command/.test(x)));
});

test('check 15 leg 3: a pid the command printed is read against the process table, alive or gone', () => {
  const w = world();
  const root = repo(w);
  const run = (id, command, text) => [useOf(id, 'Bash', { command }), resultOf(id, text, { stdout: text })];
  transcript(w, 'sess-l6', [
    ...run('p1', 'sleep 900 > /dev/null 2>&1 & echo $!', '31337\n'),
    ...run('p2', 'sleep 1 > /dev/null 2>&1 & echo $!', '31338\n'),
    // A bare number with no $! asked for is a count, not a pid: unproven, not gone.
    ...run('p3', 'sleep 3 & wc -l /etc/hosts', '31339\n'),
  ]);
  // sleep is an Apple platform binary: ps -E shows no environment, yet its pid is in the table.
  psLines(w, ['31337 1 05:00 sleep 900', '31339 1 00:10 sleep 3']);
  const j = json(w, root, ['--session', 'sess-l6']);
  const bad = lw(j).items.filter((x) => x.startsWith('❌'));
  assert.equal(bad.length, 2, bad.join('\n'));
  assert.ok(bad.some((x) => /sleep 900.* — pid 31337 is still alive \(5m, sleep 900\)/.test(x)));
  assert.ok(bad.some((x) => /sleep 3 & wc -l.* — &: the command let go of it/.test(x)));
  assert.ok(lw(j).items.some((x) => /sleep 1 .* — pid 31338 is gone/.test(x)));
  assert.equal(lw(j).counts.launches, 2);
});

test('check 15 leg 3: a launch a live process already accounts for is counted once, in leg 1', () => {
  const w = world();
  const root = repo(w);
  transcript(w, 'sess-l7', [useOf('d1', 'Bash', { command: 'nohup python3 /w/crawler.py > c.log 2>&1 &' }), resultOf('d1', '', { stdout: '' })]);
  psLines(w, [proc(5150, 1, '00:20:00', 'python3 /w/crawler.py', 'sess-l7')]);
  const j = json(w, root, ['--session', 'sess-l7']);
  assert.equal(lw(j).counts.processes, 1);
  assert.equal(lw(j).counts.launches, 0);
  assert.equal(lw(j).itemsTotal, 1);
});

test('check 15 leg 4: harness tools that start work elsewhere are listed; unfinished ones block, schedules warn', () => {
  const w = world();
  const root = repo(w);
  const MS = NOW;
  transcript(w, 'sess-l8', [
    useOf('h1', 'Monitor', { command: 'tail -f build.log' }), resultOf('h1', 'Monitor started (task mon1, expires in 30m unless the source ends first).', { taskId: 'mon1', timeoutMs: 1800000, persistent: false }),
    useOf('h2', 'Monitor', { command: 'watch done' }), resultOf('h2', 'Monitor started (task mon2, expires in 30m).', { taskId: 'mon2', timeoutMs: 1800000, persistent: false }),
    viaAttachment('mon2', 'completed'),
    useOf('h3', 'Workflow', { workflow: 'big-job' }), resultOf('h3', 'Workflow launched.', { stdout: '' }),
    useOf('h4', 'RemoteTrigger', { action: 'run', trigger_id: 'trig_x' }), resultOf('h4', 'HTTP 200', { status: 200 }),
    useOf('h5', 'RemoteTrigger', { action: 'get', trigger_id: 'trig_x' }), resultOf('h5', 'HTTP 200', { status: 200 }),
    useOf('h6', 'CronCreate', { cron: '*/5 * * * *', prompt: 'x' }), resultOf('h6', 'Scheduled recurring job cron1.', { id: 'cron1', durable: false }),
    useOf('h7', 'CronCreate', { cron: '0 9 * * *', prompt: 'x' }), resultOf('h7', 'Scheduled recurring job cron2.', { id: 'cron2', durable: true }),
    useOf('h8', 'CronDelete', { id: 'cron2' }), resultOf('h8', 'Cancelled job cron2.', { id: 'cron2' }),
    useOf('h9', 'ScheduleWakeup', { delaySeconds: 60, reason: 'r', prompt: 'p' }), resultOf('h9', 'Next wakeup scheduled', { scheduledFor: MS - 5 * MIN }),
    useOf('h10', 'ScheduleWakeup', { delaySeconds: 1800, reason: 'r', prompt: 'p' }), resultOf('h10', 'Next wakeup scheduled', { scheduledFor: MS + 30 * MIN }),
  ]);
  const j = json(w, root, ['--session', 'sess-l8']);
  assert.equal(lw(j).status, 'fail');
  // Monitor mon1 (no notice, 30 min not yet elapsed from its call 20 min back), Workflow, RemoteTrigger run: three blockers.
  assert.equal(lw(j).counts.harness, 3);
  assert.equal(lw(j).counts.scheduled, 2);      // cron1 (session-only) and the pending wakeup
  assert.equal(lw(j).counts.ended, 3);          // mon2 notified, cron2 deleted, the fired wakeup
  const text = lw(j).items.join('\n');
  assert.match(text, /❌ harness: .* Monitor tail -f build\.log — task mon1: no terminal notification/);
  assert.match(text, /❌ harness: .* Workflow big-job — no task id in its result/);
  assert.match(text, /❌ harness: .* RemoteTrigger run — no task id/);
  assert.match(text, /⚠️ harness: .* cron \*\/5 \* \* \* \* — a schedule \(session-only: it ends with the session\)/);
  assert.match(text, /✅ harness: .* wakeup in 60s — the wakeup has fired/);
  assert.doesNotMatch(text, /RemoteTrigger get/);
});

test('check 15 leg 4: a Monitor past its time limit has ended; only schedules left: warn, exit 0', () => {
  const w = world();
  const root = repo(w);
  transcript(w, 'sess-l9', [
    { ...useOf('m1', 'Monitor', { command: 'old watch' }), timestamp: at(-50) },
    { ...resultOf('m1', 'Monitor started (task monx).', { taskId: 'monx', timeoutMs: 600000, persistent: false }), timestamp: at(-50) },
    useOf('w1', 'ScheduleWakeup', { delaySeconds: 1800 }), resultOf('w1', 'Next wakeup', { scheduledFor: NOW + 30 * MIN }),
  ]);
  const j = json(w, root, ['--session', 'sess-l9']);
  assert.equal(lw(j).status, 'warn');
  assert.equal(lw(j).counts.harness, 0);
  assert.equal(j.code, 0);
  assert.equal(j.verdict.status, 'warn');
});

test('check 15: the list is capped and the cut counted; --json carries counts and the capped legs', () => {
  const w = world();
  const root = repo(w);
  const recs = [];
  for (let i = 0; i < cc.CAP + 5; i++) recs.push(...bgRun(`bg${i}`, `job ${i}`, `tid${i}`));
  transcript(w, 'sess-l10', recs);
  const j = json(w, root, ['--session', 'sess-l10']);
  assert.equal(lw(j).counts.background, cc.CAP + 5);
  assert.equal(lw(j).items.length, cc.CAP);
  assert.equal(lw(j).itemsTotal, cc.CAP + 5);
  assert.equal(lw(j).legs.background.length, cc.CAP);
  assert.match(ccclose(w, root, ['--session', 'sess-l10']).out, /… and 5 more/);
});

test('check 15 reads a PAST session\'s id too: --session names the transcript, and its processes are looked for', () => {
  const w = world();
  const root = repo(w);
  transcript(w, 'sess-old');
  psLines(w, [proc(6001, 1, '2-03:00:00', 'python3 orphan.py', 'sess-old')]);
  const j = json(w, root, ['--session', 'sess-old'], { CLAUDE_CODE_SESSION_ID: 'a-different-live-session' });
  assert.equal(lw(j).counts.processes, 1);
  assert.match(lw(j).items[0], /pid 6001 · 2d · python3 orphan\.py/);
});

test('--identifiers: launched work is a sub-line of Agents, with every count, zeros included, and the field set holds', () => {
  const w = world();
  const root = repo(w);
  transcript(w, 'sess-l11');
  let out = idRun(w, root, 'sess-l11').out;
  assert.deepEqual(headings(out), FIELDS);
  assert.match(out, /- \*\*Agents\*\*: 0 · none launched\n  - other launched work: 0 live process\(es\) · 0 background command\(s\) not ended · 0 detached launch\(es\) not shown finished · 0 harness-started item\(s\) not ended · 0 schedule\(s\) pending · 0 ended or stopped\n/);
  transcript(w, 'sess-l12', bgRun('q1', 'make x', 'qid'));
  psLines(w, [proc(5555, 1, '00:01:40', 'python3 w.py', 'sess-l12')]);
  out = idRun(w, root, 'sess-l12').out;
  assert.match(out, /  - other launched work: 1 live process\(es\) · 1 background command\(s\) not ended/);
  assert.match(out, /    - ❌ live process: pid 5555 · 2m · python3 w\.py/);
  assert.match(out, /    - ❌ background command: .* make x — task qid/);
  const j = parseId(w, root, 'sess-l12');
  assert.equal(j.launched.known, true);
  assert.equal(j.launched.counts.processes, 1);
  assert.equal(j.launched.items.length, 2);
});

test('parseEtime and argvShown: the age forms ps prints, and an argv cut with its values hidden', () => {
  assert.equal(cc.parseEtime('05:30'), 330);
  assert.equal(cc.parseEtime('01:02:03'), 3723);
  assert.equal(cc.parseEtime('2-03:00:00'), 2 * 86400 + 3 * 3600);
  assert.equal(cc.parseEtime('garbage'), null);
  assert.equal(cc.argvShown('/usr/bin/python3 run.py --key=abc123 --other tail HOME=/x'), 'python3 run.py --key=…');
  assert.equal(cc.argvShown('curl -H Authorization: Bearer SECRET'), 'curl -H …');
});

// --- 210/480: what the prompt asked in words --------------------------------

const human = (text) => ({ type: 'attachment', attachment: { type: 'queued_command', commandMode: 'prompt', origin: { kind: 'human' }, prompt: text } });
const prompt = (text) => ({ type: 'user', message: { role: 'user', content: text } });
const say = (text) => ({ type: 'assistant', message: { model: 'claude-opus-5-5', content: [{ type: 'text', text }] } });
const ask = (id, questions) => useOf(id, 'AskUserQuestion', { questions });
const q = (header, question) => ({ header, question, multiSelect: false, options: [{ label: 'A' }, { label: 'B' }] });
const answered = (id, answers) => resultOf(id, `Your questions have been answered: ${Object.entries(answers).map(([k, v]) => `"${k}"="${v}"`).join(', ')}. You can now continue.`, { answers });

test('210/480 every ask: every principal prompt is listed with its ref, the close-shaped ones tagged, answers and harness text left out', () => {
  const w = world();
  const root = repo(w);
  transcript(w, 'sess-a1', [
    prompt('Please close out the session and record the learnings'),
    human('Also rename the helper to something clearer'),
    prompt('<task-notification><task-id>t</task-id><status>completed</status></task-notification>'),
    ask('qa', [q('Pick', 'Which one?')]), answered('qa', { 'Which one?': 'A' }),
    prompt('And add a changelog line for it'),
  ]);
  const j = json(w, root, ['--session', 'sess-a1']);
  const all = j.askedAll;
  assert.equal(all.total, 4);          // the opening prompt, the close ask, the mid-turn one, the changelog one
  assert.equal(all.closeShaped, 1);
  assert.deepEqual(all.items.map((x) => [x.channel, x.ref, x.close]),
    [['turn', '1', false], ['turn', '2', true], ['mid-turn', '2+1', false], ['turn', '4', false]]);
  assert.ok(all.items.every((x) => !/Which one|answered/.test(x.quote)), 'a tool result is not a prompt');
  assert.equal(j.asked.total, 1, 'the old close-shaped list is unchanged');
  assert.match(j.verdict.line, /4 prompt\(s\) to answer \(1 close-shaped\)/);
  assert.equal(j.verdict.prompts, 4);
  assert.equal(j.verdict.asks, 1);
  const text = ccclose(w, root, ['--session', 'sess-a1']).out;
  assert.match(text, /Asked in this session — answer each: done \/ queued \(item\) \/ not done/);
  assert.match(text, /  2\. .* UTC · turn 2 \[close\] · "Please close out the session/);
  assert.match(text, /  3\. .* UTC · mid-turn 2\+1 · "Also rename the helper/);
  assert.doesNotMatch(text, /turn 1 \[close\]/);
  assert.match(text, /4 prompt\(s\), 1 close-shaped/);
});

test('210/480 every ask: the list is capped and the whole count printed', () => {
  const w = world();
  const root = repo(w);
  transcript(w, 'sess-a2', Array.from({ length: 45 }, (_, i) => prompt(`Do task number ${i}`)));
  const j = json(w, root, ['--session', 'sess-a2']);
  assert.equal(j.askedAll.total, 46);
  assert.equal(j.askedAll.items.length, 40);
  assert.match(ccclose(w, root, ['--session', 'sess-a2']).out, /… and 6 more \(46 in all; cctranscript lists every one\)/);
});

test('210/480 questions: each AskUserQuestion is listed with its answer, or why it has none; an unanswered one warns, never fails', () => {
  const w = world();
  const root = repo(w);
  transcript(w, 'sess-q1', [
    ask('q1', [q('Build', 'Build it now?')]), answered('q1', { 'Build it now?': 'Yes (Recommended)' }),
    ask('q2', [q('Cut', 'Cut the extra?')]),
    resultOf('q2', "[Tool call interrupted: the session ended before this call's result was recorded, so its outcome is unknown.]", "[Tool call interrupted]", true),
    ask('q3', [q('Never', 'Never answered?')]),
    ask('q4', [q('One', 'First of two?'), q('Two', 'Second of two?')]), answered('q4', { 'First of two?': 'X' }),
    useOf('q5', 'AskUserQuestion', { questions: [q('Rej', 'Declined?')] }),
    resultOf('q5', "The user doesn't want to proceed with this tool use.", { stdout: '' }, true),
    say('Here is the plan.\n🎯 **Your call:** whether to ship now.\nBody text.\n⏳ Waiting on your word for the merge.\n🎯 **Your call:** whether to ship now.'),
  ]);
  const j = json(w, root, ['--session', 'sess-q1']);
  const items = j.questions.items;
  assert.equal(j.questions.total, 6);
  assert.equal(j.questions.open, 5 - 1);   // q1 and the first of q4 answered: 6 questions, 4 not
  const by = Object.fromEntries(items.map((x) => [x.question.split(':')[0], x]));
  assert.equal(by.Build.answered, true);
  assert.equal(by.Build.answer, 'Yes (Recommended)');
  assert.match(by.Cut.why, /interrupted before he answered/);
  assert.match(by.Never.why, /no result recorded/);
  assert.equal(by.One.answered, true);
  assert.match(by.Two.why, /no answer recorded for this question/);
  assert.match(by.Rej.why, /declined/);
  assert.equal(j.questions.callouts.total, 2, 'a repeated call-out line counts once');
  assert.match(j.questions.callouts.items[0].text, /^🎯 \*\*Your call:\*\* whether to ship now\./);
  assert.equal(j.code, 0, 'an unanswered question never fails the close');
  assert.equal(j.verdict.status, 'warn');
  assert.match(j.verdict.line, /4 unanswered question\(s\)/);
  const text = ccclose(w, root, ['--session', 'sess-q1']).out;
  assert.match(text, /✅ .* · Build: Build it now\? — answered: Yes \(Recommended\)/);
  assert.match(text, /⚠️ .* · Never: Never answered\? — NOT answered: no result recorded/);
  assert.match(text, /6 question\(s\), 4 unanswered/);
  assert.match(text, /Call-out lines \(🎯 or ⏳\) in the session's own replies: 2, each an open ask/);
});

test('210/480 questions: none asked prints a known zero, and no transcript prints unknown', () => {
  const w = world();
  const root = repo(w);
  transcript(w, 'sess-q2');
  const text = ccclose(w, root, ['--session', 'sess-q2']).out;
  assert.match(text, /none asked \(AskUserQuestion\)\n  0 question\(s\), 0 unanswered\n  Call-out lines \(🎯 or ⏳\) in the session's own replies: 0\n/);
  const k = json(w, root, ['--session', 'no-such']);
  assert.equal(k.questions.total, null);
  assert.equal(k.askedAll.total, null);
  assert.match(k.verdict.line, /prompts unknown · questions unknown/);
});

// A second repo with an unpushed commit from the window, and a third that was
// only visited. The transcript's Bash records carry the directories.
function twoRepoWorld(sid, extra = []) {
  const w = world();
  const root = repo(w);
  const other = repo(w, 'other');
  const calm = repo(w, 'calm');
  write(other, 'docs/sessions/README.md', 'the session log\n');
  commit(w, other, 'other: seed the session folder', NOW - 2 * 24 * 60 * MIN);
  write(other, 'o.txt', 'o\n');
  commit(w, other, 'other: work', NOW - 30 * MIN);
  const recs = [
    bashUse('o1', 'ls', other), bashUse('o2', `cd ${calm} && git log -1`, root),
    bashUse('o3', `git -C ${other} status`, root),
    bashUse('o4', 'ls', '/nonexistent-dir-xyz/sub'),
    ...extra,
  ];
  transcript(w, sid, recs);
  return { w, root, other, calm };
}

test('210/480 other repos: a repo the session worked in elsewhere gets the repo checks, and a failure there fails the close', () => {
  const { w, root, other } = twoRepoWorld('sess-r1');
  const j = json(w, root, ['--session', 'sess-r1']);
  const o = j.otherRepos;
  assert.equal(o.known, true);
  assert.deepEqual(o.items.map((x) => x.name).sort(), ['calm', 'other']);
  const rep = Object.fromEntries(o.items.map((x) => [x.name, x]));
  assert.equal(rep.other.root, fs.realpathSync(other));
  assert.equal(rep.other.commitsInWindow, 1);
  assert.equal(rep.other.status, 'fail');
  assert.deepEqual(rep.other.checks.map((c) => c.id), ['worktrees', 'branches', 'pushed', 'session-record', 'claims', 'tree']);
  const st = Object.fromEntries(rep.other.checks.map((c) => [c.id, c.status]));
  assert.equal(st.pushed, 'fail');
  assert.equal(st['session-record'], 'fail', 'the session committed there and wrote no record');
  assert.equal(rep.calm.status, 'pass');
  assert.equal(rep.calm.commitsInWindow, 0);
  assert.equal(rep.calm.checks.find((c) => c.id === 'session-record').status, 'na', 'a repo only visited owes no record');
  assert.equal(o.unresolved, 1, 'the path that is in no repo is counted');
  assert.equal(j.verdict.otherRepoFail, 2);
  assert.equal(j.verdict.fail, 2);
  assert.equal(j.code, 1);
  assert.match(j.verdict.line, /2 other repo\(s\) touched/);
  const text = ccclose(w, root, ['--session', 'sess-r1']).out;
  assert.match(text, /❌ other · .*other · 1 commit\(s\) in the window\n +✅ worktrees · ✅ branches · ❌ pushed · ❌ record · ➖ claims · ✅ tree/);
  assert.match(text, /✅ calm · .* 0 commit\(s\) in the window/);
  assert.match(text, /1 path\(s\) the session worked in could not be placed in a repo/);
});

test('210/480 other repos: the home repo\'s own worktrees and scratch folders are not other repos; a worktree path created counts toward its repo', () => {
  const w = world();
  const root = repo(w);
  const wt = path.join(w.base, 'wt-home');
  sh(w, root, ['worktree', 'add', '-q', '-b', 'side', wt]);
  const other = repo(w, 'elsewhere');
  const otherWt = path.join(w.base, 'wt-elsewhere');
  sh(w, other, ['worktree', 'add', '-q', '-b', 'side2', otherWt]);
  transcript(w, 'sess-r2', [bashUse('h1', 'ls', wt), bashUse('h2', 'ls', otherWt),
    { type: 'attachment', attachment: { type: 'environment', snapshot: { scratchpadDirectory: path.join(w.base, 'scratch') } } }]);
  fs.mkdirSync(path.join(w.base, 'scratch'));
  const j = json(w, root, ['--session', 'sess-r2']);
  assert.deepEqual(j.otherRepos.items.map((x) => x.name), ['elsewhere'], 'the home worktree and the scratch folder are no other repo');
  assert.equal(j.otherRepos.items[0].root, fs.realpathSync(other), 'checks run on the main checkout, not the linked worktree');
});

test('210/480 other repos: the identifiers line names them with their commits, counts what it could not place, and says how to name a private one', () => {
  const { w, root } = twoRepoWorld('sess-r3');
  const out = idRun(w, root, 'sess-r3').out;
  assert.deepEqual(headings(out), FIELDS);
  assert.match(out, /- \*\*Other repos\*\* \(2\):\n  - other — 1 commit\(s\) in the window; its checks: fail\n  - calm — 0 commit\(s\) in the window\n/);
  assert.match(out, /  - 1 path\(s\) could not be placed in a repo — fill in by hand\n/);
  assert.match(out, /  - name a private repo generically in a public record/);
  assert.doesNotMatch(out, /fill in by hand\n.*\n## /);
  const j = parseId(w, root, 'sess-r3');
  assert.equal(j.otherRepos, 'other, calm');
  assert.equal(j.touched.known, true);
  assert.equal(j.touched.items.length, 2);
  assert.equal(j.touched.unresolved, 1);
  // Nothing found, and no transcript, each print a known state rather than a stale fill-in line.
  const w2 = world();
  const root2 = repo(w2);
  transcript(w2, 'sess-r4');
  assert.match(idRun(w2, root2, 'sess-r4').out, /- \*\*Other repos\*\*: none found\n/);
  assert.match(idRun(w2, root2, 'no-such').out, /- \*\*Other repos\*\*: by hand — no transcript/);
});

test('210/480 other repos: a plain run exits 0 when every other repo is clean', () => {
  const w = world();
  const root = repo(w);
  const calm = repo(w, 'calm');
  write(root, 'docs/sessions/2020-01-01-0000-x.md', '# x\n');
  commit(w, root, 'records: session close', NOW - 30 * MIN);
  sh(w, root, ['push', '-q', 'origin', 'main']);
  transcript(w, 'sess-r5', [bashUse('c1', `cd ${calm} && git log -1`, root)]);
  const j = json(w, root, ['--session', 'sess-r5']);
  assert.equal(j.otherRepos.items.length, 1);
  assert.equal(j.verdict.otherRepoFail, 0);
  assert.equal(j.code, 0);
  assert.equal(j.verdict.status, 'pass');
  assert.match(j.verdict.line, /^✅ ready to close/);
});

// Another session's transcript, written now (live) or a while ago (stale), with
// the working directory it recorded.
function peerSession(w, id, cwd, { agoMin = 0, title = 'A peer job' } = {}) {
  const p = path.join(w.home, '.claude', 'projects', 'proj', `${id}.jsonl`);
  const recs = [{ type: 'user', timestamp: new Date(NOW).toISOString(), cwd, gitBranch: 'main', message: { role: 'user', content: 'hello' } },
    { type: 'ai-title', aiTitle: title }];
  fs.writeFileSync(p, recs.map((r) => JSON.stringify(r)).join('\n') + '\n');
  const t = new Date(Date.now() - agoMin * MIN);
  fs.utimesSync(p, t, t);
}

test('210/480 live sessions: another session written in the last ten minutes in these repos is listed as a warning, never a failure', () => {
  const { w, root, other } = twoRepoWorld('sess-s1');
  sh(w, other, ['push', '-q', 'origin', 'main']);
  peerSession(w, 'peer-in-root', root, { title: 'Peer in the root repo' });
  peerSession(w, 'peer-in-other', other, { agoMin: 3, title: 'Peer in a touched repo' });
  peerSession(w, 'peer-stale', root, { agoMin: 40 });
  peerSession(w, 'peer-elsewhere', path.join(w.base, 'unrelated'), {});
  fs.mkdirSync(path.join(w.base, 'unrelated'));
  const j = json(w, root, ['--session', 'sess-s1']);
  const l = j.liveSessions;
  assert.equal(l.known, true);
  assert.deepEqual(l.items.map((x) => x.session).sort(), ['peer-in-other', 'peer-in-root']);
  assert.ok(!l.items.some((x) => x.session === 'sess-s1'), 'the session checked is not another');
  assert.equal(j.verdict.liveSessions, 2);
  assert.match(j.verdict.line, /2 other live session\(s\)/);
  const text = ccclose(w, root, ['--session', 'sess-s1']).out;
  assert.match(text, /Other live sessions in these repos — answer: do they have what they need from you\?\n  ⚠️ peer-in- · repo · /);
  assert.match(text, /⚠️ peer-in- · other · .* · written 3m(\d+s)? ago · Peer in a touched repo/);
  assert.doesNotMatch(text, /written \d+\.\d+ms ago/, 'an age prints whole milliseconds');
});

test('210/480 live sessions: none is a known zero (➖), and a live peer alone only asks for a look: exit 0', () => {
  const w = world();
  const root = repo(w);
  write(root, 'docs/sessions/2020-01-01-0000-x.md', '# x\n');
  commit(w, root, 'records: session close', NOW - 30 * MIN);
  sh(w, root, ['push', '-q', 'origin', 'main']);
  transcript(w, 'sess-s2');
  let j = json(w, root, ['--session', 'sess-s2']);
  assert.equal(j.liveSessions.known, true);
  assert.deepEqual(j.liveSessions.items, []);
  assert.match(ccclose(w, root, ['--session', 'sess-s2']).out, /  ➖ none \(no other transcript written in the last 10 min/);
  assert.equal(j.verdict.status, 'pass');
  peerSession(w, 'peer-x', root);
  j = json(w, root, ['--session', 'sess-s2']);
  assert.equal(j.verdict.status, 'warn');
  assert.equal(j.code, 0);
  assert.match(j.verdict.line, /^⚠️ no check fails; some need a look/);
});

test('210/480 the default run is one command: the four listings, the verdict, then the identifiers block; --identifiers alone is the block', () => {
  const { w, root } = twoRepoWorld('sess-o1');
  const out = ccclose(w, root, ['--session', 'sess-o1']).out;
  const at = (s) => out.indexOf(s);
  const order = ['\nChecks\n', '\nAsked in this session', '\nQuestions put to the principal', '\nOther repos touched', '\nOther live sessions in these repos', '\n❌ not ready to close', '\n## Identifiers\n'];
  const pos = order.map(at);
  assert.ok(pos.every((x) => x >= 0), JSON.stringify(pos));
  assert.deepEqual([...pos].sort((a, b) => a - b), pos, 'in this order');
  const alone = idRun(w, root, 'sess-o1').out;
  assert.ok(alone.startsWith('## Identifiers\n'));
  assert.doesNotMatch(alone, /Asked in this session|Other live sessions/);
});
