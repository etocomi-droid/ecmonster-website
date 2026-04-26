## Public Bucket with Custom Domain

```typescript
export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    // CORS preflight
    if (request.method === 'OPTIONS') {
      return new Response(null, {
        headers: {
          'access-control-allow-origin': '*',
          'access-control-allow-methods': 'GET, HEAD',
          'access-control-max-age': '86400'
        }
      });
    }

    const key = new URL(request.url).pathname.slice(1);
    if (!key) return Response.redirect('/index.html', 302);

    const object = await env.MY_BUCKET.get(key);
    if (!object) return new Response('Not found', { status: 404 });

    const headers = new Headers();
    object.writeHttpMetadata(headers);
    headers.set('etag', object.httpEtag);
    headers.set('access-control-allow-origin', '*');
    headers.set('cache-control', 'public, max-age=31536000, immutable');

    return new Response(object.body, { headers });
  }
};
```

