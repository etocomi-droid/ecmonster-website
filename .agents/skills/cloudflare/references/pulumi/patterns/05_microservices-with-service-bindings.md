## Microservices with Service Bindings

```typescript
const authWorker = new cloudflare.WorkerScript("auth", {accountId, name: "auth-service", content: authCode});
const apiWorker = new cloudflare.WorkerScript("api", {
    accountId, name: "api-service", content: apiCode,
    serviceBindings: [{name: "AUTH", service: authWorker.name}],
});
```

