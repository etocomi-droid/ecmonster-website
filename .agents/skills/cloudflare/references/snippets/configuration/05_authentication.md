## Authentication

### API Token (Recommended)
```bash
# Create token at: https://dash.cloudflare.com/profile/api-tokens
# Required permissions: Zone.Snippets:Edit, Zone.Rules:Edit
export CLOUDFLARE_API_TOKEN="your_token_here"
```

### API Key (Legacy)
```bash
export CLOUDFLARE_EMAIL="your@email.com"
export CLOUDFLARE_API_KEY="your_global_api_key"
``` 