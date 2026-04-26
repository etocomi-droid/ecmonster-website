## Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| **Widget not rendering** | Incorrect sitekey, CSP blocking, file:// protocol | Check sitekey, add CSP for challenges.cloudflare.com, use http:// |
| **timeout-or-duplicate** | Token expired (>5min) or reused | Generate fresh token, don't cache >5min |
| **invalid-input-secret** | Wrong secret key | Verify secret from dashboard, check env vars |
| **missing-input-response** | Token not sent | Check form field name is 'cf-turnstile-response' |

