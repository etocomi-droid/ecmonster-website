## Skip Rules

Skip rules bypass subsequent rule evaluation. Two skip types:

**Skip current ruleset**: Skip remaining rules in current phase only
```typescript
{
  action: 'skip',
  action_parameters: {
    ruleset: 'current', // Skip rest of current ruleset
  },
  expression: 'http.request.uri.path ends_with ".jpg" or http.request.uri.path ends_with ".css"',
  enabled: true,
}
```

**Skip entire phases**: Skip one or more phases completely
```typescript
{
  action: 'skip',
  action_parameters: {
    phases: ['http_request_firewall_managed', 'http_ratelimit'], // Skip multiple phases
  },
  expression: 'ip.src in {192.0.2.0/24 203.0.113.0/24}',
  enabled: true,
}
```

**Note**: Skip rules in custom phase can skip managed/ratelimit phases, but not vice versa (execution order).