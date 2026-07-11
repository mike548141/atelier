// Stdlib-only tests for ccrepo — Node's built-in node:test + node:assert, zero
// third-party dep (mirrors tools/'s "stdlib only, no pytest" floor). Named
// *.test.js per node:test convention; the shell glob expands at run time, so a
// new test file is picked up without editing any command. Run:
//   node --test instruments/*.test.js
//
// ccrepo shells out to `ccusage` (execFileSync) for its per-session rows, so a
// true end-to-end run needs that binary. The aggregation — the part ccrepo owns
// — is factored behind aggregate(sessions, index, groupBy), a pure function over
// fixture session data and a fixture session->repo index. That is what these
// tests drive. HONEST SCOPE (see ROADMAP residual): the ccusage invocation, JSON
// parse, FX conversion, and table render are NOT covered here — only the pure
// functions and the aggregation fold are.

const test = require('node:test');
const assert = require('node:assert');

const r = require('./ccrepo');

// --- pure functions -----------------------------------------------------

test('symbolFor knows the common codes and prefixes the rest', () => {
  assert.equal(r.symbolFor('NZD'), 'NZ$');
  assert.equal(r.symbolFor('USD'), 'US$');
  assert.equal(r.symbolFor('GBP'), '£');
  assert.equal(r.symbolFor('XYZ'), 'XYZ ');   // unknown → explicit code prefix
});

test('shortModel drops the claude- prefix, passes others through, tolerates absence', () => {
  assert.equal(r.shortModel('claude-opus-4-8'), 'opus-4-8');
  assert.equal(r.shortModel('gpt-4'), 'gpt-4');
  // A ccusage breakdown row may drift and drop modelName; the fold must not throw.
  assert.equal(r.shortModel(undefined), 'unknown');
  assert.equal(r.shortModel(''), 'unknown');
});

test('dayOf returns unknown for missing/invalid, YYYY-MM-DD otherwise', () => {
  assert.equal(r.dayOf(null), 'unknown');
  assert.equal(r.dayOf('garbage'), 'unknown');
  assert.match(r.dayOf('2026-01-02T03:04:05.000Z'), /^\d{4}-\d{2}-\d{2}$/); // local tz, shape only
});

test('zeroAgg / addTo / addChild accumulate correctly', () => {
  const z = r.zeroAgg();
  assert.deepEqual(z, { sessions: 0, inputTokens: 0, outputTokens: 0,
    cacheCreationTokens: 0, cacheReadTokens: 0, totalTokens: 0, cost: 0 });
  r.addTo(z, { sessions: 1, inputTokens: 2, outputTokens: 3,
    cacheCreationTokens: 1, cacheReadTokens: 4, totalTokens: 10, cost: 0.5 });
  r.addTo(z, { sessions: 1, inputTokens: 8, outputTokens: 7, totalTokens: 15, cost: 1.5 }); // no cache fields → 0
  assert.deepEqual(z, { sessions: 2, inputTokens: 10, outputTokens: 10,
    cacheCreationTokens: 1, cacheReadTokens: 4, totalTokens: 25, cost: 2 });

  const repo = { children: new Map() };
  r.addChild(repo, 'opus', { sessions: 1, inputTokens: 4, outputTokens: 1, totalTokens: 5, cost: 0.4 });
  r.addChild(repo, 'opus', { sessions: 1, inputTokens: 6, outputTokens: 1, totalTokens: 7, cost: 0.6 });
  assert.equal(repo.children.size, 1);
  assert.deepEqual(repo.children.get('opus'),
    { sessions: 2, inputTokens: 10, outputTokens: 2,
      cacheCreationTokens: 0, cacheReadTokens: 0, totalTokens: 12, cost: 1 });
});

test('cacheHitRate is read share of prompt-side tokens, null when there are none', () => {
  // 20 reads / (100 input + 10 create + 20 read) = 20/130
  assert.ok(Math.abs(r.cacheHitRate({ inputTokens: 100, cacheCreationTokens: 10, cacheReadTokens: 20 }) - 20 / 130) < 1e-12);
  assert.equal(r.cacheHitRate({ inputTokens: 0, cacheCreationTokens: 0, cacheReadTokens: 0 }), null);
  assert.equal(r.cacheHitRate(r.zeroAgg()), null);
  // output tokens play no part in the ratio
  assert.equal(r.cacheHitRate({ inputTokens: 50, cacheCreationTokens: 0, cacheReadTokens: 50, outputTokens: 999 }), 0.5);
});

test('label prefers the index name, else dash-decodes the last segment', () => {
  assert.equal(r.label('weird', new Map([['weird', 'Nice Name']])), 'Nice Name'); // index hit
  assert.equal(r.label('-Users-dev-atelier', new Map()), 'atelier');              // fallback
  assert.equal(r.label('foo-bar-baz', new Map()), 'baz');
});

// --- aggregation over fixture ccusage session rows ----------------------

