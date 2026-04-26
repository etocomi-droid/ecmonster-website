## SQL Feature Limitations

| Feature | Supported | Notes |
|---------|-----------|-------|
| SELECT, WHERE, GROUP BY, HAVING | ✅ | Standard support |
| COUNT, SUM, AVG, MIN, MAX | ✅ | Standard aggregations |
| ORDER BY partition/aggregation | ✅ | See above |
| LIMIT | ✅ | Max 10,000 |
| Column aliases | ❌ | No AS alias |
| Expressions in SELECT | ❌ | No col1 + col2 |
| ORDER BY non-partition | ❌ | Fails at runtime |
| JOINs, subqueries, CTEs | ❌ | Denormalize at write time |
| Window functions, UNION | ❌ | Use external engines |
| INSERT/UPDATE/DELETE | ❌ | Use PyIceberg/Pipelines |
| Nested columns, arrays, JSON | ❌ | Flatten at write time |

**Workarounds:**
- No JOINs: Denormalize data or use Spark/PyIceberg
- No subqueries: Split into multiple queries
- No aliases: Accept generated names, transform in app

