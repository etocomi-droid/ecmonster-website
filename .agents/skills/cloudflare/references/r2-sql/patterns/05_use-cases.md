## Use Cases

### Log Analytics
```sql
-- Error rate by endpoint
SELECT path, COUNT(*), SUM(CASE WHEN status >= 400 THEN 1 ELSE 0 END) as errors
FROM logs.http_requests
WHERE timestamp BETWEEN '2025-01-01T00:00:00Z' AND '2025-01-31T23:59:59Z'
GROUP BY path ORDER BY errors DESC LIMIT 20;

-- Response time stats
SELECT method, MIN(response_time_ms), AVG(response_time_ms), MAX(response_time_ms)
FROM logs.http_requests WHERE timestamp >= '2025-01-15T00:00:00Z' GROUP BY method;

-- Traffic by status
SELECT status, COUNT(*) FROM logs.http_requests
WHERE timestamp >= '2025-01-15T00:00:00Z' AND method = 'GET'
GROUP BY status ORDER BY COUNT(*) DESC;
```

### Fraud Detection
```sql
-- High-value transactions
SELECT location, COUNT(*), SUM(amount), AVG(amount)
FROM fraud.transactions WHERE transaction_timestamp >= '2025-01-01T00:00:00Z' AND amount > 1000.0
GROUP BY location ORDER BY SUM(amount) DESC LIMIT 20;

-- Flagged transactions
SELECT merchant_category, COUNT(*), AVG(amount) FROM fraud.transactions
WHERE is_fraud_flag = true AND transaction_timestamp >= '2025-01-01T00:00:00Z'
GROUP BY merchant_category HAVING COUNT(*) > 10 ORDER BY COUNT(*) DESC;
```

### Business Intelligence
```sql
-- Sales by department
SELECT department, SUM(revenue), AVG(revenue), COUNT(*) FROM sales.transactions
WHERE sale_date >= '2024-01-01' GROUP BY department ORDER BY SUM(revenue) DESC LIMIT 10;

-- Product performance
SELECT category, COUNT(DISTINCT product_id), SUM(units_sold), SUM(revenue)
FROM sales.product_sales WHERE sale_date BETWEEN '2024-10-01' AND '2024-12-31'
GROUP BY category ORDER BY SUM(revenue) DESC;
```

