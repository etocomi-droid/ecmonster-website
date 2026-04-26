## Development

### "AI inference doesn't work locally"
```bash
# ❌ Local AI doesn't work
wrangler dev
# ✅ Use remote
wrangler dev --remote
```

### "env.AI is undefined"
Add binding to wrangler.jsonc:
```jsonc
{ "ai": { "binding": "AI" } }
```

