## Key Points

- **64 binding limit** (all types combined)
- **Secrets**: Always use `wrangler secret put`, never commit
- **Types**: Run `npx wrangler types` after config changes
- **Environments**: Use `env` field for staging/production variants
- **Development**: Use `preview_id` or `--remote` flag
- **IDs vs Names**: Some bindings use `id` (KV, D1), others use `name` (R2, Queues)

