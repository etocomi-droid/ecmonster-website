### GraphQL Analytics API

**Endpoint**: `https://api.cloudflare.com/client/v4/graphql`

**Query Workers Metrics**:
```graphql
query {
  viewer {
    accounts(filter: { accountTag: $accountId }) {
      workersInvocationsAdaptive(
        limit: 100
        filter: {
          datetime_geq: "2025-01-01T00:00:00Z"
          datetime_leq: "2025-01-31T23:59:59Z"
          scriptName: "my-worker"
        }
      ) {
        sum {
          requests
          errors
          subrequests
        }
        quantiles {
          cpuTimeP50
          cpuTimeP99
          wallTimeP50
          wallTimeP99
        }
      }
    }
  }
}
```

