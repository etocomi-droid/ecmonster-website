## Custom Rules

```typescript
await client.rulesets.create({
  zone_id: 'zone_id',
  kind: 'zone',
  phase: 'http_request_firewall_custom',
  name: 'Custom WAF Rules',
  rules: [
    // Attack score-based
    { action: 'block', expression: 'cf.waf.score gt 50', enabled: true },
    { action: 'challenge', expression: 'cf.waf.score gt 20', enabled: true },
    
    // Specific attack types
    { action: 'block', expression: 'cf.waf.score.sqli gt 30 or cf.waf.score.xss gt 30', enabled: true },
    
    // Geographic blocking
    { action: 'block', expression: 'ip.geoip.country in {"CN" "RU"}', enabled: true },
  ],
});
```

