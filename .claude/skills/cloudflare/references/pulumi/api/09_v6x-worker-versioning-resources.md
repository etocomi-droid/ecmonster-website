## v6.x Worker Versioning Resources

**Worker** - Container for versions:
```typescript
const worker = new cloudflare.Worker("api", {accountId, name: "api-worker"});
export const workerId = worker.id;
```

**WorkerVersion** - Immutable code + config:
```typescript
const version = new cloudflare.WorkerVersion("v1", {
    accountId, workerId: worker.id,
    content: fs.readFileSync("./dist/worker.js", "utf8"),
    compatibilityDate: "2025-01-01",
});
export const versionId = version.id;
```

**WorkersDeployment** - Active deployment with bindings:
```typescript
const deployment = new cloudflare.WorkersDeployment("prod", {
    accountId, workerId: worker.id, versionId: version.id,
    kvNamespaceBindings: [{name: "MY_KV", namespaceId: kv.id}],
});
```

**Use:** Advanced deployments (canary, blue-green). Most apps should use `WorkerScript` (auto-versioning).

---
See: [README.md](./README.md), [configuration.md](./configuration.md), [patterns.md](./patterns.md), [gotchas.md](./gotchas.md)
