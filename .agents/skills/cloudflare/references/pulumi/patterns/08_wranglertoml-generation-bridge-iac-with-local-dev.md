## Wrangler.toml Generation (Bridge IaC with Local Dev)

Generate wrangler.toml from Pulumi config to keep local dev in sync:

```typescript
import * as command from "@pulumi/command";

const workerConfig = {
    name: "my-worker",
    compatibilityDate: "2025-01-01",
    compatibilityFlags: ["nodejs_compat"],
};

// Create resources
const kv = new cloudflare.WorkersKvNamespace("kv", {accountId, title: "my-kv"});
const db = new cloudflare.D1Database("db", {accountId, name: "my-db"});
const bucket = new cloudflare.R2Bucket("bucket", {accountId, name: "my-bucket"});

// Generate wrangler.toml after resources created
const wranglerGen = new command.local.Command("gen-wrangler", {
    create: pulumi.interpolate`cat > wrangler.toml <<EOF
name = "${workerConfig.name}"
main = "src/index.ts"
compatibility_date = "${workerConfig.compatibilityDate}"
compatibility_flags = ${JSON.stringify(workerConfig.compatibilityFlags)}

[[kv_namespaces]]
binding = "MY_KV"
id = "${kv.id}"

[[d1_databases]]
binding = "DB"
database_id = "${db.id}"
database_name = "${db.name}"

[[r2_buckets]]
binding = "MY_BUCKET"
bucket_name = "${bucket.name}"
EOF`,
}, {dependsOn: [kv, db, bucket]});

// Deploy worker after wrangler.toml generated
const worker = new cloudflare.WorkerScript("worker", {
    accountId, name: workerConfig.name, content: code,
    compatibilityDate: workerConfig.compatibilityDate,
    compatibilityFlags: workerConfig.compatibilityFlags,
    kvNamespaceBindings: [{name: "MY_KV", namespaceId: kv.id}],
    d1DatabaseBindings: [{name: "DB", databaseId: db.id}],
    r2BucketBindings: [{name: "MY_BUCKET", bucketName: bucket.name}],
}, {dependsOn: [wranglerGen]});
```

**Benefits:**
- `wrangler dev` uses same bindings as production
- No config drift between Pulumi and local dev
- Single source of truth (Pulumi config)

**Alternative:** Read wrangler.toml in Pulumi (reverse direction) if wrangler is source of truth

