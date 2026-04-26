## Performance Optimization

### Sandbox ID Strategy

```typescript
// ❌ BAD: New sandbox every time (slow)
const sandbox = getSandbox(env.Sandbox, `user-${Date.now()}`);

// ✅ GOOD: Reuse per user
const sandbox = getSandbox(env.Sandbox, `user-${userId}`);
```

### Sleep & Traffic Config

```typescript
// Cost-optimized
getSandbox(env.Sandbox, 'id', { sleepAfter: '30m', keepAlive: false });

// Always-on (requires destroy())
getSandbox(env.Sandbox, 'id', { keepAlive: true });
```

```jsonc
// High traffic: increase max_instances
{ "containers": [{ "class_name": "Sandbox", "max_instances": 50 }] }
```

