## Endpoints

### HTTP DDoS (L7)

```typescript
// Zone-level
PUT /zones/{zoneId}/rulesets/phases/ddos_l7/entrypoint
GET /zones/{zoneId}/rulesets/phases/ddos_l7/entrypoint

// Account-level (Enterprise Advanced)
PUT /accounts/{accountId}/rulesets/phases/ddos_l7/entrypoint
GET /accounts/{accountId}/rulesets/phases/ddos_l7/entrypoint
```

### Network DDoS (L3/4)

```typescript
// Account-level only
PUT /accounts/{accountId}/rulesets/phases/ddos_l4/entrypoint
GET /accounts/{accountId}/rulesets/phases/ddos_l4/entrypoint
```

