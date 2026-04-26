## Caching with KV

```typescript
async function getCachedUser(userId: number, env: { DB: D1Database; CACHE: KVNamespace }) {
  const cacheKey = `user:${userId}`;
  const cached = await env.CACHE?.get(cacheKey, 'json');
  if (cached) return cached;
  const user = await env.DB.prepare('SELECT * FROM users WHERE id = ?').bind(userId).first();
  if (user) await env.CACHE?.put(cacheKey, JSON.stringify(user), { expirationTtl: 300 });
  return user;
}
```

