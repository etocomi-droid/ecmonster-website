## Caching

```typescript
// functions/api/data.ts
export const onRequestGet: PagesFunction<Env> = async ({ env, request }) => {
  const cacheKey = `data:${new URL(request.url).pathname}`;
  const cached = await env.KV.get(cacheKey, 'json');
  if (cached) return Response.json(cached, { headers: { 'X-Cache': 'HIT' } });
  
  const data = await env.DB.prepare('SELECT * FROM data').first();
  await env.KV.put(cacheKey, JSON.stringify(data), {expirationTtl: 3600});
  return Response.json(data, {headers: {'X-Cache': 'MISS'}});
};
```

