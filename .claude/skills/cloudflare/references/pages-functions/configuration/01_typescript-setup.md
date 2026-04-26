## TypeScript Setup

**Generate types from wrangler.jsonc** (replaces deprecated `@cloudflare/workers-types`):

```bash
npx wrangler types
```

Creates `worker-configuration.d.ts` with typed `Env` interface based on your bindings.

```typescript
// functions/api.ts
export const onRequest: PagesFunction<Env> = async (ctx) => {
  // ctx.env.KV, ctx.env.DB, etc. are fully typed
  return Response.json({ ok: true });
};
```

**Manual types** (if not using wrangler types):

```typescript
interface Env {
  KV: KVNamespace;
  DB: D1Database;
  API_KEY: string;
}
export const onRequest: PagesFunction<Env> = async (ctx) => { /* ... */ };
```

