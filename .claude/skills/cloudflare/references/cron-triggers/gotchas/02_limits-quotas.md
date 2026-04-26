## Limits & Quotas

| Limit | Free | Paid | Notes |
|-------|------|------|-------|
| Triggers per Worker | 3 | Unlimited | Maximum cron schedules per Worker |
| CPU time | 10ms | 50ms | May need `ctx.waitUntil()` or Workflows |
| Execution guarantee | At-least-once | At-least-once | Duplicates possible - use idempotency |
| Propagation delay | Up to 15 minutes | Up to 15 minutes | Time for changes to take effect globally |
| Min interval | 1 minute | 1 minute | Cannot schedule more frequently |
| Cron accuracy | ±1 minute | ±1 minute | Execution may drift slightly |

