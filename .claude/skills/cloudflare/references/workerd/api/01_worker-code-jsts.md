## Worker Code (JS/TS)

### ES Modules (Recommended)
```javascript
export default {
  async fetch(request, env, ctx) {
    const value = await env.KV.get("key");           // Bindings in env
    const response = await env.API.fetch(request);   // Service binding
    ctx.waitUntil(logRequest(request));              // Background task
    return new Response("OK");
  },
  async adminApi(request, env, ctx) { /* Named entrypoint */ },
  async queue(batch, env, ctx) { /* Queue consumer */ },
  async scheduled(event, env, ctx) { /* Cron handler */ }
};
```

### TypeScript Types

**Generate from wrangler.toml (Recommended):**
```bash
wrangler types  # Output: worker-configuration.d.ts
```

**Manual types:**
```typescript
interface Env {
  API: Fetcher;
  CACHE: KVNamespace;
  STORAGE: R2Bucket;
  ROOMS: DurableObjectNamespace;
  API_KEY: string;
}

export default {
  async fetch(request: Request, env: Env, ctx: ExecutionContext): Promise<Response> {
    return new Response(await env.CACHE.get("key"));
  }
};
```

**Setup:**
```bash
npm install -D @cloudflare/workers-types
```

```json
// tsconfig.json
{"compilerOptions": {"types": ["@cloudflare/workers-types"]}}
```

### Service Worker Syntax (Legacy)
```javascript
addEventListener('fetch', event => {
  event.respondWith(handleRequest(event.request));
});

async function handleRequest(request) {
  const value = await KV.get("key");  // Bindings as globals
  return new Response("OK");
}
```

### Durable Objects
```javascript
export class Room {
  constructor(state, env) { this.state = state; this.env = env; }
  
  async fetch(request) {
    const url = new URL(request.url);
    if (url.pathname === "/increment") {
      const value = (await this.state.storage.get("counter")) || 0;
      await this.state.storage.put("counter", value + 1);
      return new Response(String(value + 1));
    }
    return new Response("Not found", {status: 404});
  }
}
```

### RPC Between Services
```javascript
// Caller: env.AUTH.validateToken(token) returns structured data
const user = await env.AUTH.validateToken(request.headers.get("Authorization"));

// Callee: export methods that return data
export default {
  async validateToken(token) { return {id: 123, name: "Alice"}; }
};
```

