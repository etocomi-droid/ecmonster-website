## When to Use

**Use R2 SQL for:**
- **Log analytics** - Query application/system logs with WHERE filters and aggregations
- **BI dashboards** - Generate reports from large analytical datasets
- **Fraud detection** - Analyze transaction patterns with GROUP BY/HAVING
- **Multi-cloud analytics** - Query data from any cloud without egress fees
- **Ad-hoc exploration** - Run SQL queries on Iceberg tables via Wrangler CLI

**Don't use R2 SQL for:**
- **Workers/Pages runtime** - R2 SQL has no Workers binding, use HTTP API from external systems
- **Real-time queries (<100ms)** - Optimized for analytical batch queries, not OLTP
- **Complex joins/CTEs** - Limited SQL feature set (no JOINs, subqueries, CTEs currently)
- **Small datasets (<1GB)** - Setup overhead not justified

