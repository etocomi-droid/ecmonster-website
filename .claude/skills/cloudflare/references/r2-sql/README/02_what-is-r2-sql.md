## What is R2 SQL?

R2 SQL is Cloudflare's **serverless distributed analytics query engine** for querying Apache Iceberg tables in R2 Data Catalog. Features:

- **Serverless** - No clusters to manage, no infrastructure
- **Distributed** - Leverages Cloudflare's global network for parallel execution
- **SQL interface** - Familiar SQL syntax for analytics queries
- **Zero egress fees** - Query from any cloud/region without data transfer costs
- **Open beta** - Free during beta (standard R2 storage costs apply)

### What is Apache Iceberg?

Open table format for large-scale analytics datasets in object storage:
- **ACID transactions** - Safe concurrent reads/writes
- **Metadata optimization** - Fast queries without full table scans
- **Schema evolution** - Add/rename/drop columns without rewrites
- **Partitioning** - Organize data for efficient pruning

