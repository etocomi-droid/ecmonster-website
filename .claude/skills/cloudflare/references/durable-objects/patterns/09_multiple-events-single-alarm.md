## Multiple Events (Single Alarm)

Queue pattern to schedule multiple events:

```typescript
async scheduleEvent(id: string, runAt: number) {
  await this.ctx.storage.put(`event:${id}`, { id, runAt });
  const curr = await this.ctx.storage.getAlarm();
  if (!curr || runAt < curr) await this.ctx.storage.setAlarm(runAt);
}

async alarm() {
  const events = await this.ctx.storage.list({ prefix: "event:" }), now = Date.now();
  let next = null;
  for (const [key, ev] of events) {
    if (ev.runAt <= now) {
      await this.processEvent(ev);
      await this.ctx.storage.delete(key);
    } else if (!next || ev.runAt < next) next = ev.runAt;
  }
  if (next) await this.ctx.storage.setAlarm(next);
}
```

