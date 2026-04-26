## Anti-Patterns

**❌ Hardcoding credentials:** `const apiKey = 'sk_live_abc123'`  
**✅** `npx wrangler secret put API_KEY`

**❌ Using REST API:** `fetch('https://api.cloudflare.com/.../kv/...')`  
**✅** `env.MY_KV.get('key')`

**❌ Polling storage:** `setInterval(() => env.KV.get('config'), 1000)`  
**✅** Use Durable Objects for real-time state

**❌ Large data in vars:** `{ "vars": { "HUGE_CONFIG": "..." } }` (5KB max)  
**✅** `env.MY_KV.put('config', data)`

**❌ Caching env globally:** `const apiKey = env.API_KEY` outside fetch()  
**✅** Access `env.API_KEY` per-request inside fetch()

