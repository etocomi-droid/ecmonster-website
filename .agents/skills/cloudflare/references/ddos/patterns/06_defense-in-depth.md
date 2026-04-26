## Defense in Depth

Layered security stack: DDoS + WAF + Rate Limiting + Bot Management.

```typescript
// Layer 1: DDoS (volumetric attacks)
await client.zones.rulesets.phases.entrypoint.update("ddos_l7", {
  zone_id: zoneId,
  rules: [{ expression: "true", action: "execute", action_parameters: { id: ddosRulesetId, overrides: { sensitivity_level: "medium" } } }],
});

// Layer 2: WAF (exploit protection)
await client.zones.rulesets.phases.entrypoint.update("http_request_firewall_managed", {
  zone_id: zoneId,
  rules: [{ expression: "true", action: "execute", action_parameters: { id: wafRulesetId } }],
});

// Layer 3: Rate Limiting (abuse prevention)
await client.zones.rulesets.phases.entrypoint.update("http_ratelimit", {
  zone_id: zoneId,
  rules: [{ expression: "http.request.uri.path eq \"/api/login\"", action: "block", ratelimit: { characteristics: ["ip.src"], period: 60, requests_per_period: 5 } }],
});

// Layer 4: Bot Management (automation detection)
await client.zones.rulesets.phases.entrypoint.update("http_request_sbfm", {
  zone_id: zoneId,
  rules: [{ expression: "cf.bot_management.score lt 30", action: "managed_challenge" }],
});
```

