## v6.x Versioned Deployments (Blue-Green/Canary)

```typescript
const worker = new cloudflare.Worker("api", {accountId, name: "api-worker"});
const v1 = new cloudflare.WorkerVersion("v1", {accountId, workerId: worker.id, content: fs.readFileSync("./dist/v1.js", "utf8"), compatibilityDate: "2025-01-01"});
const v2 = new cloudflare.WorkerVersion("v2", {accountId, workerId: worker.id, content: fs.readFileSync("./dist/v2.js", "utf8"), compatibilityDate: "2025-01-01"});

// Gradual rollout: 10% v2, 90% v1
const deployment = new cloudflare.WorkersDeployment("canary", {
    accountId, workerId: worker.id,
    versions: [{versionId: v2.id, percentage: 10}, {versionId: v1.id, percentage: 90}],
    kvNamespaceBindings: [{name: "MY_KV", namespaceId: kv.id}],
});
```

**Use:** Canary releases, A/B testing, blue-green. Most apps use `WorkerScript` (auto-versioning).

