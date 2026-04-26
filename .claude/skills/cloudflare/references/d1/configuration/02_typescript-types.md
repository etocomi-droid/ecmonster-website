## TypeScript Types

```typescript
interface Env { DB: D1Database; ANALYTICS_DB?: D1Database; }

export default {
  async fetch(request: Request, env: Env, ctx: ExecutionContext): Promise<Response> {
    const result = await env.DB.prepare('SELECT * FROM users').all();
    return Response.json(result.results);
  }
}
```

