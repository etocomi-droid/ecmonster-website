## Activity Timeout Renewal

```typescript
export class LongRunningContainer extends Container {
  sleepAfter = "5m";

  async processLongJob(data: unknown) {
    const interval = setInterval(() => {
      this.ctx.storage.put("keepalive", Date.now());
    }, 60000);

    try {
      await this.doLongWork(data);
    } finally {
      clearInterval(interval);
    }
  }
}
```

**Use:** Long operations exceeding `sleepAfter`.

