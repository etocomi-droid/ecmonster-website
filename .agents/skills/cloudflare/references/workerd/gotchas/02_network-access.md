## Network Access

**Problem:** Fetch fails with network error
**Cause:** No network service configured (workerd has no global fetch)
**Solution:** Add network service binding:
```capnp
services = [(name = "internet", network = (allow = ["public"]))]
bindings = [(name = "NET", service = "internet")]
```

Or external service:
```capnp
bindings = [(name = "API", service = (external = (address = "api.com:443", http = (style = tls))))]
```

### "Worker not responding"
**Cause:** Socket misconfigured, no fetch handler, or port unavailable
**Solution:** Verify socket `address` matches, worker exports `fetch()`, port available

### "Binding not found"
**Cause:** Name mismatch or service doesn't exist
**Solution:** Check binding name in config matches code (`env.BINDING` for ES modules)

### "Module not found"
**Cause:** Module name doesn't match import or bad embed path
**Solution:** Module `name` must match import path exactly, verify `embed` path

### "Compatibility error"
**Cause:** Date not set or API unavailable on that date
**Solution:** Set `compatibilityDate`, verify API available on that date

