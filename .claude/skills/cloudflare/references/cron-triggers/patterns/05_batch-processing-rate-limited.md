## Batch Processing (Rate-Limited)

```typescript
export default {
  async scheduled(controller, env, ctx) {
    const queueData = await env.QUEUE_KV.get("pending_items", "json");
    if (!queueData || queueData.length === 0) return;
    const batch = queueData.slice(0, 100);
    const results = await Promise.allSettled(batch.map(item => fetch("https://api.example.com/process", {method: "POST", headers: {"Authorization": `Bearer ${env.API_KEY}`, "Content-Type": "application/json"}, body: JSON.stringify(item)})));
    console.log(`Processed ${results.filter(r => r.status === "fulfilled").length}/${batch.length} items`);
    ctx.waitUntil(env.QUEUE_KV.put("pending_items", JSON.stringify(queueData.slice(100))));
  },
};
```

