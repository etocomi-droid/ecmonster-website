## RPC vs fetch()

**RPC** (compat ≥2024-04-03): Type-safe, simpler, default for new projects  
**fetch()**: Legacy compat, HTTP semantics, proxying

```typescript
const count = await stub.increment();  // RPC
const count = await (await stub.fetch(req)).json();  // fetch()
```

