## Enable Argo + Tiered Cache

```typescript
async function enableOptimalPerformance(client: Cloudflare, zoneId: string) {
  await Promise.all([
    client.argo.smartRouting.edit({ zone_id: zoneId, value: 'on' }),
    client.argo.tieredCaching.edit({ zone_id: zoneId, value: 'on' }),
  ]);
}
```

**Flow:** Visitor → Edge (Lower-Tier) → [Cache Miss] → Upper-Tier → [Cache Miss + Argo] → Origin

**Impact:** Argo ~30% latency reduction + Tiered Cache 50-80% origin offload

