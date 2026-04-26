## HAVING Clause

Filter aggregated results (after GROUP BY):

```sql
SELECT category, SUM(amount)
FROM sales.transactions
GROUP BY category
HAVING SUM(amount) > 10000;
```

