## Maintenance Issues

### Snapshot/Orphan Issues

**Problem:** Expiration fails or orphan cleanup deletes active data.  
**Cause:** Too aggressive retention or wrong order.  
**Solution:** Always expire snapshots first with `retain_last=10`, then cleanup orphans with 3+ day threshold.

