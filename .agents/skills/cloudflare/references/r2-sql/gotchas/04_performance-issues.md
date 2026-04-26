## Performance Issues

### Slow Queries

**Causes:** Too many partitions, large LIMIT, no filters, small files

```sql
-- ❌ Slow: No filters
SELECT * FROM logs.requests LIMIT 10000;

-- ✅ Fast: Filter on partition key
SELECT * FROM logs.requests 
WHERE timestamp >= '2025-01-15T00:00:00Z' AND timestamp < '2025-01-16T00:00:00Z'
LIMIT 1000;

-- ✅ Faster: Multiple filters
SELECT * FROM logs.requests 
WHERE timestamp >= '2025-01-15T00:00:00Z' AND status = 404 AND method = 'GET'
LIMIT 1000;
```

**File optimization:**
- Target Parquet size: 100-500MB compressed
- Pipelines roll interval: 300+ sec (prod), 10 sec (dev)
- Run compaction to merge small files

### Query Timeout

**Solution:** Add restrictive WHERE filters, reduce time range, query smaller intervals

```sql
-- ❌ Times out: Year-long aggregation
SELECT status, COUNT(*) FROM logs.requests 
WHERE timestamp >= '2024-01-01T00:00:00Z' GROUP BY status;

-- ✅ Faster: Month-long aggregation
SELECT status, COUNT(*) FROM logs.requests 
WHERE timestamp >= '2025-01-01T00:00:00Z' AND timestamp < '2025-02-01T00:00:00Z'
GROUP BY status;
```

