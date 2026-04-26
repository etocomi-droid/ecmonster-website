## Logpush Fields

```txt
BotScore              # 1-99 or 0 if not computed
BotScoreSrc           # Detection engine (ML, Heuristics, etc.)
BotTags               # Classification tags
BotDetectionIDs       # Heuristic detection IDs
```

**BotScoreSrc values:**
- `"Heuristics"` - Known fingerprint
- `"Machine Learning"` - ML model
- `"Anomaly Detection"` - Baseline anomaly
- `"JS Detection"` - JavaScript check
- `"Cloudflare Service"` - Zero Trust
- `"Not Computed"` - Score = 0

Access via Logpush (stream to cloud storage/SIEM), Logpull (API to fetch logs), or GraphQL API (query analytics data).

