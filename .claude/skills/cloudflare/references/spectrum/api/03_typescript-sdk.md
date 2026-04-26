## TypeScript SDK

```typescript
import Cloudflare from 'cloudflare';

const client = new Cloudflare({ apiToken: process.env.CLOUDFLARE_API_TOKEN });

// Create
const app = await client.spectrum.apps.create({
  zone_id: 'your-zone-id',
  protocol: 'tcp/22',
  dns: { type: 'CNAME', name: 'ssh.example.com' },
  origin_direct: ['tcp://192.0.2.1:22'],
  ip_firewall: true,
  tls: 'off',
});

// List
const apps = await client.spectrum.apps.list({ zone_id: 'your-zone-id' });

// Get
const appDetails = await client.spectrum.apps.get({ zone_id: 'your-zone-id', app_id: app.id });

// Update
await client.spectrum.apps.update({ zone_id: 'your-zone-id', app_id: app.id, tls: 'full' });

// Delete
await client.spectrum.apps.delete({ zone_id: 'your-zone-id', app_id: app.id });

// Analytics
const analytics = await client.spectrum.analytics.aggregate({
  zone_id: 'your-zone-id',
  metrics: ['bytesIngress', 'bytesEgress'],
  since: new Date(Date.now() - 3600000).toISOString(),
});
```

