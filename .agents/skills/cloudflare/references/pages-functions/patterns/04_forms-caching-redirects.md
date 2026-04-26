## Forms, Caching, Redirects

```typescript
// JSON & file upload
export async function onRequestPost(ctx) {
  const ct = ctx.request.headers.get('content-type') || '';
  if (ct.includes('application/json')) return Response.json(await ctx.request.json());
  if (ct.includes('multipart/form-data')) {
    const file = (await ctx.request.formData()).get('file') as File;
    await ctx.env.BUCKET.put(file.name, file.stream());
    return Response.json({ uploaded: file.name });
  }
}

// Cache API
export async function onRequest(ctx) {
  let res = await caches.default.match(ctx.request);
  if (!res) {
    res = new Response('Data');
    res.headers.set('Cache-Control', 'public, max-age=3600');
    ctx.waitUntil(caches.default.put(ctx.request, res.clone()));
  }
  return res;
}

// Redirects
export async function onRequest(ctx) {
  if (new URL(ctx.request.url).pathname === '/old') {
    return Response.redirect(new URL('/new', ctx.request.url), 301);
  }
  return ctx.next();
}
```

