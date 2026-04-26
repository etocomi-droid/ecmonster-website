## Full Setup Pattern

```typescript
async function setupArgo(client: Cloudflare, zoneId: string) {
  // 1. Validate
  const { canEnable, issues } = await validateArgoEligibility(client, zoneId);
  if (!canEnable) throw new Error(issues.join(', '));
  
  // 2. Enable both features
  await Promise.all([
    client.argo.smartRouting.edit({ zone_id: zoneId, value: 'on' }),
    client.argo.tieredCaching.edit({ zone_id: zoneId, value: 'on' }),
  ]);
  
  // 3. Verify
  const [argo, cache] = await Promise.all([
    client.argo.smartRouting.get({ zone_id: zoneId }),
    client.argo.tieredCaching.get({ zone_id: zoneId }),
  ]);
  
  return { argo: argo.value === 'on', tieredCache: cache.value === 'on' };
}
```

**When to combine:** High-traffic sites (>1TB/mo), global users, cacheable content.
