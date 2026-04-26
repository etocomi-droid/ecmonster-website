## Spectrum TCP Integration

Enable Argo for non-HTTP traffic (databases, game servers, IoT):

```typescript
// Update existing app
await client.spectrum.apps.update(appId, { zone_id: zoneId, argo_smart_routing: true });

// Create new app with Argo
await client.spectrum.apps.create({
  zone_id: zoneId,
  dns: { type: 'CNAME', name: 'tcp.example.com' },
  origin_direct: ['tcp://origin.example.com:3306'],
  protocol: 'tcp/3306',
  argo_smart_routing: true,
});
```

**Use cases:** MySQL/PostgreSQL (3306/5432), game servers, MQTT (1883), SSH (22)

