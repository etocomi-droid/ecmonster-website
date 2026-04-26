## Dynamic Response to Attacks

```typescript
interface Env { CLOUDFLARE_API_TOKEN: string; ZONE_ID: string; KV: KVNamespace; }

export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    if (request.url.includes("/attack-detected")) {
      const attackData = await request.json();
      await env.KV.put(`attack:${Date.now()}`, JSON.stringify(attackData), { expirationTtl: 86400 });
      const recentAttacks = await getRecentAttacks(env.KV);
      if (recentAttacks.length > 5) {
        await setProtectionLevel(env.ZONE_ID, ProtectionLevel.HIGH, managedRulesetId, client);
        return new Response("Protection increased");
      }
    }
    return new Response("OK");
  },
  async scheduled(event: ScheduledEvent, env: Env): Promise<void> {
    const recentAttacks = await getRecentAttacks(env.KV);
    if (recentAttacks.length === 0) await setProtectionLevel(env.ZONE_ID, ProtectionLevel.MEDIUM, managedRulesetId, client);
  },
};
```

