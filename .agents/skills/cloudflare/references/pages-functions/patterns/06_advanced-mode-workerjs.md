## Advanced Mode (_worker.js)

Use `_worker.js` for complex routing (replaces `/functions`):

```typescript
interface Env { ASSETS: Fetcher; KV: KVNamespace; }

export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    const url = new URL(request.url);
    if (url.pathname.startsWith('/api/')) {
      return Response.json({ data: await env.KV.get('key') });
    }
    return env.ASSETS.fetch(request); // Static files
  }
} satisfies ExportedHandler<Env>;
```

**When:** Existing Worker, framework-generated (Next.js/SvelteKit), custom routing logic

**See also:** [api.md](./api.md) for `env.ASSETS.fetch()` | [gotchas.md](./gotchas.md) for debugging
