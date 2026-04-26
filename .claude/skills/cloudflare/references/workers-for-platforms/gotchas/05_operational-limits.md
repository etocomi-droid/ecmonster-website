## Operational Limits

| Operation | Limit | Notes |
|-----------|-------|-------|
| CPU time (custom limits) | Up to Workers plan limit | Set per-invocation in dispatch worker |
| Subrequests (custom limits) | Up to Workers plan limit | Set per-invocation in dispatch worker |
| Outbound Worker subrequests | Not intercepted for DO/mTLS | Only regular fetch() calls |
| TCP sockets with outbound | Disabled | `connect()` API unavailable |

See [README.md](./README.md), [configuration.md](./configuration.md), [api.md](./api.md), [patterns.md](./patterns.md)
