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
  assert.equal(r.priceBase('opus-5'), 5);
  assert.equal(r.priceBase('opus-4-8'), 5);
  // 'opus-5' must not swallow 'opus-4-8' (or vice versa) — they're siblings, not
  // prefixes of each other, and both must resolve to their own entry.
  assert.equal(r.priceBase('opus-4-7'), null, 'an unlisted opus stays unpriced, not silently $5');
  assert.equal(r.priceBase('fable-5'), 10);
  assert.equal(r.priceBase('sonnet-4-6'), 3);   // 'sonnet-4' beats 'sonnet-5' by prefix
  assert.equal(r.priceBase('haiku-4-5-20251001'), 1);
  assert.equal(r.priceBase('gpt-4'), null);
  assert.equal(r.priceBase('<synthetic>'), null);
});

test('a bare number still means "always" — the pre-interval form keeps working', () => {
  // The compatibility guarantee, stated as a test: every entry that was a plain
  // number before time-bounding must resolve identically with or without a
  // timestamp. If this breaks, every existing ccrepo-pricing.json breaks with it.
  for (const ts of [undefined, '2020-01-01T00:00:00.000Z', '2099-12-31T23:59:59.000Z']) {
    assert.equal(r.priceBase('opus-5', null, ts), 5);
    assert.equal(r.priceBase('haiku-4-5-20251001', null, ts), 1);
  }
});

test('a time-bounded price resolves at the message timestamp, both sides of the date', () => {
  // sonnet-5 ships as two intervals: $2 through 2026-08-31, $3 from 2026-09-01.
  assert.equal(r.priceBase('sonnet-5', null, '2026-07-26T07:00:00.000Z'), 2, 'intro rate before the boundary');
  assert.equal(r.priceBase('sonnet-5', null, '2026-08-31T23:59:59.000Z'), 2, 'the "to" bound is inclusive');
  assert.equal(r.priceBase('sonnet-5', null, '2026-09-01T00:00:00.000Z'), 3, 'the "from" bound is inclusive');
  assert.equal(r.priceBase('sonnet-5', null, '2027-05-05T00:00:00.000Z'), 3, 'open-ended at the far end');
  // The boundary is the UTC *date*, and the stamps are Z — no local-day guess.
  assert.equal(r.priceBase('sonnet-5', null, '2026-08-31T11:30:00.000Z'), 2);
});

test('a date inside no interval is unpriced, never snapped to the nearest one', () => {
  const table = { 'gap-1': [{ from: '2026-01-01', to: '2026-01-31', base: 7 }] };
  assert.equal(r.priceBase('gap-1', table, '2026-01-15T00:00:00.000Z'), 7);
  assert.equal(r.priceBase('gap-1', table, '2025-12-31T00:00:00.000Z'), null, 'before the first interval');
  assert.equal(r.priceBase('gap-1', table, '2026-02-01T00:00:00.000Z'), null, 'after the last interval');
  // No timestamp against a dated entry is also unpriced: an undated lookup can't
  // be answered from a table that varies by date, and answering it with "today"
  // would reintroduce the bug the intervals exist to fix.
  assert.equal(r.priceBase('gap-1', table, undefined), null);
  // ...and the message cost follows it down the unknown-model path, not to a guess.
  assert.deepEqual(r.messageCost('gap-1', { input: 1e6 }, table, '2026-02-01T00:00:00.000Z'),
    { cost: 0, priced: false });
});

