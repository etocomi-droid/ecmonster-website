### "Execution Failures"

**Cause:** CPU exceeded, unhandled exceptions, network timeouts, binding errors  
**Solution:** Use try-catch, AbortController timeouts, `ctx.waitUntil()` for long ops, or Workflows for heavy tasks

