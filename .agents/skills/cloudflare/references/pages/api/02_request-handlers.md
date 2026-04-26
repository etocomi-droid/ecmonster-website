## Request Handlers

```typescript
import type { PagesFunction } from '@cloudflare/workers-types';

interface Env {
  DB: D1Database;
  KV: KVNamespace;
}

// All methods
export const onRequest: PagesFunction<Env> = async (context) => {
  return new Response('All methods');
};

// Method-specific
export const onRequestGet: PagesFunction<Env> = async (context) => {
  const { request, env, params, data } = context;
  
  const user = await env.DB.prepare(
    'SELECT * FROM users WHERE id = ?'
  ).bind(params.id).first();
  
  return Response.json(user);
};

export const onRequestPost: PagesFunction<Env> = async (context) => {
  const body = await context.request.json();
  return Response.json({ success: true });
};

// Also: onRequestPut, onRequestPatch, onRequestDelete, onRequestHead, onRequestOptions
```

