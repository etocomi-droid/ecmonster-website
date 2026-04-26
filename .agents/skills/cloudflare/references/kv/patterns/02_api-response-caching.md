## API Response Caching

```typescript
async function getCachedData(env: Env, key: string, fetcher: () => Promise<any>): Promise<any> {
  const cached = await env.MY_KV.get(key, "json");
  if (cached) return cached;
  
  const data = await fetcher();
  await env.MY_KV.put(key, JSON.stringify(data), { expirationTtl: 300 });
  return data;
}

const apiData = await getCachedData(
  env,
  "cache:users",
  () => fetch("https://api.example.com/users").then(r => r.json())
);
```

