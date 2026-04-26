## Security Checklist

- [ ] Credentials generated server-side only (never client-side)
- [ ] TURN_KEY_SECRET in wrangler secrets, not vars
- [ ] TTL ≤ expected session duration (and ≤ 48 hours)
- [ ] Rate limiting on credential generation endpoint
- [ ] Client authentication before issuing credentials
- [ ] Credential revocation API for compromised sessions
- [ ] No hardcoded IPs (or DNS monitoring in place)
- [ ] Port 53 filtered for browser clients

