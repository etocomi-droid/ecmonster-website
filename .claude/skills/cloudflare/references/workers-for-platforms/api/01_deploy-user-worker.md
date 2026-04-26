## Deploy User Worker

```bash
curl -X PUT \
  "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/workers/dispatch/namespaces/$NAMESPACE/scripts/$SCRIPT_NAME" \
  -H "Authorization: Bearer $API_TOKEN" \
  -F 'metadata={"main_module": "worker.mjs"};type=application/json' \
  -F 'worker.mjs=@worker.mjs;type=application/javascript+module'
```

### TypeScript SDK
```typescript
import Cloudflare from "cloudflare";

const client = new Cloudflare({ apiToken: process.env.API_TOKEN });

const scriptFile = new File([scriptContent], `${scriptName}.mjs`, {
  type: "application/javascript+module",
});

await client.workersForPlatforms.dispatch.namespaces.scripts.update(
  namespace, scriptName,
  {
    account_id: accountId,
    metadata: { main_module: `${scriptName}.mjs` },
    files: [scriptFile],
  }
);
```

