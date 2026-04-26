## Performance Tips

| Scenario | Recommendation | Why |
|----------|----------------|-----|
| Large values (>1MB) | Use `stream` type | Avoids buffering entire value in memory |
| Many small keys | Coalesce into one JSON object | Reduces operations, improves cache hit rate |
| High write volume | Spread across different keys | Avoid 1 write/second per-key limit |
| Cold reads | Increase `cacheTtl` parameter | Reduces latency for frequently-read data |
| Bulk operations | Use array form of get() | Single operation, better performance |

