### Analytics Engine SQL API

**Endpoint**: `https://api.cloudflare.com/client/v4/accounts/{account_id}/analytics_engine/sql`

**Authentication**: `Authorization: Bearer <API_TOKEN>` (Account Analytics Read permission)

**Common Queries**:

```sql
-- List all datasets
SHOW TABLES;

-- Time-series aggregation (5-minute buckets)
SELECT
  intDiv(toUInt32(timestamp), 300) * 300 AS time_bucket,
  blob1 AS endpoint,
  SUM(_sample_interval) AS total_requests,
  AVG(double1) AS avg_response_time_ms
FROM api_metrics
WHERE timestamp >= NOW() - INTERVAL '24' HOUR
GROUP BY time_bucket, endpoint
ORDER BY time_bucket DESC;

-- Top customers by usage
SELECT
  index1 AS customer_id,
  SUM(_sample_interval * double1) AS total_api_calls,
  AVG(double2) AS avg_response_time_ms
FROM api_usage
WHERE timestamp >= NOW() - INTERVAL '7' DAY
GROUP BY customer_id
ORDER BY total_api_calls DESC
LIMIT 100;

-- Error rate analysis
SELECT
  blob1 AS error_type,
  COUNT(*) AS occurrences,
  MAX(timestamp) AS last_seen
FROM error_tracking
WHERE timestamp >= NOW() - INTERVAL '1' HOUR
GROUP BY error_type
ORDER BY occurrences DESC;
```

