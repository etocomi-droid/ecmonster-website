## Limits

| Resource | Recommended | Impact if Exceeded |
|----------|-------------|-------------------|
| Tables/namespace | <10k | Slow list ops |
| Files/table | <100k | Slow query planning |
| Partitions/table | 100-1k | Metadata overhead |
| Snapshots/table | Expire >7d | Metadata bloat |

