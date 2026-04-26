## Limits in Playground

Same as production Free plan:

| Resource | Limit | Notes |
|----------|-------|-------|
| CPU time | 10ms | Per request |
| Memory | 128 MB | Per request |
| Script size | 1 MB | After compression |
| Subrequests | 50 | Outbound fetch calls |
| Request size | 100 MB | Incoming |
| Response size | Unlimited | Outgoing (streamed) |

**Exceeding CPU time** throws error immediately. Optimize hot paths or upgrade to Paid plan (50ms CPU).
