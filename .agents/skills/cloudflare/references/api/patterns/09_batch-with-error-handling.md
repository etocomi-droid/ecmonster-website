## Batch with Error Handling

```typescript
// Process multiple zones, continue on errors
const results = await Promise.allSettled(
  zoneIds.map(id => client.zones.get({ zone_id: id }))
);

results.forEach((result, i) => {
  if (result.status === 'fulfilled') {
    console.log(`Zone ${i}: ${result.value.name}`);
  } else {
    console.error(`Zone ${i} failed:`, result.reason.message);
  }
});
```

