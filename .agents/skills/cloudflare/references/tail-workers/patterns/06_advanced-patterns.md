## Advanced Patterns

### Batching with Durable Objects

Accumulate events before sending:

```typescript
export default {
  async tail(events, env, ctx) {
    const batch = env.BATCH_DO.get(env.BATCH_DO.idFromName("batch"));
    ctx.waitUntil(batch.fetch("https://batch/add", {
      method: "POST",
      body: JSON.stringify(events),
    }));
  }
};
```

See durable-objects skill for full implementation.

### Workers for Platforms

Dynamic dispatch sends TWO events per request. Filter by `scriptName` to distinguish dispatch vs user Worker events.

### Error Handling

Always wrap external calls. See gotchas.md for fallback storage pattern.
