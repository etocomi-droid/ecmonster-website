## Update Replaces All Rules

**Problem:** Updating ruleset deletes other rules
**Cause:** `update()` replaces entire rule list
**Solution:**

```typescript
// WRONG: This deletes all existing rules!
await client.rulesets.update({
  zone_id: 'zone_id',
  ruleset_id: 'ruleset_id',
  rules: [{ action: 'block', expression: 'cf.waf.score gt 50' }],
});

// CORRECT: Get existing rules first
const ruleset = await client.rulesets.get({ zone_id: 'zone_id', ruleset_id: 'ruleset_id' });
await client.rulesets.update({
  zone_id: 'zone_id',
  ruleset_id: 'ruleset_id',
  rules: [...ruleset.rules, { action: 'block', expression: 'cf.waf.score gt 50' }],
});
```

