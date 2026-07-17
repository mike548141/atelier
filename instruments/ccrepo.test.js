// Stdlib-only tests for ccrepo — Node's built-in node:test + node:assert, zero
// third-party dep (mirrors tools/'s "stdlib only, no pytest" floor). Named
// *.test.js per node:test convention; the shell glob expands at run time. Run:
//   node --test instruments/*.test.js
//
// v2 reads the raw logs and computes cost itself, so the pure core is bigger:
// pricing, message parsing, N-level grouping, sorting, filters, and the ccusage
// reconciliation are all factored into pure functions the tests drive directly.
// HONEST SCOPE: the disk walk (readAllEvents), the live ccusage/FX calls, and the
// terminal render are NOT unit-covered — only the pure functions they compose.

const test = require('node:test');
const assert = require('node:assert');

const r = require('./ccrepo');

// --- currency + model names ---------------------------------------------

test('symbolFor gives a bare money marker; header + footnote name the currency', () => {
  assert.equal(r.symbolFor('NZD'), '$');
  assert.equal(r.symbolFor('USD'), '$');
  assert.equal(r.symbolFor('GBP'), '£');
  assert.equal(r.symbolFor('XYZ'), '');
});

test('shortModel drops the claude- prefix, passes others through, tolerates absence', () => {
  assert.equal(r.shortModel('claude-opus-4-8'), 'opus-4-8');
  assert.equal(r.shortModel('gpt-4'), 'gpt-4');
  assert.equal(r.shortModel(undefined), 'unknown');
  assert.equal(r.shortModel(''), 'unknown');
});

// --- time bucketing ------------------------------------------------------

test('timeBucket keys by local granularity; unknown for missing/bad', () => {
  const t = '2026-07-15T12:00:00.000Z'; // midday UTC → same calendar day in every real offset
  assert.equal(r.timeBucket(t, 'year'), '2026');
  assert.equal(r.timeBucket(t, 'month'), '2026-07');
  assert.match(r.timeBucket(t, 'day'), /^2026-07-\d{2}$/);
  assert.match(r.timeBucket(t, 'hour'), /^2026-07-\d{2} \d{2}h$/);
  assert.match(r.timeBucket(t, 'week'), /^2026-W\d{2}$/);
  assert.equal(r.timeBucket(null, 'day'), 'unknown');
  assert.equal(r.timeBucket('garbage', 'month'), 'unknown');
});

test('isoWeek follows ISO-8601 (Mon start, week 1 holds Jan 4)', () => {
  // 2026-01-01 is a Thursday → ISO week 1 of 2026.
  assert.equal(r.isoWeek(new Date(2026, 0, 1)), '2026-W01');
  // 2026-01-04 (Sunday) is still week 1; 2026-01-05 (Monday) starts week 2.
  assert.equal(r.isoWeek(new Date(2026, 0, 5)), '2026-W02');
});

// --- pricing -------------------------------------------------------------

test('priceBase uses longest-prefix match; null for unpriced', () => {
  assert.equal(r.priceBase('opus-4-8'), 5);
  assert.equal(r.priceBase('fable-5'), 10);
  assert.equal(r.priceBase('sonnet-5'), 2);
  assert.equal(r.priceBase('sonnet-4-6'), 3);   // 'sonnet-4' beats 'sonnet-5' by prefix
  assert.equal(r.priceBase('haiku-4-5-20251001'), 1);
  assert.equal(r.priceBase('gpt-4'), null);
  assert.equal(r.priceBase('<synthetic>'), null);
});

test('messageCost sums five token classes at the standard multipliers', () => {
  // opus base $5/MTok: in 5, out 25, read 0.5, write5m 6.25, write1h 10.
  const { cost, priced } = r.messageCost('opus-4-8',
    { input: 100, output: 50, cacheRead: 1000, write5m: 40, write1h: 60 });
  // (100*5 + 50*25 + 1000*0.5 + 40*6.25 + 60*10) / 1e6 = 3100/1e6
  assert.ok(Math.abs(cost - 0.0031) < 1e-12);
  assert.equal(priced, true);
  // unpriced model → zero, priced:false (surfaced in the drift report, not guessed)
  const syn = r.messageCost('<synthetic>', { input: 10, output: 10 });
  assert.deepEqual(syn, { cost: 0, priced: false });
});

