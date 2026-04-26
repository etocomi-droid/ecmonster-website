## Environment Variables

### Local (.dev.vars)
```bash
# .dev.vars (never commit)
SECRET_KEY="local-secret-key"
API_TOKEN="dev-token-123"
```

### Production
```bash
echo "secret-value" | npx wrangler pages secret put SECRET_KEY --project-name=my-project
npx wrangler pages secret list --project-name=my-project
npx wrangler pages secret delete SECRET_KEY --project-name=my-project
```

Access: `env.SECRET_KEY`

