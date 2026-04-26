## Performance Monitoring

```typescript
const start = Date.now();
const response = await fetch(url);
env.ANALYTICS.writeDataPoint({
  blobs: [url, response.status.toString()],
  doubles: [Date.now() - start, response.status]
});
```

```sql
SELECT blob1 AS url, AVG(double1) AS avg_ms, percentile(double1, 0.95) AS p95_ms
FROM fetch_metrics WHERE timestamp >= NOW() - INTERVAL '1' HOUR
GROUP BY url
```

