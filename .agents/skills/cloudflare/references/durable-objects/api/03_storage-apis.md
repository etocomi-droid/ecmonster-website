## Storage APIs

For detailed storage documentation including SQLite queries, KV operations, transactions, and Point-in-Time Recovery, see **[DO Storage](../do-storage/README.md)**.

Quick reference:

```typescript
// SQLite (recommended)
this.ctx.storage.sql.exec("SELECT * FROM users WHERE id = ?", userId).one()

// Sync KV (SQLite DOs only)
this.ctx.storage.kv.get("key")

// Async KV (legacy)
await this.ctx.storage.get("key")
```

