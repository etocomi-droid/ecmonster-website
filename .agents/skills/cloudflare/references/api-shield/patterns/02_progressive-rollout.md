## Progressive Rollout

```
1. Log mode: Observe false positives
   - Schema: Action = Log
   - JWT: Action = Log

2. Block subset: Protect critical endpoints
   - Change specific endpoint actions to Block
   - Monitor firewall events

3. Full enforcement: Block all violations
   - Change default action to Block
   - Handle fallthrough with custom rule
```

