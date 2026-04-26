## Monitoring

```bash
npx wrangler tail  # Check for sampling/write errors
```

```sql
-- Check write activity
SELECT DATE_TRUNC('hour', timestamp) AS hour, COUNT(*) AS writes
FROM my_dataset
WHERE timestamp >= NOW() - INTERVAL '24' HOUR
GROUP BY hour
```
