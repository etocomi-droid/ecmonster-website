## SDK Configuration

### TypeScript

```typescript
const client = new Cloudflare({
  apiToken: process.env.CLOUDFLARE_API_TOKEN,
  timeout: 120000,        // 2 min (default 60s), in milliseconds
  maxRetries: 5,          // default 2
  baseURL: 'https://...', // proxy (rare)
});

// Per-request overrides
await client.zones.get(
  { zone_id: 'zone-id' },
  { timeout: 5000, maxRetries: 0 }
);
```

### Python

```python
client = Cloudflare(
    api_token=os.environ["CLOUDFLARE_API_TOKEN"],
    timeout=120,         # seconds (default 60)
    max_retries=5,       # default 2
    base_url="https://...",  # proxy (rare)
)

# Per-request overrides
client.with_options(timeout=5, max_retries=0).zones.get(zone_id="zone-id")
```

### Go

```go
client := cloudflare.NewClient(
    option.WithAPIToken(os.Getenv("CLOUDFLARE_API_TOKEN")),
    option.WithMaxRetries(5),  // default 10 (higher than TS/Python)
    option.WithRequestTimeout(2 * time.Minute),  // default 60s
    option.WithBaseURL("https://..."),  // proxy (rare)
)

// Per-request overrides
client.Zones.Get(ctx, "zone-id", option.WithMaxRetries(0))
```

