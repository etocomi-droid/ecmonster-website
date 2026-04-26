## Limits Reference

| Resource | Limit | Impact | Plan |
|----------|-------|--------|------|
| **Bindings per Worker** | 64 total | All binding types combined | All |
| **Environment variables** | 64 max, 5KB each | Per Worker | All |
| **Secret size** | 1KB | Per secret | All |
| **KV key size** | 512 bytes | UTF-8 encoded | All |
| **KV value size** | 25 MB | Per value | All |
| **KV writes per key** | 1/second | Per key; exceeding = 429 error | All |
| **KV list() results** | 1000 keys | Per call; use cursor for more | All |
| **KV operations** | 1000 reads/day | Free tier only | Free |
| **R2 object size** | 5 TB | Per object | All |
| **R2 operations** | 1M Class A/month free | Writes | All |
| **D1 database size** | 10 GB | Per database | All |
| **D1 rows per query** | 100,000 | Result set limit | All |
| **D1 databases** | 10 | Free tier | Free |
| **Queue batch size** | 100 messages | Per consumer batch | All |
| **Queue message size** | 128 KB | Per message | All |
| **Service binding calls** | Unlimited | Counts toward CPU time | All |
| **Durable Objects** | 1M requests/month free | First 1M | Free |

