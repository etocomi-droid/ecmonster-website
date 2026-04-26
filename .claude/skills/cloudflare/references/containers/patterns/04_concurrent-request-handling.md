## Concurrent Request Handling

```typescript
export class SafeContainer extends Container {
  private initialized = false;

  async fetch(request: Request) {
    await this.ctx.blockConcurrencyWhile(async () => {
      if (!this.initialized) {
        await this.startAndWaitForPorts();
        this.initialized = true;
      }
    });
    return super.fetch(request);
  }
}
```

**Use:** One-time initialization, preventing concurrent startup.

