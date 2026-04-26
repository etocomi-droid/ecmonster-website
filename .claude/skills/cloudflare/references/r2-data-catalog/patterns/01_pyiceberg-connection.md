## PyIceberg Connection

```python
import os
from pyiceberg.catalog.rest import RestCatalog
from pyiceberg.exceptions import NamespaceAlreadyExistsError

catalog = RestCatalog(
    name="r2_catalog",
    warehouse=os.getenv("R2_WAREHOUSE"),      # bucket name
    uri=os.getenv("R2_CATALOG_URI"),          # catalog endpoint
    token=os.getenv("R2_TOKEN"),              # API token
)

# Create namespace (idempotent)
try:
    catalog.create_namespace("default")
except NamespaceAlreadyExistsError:
    pass
```

