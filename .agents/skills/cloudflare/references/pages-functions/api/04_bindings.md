## Bindings

### KV

```typescript
interface Env { KV: KVNamespace; }
export const onRequest: PagesFunction<Env> = async (ctx) => {
  await ctx.env.KV.put('key', 'value', { expirationTtl: 3600 });
  const val = await ctx.env.KV.get('key', { type: 'json' });
  const keys = await ctx.env.KV.list({ prefix: 'user:' });
  return Response.json({ val });
};
```

### D1

```typescript
interface Env { DB: D1Database; }
export const onRequest: PagesFunction<Env> = async (ctx) => {
  const user = await ctx.env.DB.prepare('SELECT * FROM users WHERE id = ?').bind(123).first();
  return Response.json(user);
};
```

### R2

```typescript
interface Env { BUCKET: R2Bucket; }
export const onRequest: PagesFunction<Env> = async (ctx) => {
  const obj = await ctx.env.BUCKET.get('file.txt');
  if (!obj) return new Response('Not found', { status: 404 });
  await ctx.env.BUCKET.put('file.txt', ctx.request.body);
  return new Response(obj.body);
};
```

### Durable Objects

```typescript
interface Env { COUNTER: DurableObjectNamespace; }
export const onRequest: PagesFunction<Env> = async (ctx) => {
  const stub = ctx.env.COUNTER.get(ctx.env.COUNTER.idFromName('global'));
  return stub.fetch(ctx.request);
};
```

### Workers AI

```typescript
interface Env { AI: Ai; }
export const onRequest: PagesFunction<Env> = async (ctx) => {
  const resp = await ctx.env.AI.run('@cf/meta/llama-3.1-8b-instruct', { prompt: 'Hello' });
  return Response.json(resp);
};
```

### Service Bindings & Env Vars

```typescript
interface Env { AUTH: Fetcher; API_KEY: string; }
export const onRequest: PagesFunction<Env> = async (ctx) => {
  // Service binding: forward to another Worker
  return ctx.env.AUTH.fetch(ctx.request);
  
  // Environment variable
  return Response.json({ key: ctx.env.API_KEY });
};
```

