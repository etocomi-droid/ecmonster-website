## API Data Sync

```typescript
export default {
  async scheduled(controller, env, ctx) {
    const response = await fetch("https://api.example.com/data", {headers: { "Authorization": `Bearer ${env.API_KEY}` }});
    if (!response.ok) throw new Error(`API error: ${response.status}`);
    ctx.waitUntil(env.MY_KV.put("cached_data", JSON.stringify(await response.json()), {expirationTtl: 3600}));
  },
};
```

