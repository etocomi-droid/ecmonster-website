## Best Practices

| Area | Guideline |
|------|-----------|
| **Partitioning** | Use day/hour for time-series; 100-1000 partitions; avoid high cardinality |
| **File sizes** | Target 128-512MB; compact when avg <10MB or >10k files |
| **Schema** | Add columns as nullable (`required=False`); batch changes |
| **Maintenance** | Compact high-write daily/weekly; expire snapshots 7-30d; cleanup orphans after |
| **Concurrency** | Reads automatic; writes to different partitions safe; retry same partition |
| **Performance** | Filter on partitions; select only needed columns; batch appends 100MB+ |
