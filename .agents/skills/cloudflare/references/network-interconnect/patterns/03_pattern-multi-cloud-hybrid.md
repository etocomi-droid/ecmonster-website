## Pattern: Multi-Cloud Hybrid

**Use Case:** AWS/GCP workloads with Cloudflare.

**AWS Direct Connect:**
```typescript
// 1. Order Direct Connect in AWS Console
// 2. Get LOA + VLAN from AWS
// 3. Send to CF account team (no API)
// 4. Configure static routes in Magic WAN

await configureStaticRoutes(id, {
  prefix: '10.0.0.0/8',
  nexthop: 'aws-direct-connect',
});
```

**GCP Cloud Interconnect:**
```
1. Get VLAN attachment pairing key from GCP Console
2. Create via Dashboard: Interconnects → Create → Cloud Interconnect → Google
   - Enter pairing key, name, MTU, speed
3. Configure static routes in Magic WAN (BGP routes from GCP ignored)
4. Configure custom learned routes in GCP Cloud Router
```

**Note:** Dashboard-only. No API/SDK support yet.

