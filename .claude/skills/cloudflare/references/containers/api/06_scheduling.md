## Scheduling

```typescript
export class ScheduledContainer extends Container {
  async fetch(request: Request) {
    await this.schedule(Date.now() + 60000);  // 1 minute
    await this.schedule("2026-01-28T00:00:00Z");  // ISO string
    return new Response("Scheduled");
  }

  async alarm() {
    // Called when schedule fires (SQLite-backed, survives restarts)
  }
}
```

**⚠️ Don't override `alarm()` directly when using `schedule()` helper.**

