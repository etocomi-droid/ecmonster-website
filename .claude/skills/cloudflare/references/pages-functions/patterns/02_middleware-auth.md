## Middleware & Auth

```typescript
// functions/_middleware.js (global) or functions/users/_middleware.js (scoped)
export async function onRequest(ctx) {
  try { return await ctx.next(); } 
  catch (err) { return new Response(err.message, { status: 500 }); }
}

// Chained: export const onRequest = [errorHandler, auth, logger];

// Auth
async function auth(ctx: EventContext<Env>) {
  const token = ctx.request.headers.get('authorization')?.replace('Bearer ', '');
  if (!token) return new Response('Unauthorized', { status: 401 });
  const session = await ctx.env.KV.get(`session:${token}`);
  if (!session) return new Response('Invalid', { status: 401 });
  ctx.data.user = JSON.parse(session);
  return ctx.next();
}
```

