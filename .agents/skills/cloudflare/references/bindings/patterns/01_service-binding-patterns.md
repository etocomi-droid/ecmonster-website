## Service Binding Patterns

### RPC via Service Bindings

```typescript
// auth-worker
export default {
  async fetch(request: Request, env: Env) {
    const token = request.headers.get('Authorization');
    return new Response(JSON.stringify({ valid: await validateToken(token) }));
  }
}

// api-worker
const response = await env.AUTH_SERVICE.fetch(
  new Request('https://fake-host/validate', {
    headers: { 'Authorization': token }
  })
);
```

**Why RPC?** Zero latency (same datacenter), no DNS, free, type-safe.

**HTTP vs Service:**
```typescript
// ❌ HTTP (slow, paid, cross-region latency)
await fetch('https://auth-worker.example.com/validate');

// ✅ Service binding (fast, free, same isolate)
await env.AUTH_SERVICE.fetch(new Request('https://fake-host/validate'));
```

**URL doesn't matter:** Service bindings ignore hostname/protocol, routing happens via binding name.

### Typed Service RPC

```typescript
// shared-types.ts
export interface AuthRequest { token: string; }
export interface AuthResponse { valid: boolean; userId?: string; }

// auth-worker
export default {
  async fetch(request: Request): Promise<Response> {
    const body: AuthRequest = await request.json();
    const response: AuthResponse = { valid: true, userId: '123' };
    return Response.json(response);
  }
}

// api-worker
const response = await env.AUTH_SERVICE.fetch(
  new Request('https://fake/validate', {
    method: 'POST',
    body: JSON.stringify({ token } satisfies AuthRequest)
  })
);
const data: AuthResponse = await response.json();
```

