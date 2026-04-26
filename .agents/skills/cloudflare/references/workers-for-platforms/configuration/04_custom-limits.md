## Custom Limits

Set CPU time and subrequest limits per invocation:

```typescript
const userWorker = env.DISPATCHER.get(
  workerName,
  {},
  {
    limits: { 
      cpuMs: 10,        // Max CPU ms
      subRequests: 5    // Max fetch() calls
    }
  }
);
```

Handle limit violations:
```typescript
try {
  return await userWorker.fetch(request);
} catch (e) {
  if (e.message.includes("CPU time limit")) {
    return new Response("CPU limit exceeded", { status: 429 });
  }
  throw e;
}
```

