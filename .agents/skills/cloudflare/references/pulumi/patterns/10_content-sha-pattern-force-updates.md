## Content SHA Pattern (Force Updates)

Prevent false "no changes" detections:

```typescript
const version = Date.now().toString();
const worker = new cloudflare.WorkerScript("worker", {
    accountId, name: "my-worker", content: code,
    plainTextBindings: [{name: "VERSION", text: version}], // Forces deployment
});
```

---
See: [README.md](./README.md), [configuration.md](./configuration.md), [api.md](./api.md), [gotchas.md](./gotchas.md)
