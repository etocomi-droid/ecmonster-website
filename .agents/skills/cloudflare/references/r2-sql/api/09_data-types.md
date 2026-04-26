## Data Types

| Type | SQL Literal | Example |
|------|-------------|---------|
| `integer` | Unquoted number | `42`, `-10` |
| `float` | Decimal number | `3.14`, `-0.5` |
| `string` | Single quotes | `'hello'`, `'GET'` |
| `boolean` | Keyword | `true`, `false` |
| `timestamp` | RFC3339 string | `'2025-01-01T00:00:00Z'` |
| `date` | ISO 8601 date | `'2025-01-01'` |

### Type Safety

- Quote strings with single quotes: `'value'`
- Timestamps must be RFC3339: `'2025-01-01T00:00:00Z'` (include timezone)
- Dates must be ISO 8601: `'2025-01-01'` (YYYY-MM-DD)
- No implicit conversions

```sql
-- ✅ Correct
WHERE status = 200 AND method = 'GET' AND timestamp > '2025-01-01T00:00:00Z'

-- ❌ Wrong
WHERE status = '200'              -- string instead of integer
WHERE timestamp > '2025-01-01'    -- missing time/timezone
WHERE method = GET                -- unquoted string
```

