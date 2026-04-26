## Concurrency Issues

### Concurrent Write Conflicts

**Problem:** `CommitFailedException` with multiple writers.  
**Cause:** Optimistic locking - simultaneous commits.  
**Solution:** Add retry with exponential backoff (see [patterns.md](patterns.md#pattern-6-concurrent-writes-with-retry)).

### Stale Metadata

**Problem:** Old schema/data after external update.  
**Cause:** Cached metadata.  
**Solution:** Reload table: `table = catalog.load_table(("ns", "table"))`

