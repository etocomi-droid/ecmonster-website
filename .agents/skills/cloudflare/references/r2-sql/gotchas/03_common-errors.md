## Common Errors

### "Column not found"
**Cause:** Typo, column doesn't exist, or case mismatch  
**Solution:** `DESCRIBE namespace.table_name` to check schema

### "Type mismatch"
```sql
-- ❌ Wrong types
WHERE status = '200'              -- string instead of integer
WHERE timestamp > '2025-01-01'    -- missing time/timezone

-- ✅ Correct types
WHERE status = 200
WHERE timestamp > '2025-01-01T00:00:00Z'
```

### "ORDER BY column not in partition key"
**Cause:** Ordering by non-partition column  
**Solution:** Use partition key, aggregation, or remove ORDER BY. Check: `DESCRIBE table`

### "Token authentication failed"
```bash
# Check/set token
echo $WRANGLER_R2_SQL_AUTH_TOKEN
export WRANGLER_R2_SQL_AUTH_TOKEN=<your-token>

# Or .env file
echo "WRANGLER_R2_SQL_AUTH_TOKEN=<your-token>" > .env
```

### "Table not found"
```sql
-- Verify catalog and tables
SHOW DATABASES;
SHOW TABLES IN namespace_name;
```

Enable catalog: `npx wrangler r2 bucket catalog enable <bucket>`

### "LIMIT exceeds maximum"
Max LIMIT is 10,000. For pagination, use WHERE filters with partition keys.

### "No data returned" (unexpected)
**Debug steps:**
1. `SELECT COUNT(*) FROM table` - verify data exists
2. Remove WHERE filters incrementally
3. `SELECT * FROM table LIMIT 10` - inspect actual data/types

