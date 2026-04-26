## LIMIT Clause

```sql
SELECT * FROM logs.requests LIMIT 100;
```

| Setting | Value |
|---------|-------|
| Min | 1 |
| Max | 10,000 |
| Default | 500 |

**Always use LIMIT** to enable early termination optimization.

