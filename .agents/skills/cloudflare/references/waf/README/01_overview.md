## Overview

Cloudflare WAF protects web applications from attacks through managed rulesets and custom rules.

**Detection (Managed Rulesets)**
- Pre-configured rules maintained by Cloudflare
- CVE-based rules, OWASP Top 10 coverage
- Three main rulesets: Cloudflare Managed, OWASP CRS, Exposed Credentials
- Actions: log, block, challenge, js_challenge, managed_challenge

**Mitigation (Custom Rules & Rate Limiting)**
- Custom expressions using Wirefilter syntax
- Attack score-based blocking (`cf.waf.score`)
- Rate limiting with per-IP, per-user, or custom characteristics
- Actions: block, challenge, js_challenge, managed_challenge, log, skip

