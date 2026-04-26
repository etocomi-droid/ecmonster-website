## Quick Decision Tree

```
Need to test your Worker?
├─ Testing full Worker with bindings → api.md §startWorker
├─ Testing individual functions → api.md §getPlatformProxy
└─ Testing with Vitest → patterns.md §Testing with Vitest

Need to configure something?
├─ Bindings (KV, D1, R2, etc.) → configuration.md §Bindings
├─ Multiple environments → configuration.md §Environments
├─ Static files → configuration.md §Workers Assets
└─ Routing → configuration.md §Routing

Development not working?
├─ Local differs from production → Use `wrangler dev --remote`
├─ Bindings not available → gotchas.md §Binding Not Available
└─ Auth issues → wrangler login
```

