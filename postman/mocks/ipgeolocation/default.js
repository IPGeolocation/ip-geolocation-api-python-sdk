const http = require('node:http');

http.createServer((req, res) => {
  const url = new URL(req.url, 'http://localhost');
  const reply = (status, body) => {
    res.writeHead(status, {
      'Content-Type': 'application/json',
      'X-Credits-Charged': '1',
      'X-Successful-Records': '1',
    });
    res.end(JSON.stringify(body));
  };
  if (!['/v3/ipgeo', '/v3/ipgeo-bulk'].includes(url.pathname)) {
    return reply(501, { message: 'Endpoint not modeled' });
  }
  const bulk = url.pathname === '/v3/ipgeo-bulk';
  if (req.method !== (bulk ? 'POST' : 'GET')) {
    return reply(400, { message: 'Unexpected HTTP method' });
  }
  const key = url.searchParams.get('apiKey');
  const statuses = { BAD_KEY: 401, FORBIDDEN: 403, RATE_LIMIT: 429, SERVER_ERROR: 503 };
  if (statuses[key]) return reply(statuses[key], { message: `Test failure for ${key}` });
  if (key === 'BAD_JSON') { res.writeHead(200); return res.end('{'); }
  if (key === 'BAD_ENCODING') {
    res.writeHead(200, { 'Content-Type': 'application/json; charset=unknown-encoding' });
    return res.end(JSON.stringify({ ip: '8.8.8.8', location: { city: '東京' } }));
  }
  if (key === 'LARGE_RESPONSE') {
    return reply(200, { ip: '8.8.8.8', location: { city: '東京'.repeat(2000) } });
  }
  if (key === 'SLOW_REQUEST') {
    return setTimeout(() => reply(200, { ip: '8.8.8.8' }), 300);
  }
  if (key !== 'TEST_KEY &+?=#%' && !(key === null && req.headers.origin === 'https://app.example.test')) {
    return reply(401, { message: 'Invalid test key' });
  }
  if (bulk && (req.headers['content-type'] !== 'application/json' || !Array.isArray(req.body?.ips))) {
    return reply(400, { message: 'Expected JSON ips array' });
  }
  const result = {
    ip: bulk ? req.body.ips[0] : url.searchParams.get('ip'),
    location: { city: 'Test City' },
    _request: {
      method: req.method,
      query: Object.fromEntries(url.searchParams),
      headers: req.headers,
      body: bulk ? req.body : null,
    },
  };
  reply(200, bulk ? [result, { message: 'IP address not found' }] : result);
}).listen(process.env.PORT || 4500);
