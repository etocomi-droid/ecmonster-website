## Caching with Cache API

```typescript
export default {
  async fetch(request: Request, env: Env, ctx: ExecutionContext): Promise<Response> {
    const cache = caches.default;
    const url = new URL(request.url);
    const cacheKey = new Request(url.toString(), request);

    // Check cache first
    let response = await cache.match(cacheKey);
    if (response) return response;

    // Fetch from R2
    const key = url.pathname.slice(1);
    const object = await env.MY_BUCKET.get(key);
    if (!object) return new Response('Not found', { status: 404 });

    const headers = new Headers();
    object.writeHttpMetadata(headers);
    headers.set('etag', object.httpEtag);
    headers.set('cache-control', 'public, max-age=31536000, immutable');

    response = new Response(object.body, { headers });

    // Cache for subsequent requests
    ctx.waitUntil(cache.put(cacheKey, response.clone()));

    return response;
  }
};
```

