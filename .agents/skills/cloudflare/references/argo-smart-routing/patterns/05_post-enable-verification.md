## Post-Enable Verification

```typescript
async function verifyArgoEnabled(client: Cloudflare, zoneId: string): Promise<boolean> {
  await new Promise(r => setTimeout(r, 2000)); // Wait for propagation
  const status = await client.argo.smartRouting.get({ zone_id: zoneId });
  return status.value === 'on';
}
```

