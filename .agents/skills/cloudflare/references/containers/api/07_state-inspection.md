## State Inspection

### External state check

```typescript
const state = await container.getState();
// state.status: "starting" | "running" | "stopping" | "stopped"
```

### Internal state check

```typescript
export class MyContainer extends Container {
  async fetch(request: Request) {
    if (this.ctx.container.running) { ... }
  }
}
```

**⚠️ Use `getState()` for external checks, `ctx.container.running` for internal.**
