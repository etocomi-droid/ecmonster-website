## Table Maintenance

### Compaction

```python
files = table.scan().plan_files()
avg_mb = sum(f.file_size_in_bytes for f in files) / len(files) / (1024**2)
print(f"Files: {len(files)}, Avg: {avg_mb:.1f} MB")

table.rewrite_data_files(target_file_size_bytes=128 * 1024 * 1024)
```

**When:** Avg <10MB or >1000 files. **Frequency:** High-write daily, medium weekly.

### Snapshot Expiration

```python
from datetime import datetime, timedelta

seven_days_ms = int((datetime.now() - timedelta(days=7)).timestamp() * 1000)
table.expire_snapshots(older_than=seven_days_ms, retain_last=10)
```

**Retention:** Production 7-30d, dev 1-7d, audit 90+d.

### Orphan Cleanup

```python
three_days_ms = int((datetime.now() - timedelta(days=3)).timestamp() * 1000)
table.delete_orphan_files(older_than=three_days_ms)
```

⚠️ Always expire snapshots first, use 3+ day threshold, run during low traffic.

### Full Maintenance

```python
# Compact → Expire → Cleanup (in order)
if len(table.scan().plan_files()) > 1000:
    table.rewrite_data_files(target_file_size_bytes=128 * 1024 * 1024)
seven_days_ms = int((datetime.now() - timedelta(days=7)).timestamp() * 1000)
table.expire_snapshots(older_than=seven_days_ms, retain_last=10)
three_days_ms = int((datetime.now() - timedelta(days=3)).timestamp() * 1000)
table.delete_orphan_files(older_than=three_days_ms)
```

