## Resource Dependencies

Implicit dependencies via outputs:

```typescript
const kv = new cloudflare.WorkersKvNamespace("kv", {
    accountId: accountId,
    title: "my-kv",
});

// Worker depends on KV (implicit via kv.id)
const worker = new cloudflare.WorkerScript("worker", {
    accountId: accountId,
    name: "my-worker",
    content: code,
    kvNamespaceBindings: [{name: "MY_KV", namespaceId: kv.id}], // Creates dependency
});
```

Explicit dependencies:

```typescript
const migration = new command.local.Command("migration", {
    create: pulumi.interpolate`wrangler d1 execute ${db.name} --file ./schema.sql`,
}, {dependsOn: [db]});

const worker = new cloudflare.WorkerScript("worker", {
    accountId: accountId,
    name: "worker",
    content: code,
    d1DatabaseBindings: [{name: "DB", databaseId: db.id}],
}, {dependsOn: [migration]}); // Ensure migrations run first
```

