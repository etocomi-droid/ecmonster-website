## Environment Variables Pattern

```bash
# .env (never commit)
R2_CATALOG_URI=https://<account-id>.r2.cloudflarestorage.com/iceberg/<bucket>
R2_WAREHOUSE=<bucket-name>
R2_TOKEN=<api-token>
```

```python
import os
from pyiceberg.catalog.rest import RestCatalog

catalog = RestCatalog(
    name="r2",
    uri=os.getenv("R2_CATALOG_URI"),
    warehouse=os.getenv("R2_WAREHOUSE"),
    token=os.getenv("R2_TOKEN"),
)
```

