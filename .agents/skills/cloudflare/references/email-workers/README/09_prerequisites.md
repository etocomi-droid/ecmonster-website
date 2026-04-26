## Prerequisites

Before deploying Email Workers:

1. **Enable Email Routing** in Cloudflare dashboard for your domain
2. **Verify destination addresses** for forwarding
3. **Configure DMARC/SPF** for sending domains (required for replies)
4. **Set up wrangler.jsonc** with SendEmail binding

See [configuration.md](./configuration.md) for detailed setup.

