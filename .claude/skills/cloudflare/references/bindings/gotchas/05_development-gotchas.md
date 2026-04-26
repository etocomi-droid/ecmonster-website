## Development Gotchas

**wrangler dev vs deploy:**
- dev: Uses `preview_id` or local bindings, secrets not available
- deploy: Uses production `id`, secrets available

**Access secrets in dev:** `npx wrangler dev --remote`  
**Persist local data:** `npx wrangler dev --persist`

