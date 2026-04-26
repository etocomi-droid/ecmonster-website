## TypeScript Types

```typescript
interface Env {
  BACKEND: Fetcher;
  DATABASE: D1Database;
}

export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    const data = await env.DATABASE.prepare('SELECT * FROM table').all();
    return Response.json(data);
  }
} satisfies ExportedHandler<Env>;
```

