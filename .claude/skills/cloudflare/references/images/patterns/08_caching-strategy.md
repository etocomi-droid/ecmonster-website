## Caching Strategy

```typescript
async fetch(request: Request, env: Env, ctx: ExecutionContext): Promise<Response> {
  const cache = caches.default;
  let response = await cache.match(request);
  if (!response) {
    response = await env.IMAGES.input(buffer).transform({ width: 800, format: 'avif' }).output().response();
    response = new Response(response.body, { headers: { ...response.headers, 'Cache-Control': 'public, max-age=86400' } });
    ctx.waitUntil(cache.put(request, response.clone()));
  }
  return response;
}
```

