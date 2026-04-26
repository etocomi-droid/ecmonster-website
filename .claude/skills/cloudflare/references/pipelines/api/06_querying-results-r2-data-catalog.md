## Querying Results (R2 Data Catalog)

```bash
export WRANGLER_R2_SQL_AUTH_TOKEN=YOUR_CATALOG_TOKEN

npx wrangler r2 sql query "warehouse_name" "
SELECT 
  event_type,
  COUNT(*) as event_count,
  SUM(amount) as total_revenue
FROM default.my_table
WHERE event_type = 'purchase'
  AND timestamp >= '2025-01-01'
GROUP BY event_type
ORDER BY total_revenue DESC
LIMIT 100"
```

**Note:** Iceberg tables support standard SQL queries with GROUP BY, JOINs, WHERE, ORDER BY, etc.
