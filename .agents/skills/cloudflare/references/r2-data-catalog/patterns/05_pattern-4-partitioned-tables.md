## Pattern 4: Partitioned Tables

```python
from pyiceberg.partitioning import PartitionSpec, PartitionField
from pyiceberg.transforms import DayTransform, IdentityTransform

# Partition by day + country
partition_spec = PartitionSpec(
    PartitionField(source_id=1, field_id=1000, transform=DayTransform(), name="day"),
    PartitionField(source_id=2, field_id=1001, transform=IdentityTransform(), name="country"),
)
table = catalog.create_table(("events", "user_events"), schema=schema, partition_spec=partition_spec)

# Queries prune partitions automatically
scan = table.scan(row_filter="country = 'US' AND day = '2026-01-27'")
```

