## Common Errors

### "Missing compatibility date"
**Cause:** Compatibility date not set
**Solution:**
❌ Wrong:
```capnp
const worker :Workerd.Worker = (
  serviceWorkerScript = embed "worker.js"
)
```

✅ Correct:
```capnp
const worker :Workerd.Worker = (
  serviceWorkerScript = embed "worker.js",
  compatibilityDate = "2024-01-15"  # Always set!
)
```

### Wrong Binding Type
**Problem:** JSON not parsed
**Cause:** Using `text = '{"key":"value"}'` instead of `json`
**Solution:** Use `json = '{"key":"value"}'` for parsed objects

### Service vs Namespace
**Problem:** Cannot create DO instance
**Cause:** Using `service = "room-service"` for Durable Object
**Solution:** Use `durableObjectNamespace = "Room"` for DO bindings

### Module Name Mismatch
**Problem:** Import fails
**Cause:** Module name includes path: `name = "src/index.js"`
**Solution:** Use simple names: `name = "index.js"`, embed with path

