## Frontend + Backend Split (Service Bindings)

**Frontend:** Runs at edge for fast user response
**Backend:** Smart Placement runs close to database

```typescript
// Frontend Worker - routes requests to backend
interface Env {
  BACKEND: Fetcher;  // Service Binding to backend Worker
}

export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    if (new URL(request.url).pathname.startsWith('/api/')) {
      return env.BACKEND.fetch(request);  // Forward to backend
    }
    return new Response('Frontend content');
  }
};

// Backend Worker - database operations
interface BackendEnv {
  DATABASE: D1Database;
}

export default {
  async fetch(request: Request, env: BackendEnv): Promise<Response> {
    const data = await env.DATABASE.prepare('SELECT * FROM table').all();
    return Response.json(data);
  }
};
```

**CRITICAL:** Use fetch-based Service Bindings (shown above). If using RPC with `WorkerEntrypoint`, Smart Placement will NOT optimize those method calls - only `fetch` handlers are affected.

**RPC vs Fetch - CRITICAL:** Smart Placement ONLY works with fetch-based bindings, NOT RPC.

```typescript
// ❌ RPC - Smart Placement has NO EFFECT on backend RPC methods
export class BackendRPC extends WorkerEntrypoint {
  async getData() {
    // ALWAYS runs at edge, Smart Placement ignored
    return await this.env.DATABASE.prepare('SELECT * FROM table').all();
  }
}

// ✅ Fetch - Smart Placement WORKS
export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    // Runs close to DATABASE when Smart Placement enabled
    const data = await env.DATABASE.prepare('SELECT * FROM table').all();
    return Response.json(data);
  }
};
```

