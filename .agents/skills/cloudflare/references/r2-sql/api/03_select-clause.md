## SELECT Clause

```sql
-- All columns
SELECT * FROM logs.http_requests;

-- Specific columns
SELECT user_id, timestamp, status FROM logs.http_requests;
```

**Limitations:** No column aliases, expressions, or nested column access

