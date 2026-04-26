## Alarms

Schedule future work that survives eviction:

```typescript
// Set alarm (overwrites any existing alarm)
await this.ctx.storage.setAlarm(Date.now() + 3600000)  // 1 hour from now
await this.ctx.storage.setAlarm(new Date("2026-02-01"))  // Absolute time

// Check next alarm
const nextRun = await this.ctx.storage.getAlarm()  // null if none

// Cancel alarm
await this.ctx.storage.deleteAlarm()

// Handler called when alarm fires
async alarm() {
  // Runs once alarm triggers
  // DO wakes from hibernation if needed
  // Use for cleanup, notifications, scheduled tasks
}
```

**Limitations:**
- 1 alarm per DO maximum
- Overwrites previous alarm when set
- Use queue pattern for multiple scheduled events (see [Patterns](./patterns.md))

**Reliability:**
- Alarms survive DO eviction/restart
- Cloudflare retries failed alarms automatically
- Not guaranteed exactly-once (handle idempotently)

