## Bindings Usage

```typescript
export const onRequestGet: PagesFunction<Env> = async ({ env }) => {
  // KV
  const cached = await env.KV.get('key', 'json');
  await env.KV.put('key', JSON.stringify({data: 'value'}), {expirationTtl: 3600});
  
  // D1
  const result = await env.DB.prepare('SELECT * FROM users WHERE id = ?').bind(userId).first();
  
  // R2, Queue, AI - see respective reference docs
  
  return Response.json({success: true});
};
```

