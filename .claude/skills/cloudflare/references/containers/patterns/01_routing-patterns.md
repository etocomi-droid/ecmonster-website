## Routing Patterns

### Session Affinity (Stateful)

```typescript
export class SessionBackend extends Container {
  defaultPort = 3000;
  sleepAfter = "30m";
}

export default {
  async fetch(request: Request, env: Env) {
    const sessionId = request.headers.get("X-Session-ID") || crypto.randomUUID();
    const container = env.SESSION_BACKEND.getByName(sessionId);
    await container.startAndWaitForPorts();
    return container.fetch(request);
  }
};
```

**Use:** User sessions, WebSocket, stateful games, per-user caching.

### Load Balancing (Stateless)

```typescript
export default {
  async fetch(request: Request, env: Env) {
    const container = env.STATELESS_API.getRandom();
    await container.startAndWaitForPorts();
    return container.fetch(request);
  }
};
```

**Use:** Stateless HTTP APIs, CPU-intensive work, read-only queries.

### Singleton Pattern

```typescript
export default {
  async fetch(request: Request, env: Env) {
    const container = env.GLOBAL_SERVICE.getByName("singleton");
    await container.startAndWaitForPorts();
    return container.fetch(request);
  }
};
```

**Use:** Global cache, centralized coordinator, single source of truth.

