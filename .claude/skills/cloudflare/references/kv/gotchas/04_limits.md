## Limits

| Limit | Value | Notes |
|-------|-------|-------|
| Key size | 512 bytes | Maximum key length |
| Value size | 25 MiB | Maximum value; 413 error if exceeded |
| Metadata size | 1024 bytes | Maximum metadata per key |
| cacheTtl minimum | 60s | Minimum cache TTL |
| Write rate per key | 1 write/second | All plans; 429 error if exceeded |
| Propagation time | ≤60s | Global propagation time |
| Bulk get max | 100 keys | Maximum keys per bulk operation |
| Operations per Worker | 1,000 | Per request (bulk counts as 1) |
| Reads pricing | $0.50 per 10M | Per million reads |
| Writes pricing | $5.00 per 1M | Per million writes |
| Deletes pricing | $5.00 per 1M | Per million deletes |
| Storage pricing | $0.50 per GB-month | Per GB per month |
