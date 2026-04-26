## Limits

| Limit | Free | Paid | Notes |
|-------|------|------|-------|
| SQLite storage per DO | 10 GB | 10 GB | Per Durable Object instance |
| SQLite total storage | 5 GB | Unlimited | Account-wide quota |
| Key+value size | 2 MB | 2 MB | Single KV pair (SQLite/async) |
| CPU time default | 30s | 30s | Per request; configurable |
| CPU time max | 300s | 300s | Set via `limits.cpu_ms` |
| DO classes | 100 | 500 | Distinct DO class definitions |
| SQL columns | 100 | 100 | Per table |
| SQL statement size | 100 KB | 100 KB | Max SQL query size |
| WebSocket message size | 32 MiB | 32 MiB | Per message |
| Request throughput | ~1K req/s | ~1K req/s | Per DO (soft limit - shard for more) |
| Alarms per DO | 1 | 1 | Use queue pattern for multiple events |
| Total DOs | Unlimited | Unlimited | Create as many instances as needed |
| WebSockets | Unlimited | Unlimited | Within 128MB memory limit per DO |
| Memory per DO | 128 MB | 128 MB | In-memory state + WebSocket buffers |

