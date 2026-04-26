## Pre-Flight Validation

```typescript
async function validateArgoEligibility(client: Cloudflare, zoneId: string) {
  const status = await client.argo.smartRouting.get({ zone_id: zoneId });
  const zone = await client.zones.get({ zone_id: zoneId });
  
  const issues: string[] = [];
  if (!status.editable) issues.push('Zone not editable');
  if (['free', 'pro'].includes(zone.plan.legacy_id)) issues.push('Requires Business+ plan');
  if (zone.status !== 'active') issues.push('Zone not active');
  
  return { canEnable: issues.length === 0, issues };
}
```

