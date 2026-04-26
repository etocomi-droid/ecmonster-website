## Wrangler Integration

```toml
[ai]
binding = "AI"

[[ai.gateway]]
id = "my-gateway"
```

```bash
wrangler secret put CF_API_TOKEN
wrangler secret put OPENAI_API_KEY  # If not using BYOK
```

