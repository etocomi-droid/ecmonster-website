## SQL Functions Quick Reference

Available in `INSERT INTO sink SELECT ... FROM stream` transformations:

| Function | Example | Use Case |
|----------|---------|----------|
| `UPPER(s)` | `UPPER(event_type)` | Normalize strings |
| `LOWER(s)` | `LOWER(email)` | Case-insensitive matching |
| `CONCAT(...)` | `CONCAT(user_id, '_', product_id)` | Generate composite keys |
| `CASE WHEN ... THEN ... END` | `CASE WHEN amount > 100 THEN 'high' ELSE 'low' END` | Conditional enrichment |
| `CAST(x AS type)` | `CAST(timestamp AS string)` | Type conversion |
| `COALESCE(x, y)` | `COALESCE(amount, 0.0)` | Default values |
| Math operators | `amount * 1.1`, `price / quantity` | Calculations |
| Comparison | `amount > 100`, `status IN ('active', 'pending')` | Filtering |

**String types for CAST:** `string`, `int32`, `int64`, `float32`, `float64`, `bool`, `timestamp`

Full reference: [Pipelines SQL Reference](https://developers.cloudflare.com/pipelines/sql-reference/)

