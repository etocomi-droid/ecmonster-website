## Key Datasets by Product

### Zone-Scoped (per-domain)

| Dataset | Description |
|---------|-------------|
| `httpRequestsAdaptiveGroups` | HTTP traffic: requests, bytes, cache status, bot scores, WAF scores |
| `httpRequests1hGroups` / `1dGroups` / `1mGroups` | Pre-aggregated HTTP rollups (hourly/daily/minutely) |
| `firewallEventsAdaptiveGroups` | WAF, rate limiting, bot management, firewall rule events |
| `dnsAnalyticsAdaptiveGroups` | DNS query volumes, response codes, query types |
| `loadBalancingRequestsAdaptiveGroups` | Load Balancer origin request metrics |
| `pageShieldReportsAdaptiveGroups` | Page Shield CSP reports |

### Account-Scoped (cross-domain)

| Dataset | Description |
|---------|-------------|
| `workersInvocationsAdaptive` | Workers: requests, errors, CPU time, wall time, subrequests |
| `durableObjectsInvocationsAdaptiveGroups` | DO invocations |
| `durableObjectsStorageGroups` / `durableObjectsPeriodicGroups` | DO storage and periodic metrics |
| `d1AnalyticsAdaptiveGroups` / `d1QueriesAdaptiveGroups` | D1 database analytics |
| `r2OperationsAdaptiveGroups` / `r2StorageAdaptiveGroups` | R2 operations and storage |
| `kvOperationsAdaptiveGroups` / `kvStorageAdaptiveGroups` | KV operations and storage |
| `aiInferenceAdaptiveGroups` | Workers AI inference metrics |
| `aiGatewayRequestsAdaptiveGroups` | AI Gateway request analytics |
| `pagesFunctionsInvocationsAdaptiveGroups` | Pages Functions metrics |
| `magicTransitNetworkAnalyticsAdaptiveGroups` | Magic Transit packet/byte analytics |
| `spectrumNetworkAnalyticsAdaptiveGroups` | Spectrum TCP/UDP analytics |
| `gatewayL7RequestsAdaptiveGroups` | Zero Trust Gateway HTTP metrics |
| `gatewayResolverQueriesAdaptiveGroups` | Zero Trust Gateway DNS metrics |

