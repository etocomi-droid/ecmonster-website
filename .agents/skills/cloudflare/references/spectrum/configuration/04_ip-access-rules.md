## IP Access Rules

Enable `ip_firewall: true` then configure zone-level firewall rules.

```typescript
const app = await client.spectrum.apps.create({
  // ...
  ip_firewall: true,  // Applies zone firewall rules
});
```

