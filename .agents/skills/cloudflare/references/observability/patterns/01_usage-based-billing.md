## Usage-Based Billing

```typescript
env.ANALYTICS.writeDataPoint({
  blobs: [customerId, request.url, request.method],
  doubles: [1], // request_count
  indexes: [customerId]
});
```

```sql
SELECT blob1 AS customer_id, SUM(_sample_interval * double1) AS total_calls
FROM api_usage WHERE timestamp >= DATE_TRUNC('month', NOW())
GROUP BY customer_id
```

