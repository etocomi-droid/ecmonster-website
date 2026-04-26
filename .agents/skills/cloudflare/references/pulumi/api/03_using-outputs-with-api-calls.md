## Using Outputs with API Calls

```typescript
const db = new cloudflare.D1Database("db", {accountId, name: "my-db"});

db.id.apply(async (dbId) => {
    const response = await fetch(
        `https://api.cloudflare.com/client/v4/accounts/${accountId}/d1/database/${dbId}/query`,
        {method: "POST", headers: {"Authorization": `Bearer ${apiToken}`, "Content-Type": "application/json"},
         body: JSON.stringify({sql: "CREATE TABLE users (id INT)"})}
    );
    return response.json();
});
```

