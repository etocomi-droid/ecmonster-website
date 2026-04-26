## Pattern 1: Log Analytics Pipeline

Ingest logs incrementally, query by time/level.

```python
import pyarrow as pa
from datetime import datetime
from pyiceberg.schema import Schema
from pyiceberg.types import NestedField, TimestampType, StringType, IntegerType
from pyiceberg.partitioning import PartitionSpec, PartitionField
from pyiceberg.transforms import DayTransform

# Create partitioned table (once)
schema = Schema(
    NestedField(1, "timestamp", TimestampType(), required=True),
    NestedField(2, "level", StringType(), required=True),
    NestedField(3, "service", StringType(), required=True),
    NestedField(4, "message", StringType(), required=False),
)

partition_spec = PartitionSpec(
    PartitionField(source_id=1, field_id=1000, transform=DayTransform(), name="day")
)

catalog.create_namespace("logs")
table = catalog.create_table(("logs", "app_logs"), schema=schema, partition_spec=partition_spec)

# Append logs (incremental)
data = pa.table({
    "timestamp": [datetime(2026, 1, 27, 10, 30, 0)],
    "level": ["ERROR"],
    "service": ["auth-service"],
    "message": ["Failed login"],
})
table.append(data)

# Query by time + level (leverages partitioning)
scan = table.scan(row_filter="level = 'ERROR' AND day = '2026-01-27'")
errors = scan.to_pandas()
```

