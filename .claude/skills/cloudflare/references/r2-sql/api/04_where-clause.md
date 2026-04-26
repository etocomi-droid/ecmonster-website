## WHERE Clause

### Operators

| Operator | Example |
|----------|---------|
| `=`, `!=`, `<`, `<=`, `>`, `>=` | `status = 200` |
| `LIKE` | `user_agent LIKE '%Chrome%'` |
| `BETWEEN` | `timestamp BETWEEN '2025-01-01T00:00:00Z' AND '2025-01-31T23:59:59Z'` |
| `IS NULL`, `IS NOT NULL` | `email IS NOT NULL` |
| `AND`, `OR` | `status = 200 AND method = 'GET'` |

Use parentheses for precedence: `(status = 404 OR status = 500) AND method = 'POST'`

