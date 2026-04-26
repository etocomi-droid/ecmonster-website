## AI & Gateway Analytics

```graphql
# Workers AI inference
aiInferenceAdaptiveGroups(
  filter: { datetime_gt: $start, datetime_lt: $end }, limit: 100, orderBy: [datetimeHour_DESC]
) {
  count
  sum { totalInputTokens totalOutputTokens totalRequestBytesIn }
  dimensions { modelId datetimeHour }
}

# AI Gateway requests
aiGatewayRequestsAdaptiveGroups(
  filter: { datetime_gt: $start, datetime_lt: $end }, limit: 100, orderBy: [datetimeHour_DESC]
) {
  count
  dimensions { gateway provider model datetimeHour }
  sum { cachedTokensIn cachedTokensOut uncachedTokensIn uncachedTokensOut }
}
```

Both are account-scoped — nest under `accounts(filter: { accountTag: $accountTag })`.

