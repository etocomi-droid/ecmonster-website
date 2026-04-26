## TLS Configuration

| Mode | Description | Use Case | Origin Cert |
|------|-------------|----------|-------------|
| `off` | No TLS | Non-encrypted (SSH, gaming) | No |
| `flexible` | TLS client→CF, plain CF→origin | Testing | No |
| `full` | TLS end-to-end, self-signed OK | Production | Yes (any) |
| `strict` | Full + valid cert verification | Max security | Yes (CA) |

**Example:**
```typescript
const app = await client.spectrum.apps.create({
  zone_id: 'your-zone-id',
  protocol: 'tcp/3306',
  dns: { type: 'CNAME', name: 'db.example.com' },
  origin_direct: ['tcp://192.0.2.1:3306'],
  tls: 'strict',  // Validates origin certificate
});
```

