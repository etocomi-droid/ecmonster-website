## What is R2 Data Catalog?

R2 Data Catalog is a **managed Apache Iceberg REST catalog** built directly into R2 buckets. It provides:

- **Apache Iceberg tables** - ACID transactions, schema evolution, time-travel queries
- **Zero-egress costs** - Query from any cloud/region without data transfer fees
- **Standard REST API** - Works with Spark, PyIceberg, Snowflake, Trino, DuckDB
- **No infrastructure** - Fully managed, no catalog servers to run
- **Public beta** - Available to all R2 subscribers, no extra cost beyond R2 storage

### What is Apache Iceberg?

Open table format for analytics datasets in object storage. Features:
- **ACID transactions** - Safe concurrent reads/writes
- **Metadata optimization** - Fast queries without full scans
- **Schema evolution** - Add/rename/delete columns without rewrites
- **Time-travel** - Query historical snapshots
- **Partitioning** - Organize data for efficient queries

