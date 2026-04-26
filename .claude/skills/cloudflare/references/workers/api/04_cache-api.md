## Cache API

```typescript
const cache = caches.default;
let response = await cache.match(request);

if (!response) {
  response = await fetch(request);
  response = new Response(response.body, response);
  response.headers.set('Cache-Control', 'max-age=3600');
  ctx.waitUntil(cache.put(request, response.clone()));  // Clone before caching
}
```

