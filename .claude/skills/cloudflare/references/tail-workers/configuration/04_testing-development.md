## Testing & Development

### Local Testing

**Tail Workers cannot be fully tested with `wrangler dev`.** Deploy to staging environment for testing.

### Testing Strategy

1. Deploy producer Worker to staging
2. Deploy Tail Worker to staging
3. Configure `tail_consumers` in producer
4. Trigger producer Worker requests
5. Verify Tail Worker receives events (check destination logs/storage)

### Wrangler Tail Command

```bash
# Stream logs to terminal (NOT Tail Workers)
wrangler tail my-producer-worker
```

**This is different from Tail Workers:**
- `wrangler tail` streams logs to your terminal
- Tail Workers are Workers that process events programmatically

