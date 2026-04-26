## Limits

| Resource | Limit | Notes |
|----------|-------|-------|
| Namespaces per catalog | No hard limit | Organize tables logically |
| Tables per namespace | <10,000 recommended | Performance degrades beyond this |
| Files per table | <100,000 recommended | Run compaction regularly |
| Snapshots per table | Configurable retention | Expire >7 days old |
| Partitions per table | 100-1,000 optimal | Too many = slow metadata ops |
| Table size | Same as R2 bucket | 10GB-10TB+ common |
| API rate limits | Standard R2 API limits | Shared with R2 storage operations |
| Target file size | 128-512 MB | After compaction |

