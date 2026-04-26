## Accessing Bindings

### Method 1: fetch() Handler (Recommended)

```typescript
export default {
  async fetch(request: Request, env: Env, ctx: ExecutionContext): Promise<Response> {
    const value = await env.MY_KV.get('key');
    return new Response(value);
  }
}
```

**Why:** Type-safe, aligns with Workers API, supports ctx for waitUntil/passThroughOnException.

### Method 2: Hono Framework

```typescript
import { Hono } from 'hono';

const app = new Hono<{ Bindings: Env }>();

app.get('/', async (c) => {
  const value = await c.env.MY_KV.get('key');
  return c.json({ value });
});

export default app;
```

**Why:** c.env auto-typed, ergonomic for routing-heavy apps.

### Method 3: Module Workers (Legacy)

```typescript
export async function handleRequest(request: Request, env: Env): Promise<Response> {
  const value = await env.MY_KV.get('key');
  return new Response(value);
}

addEventListener('fetch', (event) => {
  // env not directly available - requires workarounds
});
```

**Avoid:** Use fetch() handler instead (Method 1).

