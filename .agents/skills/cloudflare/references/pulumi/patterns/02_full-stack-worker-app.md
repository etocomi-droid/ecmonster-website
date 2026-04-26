## Full-Stack Worker App

```typescript
const kv = new cloudflare.WorkersKvNamespace("cache", {accountId, title: "api-cache"});
const db = new cloudflare.D1Database("db", {accountId, name: "app-database"});
const bucket = new cloudflare.R2Bucket("assets", {accountId, name: "app-assets"});

const apiWorker = new cloudflare.WorkerScript("api", {
    accountId, name: "api-worker", content: fs.readFileSync("./dist/api.js", "utf8"),
    module: true, kvNamespaceBindings: [{name: "CACHE", namespaceId: kv.id}],
    d1DatabaseBindings: [{name: "DB", databaseId: db.id}],
    r2BucketBindings: [{name: "ASSETS", bucketName: bucket.name}],
});
```

