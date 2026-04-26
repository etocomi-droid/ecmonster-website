### "v6.x Worker versioning confusion"

**Problem:** Worker deployed but not receiving traffic  
**Cause:** v6.x requires Worker + WorkerVersion + WorkersDeployment (3 resources)  
**Solution:** Use WorkerScript (auto-versioning) OR full versioning pattern

```typescript
// SIMPLE: WorkerScript auto-versions (default behavior)
const worker = new cloudflare.WorkerScript("worker", {
    accountId, name: "my-worker", content: code,
});

// ADVANCED: Manual versioning for gradual rollouts (v6.x)
const worker = new cloudflare.Worker("worker", {accountId, name: "my-worker"});
const version = new cloudflare.WorkerVersion("v1", {
    accountId, workerId: worker.id, content: code, compatibilityDate: "2025-01-01",
});
const deployment = new cloudflare.WorkersDeployment("prod", {
    accountId, workerId: worker.id, versionId: version.id,
});
```

