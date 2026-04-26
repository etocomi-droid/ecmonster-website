## Fetch Handler

```typescript
export default {
  async fetch(request: Request, env: Env, ctx: ExecutionContext): Promise<Response> {
    const url = new URL(request.url);
    if (request.method === 'POST' && url.pathname === '/api') {
      const body = await request.json();
      return new Response(JSON.stringify({ id: 1 }), {
        headers: { 'Content-Type': 'application/json' }
      });
    }
    return fetch(request);  // Subrequest to origin
  },
};
```

