## Async KV API (Both backends)

```typescript
await this.ctx.storage.get("key"); // Single
await this.ctx.storage.get(["key1", "key2"]); // Multiple (max 128)
await this.ctx.storage.put("key", value); // Single
await this.ctx.storage.put({ "key1": "v1", "key2": { nested: true } }); // Multiple (max 128)
await this.ctx.storage.delete("key");
await this.ctx.storage.delete(["key1", "key2"]);
await this.ctx.storage.list({ prefix: "user:", limit: 100 });

// Options: allowConcurrency, noCache, allowUnconfirmed
await this.ctx.storage.get("key", { allowConcurrency: true, noCache: true });
await this.ctx.storage.put("key", value, { allowUnconfirmed: true, noCache: true });
```

### Storage Options

| Option | Methods | Effect | Use Case |
|--------|---------|--------|----------|
| `allowConcurrency` | get, list | Skip input gate; allow concurrent requests during read | Read-heavy metrics that don't need strict consistency |
| `noCache` | get, put, list | Skip in-memory cache; always read from disk | Rarely-accessed data or testing storage directly |
| `allowUnconfirmed` | put, delete | Return before write confirms (still protected by output gate) | Non-critical writes where latency matters more than confirmation |

