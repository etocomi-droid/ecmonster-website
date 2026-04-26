## Context & Cleanup

```ts
const agent = getCurrentAgent<MyAgent>(); // Get current instance
async destroy() { /* cleanup before agent destroyed */ }
```

