## Key Binding Methods

**KV:**
```typescript
await env.MY_KV.get(key, { type: 'json' });  // text|json|arrayBuffer|stream
await env.MY_KV.put(key, value, { expirationTtl: 3600 });
await env.MY_KV.delete(key);
await env.MY_KV.list({ prefix: 'user:' });
```

**R2:**
```typescript
await env.BUCKET.get(key);
await env.BUCKET.put(key, value);
await env.BUCKET.delete(key);
await env.BUCKET.list({ prefix: 'images/' });
```

**D1:**
```typescript
await env.DB.prepare('SELECT * FROM users WHERE id = ?').bind(userId).first();
await env.DB.batch([stmt1, stmt2]);
```

**Service:**
```typescript
await env.MY_SERVICE.fetch(new Request('https://fake/path'));
```

**Workers AI:**
```typescript
await env.AI.run('@cf/meta/llama-3.1-8b-instruct', { prompt: 'Hello' });
```

**Queues:**
```typescript
await env.MY_QUEUE.send({ userId: 123, action: 'process' });
```

**Durable Objects:**
```typescript
const id = env.MY_DO.idFromName('user-123');
const stub = env.MY_DO.get(id);
await stub.fetch(new Request('https://fake/increment'));
```

