## Limits

| Limit | Value | Notes |
|-------|-------|-------|
| Max tail consumers per producer | 10 | Each receives all events independently |
| Events batch size | Up to 100 events per invocation | Larger batches split across invocations |
| Tail Worker CPU time | Same as regular Workers | 10ms (free), 30ms (paid), 50ms (paid bundle) |
| Pricing tier | Workers Paid or Enterprise | Not available on free plan |
| Request body size | 100 MB max | When sending to external endpoints |
| Event retention | None | Events not retried if tail handler fails |

