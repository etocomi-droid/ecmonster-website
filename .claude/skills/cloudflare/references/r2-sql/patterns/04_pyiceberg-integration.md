## PyIceberg Integration

Create and populate Iceberg tables with PyIceberg, then query with R2 SQL.

```python
from pyiceberg.catalog.rest import RestCatalog
import pyarrow as pa
import pandas as pd

# Setup catalog
catalog = RestCatalog(
    name="my_catalog",
    warehouse="my-bucket",
    uri="https://<account-id>.r2.cloudflarestorage.com/iceberg/my-bucket",
    token="<your-token>",
)
catalog.create_namespace_if_not_exists("analytics")

# Create table
schema = pa.schema([
    pa.field("user_id", pa.string(), nullable=False),
    pa.field("event_time", pa.timestamp("us", tz="UTC"), nullable=False),
    pa.field("page_views", pa.int64(), nullable=False),
])
table = catalog.create_table(("analytics", "user_metrics"), schema=schema)

# Append data
df = pd.DataFrame({
    "user_id": ["user_1", "user_2"],
    "event_time": pd.to_datetime(["2025-01-15 10:00:00", "2025-01-15 11:00:00"], utc=True),
    "page_views": [10, 25],
})
table.append(pa.Table.from_pandas(df, schema=schema))
```

Query with R2 SQL:
```bash
npx wrangler r2 sql query "my-bucket" "
  SELECT user_id, SUM(page_views)
  FROM analytics.user_metrics
  WHERE event_time >= '2025-01-15T00:00:00Z'
  GROUP BY user_id
"
```

See [r2-data-catalog/patterns.md](../r2-data-catalog/patterns.md) for advanced PyIceberg patterns.

