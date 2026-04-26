### "D1 migrations don't run on pulumi up"

**Problem:** Database schema not applied after D1 database created  
**Cause:** Pulumi creates database but doesn't run migrations  
**Solution:** Use Command resource with dependsOn

```typescript
const db = new cloudflare.D1Database("db", {accountId, name: "mydb"});

// Run migrations after DB created
const migration = new command.local.Command("migrate", {
    create: pulumi.interpolate`wrangler d1 execute ${db.name} --file ./schema.sql`,
}, {dependsOn: [db]});

// Worker depends on migrations
const worker = new cloudflare.WorkerScript("worker", {
    d1DatabaseBindings: [{name: "DB", databaseId: db.id}],
}, {dependsOn: [migration]});
```

