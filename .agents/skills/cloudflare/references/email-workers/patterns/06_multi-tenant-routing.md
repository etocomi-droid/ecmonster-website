## Multi-Tenant Routing

```typescript
// support+tenant123@example.com → tenant123
const tenantId = message.to.split('@')[0].match(/\+(.+)$/)?.[1] || 'default';
const config = await env.TENANT_CONFIG.get(tenantId, 'json');
config?.forwardTo ? await message.forward(config.forwardTo) : message.setReject('Unknown');
```

