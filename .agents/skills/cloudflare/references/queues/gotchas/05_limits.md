## Limits

| Limit | Value | Notes |
|-------|-------|-------|
| Max queues | 10,000 | Per account |
| Message size | 128 KB | Maximum per message |
| Batch size (consumer) | 100 messages | Maximum messages per batch |
| Batch size (sendBatch) | 100 msgs or 256 KB | Whichever limit reached first |
| Throughput | 5,000 msgs/sec | Per queue |
| Retention | 4-14 days | Configurable retention period |
| Max backlog | 25 GB | Maximum queue backlog size |
| Max delay | 12 hours (43,200s) | Maximum message delay |
| Max retries | 100 | Maximum retry attempts |
| CPU time default | 30s | Per consumer invocation |
| CPU time max | 300s (5 min) | Configurable via `limits.cpu_ms` |
| Operations per message | 3 (write + read + delete) | Base cost per message |
| Pricing | $0.40 per 1M operations | After 1M free operations |
| Message charging | Per 64 KB chunk | Messages charged in 64 KB increments |
