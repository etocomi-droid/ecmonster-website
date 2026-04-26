## Client Configuration

### PyIceberg

```python
from pyiceberg.catalog.rest import RestCatalog

catalog = RestCatalog(
    name="my_catalog",
    warehouse="<bucket-name>",           # Same as bucket name
    uri="<catalog-uri>",                 # From enable command
    token="<api-token>",                 # From token creation
)
```

**Full example with credentials:**
```python
import os
from pyiceberg.catalog.rest import RestCatalog

# Store credentials in environment variables
WAREHOUSE = os.getenv("R2_WAREHOUSE")      # e.g., "my-bucket"
CATALOG_URI = os.getenv("R2_CATALOG_URI")  # e.g., "https://abc123.r2.cloudflarestorage.com/iceberg/my-bucket"
TOKEN = os.getenv("R2_TOKEN")              # API token

catalog = RestCatalog(
    name="r2_catalog",
    warehouse=WAREHOUSE,
    uri=CATALOG_URI,
    token=TOKEN,
)

# Test connection
print(catalog.list_namespaces())
```

### Spark / Trino / DuckDB

See [patterns.md](patterns.md) for integration examples with other query engines.