test('loadPricing merges an override over the built-in table, ignores junk', () => {
  const fs = require('node:fs'), os = require('node:os'), p = require('node:path');
  const dir = fs.mkdtempSync(p.join(os.tmpdir(), 'ccrepo-price-'));
  const good = p.join(dir, 'ok.json');
  fs.writeFileSync(good, JSON.stringify({ 'opus-4-8': 6, 'claude-newmodel-1': 4 }));
  const merged = r.loadPricing(good);
  assert.equal(r.priceBase('opus-4-8', merged), 6);          // overridden
  assert.equal(r.priceBase('newmodel-1', merged), 4);        // added (claude- stripped)
  assert.equal(r.priceBase('haiku-4-5', merged), 1);         // built-in preserved
  const bad = p.join(dir, 'bad.json'); fs.writeFileSync(bad, '{ not json');
  const orig = console.error; console.error = () => {};
  try { assert.equal(r.priceBase('opus-4-8', r.loadPricing(bad)), 5); } finally { console.error = orig; }
});

// --- aggregates ----------------------------------------------------------

test('zeroAgg / addTo accumulate the token + cost + message fields', () => {
  const z = r.zeroAgg();
  assert.deepEqual(z, { messages: 0, inputTokens: 0, outputTokens: 0, cacheCreationTokens: 0,
    cacheReadTokens: 0, totalTokens: 0, cost: 0, coveredTokens: 0, uncoveredCost: 0 });
  r.addTo(z, { messages: 5, inputTokens: 2, outputTokens: 3, cacheCreationTokens: 1, cacheReadTokens: 4,
    totalTokens: 10, cost: 0.5, coveredTokens: 10, uncoveredCost: 0 });
  r.addTo(z, { inputTokens: 8, outputTokens: 7, totalTokens: 15, cost: 1.5 }); // missing fields → 0
  assert.deepEqual(z, { messages: 5, inputTokens: 10, outputTokens: 10, cacheCreationTokens: 1,
    cacheReadTokens: 4, totalTokens: 25, cost: 2, coveredTokens: 10, uncoveredCost: 0 });
});

test('cacheHitRate is read share of prompt-side tokens, null when there are none', () => {
  assert.ok(Math.abs(r.cacheHitRate({ inputTokens: 100, cacheCreationTokens: 10, cacheReadTokens: 20 }) - 20 / 130) < 1e-12);
  assert.equal(r.cacheHitRate(r.zeroAgg()), null);
  assert.equal(r.cacheHitRate({ inputTokens: 50, cacheCreationTokens: 0, cacheReadTokens: 50, outputTokens: 999 }), 0.5);
});

test('label prefers the index name, else dash-decodes the last segment', () => {
  assert.equal(r.label('weird', new Map([['weird', 'Nice Name']])), 'Nice Name');
  assert.equal(r.label('-Users-dev-atelier', new Map()), 'atelier');
  assert.equal(r.label('foo-bar-baz', new Map()), 'baz');
});

// --- parsing a raw assistant record into an event -----------------------

const RAW = {
  type: 'assistant', sessionId: 'sess-A', timestamp: '2026-07-15T12:00:00.000Z',
  gitBranch: 'feature-x', version: '2.1.209', entrypoint: 'cli', isSidechain: false,
  agent: null, requestId: 'req-1',
  message: {
    id: 'msg-1', model: 'claude-opus-4-8',
    usage: {
      input_tokens: 100, output_tokens: 50, cache_read_input_tokens: 1000,
      cache_creation: { ephemeral_5m_input_tokens: 40, ephemeral_1h_input_tokens: 60 },
    },
  },
};

test('eventFrom parses tokens, splits cache write, computes cost, tags dimensions', () => {
  const e = r.eventFrom(RAW, { repo: 'ros', session: 'sess-A', sub: false, covers: null });
  assert.equal(e.model, 'opus-4-8');
  assert.equal(e.repo, 'ros');
  assert.equal(e.branch, 'feature-x');
  assert.equal(e.version, '2.1.209');
  assert.equal(e.kind, 'main');
  assert.equal(e.inputTokens, 100);
  assert.equal(e.outputTokens, 50);
  assert.equal(e.cacheReadTokens, 1000);
  assert.equal(e.cacheCreationTokens, 100);   // 40 + 60
  assert.equal(e.totalTokens, 1250);          // 100 + 50 + 1000 + 100
  assert.equal(e.messages, 1);                // one event = one message
  assert.ok(Math.abs(e.cost - 0.0031) < 1e-12);
  assert.equal(e.priced, true);
});

