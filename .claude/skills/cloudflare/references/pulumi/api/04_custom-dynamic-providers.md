## Custom Dynamic Providers

For resources not in provider:

```typescript
import * as pulumi from "@pulumi/pulumi";

class D1MigrationProvider implements pulumi.dynamic.ResourceProvider {
    async create(inputs: any): Promise<pulumi.dynamic.CreateResult> {
        const response = await fetch(
            `https://api.cloudflare.com/client/v4/accounts/${inputs.accountId}/d1/database/${inputs.databaseId}/query`,
            {method: "POST", headers: {"Authorization": `Bearer ${inputs.apiToken}`, "Content-Type": "application/json"},
             body: JSON.stringify({sql: inputs.sql})}
        );
        return {id: `${inputs.databaseId}-${Date.now()}`, outs: await response.json()};
    }
    async update(id: string, olds: any, news: any): Promise<pulumi.dynamic.UpdateResult> {
        if (olds.sql !== news.sql) await this.create(news);
        return {};
    }
    async delete(id: string, props: any): Promise<void> {}
}

class D1Migration extends pulumi.dynamic.Resource {
    constructor(name: string, args: any, opts?: pulumi.CustomResourceOptions) {
        super(new D1MigrationProvider(), name, args, opts);
    }
}

const migration = new D1Migration("migration", {
    accountId, databaseId: db.id, apiToken, sql: "CREATE TABLE users (id INT)",
}, {dependsOn: [db]});
```

