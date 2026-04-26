## Monitoring and Analytics

### Dashboard Analytics

Navigate to **Caching > Cache Reserve** to view:

- **Egress Savings**: Total bytes served from Cache Reserve vs origin egress cost saved
- **Requests Served**: Cache Reserve hits vs misses breakdown
- **Storage Used**: Current GB stored in Cache Reserve (billed monthly)
- **Operations**: Class A (writes) and Class B (reads) operation counts
- **Cost Tracking**: Estimated monthly costs based on current usage

### Logpush Integration

```typescript
// Logpush field: CacheReserveUsed (boolean) - filter for Cache Reserve hits
// Query Cache Reserve hits in analytics
const logpushQuery = `
  SELECT 
    ClientRequestHost, 
    COUNT(*) as requests, 
    SUM(EdgeResponseBytes) as bytes_served,
    COUNT(CASE WHEN CacheReserveUsed = true THEN 1 END) as cache_reserve_hits,
    COUNT(CASE WHEN CacheReserveUsed = false THEN 1 END) as cache_reserve_misses
  FROM http_requests 
  WHERE Timestamp >= NOW() - INTERVAL '24 hours'
  GROUP BY ClientRequestHost 
  ORDER BY requests DESC
`;

// Filter only Cache Reserve hits
const crHitsQuery = `
  SELECT ClientRequestHost, COUNT(*) as requests, SUM(EdgeResponseBytes) as bytes
  FROM http_requests 
  WHERE CacheReserveUsed = true AND Timestamp >= NOW() - INTERVAL '7 days'
  GROUP BY ClientRequestHost 
  ORDER BY bytes DESC
`;
```

### GraphQL Analytics

```graphql
query CacheReserveAnalytics($zoneTag: string, $since: string, $until: string) {
  viewer {
    zones(filter: { zoneTag: $zoneTag }) {
      httpRequests1dGroups(
        filter: { datetime_geq: $since, datetime_leq: $until }
        limit: 1000
      ) {
        dimensions { date }
        sum {
          cachedBytes
          cachedRequests
          bytes
          requests
        }
      }
    }
  }
}
```

