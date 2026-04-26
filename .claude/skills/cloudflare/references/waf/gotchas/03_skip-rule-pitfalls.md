## Skip Rule Pitfalls

**Problem:** Skip rules don't work as expected
**Cause:** Misunderstanding skip scope
**Solution:**

Skip types:
- `ruleset: 'current'` - Skip remaining rules in current ruleset only
- `phases: ['phase_name']` - Skip entire phases

```typescript
// WRONG: Trying to skip managed rules from custom phase
// In http_request_firewall_custom:
{
  action: 'skip',
  action_parameters: { ruleset: 'current' },
  expression: 'ip.src in {192.0.2.0/24}',
}
// This only skips remaining custom rules, not managed rules

// CORRECT: Skip specific phases
{
  action: 'skip',
  action_parameters: {
    phases: ['http_request_firewall_managed', 'http_ratelimit'],
  },
  expression: 'ip.src in {192.0.2.0/24}',
}
```

