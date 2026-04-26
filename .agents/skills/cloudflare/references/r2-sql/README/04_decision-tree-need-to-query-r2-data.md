## Decision Tree: Need to Query R2 Data?

```
Do you need to query structured data in R2?
├─ YES, data is in Iceberg tables
│  ├─ Need SQL interface? → Use R2 SQL (this reference)
│  ├─ Need Python API? → See r2-data-catalog reference (PyIceberg)
│  └─ Need other engine? → See r2-data-catalog reference (Spark, Trino, etc.)
│
├─ YES, but not in Iceberg format
│  ├─ Streaming data? → Use Pipelines to write to Data Catalog, then R2 SQL
│  └─ Static files? → Use PyIceberg to create Iceberg tables, then R2 SQL
│
└─ NO, just need object storage → Use R2 reference (not R2 SQL)
```

