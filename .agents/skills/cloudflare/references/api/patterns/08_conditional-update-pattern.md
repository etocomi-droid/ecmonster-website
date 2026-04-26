## Conditional Update Pattern

```typescript
// Only update if zone is active
const zone = await client.zones.get({ zone_id: 'zone-id' });
if (zone.status === 'active') {
  await client.zones.edit(zone.id, { paused: false });
}
```

