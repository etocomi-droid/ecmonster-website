## Pattern 7: Upsert Simulation

```python
import pandas as pd
import pyarrow as pa

# Read → merge → overwrite (not atomic, use Spark MERGE INTO for production)
existing = table.scan().to_pandas()
new_data = pd.DataFrame({"id": [1, 3], "value": [100, 300]})
merged = pd.concat([existing, new_data]).drop_duplicates(subset=["id"], keep="last")
table.overwrite(pa.Table.from_pandas(merged))
```

