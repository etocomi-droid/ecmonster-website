## Overview

- **Single endpoint** for all analytics: `https://api.cloudflare.com/client/v4/graphql`
- **1,400+ schema types** spanning every Cloudflare product
- **Two scopes**: zone-level (per-domain) and account-level (cross-domain)
- **Adaptive sampling** on high-traffic datasets with confidence intervals
- **No mutations** - read-only analytics (the Mutation type is a stub)
- **Cost-based rate limiting** - default 300 queries per 5 minutes per user (max 320, varies by query cost)