test('eventFrom marks subagents (path flag OR isSidechain) and skips non-assistant', () => {
  assert.equal(r.eventFrom(RAW, { sub: true }).kind, 'subagent');            // subagent log file
  assert.equal(r.eventFrom({ ...RAW, isSidechain: true }, {}).kind, 'subagent'); // inline sidechain
  assert.equal(r.eventFrom({ type: 'user' }, {}), null);
  assert.equal(r.eventFrom(null, {}), null);
});

test('eventFrom leaves an unknown repo FALSY so the walk can resolve it later', () => {
  // A truthy placeholder ('—') would lock in and skip readAllEvents' post-walk
  // resolution — the bug that mislabelled subagent logs walked before their
  // dir's main file. Empty here; DIMS.repo shows '—' only at display time.
  const e = r.eventFrom(RAW, { sub: true });     // no repo passed
  assert.equal(e.repo, '');
  assert.equal(r.DIMS.repo(e), '—');
  assert.equal(r.DIMS.repo({ repo: 'ros' }), 'ros');
});

test('eventFrom applies the billing split via covers()', () => {
  const covers = (m) => m.startsWith('opus');
  const cov = r.eventFrom(RAW, { covers });
  assert.equal(cov.coveredTokens, 1250);       // opus is covered → all tokens covered
  assert.equal(cov.uncoveredCost, 0);
  const unc = r.eventFrom({ ...RAW, message: { ...RAW.message, model: 'claude-fable-5' } }, { covers });
  assert.equal(unc.coveredTokens, 0);
  assert.ok(unc.uncoveredCost > 0);            // fable not covered → its cost is uncovered
});

test('eventFrom falls back to lumped cache_creation_input_tokens when no split', () => {
  const noSplit = { ...RAW, message: { ...RAW.message, usage: {
    input_tokens: 1, output_tokens: 1, cache_read_input_tokens: 0, cache_creation_input_tokens: 500 } } };
  assert.equal(r.eventFrom(noSplit, {}).cacheCreationTokens, 500);
});

// --- filters -------------------------------------------------------------

test('globMatch: glob, session prefix, model substring, else exact', () => {
  assert.equal(r.globMatch('client-*', 'client-db', 'branch'), true);
  assert.equal(r.globMatch('client-*', 'main', 'branch'), false);
  assert.equal(r.globMatch('01c3', '01c3baf4-...', 'session'), true);   // prefix
  assert.equal(r.globMatch('opus', 'opus-4-8', 'model'), true);         // substring
  assert.equal(r.globMatch('ros', 'ros', 'repo'), true);               // exact
  assert.equal(r.globMatch('ro', 'ros', 'repo'), false);               // exact, not prefix
});

test('buildDimFilter: AND across dims, OR within, ! excludes', () => {
  const ev = (o) => ({ repo: 'ros', model: 'opus-4-8', branch: 'main', session: 'abc123', ...o });
  assert.equal(r.buildDimFilter({ repo: 'ros' })(ev()), true);
  assert.equal(r.buildDimFilter({ repo: 'faves' })(ev()), false);
  assert.equal(r.buildDimFilter({ repo: 'ros,faves' })(ev()), true);          // OR within
  assert.equal(r.buildDimFilter({ repo: '!scanme' })(ev()), true);            // exclude miss → keep
  assert.equal(r.buildDimFilter({ repo: '!ros' })(ev()), false);              // exclude hit → drop
  assert.equal(r.buildDimFilter({ model: 'opus' })(ev()), true);              // substring
  assert.equal(r.buildDimFilter({ repo: 'ros', model: 'fable' })(ev()), false); // AND across dims
  assert.equal(r.buildDimFilter({ session: 'abc' })(ev()), true);             // prefix
});

// --- N-level grouping + sorting -----------------------------------------

const mkEv = (o) => ({ repo: 'r', session: 's', model: 'm', branch: 'b', kind: 'main',
  entrypoint: 'cli', version: 'v', agent: '', ts: '2026-07-15T12:00:00.000Z', messages: 1,
  inputTokens: 0, outputTokens: 0, cacheCreationTokens: 0, cacheReadTokens: 0,
  totalTokens: 0, cost: 0, coveredTokens: 0, uncoveredCost: 0, ...o });

