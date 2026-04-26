## Rate Limits

| Limit | Value |
|-------|-------|
| GraphQL queries per user | **Default 300 per 5 minutes** (max 320, at least 1/sec) |
| General API rate limit | 1200 requests per 5 minutes (shared across all API calls) |
| Zone scope per query | Up to **10 zones** |
| Account scope per query | Exactly **1 account** |

The GraphQL rate limit is separate from the general API limit. Exceeding either results in `HTTP 429` and blocks all API calls for 5 minutes. Enterprise customers can contact support to raise limits.

### "429 Too Many Requests"

**Cause:** Exceeded rate limit.

**Solution:** Batch multiple datasets into single queries, cache results, increase intervals between queries. Use `{ viewer { budget } }` to monitor remaining budget.

