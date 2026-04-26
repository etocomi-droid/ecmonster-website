## Workers Domains/Routes

```typescript
// Route (pattern-based)
const route = new cloudflare.WorkerRoute("my-route", {
    zoneId: zoneId,
    pattern: "example.com/api/*",
    scriptName: worker.name,
});

// Domain (dedicated subdomain)
const domain = new cloudflare.WorkersDomain("my-domain", {
    accountId: accountId,
    hostname: "api.example.com",
    service: worker.name,
    zoneId: zoneId,
});
```

