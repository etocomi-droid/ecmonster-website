## CORS & Rate Limiting

```typescript
// CORS middleware
const cors = { 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Methods': 'GET, POST' };
export async function onRequestOptions() { return new Response(null, { headers: cors }); }
export async function onRequest(ctx) {
  const res = await ctx.next();
  Object.entries(cors).forEach(([k, v]) => res.headers.set(k, v));
  return res;
}

// Rate limiting (KV-based)
async function rateLimit(ctx: EventContext<Env>) {
  const ip = ctx.request.headers.get('CF-Connecting-IP') || 'unknown';
  const count = parseInt(await ctx.env.KV.get(`rate:${ip}`) || '0');
  if (count >= 100) return new Response('Rate limited', { status: 429 });
  await ctx.env.KV.put(`rate:${ip}`, (count + 1).toString(), { expirationTtl: 3600 });
  return ctx.next();
}
```

