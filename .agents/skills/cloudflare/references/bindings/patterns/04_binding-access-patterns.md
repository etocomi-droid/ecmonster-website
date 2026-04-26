## Binding Access Patterns

### Lazy Access

```typescript
// ✅ Access only when needed
if (url.pathname === '/cached') {
  const cached = await env.MY_KV.get('data');
  if (cached) return new Response(cached);
}
```

### Parallel Access

```typescript
// ✅ Parallelize independent calls
const [user, config, cache] = await Promise.all([
  env.DB.prepare('SELECT * FROM users WHERE id = ?').bind(userId).first(),
  env.MY_KV.get('config'),
  env.CACHE.get('data')
]);
```

