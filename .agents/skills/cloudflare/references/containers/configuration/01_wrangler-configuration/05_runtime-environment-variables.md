### Runtime Environment Variables

Cloudflare automatically provides these environment variables to containers:

| Variable | Description |
|----------|-------------|
| `CLOUDFLARE_APPLICATION_ID` | Worker application ID |
| `CLOUDFLARE_COUNTRY_A2` | Two-letter country code of request origin |
| `CLOUDFLARE_LOCATION` | Cloudflare data center location |
| `CLOUDFLARE_REGION` | Region identifier |
| `CLOUDFLARE_DURABLE_OBJECT_ID` | Container's Durable Object ID |

Custom `envVars` from Container class are merged with these. Custom vars override runtime vars if names conflict.