test('groupTree folds into an N-level tree with distinct session counts', () => {
  const evs = [
    mkEv({ repo: 'A', model: 'opus-4-8', session: 's1', totalTokens: 10, cost: 1 }),
    mkEv({ repo: 'A', model: 'opus-4-8', session: 's1', totalTokens: 5, cost: 0.5 }), // same session
    mkEv({ repo: 'A', model: 'fable-5', session: 's2', totalTokens: 20, cost: 4 }),
    mkEv({ repo: 'B', model: 'opus-4-8', session: 's3', totalTokens: 1, cost: 0.1 }),
  ];
  const root = r.groupTree(evs, ['repo', 'model']);
  assert.equal(root.sessions.size, 3);                       // s1, s2, s3 distinct
  assert.equal(root.agg.messages, 4);                        // 4 messages (not deduped to sessions)
  assert.ok(Math.abs(root.agg.cost - 5.6) < 1e-9);
  const A = root.children.get('A');
  assert.equal(A.sessions.size, 2);                          // s1, s2
  assert.equal(A.agg.messages, 3);                           // 3 messages in repo A
  assert.equal(A.children.get('opus-4-8').sessions.size, 1); // s1 twice → 1 distinct session
  assert.equal(A.children.get('opus-4-8').agg.messages, 2);  // but 2 messages
  assert.equal(A.children.get('opus-4-8').agg.totalTokens, 15);
  // keys=[] → just the root grand total, no children.
  const flat = r.groupTree(evs, []);
  assert.equal(flat.children.size, 0);
  assert.ok(Math.abs(flat.agg.cost - 5.6) < 1e-9);
});

test('sortedEntries: cost desc default, time asc default, spec overrides', () => {
  const root = r.groupTree([
    mkEv({ repo: 'cheap', session: 'a', cost: 1 }),
    mkEv({ repo: 'dear', session: 'b', cost: 9 }),
  ], ['repo']);
  assert.deepEqual(r.sortedEntries(root, 'repo', null).map((e) => e[0]), ['dear', 'cheap']); // cost desc
  assert.deepEqual(r.sortedEntries(root, 'repo', { key: 'name' }).map((e) => e[0]), ['cheap', 'dear']); // alpha
  const byMonth = r.groupTree([
    mkEv({ session: 'a', ts: '2026-07-15T12:00:00Z' }),
    mkEv({ session: 'b', ts: '2026-06-15T12:00:00Z' }),
  ], ['month']);
  assert.deepEqual(r.sortedEntries(byMonth, 'month', null).map((e) => e[0]), ['2026-06', '2026-07']); // time asc
});

test('treeRows walks pre-order with depth; leafRows gives full key paths', () => {
  const evs = [
    mkEv({ repo: 'A', model: 'opus-4-8', session: 's1', cost: 2 }),
    mkEv({ repo: 'A', model: 'fable-5', session: 's2', cost: 1 }),
  ];
  const root = r.groupTree(evs, ['repo', 'model']);
  const specs = [null, null];
  const tr = r.treeRows(root, ['repo', 'model'], specs);
  assert.deepEqual(tr.map((x) => [x.depth, x.label]), [[1, 'A'], [2, 'opus-4-8'], [2, 'fable-5']]);
  const lr = r.leafRows(root, ['repo', 'model'], specs);
  assert.deepEqual(lr.map((x) => x.path), [['A', 'opus-4-8'], ['A', 'fable-5']]);
  // keys=[] → one leaf, empty path (the grand total).
  assert.deepEqual(r.leafRows(root, [], []).map((x) => x.path), [[]]);
});

// --- reconciliation ------------------------------------------------------

