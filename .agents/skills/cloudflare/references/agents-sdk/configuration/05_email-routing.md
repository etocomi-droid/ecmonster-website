## Email Routing

**Code setup:**

```typescript
import { routeAgentEmail } from "agents";

export default {
  fetch: (req: Request, env: Env) => routeAgent(req, env),
  email: (message: ForwardableEmailMessage, env: Env) => {
    return routeAgentEmail(message, env);
  }
}
```

**Dashboard setup:**

Configure email routing in Cloudflare dashboard:

```
Destination: Workers with Durable Objects
Worker: my-agents-app
```

Then handle in agent:

```typescript
export class EmailAgent extends Agent<Env> {
  async onEmail(email: AgentEmail) {
    const text = await email.text();
    // Process email
  }
}
```

