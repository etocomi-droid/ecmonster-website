## Enable R2 Data Catalog

R2 SQL queries Apache Iceberg tables in R2 Data Catalog. Must enable catalog on bucket first.

### Via Wrangler CLI

```bash
npx wrangler r2 bucket catalog enable <bucket-name>
```

Output includes:
- **Warehouse name** - Typically same as bucket name
- **Catalog URI** - REST endpoint for catalog operations

Example output:
```
Catalog enabled successfully
Warehouse: my-bucket
Catalog URI: https://abc123.r2.cloudflarestorage.com/iceberg/my-bucket
```

### Via Dashboard

1. Navigate to **R2 Object Storage** → Select your bucket
2. Click **Settings** tab
3. Scroll to **R2 Data Catalog** section
4. Click **Enable**
5. Note the **Catalog URI** and **Warehouse** name

**Important:** Enabling catalog creates metadata directories in bucket but does not modify existing objects.

