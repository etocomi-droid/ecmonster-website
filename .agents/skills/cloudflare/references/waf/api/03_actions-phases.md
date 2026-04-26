## Actions & Phases

### Actions by Phase

| Action | Custom | Managed | Rate Limit | Description |
|--------|--------|---------|------------|-------------|
| `block` | ✅ | ❌ | ✅ | Block request with 403 |
| `challenge` | ✅ | ❌ | ✅ | Show CAPTCHA challenge |
| `js_challenge` | ✅ | ❌ | ✅ | JS-based challenge |
| `managed_challenge` | ✅ | ❌ | ✅ | Smart challenge (recommended) |
| `log` | ✅ | ❌ | ✅ | Log only, don't block |
| `skip` | ✅ | ❌ | ❌ | Skip rule evaluation |
| `execute` | ❌ | ✅ | ❌ | Deploy managed ruleset |

### Phases (Execution Order)

1. `http_request_firewall_custom` - Custom rules (first line of defense)
2. `http_request_firewall_managed` - Managed rulesets (pre-configured protection)
3. `http_ratelimit` - Rate limiting (request throttling)
4. `http_request_sbfm` - Super Bot Fight Mode (Pro+ only)

