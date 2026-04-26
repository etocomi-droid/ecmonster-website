## Agent Routing

**Recommended: Use route helpers**

```typescript
import { routeAgent } from "agents";

export default {
  fetch(request: Request, env: Env) {
    return routeAgent(request, env);
  }
}
```

Helper routes requests to agents automatically based on URL patterns.

**Manual routing (advanced):**

```typescript
export default {
  async fetch(request: Request, env: Env) {
    const url = new URL(request.url);
    
    // Named ID (deterministic)
    const id = env.MyAgent.idFromName("user-123");
    
    // Random ID (from URL param)
    // const id = env.MyAgent.idFromString(url.searchParams.get("id"));
    
    const stub = env.MyAgent.get(id);
    return stub.fetch(request);
  }
}
```

**Multi-agent setup:**

```typescript
import { routeAgent } from "agents";

export default {
  fetch(request: Request, env: Env) {
    const url = new URL(request.url);
    
    // Route by path
    if (url.pathname.startsWith("/chat")) {
      return routeAgent(request, env, "ChatAgent");
    }
    if (url.pathname.startsWith("/task")) {
      return routeAgent(request, env, "TaskAgent");
    }
    
    return new Response("Not found", { status: 404 });
  }
}
```