// Shape mirrors `ccusage session --json`'s .session entries: period is the
// session UUID, plus token counts, totalCost, per-model breakdowns, metadata.
const SESSIONS = [
  // ccusage's totalTokens already includes the cache tokens (input+output+create+read).
  // lastActivity times sit at midday UTC, minutes apart: dayOf() buckets by
  // LOCAL day, and midday-UTC stamps this close share a calendar day in every
  // real offset (-12:00..+14:00) — timestamps near 00:00Z straddle local
  // midnight in UTC-4/-3:30 zones and make the --by-day test tz-dependent.
  { period: 's1', inputTokens: 100, outputTokens: 50,
    cacheCreationTokens: 10, cacheReadTokens: 20, totalTokens: 180, totalCost: 1.0,
    metadata: { lastActivity: '2026-01-02T12:00:00.000Z' },
    modelBreakdowns: [{ modelName: 'claude-opus-4-8', inputTokens: 100, outputTokens: 50,
      cacheCreationTokens: 10, cacheReadTokens: 20, cost: 1.0 }] },
  { period: 's2', inputTokens: 200, outputTokens: 100,
    cacheCreationTokens: 0, cacheReadTokens: 0, totalTokens: 300, totalCost: 2.0,
    metadata: { lastActivity: '2026-01-02T12:05:00.000Z' },
    modelBreakdowns: [{ modelName: 'claude-sonnet-5', inputTokens: 200, outputTokens: 100,
      cacheCreationTokens: 0, cacheReadTokens: 0, cost: 2.0 }] },
  // s3 is deliberately absent from the index → must count as unmatched.
  { period: 's3', inputTokens: 5, outputTokens: 5, totalTokens: 10, totalCost: 0.1,
    modelBreakdowns: [] },
];
const INDEX = new Map([['s1', '-a-repoA'], ['s2', '-a-repoA']]);

test('aggregate folds matched sessions per repo and counts unmatched', () => {
  const { repos, unmatched } = r.aggregate(SESSIONS, INDEX, null);
  assert.equal(unmatched, 1);                    // s3 had no repo folder
  const a = repos.get('-a-repoA');
  assert.equal(a.sessions, 2);
  assert.equal(a.inputTokens, 300);
  assert.equal(a.outputTokens, 150);
  assert.equal(a.cacheCreationTokens, 10);
  assert.equal(a.cacheReadTokens, 20);
  assert.equal(a.totalTokens, 480);
  assert.ok(Math.abs(a.cost - 3.0) < 1e-9);
  assert.ok(Math.abs(r.cacheHitRate(a) - 20 / 330) < 1e-12); // 20 reads / (300 in + 10 create + 20 read)
  assert.equal(a.children.size, 0);              // no grouping requested
});

test('aggregate --by-model breaks each repo down by model, cache tokens folded into total', () => {
  const { repos } = r.aggregate(SESSIONS, INDEX, 'model');
  const a = repos.get('-a-repoA');
  assert.equal(a.children.size, 2);
  const opus = a.children.get('opus-4-8');
  assert.equal(opus.sessions, 1);
  assert.equal(opus.cacheCreationTokens, 10);
  assert.equal(opus.cacheReadTokens, 20);
  assert.equal(opus.totalTokens, 180);           // 100 + 50 + 10 (cache create) + 20 (cache read)
  assert.ok(Math.abs(opus.cost - 1.0) < 1e-9);
  assert.equal(a.children.get('sonnet-5').totalTokens, 300); // 200 + 100 + 0 + 0
});

test('aggregate --by-day buckets whole sessions by last-activity day', () => {
  const { repos } = r.aggregate(SESSIONS, INDEX, 'day');
  const a = repos.get('-a-repoA');
  // Both sessions share a local day here; assert the fold, not the tz-local key.
  assert.equal(a.children.size, 1);
  const day = [...a.children.values()][0];
  assert.equal(day.sessions, 2);
  assert.equal(day.totalTokens, 480);
});

test('aggregate --by-model survives a breakdown row without modelName', () => {
  const drifted = [{ period: 's1', inputTokens: 1, outputTokens: 1, totalTokens: 2, totalCost: 0.1,
    modelBreakdowns: [{ inputTokens: 1, outputTokens: 1, cost: 0.1 }] }];
  const { repos } = r.aggregate(drifted, new Map([['s1', '-a-repoA']]), 'model');
  assert.ok(repos.get('-a-repoA').children.has('unknown'));
});

// --- module-load safety (require must be inert) --------------------------

const { execFileSync } = require('node:child_process');
const path = require('node:path');

test('requiring ccrepo never acts on the host argv (help/validation live in main)', () => {
  const script = path.join(__dirname, 'ccrepo');
  // The -e host's argv.slice(2) is exactly the flags after the script path:
  // '-h' used to print ccrepo's help and exit(0), killing the host; conflicting
  // flags used to exit(2) at load. Both must now be inert under require().
  for (const flags of [['-h'], ['--by-model', '--by-day']]) {
    const out = execFileSync('node',
      ['-e', 'require(process.argv[1]); console.log("host-alive")', script, ...flags],
      { encoding: 'utf8' });
    assert.equal(out.trim(), 'host-alive');
  }
});
