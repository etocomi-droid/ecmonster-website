### Environment-Specific Configuration

**Development** (verbose logs, full sampling):
```jsonc
// wrangler.dev.jsonc
{
  "observability": {
    "enabled": true,
    "head_sampling_rate": 1.0,
    "traces": {
      "enabled": true
    }
  }
}
```

**Production** (reduced sampling, structured logs):
```jsonc
// wrangler.prod.jsonc
{
  "observability": {
    "enabled": true,
    "head_sampling_rate": 0.1, // 10% sampling
    "traces": {
      "enabled": true
    }
  }
}
```

Deploy with env-specific config:
```bash
wrangler deploy --config wrangler.prod.jsonc --env production
```