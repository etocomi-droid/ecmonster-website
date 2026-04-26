## Override Conflicts

**Problem:** Managed ruleset overrides don't apply
**Cause:** Rule ID doesn't exist or category name incorrect
**Solution:**

```typescript
// List managed ruleset rules to find IDs
const ruleset = await client.rulesets.get({
  zone_id: 'zone_id',
  ruleset_id: 'efb7b8c949ac4650a09736fc376e9aee',
});
console.log(ruleset.rules.map(r => ({ id: r.id, description: r.description })));

// Use correct IDs in overrides
{ action: 'execute', action_parameters: { id: 'efb7b8c949ac4650a09736fc376e9aee', 
  overrides: { rules: [{ id: '5de7edfa648c4d6891dc3e7f84534ffa', action: 'log' }] } } }
```

