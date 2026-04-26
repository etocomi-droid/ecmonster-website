## Which Sink Type?

```
Need SQL queries on data?
  → R2 Data Catalog (Iceberg)
    ✅ ACID transactions, time-travel, schema evolution
    ❌ More setup complexity (namespace, table, catalog token)

Just file storage/archival?
  → R2 Storage (Parquet)
    ✅ Simple, direct file access
    ❌ No built-in SQL queries

Using external tools (Spark/Athena)?
  → R2 Storage (Parquet with partitioning)
    ✅ Standard format, partition pruning for performance
    ❌ Must manage schema compatibility yourself
```

