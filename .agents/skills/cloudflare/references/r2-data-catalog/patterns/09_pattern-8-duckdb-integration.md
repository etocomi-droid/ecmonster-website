## Pattern 8: DuckDB Integration

```python
import duckdb

arrow_table = table.scan().to_arrow()
con = duckdb.connect()
con.register("logs", arrow_table)
result = con.execute("SELECT level, COUNT(*) FROM logs GROUP BY level").fetchdf()
```

