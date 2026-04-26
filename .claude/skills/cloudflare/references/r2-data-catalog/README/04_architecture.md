## Architecture

```
┌─────────────────────────────────────────────────┐
│  Query Engines                                  │
│  (PyIceberg, Spark, Trino, Snowflake, DuckDB)  │
└────────────────┬────────────────────────────────┘
                 │
                 │ REST API (OAuth2 token)
                 ▼
┌─────────────────────────────────────────────────┐
│  R2 Data Catalog (Managed Iceberg REST Catalog)│
│  • Namespace/table metadata                     │
│  • Transaction coordination                     │
│  • Snapshot management                          │
└────────────────┬────────────────────────────────┘
                 │
                 │ Vended credentials
                 ▼
┌─────────────────────────────────────────────────┐
│  R2 Bucket Storage                              │
│  • Parquet data files                           │
│  • Metadata files                               │
│  • Manifest files                               │
└─────────────────────────────────────────────────┘
```

**Key concepts:**
- **Catalog URI** - REST endpoint for catalog operations (e.g., `https://<account-id>.r2.cloudflarestorage.com/iceberg/<bucket>`)
- **Warehouse** - Logical grouping of tables (typically same as bucket name)
- **Namespace** - Schema/database containing tables (e.g., `logs`, `analytics`)
- **Table** - Iceberg table with schema, data files, snapshots
- **Vended credentials** - Temporary S3 credentials catalog provides for data access

