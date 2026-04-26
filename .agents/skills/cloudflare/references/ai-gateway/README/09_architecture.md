## Architecture

AI Gateway acts as a proxy between your application and AI providers:

```
Your App → AI Gateway → AI Provider (OpenAI, Anthropic, etc.)
         ↓
    Analytics, Caching, Rate Limiting, Logging
```

**Key URL patterns:**
- Unified API (OpenAI-compatible): `https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/compat/chat/completions`
- Provider-specific: `https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/{provider}/{endpoint}`
- Dynamic routes: Use route name instead of model: `dynamic/{route-name}`

