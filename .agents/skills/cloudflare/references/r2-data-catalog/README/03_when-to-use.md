## When to Use

**Use R2 Data Catalog for:**
- **Log analytics** - Store and query application/system logs
- **Data lakes/warehouses** - Analytical datasets queried by multiple engines
- **BI pipelines** - Aggregate data for dashboards and reports
- **Multi-cloud analytics** - Share data across clouds without egress fees
- **Time-series data** - Event streams, metrics, sensor data

**Don't use for:**
- **Transactional workloads** - Use D1 or external database instead
- **Sub-second latency** - Iceberg optimized for batch/analytical queries
- **Small datasets (<1GB)** - Setup overhead not worth it
- **Unstructured data** - Store files directly in R2, not as Iceberg tables

