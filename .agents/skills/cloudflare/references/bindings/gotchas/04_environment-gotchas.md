## Environment Gotchas

### Wrong Environment Deployed

**Solution:** Check `npx wrangler deployments list`, use `--env` flag

### Secrets Not Per-Environment

**Solution:** Set per environment: `npx wrangler secret put API_KEY --env staging`

