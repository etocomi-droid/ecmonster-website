## Secrets Management

```typescript
import * as pulumi from "@pulumi/pulumi";

const config = new pulumi.Config();
const apiKey = config.requireSecret("apiKey"); // Encrypted in state

const worker = new cloudflare.WorkerScript("worker", {
    accountId: accountId,
    name: "my-worker",
    content: code,
    secretTextBindings: [{name: "API_KEY", text: apiKey}],
});
```

Store secrets:
```bash
pulumi config set --secret apiKey "secret-value"
```

