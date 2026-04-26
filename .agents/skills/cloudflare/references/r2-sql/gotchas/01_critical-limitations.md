## Critical Limitations

### No Workers Binding

**Cannot call R2 SQL from Workers/Pages code** - no binding exists.

```typescript
// ❌ This doesn't exist
export default {
  async fetch(request, env) {
    const result = await env.R2_SQL.query("SELECT * FROM table");  // Not possible
    return Response.json(result);
  }
};
```

**Solutions:**
- HTTP API from external systems (not Workers)
- PyIceberg/Spark via r2-data-catalog REST API
- For Workers, use D1 or external databases

### ORDER BY Limitations

Can only order by:
1. **Partition key columns** - Always supported
2. **Aggregation functions** - Supported via shuffle strategy

**Cannot order by** regular non-partition columns.

```sql
-- ✅ Valid: ORDER BY partition key
SELECT * FROM logs.requests ORDER BY timestamp DESC LIMIT 100;

-- ✅ Valid: ORDER BY aggregation
SELECT region, SUM(amount) FROM sales.transactions
GROUP BY region ORDER BY SUM(amount) DESC;

-- ❌ Invalid: ORDER BY non-partition column
SELECT * FROM logs.requests ORDER BY user_id;

-- ❌ Invalid: ORDER BY alias (must repeat function)
SELECT region, SUM(amount) as total FROM sales.transactions
GROUP BY region ORDER BY total;  -- Use ORDER BY SUM(amount)
```

Check partition spec: `DESCRIBE namespace.table_name`