test('priceEntry separates "no such model" from "no price on that date"', () => {
  // The two gaps need different fixes, so the footnote has to tell them apart.
  const table = { 'gap-1': [{ from: '2026-01-01', to: '2026-01-31', base: 7 }] };
  assert.notEqual(r.priceEntry('gap-1', table), null, 'the model is in the table');
  assert.equal(r.priceEntry('nope-9', table), null, 'the model is not');
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

test('an override may be a list of intervals; a malformed entry loses only itself', () => {
  const fs = require('node:fs'), os = require('node:os'), p = require('node:path');
  const dir = fs.mkdtempSync(p.join(os.tmpdir(), 'ccrepo-price-iv-'));
  const f = p.join(dir, 'iv.json');
  fs.writeFileSync(f, JSON.stringify({
    'opus-4-8': [{ to: '2026-06-30', base: 4 }, { from: '2026-07-01', base: 6 }],
    'bad-dates': [{ from: 'June 2026', base: 9 }],   // not an ISO date
    'bad-base': [{ from: '2026-01-01', base: 0 }],   // not a positive number
    'empty-list': [],
    'haiku-4-5': 2,                                   // a plain number alongside
  }));
  const orig = console.error; const warned = []; console.error = (m) => warned.push(String(m));
  let merged; try { merged = r.loadPricing(f); } finally { console.error = orig; }
  assert.equal(r.priceBase('opus-4-8', merged, '2026-06-30T00:00:00.000Z'), 4);
  assert.equal(r.priceBase('opus-4-8', merged, '2026-07-01T00:00:00.000Z'), 6);
  assert.equal(r.priceBase('haiku-4-5', merged, '2026-07-01T00:00:00.000Z'), 2);
  // One bad entry must not sink the file — the other five corrections survive.
  assert.equal(r.priceEntry('bad-dates', merged), null);
  assert.equal(r.priceEntry('bad-base', merged), null);
  assert.equal(r.priceEntry('empty-list', merged), null);
  assert.equal(warned.length, 3, 'each dropped entry is named, not swallowed');
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
  // Context = everything SENT (input + cache read + cache create), output excluded:
  // output isn't in the window the request was served against. 100 + 1000 + 100.
  assert.equal(e.context, 1200);
  assert.notEqual(e.context, e.totalTokens);   // and so is never just the token total
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

// --- context size (per-session peak windows) -----------------------------

test('quantile interpolates linearly; median is the average of the two middles', () => {
  const s = [10, 20, 30, 40];
  assert.equal(r.quantile(s, 0), 10);
  assert.equal(r.quantile(s, 1), 40);
  assert.equal(r.quantile(s, 0.5), 25);            // (20+30)/2, not a bare middle pick
  assert.equal(r.quantile([10, 20, 30], 0.5), 20); // odd length → the true middle
  assert.equal(r.quantile(s, 0.25), 17.5);         // interpolated, not step-wise
  assert.equal(r.quantile([], 0.5), null);
});

test('bumpPeak keeps the high-water mark per session, never a sum', () => {
  const m = new Map();
  r.bumpPeak(m, 's1', 100);
  r.bumpPeak(m, 's1', 500);
  r.bumpPeak(m, 's1', 200);   // a later, smaller window must not lower the peak…
  assert.equal(m.get('s1'), 500);
  assert.equal(m.size, 1);    // …nor add a second entry (Sessions stays a distinct count)
  r.bumpPeak(m, 's2', undefined);
  assert.equal(m.get('s2'), 0);  // a missing context is 0, not NaN/undefined
});

test('contextStats summarises session peaks; empty and all-zero report null', () => {
  const st = r.contextStats(new Map([['a', 100], ['b', 200], ['c', 300], ['d', 400]]));
  assert.equal(st.sessions, 4);
  assert.equal(st.min, 100);
  assert.equal(st.median, 250);
  assert.equal(st.max, 400);
  assert.equal(st.mean, 250);
  // A slice whose messages carried no usage record reports nothing, not a fake 0.
  for (const empty of [new Map(), new Map([['a', 0], ['b', 0]])]) {
    const z = r.contextStats(empty);
    assert.equal(z.sessions, 0);
    assert.equal(z.median, null);
    assert.equal(z.max, null);
  }
  // Zero-peak sessions are excluded from the stats, not counted as tiny sessions.
  assert.equal(r.contextStats(new Map([['a', 0], ['b', 400]])).sessions, 1);
  assert.equal(r.contextStats(new Map([['a', 0], ['b', 400]])).min, 400);
});

test('groupTree tracks context as peaks-of-peaks, never a sum', () => {
  const evs = [
    mkEv({ repo: 'A', session: 's1', context: 100 }),
    mkEv({ repo: 'A', session: 's1', context: 900 }),  // same session, bigger window
    mkEv({ repo: 'A', session: 's2', context: 300 }),
    mkEv({ repo: 'B', session: 's3', context: 500 }),
  ];
  const root = r.groupTree(evs, ['repo']);
  const A = root.children.get('A');
  // s1's four messages carry 1000 tokens of context between them, but the session
  // only ever held 900 — summing would invent a window that never existed.
  assert.equal(A.sessions.get('s1'), 900);
  assert.equal(r.contextStats(A.sessions).max, 900);
  assert.equal(r.contextStats(A.sessions).median, 600);   // peaks 300 and 900
  assert.equal(A.sessions.size, 2);                       // Sessions count unaffected
  // The root is the max across groups, not the sum of them.
  assert.equal(r.contextStats(root.sessions).max, 900);
  assert.equal(r.contextStats(root.sessions).sessions, 3);
});

test('a session split across groups keeps a real peak in each slice', () => {
  // One session that ran on two branches: each slice reports the largest window
  // reached *while on that branch*, which is what a per-branch reading means.
  const evs = [
    mkEv({ session: 's1', branch: 'main', context: 100 }),
    mkEv({ session: 's1', branch: 'feature', context: 800 }),
  ];
  const root = r.groupTree(evs, ['branch']);
  assert.equal(r.contextStats(root.children.get('main').sessions).max, 100);
  assert.equal(r.contextStats(root.children.get('feature').sessions).max, 800);
  assert.equal(root.sessions.size, 1);                    // still one distinct session
  assert.equal(r.contextStats(root.sessions).max, 800);   // whose true peak is 800
});

test('fmtTokens scales; non-positive and non-finite are null, not "0"', () => {
  assert.equal(r.fmtTokens(934000), '934k');
  assert.equal(r.fmtTokens(1_250_000), '1.3M');
  assert.equal(r.fmtTokens(1500), '1.5k');
  assert.equal(r.fmtTokens(950), '950');
  assert.equal(r.fmtTokens(0), null);
  assert.equal(r.fmtTokens(NaN), null);
});

// --- --context: session-grain filter (ROADMAP ccrepo v3 ask 2) -----------

test('parseContextAmount: k/m suffixes, decimals, case-insensitive, rejects junk', () => {
  assert.equal(r.parseContextAmount('100'), 100);
  assert.equal(r.parseContextAmount('100k'), 100000);
  assert.equal(r.parseContextAmount('100K'), 100000);
  assert.equal(r.parseContextAmount('1.5m'), 1500000);
  assert.equal(r.parseContextAmount('1.5M'), 1500000);
  assert.equal(r.parseContextAmount('0'), 0);
  assert.equal(r.parseContextAmount(''), null);
  assert.equal(r.parseContextAmount('abc'), null);
  assert.equal(r.parseContextAmount('100kb'), null);
  assert.equal(r.parseContextAmount('-100k'), null);   // a bare amount is never negative
});

test('parseContextRange: MIN-MAX, MIN-, -MAX, k/m suffixes', () => {
  assert.deepEqual(r.parseContextRange('100k-500k'), { min: 100000, max: 500000 });
  assert.deepEqual(r.parseContextRange('400k-'), { min: 400000, max: null });
  assert.deepEqual(r.parseContextRange('-100k'), { min: null, max: 100000 });
  assert.deepEqual(r.parseContextRange('500000-1000000'), { min: 500000, max: 1000000 });
  assert.deepEqual(r.parseContextRange('1m-'), { min: 1000000, max: null });
});

test('parseContextRange: a malformed spec is REJECTED with a clear error, never matches everything', () => {
  // No dash at all — ambiguous, refused rather than guessed.
  assert.ok(r.parseContextRange('500k').error);
  // Neither bound present.
  assert.ok(r.parseContextRange('-').error);
  // An unparsable bound on either side.
  assert.ok(r.parseContextRange('abc-500k').error);
  assert.ok(r.parseContextRange('100k-abc').error);
  // Lower bound exceeds upper bound.
  assert.ok(r.parseContextRange('500k-100k').error);
  // Every error is a human-readable string, not a blank/undefined message.
  for (const bad of ['500k', '-', 'abc-500k', '100k-abc', '500k-100k']) {
    assert.equal(typeof r.parseContextRange(bad).error, 'string');
    assert.ok(r.parseContextRange(bad).error.length > 10);
  }
});

test('sessionPeaks + buildContextFilter: SESSION-grain, not message-grain', () => {
  // Two sessions: s1 ramps 100 → 900 (peak 900), s2 sits flat at 300. A range
  // that only 's1 at its peak' falls in must admit EVERY message of s1 —
  // including its early, low-context messages — and exclude s2 entirely. A
  // message-grain filter would instead admit s1's 100-context message under a
  // low band too, which is exactly the near-meaningless reading the design
  // rules out.
  const evs = [
    mkEv({ session: 's1', context: 100 }),
    mkEv({ session: 's1', context: 900 }),
    mkEv({ session: 's2', context: 300 }),
  ];
  const peaks = r.sessionPeaks(evs);
  assert.equal(peaks.get('s1'), 900);
  assert.equal(peaks.get('s2'), 300);
  const high = r.buildContextFilter({ min: 500, max: null }, peaks); // peak >= 500
  assert.deepEqual(evs.filter(high).map((e) => e.context), [100, 900]);   // BOTH of s1's messages
  const mid = r.buildContextFilter({ min: 200, max: 400 }, peaks);
  assert.deepEqual(evs.filter(mid).map((e) => e.session), ['s2']);
  // No range ⇒ everything passes.
  assert.equal(evs.filter(r.buildContextFilter(null, peaks)).length, 3);
});

test('contract: --context filters sessions by peak (session-grain), not messages, and pairs with -g session', () => {
  const dest = makeCcrepoArchive();   // one session, one message, 1e6-token context
  const inBand = runCcrepoJson(dest, ['--from-archive', '--dest', dest, '-g', 'session', '--context', '500k-']);
  assert.equal(inBand.rows.length, 1);
  const outOfBand = runCcrepoJson(dest, ['--from-archive', '--dest', dest, '-g', 'session', '--context', '-500k']);
  assert.equal(outOfBand.rows.length, 0);
  assert.equal(outOfBand.meta.total.sessions, 0, 'TOTAL also reflects the filtered scope, same as any other filter');
  assert.equal(inBand.meta.filters.context, '500k-');
});

test('contract: a malformed --context exits 2 with a clear error, not a silent match-everything run', () => {
  const dest = makeCcrepoArchive();
  const script = pathMod.join(__dirname, 'ccrepo');
  assert.throws(() => {
    require('node:child_process').execFileSync('node',
      [script, '--from-archive', '--dest', dest, '--context', 'nonsense', '--fx', 'usd', '--no-billing'],
      { encoding: 'utf8', stdio: ['ignore', 'pipe', 'pipe'] });
  }, /Command failed/);
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

test('contract: -g session groups on the full UUID and machine output keeps it whole', () => {
  const dest = makeCcrepoArchive();
  const j = runCcrepoJson(dest, ['--from-archive', '--dest', dest, '-g', 'session']);
  assert.equal(j.rows.length, 1);
  const id = j.rows[0].session;
  // The key is the whole id. The human table shows an 8-char prefix, but --json
  // must carry something you can paste back into --session and look up.
  assert.ok(id && id.length > 8, `expected a full session id, got ${JSON.stringify(id)}`);
  // Same numbers as grouping by repo — a new dimension must not move the totals.
  const byRepo = runCcrepoJson(dest, ['--from-archive', '--dest', dest, '-g', 'repo']);
  assert.equal(j.rows[0].totalTokens, byRepo.rows.find((x) => x.repo === 'synthetic-ccrepo').totalTokens);
  // And the dimension is filterable by the same prefix it groups by (one getter).
  const filtered = runCcrepoJson(dest,
    ['--from-archive', '--dest', dest, '-g', 'session', '--session', id.slice(0, 8)]);
  assert.equal(filtered.rows.length, 1);
  assert.equal(filtered.rows[0].session, id);
});

test('contract: --json/--csv carry the whole context distribution, not just med/max', () => {
  const dest = makeCcrepoArchive();
  const j = runCcrepoJson(dest, ['--from-archive', '--dest', dest, '-g', 'repo']);
  const row = j.rows.find((x) => x.repo === 'synthetic-ccrepo');
  // The log's one message: 1e6 input, 1e6 output, no cache. Context is what was
  // SENT — 1e6 — so it is deliberately NOT the 2e6 token total.
  assert.equal(row.contextMax, 1000000);
  assert.equal(row.contextMedian, 1000000);
  assert.equal(row.totalTokens, 2000000);
  // Everything a consumer could want, even where no terminal column fits it.
  for (const k of ['contextSessions', 'contextMin', 'contextP25', 'contextMedian',
    'contextP75', 'contextP90', 'contextMax', 'contextMean']) {
    assert.ok(k in row, `${k} missing from the tidy row`);
  }
  // The grand total ships in meta: peaks-of-peaks can't be re-aggregated from
  // leaves once sessions are split across groups, so a machine can't derive it.
  assert.equal(j.meta.total.contextMax, 1000000);
  assert.equal(j.meta.total.sessions, 1);
});

test('contract: the rollup schema bump discards a ledger written before `context`', () => {
  // A pre-/2 ledger's cached events have no `context` field. The (mtime,size)
  // fingerprint would pass, so without the schema check they'd be served as valid
  // and every warm archive run would report a confident 0 context, forever.
  const dest = makeCcrepoArchive();
  const led = pathMod.join(fs.mkdtempSync(pathMod.join(os.tmpdir(), 'ccrepo-oldled-')), 'rollup.json');
  const args = ['--from-archive', '--dest', dest, '-g', 'repo'];
  runCcrepoJson(dest, args, { CCREPO_ROLLUP: led });                 // populate at the current schema
  const ledger = JSON.parse(fs.readFileSync(led, 'utf8'));
  assert.equal(ledger.schema, 'ccrepo-rollup/2');
  // Rewind it to the old schema, stripping `context` exactly as a v1 ledger lacked it.
  ledger.schema = 'ccrepo-rollup/1';
  for (const root of Object.values(ledger.roots)) {
    for (const f of Object.values(root.files)) for (const e of f.events) delete e.context;
  }
  fs.writeFileSync(led, JSON.stringify(ledger));
  const after = runCcrepoJson(dest, args, { CCREPO_ROLLUP: led });
  assert.equal(after.meta.rollup.misses, 1, 'the stale-schema ledger must be re-read, not trusted');
  assert.equal(after.meta.rollup.hits, 0);
  assert.equal(after.rows.find((x) => x.repo === 'synthetic-ccrepo').contextMax, 1000000);
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
test('contract: time-bounding a price invalidates the rollup ledger by itself', () => {
  // The roadmap flagged this to *verify, not assume*: cached events bake their
  // cost, so if turning a flat price into intervals didn't change the recipe
  // signature, every warm archive run would keep serving the old dollar figure —
  // confidently, and forever. It does not need a ROLLUP_SCHEMA bump, because the
  // event *shape* is unchanged (cost is still a number); the signature covers
  // changed *values*, which is what this is. Proven in two halves.
  //
  // Half one: the signature genuinely moves when a flat entry becomes intervals.
  const flat = { 'sonnet-5': 2 };
  const timed = { 'sonnet-5': [{ to: '2026-08-31', base: 2 }, { from: '2026-09-01', base: 3 }] };
  const covers = { covers: ['opus'], perTokenModels: [] };
  assert.notEqual(r.recipeSig(flat, covers), r.recipeSig(timed, covers),
    'flat and time-bounded tables must not sign the same');
  // ...even when today's effective price is identical, because tomorrow's isn't.
  assert.notEqual(r.recipeSig(flat, covers), r.recipeSig({ 'sonnet-5': [{ base: 2 }] }, covers));
  // Half two — that a moved signature rebuilds the root rather than serving the
  // baked cost — is already pinned, with a sentinel cost, by
  // 'recipe-signature mismatch (e.g. a price table move) rebuilds the whole
  // ledger' below. The two halves together are the whole chain; this test adds
  // only the link that was previously untested.
});

test('recipeSig is stable under key order and reflects pricing + covers changes', () => {
  const a = r.recipeSig({ 'opus-4-8': 5, 'fable-5': 10 }, { covers: ['opus'], perTokenModels: [] });
  const b = r.recipeSig({ 'fable-5': 10, 'opus-4-8': 5 }, { perTokenModels: [], covers: ['opus'] });
  assert.equal(a, b, 'key order must not change the signature');
  assert.notEqual(a, r.recipeSig({ 'opus-4-8': 6, 'fable-5': 10 }, { covers: ['opus'], perTokenModels: [] })); // price moved
  assert.notEqual(a, r.recipeSig({ 'opus-4-8': 5, 'fable-5': 10 }, null));                                     // covers dropped
});

test('loadRollup: absent ⇒ fresh; wrong schema ⇒ fresh; malformed ⇒ fresh + warning', () => {
  const fresh = r.loadRollup(pathMod.join(os.tmpdir(), 'no-such-rollup-xyz.json'));
  assert.deepEqual(fresh, { schema: 'ccrepo-rollup/2', roots: {} });
  const dir = fs.mkdtempSync(pathMod.join(os.tmpdir(), 'ccrepo-rollup-u-'));
  const wrong = pathMod.join(dir, 'w.json'); fs.writeFileSync(wrong, JSON.stringify({ schema: 'other', roots: {} }));
  assert.deepEqual(r.loadRollup(wrong).roots, {});
  const bad = pathMod.join(dir, 'b.json'); fs.writeFileSync(bad, '{ not json');
  const q = quietErr(() => r.loadRollup(bad));
  assert.deepEqual(q.result, { schema: 'ccrepo-rollup/2', roots: {} });
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

// Interim bump (was 40): --context (ROADMAP ccrepo v3 ask 2) adds one flag
// line to the still-flat OPTIONS block. Ask 5 resections the whole surface
// and rebases this guard on a fully-grounded figure at that point — this
// interim number is exactly old-budget + 1 new line, not a fitted afterthought.
const HELP_LINE_BUDGET = 41;

test('--help is a concise digest that points at the man page', () => {
  const help = execFileSync('node', [SCRIPT, '-h'], { encoding: 'utf8' });
  assert.ok(help.split('\n').length <= HELP_LINE_BUDGET,
    `--help should stay within its grounded line budget (${HELP_LINE_BUDGET})`);
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
