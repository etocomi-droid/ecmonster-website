## Architecture Overview

**Query Planner:**
- Top-down metadata investigation with multi-layer pruning
- Partition-level, column-level, and row-group pruning
- Streaming pipeline - execution starts before planning completes
- Early termination with LIMIT - stops when result complete

**Query Execution:**
- Coordinator distributes work to workers across Cloudflare network
- Workers run Apache DataFusion for parallel query execution
- Parquet column pruning - reads only required columns
- Ranged reads from R2 for efficiency

**Aggregation Strategies:**
- Scatter-gather - simple aggregations (SUM, COUNT, AVG)
- Shuffling - ORDER BY/HAVING on aggregates via hash partitioning

