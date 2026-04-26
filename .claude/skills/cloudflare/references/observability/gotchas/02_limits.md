## Limits

| Resource/Limit | Value | Notes |
|----------------|-------|-------|
| Max log size | 256 KB | Logs exceeding this are truncated |
| Default sampling rate | 1.0 (100%) | Reduce for high-traffic Workers |
| Max destinations | Varies by plan | Check dashboard |
| Trace context propagation | 100 spans max | Deep call chains may lose spans |
| Analytics Engine write rate | 25 writes/request | Excess writes dropped silently |

