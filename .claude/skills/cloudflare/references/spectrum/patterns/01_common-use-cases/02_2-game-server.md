### 2. Game Server

**TypeScript (Minecraft):**
```typescript
const app = await client.spectrum.apps.create({
  zone_id: 'your-zone-id',
  protocol: 'tcp/25565',
  dns: { type: 'CNAME', name: 'mc.example.com' },
  origin_direct: ['tcp://192.168.1.10:25565'],
  proxy_protocol: 'v1',  // Preserves player IPs
  argo_smart_routing: true,
});
```

**Benefits:** DDoS protection, hide origin IP, Proxy Protocol for player IPs/bans, Argo reduces latency

