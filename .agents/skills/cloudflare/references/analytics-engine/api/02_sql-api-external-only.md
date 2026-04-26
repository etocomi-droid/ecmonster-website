## SQL API (External Only)

```bash
curl -X POST https://api.cloudflare.com/client/v4/accounts/{account_id}/analytics_engine/sql \
  -H "Authorization: Bearer $TOKEN" \
  -d "SELECT blob1 AS endpoint, COUNT(*) AS requests FROM dataset WHERE timestamp >= NOW() - INTERVAL '1' HOUR GROUP BY blob1"
```

### Column References

```sql
-- blob1..blob20, double1..double20, index1, timestamp
SELECT blob1 AS endpoint, SUM(double1) AS latency, COUNT(*) AS requests
FROM my_dataset
WHERE index1 = 'customer_123' AND timestamp >= NOW() - INTERVAL '7' DAY
GROUP BY blob1
HAVING COUNT(*) > 100
ORDER BY requests DESC LIMIT 100
```

**Aggregations:** `SUM()`, `AVG()`, `COUNT()`, `MIN()`, `MAX()`, `quantile(0.95)()`

**Time ranges:** `NOW() - INTERVAL '1' HOUR`, `BETWEEN '2026-01-01' AND '2026-01-31'`

### Query Examples

```sql
-- Top endpoints
SELECT blob1, COUNT(*) AS requests, AVG(double1) AS avg_latency
FROM api_requests WHERE timestamp >= NOW() - INTERVAL '24' HOUR
GROUP BY blob1 ORDER BY requests DESC LIMIT 20

-- Error rate
SELECT blob1, COUNT(*) AS total,
  SUM(CASE WHEN blob3 LIKE '5%' THEN 1 ELSE 0 END) AS errors
FROM api_requests WHERE timestamp >= NOW() - INTERVAL '1' HOUR
GROUP BY blob1 HAVING total > 50

-- P95 latency
SELECT blob1, quantile(0.95)(double1) AS p95
FROM api_requests GROUP BY blob1
```

