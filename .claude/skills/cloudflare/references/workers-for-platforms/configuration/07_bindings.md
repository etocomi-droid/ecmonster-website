## Bindings

**Supported binding types:** 29 total including KV, D1, R2, Durable Objects, Analytics Engine, Service, Assets, Queue, Vectorize, Hyperdrive, Workflow, AI, Browser, and more.

Add via API metadata (see [api.md](./api.md#deploy-with-bindings)):
```json
{
  "bindings": [
    {"type": "kv_namespace", "name": "USER_KV", "namespace_id": "..."},
    {"type": "r2_bucket", "name": "STORAGE", "bucket_name": "..."},
    {"type": "d1", "name": "DB", "id": "..."}
  ]
}
```

Preserve existing bindings:
```json
{
  "bindings": [{"type": "r2_bucket", "name": "STORAGE", "bucket_name": "new"}],
  "keep_bindings": ["kv_namespace", "d1"]  // Preserves existing bindings of these types
}
```

For complete binding type reference, see [bindings](../bindings/) documentation

See [README.md](./README.md), [api.md](./api.md), [patterns.md](./patterns.md), [gotchas.md](./gotchas.md)
