## Bandwidth and Rate Limits

| Limit | Value | Notes |
|-------|-------|-------|
| Request size | 100 MB | Single HTTP request |
| Upload speed | No hard limit | Governed by network/plan |
| Concurrent connections | 1000 per tunnel | Across all replicas |
| Requests per second | No limit | Subject to DDoS detection |

**Large file transfers:**
Use R2 or Workers with chunked uploads instead of streaming through tunnel.
