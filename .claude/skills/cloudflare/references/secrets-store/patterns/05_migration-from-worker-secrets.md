## Migration from Worker Secrets

Change `env.SECRET` (direct) to `await env.SECRET.get()` (async).

Steps:
1. Create in Secrets Store: `wrangler secrets-store secret create <store-id> --name API_KEY --scopes workers --remote`
2. Add binding to `wrangler.jsonc`: `{"binding": "API_KEY", "store_id": "abc123", "secret_name": "api_key"}`
3. Update code: `const key = await env.API_KEY.get();`
4. Test staging, deploy
5. Remove old: `wrangler secret delete API_KEY`

