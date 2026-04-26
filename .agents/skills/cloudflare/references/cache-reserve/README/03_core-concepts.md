## Core Concepts

### What is Cache Reserve?

- **Persistent storage layer**: Built on R2, sits above tiered cache hierarchy
- **Long-term retention**: 30-day default retention, extended on each access
- **Automatic operation**: Works seamlessly with existing CDN, no code changes required
- **Origin shielding**: Dramatically reduces origin egress by serving cached content longer
- **Usage-based pricing**: Pay only for storage + read/write operations

### Cache Hierarchy

```
Visitor Request
    ↓
Lower-Tier Cache (closest to visitor)
    ↓ (on miss)
Upper-Tier Cache (closest to origin)
    ↓ (on miss)
Cache Reserve (R2 persistent storage)
    ↓ (on miss)
Origin Server
```

### How It Works

1. **On cache miss**: Content fetched from origin �� written to Cache Reserve + edge caches simultaneously
2. **On edge eviction**: Content may be evicted from edge cache but remains in Cache Reserve
3. **On subsequent request**: If edge cache misses but Cache Reserve hits → content restored to edge caches
4. **Retention**: Assets remain in Cache Reserve for 30 days since last access (configurable via TTL)

