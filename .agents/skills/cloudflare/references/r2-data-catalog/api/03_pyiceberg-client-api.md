## PyIceberg Client API

Most users use PyIceberg, not raw REST.

### Connection

```python
from pyiceberg.catalog.rest import RestCatalog

catalog = RestCatalog(
    name="my_catalog",
    warehouse="<bucket-name>",
    uri="<catalog-uri>",
    token="<api-token>",
)
```

### Namespace Operations

```python
from pyiceberg.exceptions import NamespaceAlreadyExistsError

namespaces = catalog.list_namespaces()  # [('default',), ('logs',)]
catalog.create_namespace("logs", properties={"owner": "team"})
catalog.drop_namespace("logs")  # Must be empty
```

### Table Operations

```python
from pyiceberg.schema import Schema
from pyiceberg.types import NestedField, StringType, IntegerType

schema = Schema(
    NestedField(1, "id", IntegerType(), required=True),
    NestedField(2, "name", StringType(), required=False),
)
table = catalog.create_table(("logs", "app_logs"), schema=schema)
tables = catalog.list_tables("logs")
table = catalog.load_table(("logs", "app_logs"))
catalog.rename_table(("logs", "old"), ("logs", "new"))
```

### Data Operations

```python
import pyarrow as pa

data = pa.table({"id": [1, 2], "name": ["Alice", "Bob"]})
table.append(data)
table.overwrite(data)

# Read with filters
scan = table.scan(row_filter="id > 100", selected_fields=["id", "name"])
df = scan.to_pandas()
```

### Schema Evolution

```python
from pyiceberg.types import IntegerType, LongType

with table.update_schema() as update:
    update.add_column("user_id", IntegerType(), doc="User ID")
    update.rename_column("msg", "message")
    update.delete_column("old_field")
    update.update_column("id", field_type=LongType())  # int→long only
```

### Time-Travel

```python
from datetime import datetime, timedelta

# Query specific snapshot or timestamp
scan = table.scan(snapshot_id=table.snapshots()[-2].snapshot_id)
yesterday_ms = int((datetime.now() - timedelta(days=1)).timestamp() * 1000)
scan = table.scan(as_of_timestamp=yesterday_ms)
```

### Partitioning

```python
from pyiceberg.partitioning import PartitionSpec, PartitionField
from pyiceberg.transforms import DayTransform
from pyiceberg.types import TimestampType

partition_spec = PartitionSpec(
    PartitionField(source_id=1, field_id=1000, transform=DayTransform(), name="day")
)
table = catalog.create_table(("events", "actions"), schema=schema, partition_spec=partition_spec)
scan = table.scan(row_filter="day = '2026-01-27'")  # Prunes partitions
```

