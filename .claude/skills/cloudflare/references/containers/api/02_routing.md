## Routing

**getByName(id)** - Named instance for session affinity, per-user state
**getRandom()** - Random instance for load balancing stateless services

```typescript
const container = env.MY_CONTAINER.getByName("user-123");
const container = env.MY_CONTAINER.getRandom();
```

