## Pattern 3: Schema Evolution

```python
from pyiceberg.types import StringType

table = catalog.load_table(("users", "profiles"))

with table.update_schema() as update:
    update.add_column("email", StringType(), required=False)
    update.rename_column("name", "full_name")
# Old readers ignore new columns, new readers see nulls for old data
```

