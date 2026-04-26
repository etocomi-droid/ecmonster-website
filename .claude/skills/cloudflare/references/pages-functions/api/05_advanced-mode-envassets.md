## Advanced Mode (env.ASSETS)

When using `_worker.js`, access static assets via `env.ASSETS.fetch()`:

```typescript
interface Env { ASSETS: Fetcher; KV: KVNamespace; }

export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    const url = new URL(request.url);
    if (url.pathname.startsWith('/api/')) {
      return Response.json({ data: await env.KV.get('key') });
    }
    return env.ASSETS.fetch(request); // Fallback to static
  }
} satisfies ExportedHandler<Env>;
```

**See also:** [configuration.md](./configuration.md) for TypeScript setup and wrangler.jsonc | [patterns.md](./patterns.md) for middleware and auth patterns
