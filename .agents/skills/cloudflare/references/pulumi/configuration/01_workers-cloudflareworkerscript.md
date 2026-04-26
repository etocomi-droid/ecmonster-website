## Workers (cloudflare.WorkerScript)

```typescript
import * as cloudflare from "@pulumi/cloudflare";
import * as fs from "fs";

const worker = new cloudflare.WorkerScript("my-worker", {
    accountId: accountId,
    name: "my-worker",
    content: fs.readFileSync("./dist/worker.js", "utf8"),
    module: true, // ES modules
    compatibilityDate: "2025-01-01",
    compatibilityFlags: ["nodejs_compat"],
    
    // v6.x: Observability
    logpush: true, // Enable Workers Logpush
    tailConsumers: [{service: "log-consumer"}], // Stream logs to Worker
    
    // v6.x: Placement
    placement: {mode: "smart"}, // Smart placement for latency optimization
    
    // Bindings
    kvNamespaceBindings: [{name: "MY_KV", namespaceId: kv.id}],
    r2BucketBindings: [{name: "MY_BUCKET", bucketName: bucket.name}],
    d1DatabaseBindings: [{name: "DB", databaseId: db.id}],
    queueBindings: [{name: "MY_QUEUE", queue: queue.id}],
    serviceBindings: [{name: "OTHER_SERVICE", service: other.name}],
    plainTextBindings: [{name: "ENV_VAR", text: "value"}],
    secretTextBindings: [{name: "API_KEY", text: secret}],
    
    // v6.x: Advanced bindings
    analyticsEngineBindings: [{name: "ANALYTICS", dataset: "my-dataset"}],
    browserBinding: {name: "BROWSER"}, // Browser Rendering
    aiBinding: {name: "AI"}, // Workers AI
    hyperdriveBindings: [{name: "HYPERDRIVE", id: hyperdriveConfig.id}],
});
```

