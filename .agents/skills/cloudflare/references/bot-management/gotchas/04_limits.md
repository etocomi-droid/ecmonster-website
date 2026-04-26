## Limits

| Limit | Value | Notes |
|-------|-------|-------|
| Bot Score = 0 | Means not computed | Not score = 100 |
| First request JSD data | May not be available | JSD data appears on subsequent requests |
| Score accuracy | Not 100% guaranteed | False positives/negatives possible |
| JSD on first HTML page visit | Not supported | Requires subsequent page load |
| JSD requirements | JavaScript-enabled browser | Won't work with JS disabled or ad blockers |
| JSD ETag stripping | Strips ETags from HTML responses | May affect caching behavior |
| JSD CSP compatibility | Requires specific CSP | Not compatible with some CSP configurations |
| JSD meta CSP tags | Not supported | Must use HTTP headers |
| JSD WebSocket support | Not supported | WebSocket endpoints won't work with JSD |
| JSD mobile app support | Native apps won't pass | Only works in browsers |
| JA3/JA4 traffic type | HTTPS/TLS only | Not available for non-HTTPS traffic |
| JA3/JA4 Worker routing | Missing for Worker-routed traffic | Check request routing |
| JA3/JA4 uniqueness | Not unique per user | Shared by clients with same browser/library |
| JA3/JA4 stability | Can change with updates | Browser/library updates affect fingerprints |
| WAF custom rules (Free) | 5 | Varies by plan |
| WAF custom rules (Pro) | 20 | Varies by plan |
| WAF custom rules (Business) | 100 | Varies by plan |
| WAF custom rules (Enterprise) | 1,000+ | Varies by plan |
| Workers CPU time | Varies by plan | Applies to bot logic |
| Bot Analytics sampling | 1-10% adaptive | High-volume zones sampled more aggressively |
| Bot Analytics history | 30 days max | Historical data retention limit |
| CSP requirements for JSD | Must allow `/cdn-cgi/challenge-platform/` | Required for JSD to function |

### Plan Restrictions

| Feature | Free | Pro/Business | Enterprise |
|---------|------|--------------|------------|
| Granular scores (1-99) | No | No | Yes |
| JA3/JA4 | No | No | Yes |
| Anomaly Detection | No | No | Yes |
| Corporate Proxy detection | No | No | Yes |
| Verified bot categories | Limited | Limited | Full |
| Custom WAF rules | 5 | 20/100 | 1,000+ |
