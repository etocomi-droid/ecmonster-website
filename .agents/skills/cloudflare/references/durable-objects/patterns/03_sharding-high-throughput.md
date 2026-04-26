## Sharding (High Throughput)

Single DO ~1K req/s max. Shard for higher throughput:

```typescript
export default {
  async fetch(req: Request, env: Env): Promise<Response> {
    const userId = new URL(req.url).searchParams.get("user");
    const hash = hashCode(userId) % 100;  // 100 shards
    const id = env.COUNTER.idFromName(`shard:${hash}`);
    return env.COUNTER.get(id).fetch(req);
  }
};

function hashCode(str: string): number {
  let hash = 0;
  for (let i = 0; i < str.length; i++) hash = ((hash << 5) - hash) + str.charCodeAt(i);
  return Math.abs(hash);
}
```

**Decisions:**
- **Shard count**: 10-1000 typical (start with 100, measure, adjust)
- **Shard key**: User ID, IP, session - must distribute evenly (use hash)
- **Aggregation**: Coordinator DO or external system (D1, R2)

