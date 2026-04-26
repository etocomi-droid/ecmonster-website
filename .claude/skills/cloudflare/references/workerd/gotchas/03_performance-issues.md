## Performance Issues

**Problem:** High memory usage
**Cause:** Large caches or many isolates
**Solution:** Set cache limits, reduce isolate count, or use V8 flags (caution)

**Problem:** Slow startup
**Cause:** Many modules or complex config
**Solution:** Compile to binary (`workerd compile`), reduce imports

**Problem:** Request timeouts
**Cause:** External service issues or DNS problems
**Solution:** Check connectivity, DNS resolution, TLS handshake

