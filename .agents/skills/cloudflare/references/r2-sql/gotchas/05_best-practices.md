## Best Practices

### Partitioning
- **Time-series:** Partition by day/hour on timestamp
- **Avoid:** High-cardinality keys (user_id), >10,000 partitions

```python
from pyiceberg.partitioning import PartitionSpec, PartitionField
from pyiceberg.transforms import DayTransform

PartitionSpec(PartitionField(source_id=1, field_id=1000, transform=DayTransform(), name="day"))
```

### Query Writing
- **Always use LIMIT** for early termination
- **Filter on partition keys first** for pruning
- **Combine filters with AND** for more pruning

```sql
-- Good
WHERE timestamp >= '2025-01-15T00:00:00Z' AND status = 404 AND method = 'GET' LIMIT 100
```

### Type Safety
- Quote strings: `'GET'` not `GET`
- RFC3339 timestamps: `'2025-01-01T00:00:00Z'` not `'2025-01-01'`
- ISO dates: `'2025-01-15'` not `'01/15/2025'`

### Data Organization
- **Pipelines:** Dev `roll_file_time: 10`, Prod `roll_file_time: 300+`
- **Compression:** Use `zstd`
- **Maintenance:** Compaction for small files, expire old snapshots

