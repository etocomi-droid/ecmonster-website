## v6.x Versioned Deployments (Advanced)

For gradual rollouts, use 3-resource pattern:

```typescript
// 1. Worker (container for versions)
const worker = new cloudflare.Worker("api", {
    accountId: accountId,
    name: "api-worker",
});

// 2. Version (immutable code + config)
const version = new cloudflare.WorkerVersion("v1", {
    accountId: accountId,
    workerId: worker.id,
    content: fs.readFileSync("./dist/worker.js", "utf8"),
    compatibilityDate: "2025-01-01",
    compatibilityFlags: ["nodejs_compat"],
    // Note: Bindings configured at deployment level
});

// 3. Deployment (version + bindings + traffic split)
const deployment = new cloudflare.WorkersDeployment("prod", {
    accountId: accountId,
    workerId: worker.id,
    versionId: version.id,
    // Bindings applied to deployment
    kvNamespaceBindings: [{name: "MY_KV", namespaceId: kv.id}],
});
```

**When to use:** Blue-green deployments, canary releases, gradual rollouts  
**When NOT to use:** Simple single-version deployments (use WorkerScript)

---
See: [README.md](./README.md), [api.md](./api.md), [patterns.md](./patterns.md), [gotchas.md](./gotchas.md)
