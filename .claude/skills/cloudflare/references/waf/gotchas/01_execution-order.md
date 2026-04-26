## Execution Order

**Problem:** Rules execute in unexpected order
**Cause:** Misunderstanding phase execution
**Solution:**

Phases execute sequentially (can't be changed):
1. `http_request_firewall_custom` - Custom rules
2. `http_request_firewall_managed` - Managed rulesets
3. `http_ratelimit` - Rate limiting

Within phase: top-to-bottom, first match wins (unless `skip`)

```typescript
// WRONG: Can't mix phase-specific actions
await client.rulesets.create({
  phase: 'http_request_firewall_custom',
  rules: [
    { action: 'block', expression: 'cf.waf.score gt 50' },
    { action: 'execute', action_parameters: { id: 'managed_id' } }, // WRONG
  ],
});

// CORRECT: Separate rulesets per phase
await client.rulesets.create({ phase: 'http_request_firewall_custom', rules: [...] });
await client.rulesets.create({ phase: 'http_request_firewall_managed', rules: [...] });
```

