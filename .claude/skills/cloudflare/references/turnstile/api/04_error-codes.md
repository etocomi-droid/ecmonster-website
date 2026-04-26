## Error Codes

| Code | Cause | Solution |
|------|-------|----------|
| `missing-input-secret` | Secret key not provided | Include `secret` in request |
| `invalid-input-secret` | Secret key is wrong | Check secret key in dashboard |
| `missing-input-response` | Token not provided | Include `response` token |
| `invalid-input-response` | Token is invalid/malformed | Verify token from widget |
| `timeout-or-duplicate` | Token expired (>5min) or reused | Generate new token, validate once |
| `internal-error` | Cloudflare server error | Retry with exponential backoff |
| `bad-request` | Malformed request | Check JSON/form encoding |

