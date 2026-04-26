## Performance Gotchas

### Sequential Binding Calls

```typescript
// ❌ Slow
const user = await env.DB.prepare('...').first();
const config = await env.MY_KV.get('config');

// ✅ Parallel
const [user, config] = await Promise.all([
  env.DB.prepare('...').first(),
  env.MY_KV.get('config')
]);
```

