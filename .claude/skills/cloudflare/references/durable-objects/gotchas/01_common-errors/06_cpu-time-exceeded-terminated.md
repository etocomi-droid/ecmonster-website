### "CPU Time Exceeded (Terminated)"

**Problem:** Request terminated mid-execution  
**Cause:** Processing exceeding 30s CPU time default limit  
**Solution:** Increase `limits.cpu_ms` in wrangler.jsonc (max 300s) or chunk work

