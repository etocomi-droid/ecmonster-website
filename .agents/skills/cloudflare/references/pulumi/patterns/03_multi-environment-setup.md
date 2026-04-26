## Multi-Environment Setup

```typescript
const stack = pulumi.getStack();
const worker = new cloudflare.WorkerScript(`worker-${stack}`, {
    accountId, name: `my-worker-${stack}`, content: code,
    plainTextBindings: [{name: "ENVIRONMENT", text: stack}],
});
```

