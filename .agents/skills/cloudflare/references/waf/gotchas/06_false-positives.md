## False Positives

**Problem:** Legitimate traffic blocked
**Cause:** Aggressive rules/thresholds
**Solution:**

1. Start with log mode: `overrides: { action: 'log' }`
2. Review Security Events to identify false positives
3. Override specific rules: `overrides: { rules: [{ id: 'rule_id', action: 'log' }] }`

