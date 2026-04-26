### "Durable Object Overloaded (503 errors)"

**Problem:** 503 errors under load  
**Cause:** Single DO exceeding ~1K req/s throughput limit  
**Solution:** Shard across multiple DOs (see [Patterns: Sharding](./patterns.md))

