## Decision Trees

### What do you need?

```
├─ Coordinate requests (rate limit, lock, session)
│   → idFromName(identifier) → [Patterns: Rate Limiting/Locks](./patterns.md)
│
├─ High throughput (>1K req/s)
│   → Sharding with newUniqueId() or hash → [Patterns: Sharding](./patterns.md)
│
├─ Real-time updates (WebSocket, chat, collab)
│   → WebSocket hibernation + room pattern → [Patterns: Real-time](./patterns.md)
│
├─ Background work (cleanup, notifications, scheduled tasks)
│   → Alarms + queue pattern (1 alarm/DO) → [Patterns: Multiple Events](./patterns.md)
│
└─ User sessions with expiration
    → Session pattern + alarm cleanup → [Patterns: Session Management](./patterns.md)
```

### Which access pattern?

```
├─ New project + typed methods → RPC (compat ≥2024-04-03)
├─ Need HTTP semantics → fetch()
├─ Proxying to DO → fetch()
└─ Legacy compat → fetch()
```

See [Patterns: RPC vs fetch()](./patterns.md) for examples.

### Which storage?

```
├─ Structured data, SQL queries, transactions → SQLite (recommended)
├─ Simple KV on SQLite DO → ctx.storage.kv (sync API)
└─ Legacy KV-only DO → ctx.storage (async API)
```

See [DO Storage](../do-storage/README.md) for complete guide.

