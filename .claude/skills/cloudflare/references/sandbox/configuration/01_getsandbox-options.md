## getSandbox Options

```typescript
const sandbox = getSandbox(env.Sandbox, 'sandbox-id', {
  normalizeId: true,         // lowercase ID (required for preview URLs)
  sleepAfter: '10m',         // sleep after inactivity: '5m', '1h', '2d' (default: '10m')
  keepAlive: false,          // false = auto-timeout, true = never sleep
  
  containerTimeouts: {
    instanceGetTimeoutMS: 30000,  // 30s for provisioning (default: 30000)
    portReadyTimeoutMS: 90000     // 90s for container startup (default: 90000)
  }
});
```

**Sleep Config**:
- `sleepAfter`: Duration string (e.g., '5m', '10m', '1h') - default: '10m'
- `keepAlive: false`: Auto-sleep (default, cost-optimized)
- `keepAlive: true`: Never sleep (higher cost, requires explicit `destroy()`)
- Sleeping sandboxes wake automatically (cold start)

