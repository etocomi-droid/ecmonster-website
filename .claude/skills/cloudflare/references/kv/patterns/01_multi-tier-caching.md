## Multi-Tier Caching

```typescript
// Memory → KV → Origin (3-tier cache)
const memoryCache = new Map<string, { data: any; expires: number }>();

async function getCached(env: Env, key: string): Promise<any> {
  const now = Date.now();
  
  // L1: Memory cache (fastest)
  const cached = memoryCache.get(key);
  if (cached && cached.expires > now) {
    return cached.data;
  }
  
  // L2: KV cache (fast)
  const kvValue = await env.CACHE.get(key, "json");
  if (kvValue) {
    memoryCache.set(key, { data: kvValue, expires: now + 60000 }); // 1min in memory
    return kvValue;
  }
  
  // L3: Origin (slow)
  const origin = await fetch(`https://api.example.com/${key}`).then(r => r.json());
  
  // Backfill caches
  await env.CACHE.put(key, JSON.stringify(origin), { expirationTtl: 300 }); // 5min in KV
  memoryCache.set(key, { data: origin, expires: now + 60000 });
  
  return origin;
}
```

