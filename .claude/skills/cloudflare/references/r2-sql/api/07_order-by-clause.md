## ORDER BY Clause

Sort results by:
- **Partition key columns** - Always supported
- **Aggregation functions** - Supported via shuffle strategy

```sql
-- Order by partition key
SELECT * FROM logs.requests ORDER BY timestamp DESC LIMIT 100;

-- Order by aggregation (repeat function, aliases not supported)
SELECT region, SUM(amount)
FROM sales.transactions
GROUP BY region
ORDER BY SUM(amount) DESC;
```

**Limitations:** Cannot order by non-partition columns. See [gotchas.md](gotchas.md#order-by-limitations)

