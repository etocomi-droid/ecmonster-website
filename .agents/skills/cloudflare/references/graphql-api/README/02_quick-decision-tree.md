## Quick Decision Tree

```
Need analytics data from Cloudflare?
├─ HTTP traffic (requests, bandwidth, cache) → httpRequestsAdaptiveGroups (zone or account)
├─ Workers performance (CPU, wall time, errors) → workersInvocationsAdaptive (account)
├─ Firewall/WAF events → firewallEventsAdaptive / firewallEventsAdaptiveGroups (zone or account)
├─ DNS query analytics → dnsAnalyticsAdaptive / dnsAnalyticsAdaptiveGroups (zone or account)
├─ Network layer (DDoS, Magic Transit) → *NetworkAnalyticsAdaptiveGroups (account)
├─ Storage (R2, KV, D1, DO) → r2OperationsAdaptiveGroups / kvOperationsAdaptiveGroups / etc. (account)
├─ AI (Workers AI, AI Gateway) → aiInferenceAdaptive / aiGatewayRequestsAdaptiveGroups (account)
├─ Load Balancing → loadBalancingRequestsAdaptiveGroups (zone)
├─ Custom high-cardinality metrics → Workers Analytics Engine (see ../analytics-engine/)
└─ Need raw logs, not aggregates → Logpush (see Cloudflare docs)
```

