## Deploying from Playground

Click **Deploy** button to move code to production:

1. **Log in** to Cloudflare account (creates free account if needed)
2. **Review** Worker name and code
3. **Deploy** to global network (takes ~30 seconds)
4. **Get URL**: Deployed to `<name>.workers.dev` subdomain
5. **Manage** from dashboard: add bindings, custom domains, analytics

**After deploy:**
- Code runs on Cloudflare's global network (300+ cities)
- Can add KV, D1, R2, Durable Objects bindings
- Configure custom domains and routes
- View analytics and logs
- Set environment variables and secrets

**Note:** Deployed Workers are production-ready but start on Free plan (100k requests/day).

