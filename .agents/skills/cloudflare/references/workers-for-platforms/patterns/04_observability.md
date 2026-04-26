## Observability

### Logpush
- Enable on dispatch Worker → captures all user Worker logs
- Filter by `Outcome` or `Script Name`

### Tail Workers
- Real-time logs with custom formatting
- Receives HTTP status, `console.log()`, exceptions, diagnostics

### Analytics Engine
```typescript
// Track violations
env.ANALYTICS.writeDataPoint({
  indexes: [customerName],
  blobs: ["cpu_limit_exceeded"],
});
```

### GraphQL
```graphql
query {
  viewer {
    accounts(filter: {accountTag: $accountId}) {
      workersInvocationsAdaptive(filter: {dispatchNamespaceName: "production"}) {
        sum { requests errors cpuTime }
      }
    }
  }
}
```

