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
  // Per-model is scoped to the MATCHED sessions, same as the total: session 'c'
  // (my-only) is excluded, so opus is 10 vs 10.5 — not 12 vs 10.5. A one-sided
  // session is a scope gap (myOnly), never a phantom per-model delta.
  assert.ok(Math.abs(opus.delta - (10 - 10.5)) < 1e-9);
  const fable = rec.models.find((m) => m.model === 'fable-5');
  assert.ok(Math.abs(fable.delta - 0) < 1e-9);     // b matched both sides
  assert.equal(r.reconcile(my, null), null);       // ccusage unavailable
});

test('reconcile: a session only ccusage has is cuOnly, kept out of per-model', () => {
  const my = [{ session: 'a', model: 'opus-4-8', cost: 4 }];
  const ccu = [
    { period: 'a', totalCost: 4, modelBreakdowns: [{ modelName: 'claude-opus-4-8', cost: 4 }] },
    { period: 'z', totalCost: 99, modelBreakdowns: [{ modelName: 'claude-fable-5', cost: 99 }] }, // ccu-only
  ];
  const rec = r.reconcile(my, ccu);
  assert.equal(rec.matched, 1);
  assert.equal(rec.cuOnly, 1);
  // fable lives only in the unmatched 'z' → it must not appear as ccusage-side drift.
  assert.equal(rec.models.find((m) => m.model === 'fable-5'), undefined);
  const opus = rec.models.find((m) => m.model === 'opus-4-8');
  assert.ok(Math.abs(opus.delta - 0) < 1e-9);
});

// --- dedup: max-total-wins (keepRicher) ----------------------------------

test('keepRicher keeps the richest record per key; ordinary streams unaffected', () => {
  const ev = (total) => ({ total });
  // A duplicate (id,requestId) whose trailing line zeroes usage: last-wins would
  // take the 0 and undercount (the live sonnet-5 class); keepRicher holds the full
  // record. This is the whole per-model drift, recovered.
  const m1 = new Map();
  r.keepRicher(m1, 'k', ev(291340));   // complete line
  r.keepRicher(m1, 'k', ev(0));        // zeroed trailing duplicate
  assert.equal(m1.get('k').total, 291340);
  // Ascending stream (partial → complete): the final line already IS the max, so
  // keepRicher == last-wins here — no regression on the normal case.
  const m2 = new Map();
  r.keepRicher(m2, 'k', ev(10));
  r.keepRicher(m2, 'k', ev(100));      // final, complete
  assert.equal(m2.get('k').total, 100);
  // Order-independent: richest wins regardless of arrival order (unlike last/first).
  const m3 = new Map();
  r.keepRicher(m3, 'k', ev(100));
  r.keepRicher(m3, 'k', ev(40));       // partial arriving last
  assert.equal(m3.get('k').total, 100);
  // Distinct keys coexist; a missing total counts as 0.
  const m4 = new Map();
  r.keepRicher(m4, 'a', ev(5));
  r.keepRicher(m4, 'b', {});           // no total → 0, still stored (first for its key)
  assert.equal(m4.get('a').total, 5);
  assert.equal(m4.size, 2);
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
  assert.deepEqual(b.spend, { mode: 'plan', periods: {} });   // no spend block ⇒ plan-mode default
  const noCost = quietErr(() => r.loadBilling(tmpConfig(JSON.stringify({ plan: { name: 'x' } }))));
  assert.equal(noCost.result, null);
  assert.match(noCost.msgs.join(' '), /monthlyCost > 0/);
});