test('reconcile compares per-session + per-model cost; null when ccusage absent', () => {
  const my = [
    { session: 'a', model: 'opus-4-8', cost: 10 },
    { session: 'b', model: 'fable-5', cost: 5 },
    { session: 'c', model: 'opus-4-8', cost: 2 },   // 'c' not in ccusage → my-only
  ];
  const ccu = [
    { period: 'a', totalCost: 10.5, modelBreakdowns: [{ modelName: 'claude-opus-4-8', cost: 10.5 }] },
    { period: 'b', totalCost: 5, modelBreakdowns: [{ modelName: 'claude-fable-5', cost: 5 }] },
  ];
  const rec = r.reconcile(my, ccu);
  assert.equal(rec.matched, 2);                    // a, b in both
  assert.equal(rec.myOnly, 1);                     // c
  assert.ok(Math.abs(rec.myTot - 15) < 1e-9);      // a+b mine (c excluded from matched)
  assert.ok(Math.abs(rec.cuTot - 15.5) < 1e-9);
  assert.ok(Math.abs(rec.delta - -0.5) < 1e-9);
  const opus = rec.models.find((m) => m.model === 'opus-4-8');
  assert.ok(Math.abs(opus.delta - (12 - 10.5)) < 1e-9); // per-model uses ALL my events (10+2 vs 10.5)
  assert.equal(r.reconcile(my, null), null);       // ccusage unavailable
});

// --- billing model (Actual vs Est) — carried from v1 ---------------------

const fs = require('node:fs');
const os = require('node:os');
const pathMod = require('node:path');

function tmpConfig(contents) {
  const dir = fs.mkdtempSync(pathMod.join(os.tmpdir(), 'ccrepo-billing-'));
  const p = pathMod.join(dir, 'ccrepo-billing.json');
  fs.writeFileSync(p, contents);
  return p;
}
function quietErr(fn) {
  const orig = console.error; const msgs = [];
  console.error = (...a) => msgs.push(a.join(' '));
  try { return { result: fn(), msgs }; } finally { console.error = orig; }
}

test('loadBilling: absent ⇒ null; valid normalises; malformed ⇒ null + warning', () => {
  assert.equal(r.loadBilling(pathMod.join(os.tmpdir(), 'does-not-exist-ccrepo.json')), null);
  const b = r.loadBilling(tmpConfig(JSON.stringify({
    currency: 'usd', plan: { name: 'Max 20x', monthlyCost: 200, covers: ['Opus', 'SONNET'] }, perTokenModels: ['GPT-4'],
  })));
  assert.equal(b.currency, 'USD');
  assert.deepEqual(b.plan.covers, ['opus', 'sonnet']);
  assert.deepEqual(b.perTokenModels, ['gpt-4']);
  const noCost = quietErr(() => r.loadBilling(tmpConfig(JSON.stringify({ plan: { name: 'x' } }))));
  assert.equal(noCost.result, null);
  assert.match(noCost.msgs.join(' '), /monthlyCost > 0/);
});

test('coversPredicate: family-prefix match, perTokenModels carve-out, null off', () => {
  assert.equal(r.coversPredicate(null), null);
  const covers = r.coversPredicate({ plan: { covers: ['opus', 'sonnet'] }, perTokenModels: ['opus-4-8-special'] });
  assert.equal(covers('opus-4-8'), true);
  assert.equal(covers('gpt-4'), false);
  assert.equal(covers('opus-4-8-special'), false);
});

test('actualFor: uncovered cost + apportioned plan share (covered / total basis)', () => {
  const A = { coveredTokens: 300, uncoveredCost: 0, totalTokens: 300 };
  const B = { coveredTokens: 100, uncoveredCost: 5, totalTokens: 250 };
  const p = { monthlyCostUSD: 200, totalCovered: 400, totalAllTokens: 550 };
  assert.ok(Math.abs(r.actualFor(A, p) - 150) < 1e-9);
  assert.ok(Math.abs(r.actualFor(B, p) - 55) < 1e-9);
  const X = { coveredTokens: 0, uncoveredCost: 2, totalTokens: 100 };
  const q = { monthlyCostUSD: 200, totalCovered: 0, totalAllTokens: 400 };
  assert.ok(Math.abs(r.actualFor(X, q) - 52) < 1e-9);   // falls back to total-token share
});

// --- module-load safety (require must be inert) --------------------------

const { execFileSync } = require('node:child_process');
const path = require('node:path');

test('requiring ccrepo never acts on the host argv (help/validation live in main)', () => {
  const script = path.join(__dirname, 'ccrepo');
  for (const flags of [['-h'], ['-g', 'bogus-dim'], ['--json', '--csv']]) {
    const out = execFileSync('node',
      ['-e', 'require(process.argv[1]); console.log("host-alive")', script, ...flags],
      { encoding: 'utf8' });
    assert.equal(out.trim(), 'host-alive');
  }
});
