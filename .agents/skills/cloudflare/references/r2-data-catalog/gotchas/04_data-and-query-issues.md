## Data and Query Issues

### Empty Scan Results

**Error:** Scan returns no data.  
**Cause:** Incorrect filter or partition column.  
**Solution:** Test without filter first: `table.scan().to_pandas()`. Verify partition column names.

### Slow Queries

**Error:** Performance degrades over time.  
**Cause:** Too many small files.  
**Solution:** Check file count, compact if >1000 or avg <10MB. See [api.md](api.md#compaction).

### Type Mismatch

**Error:** `"Cannot cast"` on append.  
**Cause:** PyArrow types don't match Iceberg schema.  
**Solution:** Cast to int64 (Iceberg default), not int32. Check `table.schema()`.

