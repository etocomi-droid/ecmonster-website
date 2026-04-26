## Core Concepts

### Class Structure
All DOs extend `DurableObject` base class with constructor receiving `DurableObjectState` (storage, WebSockets, alarms) and `Env` (bindings).

### Lifecycle States

```
[Not Created] → [Active] ⇄ [Hibernated] → [Evicted]
                   ↓
              [Destroyed]
```

- **Not Created**: DO ID exists but instance never spawned
- **Active**: Processing requests, in-memory state valid, billed per GB-hour
- **Hibernated**: WebSocket connections open but zero compute, zero cost
- **Evicted**: Removed from memory; next request triggers cold start
- **Destroyed**: Data deleted via migration or manual deletion

### Accessing from Workers
Workers use bindings to get stubs, then call RPC methods directly (recommended) or use fetch handler (legacy).

**RPC vs fetch() decision:**
```
├─ New project + compat ≥2024-04-03 → RPC (type-safe, simpler)
├─ Need HTTP semantics (headers, status) → fetch()
├─ Proxying requests to DO → fetch()
└─ Legacy compatibility → fetch()
```

See [Patterns: RPC vs fetch()](./patterns.md) for examples.

### ID Generation
- `idFromName()`: Deterministic, named coordination (rate limiting, locks)
- `newUniqueId()`: Random IDs for sharding high-throughput workloads
- `idFromString()`: Derive from existing IDs
- Jurisdiction option: Data locality compliance

### Storage Options

**Which storage API?**
```
├─ Structured data, relations, transactions → SQLite (recommended)
├─ Simple KV on SQLite DO → ctx.storage.kv (sync KV)
└─ Legacy KV-only DO → ctx.storage (async KV)
```

- **SQLite** (recommended): Structured data, transactions, 10GB/DO
- **Synchronous KV API**: Simple key-value on SQLite objects
- **Asynchronous KV API**: Legacy/advanced use cases

See [DO Storage](../do-storage/README.md) for deep dive.

### Special Features
- **Alarms**: Schedule future execution per-DO (1 per DO - use queue pattern for multiple)
- **WebSocket Hibernation**: Zero-cost idle connections (memory cleared on hibernation)
- **Point-in-Time Recovery**: Restore to any point in 30 days (SQLite only)