test('loadBilling: spend block normalises mode + periods, drops junk with a warning', () => {
  const good = r.loadBilling(tmpConfig(JSON.stringify({
    plan: { name: 'Max 5x', monthlyCost: 100 },
    spend: { mode: 'USAGE', periods: { '2026-06': 100, '2026-07': 137.2 } },
  })));
  assert.equal(good.spend.mode, 'usage');                     // case-folded
  assert.deepEqual(good.spend.periods, { '2026-06': 100, '2026-07': 137.2 });
  const junk = quietErr(() => r.loadBilling(tmpConfig(JSON.stringify({
    plan: { name: 'p', monthlyCost: 100 },
    spend: { mode: 'wat', periods: { '2026-07': 42, 'julyish': 9, '2026-08': -3 } },
  }))));
  assert.equal(junk.result.spend.mode, 'plan');               // bad mode ⇒ plan fallback
  assert.deepEqual(junk.result.spend.periods, { '2026-07': 42 }); // bad key + negative dropped
  assert.match(junk.msgs.join(' '), /expected 'plan' or 'usage'/);
  assert.match(junk.msgs.join(' '), /julyish/);
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

// --- actual spend vs estimate (reconcileSpend) --------------------------

// Synthetic events, only the fields reconcileSpend reads (ts, cost, uncoveredCost).
const spendEv = (ts, cost, uncoveredCost = 0) => ({ ts, cost, uncoveredCost });

test('reconcileSpend: null with no billing config', () => {
  assert.equal(r.reconcileSpend([spendEv('2026-07-15T12:00:00Z', 10)], null, {}), null);
});

test('reconcileSpend plan mode: billed = fee × distinct months + uncovered spend', () => {
  const events = [
    spendEv('2026-06-10T12:00:00Z', 40),
    spendEv('2026-07-05T12:00:00Z', 30, 6),   // 6 of this is uncovered per-token
    spendEv('2026-07-20T12:00:00Z', 20),
  ];
  const sr = r.reconcileSpend(events, { mode: 'plan', periods: {} },
    { monthlyCostUSD: 100, planName: 'Max 5x', periodsUSD: {} });
  assert.equal(sr.available, true);
  assert.equal(sr.mode, 'plan');
  assert.deepEqual(sr.months, ['2026-06', '2026-07']);
  assert.equal(sr.monthsCount, 2);
  assert.ok(Math.abs(sr.estimate - 90) < 1e-9);           // 40 + 30 + 20
  assert.ok(Math.abs(sr.uncovered - 6) < 1e-9);
  assert.ok(Math.abs(sr.billed - 206) < 1e-9);            // 100 × 2 months + 6 uncovered
  assert.ok(Math.abs(sr.delta - 116) < 1e-9);             // 206 − 90
  assert.ok(Math.abs(sr.pct - 116 / 90) < 1e-9);
});

test('reconcileSpend usage mode: billed = Σ invoiced figures for months in scope', () => {
  const events = [spendEv('2026-06-10T12:00:00Z', 40), spendEv('2026-07-05T12:00:00Z', 50)];
  const sr = r.reconcileSpend(events, { mode: 'usage', periods: {} },
    { monthlyCostUSD: 100, planName: 'Max 5x', periodsUSD: { '2026-06': 100, '2026-07': 137.2 } });
  assert.equal(sr.available, true);
  assert.deepEqual(sr.covered, ['2026-06', '2026-07']);
  assert.deepEqual(sr.gaps, []);
  assert.ok(Math.abs(sr.billed - 237.2) < 1e-9);
  assert.ok(Math.abs(sr.estimate - 90) < 1e-9);
  assert.ok(Math.abs(sr.delta - 147.2) < 1e-9);
});

test('reconcileSpend usage mode: a month with no figure is a stated gap, not smeared', () => {
  const events = [spendEv('2026-06-10T12:00:00Z', 40), spendEv('2026-07-05T12:00:00Z', 50)];
  const sr = r.reconcileSpend(events, { mode: 'usage', periods: {} },
    { periodsUSD: { '2026-06': 100 } });                  // July invoice missing
  assert.equal(sr.available, true);
  assert.deepEqual(sr.covered, ['2026-06']);
  assert.deepEqual(sr.gaps, ['2026-07']);
  assert.ok(Math.abs(sr.billed - 100) < 1e-9);            // only the covered month
});

test('reconcileSpend usage mode: unavailable when no month has an invoice figure', () => {
  const events = [spendEv('2026-07-05T12:00:00Z', 50)];
  const sr = r.reconcileSpend(events, { mode: 'usage', periods: {} }, { periodsUSD: {} });
  assert.equal(sr.available, false);
  assert.match(sr.reason, /no spend\.periods figure covers any month/);
  assert.ok(Math.abs(sr.estimate - 50) < 1e-9);           // estimate still reported
});

test('reconcileSpend: unavailable (never fabricates) when the range has no usage', () => {
  const planEmpty = r.reconcileSpend([], { mode: 'plan', periods: {} }, { monthlyCostUSD: 100 });
  assert.equal(planEmpty.available, false);
  assert.match(planEmpty.reason, /no usage in range/);
  const usageEmpty = r.reconcileSpend([], { mode: 'usage', periods: {} }, { periodsUSD: { '2026-07': 100 } });
  assert.equal(usageEmpty.available, false);
});

// --- reading the ccarchive mirror (--from-archive) -----------------------
// The disk walk isn't unit-covered (see HONEST SCOPE up top), so this drives the
// real CLI over a synthetic archive shaped exactly as ccarchive lays it out:
//   <dest>/<encoded-repo>/<uuid>.jsonl.gz
// The contract: ccrepo reads the gzip mirror and prices it like a live log, --dest
// alone implies --from-archive, ccusage is off (it can't see pruned history), and
// an evicted (dataless) mirror is skipped + counted through the same
// CCARCHIVE_SIMULATE_DATALESS seam ccarchive's own tests use. Tests stay offline:
// --fx usd (no FX fetch) + --no-billing (no config / no plan-currency fetch).

const zlib = require('node:zlib');
const CCREPO_UUID = 'a1b2c3d4-0000-4000-8000-000000000000';
// One assistant message, opus at clean round tokens: (1e6·5 + 1e6·25)/1e6 = $30.
const ARCHIVE_LOG = [
  JSON.stringify({ type: 'summary', cwd: '/home/dev/synthetic-ccrepo' }),
  JSON.stringify({
    type: 'assistant', sessionId: CCREPO_UUID, timestamp: '2026-05-01T12:00:00.000Z',
    requestId: 'req-1',
    message: { id: 'msg-1', model: 'claude-opus-4-8',
      usage: { input_tokens: 1000000, output_tokens: 1000000 } },
  }),
].join('\n') + '\n';

function makeCcrepoArchive() {
  const os2 = require('node:os');
  const dest = fs.mkdtempSync(pathMod.join(os2.tmpdir(), 'ccrepo-archive-'));
  const repoDir = pathMod.join(dest, '-home-dev-synthetic-ccrepo');
  fs.mkdirSync(repoDir, { recursive: true });
  fs.writeFileSync(pathMod.join(repoDir, `${CCREPO_UUID}.jsonl.gz`), zlib.gzipSync(ARCHIVE_LOG));
  return dest;
}
function runCcrepoJson(dest, extra = [], env = {}) {
  const script = pathMod.join(__dirname, 'ccrepo');
  // Isolate the rollup ledger to a throwaway temp file so archive-mode runs never
  // touch the real ~/.claude/ccrepo-rollup.json (and never cross-contaminate). A
  // caller that wants a specific ledger (the rollup tests) passes CCREPO_ROLLUP in.
  const ledger = env.CCREPO_ROLLUP
    || pathMod.join(fs.mkdtempSync(pathMod.join(os.tmpdir(), 'ccrepo-rollup-')), 'rollup.json');
  const out = require('node:child_process').execFileSync('node',
    [script, '--json', '--fx', 'usd', '--no-billing', ...extra], {
      encoding: 'utf8', env: { ...process.env, CCREPO_ROLLUP: ledger, ...env },
    });
  return JSON.parse(out);
}

test('contract: --from-archive prices a .gz mirror; ccusage cross-check is off', () => {
  const dest = makeCcrepoArchive();
  const j = runCcrepoJson(dest, ['--from-archive', '--dest', dest, '-g', 'repo']);
  assert.equal(j.meta.source, 'archive');
  assert.equal(j.meta.archiveRoot, dest);
  assert.equal(j.meta.evicted, 0);
  assert.equal(j.meta.reconciliation, null);         // ccusage off in archive mode
  const row = j.rows.find((x) => x.repo === 'synthetic-ccrepo');   // cwd recovered through gzip
  assert.ok(row, 'the archived repo is priced');
  assert.equal(row.totalTokens, 2000000);
  assert.ok(Math.abs(row.cost - 30) < 1e-9);         // $30 at usd (rate 1)
});

test('contract: --dest alone implies --from-archive', () => {
  const dest = makeCcrepoArchive();
  const j = runCcrepoJson(dest, ['--dest', dest, '-g', 'repo']);
  assert.equal(j.meta.source, 'archive');
  assert.ok(j.rows.some((x) => x.repo === 'synthetic-ccrepo'));
});

test('contract: an evicted mirror is skipped + counted, its spend not priced', () => {
  const dest = makeCcrepoArchive();
  const j = runCcrepoJson(dest, ['--from-archive', '--dest', dest, '-g', 'repo'],
    { CCARCHIVE_SIMULATE_DATALESS: CCREPO_UUID });
  assert.equal(j.meta.evicted, 1);
  assert.equal(j.rows.find((x) => x.repo === 'synthetic-ccrepo'), undefined); // not counted
  // --materialise opts back into reading it.
  const m = runCcrepoJson(dest, ['--from-archive', '--dest', dest, '--materialise', '-g', 'repo'],
    { CCARCHIVE_SIMULATE_DATALESS: CCREPO_UUID });
  assert.equal(m.meta.evicted, 0);
  assert.ok(m.rows.some((x) => x.repo === 'synthetic-ccrepo'));
});

test('readLogText gunzips a .gz and passes plain files through; isDatalessFlags bit', () => {
  const os2 = require('node:os');
  const dir = fs.mkdtempSync(pathMod.join(os2.tmpdir(), 'ccrepo-rlt-'));
  const plain = pathMod.join(dir, 'a.jsonl'), gz = pathMod.join(dir, 'a.jsonl.gz');
  fs.writeFileSync(plain, 'x\n'); fs.writeFileSync(gz, zlib.gzipSync('x\n'));
  assert.equal(r.readLogText(plain), 'x\n');
  assert.equal(r.readLogText(gz), 'x\n');
  assert.equal(r.isDatalessFlags(0x40000060), true);   // real evicted value
  assert.equal(r.isDatalessFlags(0x20), false);        // UF_COMPRESSED alone
  assert.equal(typeof r.defaultArchiveDest('/home/x'), 'string');
});

// --- rollup precompute ledger (the speed layer) --------------------------
// The rollup ledger caches each archive file's parsed, priced events under a
// (mtime,size) fingerprint so a warm --from-archive run gunzips only new files.
// The non-negotiable claim is rollup == full recompute: identical numbers with
// the cache on or off. These tests drive the real CLI over synthetic archives +
// an isolated temp ledger (CCREPO_ROLLUP), so they exercise the whole disk path
// the pure-function tests deliberately don't reach.

// The pure helpers first (cheap, deterministic).
test('recipeSig is stable under key order and reflects pricing + covers changes', () => {
  const a = r.recipeSig({ 'opus-4-8': 5, 'fable-5': 10 }, { covers: ['opus'], perTokenModels: [] });
  const b = r.recipeSig({ 'fable-5': 10, 'opus-4-8': 5 }, { perTokenModels: [], covers: ['opus'] });
  assert.equal(a, b, 'key order must not change the signature');
  assert.notEqual(a, r.recipeSig({ 'opus-4-8': 6, 'fable-5': 10 }, { covers: ['opus'], perTokenModels: [] })); // price moved
  assert.notEqual(a, r.recipeSig({ 'opus-4-8': 5, 'fable-5': 10 }, null));                                     // covers dropped
});

test('loadRollup: absent ⇒ fresh; wrong schema ⇒ fresh; malformed ⇒ fresh + warning', () => {
  const fresh = r.loadRollup(pathMod.join(os.tmpdir(), 'no-such-rollup-xyz.json'));
  assert.deepEqual(fresh, { schema: 'ccrepo-rollup/1', roots: {} });
  const dir = fs.mkdtempSync(pathMod.join(os.tmpdir(), 'ccrepo-rollup-u-'));
  const wrong = pathMod.join(dir, 'w.json'); fs.writeFileSync(wrong, JSON.stringify({ schema: 'other', roots: {} }));
  assert.deepEqual(r.loadRollup(wrong).roots, {});
  const bad = pathMod.join(dir, 'b.json'); fs.writeFileSync(bad, '{ not json');
  const q = quietErr(() => r.loadRollup(bad));
  assert.deepEqual(q.result, { schema: 'ccrepo-rollup/1', roots: {} });
  assert.match(q.msgs.join(' '), /rebuilding/);
});

// A richer multi-month, multi-session, multi-model archive so grouping is real.
function makeRolloutArchive() {
  const dest = fs.mkdtempSync(pathMod.join(os.tmpdir(), 'ccrepo-rollarch-'));
  const repoDir = pathMod.join(dest, '-home-dev-rollup-demo');
  fs.mkdirSync(repoDir, { recursive: true });
  const write = (uuid, ts, model, inTok, outTok) => {
    const log = [
      JSON.stringify({ type: 'summary', cwd: '/home/dev/rollup-demo' }),
      JSON.stringify({
        type: 'assistant', sessionId: uuid, timestamp: ts, requestId: 'req-' + uuid,
        message: { id: 'msg-' + uuid, model, usage: { input_tokens: inTok, output_tokens: outTok } },
      }),
    ].join('\n') + '\n';
    fs.writeFileSync(pathMod.join(repoDir, `${uuid}.jsonl.gz`), zlib.gzipSync(log));
  };
  // Two months, two models. opus base $5: (in·5 + out·25)/1e6; fable base $10.
  write('11111111-0000-4000-8000-000000000001', '2026-05-10T12:00:00.000Z', 'claude-opus-4-8', 1000000, 1000000); // $30
  write('22222222-0000-4000-8000-000000000002', '2026-05-20T12:00:00.000Z', 'claude-fable-5', 1000000, 0);        // $10
  write('33333333-0000-4000-8000-000000000003', '2026-06-05T12:00:00.000Z', 'claude-opus-4-8', 2000000, 0);       // $10
  return { dest, repoDir, write };
}
function tmpLedger() {
  return pathMod.join(fs.mkdtempSync(pathMod.join(os.tmpdir(), 'ccrepo-led-')), 'rollup.json');
}

test('FLOOR: rollup == full recompute — identical rows/total with the cache on vs off', () => {
  const { dest } = makeRolloutArchive();
  const args = ['--from-archive', '--dest', dest, '-g', 'month,model'];
  const off = runCcrepoJson(dest, [...args, '--no-rollup']);        // full re-walk, no cache
  const cold = runCcrepoJson(dest, args, { CCREPO_ROLLUP: tmpLedger() }); // cache built this run
  // Same ledger reused: a genuinely warm run (every file a hit).
  const led = tmpLedger();
  runCcrepoJson(dest, args, { CCREPO_ROLLUP: led });                // populate
  const warm = runCcrepoJson(dest, args, { CCREPO_ROLLUP: led });   // all-hits
  assert.deepEqual(cold.rows, off.rows, 'cold cache run must equal the uncached recompute');
  assert.deepEqual(warm.rows, off.rows, 'warm cache run must equal the uncached recompute');
  // The three sessions: $30 + $10 + $10 = $50 total, exact.
  const total = off.rows.reduce((s, x) => s + x.cost, 0);
  assert.ok(Math.abs(total - 50) < 1e-9, `expected $50, got ${total}`);
  assert.equal(warm.meta.rollup.hits, 3);
  assert.equal(warm.meta.rollup.misses, 0);                        // warm: nothing re-read
});

test('cache hit: a warm run serves the ledger, not the disk (fingerprint unchanged)', () => {
  const { dest } = makeRolloutArchive();
  const led = tmpLedger();
  const args = ['--from-archive', '--dest', dest, '-g', 'total'];
  const cold = runCcrepoJson(dest, args, { CCREPO_ROLLUP: led });
  assert.equal(cold.meta.rollup.misses, 3);                         // first run reads all three
  // Tamper the CACHE (not the source): halve one file's stored token/cost. A hit
  // path must surface the tampered value; a disk read would ignore it. This is the
  // cleanest hit proof — same (mtime,size) ⇒ the ledger is trusted verbatim.
  const ledger = JSON.parse(fs.readFileSync(led, 'utf8'));
  const root = ledger.roots[dest];
  const anyFile = Object.values(root.files)[0];
  anyFile.events[0].cost = 999;                                    // sentinel only the cache carries
  fs.writeFileSync(led, JSON.stringify(ledger));
  const warm = runCcrepoJson(dest, args, { CCREPO_ROLLUP: led });
  assert.equal(warm.meta.rollup.hits, 3);
  assert.equal(warm.meta.rollup.misses, 0);
  const total = warm.rows[0].cost;
  assert.ok(total > 900, `sentinel from the cache must show through (got ${total})`);
});

test('invalidation: a stale file is re-read when its fingerprint changes', () => {
  const { dest, write } = makeRolloutArchive();
  const led = tmpLedger();
  const args = ['--from-archive', '--dest', dest, '-g', 'total'];
  runCcrepoJson(dest, args, { CCREPO_ROLLUP: led });               // populate
  // Tamper the cache with a sentinel, THEN rewrite the source file with different
  // content (so mtime+size move). The fingerprint mismatch must force a re-read,
  // discarding the sentinel and restoring the true number.
  const ledger = JSON.parse(fs.readFileSync(led, 'utf8'));
  Object.values(ledger.roots[dest].files)[0].events[0].cost = 999;
  fs.writeFileSync(led, JSON.stringify(ledger));
  write('11111111-0000-4000-8000-000000000001', '2026-05-10T12:00:00.000Z', 'claude-opus-4-8', 1000000, 1000000); // same numbers, new bytes/mtime
  const after = runCcrepoJson(dest, args, { CCREPO_ROLLUP: led });
  assert.ok(after.meta.rollup.misses >= 1, 'the rewritten file must miss and be re-read');
  assert.ok(Math.abs(after.rows[0].cost - 50) < 1e-9, 'true $50 restored, sentinel discarded');
});

test('invalidation: a NEW file landing under a period recomputes that period', () => {
  const { dest, write } = makeRolloutArchive();
  const led = tmpLedger();
  const args = ['--from-archive', '--dest', dest, '-g', 'month'];
  const before = runCcrepoJson(dest, args, { CCREPO_ROLLUP: led });
  const may0 = before.rows.find((x) => x.month === '2026-05').cost;
  assert.ok(Math.abs(may0 - 40) < 1e-9, `May starts at $40 (opus $30 + fable $10), got ${may0}`);
  // A new May session lands ($30 opus). Old files stay hits; the new one is a miss.
  write('44444444-0000-4000-8000-000000000004', '2026-05-25T12:00:00.000Z', 'claude-opus-4-8', 1000000, 1000000);
  const after = runCcrepoJson(dest, args, { CCREPO_ROLLUP: led });
  assert.equal(after.meta.rollup.hits, 3, 'the three original files are served from cache');
  assert.equal(after.meta.rollup.misses, 1, 'only the new file is read');
  const may1 = after.rows.find((x) => x.month === '2026-05').cost;
  assert.ok(Math.abs(may1 - 70) < 1e-9, `May must grow to $70 after the new session, got ${may1}`);
});

test('recipe-signature mismatch (e.g. a price table move) rebuilds the whole ledger', () => {
  const { dest } = makeRolloutArchive();
  const led = tmpLedger();
  const args = ['--from-archive', '--dest', dest, '-g', 'total'];
  runCcrepoJson(dest, args, { CCREPO_ROLLUP: led });               // built → $50, sig recorded
  // The baked cost/covered split depends on the price table + covers-list, folded
  // into the root's recipe signature. Simulate either of them moving by staling the
  // stored sig, and plant a sentinel cost. A signature mismatch must rebuild the
  // whole root (every file a miss), discarding the sentinel — never serve a cost
  // computed under the old recipe.
  const ledger = JSON.parse(fs.readFileSync(led, 'utf8'));
  ledger.roots[dest].sig = 'stale-recipe-signature';
  Object.values(ledger.roots[dest].files)[0].events[0].cost = 999;
  fs.writeFileSync(led, JSON.stringify(ledger));
  const after = runCcrepoJson(dest, args, { CCREPO_ROLLUP: led });
  assert.equal(after.meta.rollup.misses, 3, 'a recipe mismatch forces a full re-read');
  assert.equal(after.meta.rollup.hits, 0);
  assert.ok(Math.abs(after.rows[0].cost - 50) < 1e-9, `true $50 restored, stale sentinel discarded (got ${after.rows[0].cost})`);
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

// --- documentation convention (REPO-STANDARD: concise --help + a man page) --

const SCRIPT = path.join(__dirname, 'ccrepo');

test('--help is a concise digest that points at the man page', () => {
  const help = execFileSync('node', [SCRIPT, '-h'], { encoding: 'utf8' });
  assert.ok(help.split('\n').length <= 40, '--help should stay a one-screen digest');
  assert.match(help, /man ccrepo/, '--help must point at the full manual');
  // Rationale + worked examples belong in the page, not the digest.
  assert.ok(!/^EXAMPLES$/m.test(help), '--help must not carry a worked EXAMPLES block');
  for (const opt of ['-g', '--repo', '--json', '--no-reconcile']) assert.ok(help.includes(opt));
});

test('a man page ships and is well-formed roff', () => {
  const page = path.join(__dirname, 'man', 'ccrepo.1');
  assert.ok(fs.existsSync(page), 'instruments/man/ccrepo.1 must exist');
  const roff = fs.readFileSync(page, 'utf8');
  assert.match(roff, /^\.TH CCREPO 1 /m, 'a .TH title line');
  for (const sec of ['NAME', 'SYNOPSIS', 'DESCRIPTION', 'OPTIONS', 'EXAMPLES', 'EXIT STATUS', 'SEE ALSO']) {
    assert.match(roff, new RegExp(`^\\.SH ${sec}`, 'm'), `a ${sec} section`);
  }
});

test('drift guard: every flag --help prints appears in the man page (superset relation)', () => {
  const help = execFileSync('node', [SCRIPT, '-h'], { encoding: 'utf8' });
  const page = fs.readFileSync(path.join(__dirname, 'man', 'ccrepo.1'), 'utf8');
  // Roff hyphenates flags as \-\-flag; normalise the page before matching.
  const pageFlat = page.replace(/\\-/g, '-');
  const flags = [...new Set(help.match(/--[\w-]+/g))];
  assert.ok(flags.length >= 15, `expected a real flag list, got ${flags.length}`);
  for (const flag of flags) {
    assert.ok(pageFlat.includes(flag), `man page must document ${flag} (--help is the digest, the page the superset)`);
  }
});
