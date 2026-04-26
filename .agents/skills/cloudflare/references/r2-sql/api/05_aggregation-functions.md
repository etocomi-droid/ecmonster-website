## Aggregation Functions

| Function | Description |
|----------|-------------|
| `COUNT(*)` | Count all rows |
| `COUNT(column)` | Count non-null values |
| `COUNT(DISTINCT column)` | Count unique values |
| `SUM(column)`, `AVG(column)` | Numeric aggregations |
| `MIN(column)`, `MAX(column)` | Min/max values |

```sql
-- Multiple aggregations with GROUP BY
SELECT region, COUNT(*), SUM(amount), AVG(amount)
FROM sales.transactions
WHERE sale_date >= '2024-01-01'
GROUP BY region;
```

