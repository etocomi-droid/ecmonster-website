## Usage Analytics (GraphQL)

```graphql
query ArgoAnalytics($zoneTag: string!) {
  viewer {
    zones(filter: { zoneTag: $zoneTag }) {
      httpRequestsAdaptiveGroups(limit: 1000) {
        sum { argoBytes, bytes }
      }
    }
  }
}
```

**Billing:** ~$0.10/GB. DDoS-mitigated and WAF-blocked traffic NOT charged.

