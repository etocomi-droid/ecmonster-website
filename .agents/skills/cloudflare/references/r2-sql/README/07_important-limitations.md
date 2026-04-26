## Important Limitations

**CRITICAL: No Workers Binding**
- R2 SQL cannot be called directly from Workers/Pages code
- For programmatic access, use HTTP API from external systems
- Or query via PyIceberg, Spark, etc. (see r2-data-catalog reference)

**SQL Feature Set:**
- No JOINs, CTEs, subqueries, window functions
- ORDER BY supports aggregation columns (not just partition keys)
- LIMIT max 10,000 (default 500)
- See [gotchas.md](gotchas.md) for complete limitations

