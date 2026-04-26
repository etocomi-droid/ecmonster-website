## Dimensions

Dimensions are fields you can group by via the `dimensions` sub-selection.

### Time Dimensions

| Dimension | Granularity |
|-----------|------------|
| `date` | Day |
| `datetime` | Exact timestamp |
| `datetimeMinute` | 1 minute |
| `datetimeFiveMinutes` | 5 minutes |
| `datetimeFifteenMinutes` | 15 minutes |
| `datetimeHour` | 1 hour |

Workers datasets also support `datetimeSixHours`.

### HTTP Request Dimensions (httpRequestsAdaptiveGroups)

83 dimensions available. Key ones:

| Dimension | Description |
|-----------|-------------|
| `clientCountryName` | Country of origin |
| `clientRequestHTTPHost` | Requested hostname |
| `clientRequestHTTPMethodName` | HTTP method |
| `clientRequestPath` | URI path |
| `edgeResponseStatus` | Edge HTTP status code |
| `cacheStatus` | Cache status (hit, miss, dynamic, etc.) |
| `coloCode` | Cloudflare datacenter IATA code |
| `clientIP` / `clientAsn` | Client IP address / ASN |
| `botScore` / `botManagementDecision` | Bot management score (0-99) / verdict |
| `wafAttackScore` / `securityAction` | WAF score / firewall action taken |
| `ja3Hash` / `ja4` | TLS fingerprints |
| `sampleInterval` | ABR sample interval |

### Workers Dimensions (workersInvocationsAdaptive)

`scriptName`, `scriptTag`, `scriptVersion`, `environmentName`, `status`, `usageModel`, `coloCode`, `dispatchNamespaceName`, `isDispatcher`

### Firewall Dimensions (firewallEventsAdaptive)

`action`, `source`, `ruleId`, `clientCountryName`, `clientIP`, `clientAsn`, `userAgent`

