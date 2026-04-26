## Limits

| Limit | Value | Notes |
|-------|-------|-------|
| Minimum TTL | 10 hours (36000 seconds) | Assets with shorter TTL not eligible |
| Default retention | 30 days (2592000 seconds) | Configurable |
| Maximum file size | Same as R2 limits | No practical limit |
| Purge/clear time | Up to 24 hours | Complete propagation time |
| Plan requirement | Paid Cache Reserve or Smart Shield | Not available on free plans |
| Content-Length header | Required | Must be present for eligibility |
| Set-Cookie header | Blocks caching | Must not be present (or use private directive) |
| Vary header | Cannot be * | Can use Vary: Accept-Encoding |
| Image transformations | Variants not eligible | Original images only |
| Range requests | NOT supported | HTTP 206 bypasses Cache Reserve |
| Compression | Fetches uncompressed | Serves compressed to visitors |
| Worker control | Zone-level only | Cannot control per-request |
| O2O requests | Bypassed | Orange-to-Orange not eligible |

