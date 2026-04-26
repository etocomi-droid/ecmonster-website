## Firewall / Security

```graphql
query RecentFirewallEvents($zoneTag: string!, $start: Time!) {
  viewer {
    zones(filter: { zoneTag: $zoneTag }) {
      firewallEventsAdaptive(
        filter: { datetime_gt: $start }
        limit: 50
        orderBy: [datetime_DESC]
      ) {
        action source clientIP clientCountryName userAgent
        clientRequestHTTPHost clientRequestPath ruleId datetime
      }
    }
  }
}
```

For aggregated firewall stats, use `firewallEventsAdaptiveGroups` with `action: "block"` filter and group by `ruleId`, `source`, `datetimeHour`.

