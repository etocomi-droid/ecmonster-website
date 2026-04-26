## Pattern 2: Time-Travel Queries

```python
from datetime import datetime, timedelta

table = catalog.load_table(("logs", "app_logs"))

# Query specific snapshot
snapshot_id = table.current_snapshot().snapshot_id
data = table.scan(snapshot_id=snapshot_id).to_pandas()

# Query as of timestamp (yesterday)
yesterday_ms = int((datetime.now() - timedelta(days=1)).timestamp() * 1000)
data = table.scan(as_of_timestamp=yesterday_ms).to_pandas()
```

