## RPC Methods Not Affected (Critical Limitation)

**Problem:** Enabled Smart Placement on backend but RPC calls still slow.

**Cause:** Smart Placement ONLY affects `fetch` handlers. RPC methods (Service Bindings with `WorkerEntrypoint`) are NEVER affected.

**Why:** RPC bypasses `fetch` handler - Smart Placement can only route `fetch` requests.

**Solution:** Convert to fetch-based Service Bindings:

```typescript
// ❌ RPC - Smart Placement has NO EFFECT
export class BackendRPC extends WorkerEntrypoint {
  async getData() {
    // ALWAYS runs at edge
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
}
```

