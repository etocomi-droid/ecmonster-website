## Pattern 5: Table Maintenance

```python
from datetime import datetime, timedelta

table = catalog.load_table(("logs", "app_logs"))

# Compact → expire → cleanup (in order)
table.rewrite_data_files(target_file_size_bytes=128 * 1024 * 1024)
seven_days_ms = int((datetime.now() - timedelta(days=7)).timestamp() * 1000)
table.expire_snapshots(older_than=seven_days_ms, retain_last=10)
three_days_ms = int((datetime.now() - timedelta(days=3)).timestamp() * 1000)
table.delete_orphan_files(older_than=three_days_ms)
```

See [api.md](api.md#table-maintenance) for detailed parameters.

