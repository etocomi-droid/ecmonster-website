## Alarms

```typescript
await this.ctx.storage.setAlarm(Date.now() + 60000); // Timestamp or Date
await this.ctx.storage.getAlarm();
await this.ctx.storage.deleteAlarm();

async alarm() { await this.doScheduledWork(); }
```

