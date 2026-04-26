## D1 Databases (cloudflare.D1Database)

```typescript
const db = new cloudflare.D1Database("my-db", {accountId, name: "my-database"});

// Migrations via wrangler
import * as command from "@pulumi/command";
const migration = new command.local.Command("d1-migration", {
    create: pulumi.interpolate`wrangler d1 execute ${db.name} --file ./schema.sql`,
}, {dependsOn: [db]});
```

